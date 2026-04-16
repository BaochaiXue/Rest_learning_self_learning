SHELL := /bin/bash
BOOK_DIR := nested_learning_textbook/book
SCRIPTS_DIR := nested_learning_textbook/scripts
RESEARCH_CHECK := scripts/research_check.py

.PHONY: audit corpus book check clean help research-check

help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  audit    Run all repository audit/check scripts"
	@echo "  research-check  Validate the root research OS files"
	@echo "  corpus   Run incremental literature corpus pipeline"
	@echo "  book     Compile LaTeX book to PDF"
	@echo "  check    Run all checks (audit + validate)"
	@echo "  clean    Remove LaTeX build artifacts"

audit:
	@echo "=== Running repo audit scripts ==="
	python3 $(SCRIPTS_DIR)/check_absolute_paths.py
	python3 $(SCRIPTS_DIR)/validate_manifest.py
	python3 $(SCRIPTS_DIR)/check_book_structure.py

research-check:
	@echo "=== Checking root research OS files ==="
	python3 $(RESEARCH_CHECK)

corpus:
	@echo "=== Running corpus pipeline ==="
	cd nested_learning_textbook && python3 scripts/corpus_pipeline.py

book:
	@echo "=== Compiling LaTeX book ==="
	cd $(BOOK_DIR) && latexmk -xelatex -interaction=nonstopmode main.tex
	@echo "Output: $(BOOK_DIR)/build/main.pdf"

check: research-check audit
	@echo "=== All checks complete ==="

clean:
	@echo "=== Cleaning LaTeX build artifacts ==="
	cd $(BOOK_DIR) && latexmk -C && rm -f *.aux *.log *.out *.toc *.bbl *.bcf *.blg *.run.xml
	@echo "Done."
