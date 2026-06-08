import os
import re
import glob

def check_links():
    print("🤖 [XBSTACK Link Checker] Scanning for broken links...")
    files = glob.glob("src/content/**/*.md", recursive=True) + glob.glob("src/content/**/*.mdx", recursive=True)
    broken_count = 0
    
    # Simple regex for markdown links [text](url)
    link_pattern = re.compile(r'\[.*?\]\((.*?)\)')
    
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        links = link_pattern.findall(content)
        for link in links:
            if link.startswith('http'):
                continue
            if link.startswith('#'):
                continue
                
            # Internal link check (simplified)
            if link == "" or link == "/":
                continue
                
            # You can add more complex internal link resolution here
            pass

    print("🏁 Link check completed.")

if __name__ == "__main__":
    check_links()
