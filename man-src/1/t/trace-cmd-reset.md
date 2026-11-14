---
title: "trace-cmd-reset(1)"
name: "trace-cmd-reset"
section: "1"
letter: "t"
url: "/docs/linux/man/1-trace-cmd-reset/"
description: "trace-cmd-reset – turn off all Ftrace tracing to bring back full performance"
---

<h2 class="name">NAME</h2>
<p> trace-cmd-reset &#8211; turn off all Ftrace tracing to bring back full performance </p>
<h2>SYNOPSIS</h2>
<p> <code>trace-cmd reset</code> [<i>OPTIONS</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <a href="/docs/linux/man/1-trace-cmd/">trace-cmd</a>(1) reset command turns off all tracing of Ftrace. This will bring back the performance of the system before tracing was enabled. This is necessary since <i><a href="/docs/linux/man/1-trace-cmd-record/">trace-cmd-record</a>(1)</i>, <i><a href="/docs/linux/man/1-trace-cmd-stop/">trace-cmd-stop</a>(1)</i> and <i><a href="/docs/linux/man/1-trace-cmd-extract/">trace-cmd-extract</a>(1)</i> do not disable the tracer, event after the data has been pulled from the buffers. The rational is that the user may want to manually enable the tracer with the Ftrace pseudo file system, or examine other parts of Ftrace to see what trace-cmd did. After the reset command happens, the data in the ring buffer, and the options that were used are all lost.</p>
<h2>OPTIONS</h2>
<p> Please note that the order that options are specified on the command line is significant. See EXAMPLES. </p>
<p> <code>-b</code> <i>buffer_size</i></p>
<dl>
<dt>
<dd> When the kernel boots, the Ftrace ring buffer is of a minimal size (3 pages per CPU). The first time the tracer is used, the ring buffer size expands to what it was set for (default 1.4 Megs per CPU). </p>
<dl>
<dt>
<dd>
<pre>
If no more tracing is to be done, this option allows you to shrink the
ring buffer down to free up available memory.
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
trace-cmd reset -b 1
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
The buffer instance affected is the one (or ones) specified by the most
recently preceding *-B*, *-t*, or *-a* option:
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
When used after *-B*, resizes the buffer instance that precedes it on
the command line.
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
When used after *-a*, resizes all buffer instances except the top one.
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
When used after *-t* or before any *-B* or *-a*, resizes the top
instance.
</pre>
</dl>
</dl>
<p> <code>-B</code> <i>buffer-name</i></p>
<dl>
<dt>
<dd> If the kernel supports multiple buffers, this will reset the trace for only the given buffer. It does not affect any other buffer. This may be used multiple times to specify different buffers. The top level buffer will not be reset if this option is given (unless the <code>-t</code> option is also supplied).</dl>
<p> <code>-a</code></p>
<dl>
<dt>
<dd> Reset the trace for all existing buffer instances. When this option is used, the top level instance will not be reset unless <code>-t</code> is given.</dl>
<p> <code>-d</code></p>
<dl>
<dt>
<dd> This option deletes the instance buffer(s) specified by the most recently preceding <code>-B</code> or <code>-a</code> option. Because the top-level instance buffer cannot be deleted, it is invalid to use this immediatly following <code>-t</code> or prior to any <code>-B</code> or <code>-a</code> option on the command line.</dl>
<p> <code>-t</code></p>
<dl>
<dt>
<dd> Resets the top level instance buffer. Without the <code>-B</code> or <code>-a</code> option this is the same as the default. But if <code>-B</code> or <code>-a</code> is used, this is required if the top level instance buffer should also be reset.</dl>
<h2>EXAMPLES</h2>
<p> Reset tracing for instance-one and set its per-cpu buffer size to 4096kb. Also deletes instance-two. The top level instance and any other instances remain unaffected: </p>
<dl>
<dt>
<dd>
<pre>
trace-cmd reset -B instance-one -b 4096 -B instance-two -d
</pre>
</dl>
<p> Delete all instance buffers. Top level instance remains unaffected: </p>
<dl>
<dt>
<dd>
<pre>
trace-cmd reset -a -d
</pre>
</dl>
<p> Delete all instance buffers and also reset the top instance: </p>
<dl>
<dt>
<dd>
<pre>
trace-cmd reset -t -a -d
</pre>
</dl>
<p> Invalid. This command implies an attempt to delete the top instance: </p>
<dl>
<dt>
<dd>
<pre>
trace-cmd reset -a -t -d
</pre>
</dl>
<p> Reset the top instance and set its per-cpu buffer size to 1024kb. If any instance buffers exist, they will be unaffected: </p>
<dl>
<dt>
<dd>
<pre>
trace-cmd reset -b 1024
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-trace-cmd/">trace-cmd</a>(1), <a href="/docs/linux/man/1-trace-cmd-record/">trace-cmd-record</a>(1), <a href="/docs/linux/man/1-trace-cmd-report/">trace-cmd-report</a>(1), <a href="/docs/linux/man/1-trace-cmd-start/">trace-cmd-start</a>(1), <a href="/docs/linux/man/1-trace-cmd-stop/">trace-cmd-stop</a>(1), <a href="/docs/linux/man/1-trace-cmd-extract/">trace-cmd-extract</a>(1), <a href="/docs/linux/man/1-trace-cmd-split/">trace-cmd-split</a>(1), <a href="/docs/linux/man/1-trace-cmd-list/">trace-cmd-list</a>(1), <a href="/docs/linux/man/1-trace-cmd-listen/">trace-cmd-listen</a>(1)</p>
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
