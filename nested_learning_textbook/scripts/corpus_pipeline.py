#!/usr/bin/env python3
"""
corpus_pipeline.py — Incremental, idempotent literature corpus builder.
Usage: cd nested_learning_textbook && python3 scripts/corpus_pipeline.py [--slug SLUG] [--force-pdf]

Features:
- Repo-relative paths only; no hardcoded absolute paths
- Idempotent: safe to run multiple times
- Incremental: skips already-completed papers
- Logs all actions to stdout
- Handles TeX source + merged_paper.tex generation
- Falls back to PDF download if no TeX source
"""
import os, re, csv, gzip, shutil, tarfile, urllib.request, warnings, pathlib, datetime, sys

# ─────────────────── Path setup ───────────────────
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent.parent          # Rest_learning/
NLT_ROOT = REPO_ROOT / "nested_learning_textbook"
PAPERS_DIR = NLT_ROOT / "papers"
DOWNLOADS_DIR = NLT_ROOT / "downloads"
MANIFESTS_DIR = NLT_ROOT / "manifests"
NOTES_DIR = NLT_ROOT / "notes" / "papers"

for d in [PAPERS_DIR, DOWNLOADS_DIR, MANIFESTS_DIR, NOTES_DIR]:
    d.mkdir(parents=True, exist_ok=True)

TODAY = datetime.date.today().isoformat()

# ─────────────────── Paper definitions ───────────────────
PAPERS = [
    {"title":"Titans: Learning to Memorize at Test Time","slug":"titans_learning_to_memorize_at_test_time","category":"frontier_core","page_url":"https://arxiv.org/abs/2501.00663","source_url":"https://arxiv.org/e-print/2501.00663","pdf_url":"https://arxiv.org/pdf/2501.00663"},
    {"title":"Nested Learning: The Illusion of Deep Learning Architectures","slug":"nested_learning_the_illusion_of_deep_learning_architectures","category":"frontier_core","page_url":"https://arxiv.org/abs/2512.24695","source_url":"https://arxiv.org/e-print/2512.24695","pdf_url":"https://arxiv.org/pdf/2512.24695"},
    {"title":"Test-time regression: a unifying framework for designing sequence models with associative memory","slug":"test_time_regression_a_unifying_framework_for_designing_sequence_models_with_associative_memory","category":"frontier_core","page_url":"https://arxiv.org/abs/2501.12352","source_url":"https://arxiv.org/e-print/2501.12352","pdf_url":"https://arxiv.org/pdf/2501.12352"},
    {"title":"It's All Connected: A Journey Through Test-Time Memorization, Attentional Bias, Retention, and Online Optimization","slug":"its_all_connected_a_journey_through_test_time_memorization_attentional_bias_retention_and_online_optimization","category":"frontier_core","page_url":"https://arxiv.org/abs/2504.13173","source_url":"https://arxiv.org/e-print/2504.13173","pdf_url":"https://arxiv.org/pdf/2504.13173"},
    {"title":"Dynamic Evaluation of Neural Sequence Models","slug":"dynamic_evaluation_of_neural_sequence_models","category":"ttt_early","page_url":"https://arxiv.org/abs/1709.07432","source_url":"https://arxiv.org/e-print/1709.07432","pdf_url":"https://arxiv.org/pdf/1709.07432"},
    {"title":"Test-Time Training with Self-Supervision for Generalization under Distribution Shifts","slug":"test_time_training_with_self_supervision_for_generalization_under_distribution_shifts","category":"ttt_early","page_url":"https://arxiv.org/abs/1909.13231","source_url":"https://arxiv.org/e-print/1909.13231","pdf_url":"https://arxiv.org/pdf/1909.13231"},
    {"title":"Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks","slug":"model_agnostic_meta_learning_for_fast_adaptation_of_deep_networks","category":"meta_learning","page_url":"https://arxiv.org/abs/1703.03400","source_url":"https://arxiv.org/e-print/1703.03400","pdf_url":"https://arxiv.org/pdf/1703.03400"},
    {"title":"Optimization as a Model for Few-Shot Learning","slug":"optimization_as_a_model_for_few_shot_learning","category":"meta_learning","page_url":"https://openreview.net/forum?id=rJY0-Kcll","source_url":"","pdf_url":"https://openreview.net/pdf?id=rJY0-Kcll"},
    {"title":"Learning to learn by gradient descent by gradient descent","slug":"learning_to_learn_by_gradient_descent_by_gradient_descent","category":"meta_learning","page_url":"https://arxiv.org/abs/1606.04474","source_url":"https://arxiv.org/e-print/1606.04474","pdf_url":"https://arxiv.org/pdf/1606.04474"},
    {"title":"Meta-Learning with Memory-Augmented Neural Networks","slug":"meta_learning_with_memory_augmented_neural_networks","category":"memory_meta_learning","page_url":"https://proceedings.mlr.press/v48/santoro16.html","source_url":"","pdf_url":"https://proceedings.mlr.press/v48/santoro16.pdf"},
    {"title":"One-shot Learning with Memory-Augmented Neural Networks","slug":"one_shot_learning_with_memory_augmented_neural_networks","category":"memory_meta_learning_source_proxy","page_url":"https://arxiv.org/abs/1605.06065","source_url":"https://arxiv.org/e-print/1605.06065","pdf_url":"https://arxiv.org/pdf/1605.06065"},
    {"title":"HyperNetworks","slug":"hypernetworks","category":"memory_meta_learning","page_url":"https://arxiv.org/abs/1609.09106","source_url":"https://arxiv.org/e-print/1609.09106","pdf_url":"https://arxiv.org/pdf/1609.09106"},
    {"title":"Using Fast Weights to Attend to the Recent Past","slug":"using_fast_weights_to_attend_to_the_recent_past","category":"fast_weights_attention","page_url":"https://arxiv.org/abs/1610.06258","source_url":"https://arxiv.org/e-print/1610.06258","pdf_url":"https://arxiv.org/pdf/1610.06258"},
    {"title":"Attention Is All You Need","slug":"attention_is_all_you_need","category":"attention_core","page_url":"https://arxiv.org/abs/1706.03762","source_url":"https://arxiv.org/e-print/1706.03762","pdf_url":"https://arxiv.org/pdf/1706.03762"},
    {"title":"Transformers are RNNs: Fast Autoregressive Transformers with Linear Attention","slug":"transformers_are_rnns_fast_autoregressive_transformers_with_linear_attention","category":"attention_core","page_url":"https://arxiv.org/abs/2006.16236","source_url":"https://arxiv.org/e-print/2006.16236","pdf_url":"https://arxiv.org/pdf/2006.16236"},
    {"title":"Linear Transformers Are Secretly Fast Weight Programmers","slug":"linear_transformers_are_secretly_fast_weight_programmers","category":"attention_core","page_url":"https://arxiv.org/abs/2102.11174","source_url":"https://arxiv.org/e-print/2102.11174","pdf_url":"https://arxiv.org/pdf/2102.11174"},
    {"title":"What Can Transformers Learn In-Context? A Case Study of Simple Function Classes","slug":"what_can_transformers_learn_in_context_a_case_study_of_simple_function_classes","category":"icl_core","page_url":"https://arxiv.org/abs/2208.01066","source_url":"https://arxiv.org/e-print/2208.01066","pdf_url":"https://arxiv.org/pdf/2208.01066"},
    {"title":"In-context Learning and Induction Heads","slug":"in_context_learning_and_induction_heads","category":"icl_core","page_url":"https://arxiv.org/abs/2209.11895","source_url":"https://arxiv.org/e-print/2209.11895","pdf_url":"https://arxiv.org/pdf/2209.11895"},
    {"title":"Transformers learn in-context by gradient descent","slug":"transformers_learn_in_context_by_gradient_descent","category":"icl_core","page_url":"https://arxiv.org/abs/2212.07677","source_url":"https://arxiv.org/e-print/2212.07677","pdf_url":"https://arxiv.org/pdf/2212.07677"},
    {"title":"Transformers learn to implement preconditioned gradient descent for in-context learning","slug":"transformers_learn_to_implement_preconditioned_gradient_descent_for_in_context_learning","category":"icl_core","page_url":"https://arxiv.org/abs/2306.00297","source_url":"https://arxiv.org/e-print/2306.00297","pdf_url":"https://arxiv.org/pdf/2306.00297"},
    {"title":"Transformers Learn to Achieve Second-Order Convergence Rates for In-Context Linear Regression","slug":"transformers_learn_to_achieve_second_order_convergence_rates_for_in_context_linear_regression","category":"icl_core","page_url":"https://arxiv.org/abs/2310.17086","source_url":"https://arxiv.org/e-print/2310.17086","pdf_url":"https://arxiv.org/pdf/2310.17086"},
    {"title":"Learning to (Learn at Test Time)","slug":"learning_to_learn_at_test_time","category":"ttt_modern_bridge","page_url":"https://arxiv.org/abs/2310.13807","source_url":"https://arxiv.org/e-print/2310.13807","pdf_url":"https://arxiv.org/pdf/2310.13807"},
    {"title":"Learning to (Learn at Test Time): RNNs with Expressive Hidden States","slug":"learning_to_learn_at_test_time_rnns_with_expressive_hidden_states","category":"ttt_modern_bridge","page_url":"https://arxiv.org/abs/2407.04620","source_url":"https://arxiv.org/e-print/2407.04620","pdf_url":"https://arxiv.org/pdf/2407.04620"},
    {"title":"Test-Time Training Done Right","slug":"test_time_training_done_right","category":"ttt_modern_bridge","page_url":"https://arxiv.org/abs/2505.23884","source_url":"https://arxiv.org/e-print/2505.23884","pdf_url":"https://arxiv.org/pdf/2505.23884"},
]

# ─────────────────── Helpers ───────────────────

def http_get(url, dest):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as r, open(dest, "wb") as f:
        shutil.copyfileobj(r, f)

def find_main_tex(folder):
    for fname in os.listdir(folder):
        if not fname.endswith(".tex") or fname == "merged_paper.tex":
            continue
        fpath = folder / fname
        try:
            if "\\documentclass" in fpath.read_text(encoding="utf-8", errors="ignore")[:10000]:
                return fpath
        except Exception:
            pass
    return None

def resolve_inputs(file_path, visited, folder):
    if str(file_path) in visited:
        return ""
    visited.add(str(file_path))
    if not file_path.exists():
        return ""
    try:
        content = file_path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""

    def repl(m):
        inc = m.group(1)
        if not inc.endswith(".tex"):
            inc += ".tex"
        inc_path = folder / inc
        if inc_path.exists():
            return "\n% --- BEGIN " + inc + " ---\n" + resolve_inputs(inc_path, visited, folder) + "\n% --- END " + inc + " ---\n"
        return m.group(0)

    return re.sub(r"\\(?:input|include|subfile)\{([^}]+)\}", repl, content)

def build_merged(paper_dir):
    main = find_main_tex(paper_dir)
    if not main:
        return False, "no main tex found"
    try:
        merged = resolve_inputs(main, set(), paper_dir)
        # strip comments but preserve \%
        merged = re.sub(r"(?<!\\)%.*", "", merged)
        # collapse blank lines
        merged = re.sub(r"\n[ \t]*\n+", "\n\n", merged)
        out = paper_dir / "merged_paper.tex"
        out.write_text(merged.strip() + "\n", encoding="utf-8")
        return True, str(out)
    except Exception as e:
        return False, str(e)

def get_rel(path):
    """Return path relative to REPO_ROOT."""
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)

def process_paper(p, force_pdf=False):
    slug = p["slug"]
    paper_dir = PAPERS_DIR / slug
    status = "unknown"
    main_tex = ""
    merged_tex = ""

    # Already has merged — skip unless forced
    if (paper_dir / "merged_paper.tex").exists():
        print(f"  [SKIP] {slug} — merged_paper.tex already exists")
        main_tex_f = find_main_tex(paper_dir)
        return {
            "status": "source_and_merged",
            "main_tex": main_tex_f.name if main_tex_f else "",
            "merged_tex": "merged_paper.tex",
        }

    # Try TeX source
    if p.get("source_url") and not paper_dir.exists():
        tmp = DOWNLOADS_DIR / f"{slug}_src.bin"
        try:
            print(f"  [DL]   {slug} — downloading TeX source...")
            http_get(p["source_url"], tmp)
            # Detect type
            import subprocess
            result = subprocess.run(["file", str(tmp)], capture_output=True, text=True)
            file_type = result.stdout.lower()
            paper_dir.mkdir(parents=True, exist_ok=True)
            if "pdf" in file_type:
                # It's actually a PDF despite source URL
                pdf_dest = DOWNLOADS_DIR / f"{slug}.pdf"
                shutil.move(str(tmp), str(pdf_dest))
                print(f"  [PDF]  {slug} — source URL returned PDF, saved to downloads/")
                return {"status": "pdf_only", "main_tex": "", "merged_tex": ""}
            else:
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore")
                    with tarfile.open(tmp, "r:gz") as tar:
                        tar.extractall(path=paper_dir)
                tmp.unlink()
                print(f"  [OK]   {slug} — TeX source extracted")
                status = "downloaded_source"
        except Exception as e:
            if tmp.exists():
                tmp.unlink()
            print(f"  [ERR]  {slug} — source download failed: {e}")
            status = "source_download_failed"
    elif paper_dir.exists():
        status = "already_local"
    else:
        status = "no_source"

    # Build merged_paper.tex if we have a folder with tex
    if paper_dir.exists():
        ok, info = build_merged(paper_dir)
        if ok:
            merged_tex = "merged_paper.tex"
            main_tex_f = find_main_tex(paper_dir)
            main_tex = main_tex_f.name if main_tex_f else ""
            status = "source_and_merged"
            print(f"  [MRGD] {slug} — merged_paper.tex generated")
        else:
            print(f"  [WARN] {slug} — merge failed: {info}")

    # PDF fallback
    if not paper_dir.exists() and (p.get("pdf_url") or force_pdf):
        pdf_dest = DOWNLOADS_DIR / f"{slug}.pdf"
        if not pdf_dest.exists():
            try:
                print(f"  [PDF]  {slug} — downloading PDF fallback...")
                http_get(p["pdf_url"], pdf_dest)
                status = "pdf_only"
            except Exception as e:
                print(f"  [ERR]  {slug} — pdf download failed: {e}")
                status = "download_failed"
        else:
            status = "pdf_only"

    return {"status": status, "main_tex": main_tex, "merged_tex": merged_tex}

def ensure_note(p):
    slug = p["slug"]
    note_path = NOTES_DIR / f"{slug}.md"
    if not note_path.exists():
        note_path.write_text(f"""# {p['title']}

## 在本教材中的角色
<!-- TODO: 描述这篇论文在 inference-time learning 主线中扮演什么角色 -->

## 对应主线哪一环
- 类别: {p['category']}
- 主线位置: <!-- TODO: 例如 "TTT 2020 起点" / "ICL 作为优化" / "终局 NL 框架" -->

## 本科生最值得理解的 3 个点
1. <!-- TODO -->
2. <!-- TODO -->
3. <!-- TODO -->

## 哪些内容是机制性共识
<!-- TODO: 列出可作为事实陈述的部分 -->

## 哪些内容更像解释/视角/研究议程
<!-- TODO: 需要在教材中标注为 "一种视角" 的部分 -->

## 与其他论文的桥梁关系
<!-- TODO: 例如 "前接 MAML，后接 TTT-Layer" -->
""", encoding="utf-8")

# ─────────────────── Main ───────────────────

def main():
    force_pdf = "--force-pdf" in sys.argv
    slug_filter = None
    if "--slug" in sys.argv:
        idx = sys.argv.index("--slug")
        slug_filter = sys.argv[idx+1] if idx+1 < len(sys.argv) else None

    print(f"=== Corpus Pipeline — {TODAY} ===")
    print(f"Papers dir: {PAPERS_DIR}")
    print()

    manifest_rows = []
    for p in PAPERS:
        if slug_filter and p["slug"] != slug_filter:
            continue
        print(f"[{p['category']}] {p['title'][:60]}...")
        result = process_paper(p, force_pdf=force_pdf)
        ensure_note(p)

        paper_dir = PAPERS_DIR / p["slug"]
        row = {
            "title": p["title"],
            "slug": p["slug"],
            "category": p["category"],
            "page_url": p["page_url"],
            "source_url": p.get("source_url", ""),
            "pdf_url": p.get("pdf_url", ""),
            "local_folder": get_rel(paper_dir) if paper_dir.exists() else "",
            "status": result["status"],
            "main_tex": result["main_tex"],
            "merged_tex": result["merged_tex"],
            "note_path": get_rel(NOTES_DIR / f"{p['slug']}.md"),
            "source_type": "tex" if result["main_tex"] else ("pdf" if result["status"]=="pdf_only" else "none"),
            "last_verified": TODAY,
        }
        manifest_rows.append(row)

    # Write manifest
    if not slug_filter:
        fields = ["title","slug","category","page_url","source_url","pdf_url","local_folder","status","main_tex","merged_tex","note_path","source_type","last_verified"]
        with open(MANIFESTS_DIR/"papers_manifest.csv","w",newline="",encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            for r in manifest_rows:
                w.writerow({k:r[k] for k in fields})

        # MD summary
        with open(MANIFESTS_DIR/"papers_manifest.md","w",encoding="utf-8") as f:
            f.write(f"# Papers Manifest\nGenerated: {TODAY}\n\n")
            status_counts = {}
            for r in manifest_rows:
                status_counts[r["status"]] = status_counts.get(r["status"],0)+1
            f.write("## Summary\n")
            for k,v in status_counts.items():
                f.write(f"- `{k}`: {v}\n")
            f.write("\n## Papers\n\n")
            for r in manifest_rows:
                icon = "✅" if r["status"]=="source_and_merged" else ("⚠️" if "pdf" in r["status"] else "❌")
                f.write(f"- {icon} **{r['title']}** (`{r['slug']}`)\n")
                f.write(f"  - status: `{r['status']}`\n")
                f.write(f"  - category: `{r['category']}`\n\n")
        print(f"\nManifest written: {MANIFESTS_DIR}/papers_manifest.csv")

    status_counts = {}
    for r in manifest_rows:
        status_counts[r["status"]] = status_counts.get(r["status"],0)+1
    print("\n=== Summary ===")
    for k,v in status_counts.items():
        print(f"  {k}: {v}")

if __name__ == "__main__":
    main()
