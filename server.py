import os
# from dotenv import load_dotenv
import uvicorn

# load_dotenv()  # Loads variables from .env file

APP_NAME = os.getenv("APP_NAME", default="app")
APP_DIR = os.getenv("APP_DIR", default=".")
APP_PORT = int(os.getenv("APP_PORT", default="5000"))
ALLOWED_HOSTS = os.getenv(
    "ALLOWED_HOSTS", default="localhost,0.0.0.0"
).split(',')
HOST = ALLOWED_HOSTS[1]

if __name__ == '__main__':
    uvicorn.run(
        app=f"{APP_NAME}:asgi_flask_app",
        port=APP_PORT,
        app_dir=APP_DIR,
        host=HOST,
        reload=True,
        reload_includes=[
            "templates/*.html",
            "templates/**/*.html",
            "static/css/*.css",
            "static/**/*",
            "static/**/**/*",
        ]
    )
