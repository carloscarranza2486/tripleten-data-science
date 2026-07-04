# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository purpose

This is a personal learning portfolio for the TripleTen Data Science bootcamp (see `README.md`: "Mi Portafolio de Data Science - TripleTen"). It is a collection of Jupyter notebooks and standalone Python scripts completed as coursework — not a deployable application or library. There is no build system, package manifest (no `requirements.txt`/`pyproject.toml`), linter config, or test suite; work is done and evaluated interactively inside notebooks.

## Structure

Content is organized by sprint (course module), roughly in chronological/curriculum order:

- `sprint-01-python` — Python fundamentals
- `sprint-02-eda` — control flow, dicts, functions, loops exercises (`Conditionals/`, `Dicts/`, `Funciones/`, `bucles/`), plus a `final_project/`
- `sprint-03-eda` — pandas basics (`1_pandas/`), chapter-numbered subfolders (`ch1`...`ch5`)
- `sprint-04-data-wrangling2.0` — dates/strings/timezones, feature engineering, grouping/concatenation, visualization (`s4_ch1`...`s4_ch4`), plus a `final_project/` with CSV datasets (Instacart-style order data)
- `sprint-05-data_statistical-analysis` — descriptive stats, probability theory, hypothesis testing (`ch1`...`ch3`), plus `final_project_megaline_fees/` with CSV datasets
- `sprint-06-module-project-1` — games sales analysis project (`games.csv`, project notebook)
- `sprint-7-softearew-developer-tools` — dev tooling exercises (file/dir handling, JSON, small scripts)
- `sprint-8-sql` — SQL/EDA project correlating weather and ride duration
- `sprint-10-ML` — first ML model training practice

Each sprint/project folder is self-contained: notebooks reference CSV files sitting alongside them (relative paths) or, for the ML sprint, an external `/datasets/` path used by the TripleTen JupyterHub environment. Don't assume shared modules or imports across folders — there are none; each notebook is standalone.

## Working with this repo

- Common libraries used throughout: `pandas`, `numpy`, `matplotlib`/`seaborn`, `scipy.stats`, `requests`, `BeautifulSoup` (bs4), `json`, `math`. No `sklearn` usage yet despite the "ML" sprint name — that notebook currently only loads a CSV with pandas.
- To run a notebook: `jupyter notebook <path>` or open it in VS Code / Cursor with the Jupyter extension. There's no requirements file, so ensure `pandas`, `numpy`, `matplotlib`, `seaborn`, and `scipy` are available in the active Python environment before running.
- `.cursorignore` excludes `.venv/`, `node_modules/`, `.git/`, `datasets/`, `*.csv`, `*.xlsx`, and `.ipynb_checkpoints/` from Cursor's context/indexing — treat these as noise, not signal, when exploring the repo.
- Filenames and folder names are inconsistent (Spanish/English mixed, typos like `softearew`, versioned suffixes like `_ES_updated`) — this reflects iterative coursework, not a naming convention to replicate.
- When editing a notebook, preserve the existing pattern of the specific sprint (e.g., chapter-numbered exercise files vs. one big project notebook) rather than introducing new structure.
