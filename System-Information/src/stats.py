import psutil

def get_system_stats():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage('/')
    network_info = psutil.net_io_counters()

    return {
        "cpu_usage": cpu_usage,
        "memory_total": memory_info.total,
        "memory_used": memory_info.used,
        "memory_free": memory_info.free,
        "disk_total": disk_info.total,
        "disk_used": disk_info.used,
        "disk_free": disk_info.free,
        "network_sent": network_info.bytes_sent,
        "network_received": network_info.bytes_recv
    }
