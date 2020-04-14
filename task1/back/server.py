from aiohttp import web
import aiohttp_cors
from app.views import image_stft, get_image_stft
from app.routes import setup_routes


def main():

    app = web.Application(client_max_size=1024**3)

    cors = aiohttp_cors.setup(app)
    cors.add(
        app.router.add_route("POST", "/image_stft", image_stft),
        {
            "*": aiohttp_cors.ResourceOptions(
                allow_credentials=True, expose_headers="*", allow_headers="*"
            ),
        },
    )

    cors.add(
        app.router.add_route("GET", "/get_image_stft", get_image_stft),
        {
            "*": aiohttp_cors.ResourceOptions(
                allow_credentials=True, expose_headers="*", allow_headers="*"
            ),
        },
    )

    # setup_routes(app)
    web.run_app(app, host="0.0.0.0", port=8001)

if __name__ == "__main__":
    main()
