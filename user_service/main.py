from fastapi import FastAPI, HTTPException
from prometheus_client import Counter, generate_latest
from fastapi.responses import Response

app = FastAPI()

# Prometheus counter
REGISTRATION_COUNTER = Counter("user_registrations_total", "Total user registrations")

users_db = {}

@app.get("/")
def health_check():
    return {"message": "User Service is running"}

@app.post("/register")
def register_user(username: str):
    if username in users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    users_db[username] = {"username": username}
    REGISTRATION_COUNTER.inc()
    return {"message": f"User '{username}' registered successfully"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")
