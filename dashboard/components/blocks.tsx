import type { Briefing, BriefingItem } from "@/lib/data";

function Item({ item }: { item: BriefingItem }) {
  if (typeof item === "string") return <li>{item}</li>;
  return (
    <li>
      {item.text}
      {item.sub ? <span className="muted"> — {item.sub}</span> : null}
    </li>
  );
}

function Card({ title, items }: { title: string; items?: BriefingItem[] }) {
  return (
    <section className="card">
      <h2>{title}</h2>
      {items && items.length ? (
        <ul>{items.map((it, i) => <Item key={i} item={it} />)}</ul>
      ) : (
        <p className="empty">nothing</p>
      )}
    </section>
  );
}

export function Blocks({ data }: { data: Briefing | null }) {
  if (!data) {
    return (
      <p className="empty">
        No briefing yet. Once the VPS pushes data to <code>/api/ingest</code>, it shows up here.
      </p>
    );
  }
  const cost: BriefingItem[] = [];
  if (data.cost?.spent24h) cost.push(`Spent (24h): ${data.cost.spent24h}`);
  if (data.cost?.balance) cost.push(`Balance: ${data.cost.balance}`);
  const brain: BriefingItem[] = [];
  if (data.brain?.status) brain.push(data.brain.status);

  return (
    <div className="grid">
      <Card title="📅 Calendar" items={data.calendar} />
      <Card title="✅ To-dos" items={data.tasks} />
      <Card title="📧 Mail" items={data.mail} />
      <Card title="💸 LLM spend" items={cost} />
      {brain.length ? <Card title="🧠 Second brain" items={brain} /> : null}
    </div>
  );
}
