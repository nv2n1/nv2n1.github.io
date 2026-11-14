---
title: "trace-cmd-split(1)"
name: "trace-cmd-split"
section: "1"
letter: "t"
url: "/docs/linux/man/1-trace-cmd-split/"
description: "trace-cmd-split – split a trace.dat file into smaller files"
---

<h2 class="name">NAME</h2>
<p> trace-cmd-split &#8211; split a trace.dat file into smaller files </p>
<h2>SYNOPSIS</h2>
<p> <code>trace-cmd split</code> [<i>OPTIONS</i>] [<i>start-time</i> [<i>end-time</i>]]</p>
<h2>DESCRIPTION</h2>
<p> The <a href="/docs/linux/man/1-trace-cmd/">trace-cmd</a>(1) split is used to break up a trace.dat into small files. The <i>start-time</i> specifies where the new file will start at. Using <i><a href="/docs/linux/man/1-trace-cmd-report/">trace-cmd-report</a>(1)</i> and copying the time stamp given at a particular event, can be used as input for either <i>start-time</i> or <i>end-time</i>. The split will stop creating files when it reaches an event after <i>end-time</i>. If only the end-time is needed, use 0.0 as the start-time. </p>
<p> If start-time is left out, then the split will start at the beginning of the file. If end-time is left out, then split will continue to the end unless it meets one of the requirements specified by the options.</p>
<h2>OPTIONS</h2>
<p> <code>-i</code> <i>file</i></p>
<dl>
<dt>
<dd> If this option is not specified, then the split command will look for the file named <i>trace.dat</i>. This options will allow the reading of another file other than <i>trace.dat</i>.</dl>
<p> <code>-o</code> <i>file</i></p>
<dl>
<dt>
<dd> By default, the split command will use the input file name as a basis of where to write the split files. The output file will be the input file with an attached &#8216;.#\&#8217; to the end: trace.dat.1, trace.dat.2, etc. </p>
<dl>
<dt>
<dd>
<pre>
This option will change the name of the base file used.
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
-o file  will create file.1, file.2, etc.
</pre>
</dl>
</dl>
<p> <code>-s</code> <i>seconds</i></p>
<dl>
<dt>
<dd> This specifies how many seconds should be recorded before the new file should stop.</dl>
<p> <code>-m</code> <i>milliseconds</i></p>
<dl>
<dt>
<dd> This specifies how many milliseconds should be recorded before the new file should stop.</dl>
<p> <code>-u</code> <i>microseconds</i></p>
<dl>
<dt>
<dd> This specifies how many microseconds should be recorded before the new file should stop.</dl>
<p> <code>-e</code> <i>events</i></p>
<dl>
<dt>
<dd> This specifies how many events should be recorded before the new file should stop.</dl>
<p> <code>-p</code> <i>pages</i></p>
<dl>
<dt>
<dd> This specifies the number of pages that should be recorded before the new file should stop. </p>
<dl>
<dt>
<dd>
<pre>
Note: only one of *-p*, *-e*, *-u*, *-m*, *-s* may be specified at a time.
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
If *-p* is specified, then *-c* is automatically set.
</pre>
</dl>
</dl>
<p> <code>-r</code></p>
<dl>
<dt>
<dd> This option causes the break up to repeat until end-time is reached (or end of the input if end-time is not specified). </p>
<dl>
<dt>
<dd>
<pre>
trace-cmd split -r -e 10000
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
This will break up trace.dat into several smaller files, each with at most
10,000 events in it.
</pre>
</dl>
</dl>
<p> <code>-c</code></p>
<dl>
<dt>
<dd> This option causes the above break up to be per CPU. </p>
<dl>
<dt>
<dd>
<pre>
trace-cmd split -c -p 10
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
This will create a file that has 10 pages per each CPU from the input.
</pre>
</dl>
</dl>
<p> <code>-C</code> <i>cpu</i></p>
<dl>
<dt>
<dd> This option will split for a single CPU. Only the cpu named will be extracted from the file. </p>
<dl>
<dt>
<dd>
<pre>
trace-cmd split -C 1
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
This will split out all the events for cpu 1 in the file.
</pre>
</dl>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-trace-cmd/">trace-cmd</a>(1), <a href="/docs/linux/man/1-trace-cmd-record/">trace-cmd-record</a>(1), <a href="/docs/linux/man/1-trace-cmd-report/">trace-cmd-report</a>(1), <a href="/docs/linux/man/1-trace-cmd-start/">trace-cmd-start</a>(1), <a href="/docs/linux/man/1-trace-cmd-stop/">trace-cmd-stop</a>(1), <a href="/docs/linux/man/1-trace-cmd-extract/">trace-cmd-extract</a>(1), <a href="/docs/linux/man/1-trace-cmd-reset/">trace-cmd-reset</a>(1), <a href="/docs/linux/man/1-trace-cmd-list/">trace-cmd-list</a>(1), <a href="/docs/linux/man/1-trace-cmd-listen/">trace-cmd-listen</a>(1)</p>
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
