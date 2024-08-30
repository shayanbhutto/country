from flask import Flask, request, jsonify
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/', methods=['GET'])
def current_time():
    # Get the timezone from the query parameters
    timezone = request.args.get('timezone', 'UTC')
    
    try:
        # Create a timezone object
        tz = pytz.timezone(timezone)
    except pytz.UnknownTimeZoneError:
        return jsonify({'error': 'Unknown timezone'}), 400

    # Get the current time in UTC and then convert to the requested timezone
    utc_now = datetime.utcnow().replace(tzinfo=pytz.utc)
    local_time = utc_now.astimezone(tz)

    # Format the time as a string
    time_str = local_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')

    return jsonify({'current_time': time_str})

if __name__ == '__main__':
    app.run(debug=True)
