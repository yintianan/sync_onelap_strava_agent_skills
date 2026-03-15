import hashlib
import json
import shutil
import subprocess
import sys
import venv
from pathlib import Path


SKILL_NAME = "onelap-strava-sync"
SCRIPT_DIR = Path(__file__).resolve().parent
REQ_FILE = SCRIPT_DIR / "requirements.txt"
RUNNER = SCRIPT_DIR / "run_sync.py"
STATE_FILE = SCRIPT_DIR / ".bootstrap-state.json"


def _venv_dir() -> Path:
    return Path.home() / ".agents" / "venvs" / SKILL_NAME


def _python_bin(venv_dir: Path) -> Path:
    if sys.platform.startswith("win"):
        return venv_dir / "Scripts" / "python.exe"
    return venv_dir / "bin" / "python"


def _req_hash() -> str:
    return hashlib.sha256(REQ_FILE.read_bytes()).hexdigest()


def _load_state() -> dict:
    if not STATE_FILE.exists():
        return {}
    try:
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _save_state(data: dict) -> None:
    STATE_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")


def _create_venv(venv_dir: Path) -> None:
    venv_dir.parent.mkdir(parents=True, exist_ok=True)
    venv.EnvBuilder(with_pip=True).create(venv_dir)


def _install_requirements(py_bin: Path) -> None:
    subprocess.run(
        [str(py_bin), "-m", "pip", "install", "--upgrade", "pip"], check=True
    )
    subprocess.run(
        [str(py_bin), "-m", "pip", "install", "-r", str(REQ_FILE)], check=True
    )


def _ensure_env() -> Path:
    vdir = _venv_dir()
    py = _python_bin(vdir)
    expected = {"python": sys.version.split()[0], "requirements_sha256": _req_hash()}
    state = _load_state()

    needs_install = not py.exists() or state != expected
    if needs_install:
        if vdir.exists() and not py.exists():
            shutil.rmtree(vdir, ignore_errors=True)
        if not vdir.exists():
            _create_venv(vdir)
            py = _python_bin(vdir)
        try:
            _install_requirements(py)
        except Exception:
            # one rebuild attempt
            shutil.rmtree(vdir, ignore_errors=True)
            _create_venv(vdir)
            py = _python_bin(vdir)
            _install_requirements(py)
        _save_state(expected)

    return py


def main() -> int:
    py = _ensure_env()
    cmd = [str(py), str(RUNNER), *sys.argv[1:]]
    proc = subprocess.run(cmd, cwd=str(SCRIPT_DIR))
    return int(proc.returncode)


if __name__ == "__main__":
    raise SystemExit(main())
