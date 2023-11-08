import pyshark

def capture_network_data(pid, interface='eth0'):
    network_data = []

    # Define a packet capture filter to capture traffic associated with the specific process
    capture_filter = f'((ip.src_host == {pid}) or (ip.dst_host == {pid}))'

    # Use pyshark to capture network packets
    try:
        capture = pyshark.LiveCapture(interface=interface, display_filter=capture_filter)

        for packet in capture.sniff_continuously(packet_count=10):
            network_data.append(str(packet))

    except Exception as e:
        # Handle any exceptions that may occur during network data capture
        print(f"Error capturing network data for PID {pid}: {str(e)}")

    return network_data

def extract_network_usage(untrusted_activities):
    network_usage = []

    for activity in untrusted_activities:
        try:
            pid = activity['pid']

            # Capture network data for the specific process
            network_data = capture_network_data(pid)

            network_usage.append({
                'pid': pid,
                'network_data': network_data
            })

        except Exception as e:
            # Handle any exceptions that may occur during network data extraction
            print(f"Error extracting network data for PID {pid}: {str(e)}")

    return network_usage

# Example usage:
untrusted_activities = [{'pid': 123}, {'pid': 456}]  # Replace with your list of untrusted activities
network_usage_data = extract_network_usage(untrusted_activities)
for data in network_usage_data:
    print(f"Network data for PID {data['pid']}:")
    for packet in data['network_data']:
        print(packet)
import pyshark

def capture_network_data(pid, interface='eth0'):
    network_data = []

    # Define a packet capture filter to capture traffic associated with the specific process
    capture_filter = f'((ip.src_host == {pid}) or (ip.dst_host == {pid}))'

    # Use pyshark to capture network packets
    try:
        capture = pyshark.LiveCapture(interface=interface, display_filter=capture_filter)

        for packet in capture.sniff_continuously(packet_count=10):
            network_data.append(str(packet))

    except Exception as e:
        # Handle any exceptions that may occur during network data capture
        print(f"Error capturing network data for PID {pid}: {str(e)}")

    return network_data

def extract_network_usage(untrusted_activities):
    network_usage = []

    for activity in untrusted_activities:
        try:
            pid = activity['pid']

            # Capture network data for the specific process
            network_data = capture_network_data(pid)

            network_usage.append({
                'pid': pid,
                'network_data': network_data
            })

        except Exception as e:
            # Handle any exceptions that may occur during network data extraction
            print(f"Error extracting network data for PID {pid}: {str(e)}")

    return network_usage

# Example usage:
untrusted_activities = [{'pid': 123}, {'pid': 456}]  # Replace with your list of untrusted activities
network_usage_data = extract_network_usage(untrusted_activities)
for data in network_usage_data:
    print(f"Network data for PID {data['pid']}:")
    for packet in data['network_data']:
        print(packet)
