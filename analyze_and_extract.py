import glob
import re
import json

def analyze_html():
    for f in sorted(glob.glob('DISM_Examen/*.html')):
        with open(f, 'r', encoding='utf-8') as fh:
            text = fh.read()
        print('=== ' + f + ' ===')
        
        # Check variable declarations
        matches = re.findall(r'(const|let|var)\s+(\w+)\s*=\s*\[', text)
        print("  Arrays found:", matches)

if __name__ == '__main__':
    analyze_html()
