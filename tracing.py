from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor


def setupTracingForFlask(app):
    # Implementation of setupTracingForFlask
    FlaskInstrumentor().instrument_app(app)

def setupTracingForRequests():
    RequestsInstrumentor().instrument()
    