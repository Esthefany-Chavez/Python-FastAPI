from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

from app.schemas.device_schema import DeviceResponse
from app.schemas.user_schema import UserResponse

LoanStatus = Literal["active", "returned", "overdue"]


class LoanCreate(BaseModel):
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "user_id": 1,
                "device_id": 2,
                "loan_date": "2026-09-17T09:00:00",
                "return_date": None,
                "status": "active",
            }
        }
    )

    user_id: int
    device_id: int
    loan_date: datetime = Field(..., description="Date when the device was loaned")
    return_date: datetime | None = Field(None, description="Date when the device was returned")
    status: LoanStatus = Field(..., description="Status of the loan (e.g., active, returned, overdue)")


class LoanUpdate(BaseModel):
    user_id: int
    device_id: int
    loan_date: datetime = Field(..., description="Date when the device was loaned")
    return_date: datetime | None = Field(None, description="Date when the device was returned")
    status: LoanStatus = Field(..., description="Status of the loan (e.g., active, returned, overdue)")


class LoanResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    device_id: int
    loan_date: datetime
    return_date: datetime | None
    status: LoanStatus


class LoanDetailResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    loan_id: int
    user_id: int
    device_id: int
    loan_date: datetime
    return_date: datetime | None
    status: LoanStatus
    user: UserResponse
    device: DeviceResponse