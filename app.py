from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

from custom_logging import setup_logger

app = Flask(__name__)
metrics = PrometheusMetrics(app)  # This will automatically expose default metrics

logger = setup_logger("api")


@app.route('/')
def home():
    logger.info("----------Home----------")
    return "Hello, Prometheus!"


@app.route('/test')
def test():
    logger.info("----------Test----------")
    return "******************"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
