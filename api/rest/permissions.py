from api.db import *
from typing import List
from api.domain import *
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter, Body

router = APIRouter()

@router.post("/permission")
def add_permissions(permission_data: PermissionSchema, db: Session = Depends(get_db)):
    result = permission_add(permission_data,db)
    if result:
        return {
                "response": {
                    "code": 200,
                    "status": "success",
                    "alert": [{
                        "message": "new user permissions added.",
                        "type":"Created"
                    }]
                }
        }
    else:
        {
            "respnse":{
                "code":404,
                "status":"failure",
                "alert":[{
                    "message":"Failed to add permission",
                    "type":"failure"
                }]
            }
        }

@router.get("/permission")
def get_permissions(db: Session = Depends(get_db)):
    result=permission_get(db)
    is_data = 1 if result else 0

    if result:
        permission_list = []
        for permission in result:
            permission_data = {
                "id":permission.id,
                "permission_name": permission.permission_name,
                "permission_type": permission.permission_type,
                "collection":permission.collection,
                "status": permission.status
            }
            permission_list.append(permission_data)

        return {
            "response": {
                "code": 200,
                "status": "success",
               "alert": [{
                    "message": "Permission fetched successfully ",
                    "type": "success"
                }],
                "data": permission_list,
                "is_data":is_data
            }
        }
    else:
        return {
            "response": {
                "code": 404,
                "status": "failure",
                "alert": [{
                    "message": "No Permissions found",
                    "type": "failure"
                }],
                "is_data":is_data
            }
        }

@router.put("/permission")
def update_permissions(perm_id: str, perm_data: PermissionSchema,  db: Session = Depends(get_db)):
    result = permissions_update(perm_id, perm_data, db)
    is_data = 1 if result else 0

    if result:
        permission = {
                "permission_name": result.permission_name,
                "permission_type": result.permission_type,
                "collection":result.collection,
                "status": result.status
        }
        return {
            "response": {
                "code": 200,
                "status": "success",
                "alert": [{
                    "message": f"permission updated successfully",
                    "type": "Update",
                }],
                "data":permission,
                "is_data":is_data
            }
        }
    else:
        return {
            "response": {
                "code": 404,
                "status": "Failure",
                "alert": [{
                    "message": "Permission id not found",
                    "type": "Failure"
                }],
                "is_data":is_data
            }
        }
    
@router.delete("/permission")
def delete_permission(perm_id: str,db: Session = Depends(get_db)):

    result = permission_delete(perm_id, db)
    if result:
        return {
            "response": {
                "code": 200,
                "status": "success",
                "alert": [{
                    "message": "Permission deleted successfully",
                    "type": "deleted"
                }],
            }
        }
    else:
        return {
            "response": {
                "code": 404,
                "status": "failure",
                "alert": [{
                    "message": "Permission not found",
                    "type": "failure"
                }],
            }
        }

#Update users
@router.put("/updateuser") 
def update_user(bulk: bool, multiple_users_data: List[UpdateStatusSchema]=None, single_user_data: CmsUpdate=None,user_id: str= Body(),  db: Session = Depends(get_db)): 
    if bulk: 
        result = update_multiple_users(multiple_users_data, db) 
        is_data = 1 if result else 0 
        if isinstance(result, dict) and "code" in result and "message" in result:
            return { 
                "response": {
                "code": result["code"],
                "status": "Failure", 
                "alert": 
                    [{ 
                    "message": result["message"],
                    "type": "Failure"
                        }], 
                    "is_data":0 
                    } 
                } 
        else: 
            return { 
                "response": { 
                    "code": 200, 
                    "status": "Success", 
                    "alert": [{ 
                        "message": "Users updated.", 
                        "type": "Success" 
                            }],
                        "data":multiple_users_data, 
                        "is_data":is_data 
                        } 
                    }
        
    else:
        result = update_single_user(user_id, single_user_data, db) 
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
                    "code": 200,
                    "status": "success",
                    "alert": [{
                        "message": f"user id : {user_id}  updated successfully",
                        "type": "Update"
                    }],
                    "data": result,
                    "is_data": is_data
                }
            }