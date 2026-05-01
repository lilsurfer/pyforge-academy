"""
executor.py — Wasm-compatible safe Python executor.
Uses exec() instead of subprocess (subprocess is not available in Pyodide/stlite).
"""
import sys
import io
import time
import traceback
from dataclasses import dataclass


@dataclass
class ExecutionResult:
    output: str
    error: str
    exec_time: float
    timed_out: bool = False


def run_code(code: str, timeout: int = 5) -> ExecutionResult:
    start = time.perf_counter()
    old_stdout = sys.stdout
    captured = io.StringIO()
    sys.stdout = captured
    error = ""
    try:
        exec(code, {"__name__": "__main__"})
    except Exception:
        error = traceback.format_exc()
    finally:
        sys.stdout = old_stdout  # ALWAYS restore — was bugged before
    return ExecutionResult(
        output=captured.getvalue(),
        error=error,
        exec_time=time.perf_counter() - start,
    )
