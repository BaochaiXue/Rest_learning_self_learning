#!/usr/bin/env python3
"""
scripts/check_chapter_completeness.py
Checks whether each core latex chapter contains the required textbook pedagogical components.

Required components:
1. \section{本章想回答什么问题}
2. \begin{toybox} / \section{最小例子}
3. \section{直觉解释}
4. \begin{equation} or similar math
5. \cite{...} or \citet{...}
6. \section{和前后章节的关系}
7. \begin{labbox}
8. \begin{misconceptionbox} or \section{常见误解}
9. \section{练习题} / \begin{exercise}
10. \section{本章小结}
11. 读完本章
"""

import os
import re
import sys

def check_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    filename = os.path.basename(path)
    if not filename.endswith('.tex') or not filename[0].isdigit():
        return True # Skip non-core chapters

    checks = {
        "Goal/Questions": r"本章想回答什么问题",
        "Toy Example": r"玩具问题|最小例子|\begin{toybox",
        "Intuition": r"直觉解释",
        "Math (equation)": r"\\begin\{equation\}|\\begin\{align\}|\\\[",
        "Paper Citation": r"\\cite",
        "Context/Bridges": r"和前后章节的关系",
        "Lab Assignment": r"实验|Lab |\\begin\{labbox",
        "Misconceptions": r"常见误解|\\begin\{misconceptionbox",
        "Neuroscience Analogy": r"\\begin\{neurosciencebox\}",
        "Analogy Boundary": r"\\begin\{analogyboundarybox\}",
        "Exercises": r"练习题|\\begin\{exercise\}",
        "Summary": r"小结",
        "Learning Objectives": r"读完本章|你应该能够|你现在应该会"
    }

    missing = []
    for name, pattern in checks.items():
        if not re.search(pattern, content):
            missing.append(name)
            
    if missing:
        print(f"❌ {filename} is missing: {', '.join(missing)}")
        return False
    else:
        print(f"✅ {filename} has all required components.")
        return True

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
        print("\nSome chapters are missing required pedagogical elements.")
        sys.exit(1)
    else:
        print("\nAll chapters passed completeness check!")
        sys.exit(0)

if __name__ == '__main__':
    main()
