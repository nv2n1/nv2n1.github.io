---
title: "trace-cmd(1)"
name: "trace-cmd"
section: "1"
letter: "t"
url: "/docs/linux/man/1-trace-cmd/"
description: "trace-cmd – interacts with Ftrace Linux kernel internal tracer"
---

<h2 class="name">NAME</h2>
<p> trace-cmd &#8211; interacts with Ftrace Linux kernel internal tracer </p>
<h2>SYNOPSIS</h2>
<p> <code>trace-cmd</code> <i>COMMAND</i> [<i>OPTIONS</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <a href="/docs/linux/man/1-trace-cmd/">trace-cmd</a>(1) command interacts with the Ftrace tracer that is built inside the Linux kernel. It interfaces with the Ftrace specific files found in the debugfs file system under the tracing directory. A <i>COMMAND</i> must be specified to tell trace-cmd what to do.</p>
<h2>COMMANDS</h2>
<dl>
<dt>
<dd>
<pre>
record  - record a live trace and write a trace.dat file to the
          local disk or to the network.
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
report  - reads a trace.dat file and converts the binary data to a
          ASCII text readable format.
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
hist    - show a histogram of the events.
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
stat    - show tracing (ftrace) status of the running system
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
options - list the plugin options that are available to *report*
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
start   - start the tracing without recording to a trace.dat file.
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
stop    - stop tracing (only disables recording, overhead of tracer
          is still in effect)
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
restart - restart tracing from a previous stop (only effects recording)
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
extract - extract the data from the kernel buffer and create a trace.dat
          file.
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
reset   - disables all tracing and gives back the system performance.
          (clears all data from the kernel buffers)
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
split   - splits a trace.dat file into smaller files.
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
list    - list the available plugins or events that can be recorded.
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
listen  - open up a port to listen for remote tracing connections.
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
restore - restore the data files of a crashed run of trace-cmd record
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
stack   - run and display the stack tracer
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
check-events - parse format strings for all trace events and return
               whether all formats are parseable
</pre>
</dl>
<h2>OPTIONS</h2>
<p> <code>-h</code>, &#8211;help</p>
<dl>
<dt>
<dd> Display the help text.</dl>
<p> Other options see the man page for the corresponding command.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-trace-cmd-record/">trace-cmd-record</a>(1), <a href="/docs/linux/man/1-trace-cmd-report/">trace-cmd-report</a>(1), <a href="/docs/linux/man/1-trace-cmd-hist/">trace-cmd-hist</a>(1), <a href="/docs/linux/man/1-trace-cmd-start/">trace-cmd-start</a>(1), <a href="/docs/linux/man/1-trace-cmd-stop/">trace-cmd-stop</a>(1), <a href="/docs/linux/man/1-trace-cmd-extract/">trace-cmd-extract</a>(1), <a href="/docs/linux/man/1-trace-cmd-reset/">trace-cmd-reset</a>(1), <a href="/docs/linux/man/1-trace-cmd-restore/">trace-cmd-restore</a>(1), <a href="/docs/linux/man/1-trace-cmd-stack/">trace-cmd-stack</a>(1), <a href="/docs/linux/man/1-trace-cmd-split/">trace-cmd-split</a>(1), <a href="/docs/linux/man/1-trace-cmd-list/">trace-cmd-list</a>(1), <a href="/docs/linux/man/1-trace-cmd-listen/">trace-cmd-listen</a>(1), <a href="/docs/linux/man/5-trace-cmd-dat/">trace-cmd.dat</a>(5), <a href="/docs/linux/man/1-trace-cmd-check-events/">trace-cmd-check-events</a>(1) <a href="/docs/linux/man/1-trace-cmd-stat/">trace-cmd-stat</a>(1)</p>
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
