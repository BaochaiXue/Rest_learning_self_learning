#!/usr/bin/env python3
"""
Extended chapter quality check script.
Checks: depth, structural elements, rhetorical heuristics.
"""

import os
import re
import sys

CHAPTERS_DIR = os.path.join(os.path.dirname(__file__), '..', 'book', 'chapters')

REQUIRED_ELEMENTS = {
    'toybox': r'\\begin\{toybox\}',
    'insight_or_example': r'\\begin\{(insight|example)\}',
    'theorem_or_definition': r'\\begin\{(theorem|definition)\}',
    'misconceptionbox': r'\\begin\{misconceptionbox\}',
    'neurosciencebox': r'\\begin\{neurosciencebox\}',
    'analogyboundarybox': r'\\begin\{analogyboundarybox\}',
    'labbox': r'\\begin\{labbox\}',
    'exercises': r'\\begin\{exercise\}',
}

# Chapters that must have theorem/definition (not intro/bridge chapters)
THEOREM_REQUIRED = [
    '03_bilevel', '05_attention', '06_is_in_context',
    '10_test_time', '11_nested',
]

# Heuristic: too many exclamation marks in mainline suggests rhetorical excess
RHETORIC_THRESHOLD = 10  # max exclamation marks outside boxes


def count_chinese_chars(text):
    return len(re.findall(r'[\u4e00-\u9fff]', text))


def count_pattern(text, pattern):
    return len(re.findall(pattern, text))


def check_rhetoric(text):
    """Check for rhetorical excess heuristics."""
    issues = []
    
    # Remove box environments for the check (rhetoric in boxes is OK)
    cleaned = re.sub(
        r'\\begin\{(toybox|insight|neurosciencebox|analogyboundarybox|viewpointbox)\}.*?\\end\{\1\}',
        '', text, flags=re.DOTALL
    )
    
    # Count exclamation marks in mainline
    excl_count = cleaned.count('！') + cleaned.count('!')
    if excl_count > RHETORIC_THRESHOLD:
        issues.append(f'  ⚠️  {excl_count} exclamation marks in mainline (threshold: {RHETORIC_THRESHOLD})')
    
    return issues


def check_chapter(filepath):
    """Check a single chapter file."""
    basename = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.count('\n') + 1
    chinese_count = count_chinese_chars(content)
    
    results = {
        'file': basename,
        'lines': lines,
        'chinese_chars': chinese_count,
        'elements': {},
        'rhetoric_issues': [],
        'passed': True,
        'issues': [],
    }
    
    # Check structural elements
    for name, pattern in REQUIRED_ELEMENTS.items():
        count = count_pattern(content, pattern)
        results['elements'][name] = count
        if count == 0:
            if name in ('theorem_or_definition',):
                # Only required for certain chapters
                stem = basename.split('.')[0]
                if any(stem.startswith(t) for t in THEOREM_REQUIRED):
                    results['issues'].append(f'  ❌ Missing {name}')
                    results['passed'] = False
            elif name in ('neurosciencebox', 'analogyboundarybox'):
                results['issues'].append(f'  ❌ Missing {name}')
                results['passed'] = False
    
    # Check depth
    min_chars = 3500 if chinese_count > 2000 else 2500
    if chinese_count < min_chars:
        results['issues'].append(f'  ❌ DEPTH: {chinese_count} / {min_chars} Chinese chars')
        results['passed'] = False
    
    # Check rhetoric
    results['rhetoric_issues'] = check_rhetoric(content)
    
    return results


def main():
    chapters = sorted([
        os.path.join(CHAPTERS_DIR, f) for f in os.listdir(CHAPTERS_DIR)
        if f.endswith('.tex')
    ])
    
    all_results = []
    all_passed = True
    
    for ch in chapters:
        result = check_chapter(ch)
        all_results.append(result)
        if not result['passed']:
            all_passed = False
    
    # Print summary
    print('=' * 70)
    print('CHAPTER QUALITY REPORT')
    print('=' * 70)
    
    for r in all_results:
        status = '✅' if r['passed'] else '❌'
        print(f"\n{status} {r['file']} ({r['lines']} lines, {r['chinese_chars']} 中文字)")
        
        # Element summary
        elems = []
        for name, count in r['elements'].items():
            symbol = '✓' if count > 0 else '✗'
            elems.append(f'{symbol}{name}({count})')
        print(f'  Elements: {", ".join(elems)}')
        
        for issue in r['issues']:
            print(issue)
        for issue in r['rhetoric_issues']:
            print(issue)
    
    print('\n' + '=' * 70)
    if all_passed:
        print('All chapters passed quality check!')
    else:
        print('Some chapters have issues.')
        sys.exit(1)
    
    # Generate markdown report
    report_dir = os.path.join(os.path.dirname(__file__), '..', 'docs', 'generated')
    os.makedirs(report_dir, exist_ok=True)
    
    report_path = os.path.join(report_dir, 'chapter_depth_report.md')
    with open(report_path, 'w') as f:
        f.write('# Chapter Depth & Quality Report\n\n')
        f.write(f'**Generated**: {__import__("datetime").datetime.now().strftime("%Y-%m-%d %H:%M")}\n\n')
        f.write('| Chapter | Lines | 中文字 | Toy | Thm/Def | Neuro | Boundary | Lab | Exercises | Status |\n')
        f.write('|---|---|---|---|---|---|---|---|---|---|\n')
        for r in all_results:
            e = r['elements']
            status = '✅' if r['passed'] else '❌'
            f.write(f"| {r['file'][:30]} | {r['lines']} | {r['chinese_chars']} "
                    f"| {e.get('toybox', 0)} | {e.get('theorem_or_definition', 0)} "
                    f"| {e.get('neurosciencebox', 0)} | {e.get('analogyboundarybox', 0)} "
                    f"| {e.get('labbox', 0)} | {e.get('exercises', 0)} | {status} |\n")
    
    print(f'\nReport written to: {report_path}')


if __name__ == '__main__':
    main()
