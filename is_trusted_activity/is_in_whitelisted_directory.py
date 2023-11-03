import os

# Define a list of trusted directories
# Commonly whitelisted directories for Windows
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


def is_in_whitelisted_directory(file_path):
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
file_path = 'C:\\Windows\\System32\\RuntimeBroker.exe'
if is_in_whitelisted_directory(file_path):
    print(f"'{file_path}' is in a whitelisted directory.")
else:
    print(f"'{file_path}' is not in a whitelisted directory.")
