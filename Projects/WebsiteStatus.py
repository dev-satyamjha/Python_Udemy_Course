import requests
from requests import Response

def normalise_url(url: str) -> None:
    return url if url.startswith(('http://', 'https://')) else f'https://{url}'

def check_website(url:str, timeout: int = 10):
    url = normalise_url(url)
    print(f"== Website Diagnostics for '{url}' ==")

    try:
        response: Response = requests.get(url, timeout = timeout)
    except Exception as e:
        print(f"Error: {e}")
        return

    status_code : int = response.status_code
    elapsed_time: int = response.elapsed.total_seconds()
    reason: str = response.reason
    content_type: str = response.headers.get('Content-Type', '')
    encoding: str | None = response.encoding
    headers: dict[str | str] = dict(response.headers)

    print(f'Status Code : {status_code} ({reason})')
    print(f'Elapsed Time : {elapsed_time}s')
    print(f'Content-Type: {content_type}')
    print(f'Encoding : {encoding or 'n/a'}')
    print('Headers:    ')

    for key, value in headers.items():
        print(f'    . {key}: {value}')

check_website('satyamjha.is-a.dev')
