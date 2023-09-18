import socks, socket
from stem.process import launch_tor

def start_tor_proxy():
    # launches tor in background using default settings
    print("[*] Starting tor in background..")
    tor_process = launch_tor()
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 9050)
    socket.socket = socks.socksocket
    print("[*] Tor bootstrapped 100%\n")
    return tor_process