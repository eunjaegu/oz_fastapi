from fastapi import APIRouter

from app.dtos.create_meeting_response import CreateMeetingResponse
from app.services.meeting_sercice_edgedb import service_create_meeting_edgedb

edgedb_router = APIRouter(prefix="/v1/edgedb/meetings", tags=["Meeting"])
mysql_router = APIRouter(prefix="/v1/mysql/meetings", tags=["Meeting"])
# 원래는 어떤 DB를 쓰는지 URL에 적을 필요가 없다.
# 강의에서만 이렇게 한다.
# 실전에서는 db이름을 url 에 넣지 마세요.


@edgedb_router.post("", description="meeting을 생성합니다.")
async def api_create_meeting_edgedb() -> CreateMeetingResponse:
    return CreateMeetingResponse(url_code=(await service_create_meeting_edgedb()).url_code)


@mysql_router.post("", description="meeting을 생성합니다.")
async def api_create_meeting_mysql() -> CreateMeetingResponse:
    return CreateMeetingResponse(url_code="abc")
