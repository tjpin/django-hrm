/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "../../templates/**/*.{html, js}",
    "../../static/**/*.{html, js}",
  ],
  theme: {
    extend: {
      colors: {
        mainCyan: "#056381",
        mainText: "#4b5563",
        primary:'#1694A4',
				accent: '#1AADC0',
				hg: '#F3F3F3',
				mg: "#1FC20B",
      }
    },
  },
  plugins: [
    require('tailwind-scrollbar'),
  ],
}


// npx tailwindcss -i input.css -o style.css --watch