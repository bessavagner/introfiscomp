#!/bin/bash

# Process Markdown files and parse to json
pip install -r requirements.txt

# Install tailwindcss
npm install tailwindcss
npm install @tailwindcss/typography
npm install @tailwindcss/typography
npm install daisyui@latest

# build files to serve
python build.py

# Start the Tailwind CLI build process
npx tailwindcss -i ./static/css/input.css -o ./static/css/styles.css
