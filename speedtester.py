import speedtest
import time
import sys
from colorama import init, Fore, Style

init(autoreset=True)

def progress_bar(value, max_value=1000, bar_length=40, color=Fore.GREEN):
    progress = int((value / max_value) * bar_length)
    bar = f"{color}[{'#' * progress}{'.' * (bar_length - progress)}]{Style.RESET_ALL}"
    return bar

def run_speed_test():
    st = speedtest.Speedtest()
    st.get_best_server()

    print(Fore.YELLOW + "\nİndirme hızı test ediliyor...\n" + Style.RESET_ALL)
    download_speeds = []
    start_time = time.time()
    
    while time.time() - start_time < 15:  
        speed = st.download() / 1_000_000  
        download_speeds.append(speed)
        avg_speed = sum(download_speeds) / len(download_speeds)
        elapsed_time = time.time() - start_time
        sys.stdout.write(f"\r{progress_bar(avg_speed, color=Fore.GREEN)} {Fore.CYAN}{avg_speed:.2f} Mbps{Style.RESET_ALL} (⏳ {elapsed_time:.1f}s)")
        sys.stdout.flush()
        time.sleep(0.1) 

    print(Fore.YELLOW + "\n\nYükleme hızı test ediliyor...\n" + Style.RESET_ALL)
    upload_speeds = []
    start_time = time.time()

    while time.time() - start_time < 15:  
        speed = st.upload() / 1_000_000 
        upload_speeds.append(speed)
        avg_speed = sum(upload_speeds) / len(upload_speeds)
        elapsed_time = time.time() - start_time
        sys.stdout.write(f"\r{progress_bar(avg_speed, color=Fore.BLUE)} {Fore.CYAN}{avg_speed:.2f} Mbps{Style.RESET_ALL} (⏳ {elapsed_time:.1f}s)")
        sys.stdout.flush()
        time.sleep(0.1)

    ping = st.results.ping

    print(Fore.YELLOW + "\n\n--- 📊 İnternet Hız Testi Sonuçları ---\n" + Style.RESET_ALL)
    print(Fore.WHITE + f"⚡ Ping: {Fore.CYAN}{ping:.2f} ms")
    print(Fore.WHITE + f"⬇️ İndirme Hızı: {Fore.GREEN}{max(download_speeds):.2f} Mbps (Maks.)")
    print(Fore.WHITE + f"⬇️ İndirme Hızı: {Fore.GREEN}{sum(download_speeds)/len(download_speeds):.2f} Mbps (Ortalama)")
    print(Fore.WHITE + f"⬇️ İndirme Hızı: {Fore.GREEN}{min(download_speeds):.2f} Mbps (Minimum)")
    print(Fore.WHITE + f"⬆️ Yükleme Hızı: {Fore.BLUE}{max(upload_speeds):.2f} Mbps (Maks.)")
    print(Fore.WHITE + f"⬆️ Yükleme Hızı: {Fore.BLUE}{sum(upload_speeds)/len(upload_speeds):.2f} Mbps (Ortalama)")
    print(Fore.WHITE + f"⬆️ Yükleme Hızı: {Fore.BLUE}{min(upload_speeds):.2f} Mbps (Minimum)")

if __name__ == "__main__":
    run_speed_test()
