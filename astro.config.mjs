import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'http://localhost:3000',
  integrations: [],
  build: {
    outDir: 'dist',
  },
  server: {
    port: 3000,
  },
  css: {
    preprocessorOptions: {
      scss: {
        additionalData: `@import "src/styles/global.scss";`
      }
    }
  }
});
