# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

A collection of standalone Python utility scripts for everyday file/system operations.

## Running Utilities

Scripts are executable and use `#!/usr/bin/env python3`:

```bash
python3 remove_space_in_filename.py          # interactive mode (prompts per file)
python3 remove_space_in_filename.py -force   # batch mode (no prompts)
```

## Conventions

- Python 3, standard library only (no external dependencies)
- Scripts operate on the current working directory
- Interactive by default with a `-force` flag for batch/scripted use
