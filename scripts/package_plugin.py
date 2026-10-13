#!/usr/bin/env python3
"""Build the uploadable plugin zip: plugin root at the zip root, fixed timestamps.

    python3 scripts/package_plugin.py dist/tc-assistant.zip

The zip is what the agent downloads from their loanark.com AI audit page. It installs in
Claude via Customize -> Plugins -> Add -> Upload plugin, and the same file, unzipped, holds
mac-tap/ for the optional Mac text reader. Copy it to the loanark-website repo's
public/downloads/ after every release (see that folder's README).
"""
import pathlib, subprocess, sys, zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKIP_PREFIXES = (".git/", ".github/", "dist/", "runs/")
SKIP_FILES = {".claude-plugin/marketplace.json", "metrics/runs.jsonl"}
STAMP = (2026, 1, 1, 0, 0, 0)


def main():
    out = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ROOT / "dist" / "tc-assistant.zip")
    files = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True,
                           check=True).stdout.split("\n")
    files = sorted(f for f in files if f and not f.startswith(SKIP_PREFIXES) and f not in SKIP_FILES)
    out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for f in files:
            info = zipfile.ZipInfo(f, STAMP)
            mode = (ROOT / f).stat().st_mode & 0o777
            info.external_attr = (0o100000 | mode) << 16  # keep install.sh executable
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, (ROOT / f).read_bytes())
    print(f"{len(files)} files -> {out}")


if __name__ == "__main__":
    main()
