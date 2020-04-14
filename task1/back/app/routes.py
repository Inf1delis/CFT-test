from app.views import image_stft


def setup_routes(app):
    app.router.add_post("/image_stft", image_stft)
    app.router.add_post("/get_image_stft", image_stft)
