# flask-api

after cloning the repository

create a virtual env by running
python -m venv .venv

activate the virtual environment
.venv/scripts/activate

install flask and otel package

pip install flask
pip install "splunk-opentelemetry[all]"

run bootstrap
splunk-py-trace-bootstrap

set environment variables
./setenv.ps1

validate environment variables
./testenv.bat

Start the collector
Start-Service splunk-otel-collector

fianlly running the api
splunk-py-trace python main.py


![alt text](image.png)

Kill python process
Stop-Process -Name *python

# Check the registry key for environment variables
Get-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\splunk-otel-collector" -Name Environment

curl -X POST "https://ingest.us1.signalfx.com/v2/trace/otlp" -H "Content-Type: application/x-protobuf" -H "X-SF-Token: QHAkDNYhl2aOrwsU68CrQQ" -d "string"