from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from textSummarizer.logging import logger

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<")
except Exception as e:
    logger.exception(e)
    raise e
