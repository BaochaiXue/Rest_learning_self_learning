import os
import re
import csv
import urllib.request
import shutil
import tarfile
import gzip

papers_def = [
    {"title": "Titans: Learning to Memorize at Test Time", "category": "frontier_core", "page_url": "https://arxiv.org/abs/2501.00663", "source_url": "https://arxiv.org/e-print/2501.00663", "pdf_url": "https://arxiv.org/pdf/2501.00663"},
    {"title": "Nested Learning: The Illusion of Deep Learning Architectures", "category": "frontier_core", "page_url": "https://arxiv.org/abs/2512.24695", "source_url": "https://arxiv.org/e-print/2512.24695", "pdf_url": "https://arxiv.org/pdf/2512.24695"},
    {"title": "Test-time regression: a unifying framework for designing sequence models with associative memory", "category": "frontier_core", "page_url": "https://arxiv.org/abs/2501.12352", "source_url": "https://arxiv.org/e-print/2501.12352", "pdf_url": "https://arxiv.org/pdf/2501.12352"},
    {"title": "It’s All Connected: A Journey Through Test-Time Memorization, Attentional Bias, Retention, and Online Optimization", "category": "frontier_core", "page_url": "https://arxiv.org/abs/2504.13173", "source_url": "https://arxiv.org/e-print/2504.13173", "pdf_url": "https://arxiv.org/pdf/2504.13173"},
    {"title": "Dynamic Evaluation of Neural Sequence Models", "category": "ttt_early", "page_url": "https://arxiv.org/abs/1709.07432", "source_url": "https://arxiv.org/e-print/1709.07432", "pdf_url": "https://arxiv.org/pdf/1709.07432"},
    {"title": "Test-Time Training with Self-Supervision for Generalization under Distribution Shifts", "category": "ttt_early", "page_url": "https://arxiv.org/abs/1909.13231", "source_url": "https://arxiv.org/e-print/1909.13231", "pdf_url": "https://arxiv.org/pdf/1909.13231"},
    {"title": "Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks", "category": "meta_learning", "page_url": "https://arxiv.org/abs/1703.03400", "source_url": "https://arxiv.org/e-print/1703.03400", "pdf_url": "https://arxiv.org/pdf/1703.03400"},
    {"title": "Optimization as a Model for Few-Shot Learning", "category": "meta_learning", "page_url": "https://openreview.net/forum?id=rJY0-Kcll", "source_url": "", "pdf_url": "https://openreview.net/pdf?id=rJY0-Kcll"},
    {"title": "Learning to learn by gradient descent by gradient descent", "category": "meta_learning", "page_url": "https://arxiv.org/abs/1606.04474", "source_url": "https://arxiv.org/e-print/1606.04474", "pdf_url": "https://arxiv.org/pdf/1606.04474"},
    {"title": "Meta-Learning with Memory-Augmented Neural Networks", "category": "memory_meta_learning", "page_url": "https://proceedings.mlr.press/v48/santoro16.html", "source_url": "", "pdf_url": "https://proceedings.mlr.press/v48/santoro16.pdf"},
    {"title": "One-shot Learning with Memory-Augmented Neural Networks", "category": "memory_meta_learning_source_proxy", "page_url": "https://arxiv.org/abs/1605.06065", "source_url": "https://arxiv.org/e-print/1605.06065", "pdf_url": "https://arxiv.org/pdf/1605.06065"},
    {"title": "HyperNetworks", "category": "memory_meta_learning", "page_url": "https://arxiv.org/abs/1609.09106", "source_url": "https://arxiv.org/e-print/1609.09106", "pdf_url": "https://arxiv.org/pdf/1609.09106"},
    {"title": "Using Fast Weights to Attend to the Recent Past", "category": "fast_weights_attention", "page_url": "https://arxiv.org/abs/1610.06258", "source_url": "https://arxiv.org/e-print/1610.06258", "pdf_url": "https://arxiv.org/pdf/1610.06258"},
    {"title": "Attention Is All You Need", "category": "attention_core", "page_url": "https://arxiv.org/abs/1706.03762", "source_url": "https://arxiv.org/e-print/1706.03762", "pdf_url": "https://arxiv.org/pdf/1706.03762"},
    {"title": "Transformers are RNNs: Fast Autoregressive Transformers with Linear Attention", "category": "attention_core", "page_url": "https://arxiv.org/abs/2006.16236", "source_url": "https://arxiv.org/e-print/2006.16236", "pdf_url": "https://arxiv.org/pdf/2006.16236"},
    {"title": "Linear Transformers Are Secretly Fast Weight Programmers", "category": "attention_core", "page_url": "https://arxiv.org/abs/2102.11174", "source_url": "https://arxiv.org/e-print/2102.11174", "pdf_url": "https://arxiv.org/pdf/2102.11174"},
    {"title": "What Can Transformers Learn In-Context? A Case Study of Simple Function Classes", "category": "icl_core", "page_url": "https://arxiv.org/abs/2208.01066", "source_url": "https://arxiv.org/e-print/2208.01066", "pdf_url": "https://arxiv.org/pdf/2208.01066"},
    {"title": "In-context Learning and Induction Heads", "category": "icl_core", "page_url": "https://arxiv.org/abs/2209.11895", "source_url": "https://arxiv.org/e-print/2209.11895", "pdf_url": "https://arxiv.org/pdf/2209.11895"},
    {"title": "Transformers learn in-context by gradient descent", "category": "icl_core", "page_url": "https://arxiv.org/abs/2212.07677", "source_url": "https://arxiv.org/e-print/2212.07677", "pdf_url": "https://arxiv.org/pdf/2212.07677"},
    {"title": "Transformers learn to implement preconditioned gradient descent for in-context learning", "category": "icl_core", "page_url": "https://arxiv.org/abs/2306.00297", "source_url": "https://arxiv.org/e-print/2306.00297", "pdf_url": "https://arxiv.org/pdf/2306.00297"},
    {"title": "Transformers Learn to Achieve Second-Order Convergence Rates for In-Context Linear Regression", "category": "icl_core", "page_url": "https://arxiv.org/abs/2310.17086", "source_url": "https://arxiv.org/e-print/2310.17086", "pdf_url": "https://arxiv.org/pdf/2310.17086"},
    {"title": "Learning to (Learn at Test Time)", "category": "ttt_modern_bridge", "page_url": "https://arxiv.org/abs/2310.13807", "source_url": "https://arxiv.org/e-print/2310.13807", "pdf_url": "https://arxiv.org/pdf/2310.13807"},
    {"title": "Learning to (Learn at Test Time): RNNs with Expressive Hidden States", "category": "ttt_modern_bridge", "page_url": "https://arxiv.org/abs/2407.04620", "source_url": "https://arxiv.org/e-print/2407.04620", "pdf_url": "https://arxiv.org/pdf/2407.04620"},
    {"title": "Test-Time Training Done Right", "category": "ttt_modern_bridge", "page_url": "https://arxiv.org/abs/2505.23884", "source_url": "https://arxiv.org/e-print/2505.23884", "pdf_url": "https://arxiv.org/pdf/2505.23884"}
]

def normalize_title(title):
    t = title.lower()
    t = re.sub(r'[^a-z0-9\s-]', '', t)
    t = re.sub(r'[\s-]+', '_', t)
    return t.strip('_')

base_dir = "/Users/xinjiezhang/Rest_learning/nested_learning_textbook"
os.makedirs(f"{base_dir}/downloads", exist_ok=True)
os.makedirs(f"{base_dir}/papers", exist_ok=True)
os.makedirs(f"{base_dir}/manifests", exist_ok=True)
os.makedirs(f"{base_dir}/notes/papers", exist_ok=True)
os.makedirs(f"{base_dir}/scripts", exist_ok=True)
os.makedirs(f"{base_dir}/manuscript", exist_ok=True)

shutil.copy("/tmp/literature_engineer.py", f"{base_dir}/scripts/literature_engineer.py")

manifest_data = []

existing_folders = {
    "Titans_Learning_to_Memorize_at_Test_Time": "titans_learning_to_memorize_at_test_time",
    "Nested_Learning_The_Illusion_of_Deep_Learning_Architectures": "nested_learning_the_illusion_of_deep_learning_architectures"
}
for orig, target in existing_folders.items():
    orig_path = f"/Users/xinjiezhang/Rest_learning/{orig}"
    if os.path.exists(orig_path):
        os.rename(orig_path, f"{base_dir}/papers/{target}")

def resolve_inputs(file_path, visited, folder_path):
    if file_path in visited: return ""
    visited.add(file_path)
    if not os.path.exists(file_path): return ""
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    def repl(match):
        inc_file = match.group(1)
        if not inc_file.endswith('.tex'): inc_file += '.tex'
        inc_path = os.path.join(folder_path, inc_file)
        if os.path.exists(inc_path):
            return "\n% --- BEGIN " + inc_file + " ---\n" + resolve_inputs(inc_path, visited, folder_path) + "\n% --- END " + inc_file + " ---\n"
        return match.group(0)
    return re.sub(r'\\(?:input|include|subfile)\{([^}]+)\}', repl, content)

for p in papers_def:
    slug = normalize_title(p["title"])
    paper_dir = f"{base_dir}/papers/{slug}"
    status = ""
    main_tex = ""
    merged_tex = ""
    
    if os.path.exists(paper_dir):
        status = "already_local_source"
    elif p["source_url"]:
        try:
            print(f"Downloading source for {slug}...")
            req = urllib.request.Request(p["source_url"], headers={'User-Agent': 'Mozilla/5.0'})
            tar_path = f"{base_dir}/downloads/{slug}.tar.gz"
            with urllib.request.urlopen(req) as resp, open(tar_path, 'wb') as f:
                shutil.copyfileobj(resp, f)
            os.makedirs(paper_dir, exist_ok=True)
            try:
                import warnings
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore")
                    with tarfile.open(tar_path, "r:gz") as tar:
                        tar.extractall(path=paper_dir)
            except tarfile.ReadError:
                with gzip.open(tar_path, "rt", encoding="utf-8") as f_in:
                    with open(os.path.join(paper_dir, "main.tex"), "w", encoding="utf-8") as f_out:
                        f_out.write(f_in.read())
            os.remove(tar_path)
            status = "downloaded_source"
        except Exception as e:
            print(f"Failed source {slug}: {e}")
            status = "source_download_failed"
    elif p["pdf_url"]:
        try:
            print(f"Downloading PDF for {slug}...")
            req = urllib.request.Request(p["pdf_url"], headers={'User-Agent': 'Mozilla/5.0'})
            pdf_path = f"{base_dir}/downloads/{slug}.pdf"
            with urllib.request.urlopen(req) as resp, open(pdf_path, 'wb') as f:
                shutil.copyfileobj(resp, f)
            status = "pdf_only_no_public_source"
        except Exception as e:
            print(f"Failed pdf {slug}: {e}")
            status = "pdf_download_failed"
    
    if os.path.exists(paper_dir):
        tex_files = []
        for root, _, files in os.walk(paper_dir):
            for file in files:
                if file.endswith(".tex"):
                    tex_files.append(os.path.join(root, file))
        main_file = None
        for tf in tex_files:
            try:
                with open(tf, "r", encoding="utf-8", errors="ignore") as f:
                    if "\\documentclass" in f.read()[:10000]:
                        main_file = tf
                        break
            except: pass
        if not main_file and tex_files:
            main_file = tex_files[0]
            
        if main_file:
            main_tex = os.path.relpath(main_file, paper_dir)
            try:
                merged_content = resolve_inputs(main_file, set(), os.path.dirname(main_file))
                merged_content = re.sub(r'(?<!\\)%.*', '', merged_content) 
                merged_content = re.sub(r'\n[ \t]*\n+', '\n\n', merged_content)
                merged_tex_path = os.path.join(paper_dir, "merged_paper.tex")
                with open(merged_tex_path, "w", encoding="utf-8") as f:
                    f.write(merged_content.strip() + "\n")
                merged_tex = "merged_paper.tex"
            except Exception as e:
                print(f"Failed to merge {slug}: {e}")
    
    note_path = f"{base_dir}/notes/papers/{slug}.md"
    if not os.path.exists(note_path):
        with open(note_path, "w", encoding="utf-8") as f:
            f.write(f"# {p['title']}\n\n")
            f.write("## 在本教材中的角色\n作为核心文献支撑...\n\n")
            f.write("## 对应主线环节\n属于本教材从TTT到NL演化主线的关键一环。\n\n")
            f.write("## 重点解释\n- 机制性共识\n- 解释/研究议程观点\n")
            
    manifest_data.append({
        "title": p["title"],
        "slug": slug,
        "category": p["category"],
        "page_url": p["page_url"],
        "source_url": p["source_url"],
        "local_folder": paper_dir if os.path.exists(paper_dir) else "",
        "status": status,
        "main_tex": main_tex,
        "merged_tex": merged_tex,
        "notes": note_path
    })

with open(f"{base_dir}/manifests/papers_manifest.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=manifest_data[0].keys())
    writer.writeheader()
    writer.writerows(manifest_data)

with open(f"{base_dir}/manifests/papers_manifest.md", "w", encoding="utf-8") as f:
    f.write("# Papers Manifest\n\n")
    for d in manifest_data:
        f.write(f"- **{d['title']}** ({d['status']})\n")

