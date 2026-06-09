import os
import re
import sys

def check_links_in_file(file_path, base_dir):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all Markdown links [text](link)
    links = re.findall(r'\[.*?\]\((.*?)\)', content)
    errors = []

    for link in links:
        # Skip external links
        if link.startswith('http') or link.startswith('mailto:'):
            continue
        
        # Skip anchors
        if link.startswith('#'):
            continue

        # Handle relative paths
        # Remove query params or fragments
        clean_link = link.split('?')[0].split('#')[0]
        
        if not clean_link:
            continue

        # Check if the linked file or directory exists
        target_path = os.path.normpath(os.path.join(os.path.dirname(file_path), clean_link))
        
        if not os.path.exists(target_path):
            # Special case for Astro: links to .md often become directory/index.html
            # Or links might omit extensions
            possible_paths = [
                target_path + '.md',
                target_path + '.mdx',
                os.path.join(target_path, 'index.md'),
                os.path.join(target_path, 'index.mdx')
            ]
            if not any(os.path.exists(p) for p in possible_paths):
                errors.append(f"Broken link: '{link}' in {file_path}")

    return errors

def main():
    base_dir = '.'
    content_dir = os.path.join(base_dir, 'src', 'content')
    docs_dir = os.path.join(base_dir, 'docs')
    
    all_errors = []
    
    # Check all .md and .mdx files
    for root, _, files in os.walk(base_dir):
        if 'node_modules' in root or '.git' in root or 'dist' in root:
            continue
        for file in files:
            if file.endswith(('.md', '.mdx')):
                file_path = os.path.join(root, file)
                all_errors.extend(check_links_in_file(file_path, base_dir))

    if all_errors:
        for error in all_errors:
            print(error)
        sys.exit(1)
    else:
        print("✅ All internal links verified.")
        sys.exit(0)

if __name__ == "__main__":
    main()
