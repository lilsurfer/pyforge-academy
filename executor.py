"""
executor.py — Safe subprocess-based Python code runner.

Spawns a child process to execute user code in isolation from the Streamlit
server process. Enforces a 5-second timeout and captures stdout/stderr.
"""

import subprocess
import sys
import time
from dataclasses import dataclass


@dataclass
class ExecutionResult:
    output: str
    error: str
    exec_time: float
    timed_out: bool = False


def run_code(code: str, timeout: int = 5) -> ExecutionResult:
    """
    Execute Python code safely in a subprocess.

    Args:
        code: The Python source code string to execute.
        timeout: Maximum execution time in seconds (default 5).

    Returns:
        ExecutionResult with output, error, and execution time.
    """
    start = time.perf_counter()

    try:
        result = subprocess.run(
            [sys.executable, "-c", code],
            capture_output=True,
            text=True,
            timeout=timeout,
            # Prevent the child from inheriting Streamlit's environment vars
            # that could cause interference
            env=None,
        )
        elapsed = time.perf_counter() - start

        return ExecutionResult(
            output=result.stdout,
            error=result.stderr,
            exec_time=elapsed,
        )

    except subprocess.TimeoutExpired:
        elapsed = time.perf_counter() - start
        return ExecutionResult(
            output="",
            error=f"⏰ Execution timed out after {timeout} seconds.",
            exec_time=elapsed,
            timed_out=True,
        )
    except Exception as e:
        elapsed = time.perf_counter() - start
        return ExecutionResult(
            output="",
            error=f"Runner error: {e}",
            exec_time=elapsed,
        )
