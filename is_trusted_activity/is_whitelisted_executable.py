import os
import subprocess

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
file_path = 'C:\\Windows\\System32\\notepad.exe'
if is_whitelisted_executable(file_path):
    print(f"'{file_path}' is a whitelisted executable.")
else:
    print(f"'{file_path}' is not a whitelisted executable.")
