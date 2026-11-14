---
title: "trace-cmd-start(1)"
name: "trace-cmd-start"
section: "1"
letter: "t"
url: "/docs/linux/man/1-trace-cmd-start/"
description: "trace-cmd-start – start the Ftrace Linux kernel tracer without recording"
---

<h2 class="name">NAME</h2>
<p> trace-cmd-start &#8211; start the Ftrace Linux kernel tracer without recording </p>
<h2>SYNOPSIS</h2>
<p> <code>trace-cmd start</code> [<i>OPTIONS</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <a href="/docs/linux/man/1-trace-cmd/">trace-cmd</a>(1) start enables all the Ftrace tracing the same way <a href="/docs/linux/man/1-trace-cmd-record/">trace-cmd-record</a>(1) does. The difference is that it does not run threads to create a trace.dat file. This is useful just to enable Ftrace and you are only interested in the trace after some event has occurred and the trace is stopped. Then the trace can be read straight from the Ftrace pseudo file system or can be extracted with <a href="/docs/linux/man/1-trace-cmd-extract/">trace-cmd-extract</a>(1).</p>
<h2>OPTIONS</h2>
<p> The options are the same as <i><a href="/docs/linux/man/1-trace-cmd-record/">trace-cmd-record</a>(1)</i>, except that it does not take options specific to recording (<code>-s</code>, <code>-o</code>, <code>-F</code>, <code>-N</code>, and <code>-t</code>).</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-trace-cmd/">trace-cmd</a>(1), <a href="/docs/linux/man/1-trace-cmd-record/">trace-cmd-record</a>(1), <a href="/docs/linux/man/1-trace-cmd-report/">trace-cmd-report</a>(1), <a href="/docs/linux/man/1-trace-cmd-stop/">trace-cmd-stop</a>(1), <a href="/docs/linux/man/1-trace-cmd-extract/">trace-cmd-extract</a>(1), <a href="/docs/linux/man/1-trace-cmd-reset/">trace-cmd-reset</a>(1), <a href="/docs/linux/man/1-trace-cmd-split/">trace-cmd-split</a>(1), <a href="/docs/linux/man/1-trace-cmd-list/">trace-cmd-list</a>(1), <a href="/docs/linux/man/1-trace-cmd-listen/">trace-cmd-listen</a>(1)</p>
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
