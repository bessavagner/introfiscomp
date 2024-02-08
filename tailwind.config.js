/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./static/**/*.{html,.js,css}", "./templates/**/*.{html,.js,css}"],
  theme: {
    extend: {
      boxShadow: {
        '3xl': '0 10px 15px 10px rgba(0, 0, 0, 0.3)',
      }
    },
  },
  daisyui: {
    themes: ["light", "dark", "cupcake"],
  },
  plugins: [
    require('@tailwindcss/typography'),
    require("daisyui"),
  ],
  
}

