from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_socketio import SocketIO
from threading import Thread
from is_trusted_activity import is_trusted_activity, get_trusted_activities, get_untrusted_activities
from data_extracter import extract_running_activities, categorize_activities

app = Flask(__name__)
socketio = SocketIO(app)

# Function to extract all running activities in the system
total_scanned_Files = 0

@app.route('/')
def index():
    # running processes
    # running_activities, check_respones = extract_running_activities()
    # for activity in running_activities:
    #     trusted_activities, untrusted_activities = categorize_activities(running_activities)
    # print(check_respones)
    return render_template('index.html')

@app.route('/start_scan', methods=['POST'])
def start_scan():
    log_message = []

    # update the "Start Scan" button value to "Scanning"
    button_text = "Scanning"

    # set the response status code to 202 (Accepted)
    response = jsonify({button_text: button_text})
    response.status_code = 202

    # run the extract_running_activities() function
    running_activities, check_respones = extract_running_activities(log_message)

    # update the log-box with the log messages
    if log_message:
        response.headers['log_message'] = '\n'.join(log_message)
    # response.headers['log_message'] = '\n'.join(log_messages)

    print(check_respones)
    # update the "Start Scan" button value to "Scan Completed"
    button_text = "Scan Completed"
    response.headers['button_text'] = button_text
    # scanned_files = total_scanned_Files
 
    # update the response status code to 200 (OK)
    response.status_code = 200
    print(response.headers)
    return response

@app.route('/home')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()