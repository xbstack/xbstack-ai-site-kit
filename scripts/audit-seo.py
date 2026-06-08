import os
import re
import glob

# SEO Validation Config
REQUIRED_FRONTMATTER = ['title', 'description', 'date', 'category']
CATEGORY_ENUM = ['ai', 'dev', 'gear', 'reading', 'investing', 'finance', 'log', 'outdoor', 'notes']

def audit_posts():
    print("🔍 [XBSTACK SEO Auditor] Starting quality audit...")
    files = glob.glob("src/content/**/*.md", recursive=True) + glob.glob("src/content/**/*.mdx", recursive=True)
    errors = 0
    slugs = set()
    
    for file in files:
        if "_" in os.path.basename(file): continue # Ignore private files
        
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        filename = os.path.basename(file)
        slug = filename.split('.')[0]
        
        # 1. Slug Uniqueness
        if slug in slugs:
            print(f"❌ [Slug Conflict] {file}: Duplicate filename detected!")
            errors += 1
        slugs.add(slug)
        
        # 2. Frontmatter Validation
        for field in REQUIRED_FRONTMATTER:
            if not re.search(fr'{field}:', content):
                print(f"❌ [Metadata Missing] {file}: Missing '{field}' field.")
                errors += 1
        
        # 3. Category Validation
        cat_match = re.search(r'category:\s*["\']?([a-zA-Z]+)["\']?', content)
        if cat_match:
            cat = cat_match.group(1)
            if cat not in CATEGORY_ENUM:
                print(f"⚠️ [Category Warning] {file}: '{cat}' is not in the standard enum.")
        
        # 4. SEO Suggestion: English in Title
        h1_match = re.search(r'^#\s+(.*)', content, re.MULTILINE)
        if h1_match:
            h1 = h1_match.group(1)
            if not any(ord(char) < 128 for char in h1):
                print(f"💡 [SEO Tip] {file}: Consider adding English keywords to the title.")

    if errors == 0:
        print("\n✅ Audit passed! Your content structure is solid.")
    else:
        print(f"\n🚨 Audit failed! Found {errors} critical errors.")

if __name__ == "__main__":
    audit_posts()
