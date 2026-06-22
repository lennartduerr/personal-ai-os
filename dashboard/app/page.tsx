import { redirect } from "next/navigation";
import { isAuthed } from "@/lib/auth";
import { getBriefing } from "@/lib/data";
import { Blocks } from "@/components/blocks";

export const dynamic = "force-dynamic";

export default async function Home() {
  if (!(await isAuthed())) redirect("/login");

  const data = await getBriefing();
  const generated = data?.generatedAt ? new Date(data.generatedAt).toLocaleString() : "—";

  return (
    <main className="container">
      <div className="header">
        <h1>🛰️ Daily briefing</h1>
        <span className="muted">updated {generated}</span>
      </div>
      <p className="muted">Read-only. Pushed from your VPS — no live LLM calls.</p>
      <Blocks data={data} />
    </main>
  );
}
