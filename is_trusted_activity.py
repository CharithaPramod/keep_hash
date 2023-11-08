import os
import hashlib
import subprocess

# Function to identify trusted activities
#        is_digitally_signed(activity.file_path) and \
#        is_whitelisted_process_name(activity.process_name) and \
#        has_allowed_arguments(activity.command_line) and \
#        is_registry_allowed(activity.registry_access) and \
#        is_whitelisted_network_communication(activity.network_activity) and \
#        is_executed_by_trusted_user(activity.user_account) and \
#        is_whitelisted_scheduled_task(activity.scheduled_task) and \
#        is_whitelisted_system_service(activity.system_service) and \
#        has_allowed_system_calls(activity.system_calls) and \
#        has_normal_behavior(activity.behavior) and \
#        is_up_to_date(activity.last_update):

def get_trusted_activities(activities):
    trusted_activities = []
    for activity in activities:
        if is_trusted_activity(activity):
            trusted_activities.append(activity)
    return trusted_activities

def get_untrusted_activities(activities):
    untrusted_activities = []
    for activity in activities:
        if not is_trusted_activity(activity):
            untrusted_activities.append(activity)
    return untrusted_activities

def is_trusted_activity(activity):
    if is_in_whitelisted_directory(activity.file_path) or \
       is_whitelisted_executable(activity.file_path) or \
       is_whitelisted_hash(activity.file_path):
        return True
    else:
        return False

def is_in_whitelisted_directory(file_path):
    whitelisted_directories = [
    'C:\\Windows',
    'C:\\Program Files',
    'C:\\Program Files (x86)',  # For 32-bit applications on 64-bit Windows
    'C:\\ProgramData',
    'C:\\Users\\Public',
    'C:\\Users\\Default',
    'C:\\Users\\All Users',  # Symbolic link to C:\ProgramData on modern Windows versions
    'C:\\Users\\<YourUserName>',  # Replace with the username you trust
    'C:\\Windows\\System32',
    'C:\\Windows\\SysWOW64',  # For 32-bit system files on 64-bit Windows
    'C:\\Windows\\Microsoft.NET',
    'C:\\Windows\\Microsoft.NET\\Framework',  # .NET Framework directories
    'C:\\Windows\\assembly',  # Global Assembly Cache (GAC)
    # Add more directories as needed
    ]

    try:
        # Normalize the file path to handle variations in path format
        normalized_file_path = os.path.normpath(file_path)

        # Check if the normalized path starts with any trusted directory
        for trusted_dir in whitelisted_directories:
            if normalized_file_path.startswith(trusted_dir):
                return True

    except Exception as e:
        # Handle any exceptions that may occur during path normalization or checking
        print(f"Error checking directory: {str(e)}")

    return False

# Example usage:
# file_path = 'C:\\Windows\\System32\\RuntimeBroker.exe'
# if is_in_whitelisted_directory(file_path):
#     print(f"'{file_path}' is in a whitelisted directory.")
# else:
#     print(f"'{file_path}' is not in a whitelisted directory.")


def is_whitelisted_executable(file_path):
    # You can define a whitelist of trusted executables by their names or paths
    trusted_executables = [
    'explorer.exe',           # Windows Explorer
    'svchost.exe',            # Host Process for Windows Services
    'lsass.exe',              # Local Security Authority Subsystem Service
    'csrss.exe',              # Client/Server Runtime Subsystem
    'winlogon.exe',           # Windows Logon Application
    'wininit.exe',            # Windows Start-Up Application
    'services.exe',           # Services Control Manager
    'spoolsv.exe',            # Print Spooler Service
    'taskhost.exe',           # Host Process for Windows Tasks
    'taskeng.exe',            # Task Scheduler Engine
    'dwm.exe',                # Desktop Window Manager
    'ctfmon.exe',             # CTF Loader (Alternative User Input Text Input Processor)
    'alg.exe',                # Application Layer Gateway Service
    'conhost.exe',            # Console Window Host
    'lsmpoll.exe',            # Link-State Routing Protocol (used for networking)
    'mobsync.exe',            # Microsoft Synchronization Manager
    'explorer.exe',           # Windows Explorer
    'mstsc.exe',              # Remote Desktop Client
    'mmc.exe',                # Microsoft Management Console
    'services.exe',           # Services Control Manager
    'lsass.exe',              # Local Security Authority Subsystem Service
    'cmd.exe',                # Command Prompt
    'powershell.exe',         # Windows PowerShell
    'regedit.exe',            # Windows Registry Editor
    'notepad.exe',            # Notepad Text Editor
    'calc.exe',               # Calculator
    'calc.exe',               # Calculator
    'taskmgr.exe',            # Task Manager
    'mspaint.exe',            # Paint
    'msconfig.exe',           # System Configuration Utility
    'perfmon.exe',            # Performance Monitor
    'winword.exe',            # Microsoft Word
    'excel.exe',              # Microsoft Excel
    'iexplore.exe',           # Internet Explorer
    'firefox.exe',            # Mozilla Firefox
    'chrome.exe',             # Google Chrome
    'edge.exe',               # Microsoft Edge
    'outlook.exe',            # Microsoft Outlook
    'skype.exe',              # Skype
    'vncviewer.exe',          # VNC Viewer
    # Add more trusted executables as needed
    ]

    try:
        # Normalize the file path to handle variations in path format
        normalized_file_path = os.path.normpath(file_path)

        # Check if the file is in the whitelist by name
        file_name = os.path.basename(normalized_file_path)
        if file_name.lower() in [name.lower() for name in trusted_executables]:
            return True

        # Check the digital signature of the file
        verification_result = subprocess.check_output(
            f'powershell Get-AuthenticodeSignature "{normalized_file_path}"',
            shell=True
        ).decode()

        if "SignatureType : System" in verification_result:
            return True

    except Exception as e:
        # Handle any exceptions that may occur during the verification
        print(f"Error checking executable: {str(e)}")

    return False

# Example usage:
# file_path = 'C:\\Windows\\System32\\notepad.exe'
# if is_whitelisted_executable(file_path):
#     print(f"'{file_path}' is a whitelisted executable.")
# else:
#     print(f"'{file_path}' is not a whitelisted executable.")


def calculate_hash(file_path, hash_algorithm='sha256'):
    whitelisted_hashes = {
    'C:\\Windows\\System32\\notepad.exe': '45d494d6578e5b0b147ea654e9608db5',
    'C:\\Windows\\System32\\calc.exe': '2e88a9f06b2f9f01c10e9a875407dc9d',
    # Add more file paths and their corresponding hashes as needed
    }

    try:
        hasher = hashlib.new(hash_algorithm)

        with open(file_path, 'rb') as file:
            while True:
                data = file.read(65536)  # Read in 64k chunks
                if not data:
                    break
                hasher.update(data)

        return hasher.hexdigest()

    except Exception as e:
        # Handle any exceptions that may occur during hashing
        print(f"Error calculating hash: {str(e)}")

    return None

def is_whitelisted_hash(file_path):
    try:
        normalized_file_path = os.path.normpath(file_path)
        if normalized_file_path in whitelisted_hashes:
            return True

        # Calculate the hash of the file
        file_hash = calculate_hash(normalized_file_path)

        # Check if the calculated hash matches a whitelisted hash
        if file_hash and file_hash == whitelisted_hashes.get(normalized_file_path):
            return True

    except Exception as e:
        # Handle any exceptions that may occur during hash calculation or comparison
        print(f"Error checking file hash: {str(e)}")

    return False

# Example usage:
file_path = 'C:\\Windows\\System32\\notepad.exe'
if is_whitelisted_hash(file_path):
    print(f"'{file_path}' is a whitelisted file.")
else:
    print(f"'{file_path}' is not a whitelisted file.")
