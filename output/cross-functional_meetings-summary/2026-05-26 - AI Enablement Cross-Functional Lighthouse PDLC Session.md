## Meeting Title
AI Enablement: Cross-Functional Lighthouse PDLC Session — May 26, 2026

## Short Description
Hands-on CodeMie agent setup session. Participants walked through connecting GitHub repositories as data sources, configuring a multi-repo agent with a system prompt, and understanding how RAG (Retrieval Augmented Generation) works under the hood to power cross-repo intelligence queries.

## Key Points / Topics
- **Step-by-step CodeMie setup**:
  1. Create a GitHub Personal Access Token (PAT) with repo read permissions
  2. Add each repository as a data source in CodeMie (name, PAT, repo URL)
  3. CodeMie indexes the repository content into a vector database
  4. Create an agent, attach data sources, and write a system prompt
- **RAG mechanics explained**:
  - Repository content is chunked and embedded into a vector store
  - On each query, the top-10 most semantically relevant chunks are retrieved
  - Retrieved chunks are injected into the LLM context alongside the user query
  - The model generates a response grounded in actual repo content rather than hallucinated guesses
- **Token cost awareness**: indexing a ~400 MB repository costs approximately $5 in embedding tokens (one-time cost); subsequent queries are cheaper
- **System prompt design**: participants practiced writing agent instructions — specifying the agent's role, what repos it knows about, how to answer cross-repo questions, and what to say when it doesn't know
- **Live Q&A demo**: agent queried across multiple repos to find API owners, locate business logic, and identify shared dependencies
- **Data source limits**: discussed maximum repo sizes, refresh frequency (periodic re-indexing), and handling of private vs. public repos
- **Security note**: PATs are stored encrypted in CodeMie; access is scoped to the repos explicitly added as data sources
