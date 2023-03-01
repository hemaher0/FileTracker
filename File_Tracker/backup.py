from imports import *


def backup_file(src_file, dest_dir):

    logging.basicConfig(filename='mylog.log', level=logging.INFO)
    # Check if source file
    if not os.path.exists(src_file):
        logging.error(f"Backup failed: File {src_file} doesn't exist!")
        return

    # Create backup directory if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Create backup filename based on current date and time
    current_info = []
    now = datetime.datetime.now()

    current_info.append(os.path.basename(src_file))
    current_info.append(now.strftime('%Y-%m-%d_%H:%M'))
    current_info.append(os.path.getsize(src_file))
    current_info.append(os.path.getctime(src_file))
    current_info.append(os.path.getmtime(src_file))
    backup_file_name = os.path.join(dest_dir, f"{current_info[1]}_{os.path.basename(src_file)}")

    # Copy source
    try:
        shutil.copy(src_file, backup_file_name)
        logging.info(f"Backup succeed: {backup_file_name} at {current_info[1]}")
    except Exception as e:
        logging.error(f"Backup failed: can't copy!: {str(e)}")
