#importing pyspark
import pyspark
import json

#importing sparksessio
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_json

#creating a sparksession object and providing appName 
spark=SparkSession.builder.appName("pysparkdf").getOrCreate()

df2 = spark.read.option("header", "true").csv("../data/0226/metric/metric_0226.csv")
cmdbListSorted = list(df2.groupBy("cmdb_id").count().sort(col("count").desc()).toPandas()["cmdb_id"])
kpiDictSt = {}
for cmdb in cmdbListSorted:
    kpiDictSt[cmdb] = list(df2.filter(df2["cmdb_id"]==cmdb).groupBy("kpi_name").count()
                              .sort(col("count").desc()).toPandas()["kpi_name"])

with open("cmdb-kpi.json", "w") as f:
    json.dump(kpiDictSt, f, indent=4)