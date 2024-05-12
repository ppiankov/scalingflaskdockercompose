from flask import Flask, jsonify
from datetime import datetime
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)
metrics.info('flask_info', 'Application info', version='0.0.1', app_name='flask_app')

@app.route('/')
def home():
    return "Welcome to the Flask Web Server!"

@app.route('/status')
def status():
    return jsonify({
        "status": "OK",
        "server_time": datetime.now().isoformat(),
        "version": "1.0.0"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
