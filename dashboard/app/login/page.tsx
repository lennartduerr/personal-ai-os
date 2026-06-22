export const dynamic = "force-dynamic";

export default async function Login({
  searchParams,
}: {
  searchParams: Promise<{ error?: string }>;
}) {
  const { error } = await searchParams;
  return (
    <main className="login">
      <h1>🛰️ personal-ai-os</h1>
      <p className="muted">Enter the dashboard password.</p>
      <form action="/api/login" method="post">
        <input type="password" name="password" placeholder="Password" autoFocus required />
        <button type="submit">Sign in</button>
      </form>
      {error ? <p className="muted" style={{ color: "#ff7a7a" }}>Wrong password.</p> : null}
    </main>
  );
}
