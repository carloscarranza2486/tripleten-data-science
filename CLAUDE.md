# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository purpose

Personal learning portfolio for the TripleTen Data Science bootcamp (see `README.md`: "Mi Portafolio de Data Science - TripleTen"). It is a collection of Jupyter notebooks and standalone Python scripts completed as coursework — not a deployable application or library. There is no build system, package manifest (no `requirements.txt`/`pyproject.toml`), linter config, or test suite; work is done and evaluated interactively inside notebooks.

## Structure

Content is organized by sprint (course module), roughly in chronological/curriculum order:

- `sprint-01-python` — Python fundamentals
- `sprint-02-eda` — control flow, dicts, functions, loops exercises, plus a `final_project/`
- `sprint-03-eda` — pandas basics, chapter-numbered subfolders
- `sprint-04-data-wrangling2.0` — dates/strings/timezones, feature engineering, grouping/concatenation, visualization (`s4_ch1`...`s4_ch4`), plus a `final_project/` (Instacart-style order data)
- `sprint-05-data_statistical-analysis` — descriptive stats, probability, hypothesis testing (`ch1`...`ch3`), plus `final_project_megaline_fees/`
- `sprint-06-module-project-1` — games sales analysis project (`games.csv`)
- `sprint-7-softearew-developer-tools` — dev tooling exercises (file/dir handling, JSON, small scripts)
- `sprint-8-sql` — SQL/EDA project correlating weather and ride duration
- `sprint-10-ML` — first supervised model (Megaline plan recommendation, `users_behavior.csv`)
- `sprint-11-supervised-learning` — Beta Bank churn, class imbalance + F1/AUC-ROC (`Churn.csv`)
- `sprint_12_aprendizaje_automático_en_negocios` — ML for business (OilyGiant: region selection for 200 wells, linear regression + bootstrapping for profit/risk, `geo_data_0/1/2.csv`)
- `sprint-13-module-project-2` — gold recovery (Zyfra): recovery-formula check, sMAPE, cross-validated regression. The folder holds only `README.md` (the project brief, in Spanish) and an empty `notebook.ipynb`; **the `gold_recovery_train/test/full.csv` files are not in the repo**, so this one can only be run on the platform until they are downloaded locally.

Each sprint folder is self-contained. There are **no shared modules or imports across folders** — every notebook is standalone and re-imports what it needs.

## Running notebooks

`jupyter notebook <path>`, or open in VS Code / Cursor with the Jupyter extension.

Two environments matter and they are not the same:

- **Local (macOS, `~/miniconda3`)** — has `pandas`, `numpy`, `matplotlib`, `seaborn`; **`sklearn` and `scipy` are not installed**. So the ML sprints (10, 11, 12, 13) cannot be executed locally as-is; install into the active env first, or treat the platform as the execution target.
- **TripleTen JupyterHub** — where projects are actually run and graded. Datasets live at the absolute path `/datasets/<file>.csv`, and its library versions are **older than local**. Code that works on the Mac can raise on the grader (e.g. `ax.spines[['top','right']]` needs matplotlib ≥ 3.4 and had to be split into per-key calls — commit `9d01e94`). Prefer conservative, widely-supported API forms in notebook code.

## Notebook conventions (follow these when adding or editing)

- **Dual dataset path.** Project notebooks load data so they run in both environments. When a notebook reads several files, this is factored into one helper (sprint 12):
  ```python
  def cargar_datos(nombre_archivo):
      try:
          datos = pd.read_csv(nombre_archivo)          # local
      except FileNotFoundError:
          datos = pd.read_csv(f'/datasets/{nombre_archivo}')  # plataforma
      return datos
  ```
  For a single file an inline `try`/`except FileNotFoundError` around the two paths is used instead (sprint 11). Either order of the two paths is fine; older sprints hardcode one form.
- **Project narrative structure**, in Spanish: `# Proyecto: <título>` → `## Objetivo general` → numbered `## Paso N: ...` sections (sprint 12 uses `## Etapa N:`; match whichever the notebook already uses), each opening with a bold `**Objetivo:**` line and closing with a bold `**Conclusión:**` line that cites the actual numbers produced by the cells → `## Conclusiones generales` at the end. Conclusions must match the output the platform produced, not local output.
- **Comments and prose are in Spanish**, including short inline comments on import lines and on non-obvious steps. Identifiers mix Spanish and English (`modelo_final`, `features`, `importancias`).
- **`random_state=12345`** everywhere splits or models are seeded — keep it unless a chapter exercise specifies otherwise.
- Charts are plain matplotlib on an explicit `fig, ax = plt.subplots(...)`, with axis labels, titles and value annotations written in Spanish.
- **Edit notebooks cell by cell (`NotebookEdit`), never regenerate the file.** A full rewrite has already destroyed hand-written edits once. Recent sprint projects live in a single `notebook.ipynb` per folder (sprint 11 names it `beta_bank_project.ipynb`), next to a `README.md` holding the platform's brief in Spanish — read that brief before building the notebook; its numbered instructions are the section outline.
- Chapter/exercise notebooks (`chN_*`, `s4_chN`) are throwaway practice and don't carry the project narrative — keep them as they are.
- Filenames and folder names are inconsistent (Spanish/English mixed, typos like `softearew`, accented folder names) — this reflects iterative coursework, not a convention to replicate or "fix".

## Git

- Commit subjects use a capitalized prefix: `Built:`, `Fix:`, `Docs:`, `Refactor:`, `Feature:`, followed by what changed. Bodies explain the why when the change is non-obvious (see `9d01e94`).
- `.gitignore` covers `.DS_Store`, `Thumbs.db`, `__pycache__/`, `*.pyc`, `.ipynb_checkpoints/`, and `learning_material/` (the bootcamp's own chapter-summary PDFs, e.g. under sprint 12 — never commit or quote those). CSVs **are** committed alongside their notebooks.
- `.cursorignore` excludes `.venv/`, `node_modules/`, `.git/`, `datasets/`, `*.csv`, `*.xlsx`, `.ipynb_checkpoints/` — treat those as noise when exploring.
