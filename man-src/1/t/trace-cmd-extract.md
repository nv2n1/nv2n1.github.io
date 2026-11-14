---
title: "trace-cmd-extract(1)"
name: "trace-cmd-extract"
section: "1"
letter: "t"
url: "/docs/linux/man/1-trace-cmd-extract/"
description: "trace-cmd-extract – extract out the data from the Ftrace Linux tracer."
---

<h2 class="name">NAME</h2>
<p> trace-cmd-extract &#8211; extract out the data from the Ftrace Linux tracer. </p>
<h2>SYNOPSIS</h2>
<p> <code>trace-cmd extract [</code><i>OPTIONS</i><code>]</code></p>
<h2>DESCRIPTION</h2>
<p> The <a href="/docs/linux/man/1-trace-cmd/">trace-cmd</a>(1) extract is usually used after <i><a href="/docs/linux/man/1-trace-cmd-start/">trace-cmd-start</a>(1)</i> and <i><a href="/docs/linux/man/1-trace-cmd-stop/">trace-cmd-stop</a>(1)</i>. It can be used after the Ftrace tracer has been started manually through the Ftrace pseudo file system. </p>
<p> The extract command creates a trace.dat file that can be used by <i><a href="/docs/linux/man/1-trace-cmd-report/">trace-cmd-report</a>(1)</i> to read from. It reads the kernel internal ring buffer to produce the trace.dat file.</p>
<h2>OPTIONS</h2>
<p> <code>-p</code> <i>plugin</i></p>
<dl>
<dt>
<dd> Although <code>extract</code> does not start any traces, some of the plugins require just reading the output in ASCII format. These are the latency tracers, since the latency tracers have a separate internal buffer. The plugin option is therefore only necessary for the <i>wakeup</i>, <i>wakeup-rt</i>, <i>irqsoff</i>, <i>preemptoff</i> and <i>preemptirqsoff</i> plugins. </p>
<dl>
<dt>
<dd>
<pre>
With out this option, the extract command will extract from the internal
Ftrace buffers.
</pre>
</dl>
</dl>
<p> <code>-O</code> <i>option</i></p>
<dl>
<dt>
<dd> If a latency tracer is being extracted, and the <code>-p</code> option is used, then there are some Ftrace options that can change the format. This will update those options before extracting. To see the list of options see <i>trace-cmd-list</i>. To enable an option, write its name, to disable the option append the characters <i>no</i> to it. For example: <i>noprint-parent</i> will disable the <i>print-parent</i> option that prints the parent function in printing a function event.</dl>
<p> <code>-o</code> <i>outputfile</i></p>
<dl>
<dt>
<dd> By default, the extract command will create a <i>trace.dat</i> file. This option will change where the file is written to.</dl>
<p> <code>-s</code></p>
<dl>
<dt>
<dd> Extract from the snapshot buffer (if the kernel supports it).</dl>
<p> <code>&#8211;date</code></p>
<dl>
<dt>
<dd> This is the same as the <a href="/docs/linux/man/1-trace-cmd-record/">trace-cmd-record</a>(1) &#8211;date option, but it does cause the extract routine to disable all tracing. That is, the end of the extract will perform something similar to <a href="/docs/linux/man/1-trace-cmd-reset/">trace-cmd-reset</a>(1).</dl>
<p> <code>-B</code> <i>buffer-name</i></p>
<dl>
<dt>
<dd> If the kernel supports multiple buffers, this will extract the trace for only the given buffer. It does not affect any other buffer. This may be used multiple times to specify different buffers. When this option is used, the top level instance will not be extracted unless <code>-t</code> is given.</dl>
<p> <code>-a</code></p>
<dl>
<dt>
<dd> Extract all existing buffer instances. When this option is used, the top level instance will not be extracted unless <code>-t</code> is given.</dl>
<p> <code>-t</code></p>
<dl>
<dt>
<dd> Extracts the top level instance buffer. Without the <code>-B</code> or <code>-a</code> option this is the same as the default. But if <code>-B</code> or <code>-a</code> is used, this is required if the top level instance buffer should also be extracted.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-trace-cmd/">trace-cmd</a>(1), <a href="/docs/linux/man/1-trace-cmd-record/">trace-cmd-record</a>(1), <a href="/docs/linux/man/1-trace-cmd-report/">trace-cmd-report</a>(1), <a href="/docs/linux/man/1-trace-cmd-start/">trace-cmd-start</a>(1), <a href="/docs/linux/man/1-trace-cmd-stop/">trace-cmd-stop</a>(1), <a href="/docs/linux/man/1-trace-cmd-reset/">trace-cmd-reset</a>(1), <a href="/docs/linux/man/1-trace-cmd-split/">trace-cmd-split</a>(1), <a href="/docs/linux/man/1-trace-cmd-list/">trace-cmd-list</a>(1), <a href="/docs/linux/man/1-trace-cmd-listen/">trace-cmd-listen</a>(1)</p>
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
