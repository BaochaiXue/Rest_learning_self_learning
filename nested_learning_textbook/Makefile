SHELL := /bin/bash
BOOK_DIR := book
SCRIPTS_DIR := scripts

.PHONY: audit corpus book check clean help

help:
	@echo "Usage: make [target]  (run from nested_learning_textbook/)"
	@echo ""
	@echo "  audit    Run all repo audit/check scripts"
	@echo "  corpus   Run incremental literature corpus pipeline"
	@echo "  book     Compile LaTeX book to PDF"
	@echo "  check    Run all checks (alias for audit)"
	@echo "  clean    Remove LaTeX build artifacts"

audit:
	@echo "=== Scanning for absolute paths ==="
	python3 $(SCRIPTS_DIR)/check_absolute_paths.py
	@echo ""
	@echo "=== Validating manifest ==="
	python3 $(SCRIPTS_DIR)/validate_manifest.py
	@echo ""
	@echo "=== Checking book structure ==="
	python3 $(SCRIPTS_DIR)/check_book_structure.py

corpus:
	@echo "=== Running corpus pipeline ==="
	python3 $(SCRIPTS_DIR)/corpus_pipeline.py

book:
	@echo "=== Compiling LaTeX book ==="
	cd $(BOOK_DIR) && latexmk -xelatex -interaction=nonstopmode main.tex
	@echo "Output: $(BOOK_DIR)/build/main.pdf"

check: audit

clean:
	@echo "=== Cleaning LaTeX build artifacts ==="
	cd $(BOOK_DIR) && latexmk -C 2>/dev/null; rm -f *.aux *.log *.out *.toc *.bbl *.bcf *.blg *.run.xml 2>/dev/null; true
	@echo "Done."
