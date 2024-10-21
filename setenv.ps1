$env:OTEL_SERVICE_NAME = 'flask-api-v1'
$env:OTEL_EXPORTER_OTLP_ENDPOINT = 'https://ingest.us1.signalfx.com/v2/trace/otlp'
$env:OTEL_RESOURCE_ATTRIBUTES = 'deployment.environment=dev,service.version=1.0.0'
# This came from my profile - to send traces directly to the olly
$env:SPLUNK_ACCESS_TOKEN = 'tjpC5s4YAmxv4Mn7pWzZdw'
$env:OTEL_EXPORTER_OTLP_TRACES_PROTOCOL = 'http/protobuf'
$env:OTEL_EXPORTER_OTLP_TRACES_ENDPOINT = 'https://ingest.us1.signalfx.com/v2/trace/otlp'
$env:OTEL_LOG_LEVEL = "DEBUG"