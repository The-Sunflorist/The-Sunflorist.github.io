# Minimal makefile for Sphinx documentation

# You can set these variables from the command line,
# and also from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

SHELL := /bin/zsh

DATETIME := "[$(shell date +"%F %T %z")]"
LOG_FOLDER_PATH := $(BUILDDIR)/_logs
LOG_FILEPATH := $(LOG_FOLDER_PATH)/$(shell date +%F).log

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx
# using the new "make mode" option.
# $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@rm -rf $(BUILDDIR)/$@
	@mkdir -p $(LOG_FOLDER_PATH)
	@echo $(DATETIME) >> $(LOG_FILEPATH)
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) --color \
     $(O) 2>&1 | tee >(sed -r 's/\x1b\[[0-9;]*m//g' >> $(LOG_FILEPATH))
	@echo | tee -a $(LOG_FILEPATH)
	@[[ $@ == html ]] && python source/_pythons/refiner.py || exit 0
