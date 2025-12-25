import asyncio
from asyncio import TimeoutError
import requests
from requests import Response
from dataclasses import dataclass

@dataclass
class WebsiteResponse:
    url:str
    status : int | None
    reason: str

async def check_website(url:str) ->WebsiteResponse:
    if not url.startswith(('http://', 'https://')):
        url = f'http://{url}'

    try:
        response: Response = await asyncio.to_thread(requests.get,url)
        return WebsiteResponse(url, response.status_code, response.reason)
    except Exception as e:
        return WebsiteResponse(url, None, str(e))

async def check_websites(urls:list[str], timeout: float = 5):
    tasks =[check_website(url) for url in urls]

    try:
        for completed_task in asyncio.as_completed(tasks, timeout=timeout):
            response: WebsiteResponse = await completed_task

            if response.status is not None:
                print(f"{response.url} ONLINE ({response.status}, {response.reason})")
            else:
                print(f"{response.url} information cannot be retrieved..!!")

    except TimeoutError:
        print("Timeout error occurred for some websites...")

async def main() -> None:
    urls: list[str] = [
        'www.indently.io',
        'www.apple.com',
        'www.facebook.com',
        'nonexistent-website-404.com',
        'www.instagram.com',
        'www.reddit.com',
        'www.wikipedia.org',
        'www.fail-website.com',
        'www.amazon.com',
        'www.linkedin.com',
        'www.microsoft.com',
        'www.github.com',
    ]

    print(f"Checking {len(urls)} wesbites..")
    await check_websites(urls)
    print("Done!")

if __name__ == '__main__':
    asyncio.run(main())
