from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Crowd Calm API")

# -----------------------------
# Fake Database
# -----------------------------
users = {}     # email → password
reports = []   # crowd reports

# -----------------------------
# Models
# -----------------------------
class RegisterRequest(BaseModel):
    email: str
    password: str

class LoginRequest(BaseModel):
    email: str
    password: str

# -----------------------------
# Register API
# -----------------------------
@app.post("/register")
def register_user(request: RegisterRequest):
    if request.email in users:
        return {"success": False, "message": "User already exists"}

    users[request.email] = request.password
    return {"success": True, "message": "Registered successfully"}

# -----------------------------
# Login API
# -----------------------------
@app.post("/login")
def login_user(request: LoginRequest):
    if request.email not in users:
        return {"success": False, "message": "User not found"}

    if users[request.email] != request.password:
        return {"success": False, "message": "Incorrect password"}

    return {"success": True, "message": "Login successful"}

# -----------------------------
# Home
# -----------------------------
@app.get("/")
def home():
    return {"message": "Backend running"}