---
title: "trace-cmd-hist(1)"
name: "trace-cmd-hist"
section: "1"
letter: "t"
url: "/docs/linux/man/1-trace-cmd-hist/"
description: "trace-cmd-hist – show histogram of events in trace.dat file"
---

<h2 class="name">NAME</h2>
<p> trace-cmd-hist &#8211; show histogram of events in trace.dat file </p>
<h2>SYNOPSIS</h2>
<p> <code>trace-cmd hist</code> [<i>OPTIONS</i>][<i>input-file</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <a href="/docs/linux/man/1-trace-cmd/">trace-cmd</a>(1) hist displays a histogram form from the trace.dat file. Instead of showing the events as they were ordered, it creates a histogram that can be displayed per task or for all tasks where the most common events appear first. It uses the function tracer and call stacks that it finds to try to put together a call graph of the events.</p>
<h2>OPTIONS</h2>
<p> <code>-i</code> <i>input-file</i></p>
<dl>
<dt>
<dd> By default, trace-cmd hist will read the file <i>trace.dat</i>. But the <code>-i</code> option open up the given <i>input-file</i> instead. Note, the input file may also be specified as the last item on the command line.</dl>
<p> <code>-P</code></p>
<dl>
<dt>
<dd> To compact all events and show the call graphs by ignoring tasks and different PIDs, add the <code>-P</code> to do so. Instead of showing the task name, it will group all chains together and show &quot;&lt;all pids&gt;&quot;.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-trace-cmd/">trace-cmd</a>(1), <a href="/docs/linux/man/1-trace-cmd-record/">trace-cmd-record</a>(1), <a href="/docs/linux/man/1-trace-cmd-report/">trace-cmd-report</a>(1), <a href="/docs/linux/man/1-trace-cmd-start/">trace-cmd-start</a>(1), <a href="/docs/linux/man/1-trace-cmd-stop/">trace-cmd-stop</a>(1), <a href="/docs/linux/man/1-trace-cmd-extract/">trace-cmd-extract</a>(1), <a href="/docs/linux/man/1-trace-cmd-reset/">trace-cmd-reset</a>(1), <a href="/docs/linux/man/1-trace-cmd-split/">trace-cmd-split</a>(1), <a href="/docs/linux/man/1-trace-cmd-listen/">trace-cmd-listen</a>(1)</p>
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
