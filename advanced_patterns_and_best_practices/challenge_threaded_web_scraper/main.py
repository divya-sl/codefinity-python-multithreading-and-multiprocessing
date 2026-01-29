import threading
import urllib.request

urls = [
    "https://example.com",
    "https://www.python.org",
    "https://www.wikipedia.org"
]

def fetch_url_content(url):
    # TODO: Download content and return first 100 characters as string
    request.

def main():
    threads = []
    for url in urls:
        thread = threading.Thread(
            target=lambda u: print(f"Content from {u}: {fetch_url_content(u)}"),
            args=(url,)
        )
        threads.append(thread)
        thread.start()
        
    # TODO: Wait for all threads to finish
    for t in threads:
        t.join()

main()
