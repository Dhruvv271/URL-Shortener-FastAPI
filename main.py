from datetime import datetime
import json
from fastapi import FastAPI, HTTPException
from sqlmodel import SQLModel, Field, Session, create_engine, select
from pydantic import BaseModel
from fastapi.responses import RedirectResponse
import string, random
from fastapi.middleware.cors import CORSMiddleware
DATABASE_URL = "sqlite:///data/urls.db"



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ------------------ Models ------------------

class URL(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    original_url: str
    short_code: str
    clicks: int = 0
    click_history: str = "[]"

DATABASE_URL = "sqlite:///urls.db"
engine = create_engine(DATABASE_URL, echo=True)

def create_db():
    SQLModel.metadata.create_all(engine)

create_db()

# ------------------ Helpers ------------------

def generate_code(length=6):
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))

class URLCreate(BaseModel):
    url: str

# ------------------ Routes ------------------

@app.post("/shorten")
def shorten(data: URLCreate):
    code = generate_code()

    with Session(engine) as session:
        record = URL(original_url=data.url, short_code=code)
        session.add(record)
        session.commit()
        session.refresh(record)

    return {"short_url": f"http://localhost:8000/{code}"}

@app.get("/{code}")
def redirect(code: str):
    with Session(engine) as session:
        statement = select(URL).where(URL.short_code == code)
        record = session.exec(statement).first()

        if not record:
            raise HTTPException(status_code=404, detail="Link not found")

        # Record analytics
        record.clicks += 1

        history = json.loads(record.click_history)
        history.append(datetime.utcnow().isoformat())
        record.click_history = json.dumps(history)

        session.add(record)
        session.commit()

        return RedirectResponse(record.original_url)

@app.get("/analytics/{code}")
def get_analytics(code: str):
    with Session(engine) as session:
        statement = select(URL).where(URL.short_code == code)
        record = session.exec(statement).first()

        if not record:
            raise HTTPException(status_code=404, detail="Link not found")

        return {
            "short_code": record.short_code,
            "original_url": record.original_url,
            "clicks": record.clicks,
            "history": json.loads(record.click_history)
 
        }
@app.get("/")
def home():
    return {
        "message": "URL Shortener is running 🚀",
        "docs": "/docs",
        "shorten_endpoint": "/shorten"
    }