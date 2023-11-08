import psutil

def extract_memory_usage(untrusted_activities):
    memory_usage_data = []

    for activity in untrusted_activities:
        try:
            pid = activity['pid']
            process = psutil.Process(pid)
            memory_info = process.memory_info()

            # Resident Set Size (RSS) represents the non-swapped physical memory used by the process.
            rss = memory_info.rss

            # Virtual Memory Size (VMS) is the total amount of virtual memory used by the process.
            vms = memory_info.vms

            # Shared memory is the portion of memory that is shared among multiple processes.
            shared = memory_info.shared

            # Code size (text) represents the memory used by the program's code.
            text = memory_info.text

            # Data size is the memory used for data and stack storage.
            data = memory_info.data

            # Number of threads indicates how many threads the process has created.
            num_threads = process.num_threads()

            # Page faults represent the number of times the process had to access memory that is not currently in RAM.
            page_faults = memory_info.page_faults

            # Peak Memory Usage is the maximum working set size the process has reached.
            peak_memory = process.memory_info().peak_wset

            memory_usage_data.append({
                'pid': pid,
                'rss': rss,             # Monitoring non-swapped physical memory usage.
                'vms': vms,             # Monitoring total virtual memory usage.
                'shared': shared,       # Detecting memory shared among processes.
                'text': text,           # Monitoring memory used by the program's code.
                'data': data,           # Monitoring memory used for data and stack storage.
                'num_threads': num_threads,  # Checking the number of threads created.
                'page_faults': page_faults,  # Detecting the frequency of page faults.
                'peak_memory': peak_memory   # Monitoring maximum working set size.
            })

        except psutil.NoSuchProcess:
            # Handle the case where the process no longer exists
            pass
        except Exception as e:
            # Handle any other exceptions that may occur
            print(f"Error extracting memory usage for PID {pid}: {str(e)}")

    return memory_usage_data

# Example usage:
untrusted_activities = [{'pid': 123}, {'pid': 456}]  # Replace with your list of untrusted activities
memory_usage_data = extract_memory_usage(untrusted_activities)
for data in memory_usage_data:
    print(f"Memory usage for PID {data['pid']}:")
    print(f"RSS: {data['rss']} bytes")
    print(f"VMS: {data['vms']} bytes")
    print(f"Shared: {data['shared']} bytes")
    print(f"Text: {data['text']} bytes")
    print(f"Data: {data['data']} bytes")
    print(f"Number of Threads: {data['num_threads']}")
    print(f"Page Faults: {data['page_faults']}")
    print(f"Peak Memory: {data['peak_memory']} bytes")
import psutil

def extract_memory_usage(untrusted_activities):
    memory_usage_data = []

    for activity in untrusted_activities:
        try:
            pid = activity['pid']
            process = psutil.Process(pid)
            memory_info = process.memory_info()

            # Resident Set Size (RSS) represents the non-swapped physical memory used by the process.
            rss = memory_info.rss

            # Virtual Memory Size (VMS) is the total amount of virtual memory used by the process.
            vms = memory_info.vms

            # Shared memory is the portion of memory that is shared among multiple processes.
            shared = memory_info.shared

            # Code size (text) represents the memory used by the program's code.
            text = memory_info.text

            # Data size is the memory used for data and stack storage.
            data = memory_info.data

            # Number of threads indicates how many threads the process has created.
            num_threads = process.num_threads()

            # Page faults represent the number of times the process had to access memory that is not currently in RAM.
            page_faults = memory_info.page_faults

            # Peak Memory Usage is the maximum working set size the process has reached.
            peak_memory = process.memory_info().peak_wset

            memory_usage_data.append({
                'pid': pid,
                'rss': rss,             # Monitoring non-swapped physical memory usage.
                'vms': vms,             # Monitoring total virtual memory usage.
                'shared': shared,       # Detecting memory shared among processes.
                'text': text,           # Monitoring memory used by the program's code.
                'data': data,           # Monitoring memory used for data and stack storage.
                'num_threads': num_threads,  # Checking the number of threads created.
                'page_faults': page_faults,  # Detecting the frequency of page faults.
                'peak_memory': peak_memory   # Monitoring maximum working set size.
            })

        except psutil.NoSuchProcess:
            # Handle the case where the process no longer exists
            pass
        except Exception as e:
            # Handle any other exceptions that may occur
            print(f"Error extracting memory usage for PID {pid}: {str(e)}")

    return memory_usage_data

# Example usage:
untrusted_activities = [{'pid': 123}, {'pid': 456}]  # Replace with your list of untrusted activities
memory_usage_data = extract_memory_usage(untrusted_activities)
for data in memory_usage_data:
    print(f"Memory usage for PID {data['pid']}:")
    print(f"RSS: {data['rss']} bytes")
    print(f"VMS: {data['vms']} bytes")
    print(f"Shared: {data['shared']} bytes")
    print(f"Text: {data['text']} bytes")
    print(f"Data: {data['data']} bytes")
    print(f"Number of Threads: {data['num_threads']}")
    print(f"Page Faults: {data['page_faults']}")
    print(f"Peak Memory: {data['peak_memory']} bytes")
