import logging
from logging import NullHandler
from logging.config import dictConfig
from .config import LOG

# Configure logs
dictConfig(LOG)
# Set default logging handler to avoid \"No handler found\" warnings.
logging.getLogger(__name__).addHandler(NullHandler())
logging.getLogger('watchfiles').setLevel(logging.WARNING)
logging.getLogger('asyncio').setLevel(logging.WARNING)
logging.getLogger('httpcore').setLevel(logging.WARNING)
