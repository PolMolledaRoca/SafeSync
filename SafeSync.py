import os
import shutil
import argparse
from datetime import datetime

def create_backup(source_folder, backup_folder):
    if not os.path.exists(source_folder):
        print(f"Error: Source folder '{source_folder}' does not exist.")
        return
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_folder, f"backup_{timestamp}")
    
    try:
        shutil.copytree(source_folder, backup_path)
        print(f"Backup successful! Files copied to {backup_path}")
    except Exception as e:
        print(f"Error creating backup: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automated Backup Script")
    parser.add_argument("source", help="Path of the source folder to back up")
    parser.add_argument("destination", help="Path where backups should be stored")
    
    args = parser.parse_args()
    create_backup(args.source, args.destination)
