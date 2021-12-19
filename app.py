from flask import Blueprint, render_template, send_file
main = Blueprint('main', __name__)
 
import os
import json
from engine import MetricEngine
 
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
 
from flask import Flask, request

# @main.route('/<string: name>', methods = ['GET'])
# def getCMDB(name):
#     pass

@main.route('/', methods=['GET'])
def getIndex():
    with open("templates/index.html", "r") as f:
        print(f.readlines())
    return render_template('index.html')

@main.route('/metric/<cmdb>/<kpi>', methods=['GET'])
def getMetric(cmdb, kpi):
    logging.debug(f'metric {cmdb} {kpi} requested')
    tdf = metric_engine.metricDf
    JSONobj = tdf.filter((tdf["cmdb_id"]==cmdb)&(tdf["kpi_name"]==kpi))\
                 .toPandas().to_json(orient="records")
    # return json.dumps(JSONobj)
    return JSONobj

@main.route('/kpi/<int:row_num>', methods = ['GET'])
def getKPI(row_num):
    logging.debug(f'KPI top {row_num:4d} records requested')
    JSONobj = metric_engine.kpiDf.toJSON().take(row_num)
    return json.dumps(JSONobj)

@main.route('/lib/<name>', methods= ['GET'])
def getLib(name):
    return send_file(f'./lib/{str(name)}')

@main.route('/static/<name>', methods=['GET'])
def getStatic(name):
    return send_file(f'./{str(name)}')

def create_app(sc, dataset_path):
    global metric_engine 
 
    metric_engine = MetricEngine(sc, dataset_path)    
    
    app = Flask(__name__, template_folder='templates')
    app.register_blueprint(main)
    return app