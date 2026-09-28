from fastapi import FastAPI

app = FastAPI(title="Distro Order AI")

@app.get("/health")
def health():
    return {"status": "ok"}

# TODO Day 1-2: Gmail + Twilio ingest -> POST /ingest/email, /ingest/sms
# TODO Day 3-4: LLM parsing pipeline -> POST /orders/parse
# TODO Day 5: review queue -> GET /orders/review
# TODO Day 6: ERP push -> POST /orders/{id}/push
