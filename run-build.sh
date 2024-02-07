#!/bin/bash

# Process Markdown files and parse to json
pip install -r requirements.txt
python build.py
# Install tailwindcss
npm install tailwindcss
npm install @tailwindcss/typography
npm install @tailwindcss/typography
npm install daisyui@latest
# Start the Tailwind CLI build process
npx tailwindcss -i ./static/css/input.css -o ./static/css/styles.css
