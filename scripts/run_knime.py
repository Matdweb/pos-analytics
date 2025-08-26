#!/usr/bin/env python3
"""
run_knime.py
Simple KNIME workflow trigger script (no external deps).

Usage examples:
  python run_knime.py --knime "/usr/local/knime/knime" --workflow-file "/home/user/exports/MyFlow.knwf"
  python run_knime.py --knime "C:\Program Files\KNIME\knime.exe" --workflow-file "C:\exports\MyFlow.knwf" --log "C:\logs\knime.log"

Notes:
 - You can pass either --workflow-file (recommended: exported .knwf) OR --workflow-dir (a workflow folder in a workspace).
 - The script creates a lock file in the OS temp folder to prevent concurrent runs.
"""
import argparse
import os
import sys
import subprocess
import tempfile
import time
from datetime import datetime

def create_lock(lock_path, max_age_seconds=24*3600):
    # If lock exists and is recent => don't start. If stale => remove it and continue.
    try:
        if os.path.exists(lock_path):
            mtime = os.path.getmtime(lock_path)
            age = time.time() - mtime
            if age > max_age_seconds:
                print(f"[INFO] Found stale lock (age {int(age)}s). Removing and acquiring new lock.")
                try:
                    os.remove(lock_path)
                except Exception as e:
                    print(f"[WARN] Could not remove stale lock: {e}")
                    return False
            else:
                print(f"[ERROR] Lock file exists and is recent (age {int(age)}s). Another run may be active.")
                return False
        # create lock file with PID + timestamp
        with open(lock_path, "w", encoding="utf-8") as f:
            f.write(f"{os.getpid()}\n{datetime.utcnow().isoformat()}Z\n")
        return True
    except Exception as e:
        print(f"[ERROR] create_lock failed: {e}")
        return False

def remove_lock(lock_path):
    try:
        if os.path.exists(lock_path):
            os.remove(lock_path)
    except Exception as e:
        print(f"[WARN] remove_lock failed: {e}")

def main():
    parser = argparse.ArgumentParser(description="Trigger KNIME workflow (batch).")
    parser.add_argument("--knime", required=True, help="Path to knime executable (knime or knime.exe).")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--workflow-file", help="Path to exported .knwf file (recommended).")
    group.add_argument("--workflow-dir", help="Path to workflow folder inside workspace.")
    parser.add_argument("--log", default=None, help="Path to logfile (default: ./knime_run.log)")
    parser.add_argument("--lock-age", type=int, default=24*3600, help="Max age in seconds for stale lock (default: 86400).")
    args = parser.parse_args()

    knime_exe = os.path.abspath(args.knime)
    if not os.path.exists(knime_exe):
        print(f"[ERROR] KNIME executable not found at: {knime_exe}")
        sys.exit(2)

    if args.workflow_file:
        wf_path = os.path.abspath(args.workflow_file)
        if not os.path.exists(wf_path):
            print(f"[ERROR] workflow-file not found: {wf_path}")
            sys.exit(2)
        wf_arg = f"-workflowFile={wf_path}"
        lock_id = os.path.basename(wf_path)
    else:
        wf_dir = os.path.abspath(args.workflow_dir)
        if not os.path.exists(wf_dir):
            print(f"[ERROR] workflow-dir not found: {wf_dir}")
            sys.exit(2)
        wf_arg = f"-workflowDir={wf_dir}"
        lock_id = os.path.basename(wf_dir.rstrip(os.sep))

    log_path = os.path.abspath(args.log) if args.log else os.path.join(os.getcwd(), "knime_run.log")
    lock_path = os.path.join(tempfile.gettempdir(), f"knime_trigger_{lock_id}.lock")

    # Acquire lock
    if not create_lock(lock_path, max_age_seconds=args.lock_age):
        print("Exiting: could not acquire lock.")
        sys.exit(3)

    cmd = [knime_exe, "-nosplash", "-application", "org.knime.product.KNIME_BATCH_APPLICATION", wf_arg, "-consoleLog"]
    start_ts = datetime.utcnow().isoformat() + "Z"
    print(f"[INFO] Starting KNIME run at {start_ts}")
    print(f"[INFO] Command: {' '.join(cmd)}")
    print(f"[INFO] Logging to: {log_path}")

    # Run and append stdout/stderr into log
    try:
        with open(log_path, "a", encoding="utf-8") as logf:
            logf.write(f"\n\n===== KNIME RUN START {start_ts} =====\n")
            logf.write(f"Command: {' '.join(cmd)}\n")
            proc = subprocess.run(cmd, stdout=logf, stderr=logf, check=False)
            rc = proc.returncode
            end_ts = datetime.utcnow().isoformat() + "Z"
            logf.write(f"\n===== KNIME RUN END {end_ts} ReturnCode={rc} =====\n")
    except Exception as e:
        remove_lock(lock_path)
        print(f"[ERROR] Exception while running KNIME: {e}")
        sys.exit(4)

    # Release lock and exit with KNIME exit code
    remove_lock(lock_path)
    print(f"[INFO] KNIME finished with exit code {rc}. See log: {log_path}")
    sys.exit(rc)

if __name__ == "__main__":
    main()
