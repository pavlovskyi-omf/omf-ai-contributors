## Meeting Title
AI Enablement: Cross-Functional Lighthouse PDLC Session — May 14, 2026

## Short Description
Introduction to MCP (Model Context Protocol) servers — what they are, why they matter, and how to configure and use them in AI coding tools. The session included a live demo of GitHub MCP and Atlassian MCP inside VS Code with GitHub Copilot.

## Key Points / Topics
- **MCP (Model Context Protocol)** introduced as an open standard for connecting AI models to external tools and data sources — described as "USB-C for AI"
- MCP servers act as bridges between AI agents and real-world systems (code repos, project management tools, design tools, browsers)
- **Approved MCP servers** for use within the organization:
  - GitHub MCP
  - Atlassian MCP
  - Figma MCP
  - Playwright MCP
  - Maple MCP
- **Local vs. remote MCP servers**: local servers run as a process on the developer's machine; remote servers are hosted and accessed via URL
- **Configuration**: MCP servers are added via a JSON configuration file in VS Code (`.vscode/mcp.json` or user settings); each entry specifies the server name, command, and arguments including authentication tokens
- **Live demo**: GitHub MCP and Atlassian MCP configured and used inside GitHub Copilot Chat in VS Code — querying Jira issues and GitHub PRs directly from the chat interface
- Discussion of security considerations: personal access tokens (PATs) are required and stored locally; approved server list limits exposure
- MCP is the foundational capability enabling agentic workflows that span multiple tools without copy-pasting context
