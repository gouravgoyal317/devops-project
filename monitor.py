import psutil
import subprocess

def cpu_check():
    cpu = psutil.cpu_percent(interval=1)
    print("CPu Usage:", cpu,"%")

def memory_check():
    memory = psutil.virtual_memory().percent
    print("Memory Usage:", memory,"%")

def disk_check():
    disk = psutil.disk_usage('/').percent
    print("Disk Usage:", disk, "%")

def docker_check():
    print("\nRunning Docker Containers:")
    subprocess.run(["docker","ps"])

def alert_check():
    cpu = psutil.cpu_percent()
    if cpu > 80:
        print("ALERT: High CPU usage")

if __name__ == "__main__":
    print("Server Monitoring Tool\n")
    cpu_check()
    memory_check()
    disk_check()
    docker_check()
    alert_check()
