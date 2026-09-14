import socket


COMMON_PORTS = [
    21, 22, 23, 25, 53, 80,
    110, 135, 139, 143,
    443, 445, 3389, 8080
]


def check_local_ports(host="127.0.0.1", timeout=0.25):

    results = {}

    for port in COMMON_PORTS:

        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        sock.settimeout(timeout)

        try:

            code = sock.connect_ex(
                (host, port)
            )

            if code == 0:
                results[port] = "OPEN"
            else:
                results[port] = "CLOSED/FILTERED"

        except OSError:

            results[port] = "ERROR"

        finally:

            sock.close()

    return results