from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load('lr_model.pkl')


class ReviewRequest(BaseModel):
    text: str


@app.get("/")
def serve_home_page():
    return FileResponse("index.html")

@app.post("/predict")
def predict_sentiment(request: ReviewRequest):
    prediction = model.predict([request.text])[0]

    return {"sentiment": prediction}