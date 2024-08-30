from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_country():
    # Get the user's IP address
    user_ip = request.remote_addr
    
    # Use ipinfo.io to get location details
    response = requests.get(f'http://ipinfo.io/{user_ip}/json')
    data = response.json()
    
    # Extract the country from the response
    country = data.get('country', 'Unknown')
    
    return jsonify({"country": country})

if __name__ == '__main__':
    app.run(debug=True)
