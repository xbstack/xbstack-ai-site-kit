# Deployment

## Cloudflare Pages

1. Connect your GitHub repository
2. Set build command: `npm run build`
3. Set output directory: `dist`
4. Set Node.js version: `20`

## Vercel / Netlify

1. Connect your GitHub repository
2. The platform should automatically detect the Astro framework.
3. Build command: `npm run build`
4. Output directory: `dist`

## Environment Variables

Do not commit `.env` files. Ensure you set any required API keys directly in the hosting platform's environment variable settings.

## Production Build

```bash
npm install
npm run build
```