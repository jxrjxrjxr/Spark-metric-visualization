cd /workspace-1/CloudCompute/cc-workspace/first-application
pip3 install -r requirements.txt
/opt/spark/bin/spark-submit --master "spark://spark-master:7077" server.py