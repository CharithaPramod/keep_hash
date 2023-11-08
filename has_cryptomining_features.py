import re
import psutil
import os

# Define thresholds for CPU and memory usage (you can adjust these values)
CPU_THRESHOLD_PERCENT = 70  # CPU usage threshold
MEMORY_THRESHOLD_PERCENT = 70  # Memory usage threshold

def has_crypto_mining_features(activity):
    try:
        cmdline = activity['cmdline']  # Command-line arguments of the activity

        # Define a list of keywords and patterns often associated with crypto-mining
        crypto_mining_keywords = [
            "cgminer", "BFGMiner", "Claymore", "NiceHash", "XMRig", "cpuminer", "Ethminer", "T-Rex", "GMiner", "PhoenixMiner",
            "Bitcoin", "Ethereum", "Litecoin", "Monero", "Ripple", "Zcash", "Dash", "Dogecoin", "Bitcoin Cash", "Ethereum Classic",
            "Slush Pool", "F2Pool", "Antpool", "Nanopool", "Ethermine", "Miningpoolhub", "Suprnova", "Dwarfpool", "Prohashing", "ViaBTC",
            "ASIC", "GPU", "CPU", "FPGA", "Antminer", "Bitmain", "Innosilicon", "Nvidia", "AMD", "Mining rig",
            "SHA-256", "Scrypt", "Ethash", "X11", "Equihash", "Cryptonight", "Blake2s", "Lyra2RE", "DaggerHashimoto", "RandomX",
            "--start", "--stop", "-G", "-N", "-U", "--server", "--user", "--pass", "--algorithm", "--stratum", "--threads", "--intensity", "--benchmark", "--api-port",
            "Bitcoin wallet addresses", "Ethereum wallet addresses", "Monero wallet addresses", "Litecoin wallet addresses",
            "Hashrate", "Sol/s", "Mining farm", "Cryptocurrency yield", "Mining difficulty", "Proof of Work", "Proof of Stake", "Block reward", "Mining pool fee", "GPU overclocking",
            "Cryptojacking", "Coinhive", "Cryptocurrency malware", "Botnet mining", "GPU temperature", "Miner commission", "Mining profitability", "Dual mining", "Mining script"
        ]
        # Each line contains 30 keywords.

        for keyword in crypto_mining_keywords:
            if re.search(keyword, cmdline, re.IGNORECASE):
                return True

        # Check CPU usage
        cpu_percent = psutil.cpu_percent(interval=1)  # Get CPU usage over a 1-second interval
        if cpu_percent > CPU_THRESHOLD_PERCENT:
            return True

        # Check memory usage
        memory_percent = psutil.virtual_memory().percent
        if memory_percent > MEMORY_THRESHOLD_PERCENT:
            return True

        # Example: Check the number of network connections
        network_connections = psutil.net_connections(kind='inet')
        if len(network_connections) > 10:
            return True
        
        # Additional heuristic checks
        if check_network_connections():
            return True
        if check_file_system_access():
            return True
        if check_thread_count():
            return True

        return False

    except Exception as e:
        # Handle any exceptions that may occur during feature extraction
        print(f"Error checking for crypto-mining features: {str(e)}")

    return False

# Example usage:
activity = {'cmdline': 'c:\miner.exe -t 4 -u user -p pass'}  # Replace with actual activity data
if has_crypto_mining_features(activity):
    print("Crypto-mining features detected.")
else:
    print("No crypto-mining features detected.")

# check for suspicious network connections
def check_network_connections():
    # Retrieve network connections
    network_connections = psutil.net_connections(kind='inet')

    # Check for connections to known mining pools or suspicious IP addresses
    for conn in network_connections:
        if 'miningpool.com' in conn.raddr[0]:
            return True
    return False

# check for suspicious file system access
def check_file_system_access():
    # Check for file system activity involving sensitive directories
    sensitive_directories = ['C:\\Temp', 'C:\\Users\\User\\AppData\\Local\\Temp']

    for directory in sensitive_directories:
        if os.path.commonpath([directory, activity['file_path']]) == directory:
            return True
    return False

# check for high number of threads
def check_thread_count():
    try:
        pid = activity['pid']
        process = psutil.Process(pid)
        num_threads = process.num_threads()
        
        if num_threads > 20:  # Adjust the threshold as needed
            return True
    except psutil.NoSuchProcess:
        pass
import re
import psutil
import os

# Define thresholds for CPU and memory usage (you can adjust these values)
CPU_THRESHOLD_PERCENT = 70  # CPU usage threshold
MEMORY_THRESHOLD_PERCENT = 70  # Memory usage threshold

def has_crypto_mining_features(activity):
    try:
        cmdline = activity['cmdline']  # Command-line arguments of the activity

        # Define a list of keywords and patterns often associated with crypto-mining
        crypto_mining_keywords = [
            "cgminer", "BFGMiner", "Claymore", "NiceHash", "XMRig", "cpuminer", "Ethminer", "T-Rex", "GMiner", "PhoenixMiner",
            "Bitcoin", "Ethereum", "Litecoin", "Monero", "Ripple", "Zcash", "Dash", "Dogecoin", "Bitcoin Cash", "Ethereum Classic",
            "Slush Pool", "F2Pool", "Antpool", "Nanopool", "Ethermine", "Miningpoolhub", "Suprnova", "Dwarfpool", "Prohashing", "ViaBTC",
            "ASIC", "GPU", "CPU", "FPGA", "Antminer", "Bitmain", "Innosilicon", "Nvidia", "AMD", "Mining rig",
            "SHA-256", "Scrypt", "Ethash", "X11", "Equihash", "Cryptonight", "Blake2s", "Lyra2RE", "DaggerHashimoto", "RandomX",
            "--start", "--stop", "-G", "-N", "-U", "--server", "--user", "--pass", "--algorithm", "--stratum", "--threads", "--intensity", "--benchmark", "--api-port",
            "Bitcoin wallet addresses", "Ethereum wallet addresses", "Monero wallet addresses", "Litecoin wallet addresses",
            "Hashrate", "Sol/s", "Mining farm", "Cryptocurrency yield", "Mining difficulty", "Proof of Work", "Proof of Stake", "Block reward", "Mining pool fee", "GPU overclocking",
            "Cryptojacking", "Coinhive", "Cryptocurrency malware", "Botnet mining", "GPU temperature", "Miner commission", "Mining profitability", "Dual mining", "Mining script"
        ]
        # Each line contains 30 keywords.

        for keyword in crypto_mining_keywords:
            if re.search(keyword, cmdline, re.IGNORECASE):
                return True

        # Check CPU usage
        cpu_percent = psutil.cpu_percent(interval=1)  # Get CPU usage over a 1-second interval
        if cpu_percent > CPU_THRESHOLD_PERCENT:
            return True

        # Check memory usage
        memory_percent = psutil.virtual_memory().percent
        if memory_percent > MEMORY_THRESHOLD_PERCENT:
            return True

        # Example: Check the number of network connections
        network_connections = psutil.net_connections(kind='inet')
        if len(network_connections) > 10:
            return True
        
        # Additional heuristic checks
        if check_network_connections():
            return True
        if check_file_system_access():
            return True
        if check_thread_count():
            return True

        return False

    except Exception as e:
        # Handle any exceptions that may occur during feature extraction
        print(f"Error checking for crypto-mining features: {str(e)}")

    return False

# Example usage:
activity = {'cmdline': 'c:\miner.exe -t 4 -u user -p pass'}  # Replace with actual activity data
if has_crypto_mining_features(activity):
    print("Crypto-mining features detected.")
else:
    print("No crypto-mining features detected.")

# check for suspicious network connections
def check_network_connections():
    # Retrieve network connections
    network_connections = psutil.net_connections(kind='inet')

    # Check for connections to known mining pools or suspicious IP addresses
    for conn in network_connections:
        if 'miningpool.com' in conn.raddr[0]:
            return True
    return False

# check for suspicious file system access
def check_file_system_access():
    # Check for file system activity involving sensitive directories
    sensitive_directories = ['C:\\Temp', 'C:\\Users\\User\\AppData\\Local\\Temp']

    for directory in sensitive_directories:
        if os.path.commonpath([directory, activity['file_path']]) == directory:
            return True
    return False

# check for high number of threads
def check_thread_count():
    try:
        pid = activity['pid']
        process = psutil.Process(pid)
        num_threads = process.num_threads()
        
        if num_threads > 20:  # Adjust the threshold as needed
            return True
    except psutil.NoSuchProcess:
        pass
    return False