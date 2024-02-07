/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./static/**/*.{html,.js,css}", "./templates/**/*.{html,.js,css}"],
  theme: {
    extend: {},
  },
  daisyui: {
    themes: ["light", "dark", "cupcake"],
  },
  plugins: [
    require('@tailwindcss/typography'),
    require("daisyui"),
  ],
  
}

