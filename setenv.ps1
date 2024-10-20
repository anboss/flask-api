$env:OTEL_SERVICE_NAME = 'flask-api'
$env:OTEL_RESOURCE_ATTRIBUTES = 'deployment.environment=dev,service.version=1.0.0'
#this came from my profile - to send traces directly to the olly
$env:SPLUNK_ACCESS_TOKEN = 'JldpJnE0sSO28pJaL5zBAQ' 
$env:OTEL_EXPORTER_OTLP_TRACES_PROTOCOL = 'http/protobuf'
$env:OTEL_EXPORTER_OTLP_TRACES_ENDPOINT = 'https://ingest.us1.signalfx.com/v2/trace/otlp'
