from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()


@app.get(path="/")
async def health_check():
    return JSONResponse(content={"message": "ok"}, status_code=status.HTTP_200_OK)


@app.post(path="/factorial/{number}")
async def factorial(number: int):
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if number == 0:
        return 1
    return JSONResponse(
        content={"answer": number * factorial(number - 1)},
        status_code=status.HTTP_200_OK,
    )


if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=8000)
