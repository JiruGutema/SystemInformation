import time
from rich.console import Console
from rich.table import Table
from rich.live import Live
from rich.align import Align
from src.stats import get_system_stats
from src.process import get_process_info
from src.display import create_system_table, create_process_table

console = Console()

def run_monitor():
    with Live(console=console, refresh_per_second=1) as live:
        while True:
            system_stats = get_system_stats()
            processes = get_process_info()

            system_table = create_system_table(system_stats)
            process_table = create_process_table(processes)

            grid = Table.grid(padding=1)
            grid.add_row(
                Align.center(system_table, vertical="middle"),
                Align.center(process_table, vertical="middle")
            )

            live.update(grid)
            time.sleep(1)
