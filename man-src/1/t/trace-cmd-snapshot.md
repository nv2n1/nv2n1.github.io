---
title: "trace-cmd-snapshot(1)"
name: "trace-cmd-snapshot"
section: "1"
letter: "t"
url: "/docs/linux/man/1-trace-cmd-snapshot/"
description: "trace-cmd-snapshot – take, reset, free, or show a Ftrace kernel snapshot"
---

<h2 class="name">NAME</h2>
<p> trace-cmd-snapshot &#8211; take, reset, free, or show a Ftrace kernel snapshot </p>
<h2>SYNOPSIS</h2>
<p> <code>trace-cmd snapshot</code> [<i>OPTIONS</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <a href="/docs/linux/man/1-trace-cmd/">trace-cmd</a>(1) snapshot controls or displays the Ftrace Linux kernel snapshot feature (if the kernel supports it). This is useful to &quot;freeze&quot; an instance of a live trace but without stopping the trace. </p>
<dl>
<dt>
<dd>
<pre><code>
trace - cmd start - p function trace - cmd snapshot - s trace - cmd snapshot[dumps the content of buffer at 'trace-cmd snapshot -s'] trace - cmd snapshot - s trace - cmd snapshot[dumps the new content of the buffer at the last - s operation]
</code></pre>
</dl>
<h2>OPTIONS</h2>
<p> <code>-s</code></p>
<dl>
<dt>
<dd> Take a snapshot of the currently running buffer.</dl>
<p> <code>-r</code></p>
<dl>
<dt>
<dd> Clear out the buffer.</dl>
<p> <code>-f</code></p>
<dl>
<dt>
<dd> Free the snapshot buffer. The buffer takes up memory inside the kernel. It is best to free it when not in use. The first -s operation will allocate it if it is not already allocated.</dl>
<p> <code>-c</code> <i>cpu</i></p>
<dl>
<dt>
<dd> Operate on a per cpu snapshot (may not be fully supported by all kernels)</dl>
<p> <code>-B</code> <i>buf</i></p>
<dl>
<dt>
<dd> If a buffer instance was created, then the <code>-B</code> option will operate on the snapshot within the buffer.</dl>
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
