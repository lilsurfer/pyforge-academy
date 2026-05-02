importScripts('https://cdn.jsdelivr.net/pyodide/v0.26.2/full/pyodide.js');

let rawBuf, statusBuf, textBuf, pyodide;

// Called synchronously when Python reads from stdin.
// Blocks (via Atomics.wait) until the main thread provides input.
function readline() {
  Atomics.store(statusBuf, 0, 1);                      // 1 = waiting
  Atomics.wait(statusBuf, 0, 1, 60000);                // block until ≠ 1
  const len  = Atomics.load(statusBuf, 1);
  const text = new TextDecoder().decode(new Uint8Array(rawBuf, 8, len));
  Atomics.store(statusBuf, 0, 0);                      // 0 = idle
  return text;                                         // includes \n
}

self.onmessage = async function (e) {
  const { type, data } = e.data;

  if (type === 'init') {
    rawBuf    = data.sharedBuf;
    statusBuf = new Int32Array(rawBuf, 0, 2);          // [status, len]
    textBuf   = new Uint8Array(rawBuf, 8);

    pyodide = await loadPyodide({
      stdin:  readline,
      stdout: (t) => self.postMessage({ type: 'stdout', text: t }),
      stderr: (t) => self.postMessage({ type: 'stderr', text: t }),
    });
    self.postMessage({ type: 'ready' });
  }

  if (type === 'run') {
    Atomics.store(statusBuf, 0, 0);
    try {
      await pyodide.runPythonAsync(data.code);
    } catch (err) {
      self.postMessage({ type: 'stderr', text: err.message });
    }
    self.postMessage({ type: 'done' });
  }
};
