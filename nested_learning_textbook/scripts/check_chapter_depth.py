#!/usr/bin/env python3
"""
scripts/check_chapter_depth.py
Heuristic check for the pedagogical depth of the textbook chapters.
Ensures chapters have enough text density, not just bullet points or bare equations.
"""

import os
import re
import sys

def count_chinese_chars(text):
    return len(re.findall(r'[\u4e00-\u9fff]', text))

def check_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    filename = os.path.basename(path)
    if not filename.endswith('.tex') or not filename[0].isdigit():
        return True

    # Check length
    # Strip comments
    content_no_comments = re.sub(r'%.*?$', '', content, flags=re.MULTILINE)
    
    num_chars = count_chinese_chars(content_no_comments)
    
    # Bridge chapters (5, 6, 7, 8, 10, 11) require more depth
    heavy_chapters = ['05', '06', '07', '08', '10', '11']
    prefix = filename[:2]
    
    required_len = 2500 if prefix not in heavy_chapters else 3500
    
    # Alert words checking
    alert_words = [r"细节略", r"见原论文", r"见原文", r"读者自行参考"]
    alerts_found = []
    for aw in alert_words:
        if re.search(aw, content_no_comments):
            alerts_found.append(aw)
            
    is_pass = True
    print(f"\n--- {filename} ---")
    print(f"Chinese character count: {num_chars} / {required_len} required")
    
    if num_chars < required_len:
        print(f"❌ FAILED DEPTH: Chapter is too short. It looks like an extended outline.")
        is_pass = False
        
    if alerts_found:
        print(f"❌ FAILED SELF-CONTAINEDNESS: Found stop-words: {', '.join(alerts_found)}")
        is_pass = False

    if is_pass:
        print(f"✅ PASSED tests.")
        
    return is_pass

def main():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    chap_dir = os.path.join(root_dir, 'book', 'chapters')
    
    if not os.path.exists(chap_dir):
        print(f"Error: {chap_dir} not found.")
        sys.exit(1)
        
    all_passed = True
    for f in sorted(os.listdir(chap_dir)):
        if f.endswith('.tex') and f[0].isdigit():
            passed = check_file(os.path.join(chap_dir, f))
            if not passed:
                all_passed = False
                
    if not all_passed:
        print("\nSome chapters failed the pedagogical depth check. Please expand the explanatory prose.")
        sys.exit(1)
    else:
        print("\nAll chapters passed depth check!")
        sys.exit(0)

if __name__ == '__main__':
    main()
