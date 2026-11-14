---
title: "audit_core_dumps(9)"
name: "audit_core_dumps"
section: "9"
letter: "a"
url: "/docs/linux/man/9-audit_core_dumps/"
---

audit_core_dumps - record information about processes that end abnormally

<h2>Synopsis</h2>

<pre><code>void audit_core_dumps(long signr);</code></pre>

<h2>Arguments</h2>

<i>signr</i>
<dl><dd><dd>signal value</dl>

<h2>Description</h2>

If a process ends with a core dump, something fishy is going on and we should record the event for investigation.

<h2>Copyright</h2>


