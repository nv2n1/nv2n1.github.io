---
title: "trace-cmd-stop(1)"
name: "trace-cmd-stop"
section: "1"
letter: "t"
url: "/docs/linux/man/1-trace-cmd-stop/"
description: "trace-cmd-stop – stop the Ftrace Linux kernel tracer from writing to the ring buffer."
---

<h2 class="name">NAME</h2>
<p> trace-cmd-stop &#8211; stop the Ftrace Linux kernel tracer from writing to the ring buffer. </p>
<h2>SYNOPSIS</h2>
<p> <code>trace-cmd stop</code> [<i>OPTIONS</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <a href="/docs/linux/man/1-trace-cmd/">trace-cmd</a>(1) stop is a complement to <i><a href="/docs/linux/man/1-trace-cmd-start/">trace-cmd-start</a>(1)</i>. This will disable Ftrace from writing to the ring buffer. This does not stop the overhead that the tracing may incur. Only the updating of the ring buffer is disabled, the Ftrace tracing may still be inducing overhead. </p>
<p> After stopping the trace, the <i><a href="/docs/linux/man/1-trace-cmd-extract/">trace-cmd-extract</a>(1)</i> may strip out the data from the ring buffer and create a trace.dat file. The Ftrace pseudo file system may also be examined. </p>
<p> To disable the tracing completely to remove the overhead it causes, use <i><a href="/docs/linux/man/1-trace-cmd-reset/">trace-cmd-reset</a>(1)</i>. But after a reset is performed, the data that has been recorded is lost.</p>
<h2>OPTIONS</h2>
<p> <code>-B</code> <i>buffer-name</i></p>
<dl>
<dt>
<dd> If the kernel supports multiple buffers, this will stop the trace for only the given buffer. It does not affect any other buffer. This may be used multiple times to specify different buffers. When this option is used, the top level instance will not be stopped unless <code>-t</code> is given.</dl>
<p> <code>-a</code></p>
<dl>
<dt>
<dd> Stop the trace for all existing buffer instances. When this option is used, the top level instance will not be stopped unless <code>-t</code> is given.</dl>
<p> <code>-t</code></p>
<dl>
<dt>
<dd> Stops the top level instance buffer. Without the <code>-B</code> or <code>-a</code> option this is the same as the default. But if <code>-B</code> or <code>-a</code> is used, this is required if the top level instance buffer should also be stopped.</dl>
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
