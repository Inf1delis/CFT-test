from aiohttp import web
import asyncio
from app.utils.audio_handler import audio_spectogram


@asyncio.coroutine
def image_stft(request):
    data = yield from request.post()

    filename = data['mp3'].filename
    input_file = data['mp3'].file.read()

    image = audio_spectogram(filename, input_file)

    with open('../tmp/image.jpeg', 'wb') as file:
        file.write(image)

    return web.Response(body=image, content_type="image/jpeg")


async def get_image_stft(request):
    data = await request.post()

    for k in iter(data):
        print(f"{k}: {data[k]}")

    image = audio_spectogram("", {})

    return web.Response(body=image, content_type="image/jpeg")
