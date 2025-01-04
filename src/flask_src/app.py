from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import Column, Integer, String, Text, ForeignKey, create_engine, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
from pydantic import BaseModel
from typing import Optional, List
import os
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')

DATABASE_URL = f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}"
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define Models
class Survey(Base):
    __tablename__ = "survey"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(45), nullable=False)
    description = Column(Text, nullable=False)
    result = Column(Integer, ForeignKey("result.id", ondelete="SET NULL"), nullable=True)
    user = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    created = Column(DateTime, default=datetime.utcnow)

    result = relationship("Result", backref="surveys")

# Create tables
Base.metadata.create_all(bind=engine)

# FastAPI app
app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Schemas
class SurveyBase(BaseModel):
    name: str
    description: str
    result: Optional[int] = None
    user: int

class SurveyCreate(SurveyBase):
    pass

class SurveyResponse(SurveyBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

# CRUD Endpoints
@app.post("/Survey/AddSurvey", response_model=SurveyResponse)
def create_survey(survey: SurveyCreate, db: Session = Depends(get_db)):
    db_survey = Survey(**survey.dict())
    db.add(db_survey)
    db.commit()
    db.refresh(db_survey)
    return db_survey

@app.get("/Survey/{id}", response_model=SurveyResponse)
def read_survey(id: int, db: Session = Depends(get_db)):
    db_survey = db.query(Survey).filter(Survey.id == id).first()
    if not db_survey:
        raise HTTPException(status_code=404, detail="Survey not found")
    return db_survey

@app.put("/Survey/{id}", response_model=SurveyResponse)
def update_survey(id: int, updated_survey: SurveyCreate, db: Session = Depends(get_db)):
    db_survey = db.query(Survey).filter(Survey.id == id).first()
    if not db_survey:
        raise HTTPException(status_code=404, detail="Survey not found")

    for key, value in updated_survey.dict().items():
        setattr(db_survey, key, value)

    db.commit()
    db.refresh(db_survey)
    return db_survey

@app.delete("/Survey/{id}", response_model=dict)
def delete_survey(id: int, db: Session = Depends(get_db)):
    db_survey = db.query(Survey).filter(Survey.id == id).first()
    if not db_survey:
        raise HTTPException(status_code=404, detail="Survey not found")
    db.delete(db_survey)
    db.commit()
    return {"detail": "Survey deleted successfully"}

@app.get("/Survey/user/{user_id}", response_model=List[SurveyResponse])
def read_surveys_by_user(user_id: int, db: Session = Depends(get_db)):
    surveys = db.query(Survey).filter(Survey.user == user_id).all()
    return surveys

@app.get("/Survey/{id}/link", response_model=dict)
def get_link(id: int, db: Session = Depends(get_db)):
    db_survey = db.query(Survey).filter(Survey.id == id).first()
    if not db_survey:
        raise HTTPException(status_code=404, detail="Survey not found")
    link = f"http://example.com/surveys/{id}"
    return {"link": link}

@app.get("/Survey/GetAllSurveys", response_model=List[SurveyResponse])
def get_all_surveys(db: Session = Depends(get_db)):
    surveys = db.query(Survey).all()
    return surveys
