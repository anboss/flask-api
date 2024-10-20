$env:OTEL_SERVICE_NAME = 'flask-api'
# $env:OTEL_EXPORTER_OTLP_ENDPOINT = 'https://ingest.us1.signalfx.com/v2/trace/otlp'

# 'http://localhost:4317'
$env:OTEL_RESOURCE_ATTRIBUTES = 'deployment.environment=dev,service.version=1.0.0'

#this came from my profile - to send traces directly to the olly

$env:SPLUNK_ACCESS_TOKEN = 'tAImzntJIgm0_LS0qd4zIA' 
$env:OTEL_EXPORTER_OTLP_TRACES_PROTOCOL = 'http/protobuf'
$env:OTEL_EXPORTER_OTLP_TRACES_ENDPOINT = 'https://ingest.us1.signalfx.com/v2/trace/otlp'
$env:OTEL_METRICS_ENABLED = 'true' 
$env:OTEL_TRACES_EXPORTER = 'otlp'
$env:APPNAM = 'flask-api'
$env:APPSUBLVLNAM = 'greet'