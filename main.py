import os
import logging
import requests
import time
import google.protobuf


# # from tracing import setupTracingForFlask, setupTracingForRequests, setupTracing 
from flask import Flask, jsonify, request

from opentelemetry import trace
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.instrumentation.logging import LoggingInstrumentor
# from opentelemetry.sdk.trace import TracerProvider
# from opentelemetry.sdk.trace.export import (
#     BatchSpanProcessor,
#     ConsoleSpanExporter,
# )
# from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter

logging.basicConfig(level=logging.DEBUG)
google.protobuf.internal.api_implementation.Type = 'python'

# trace.set_tracer_provider(TracerProvider())
# span_processor = BatchSpanProcessor(OTLPSpanExporter(endpoint="https://ingest.us1.signalfx.com/v2/trace"))
# trace.get_tracer_provider().add_span_processor(
#     BatchSpanProcessor(ConsoleSpanExporter())
# )
# trace.get_tracer_provider().add_span_processor(
#     span_processor
# )

#initiate the flask api 
app = Flask(__name__)

LoggingInstrumentor().instrument(set_logging_format=True)
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()

tracer = trace.get_tracer(__name__)

#define a route
@app.route('/api/greet', methods=['GET'])

#define function greet
def greet():
    with tracer.start_as_current_span("example-request"):
        response = requests.get("http://www.google.com")
        logging.warning("Log message in span")
        logging.warning(f"Access Token: {os.environ['SPLUNK_ACCESS_TOKEN']}")
        logging.warning(f"Response status code: {response.status_code}")
        logging.warning(f"Response headers: {response.headers}")
        time.sleep(60)  # Sleep for 1 minute
    return jsonify({'message': 'Hello, World!'})

@app.route('/api/post', methods=['POST'])
def postgreet():
    data = request.get_json() 
    if data and 'name' in data:
        return jsonify({"message": f"Hello, {data['name']}!"}), 200
    else:
        return jsonify({"message": "Please provide a 'name' in the JSON payload."}), 400

#boilerplate code to run the flask app
if __name__ == '__main__':
    app.run(port=8000)





