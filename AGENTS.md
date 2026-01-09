# Repository Guidelines

## Project Structure & Module Organization
`robojudo/` is the installable package and houses modular subpackages: `controller/` for input devices, `environment/` for sim and hardware backends, `policy/` for pretrained behaviors, and `pipeline/` orchestration classes used by `scripts/run_pipeline.py`. Config presets live in `robojudo/config/`, docs and diagrams in `docs/`, assets for media in `assets/`, and verification lives under `tests/`. Keep large binaries in `logs/` or `third_party/` out of source control.

## Build, Test, and Development Commands
- `uv venv .venv && source .venv/bin/activate`: create the standard Python 3.11+ env (prefer `uv` over other managers).
- `uv pip install -e .` installs RoboJuDo plus `requirements.txt`; add `uv pip install -r requirements-dev.txt` if the team introduces more dev dependencies later.
- `python submodule_install.py` installs optional modules declared in `submodule_cfg.yaml` (use flags to narrow installs when testing a single robot stack).
- `python scripts/run_pipeline.py --config g1` runs the default RL pipeline; swap `g1` for any class defined in `robojudo/config/config_manager.py` to target other robots.
- `pre-commit run --all-files` mirrors CI’s Ruff format-and-lint pass.

## Coding Style & Naming Conventions
Follow Ruff’s configuration (`pyproject.toml`): 120-char lines, Python 3.10 syntax target, and lint rules `E,F,I,B,UP`. Modules prefer snake_case names, config classes remain PascalCase (e.g., `G1MimicCfg`). Type hints are expected for all public functions, and logging must use the `robojudo` logger hierarchy. Keep imports sorted and rely on Ruff’s formatter rather than ad-hoc styling.

## Testing Guidelines
Tests live in `tests/` and should mirror the package layout (`tests/pipeline/test_*.py`, etc.). Name files `test_<feature>.py` and functions `test_<behavior>()`. Run `pytest` (add `-k policy` or `-vv` as needed) after any Python change; CI assumes a clean `pytest` run with no skips unless documented. Include fixtures that stub real-robot dependencies so unit tests stay hardware-agnostic.

## Commit & Pull Request Guidelines
Commits follow the short, imperative style already in `git log` (“Add Atom robot configuration”, “fix link in doc”). Keep focused diffs, reference issues with `Fixes #123`, and include pipeline/test results in the PR description. Every PR should state the target robot/policy, list config changes, and attach screenshots or logs when touching operator-facing assets.

## Security & Configuration Tips
Avoid committing credentials—robot endpoints and SDK tokens belong in local `.env` files referenced by configs. When enabling hardware control, audit the corresponding section in `submodule_cfg.yaml` and document safety interlocks in the PR. Use `logs/` for runtime traces and scrub personal data before sharing traces externally.
