from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_lidar_data():
    # Define the absolute path to the JSON file
    json_file_path = r'C:\Users\sriva\OneDrive\Pictures\react - fronted- flask lidar showing\data.json'
    
    # Read LIDAR data from JSON file
    try:
        with open(json_file_path, 'r') as f:
            file_content = f.read()
            print("File Content:", file_content)  # Debugging line
            lidar_data = json.loads(file_content)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    return jsonify(lidar_data)

if __name__ == '__main__':
    app.run(debug=True)
