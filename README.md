GPS Stream Simulator (MQTT + Real-Time Data)






A lightweight IoT simulator that generates continuous GPS coordinates and streams them via MQTT.

Perfect for:

Real-time data ingestion testing

Fleet + telemetry backend testing

DevNullX backend interview preparation

IoT → Cloud → Analytics pipeline development

📁 Project Structure
gps-stream-simulator/
│── gps_simulator.py
│── mqtt_client.py
│── requirements.txt
│── README.md

🧠 Architecture Diagram
┌──────────────────────┐
│  gps_simulator.py     │
│ Random GPS generator  │
└─────────┬─────────────┘
          │ JSON payload
┌─────────▼─────────────┐
│   mqtt_client.py       │
│ Publishes to MQTT      │
└─────────┬─────────────┘
          │
          ▼
  MQTT Broker (HiveMQ / Cloud MQTT)

⚙️ Installation
Install dependencies:
pip install -r requirements.txt

Run GPS Simulator:
python gps_simulator.py

📡 Example Output
{
  "lat": 28.70456,
  "lon": 77.10204,
  "timestamp": 1731592034.4215
}


Published to topic:

cc/gps
Why This Project Matters

This GPS + MQTT simulator shows you can:

Build IoT real-time streaming systems

Work with MQTT protocols

Generate realistic telemetry data

Understand fleet monitoring concepts

This is highly relevant to companies working on GPS, trucks, telematics, and IoT pipelines.
