import os
import datetime


timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
print(timestamp)

# Generate a timestamped filename for the backup
# backup_file = f"backup_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.sql"
backup_file = f"backup_{timestamp}.sql"

# Execute the backup command
os.system(f"mysqldump -u root first_database > {backup_file}")