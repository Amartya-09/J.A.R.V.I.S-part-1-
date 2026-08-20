import socket

def is_online(host="8.8.8.8", port=53, timeout=1.5) -> bool:
    """Checks for active internet connectivity via DNS probe."""
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except (socket.timeout, Exception):
        return False