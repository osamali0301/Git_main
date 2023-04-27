import os
import uvicorn
import sys

sys.path.append("..")

ROOT_DIR = os.path.abspath(os.curdir)

if __name__ == '__main__':
	uvicorn.run("stop_alert:app", host="192.168.71.44", access_log=True, port=8000, workers=1)
# limit_concurrency=2000,backlog=50, timeout_keep_alive=5)
