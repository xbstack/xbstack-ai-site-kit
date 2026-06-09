import { defineCollection, z } from 'astro:content';

const articles = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    date: z.date(),
    updatedDate: z.date().optional(),
    category: z.enum(['ai', 'tools', 'dev', 'outdoor', 'gear', 'reading', 'investing', 'notes']),
    tags: z.array(z.string()).default([]),
    draft: z.boolean().default(false),
    featured: z.boolean().default(false),
    canonical: z.string().url().optional(),
    ogImage: z.string().optional(),
    lang: z.enum(['en', 'zh']).default('en'),
    author: z.string().default('XBSTACK'),
  }),
});

export const collections = {
  articles,
};
