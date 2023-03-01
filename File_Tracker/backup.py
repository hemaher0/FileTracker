from imports import *


def backup_file(src_file, dest_dir):
    # Check if source file
    if not os.path.exists(src_file):
        logging.error(f"File '{src_file} ' doesn't exist")
        return

    # Create backup directory if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Create backup filename based on current date and time
    now = datetime.datetime.now()
    backup_file = os.path.join(dest_dir, f"{now.strftime('%Y-%m-%d_%H-%M-%S')}_{os.path.basename(src_file)}")

    # Copy soure
    try:
        shutil.copy(src_file, backup_file)
        logging.info(f"Backup created: '{backup_file}'")
    except Exception as e:
        logging.error(f"Error creating backup: {str(e)}")