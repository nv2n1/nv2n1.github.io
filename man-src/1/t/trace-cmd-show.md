---
title: "trace-cmd-show(1)"
name: "trace-cmd-show"
section: "1"
letter: "t"
url: "/docs/linux/man/1-trace-cmd-show/"
description: "trace-cmd-show – show the contents of the Ftrace Linux kernel tracing buffer."
---

<h2 class="name">NAME</h2>
<p> trace-cmd-show &#8211; show the contents of the Ftrace Linux kernel tracing buffer. </p>
<h2>SYNOPSIS</h2>
<p> <code>trace-cmd show</code> [<i>OPTIONS</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <a href="/docs/linux/man/1-trace-cmd/">trace-cmd</a>(1) show displays the contents of one of the Ftrace Linux kernel tracing files: trace, snapshot, or trace_pipe. It is basically the equivalent of doing: </p>
<dl>
<dt>
<dd>
<pre>
cat /sys/kernel/debug/tracing/trace
</pre>
</dl>
<h2>OPTIONS</h2>
<p> <code>-p</code></p>
<dl>
<dt>
<dd> Instead of displaying the contents of the &quot;trace&quot; file, use the &quot;trace_pipe&quot; file. The difference between the two is that the &quot;trace&quot; file is static. That is, if tracing is stopped, the &quot;trace&quot; file will show the same contents each time. </p>
<dl>
<dt>
<dd>
<pre>
The &quot;trace_pipe&quot; file is a consuming read, where a read of the file
will consume the output of what was read and it will not read the
same thing a second time even if tracing is stopped. This file
als will block. If no data is available, trace-cmd show will stop
and wait for data to appear.
</pre>
</dl>
</dl>
<p> <code>-s</code></p>
<dl>
<dt>
<dd> Instead of reading the &quot;trace&quot; file, read the snapshot file. The snapshot is made by an application writing into it and the kernel will perform as swap between the currently active buffer and the current snapshot buffer. If no more swaps are made, the snapshot will remain static. This is not a consuming read.</dl>
<p> <code>-c</code> <i>cpu</i></p>
<dl>
<dt>
<dd> Read only the trace file for a specified CPU.</dl>
<p> <code>-f</code></p>
<dl>
<dt>
<dd> Display the full path name of the file that is being displayed.</dl>
<p> <code>-B</code> <i>buf</i></p>
<dl>
<dt>
<dd> If a buffer instance was created, then the <code>-B</code> option will access the files associated with the given buffer.</dl>
<p> <code>&#8211;tracing_on</code></p>
<dl>
<dt>
<dd> Show if tracing is on for the given instance.</dl>
<p> <code>&#8211;current_tracer</code></p>
<dl>
<dt>
<dd> Show what the current tracer is.</dl>
<p> <code>&#8211;buffer_size</code></p>
<dl>
<dt>
<dd> Show the current buffer size (per-cpu)</dl>
<p> <code>&#8211;buffer_total_size</code></p>
<dl>
<dt>
<dd> Show the total size of all buffers.</dl>
<p> <code>&#8211;ftrace_filter</code></p>
<dl>
<dt>
<dd> Show what function filters are set.</dl>
<p> <code>&#8211;ftrace_notrace</code></p>
<dl>
<dt>
<dd> Show what function disabled filters are set.</dl>
<p> <code>&#8211;ftrace_pid</code></p>
<dl>
<dt>
<dd> Show the PIDs the function tracer is limited to (if any).</dl>
<p> <code>&#8211;graph_function</code></p>
<dl>
<dt>
<dd> Show the functions that will be graphed.</dl>
<p> <code>&#8211;graph_notrace</code></p>
<dl>
<dt>
<dd> Show the functions that will not be graphed.</dl>
<p> <code>&#8211;cpumask</code></p>
<dl>
<dt>
<dd> Show the mask of CPUs that tracing will trace.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-trace-cmd/">trace-cmd</a>(1), <a href="/docs/linux/man/1-trace-cmd-record/">trace-cmd-record</a>(1), <a href="/docs/linux/man/1-trace-cmd-report/">trace-cmd-report</a>(1), <a href="/docs/linux/man/1-trace-cmd-start/">trace-cmd-start</a>(1), <a href="/docs/linux/man/1-trace-cmd-extract/">trace-cmd-extract</a>(1), <a href="/docs/linux/man/1-trace-cmd-reset/">trace-cmd-reset</a>(1), <a href="/docs/linux/man/1-trace-cmd-split/">trace-cmd-split</a>(1), <a href="/docs/linux/man/1-trace-cmd-list/">trace-cmd-list</a>(1), <a href="/docs/linux/man/1-trace-cmd-listen/">trace-cmd-listen</a>(1)</p>
<h2>AUTHOR</h2>
<p> Written by Steven Rostedt, &lt;m[blue]<code>rostedt [at] goodmis.org</code>m[]<font SIZE="-2">[1]</font>&gt;</p>
<h2>RESOURCES</h2>
<p> <a href="git://git.kernel.org/pub/scm/linux/kernel/git/rostedt/trace-cmd.git">git://git.kernel.org/pub/scm/linux/kernel/git/rostedt/trace-cmd.git</a></p>
<h2>COPYING</h2>
<p> Copyright (C) 2010 Red Hat, Inc. Free use of this software is granted under the terms of the GNU Public License (GPL).</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> rostedt [at] goodmis.org</p>
<dl>
<dt>
<dd> mailto:rostedt [at] goodmis.org</dl>
</dl>
<h2>Index</h2>
