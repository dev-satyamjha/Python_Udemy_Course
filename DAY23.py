import asyncio
from asyncio import Task, TimeoutError

#AsyncIO

async def download(file:str):
    print(f"{file} is downloading...")
    await asyncio.sleep(2)
    print(f"{file} is downloaded..!!")



# Tasks
async def image_dl(name:str, delay:int) ->str:
    print(f"{name} is downloading...")
    await asyncio.sleep(delay)
    print(f"{name} is downloaded..!!")
    return name

# Gather

async def image(name:str, delay:int, fail:bool) ->str:
    print(f"{name} is downloading...")
    await asyncio.sleep(delay)

    if fail:
        raise Exception(f"{name} downloading failed..")
    else:
        print(f"{name} is downloaded..!!")
        return name


async def main():
    await asyncio.gather(
    download('File1'),
    download('File2'),
    download('File3')
    )
    print('-'* 30)
    print("Starting both tasks...")
    cat_task: Task[str] = asyncio.create_task(image_dl('cat.png', 15))
    dog_task: Task[str] = asyncio.create_task(image_dl('dog.jpg', 2))
    await asyncio.sleep(2)
    print("Running code while tasks are retrieving the data..")

    try:
        cat_result: str | None = await asyncio.wait_for(cat_task, 5)
        print("Cat image retrieved..")
    except TimeoutError:
        print("Cat image is taking too long to download, skipping..")
        cat_result = None

    dog_result: str = await dog_task
    print("Dog image retrieved..")

    print(f"Downloaded images : [{cat_result}, {dog_result}]")
    print('-'* 40)

    results = await asyncio.gather(
        image('cat.png', 3, False),
        image('dog.png', 2, True),
        image('horse.jpg', 1, False),
        return_exceptions = True
    )

    print(f"Downloaded images : {results}")

if __name__== '__main__':
    asyncio.run(main())
