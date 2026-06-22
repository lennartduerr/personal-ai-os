import { NextRequest, NextResponse } from "next/server";
import { put } from "@vercel/blob";
import { revalidatePath } from "next/cache";
import { BLOB_PATH } from "@/lib/data";

// The VPS posts the briefing JSON here with: Authorization: Bearer <INGEST_SECRET>
export async function POST(req: NextRequest) {
  const auth = req.headers.get("authorization") || "";
  const expected = `Bearer ${process.env.INGEST_SECRET || ""}`;
  if (!process.env.INGEST_SECRET || auth.length !== expected.length || auth !== expected) {
    return NextResponse.json({ error: "unauthorized" }, { status: 401 });
  }

  let body: unknown;
  try {
    body = await req.json();
  } catch {
    return NextResponse.json({ error: "invalid json" }, { status: 400 });
  }

  await put(BLOB_PATH, JSON.stringify(body), {
    access: "public", // gated by password in the UI; see README for a fully-private option
    contentType: "application/json",
    allowOverwrite: true,
    token: process.env.BLOB_READ_WRITE_TOKEN,
  });

  revalidatePath("/");
  return NextResponse.json({ ok: true });
}
