import threading
import urllib.request
#import threading
import requests
#from urllib.parse import urlparse

urls = [
    "https://example.com",
    "https://www.python.org",
    "https://www.wikipedia.org"
]

def fetch_url_content(url):
    # TODO: Download content and return first 100 characters as string
    #parsed_url = urlparse(url)
    #filename = parsed_url.path.split('/')[-1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        raw = response.read(1024)

    text = raw.decode("utf-8", errors="replace")
    return text[:100]

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
