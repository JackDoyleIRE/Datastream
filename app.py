from flask import Flask, render_template, Response
from flask_sse import sse
from datagenerator import DataGenerator 
import time

import redis

# Redis configuration
redis_host = "redis"
redis_port = 6379
redis_channel = "data-channel"

app = Flask(__name__)
app.config["REDIS_URL"] = "redis://localhost"  # You need to install and run a Redis server for Flask-SSE

app.register_blueprint(sse, url_prefix='/stream')

@app.route('/')
def index():
    return render_template('index.html')

def generate_data():
    data_generator = DataGenerator()
    while True:
        yield f"data: {data_generator.generate_data()}\n\n"
        time.sleep(1)

@app.route('/stream-data')
def stream_data():
    return Response(generate_data(), content_type='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)
