#!/bin/bash

# Process Markdown files and parse to json
python build.py
# Install tailwindcss
npm install -D tailwindcss
npm install -D @tailwindcss/typography
npm install -D @tailwindcss/typography
npm i -D daisyui@latest
# Start the Tailwind CLI build process
npx tailwindcss -i ./static/css/input.css -o ./static/css/styles.css
