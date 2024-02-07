#!/bin/bash

# Start the Tailwind CSS build process
npx tailwindcss -i ./static/css/input.css -o ./static/css/styles.css
npx tailwindcss -o ./static/css/styles.css --minify

# Start the Python server
python server.py &
