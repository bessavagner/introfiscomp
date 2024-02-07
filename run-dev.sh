#!/bin/bash

# Process Markdown files and parse to json
python build.py
# Start the Python server
python server.py &
# Start the Tailwind CSS watcher
npx tailwindcss -i ./static/css/input.css -o ./static/css/styles.css --watch
