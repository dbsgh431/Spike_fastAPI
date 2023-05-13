from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    """app객체가 GET 유형의 요청을 받았을 때 처리

    Returns:
       지정한 string
    """


    return {

        "message" : "hello world"

    }