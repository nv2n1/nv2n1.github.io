---
title: "audit_alloc(9)"
name: "audit_alloc"
section: "9"
letter: "a"
url: "/docs/linux/man/9-audit_alloc/"
---

audit_alloc - allocate an audit context block for a task

<h2>Synopsis</h2>

<pre><code>int audit_alloc(struct task_struct *tsk);</code></pre>

<h2>Arguments</h2>

<i>tsk</i>
<dl><dd><dd>task</dl>

<h2>Description</h2>

Filter on the task information and allocate a per-task audit context if necessary. Doing so turns on system call auditing for the specified task. This is called from copy_process, so no lock is needed.

<h2>Copyright</h2>


