<<<<<<< HEAD
import psutil
import re

# importing functions from other files
from is_trusted_activity import is_trusted_activity

# Function to extract all running activities in the system
def extract_running_activities():
    activities = []
    for proc in psutil.process_iter(attrs=['pid', 'name', 'cmdline']):
        activities.append({
            'pid': proc.info['pid'],
            'name': proc.info['name'],
            'cmdline': proc.info['cmdline']
        })
        print(proc.info['pid'], proc.info['name'], proc.info['cmdline'])
    return activities

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


# Function to extract CPU usage from untrusted activities
def extract_cpu_usage(untrusted_activities):
    cpu_usage_data = []

    for activity in untrusted_activities:
        try:
            pid = activity['pid']
            process = psutil.Process(pid)
            cpu_percent = process.cpu_percent(interval=1.0)  # Get CPU usage over a 1-second interval

            cpu_usage_data.append({
                'pid': pid,
                'cpu_percent': cpu_percent
            })

        except psutil.NoSuchProcess:
            # Handle the case where the process no longer exists
            pass
        except Exception as e:
            # Handle any other exceptions that may occur
            print(f"Error extracting CPU usage for PID {pid}: {str(e)}")

    return cpu_usage_data

# Function to identify crypto mining related functionalities
def has_crypto_mining_features(activity):
    # Implement logic to identify crypto mining features in an activity
    # You can search for keywords like 'hash', 'blockchain', 'address', etc.
    return False  # Placeholder logic

# Function to extract network usage from untrusted activities
def extract_network_usage(untrusted_activities):
    network_usage = []
    for activity in untrusted_activities:
        # Implement logic to extract network usage for each untrusted activity
        # Example: You can use tools like pcap to capture network packets
        network_usage.append({
            'pid': activity['pid'],
            'network_data': capture_network_data(activity)
        })
    return network_usage

# Function to capture network data for an activity
def capture_network_data(activity):
    # Implement logic to capture network data, including source, destination,
    # packet content, etc., for the given activity
    return {}  # Placeholder logic

# Function to extract parameter names in the activity
def extract_parameters(activity):
    # Implement logic to search for cryptocurrency-related keywords in the activity
    keywords = ['hash', 'blockchain', 'address', ...]  # Define relevant keywords
    found_keywords = []
    
    for keyword in keywords:
        if re.search(keyword, activity['cmdline'] or activity['name']):
            found_keywords.append(keyword)
    
    return found_keywords

# Function to extract memory usage from untrusted activities
def extract_memory_usage(untrusted_activities):
    memory_usage = []
    for activity in untrusted_activities:
        # Implement logic to extract memory usage for each untrusted activity
        # Example: You can use psutil to get memory usage of a specific process
        memory_info = psutil.Process(activity['pid']).memory_info()
        memory_usage.append({
            'pid': activity['pid'],
            'memory_info': memory_info
        })
    return memory_usage

# Your extract_features function combining all the above features
def extract_features(web_content):
    activities = extract_running_activities()
    trusted_activities, untrusted_activities = categorize_activities(activities)
    
    cpu_usage = extract_cpu_usage(untrusted_activities)
    network_usage = extract_network_usage(untrusted_activities)
    memory_usage = extract_memory_usage(untrusted_activities)
    
    features = {
        'trusted_activities': trusted_activities,
        'untrusted_activities': untrusted_activities,
        'cpu_usage': cpu_usage,
        'network_usage': network_usage,
        'memory_usage': memory_usage
    }
    
    return features


=======
import psutil
import re

# importing functions from other files
from is_trusted_activity import is_trusted_activity

# Function to extract all running activities in the system
def extract_running_activities():
    activities = []
    for proc in psutil.process_iter(attrs=['pid', 'name', 'cmdline']):
        activities.append({
            'pid': proc.info['pid'],
            'name': proc.info['name'],
            'cmdline': proc.info['cmdline']
        })
        print(proc.info['pid'], proc.info['name'], proc.info['cmdline'])
    return activities

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


# Function to extract CPU usage from untrusted activities
def extract_cpu_usage(untrusted_activities):
    cpu_usage_data = []

    for activity in untrusted_activities:
        try:
            pid = activity['pid']
            process = psutil.Process(pid)
            cpu_percent = process.cpu_percent(interval=1.0)  # Get CPU usage over a 1-second interval

            cpu_usage_data.append({
                'pid': pid,
                'cpu_percent': cpu_percent
            })

        except psutil.NoSuchProcess:
            # Handle the case where the process no longer exists
            pass
        except Exception as e:
            # Handle any other exceptions that may occur
            print(f"Error extracting CPU usage for PID {pid}: {str(e)}")

    return cpu_usage_data

# Function to identify crypto mining related functionalities
def has_crypto_mining_features(activity):
    # Implement logic to identify crypto mining features in an activity
    # You can search for keywords like 'hash', 'blockchain', 'address', etc.
    return False  # Placeholder logic

# Function to extract network usage from untrusted activities
def extract_network_usage(untrusted_activities):
    network_usage = []
    for activity in untrusted_activities:
        # Implement logic to extract network usage for each untrusted activity
        # Example: You can use tools like pcap to capture network packets
        network_usage.append({
            'pid': activity['pid'],
            'network_data': capture_network_data(activity)
        })
    return network_usage

# Function to capture network data for an activity
def capture_network_data(activity):
    # Implement logic to capture network data, including source, destination,
    # packet content, etc., for the given activity
    return {}  # Placeholder logic

# Function to extract parameter names in the activity
def extract_parameters(activity):
    # Implement logic to search for cryptocurrency-related keywords in the activity
    keywords = ['hash', 'blockchain', 'address', ...]  # Define relevant keywords
    found_keywords = []
    
    for keyword in keywords:
        if re.search(keyword, activity['cmdline'] or activity['name']):
            found_keywords.append(keyword)
    
    return found_keywords

# Function to extract memory usage from untrusted activities
def extract_memory_usage(untrusted_activities):
    memory_usage = []
    for activity in untrusted_activities:
        # Implement logic to extract memory usage for each untrusted activity
        # Example: You can use psutil to get memory usage of a specific process
        memory_info = psutil.Process(activity['pid']).memory_info()
        memory_usage.append({
            'pid': activity['pid'],
            'memory_info': memory_info
        })
    return memory_usage

# Your extract_features function combining all the above features
def extract_features(web_content):
    activities = extract_running_activities()
    trusted_activities, untrusted_activities = categorize_activities(activities)
    
    cpu_usage = extract_cpu_usage(untrusted_activities)
    network_usage = extract_network_usage(untrusted_activities)
    memory_usage = extract_memory_usage(untrusted_activities)
    
    features = {
        'trusted_activities': trusted_activities,
        'untrusted_activities': untrusted_activities,
        'cpu_usage': cpu_usage,
        'network_usage': network_usage,
        'memory_usage': memory_usage
    }
    
    return features


>>>>>>> aebdb32a284f16a76dcdaeed42bbfcc427f9c797
extract_running_activities()