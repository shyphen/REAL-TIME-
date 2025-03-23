from flask import Flask, jsonify, request
import psutil
import time

# Initialize Flask app
app = Flask(__name__)



@app.route('/get_system_usage')
def get_system_usage():
    try:
        # Fetch system usage stats (e.g., using psutil)
        usage_data = {
            'cpu_percent': 55.0,  # Example data
            'memory_percent': 75.0  # Example data
        }
        return jsonify(usage_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/')
def index():
    return "Process Monitoring API is running"

# Route to fetch all processes and their details
@app.route('/get_processes', methods=['GET'])
def get_processes():
    try:
        processes = []
        for process in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info', 'num_threads']):
            processes.append({
                'pid': process.info['pid'],
                'name': process.info['name'],
                'cpu_percent': process.info['cpu_percent'],
                'memory_usage': process.info['memory_info'].rss / 1024 / 1024,  # Convert to MB
                'num_threads': process.info['num_threads']
            })
        return jsonify(processes)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/get_system_usage', methods=['GET'])
def get_system_usage():
    system_usage = {
        'cpu_percent': psutil.cpu_percent(interval=1),
        'memory_percent': psutil.virtual_memory().percent
    }
    return jsonify(system_usage)



if __name__ == '__main__':
    app.run(debug=True)
