from imports import *


def rollback(src_file, dest_dir) :
    logging.basicConfig(filename='mylog.log', level=logging.INFO)

    if not os.path.exists(src_file):
        logging.error(f"Rollback failed : File {src_file} doesn't exist")
        return

    # Create backup directory if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)