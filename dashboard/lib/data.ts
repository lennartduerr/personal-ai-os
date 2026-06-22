// Reads the latest briefing JSON that the VPS pushed to Vercel Blob.
// The ingest route writes it at a stable path; here we list + fetch it.
import { list } from "@vercel/blob";

export type BriefingItem = string | { text: string; sub?: string };

export interface Briefing {
  generatedAt?: string;
  calendar?: BriefingItem[];
  tasks?: BriefingItem[];
  mail?: BriefingItem[];
  cost?: { spent24h?: string; balance?: string } | null;
  brain?: { status?: string } | null;
  [key: string]: unknown;
}

export const BLOB_PATH = "briefing/latest.json";

export async function getBriefing(): Promise<Briefing | null> {
  const token = process.env.BLOB_READ_WRITE_TOKEN;
  if (!token) return null;
  try {
    const { blobs } = await list({ prefix: BLOB_PATH, token });
    if (!blobs.length) return null;
    const res = await fetch(blobs[0].url, { cache: "no-store" });
    if (!res.ok) return null;
    return (await res.json()) as Briefing;
  } catch {
    return null;
  }
}
