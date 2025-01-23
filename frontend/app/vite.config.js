import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    host: true,
    proxy:{
      '/upload' :{
        target: 'http://127.0.0.1:5000',
        changeOrigin: true,
      },
      '/image': {
        target: 'http://127.0.0.1:5000',
        changeOrigin: true,
      },
    },
    allowedHosts: [
      '.ngrok-free.app',
    ]
  },
})
