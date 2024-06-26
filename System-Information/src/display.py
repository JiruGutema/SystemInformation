from rich.table import Table
import psutil
from rich import box

def create_system_table(stats):
    table = Table(title="System Monitor", box=box.ROUNDED)  # Updated this line

    table.add_column("Metric", justify="right", style="cyan", no_wrap=True)
    table.add_column("Value", justify="right", style="magenta")

    table.add_row("CPU Usage", f"{stats['cpu_usage']}%")
    table.add_row("Memory Used", f"{psutil._common.bytes2human(stats['memory_used'])}/{psutil._common.bytes2human(stats['memory_total'])} ({stats['memory_used'] / stats['memory_total'] * 100:.2f}%)")
    table.add_row("Disk Used", f"{psutil._common.bytes2human(stats['disk_used'])}/{psutil._common.bytes2human(stats['disk_total'])} ({stats['disk_used'] / stats['disk_total'] * 100:.2f}%)")
    table.add_row("Network Sent", psutil._common.bytes2human(stats['network_sent']))
    table.add_row("Network Received", psutil._common.bytes2human(stats['network_received']))

    return table

def create_process_table(processes):
    table = Table(title="Top Processes", box=box.ROUNDED)  # Updated this line

    table.add_column("PID", justify="right", style="cyan", no_wrap=True)
    table.add_column("Name", justify="right", style="magenta")
    table.add_column("CPU %", justify="right", style="green")
    table.add_column("Memory %", justify="right", style="red")

    for proc in processes:
        table.add_row(str(proc['pid']), proc['name'], f"{proc['cpu_percent']}%", f"{proc['memory_percent']:.2f}%")

    return table
