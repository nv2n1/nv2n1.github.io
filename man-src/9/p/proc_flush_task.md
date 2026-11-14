---
title: "proc_flush_task(9)"
name: "proc_flush_task"
section: "9"
letter: "p"
url: "/docs/linux/man/9-proc_flush_task/"
---

proc_flush_task - Remove dcache entries for <i>task</i> from the /proc dcache.

<h2>Synopsis</h2>

<pre><code>void proc_flush_task(struct task_struct *task);</code></pre>

<h2>Arguments</h2>

<i>task</i>
<dl><dd><dd>task that should be flushed.</dl>

<h2>Description</h2>

When flushing dentries from proc, one needs to flush them from global proc (proc_mnt) and from all the namespaces' procs this task was seen in. This call is supposed to do all of this job. 

 Looks in the dcache for /proc/<i>pid</i> /proc/<i>tgid</i>/task/<i>pid</i> if either directory is present flushes it and all of it'ts children from the dcache. 

 It is safe and reasonable to cache /proc entries for a task until that task exits. After that they just clog up the dcache with useless entries, possibly causing useful dcache entries to be flushed instead. This routine is proved to flush those useless dcache entries at process exit time.

<h2>Note</h2>

This routine is just an optimization so it does not guarantee that no dcache entries will exist at process exit time it just makes it very unlikely that any will persist.

<h2>Copyright</h2>


