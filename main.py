import os
import shutil
from datetime import date
# convert date in the following format "Mon DDth, YYYY"
def format_date(d):
    month_str = d.strftime('%b')  # Get the abbreviated month name
    return f"{month_str}"    # return the date in this "Mon DDth, YYYY" format
# End of format_date() method
def delete_productivity_tracker_files(folder_path,file_name):
    # List all files in the specified folder
    all_files = os.listdir(folder_path)
    print(all_files)
    # Filter files that contain "Leave Register" in their name
    productivity_tracker_register_files = [file for file in all_files if file.startswith(file_name)]
    print(productivity_tracker_register_files)
    # Delete each leave register file
    for file in all_files:
        if file not in productivity_tracker_register_files:
            file_path = os.path.join(folder_path, file)
            os.remove(file_path)
            print(f"Deleted: {file_path}")

def delete_leave_register_folder(folder_path, folder_name):
    # List all folders in the specified path
    all_folders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]
    print(all_folders)

    # Filter folders that contain the specified folder name
    leave_register_folders = [folder for folder in all_folders if folder.startswith(folder_name)]
    leave_register_folders.append('Company Holiday List')
    print(leave_register_folders)

    # Delete each leave register folder
    for folder in all_folders:
        if folder not in leave_register_folders:
            folder_path_to_delete = os.path.join(folder_path, folder)
            shutil.rmtree(folder_path_to_delete)
            print(f"Deleted folder: {folder_path_to_delete}")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    today = date.today()  # get today's date
    productivity_formatted_date = format_date(today)  # call the format_date(today) method and pass today's date
    print(productivity_formatted_date)
    if (os.path.exists('C:/Users/ADMIN/Productivity Tracker/Activity Tracker')):
        delete_productivity_tracker_files(f'C:/Users/ADMIN/Productivity Tracker/Activity Tracker', f'Team Activity - All - Asia_Kolkata - {productivity_formatted_date}')
    # Format the date as a string in the desired format
    leave_formatted_date = today.strftime("%Y-%m")
    print(leave_formatted_date)
    if (os.path.exists('C:/Users/ADMIN/Productivity Tracker/Leave Register')):
        delete_leave_register_folder(f'C:/Users/ADMIN/Productivity Tracker/Leave Register',f'Leave Register for {leave_formatted_date}')
    if (os.path.exists('C:/Users/ADMIN/Productivity Tracker/Send Leave notification/Leave Register - to send Notification')):
        delete_leave_register_folder(f'C:/Users/ADMIN/Productivity Tracker/Send Leave notification/Leave Register - to send Notification',f'Leave Register for {leave_formatted_date}')
    if (os.path.exists('C:/Users/ADMIN/Leave Register')):
        delete_leave_register_folder(f'C:/Users/ADMIN/Leave Register',f'Leave Register for {leave_formatted_date}')