/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: "class",
  content: ["./*.html"],
  theme: {
    extend: {
      colors: {
        primary: "#ea580c",
        "primary-hover": "#c2410c",
        "background-dark": "#0f172a",
        "surface-dark": "#1e293b",
        "surface-darker": "#020617",
        "text-main": "#f1f5f9",
        "text-muted": "#94a3b8",
        "border-tech": "#334155",
      },
      fontFamily: {
        display: ["Oswald", "sans-serif"],
        "mono-tech": ["Teko", "sans-serif"],
        body: ["Inter", "sans-serif"],
      },
      borderRadius: {
        DEFAULT: "0px",
        md: "2px",
        lg: "4px",
        xl: "4px",
        full: "9999px",
      },
      backgroundImage: {
        grain:
          "url('data:image/svg+xml,%3Csvg viewBox=%220 0 200 200%22 xmlns=%22http://www.w3.org/2000/svg%22%3E%3Cfilter id=%22noiseFilter%22%3E%3CfeTurbulence type=%22fractalNoise%22 baseFrequency=%2210.5%22 numOctaves=%223%22 stitchTiles=%22stitch%22/%3E%3C/filter%3E%3Crect width=%22100%25%22 height=%22100%25%22 filter=%22url(%23noiseFilter)%22 opacity=%220.5%22/%3E%3C/svg%3E')",
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/container-queries')
  ],
};
