# RAG & Vector-Store Security (LLM08)

## Threats
- **RAG poisoning:** attacker-controlled documents enter the corpus and steer answers or carry indirect prompt injection.
- **Cross-tenant leakage:** retrieval returns another user's/tenant's documents.
- **Unauthorized retrieval:** documents a user shouldn't see are fetched into context.
- **Embedding inversion / membership inference:** sensitive info recovered from embeddings.

## Test (authorized)
- [ ] Insert a benign poisoned doc with a canary instruction; confirm the model does **not** obey it.
- [ ] As user A, attempt to retrieve user B / tenant B content.
- [ ] Query for documents outside your authorization; confirm access control blocks retrieval, not just display.
- [ ] Check whether retrieved content can trigger tool calls (indirect injection via RAG).

## Fix
- **Per-user/tenant access control at retrieval time**, enforced in the vector store query, not post-filtered in the prompt.
- **Ingestion validation & provenance:** vet sources, isolate user-contributed content, scan for embedded instructions.
- **Treat retrieved text as untrusted data** — never as instructions; keep it clearly delimited from system instructions.
- **Monitoring:** log retrievals; alert on anomalous access patterns and corpus changes.
- **Corpus isolation:** separate indexes per trust domain/tenant.
