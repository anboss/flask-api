# import os
# import logging
# import requests

# from flask import Flask, jsonify, request, redirect
# from opentelemetry import trace
# from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
# from opentelemetry.exporter.otlp.proto.grpc.exporter import OTLPMetricsExporter

# from opentelemetry.propagate import extract
# from opentelemetry.sdk.trace import TracerProvider
# from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
# from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
# from opentelemetry.sdk.metrics import MeterProvider

# from opentelemetry.sdk.trace import sampling
# from opentelemetry.sdk.resources import SERVICE_NAME, Resource
# from opentelemetry.instrumentation.flask import FlaskInstrumentor
# from opentelemetry.instrumentation.requests import RequestsInstrumentor

# def setupTracing(appnam, appsublvlnam):
#     OTEL_OTLP_ENDPOINT = os.environ["OTEL_EXPORTER_OTLP_ENDPOINT"]
#     servicename = appnam + "-" + appsublvlnam
#     resource = Resource(attributes={SERVICE_NAME: servicename})

#     provider=TracerProvider(sampler=sampling.ALWAYS_ON, resource=resource)
#     trace.set_tracer_provider(provider)

#     span_exporter = OTLPSpanExporter(endpoint=OTEL_OTLP_ENDPOINT)   
#     span_processor = BatchSpanProcessor(span_exporter)
#     provider.add_span_processor(span_processor)

#     # Set up metrics exporter
#     metrics_exporter = OTLPMetricsExporter(endpoint=OTEL_OTLP_ENDPOINT)
#     metric_reader = PeriodicExportingMetricReader(metrics_exporter)
#     meter_provider = MeterProvider(resource=resource, metric_readers=[metric_reader])
#     trace.set_meter_provider(meter_provider)

#     tracer = trace.get_tracer(__name__)
#     return tracer

# def setupTracingForFlask(app):
#     # Implementation of setupTracingForFlask
#     FlaskInstrumentor().instrument_app(app)

# def setupTracingForRequests():
#     RequestsInstrumentor().instrument()

# def enableTraceDebugLogs():
#     logging.basicConfig(level=logging.DEBUG)

# def setTags(tags):
#     for key, value in tags.items():
#         os.environ[key] = value