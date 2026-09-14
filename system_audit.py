import platform
import socket
import shutil
import os


def collect_system_info():
    return {
        "Operating System": platform.system(),
        "OS Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor() or "Not reported",
        "Hostname": socket.gethostname(),
        "Python Version": platform.python_version(),
        "Disk Free (GB)": round(
            shutil.disk_usage(os.getcwd()).free / (1024 ** 3), 2
        )
    }


def check_security_basics():
    results = {}

    results["Firewall"] = (
        "Check Windows Security > Firewall & network protection"
    )

    results["Administrator/root check"] = (
        "Running with elevated privileges"
        if hasattr(os, "geteuid") and os.geteuid() == 0
        else "Standard user / Windows privilege status should be checked manually"
    )

    results["Python security"] = "Keep Python and packages updated"

    return results