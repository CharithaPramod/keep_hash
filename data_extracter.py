import psutil
import re

from checkups import *

# importing functions from other files
from is_trusted_activity import is_trusted_activity

# Function to extract all running activities in the system
def extract_running_activities(log_messages):
    activities = []
    check_response = []
    log_messages.clear()
    log_messages.append("Scanning running activities...")

    total_scanned_files = 0
    # get the list of all running processes with all information
    print("Extracting running activities...")
    for proc in psutil.process_iter(attrs=['pid', 'name'
                                            , 'cmdline', 'exe', 'cpu_percent', 'username', 
                                            'status', 'create_time', 'cpu_percent', 'memory_percent', 'memory_info',
                                            'io_counters', 'num_threads', 'connections', 'nice', 'open_files',
                                            'ionice', 'threads', 'cpu_times', 'memory_maps'
                                    ]):
        try:
            process_info = proc.info
            activities.append({
            'pid': proc.info['pid'],
            'name': proc.info['name'],
            'cmdline': proc.cmdline(),
            'exe': proc.exe(),
            'cpu_percent': proc.info['cpu_percent'],
            'username': proc.info['username'],
            'status': proc.info['status'],
            'create_time': proc.info['create_time'],
            'memory_percent': proc.info['memory_percent'],
            'memory_info': proc.info['memory_info'],
            'io_counters': proc.info['io_counters'],
            'num_threads': proc.info['num_threads'],
            'connections': proc.info['connections'],
            'nice': proc.info['nice'],
            'open_files': proc.info['open_files'],
            'ionice': proc.info['ionice'],
            'threads': proc.info['threads'],
            'cpu_times': proc.info['cpu_times'],
            'memory_maps': proc.info['memory_maps']
        })
        except psutil.AccessDenied:
            continue
        except psutil.NoSuchProcess:
            continue

        # check there are any suspicious names
        if check_suspicious_names(process_info):
            print(f"Suspicious name detected: {process_info['name']}")
            check_response.append(f"Suspicious name detected: {process_info['name']}")
        # check for high cpu and memory usage
        if analyze_resource_usage(process_info):
            print(f"High CPU and memory usage detected for: {process_info['name']}")
            check_response.append(f"High CPU and memory usage detected for: {process_info['name']}")
        # check for unusual command line arguments
        if check_unusual_cmdline_args(process_info):
            print(f"Unusual command line arguments detected for: {process_info['name']}")
            check_response.append(f"Unusual command line arguments detected for: {process_info['name']}")
        # check for network connections
        if monitor_network_connections(process_info):
            print(f"Network connections detected for: {process_info['name']}")
            check_response.append(f"Network connections detected for: {process_info['name']}")
        # check for known mining paths
        if check_known_mining_paths(process_info):
            print(f"Known crypto mining executable path detected for: {process_info['name']}")
            check_response.append(f"Known crypto mining executable path detected for: {process_info['name']}")
        # check for hidden processes
        if check_for_hidden_processes(process_info):
            print(f"Hidden processes detected for: {process_info['name']}")
            check_response.append(f"Hidden processes detected for: {process_info['name']}")
        # check for usage over time
        if monitor_usage_over_time(process_info):
            print(f"Usage over time detected for: {process_info['name']}")
            check_response.append(f"Usage over time detected for: {process_info['name']}")
        if check_response == []:
            check_response.append("No suspicious activity detected")

        # update the total scanned files
        total_scanned_files += 1
    if not log_messages:
        log_messages.append("No suspicious activity detected")
            
    return activities, check_response


# Function to categorize activities as trusted or untrusted
def categorize_activities(activities):
    trusted_activities = []
    untrusted_activities = []
    
    for activity in activities:
        if is_trusted_activity(activity):
            trusted_activities.append(activity)
        else:
            untrusted_activities.append(activity)
    
    return trusted_activities, untrusted_activities


# # Function to extract CPU usage from untrusted activities
# def extract_cpu_usage(untrusted_activities):
#     cpu_usage_data = []

#     for activity in untrusted_activities:
#         try:
#             pid = activity['pid']
#             process = psutil.Process(pid)
#             cpu_percent = process.cpu_percent(interval=1.0)  # Get CPU usage over a 1-second interval

#             cpu_usage_data.append({
#                 'pid': pid,
#                 'cpu_percent': cpu_percent
#             })

#         except psutil.NoSuchProcess:
#             # Handle the case where the process no longer exists
#             pass
#         except Exception as e:
#             # Handle any other exceptions that may occur
#             print(f"Error extracting CPU usage for PID {pid}: {str(e)}")

#     return cpu_usage_data

# # Function to identify crypto mining related functionalities
# def has_crypto_mining_features(activity):
#     # Implement logic to identify crypto mining features in an activity
#     # You can search for keywords like 'hash', 'blockchain', 'address', etc.
#     return False  # Placeholder logic

# # Function to extract network usage from untrusted activities
# def extract_network_usage(untrusted_activities):
#     network_usage = []
#     for activity in untrusted_activities:
#         # Implement logic to extract network usage for each untrusted activity
#         # Example: You can use tools like pcap to capture network packets
#         network_usage.append({
#             'pid': activity['pid'],
#             'network_data': capture_network_data(activity)
#         })
#     return network_usage

# # Function to capture network data for an activity
# def capture_network_data(activity):
#     # Implement logic to capture network data, including source, destination,
#     # packet content, etc., for the given activity
#     return {}  # Placeholder logic

# # Function to extract parameter names in the activity
# def extract_parameters(activity):
#     # Implement logic to search for cryptocurrency-related keywords in the activity
#     keywords = ['hash', 'blockchain', 'address', ...]  # Define relevant keywords
#     found_keywords = []
    
#     for keyword in keywords:
#         if re.search(keyword, activity['cmdline'] or activity['name']):
#             found_keywords.append(keyword)
    
#     return found_keywords

# # Function to extract memory usage from untrusted activities
# def extract_memory_usage(untrusted_activities):
#     memory_usage = []
#     for activity in untrusted_activities:
#         # Implement logic to extract memory usage for each untrusted activity
#         # Example: You can use psutil to get memory usage of a specific process
#         memory_info = psutil.Process(activity['pid']).memory_info()
#         memory_usage.append({
#             'pid': activity['pid'],
#             'memory_info': memory_info
#         })
#     return memory_usage

# # Your extract_features function combining all the above features
# def extract_features(web_content):
#     activities = extract_running_activities()
#     trusted_activities, untrusted_activities = categorize_activities(activities)
    
#     cpu_usage = extract_cpu_usage(untrusted_activities)
#     network_usage = extract_network_usage(untrusted_activities)
#     memory_usage = extract_memory_usage(untrusted_activities)
    
#     features = {
#         'trusted_activities': trusted_activities,
#         'untrusted_activities': untrusted_activities,
#         'cpu_usage': cpu_usage,
#         'network_usage': network_usage,
#         'memory_usage': memory_usage
#     }
    
#     return features


# extract_running_activities()