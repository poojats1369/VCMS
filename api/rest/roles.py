from api.db import *
from api.domain import *
from api.helper.helper import *
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter

router = APIRouter()

@router.post("/roles")
def add_role(role_data: RoleSchema, db: Session = Depends(get_db)):
    result = role_add(role_data,db)
    if result:
        return {
            "response": {
                "code": 201,
                "status": "success",
                "alert": [{
                    "message": "New role added successfully",
                    "type": "created",
                }]
            }
        }
    else:
        return {
            "response": {
                "code": 401 | 500,
                "status": "failure",
                "alert": [{
                    "message": "Role already exists | internal server error",
                    "type": "failure",
                }],
            }
        }

@router.get("/roles")
def get_roles(db: Session = Depends(get_db)):
    result=roles_get(db)
    is_data = 1 if result else 0
    if result:
        role_list = []
        for user in result:
            role = {
                "id":user.id,
                "role_name": user.role_name,
                "permissions": user.permissions,
                "status": user.status
            }
            role_list.append(role)

        return {
            "response": {
                "code": 200,
                "status": "success",
               "alert": [{
                    "message": "Roles fetched successfully ",
                    "type": "Fetch"                    
                }],
                "users": role_list,
                "is_data":is_data
                
            }
        }
    else:
        return {
            "response": {
                "code": 404,
                "status": "failure",
                "alert": [{
                    "message": "No roles found",
                    "type": "failure"
                }],
                "is_data":is_data
            }
        }

@router.put("/roles")
def update_role(role_id: str, role_data: UpdateRoleSchema, db: Session = Depends(get_db)):
    result = role_update(role_id, role_data, db)
    is_data = 1 if result else 0
    if result:
        roles_data = {
                    "role_name": result.role_name,
                    "permissions": result.permissions,
                    "status": result.status
                }
        return {
            "response": {
                "code": 200,
                "status": "success",
                "alert": [{
                    "message": f"Role updated successfully",
                    "type": "Update",
                }],
                "data": roles_data,
                "is_data":is_data
            }
        }
    else:
        return {
            "response": {
                "code": 404,
                "status": "Failure",
                "alert": [{
                    "message": "Role id not found, Or the Role already exists",
                    "type": "Failure"
                }],
                "is_data":is_data
            }
        }
    
@router.delete("/roles")
def delete_role(role_id: str,db: Session = Depends(get_db)):

    result = role_delete(role_id, db)
    if result:
        return {
            "response": {
                "code": 200,
                "status": "success",
                "alert": [{
                    "message": "Role deleted successfully",
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
                    "message": "Role not found",
                    "type": "failure"
                }],
            }
        }
