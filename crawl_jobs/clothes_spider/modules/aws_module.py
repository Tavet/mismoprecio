import boto3
import json
import os

from datetime import timezone, datetime, timedelta
from dateutil import parser

from logzero import logger

BEST_DEAL_STORES_BUCKET = 'best-deal-stores-info'
BEST_DEAL_CLOTHES_FILE = 'clothes/clothes.json'


def get_clothes_data(store_name):
    logger.info(
        "------------------------------------------------------------------")
    logger.info("Leyendo el archivo de clothes para empezar a extraer datos")
    s3 = boto3.resource('s3')
    s3_object = s3.Object(BEST_DEAL_STORES_BUCKET, BEST_DEAL_CLOTHES_FILE)
    local_object = os.path.abspath(os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "../../../_static/data/clothes.json"))

    # Get object last date modified
    s3_object_datetime = s3_object.last_modified.strftime("%Y-%m-%d %H:%M:%S") # UTC 0

    # Get local object last date modified
    local_object_datetime_formatted = datetime.fromtimestamp(
        os.path.getmtime(local_object)).strftime('%Y-%m-%d %H:%M:%S') # UTC -5
    local_object_datetime_formatted_str = datetime.strptime(
        local_object_datetime_formatted, '%Y-%m-%d %H:%M:%S')
    local_object_datetime = str(
        local_object_datetime_formatted_str + timedelta(hours=5)) # from UTC-5 to UTC 0

    logger.info(
        "Última modificación archivo en AWS (UTC-0 default AWS): " + s3_object_datetime)
    logger.info("Última modificación archivo en local (from UTC-5 to UTC 0): " +
                local_object_datetime)

    # Update local object if there's changes
    if(s3_object_datetime > local_object_datetime):
        logger.info("Descargando la versión más reciente al local")
        s3.Bucket(BEST_DEAL_STORES_BUCKET).download_file(
            BEST_DEAL_CLOTHES_FILE, local_object)

    data = open(os.path.abspath(os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "../../../_static/data/clothes.json")))
    json_data = json.load(data)

    # Filter data with the store passed thorugh the param
    return [x for x in json_data if x['store'] == store_name][0]['content']
