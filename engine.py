import os
from pyspark.sql import SQLContext
 
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MetricEngine:
    def __init__(self, sc, data_path):
        logger.info("Starting up the Recommendation Engine: ")
        self.sc = sc
        self.sqlContext = SQLContext(sc)
        logger.info("Loading kpi data...")
        kpi_path = os.path.join(data_path, 'kpi_0226.csv')
        self.kpiDf = self.sqlContext.read.option("header", "true").csv(f'file://{kpi_path}')
        logger.info("Loading metric data...")
        metric_path = os.path.join(data_path, 'metric_0226.csv')
        self.metricDf = self.sqlContext.read.option("header", "true").csv(f'file://{metric_path}')

