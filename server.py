import uvicorn

from app import LOG
from app.settings import (
    APP_DIR,
    APP_NAME,
    APP_PORT,
    HOST,
    DEBUG
)

RELOAD = True
RELOAD_INCLUDES = [
    "templates/*.html",
    "templates/**/*.html",
    "static/css/*.css",
    "static/**/*",
    "static/**/**/*",
]

if not DEBUG:
    RELOAD = False
    RELOAD_INCLUDES = None


def run():
    uvicorn.run(
        app=APP_NAME,
        port=APP_PORT,
        app_dir=APP_DIR,
        host=HOST,
        reload=DEBUG,
        reload_includes=RELOAD_INCLUDES,
        log_level='info',
    )


if __name__ == '__main__':
    run()
