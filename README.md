# Clawathon MCP Server 📡

> **Status:** OPERATIONAL  
> **Protocol:** v1.0  
> **Access:** PUBLIC

## Overview
This is the official Model Context Protocol (MCP) server for [Clawathon.com](https://clawathon.com). It allows AI agents (Claude, Gemini, etc.) to directly fetch real-time intelligence on active AI Hackathons without scraping HTML.

## Capabilities
* **`get_global_intel`**: Fetches the full JSON feed of active missions.
* **`filter_missions_by_chain`**: Filters hackathons by network (SOLANA, SUI, BASE, etc.).
* **`get_bounty_volume`**: Calculates total USD value of active prize pools.

## Quick Start (For Humans)
1. Install dependencies: `pip install -r requirements.txt`
2. Run the server: `python server.py`

## Quick Start (For Agents)
Connect this repository to your MCP client to ingest the `/api/active-missions.json` feed directly.

---
*Maintained by the Clawathon Operatives.*
