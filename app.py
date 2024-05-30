from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        start_lat = data.get('start_lat')
        start_lon = data.get('start_lon')
        distance = data.get('distance')

        if not all([start_lat, start_lon, distance]):
            return jsonify({'error': 'Missing required parameters'}), 400

        # Dummy values for missing features (Replace with appropriate values)
        features = [
            0,          # price_distance
            start_lat,  # start_lat
            start_lon,  # start_lon
            0,          # end_lat
            0,          # end_lon
            0,          # price_duration
            distance,   # distance
            0,          # duration
            0,          # cost
            0,          # cost_distance
            0,          # cost_duration
            0,          # driver_score
            0           # rider_score
        ]

        model = joblib.load('model.pkl')
        prediction = model.predict([features])
        return jsonify({'prediction': prediction[0]})

    except Exception as e:
        print(f"Error during prediction: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

