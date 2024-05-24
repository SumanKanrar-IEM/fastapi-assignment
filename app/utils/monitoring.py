from prometheus_client import start_http_server, Summary
import time

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')


# Decorator to track request processing time
def track_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start_time
        REQUEST_TIME.observe(duration)
        return result
    return wrapper


# Start Prometheus server to expose metrics
def start_monitoring_server():
    start_http_server(8001)
