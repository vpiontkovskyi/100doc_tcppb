# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## About

Homework repository for the [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/) (Udemy course).

## Running Code

```bash
# Run a specific project
uv run projects/001b_band_name_generator/001_main.py

# Add a dependency
uv add <package>
```

## Project Structure

- `course/` — materials downloaded from the course
- `projects/` — self-completed coding exercises, named `NNN[b]_<exercise_name>/` (NNN = day number, optional `b` suffix for bonus)
- `resources/` — additional reference materials

Each project in `projects/` typically has one or more Python files. The main entry point follows the pattern `NNN_main.py`.

## Environment

- Package manager: **uv**
- Python 3.14 (`.venv/` managed by uv)
- No external dependencies (`pyproject.toml` lists none)
