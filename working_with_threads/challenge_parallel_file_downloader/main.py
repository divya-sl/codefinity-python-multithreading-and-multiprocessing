import threading
import requests
from urllib.parse import urlparse

def download_file(url):
    parsed_url = urlparse(url)
    filename = parsed_url.path.split('/')[-1]
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)
    print(f"Downloaded {filename}")

def parallel_download(urls):
    # Your code here
    threads = []
    for url in urls:
        #print(url)
        t = threading.Thread(target=download_file, args=(url,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

# Example usage:
urls = [
    "https://example.com/file1.txt",
    "https://example.com/file2.txt"
]
parallel_download(urls)
