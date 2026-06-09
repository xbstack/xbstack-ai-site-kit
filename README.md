# XBSTACK AI Site Kit

## Project Status

XBSTACK AI Site Kit is an early-stage open-source starter kit. The current version focuses on the foundation: Astro structure, content schema, SEO conventions, deployment workflow, and maintainer automation. More templates and automation scripts are planned.

An open-source Astro starter kit for AI engineers, indie developers, and technical creators.

## Architecture

```text
src/
  components/
  layouts/
  pages/
  content/
scripts/
docs/
.github/
```

## Why this project exists

Technical creators need more than a blog. They need a fast, SEO-friendly, AI-native publishing system that can support articles, tool pages, project pages, newsletters, and structured content workflows.

XBSTACK AI Site Kit provides a reusable Astro-based foundation for building developer-oriented content platforms.

## Features

- **Astro 5** content-driven architecture
- **SEO-ready** metadata system
- **AI / Tools / Investing / Lens** content taxonomy
- **Tool landing page** templates
- **RSS and sitemap** support
- **Cloudflare Pages** deployment
- **Content frontmatter** validation
- **Basic internal link** validation
- **AI-assisted** maintainer workflows

## Use cases

- AI engineer personal sites
- Indie developer project sites
- Technical blogs
- Tool directories
- SEO content hubs
- Open-source documentation sites

## Quick Start

```bash
git clone https://github.com/xbstack/xbstack-ai-site-kit.git
cd xbstack-ai-site-kit
npm install
npm run dev
```

## Deployment

```bash
npm run build
```

Deploy the `dist/` directory to Cloudflare Pages, Vercel, Netlify, or any static hosting platform.

## Maintainer Workflows

This project is designed to use **Codex** for:

* Pull request review
* SEO metadata auditing
* Broken link fixing
* Component refactoring
* Content schema validation
* Release note generation
* Security review

## Roadmap

See [ROADMAP.md](./ROADMAP.md).

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md).

## License

MIT
