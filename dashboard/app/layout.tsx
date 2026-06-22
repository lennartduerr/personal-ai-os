import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "personal-ai-os — dashboard",
  description: "Read-only daily briefing",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
