from api.db import *
from typing import List
from api.domain import *
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter, Body
from constants import *

router = APIRouter()

@router.post("/user-activity")
def user_activity( db: Session = Depends(get_db)):
    result = user_activity_funct(db)
    is_data = 1 if result['success'] else 0
    if result:
        return {
                "response": {
                    "code": common['SUCCESS'],
                    "status": "success",
                    "alert": [{
                        "message": common['ZZZZZZZZZZZ'],
                        "type":"Created"
                    }],
                    "is_data":is_data
                }
        }
    else:
        {
            "respnse":{
                "code":common['FAILURE'],
                "status":"failure",
                "alert":[{
                    "message":common['ZZZZZZZZZZZ'],
                    "type":"failure"
                }],
                "is_data":is_data
            }
        }


@router.get("/user_activity/{user_id}")
def get_user(user_id: str, db: Session = Depends(get_db)):
    result = get_user_activity_by_id(user_id,db)
    is_data = 1 if result['success'] else 0
    if result:
        return {
                "response": {
                    "code": common['SUCCESS'],
                    "status": "success",
                    "alert": [{
                        "message": common['USER_ACTIVITY_FETCHED_MSG'],
                        "type":"Fetch"
                    }],
                    "is_data":is_data,
                    "data": result
                }
        }
    else:
        {
            "respnse":{
                "code":common['FAILURE'],
                "status":"failure",
                "alert":[{
                    "message":common['NO_USER_ACTIVITY'],
                    "type":"failure"
                }],
                "is_data":is_data
            }
        }
    

@router.get("/user-activity")
def get_user_activity(activity: UserActivitySchema, db: Session = Depends(get_db)):
    result=get_all_user_activity(activity, db)
    is_data = 1 if result else 0 
    if "code" in result and "message" in result:
        return {
            "response": {
                "code": result["code"],
                "status": "Failure",
                "alert": [{
                    "message": result["message"],
                    "type": "Failure"
                }],
                "is_data": 0
            }
        }

    else:
        return {
            "response": {
                "code": common['SUCCESS'],
                "status": "success",
                "alert": [{
                    "message": common['NO_USER_ACTIVITY'],
                    "type": "Update"
                }],
                "is_data": is_data,
                "data": result
            }
        }
   
   