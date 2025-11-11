import ipaddress


def is_valid_ip(ip: str) -> bool:
    if not ip or not ip.strip():
        return False
    try:
        ipaddress.ip_address(ip.strip())
        return True
    except ValueError:
        return False
