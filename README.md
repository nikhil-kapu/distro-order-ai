# Distro Order AI

AI order entry for food distributors: turn messy emails and texts into clean ERP orders.

Inspired by the Asakana (YC F26) pattern — unsexy vertical, high willingness to pay, shippable in a week.

## What it does
- Ingests orders from email (Gmail) and SMS (Twilio)
- LLM parses items, quantities, SKUs, delivery dates into structured orders
- Human-in-the-loop review UI to confirm / correct before pushing
- Pushes clean orders to ERP (NetSuite / QuickBooks / CSV export for v1)

## 7-day build plan
- Day 1-2: Email + SMS ingest (Gmail API, Twilio webhook) -> raw order store
- Day 3-4: LLM parsing pipeline (Claude) with SKU fuzzy-match against product catalog CSV
- Day 5: Review UI (confirm/edit, one-click approve)
- Day 6: ERP push (start with CSV export + QuickBooks API)
- Day 7: Pilot with 1 distributor, 10 real orders

## Stack
- Backend: FastAPI + Postgres (or SQLite for v1)
- LLM: Claude for parsing, embeddings for SKU matching
- Ingest: Gmail API, Twilio
- Frontend: minimal React / HTMX review queue

## GTM
- Scrape 200 Bay Area food distributors
- Offer: "send me 10 messy orders, I'll digitize free"
- Pilot at $500/mo, scale to $1,500/mo per distributor
