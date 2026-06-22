import { NextRequest, NextResponse } from "next/server";
import { checkPassword, makeSession, SESSION_COOKIE } from "@/lib/auth";

export async function POST(req: NextRequest) {
  const form = await req.formData();
  const password = String(form.get("password") || "");
  const origin = new URL(req.url).origin;

  if (!checkPassword(password)) {
    return NextResponse.redirect(`${origin}/login?error=1`, { status: 303 });
  }

  const { value, maxAge } = await makeSession();
  const res = NextResponse.redirect(`${origin}/`, { status: 303 });
  res.cookies.set(SESSION_COOKIE, value, {
    httpOnly: true,
    secure: true,
    sameSite: "lax",
    path: "/",
    maxAge,
  });
  return res;
}
