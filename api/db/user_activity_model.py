from conf.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean


class UserActivityLog(Base):
    __tablename__ = "user_activity_log"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user_role = Column(String)
    activity_id = Column(Integer, ForeignKey("user_activity_list.activity_id"))
    activity_slug = Column(String, unique=True)
    logged_at = Column(DateTime)

    activity = relationship("UserActivityList", backref="activity_logs")  

class UserActivityList(Base):
    __tablename__ = "user_activity_list"

    activity_id = Column(Integer, primary_key=True)
    activity_name = Column(String)
    activity_description = Column(String)
    activity_slug = Column(String, unique=True)
    status = Column(Boolean)

