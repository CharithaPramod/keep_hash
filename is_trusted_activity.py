# importing functions from is_trusted_activity directory
from is_trusted_activity.is_in_whitelisted_directory import is_in_whitelisted_directory
from is_trusted_activity.is_whitelisted_executable import is_whitelisted_executable
from is_trusted_activity.is_whitelisted_hash import is_whitelisted_hash


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

def is_trusted_activity(activity):
    if is_in_whitelisted_directory(activity.file_path) and \
       is_whitelisted_executable(activity.file_path) and \
       is_whitelisted_hash(activity.file_path):
        return True
    else:
        return False
    