import logging

# Create a logger object
graphics_logger = logging.getLogger('graphics_logger')

# Optionally set the level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
graphics_logger.setLevel(logging.DEBUG)

# Create a handler (console handler, file handler, etc.)
handler = logging.StreamHandler()  # Console handler
handler.setLevel(logging.DEBUG)

# Create a formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Add the formatter to the handler
handler.setFormatter(formatter)

# Add the handler to the logger
graphics_logger.addHandler(handler)