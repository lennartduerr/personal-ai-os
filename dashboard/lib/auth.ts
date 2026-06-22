// Minimal password gate: a signed (HMAC) session cookie. No DB, no dependencies.
// Uses Web Crypto, so it runs on any runtime. Set AUTH_SECRET + DASHBOARD_PASSWORD in env.
import { cookies } from "next/headers";

const COOKIE = "pais_session";
const MAX_AGE = 60 * 60 * 24 * 7; // 7 days

function enc(s: string) {
  return new TextEncoder().encode(s);
}

async function hmac(value: string): Promise<string> {
  const secret = process.env.AUTH_SECRET || "";
  const key = await crypto.subtle.importKey(
    "raw",
    enc(secret),
    { name: "HMAC", hash: "SHA-256" },
    false,
    ["sign"],
  );
  const sig = await crypto.subtle.sign("HMAC", key, enc(value));
  return Buffer.from(new Uint8Array(sig)).toString("hex");
}

function constantTimeEqual(a: string, b: string): boolean {
  if (a.length !== b.length) return false;
  let out = 0;
  for (let i = 0; i < a.length; i++) out |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return out === 0;
}

/** Validate a submitted password against DASHBOARD_PASSWORD (constant time). */
export function checkPassword(submitted: string): boolean {
  const expected = process.env.DASHBOARD_PASSWORD || "";
  if (!expected) return false;
  return constantTimeEqual(submitted, expected);
}

/** Create the signed session cookie value: "<exp>.<hmac(exp)>". */
export async function makeSession(): Promise<{ value: string; maxAge: number }> {
  const exp = String(Math.floor(Date.now() / 1000) + MAX_AGE);
  const sig = await hmac(exp);
  return { value: `${exp}.${sig}`, maxAge: MAX_AGE };
}

/** True if the request carries a valid, unexpired session cookie. */
export async function isAuthed(): Promise<boolean> {
  const jar = await cookies();
  const raw = jar.get(COOKIE)?.value;
  if (!raw) return false;
  const [exp, sig] = raw.split(".");
  if (!exp || !sig) return false;
  if (Number(exp) < Math.floor(Date.now() / 1000)) return false;
  const expected = await hmac(exp);
  return constantTimeEqual(sig, expected);
}

export const SESSION_COOKIE = COOKIE;
