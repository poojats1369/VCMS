import uuid
from api.db import *
from conf.database import *
from fastapi import Depends
from api.helper.helper import *
from sqlalchemy.orm import Session

def user_activity_funct( db: Session = Depends(get_db)):
    pass

def get_user_activity_by_id(db:Session):
    activity_id = db.query(UserActivityLog, UserActivityList, User).join(UserActivityList,
                                                                     UserActivityLog.activity_id == UserActivityList.activity_id).filter(User.user_id == UserActivityLog.user_id).order_by(
        UserActivityLog.id).all()
    # user = db.query(UserActivityLog).filter(UserActivityLog.id == user_id).first()
    # return activity_id
    return {"success": True, "details": prepare_response_user_activity(activity_id)}

def get_all_user_activity(db:Session):
    activity = db.query(UserActivityLog, UserActivityList).all()
    # users =  db.query(UserActivityLog).all()
    if activity:
        return {"success": True, "details": prepare_response_user_activity(activity)}
    else:
        False

def prepare_response_user_activity(activityid: UserActivityIDSchema, activity: UserActivitySchema):
    return {
                "user_id" : activityid.user_id,
                "user_role" : activityid.user_role,
                "activity_id" : activityid.activity_id,
                "activity_slug" : activityid.activity_slug,
                "logged_at" : activityid.logged_at,
                "activity_name" : activity.activity_name,
                "activity_description" : activity.activity_description
    }

