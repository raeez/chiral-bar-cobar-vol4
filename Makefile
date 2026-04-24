# ============================================================================
#  Makefile -- Vol IV: Realization (verification capstone)
# ============================================================================
#
#  Usage:
#    make            Full converging build → out/main.pdf
#    make fast       Quick build (up to 4 passes) → out/main.pdf
#    make release    Full rebuild → out/ + iCloud
#    make icloud     Copy latest PDFs to iCloud Drive
#    make clean      Remove LaTeX build artifacts (preserves stamp)
#    make veryclean  Remove artifacts AND out/ (forces rebuild)
#    make clean-builds  Remove all /tmp/mkd-chiral-bar-cobar-vol4-* dirs
#    make check      Halt-on-error validation
#    make count      Manuscript statistics
#    make test       Run compute test suite (realization decorators)
#    make help       Show available targets
#
#  Build isolation (parallel agents):
#    Each build runs in its own /tmp directory.  Set MKD_BUILD_NS to reuse
#    the same directory across invocations (warm .aux files = faster builds):
#
#      export MKD_BUILD_NS="agent-$$"   # set once per agent session
#      make fast                         # cold first time, warm thereafter
#
#  All compiled output goes to out/.
#
# ============================================================================

# --- Configuration -----------------------------------------------------------

MAIN      := main
TEX       := pdflatex
TEXFLAGS  := -interaction=nonstopmode -file-line-error -synctex=0 -cnf-line='buf_size=1000000' -cnf-line='stack_size=20000'
BUILD_SCRIPT := ./scripts/build.sh
LOG_DIR   := .build_logs
PASSES    := 6
FAST_PASSES := 4
PYTEST_FAST_TIMEOUT ?= 120
PYTHON_BIN ?= $(shell if [ -x compute/.venv/bin/python ]; then echo compute/.venv/bin/python; elif [ -x .venv/bin/python ]; then echo .venv/bin/python; else echo python3; fi)

# iCloud destination for release PDFs
ICLOUD_DIR := /Users/raeez/Library/Mobile Documents/com~apple~CloudDocs/research

# Source files: every .tex file that main.tex transitively \input's or \include's.
SOURCES   := $(wildcard *.tex) \
             $(wildcard chapters/frame/*.tex) \
             $(wildcard chapters/realization/*.tex) \
             $(wildcard chapters/arithmetic/*.tex) \
             $(wildcard appendices/*.tex) \
             $(wildcard appendices/arithmetic/*.tex)

# Output -- everything goes to out/
OUT_DIR   := out
PDF       := $(OUT_DIR)/main.pdf

STAMP     := .build_stamp

# If PDF was externally deleted but stamp remains, force a rebuild.
ifeq (,$(wildcard $(PDF)))
  $(shell rm -f $(STAMP))
endif

# LaTeX intermediate extensions
AUX_EXTS  := aux log out toc synctex.gz fdb_latexmk fls bbl blg \
             nav snm vrb idx ilg ind lof lot

# ============================================================================
#  Targets
# ============================================================================

.PHONY: all fast clean veryclean clean-builds count check test help release icloud

## icloud: Copy latest PDFs to iCloud Drive (subject-organised)
icloud: $(PDF)
	@echo "  -- Copying Vol IV to iCloud (subject-organised) --"
	@mkdir -p "$(ICLOUD_DIR)/volumes"
	@mkdir -p "$(ICLOUD_DIR)/vol4_realization"
	@[ -f $(PDF) ] && cp $(PDF) "$(ICLOUD_DIR)/volumes/vol4_realization.pdf" \
		&& echo "    ok  volumes/vol4_realization.pdf" || true
	@for pdf in $(OUT_DIR)/*.pdf; do \
		name=$$(basename "$$pdf"); \
		if [ "$$name" != "main.pdf" ]; then \
			cp "$$pdf" "$(ICLOUD_DIR)/vol4_realization/$$name"; \
			echo "    ok  vol4_realization/$$name"; \
		fi; \
	done
	@echo "  Vol IV PDFs copied to iCloud."

## all: Full converging build → out/
all: $(STAMP)

$(STAMP): $(SOURCES) $(BUILD_SCRIPT)
	@echo "======================================================"
	@echo "  Building: $(MAIN).tex  ->  $(PDF)"
	@echo "======================================================"
	@$(BUILD_SCRIPT) $(PASSES)
	@if [ ! -f $(PDF) ]; then \
		echo "  Build failed -- no PDF produced."; exit 1; \
	fi
	@touch $(STAMP)
	@echo ""
	@echo "  $(PDF) built successfully."
	@echo ""

## fast: Bounded quick build for rapid iteration → out/main.pdf
## Convention: invoke at session end (CLAUDE.md "Do not run pdflatex after every edit").
fast:
	@echo "  -- Fast build (up to $(FAST_PASSES) passes) --"
	@$(BUILD_SCRIPT) $(FAST_PASSES)

## release: Full rebuild → out/ + iCloud
release:
	@rm -f $(STAMP)
	@rm -rf $(OUT_DIR)
	@mkdir -p $(LOG_DIR) $(OUT_DIR)
	@echo ""
	@echo "  =========================================="
	@echo "  -- RELEASE BUILD (Vol IV) --"
	@echo "  =========================================="
	@echo ""
	@echo "  [1/1] Main manuscript"
	@$(BUILD_SCRIPT) $(PASSES)
	@if [ -f $(PDF) ]; then \
		echo "  ok  $(PDF)"; \
	else \
		echo "  fail  manuscript build failed."; exit 1; \
	fi
	@echo ""
	@$(MAKE) --no-print-directory icloud
	@echo ""
	@echo "  =========================================="
	@echo "  Release complete. All output in out/:"
	@ls -1 $(OUT_DIR)/*.pdf 2>/dev/null | sed 's/^/    /'
	@echo "  =========================================="

## check: Halt-on-error validation
check:
	@echo "  -- Error check (halt-on-error) --"
	@mkdir -p $(LOG_DIR)
	@$(TEX) -interaction=nonstopmode -halt-on-error -file-line-error $(MAIN).tex >$(LOG_DIR)/check.log 2>&1 || { \
		echo "  fail  See $(LOG_DIR)/check.log"; \
		grep -aE '^! |Emergency stop|Runaway argument|Fatal error|Undefined control sequence|File ended while scanning|No pages of output' $(LOG_DIR)/check.log | head -n 20 || tail -n 40 $(LOG_DIR)/check.log; \
		exit 1; \
	}
	@echo "  ok  No fatal errors."
	@echo "     Log: $(LOG_DIR)/check.log"

## test: Run compute test suite (realization decorators)
test:
	@if [ -d compute/tests ] && ls compute/tests/test_*.py 1>/dev/null 2>&1; then \
		echo "  -- Running compute test suite (realization decorators) --"; \
		mkdir -p $(LOG_DIR); \
		LOG_FILE=$(LOG_DIR)/pytest.log; \
		$(PYTHON_BIN) -m pytest compute/tests/ -q -ra -m "not slow" \
			-o faulthandler_timeout=$(PYTEST_FAST_TIMEOUT) \
			--durations=10 --durations-min=1.0 >$$LOG_FILE 2>&1; rc=$$?; \
		if [ $$rc -eq 0 ]; then \
			tail -n 5 $$LOG_FILE; \
			echo "     Log: $$LOG_FILE"; \
		else \
			echo "  fail  Test run failed. See $$LOG_FILE"; \
			tail -n 120 $$LOG_FILE; \
			exit $$rc; \
		fi; \
	else \
		echo "  (no compute tests found -- skipping)"; \
	fi

## clean: Remove build debris but preserve the stamp.
clean:
	@echo "  Cleaning build artifacts..."
	@for ext in $(AUX_EXTS); do \
		rm -f $(MAIN).$$ext; \
	done
	@find chapters appendices -name '*.aux' -delete 2>/dev/null || true
	@rm -rf $(LOG_DIR)
	@rm -f texput.log
	@echo "  ok  Clean (stamp preserved -- make will skip rebuild if sources unchanged)."

## veryclean: Remove EVERYTHING including out/ and build stamp (forces full rebuild).
veryclean: clean
	@rm -f $(STAMP)
	@rm -rf $(OUT_DIR)
	@echo "  ok  Stamp and out/ removed -- next make will rebuild."

## clean-builds: Remove ALL /tmp/mkd-chiral-bar-cobar-vol4-* isolated build directories.
clean-builds:
	@echo "  Cleaning Vol IV isolated build directories..."
	@rm -rf /tmp/mkd-chiral-bar-cobar-vol4-*
	@echo "  ok  /tmp/mkd-chiral-bar-cobar-vol4-* removed."

## count: Manuscript statistics.
count:
	@echo ""
	@echo "  -- Vol IV Statistics --"
	@echo ""
	@printf "  Source files:   %s .tex files\n" "$$(find . -name '*.tex' -not -path './.build_logs/*' -not -path './out/*' | wc -l | tr -d ' ')"
	@printf "  Total lines:   %s\n" "$$(find . -name '*.tex' -not -path './.build_logs/*' -not -path './out/*' -exec cat {} + | wc -l | tr -d ' ')"
	@if [ -f $(PDF) ]; then \
		PAGES=$$(strings $(PDF) | grep -c '/Type /Page' 2>/dev/null || echo '?'); \
		printf "  PDF pages:     %s\n" "$$PAGES"; \
		printf "  PDF size:      %s\n" "$$(du -h $(PDF) | cut -f1)"; \
	else \
		echo "  PDF:           (not yet built -- run 'make')"; \
	fi
	@echo ""

## help: Show available targets.
help:
	@echo ""
	@echo "  Vol IV: Realization -- Build System"
	@echo "  ------------------------------------"
	@echo "  All compiled output goes to out/"
	@echo ""
	@echo "  make            Full converging build → out/main.pdf"
	@echo "  make fast       Quick build (up to $(FAST_PASSES) passes) → out/main.pdf"
	@echo "  make release    Full rebuild → out/ + iCloud"
	@echo "  make icloud     Copy latest PDFs to iCloud Drive"
	@echo "  make check      Halt-on-error validation"
	@echo "  make test       Run compute tests (realization decorators)"
	@echo "  make clean      Remove build debris (preserves stamp)"
	@echo "  make veryclean  Remove everything including out/"
	@echo "  make clean-builds  Remove /tmp/mkd-chiral-bar-cobar-vol4-* dirs"
	@echo "  make count      Manuscript statistics"
	@echo "  make help       This message"
	@echo ""
