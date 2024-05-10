from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
import uvicorn


from math_service import MathService


math_service = MathService()


app = FastAPI()


@app.get(path="/")
async def health_check():
    return JSONResponse(
        content={"message": "ok"},
        status_code=status.HTTP_200_OK,
    )


@app.post(path="/factorial/{number}")
async def factorial(number: int):
    return JSONResponse(
        content={"answer": math_service.factorial(number)},
        status_code=status.HTTP_200_OK,
    )


if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=8000)
