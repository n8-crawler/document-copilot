from uuid import UUID

from fastapi import Depends,APIRouter,status
from sqlalchemy.orm import Session
from app.database import get_db
from app.routers.dependencies import get_current_user
from app.models.users import User
from app.schemas.threads import ChatResponse,ChatCreate,ChatUpdate
from app.services.threads import ThreadService


router = APIRouter(prefix="/threads",tags=["threads"])

@router.post("/",response_model=ChatResponse,status_code=status.HTTP_201_CREATED)
def createthread(request:ChatCreate,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    service = ThreadService(db)
    return service.create_thread(current_user=current_user,request=request)

@router.get("/mythreads",response_model=list[ChatResponse],status_code=status.HTTP_200_OK)
def getthreads(db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    service = ThreadService(db)
    return service.get_threads(current_user=current_user)

@router.get("/mythread/{thread_id}",response_model=ChatResponse,status_code=status.HTTP_200_OK)
def getthread(thread_id:UUID,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    service = ThreadService(db)
    return service.get_thread(thread_id=thread_id,current_user=current_user)

@router.patch("/mythread/{thread_id}",response_model=ChatResponse,status_code=status.HTTP_202_ACCEPTED)
def updatethread(request:ChatUpdate,thread_id:UUID,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    service = ThreadService(db)
    return service.update_thread(thread_id=thread_id,current_user=current_user,request=request)

@router.delete("/mythread/{thread_id}",status_code=status.HTTP_204_NO_CONTENT)
def deletethread(thread_id:UUID,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    service = ThreadService(db)
    return service.delete_thread(thread_id=thread_id,current_user=current_user)