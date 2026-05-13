# [1] 라우터 : 특정 도메인(주소)한 묶어주는 역할
from fastapi import APIRouter
# APIRouter( prefix='/공통도메인') vs @RequestMapping("/공통도메인")
router = APIRouter( prefix= "/api" )

# [3] 서비스 불러오기
from service import item_service

# [2] REST API 정의
# (1) GET
# http://localhost:8002/api/item?id=1
@router.get("/item")
async def item( id: int ) : 
    return item_service.item( id )

# (2) GET
# http://localhost:8002/api/items
@router.get("/items")
async def items( ) :
    return item_service.items()
 
# (3) POST 
# http://localhost:8002/api/save
# { "id": 3, "name": "보성홍차", "price": 200 }
@router.post("/save")
async def save( item: dict ) :
    return item_service.save( item )

# (4) PUT
# { "id": 1, "name": "박진감", "price": 200 }
@router.put("/update")
async def update( item: dict ) :
    return item_service.update( item )

# (5) DELETE
# http://localhost:8002/api/delete?id=1 
@router.delete("/delete")
async def delete( id: int ) :
    return item_service.delete( id )
