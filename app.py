from fastapi import FastAPI
from networksecurity.pipeline.train_pipeline import TrainPipeline
from dotenv import load_dotenv
import os
import certifi

ca=certifi.where()
load_dotenv()
mongo_db_key=os.getenv("MONGO_DB_URI")



app = FastAPI()
###################################"""

import pymongo
from networksecurity.exeption.costum_expection import CustomException
from networksecurity.constant import training_pipeline
from networksecurity.logging.loger import get_logger

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile,Request
from uvicorn import run as app_run
from fastapi.responses import Response
from starlette.responses import RedirectResponse
import pandas as pd
import sys
from networksecurity.utils.main_utils.utils import load_object

from networksecurity.utils.ml_utils.model.estimator import NetworkModel


client = pymongo.MongoClient(mongo_db_key, tlsCAFile=ca)

from networksecurity.constant.training_pipeline import DATA_INGESTION_COLLECTION_NAME
from networksecurity.constant.training_pipeline import DATA_INGESTION_DATABASE_NAME

database = client[DATA_INGESTION_DATABASE_NAME]
collection = database[DATA_INGESTION_COLLECTION_NAME]

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="./templates")

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def train_route():
    try:
        train_pipeline = TrainPipeline()

        train_pipeline.run_pipeline()
        return Response("Training is successful")
    except Exception as e:
        raise CustomException(e,sys)
    

    
if __name__=="__main__":
    app_run(app,host="0.0.1.0",port=8000)
