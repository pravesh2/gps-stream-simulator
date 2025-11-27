GPS Stream Simulator

A lightweight Python-based real-time GPS telemetry generator that simulates vehicle movement and publishes high-frequency location data over MQTT.
Ideal for IoT, fleet systems, real-time pipelines, and technical interviews such as DevNullX.






🚀 Overview

This tool simulates a moving truck/vehicle and continuously streams:

Latitude

Longitude

Speed

Timestamp

Device ID

It is designed to closely mimic IoT hardware used in commercial fleet tracking.

📂 Project Structure
gps-stream-simulator/
│
├── gps_simulator.py       # Vehicle movement simulation logic
├── mqtt_client.py         # MQTT client to publish messages
├── requirements.txt       # Dependencies
└── README.md              # Documentation

🛠 Installation
1. Clone the repository
git clone https://github.com/pravesh2/gps-stream-simulator
cd gps-stream-simulator

2. Create & activate virtual environment
python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows

3. Install dependencies
pip install -r requirements.txt

▶️ Running the Simulator
Start GPS Streaming
python gps_simulator.py


You can edit the MQTT broker details in mqtt_client.py:

BROKER = "test.mosquitto.org"
TOPIC = "gps/data"

📡 Live Monitoring (MQTT Subscribe)

Use Mosquitto client:

mosquitto_sub -h test.mosquitto.org -t gps/data

🔄 Example Output
{
  "device_id": "truck-001",
  "lat": 28.6139,
  "lon": 77.2090,
  "speed": 54.2,
  "timestamp": "2025-11-15T12:42:23Z"
}

🧪 Use Cases

Testing backend ingestion systems

IoT/MQTT pipeline development

Load testing real-time systems

Practice for DevNullX architectural interviews

Fleet analytics and dashboards

📜 License

MIT License
