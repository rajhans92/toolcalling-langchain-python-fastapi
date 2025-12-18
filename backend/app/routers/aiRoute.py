from fastapi import APIRouter, Depends, Field, HTTPException
from sqlalchemy.orm import Session
from app.helpers.database import get_db
from app.helpers.jwt import get_current_user
from app.agents.toolCalling import toolCallingAi


router = APIRouter(prefix="/ai", tags=["ai-tool-calling"])

@router.get("/tool-calling")
async def tool_calling(question: str = Field(...), user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    try:
        reply = toolCallingAi(question)
        return {"message": reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))