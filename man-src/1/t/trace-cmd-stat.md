---
title: "trace-cmd-stat(1)"
name: "trace-cmd-stat"
section: "1"
letter: "t"
url: "/docs/linux/man/1-trace-cmd-stat/"
description: "trace-cmd-stat – show the status of the tracing (ftrace) system"
---

<h2 class="name">NAME</h2>
<p> trace-cmd-stat &#8211; show the status of the tracing (ftrace) system </p>
<h2>SYNOPSIS</h2>
<p> <code>trace-cmd stat</code></p>
<h2>DESCRIPTION</h2>
<p> The <a href="/docs/linux/man/1-trace-cmd/">trace-cmd</a>(1) stat displays the various status of the tracing (ftrace) system. The status that it shows is: </p>
<p> <code>Tracer:</code> if one of the tracers (like function_graph) is active. Otherwise nothing is displayed. </p>
<p> <code>Events:</code> Lists the events that are enable. </p>
<p> <code>Event filters:</code> Shows any filters that are set for any events </p>
<p> <code>Function filters:</code> Shows any filters for the function tracers </p>
<p> <code>Graph functions:</code> Shows any functions that the function graph tracer should graph </p>
<p> <code>Buffers:</code> Shows the trace buffer size if they have been expanded. By default, tracing buffers are in a compressed format until they are used. If they are compressed, the buffer display will not be shown. </p>
<p> <code>Trace clock:</code> If the tracing clock is anything other than the default &quot;local&quot; it will be displayed. </p>
<p> <code>Trace CPU mask:</code> If not all available CPUs are in the tracing CPU mask, then the tracing CPU mask will be displayed. </p>
<p> <code>Trace max latency:</code> Shows the value of the trace max latency if it is other than zero. </p>
<p> <code>Kprobes:</code> Shows any kprobes that are defined for tracing. </p>
<p> <code>Uprobes:</code> Shows any uprobes that are defined for tracing.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-trace-cmd/">trace-cmd</a>(1), <a href="/docs/linux/man/1-trace-cmd-record/">trace-cmd-record</a>(1), <a href="/docs/linux/man/1-trace-cmd-report/">trace-cmd-report</a>(1), <a href="/docs/linux/man/1-trace-cmd-start/">trace-cmd-start</a>(1), <a href="/docs/linux/man/1-trace-cmd-stop/">trace-cmd-stop</a>(1), <a href="/docs/linux/man/1-trace-cmd-extract/">trace-cmd-extract</a>(1), <a href="/docs/linux/man/1-trace-cmd-reset/">trace-cmd-reset</a>(1), <a href="/docs/linux/man/1-trace-cmd-split/">trace-cmd-split</a>(1), <a href="/docs/linux/man/1-trace-cmd-listen/">trace-cmd-listen</a>(1)</p>
<h2>AUTHOR</h2>
<p> Written by Steven Rostedt, &lt;m[blue]<code>rostedt [at] goodmis.org</code>m[]<font SIZE="-2">[1]</font>&gt;</p>
<h2>RESOURCES</h2>
<p> <a href="git://git.kernel.org/pub/scm/linux/kernel/git/rostedt/trace-cmd.git">git://git.kernel.org/pub/scm/linux/kernel/git/rostedt/trace-cmd.git</a></p>
<h2>COPYING</h2>
<p> Copyright (C) 2014 Red Hat, Inc. Free use of this software is granted under the terms of the GNU Public License (GPL).</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> rostedt [at] goodmis.org</p>
<dl>
<dt>
<dd> mailto:rostedt [at] goodmis.org</dl>
</dl>
<h2>Index</h2>
