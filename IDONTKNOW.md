asyncio: 비동기 프로그래밍을 위한 모듈
-> CPU작업, I/O를 병렬로 처리하게 해줌 

##### 동기: 특정 작업이 끝나면 다음 작업을 처리하는 순차처리 방식 
##### 비동기: 여러 작업을 처리하도록 예약한 뒤 작업이 끝나면 결과를 받는 방식

```
async def 함수이름():
    코드
```

GET: 서버로부터 리소스를 가져올 때 씀, READ API
> route 메소드 이용 -> str 데이터 타입을 반환함 
> JSONResponse 객체 이용 > dict 자료형을 JSON으로 변환 가능함. 

POST: 서버에 데이터를 저장하고자 하는 경우
> 스키마 디펜던시 있음: pydantic
> Pydantic에서 BaseModel 상속 없이는 POST 작성할 수 없음. 

PUT: UPDATE 해당하는 메소드, 모든 내용 바꿈
PATCH: 일부의 내용을 바꿈 

endpoint 내부에서 사용하고 있는 함수들은 async일 필요가 없음 
JWT_TOkEN: 보안때문에 사용하는 것 






