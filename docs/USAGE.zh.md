# 使用教程

欢迎使用 XBSTACK AI Site Kit。本指南将帮助你快速构建并维护你的内容平台。

## 1. 项目初始化

克隆仓库并安装依赖：

```bash
git clone https://github.com/xbstack/xbstack-ai-site-kit.git
cd xbstack-ai-site-kit
npm install
```

## 2. 本地开发

启动带热重载的开发服务器：

```bash
npm run dev
```

访问 `http://localhost:4321` 预览你的网站。

## 3. 内容管理

所有的文章都存放在 `src/content/articles/` 目录下。

### 创建新文章

创建一个新的 Markdown 或 MDX 文件，并包含以下 Frontmatter 配置：

```markdown
---
title: "你的文章标题"
description: "用于 SEO 的简短摘要"
date: 2026-06-09
category: "ai"
tags: ["入门", "教程"]
lang: "zh"
author: "你的名字"
---
```

## 4. SEO 与质量审计

在发布之前，运行自动化的审计脚本：

### SEO 审计
检查标题长度、描述长度以及必需的元数据：
```bash
npm run audit:seo
```

### 链接校验
检查死链及内部文件路径引用：
```bash
npm run check:links
```

## 5. 部署指南

执行静态构建：

```bash
npm run build
```

将生成的 `dist/` 目录部署到 **Cloudflare Pages**、**Vercel** 或 **Netlify**。

---

[切换到英文版 (English Version)](./USAGE.md)
