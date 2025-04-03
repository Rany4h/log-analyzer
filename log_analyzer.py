import re
from collections import Counter

# Define the log file name
log_file = "syslog.txt"

# Regex pattern for failed login attempts
failed_login_pattern = r"Failed password for .* from (\d+\.\d+\.\d+\.\d+)"

# Read log file
with open(log_file, "r") as file:
    logs = file.readlines()

# Extract failed login attempts
failed_ips = [re.search(failed_login_pattern, log).group(1) for log in logs if re.search(failed_login_pattern, log)]

# Count occurrences of each IP
ip_counts = Counter(failed_ips)

# Print the top offenders
print("🚨 Detected Failed Login Attempts 🚨")
for ip, count in ip_counts.most_common():
    print(f"{ip} - {count} attempts")
