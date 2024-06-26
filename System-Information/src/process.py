import psutil

def get_process_info():
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            processes.append(proc.info)
        except psutil.NoSuchProcess:
            pass
    return sorted(processes, key=lambda p: p['cpu_percent'], reverse=True)[:10]
