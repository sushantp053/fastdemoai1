from fastapi import APIRouter
from database import get_session
from model import Address
from sqlmodel import select

router = APIRouter()

@router.post("/address/")
def create_address(address: Address):
    with next(get_session()) as session:
        session.add(address)
        session.commit()
        session.refresh(address)
        return address

@router.get("/address/{user_id}")
def get_address(user_id: int):
    with next(get_session()) as session:
        address = session.exec(select(Address).where(Address.user_id == user_id)).first()
        if address:
            return address
        return {"error": "Address not found"}