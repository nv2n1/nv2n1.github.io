---
title: "trace-cmd-stack(1)"
name: "trace-cmd-stack"
section: "1"
letter: "t"
url: "/docs/linux/man/1-trace-cmd-stack/"
description: "trace-cmd-stack – read, enable or disable Ftrace Linux kernel stack tracing."
---

<h2 class="name">NAME</h2>
<p> trace-cmd-stack &#8211; read, enable or disable Ftrace Linux kernel stack tracing. </p>
<h2>SYNOPSIS</h2>
<p> <code>trace-cmd stack</code></p>
<h2>DESCRIPTION</h2>
<p> The <a href="/docs/linux/man/1-trace-cmd/">trace-cmd</a>(1) stack enables the Ftrace stack tracer within the kernel. The stack tracer enables the function tracer and at each function call within the kernel, the stack is checked. When a new maximum usage stack is discovered, it is recorded. </p>
<p> When no option is used, the current stack is displayed. </p>
<p> To enable the stack tracer, use the option <code>&#8211;start</code>, and to disable the stack tracer, use the option <code>&#8211;stop</code>. The output will be the maximum stack found since the start was enabled. </p>
<p> Use <code>&#8211;reset</code> to reset the stack counter to zero.</p>
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
