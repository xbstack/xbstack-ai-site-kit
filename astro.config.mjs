import mdx from "@astrojs/mdx";
import react from "@astrojs/react";
import tailwind from "@astrojs/tailwind";
import sitemap from "@astrojs/sitemap";
import AutoImport from "astro-auto-import";
import { defineConfig } from "astro/config";
import remarkGfm from "remark-gfm";
import { fileURLToPath, URL } from "node:url";

export default defineConfig({
  site: "https://your-site.com",
  base: "/",
  trailingSlash: "ignore",
  output: "static",
  build: {
    format: 'directory',
    assets: "_astro",
  },
  vite: {
    resolve: {
      alias: {
        "@": fileURLToPath(new URL("./src", import.meta.url)),
        "@components": fileURLToPath(new URL("./src/components", import.meta.url)),
        "@layouts": fileURLToPath(new URL("./src/layouts", import.meta.url)),
        "@assets": fileURLToPath(new URL("./src/assets", import.meta.url)),
        "@styles": fileURLToPath(new URL("./src/styles", import.meta.url)),
        "@data": fileURLToPath(new URL("./src/data", import.meta.url)),
        "@utils": fileURLToPath(new URL("./src/utils", import.meta.url)),
      }
    }
  },
  integrations: [
    react(),
    tailwind({ applyBaseStyles: false }),
    AutoImport({
      imports: [
        "@components/common/Button.astro",
      ]
    }),
    mdx(),
    sitemap({
      filter: (page) => 
        !page.includes('/404') &&
        !page.includes('/api')
    })
  ],
  markdown: {
    remarkPlugins: [remarkGfm],
    shikiConfig: {
      themes: { light: "github-light", dark: "github-dark-dimmed" } 
    }
  },
});
