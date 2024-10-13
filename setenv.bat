set OTEL_SERVICE_NAME=flask-api
set OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317
set OTEL_RESOURCE_ATTRIBUTES=deployment.environment=dev,service.version=1.0.0
set SPLUNK_ACCESS_TOKEN=30ufQYyFvKA16EmVFWe5KA
set OTEL_EXPORTER_OTLP_TRACES_PROTOCOL=http/protobuf
set OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=https://ingest.us1.signalfx.com/v2/trace/otlp
