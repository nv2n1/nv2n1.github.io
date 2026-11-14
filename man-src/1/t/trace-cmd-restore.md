---
title: "trace-cmd-restore(1)"
name: "trace-cmd-restore"
section: "1"
letter: "t"
url: "/docs/linux/man/1-trace-cmd-restore/"
description: "trace-cmd-restore – restore a failed trace record"
---

<h2 class="name">NAME</h2>
<p> trace-cmd-restore &#8211; restore a failed trace record </p>
<h2>SYNOPSIS</h2>
<p> <code>trace-cmd restore</code> [<i>OPTIONS</i>] [<i>command</i>] cpu-file [cpu-file &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> The <a href="/docs/linux/man/1-trace-cmd/">trace-cmd</a>(1) restore command will restore a crashed <a href="/docs/linux/man/1-trace-cmd-record/">trace-cmd-record</a>(1) file. If for some reason a trace-cmd record fails, it will leave a the per-cpu data files and not create the final trace.dat file. The trace-cmd restore will append the files to create a working trace.dat file that can be read with <a href="/docs/linux/man/1-trace-cmd-report/">trace-cmd-report</a>(1). </p>
<p> When trace-cmd record runs, it spawns off a process per CPU and writes to a per cpu file usually called <i>trace.dat.cpuX</i>, where X represents the CPU number that it is tracing. If the -o option was used in the trace-cmd record, then the CPU data files will have that name instead of the <i>trace.dat</i> name. If a unexpected crash occurs before the tracing is finished, then the per CPU files will still exist but there will not be any trace.dat file to read from. trace-cmd restore will allow you to create a trace.dat file with the existing data files.</p>
<h2>OPTIONS</h2>
<p> <code>-c</code></p>
<dl>
<dt>
<dd> Create a partial trace.dat file from the machine, to be used with a full trace-cmd restore at another time. This option is useful for embedded devices. If a server contains the cpu files of a crashed trace-cmd record (or trace-cmd listen), trace-cmd restore can be executed on the embedded device with the -c option to get all the stored information of that embedded device. Then the file created could be copied to the server to run the trace-cmd restore there with the cpu files. </p>
<dl>
<dt>
<dd>
<pre>
If *-o* is not specified, then the file created will be called
'trace-partial.dat'. This is because the file is not a full version
of something that <a href="//www.systutorials.com/docs/linux/man/1-trace-cmd-report/">trace-cmd-report</a>(1) could use.
</pre>
</dl>
</dl>
<p> <code>-t</code> tracing_dir</p>
<dl>
<dt>
<dd> Used with <code>-c</code>, it overrides the location to read the events from. By default, tracing information is read from the debugfs/tracing directory. <code>-t</code> will use that location instead. This can be useful if the trace.dat file to create is from another machine. Just tar -cvf events.tar debugfs/tracing and copy and untar that file locally, and use that directory instead.</dl>
<p> <code>-k</code> kallsyms</p>
<dl>
<dt>
<dd> Used with <code>-c</code>, it overrides where to read the kallsyms file from. By default, /proc/kallsyms is used. <code>-k</code> will override the file to read the kallsyms from. This can be useful if the trace.dat file to create is from another machine. Just copy the /proc/kallsyms file locally, and use <code>-k</code> to point to that file.</dl>
<p> <code>-o</code> output&#8217;</p>
<dl>
<dt>
<dd> By default, trace-cmd restore will create a <i>trace.dat</i> file (or <i>trace-partial.dat</i> if <code>-c</code> is specified). You can specify a different file to write to with the <code>-o</code> option.</dl>
<p> <code>-i</code> input</p>
<dl>
<dt>
<dd> By default, trace-cmd restore will read the information of the current system to create the initial data stored in the <i>trace.dat</i> file. If the crash was on another machine, then that machine should have the trace-cmd restore run with the <code>-c</code> option to create the trace.dat partial file. Then that file can be copied to the current machine where trace-cmd restore will use <code>-i</code> to load that file instead of reading from the current system.</dl>
<h2>EXAMPLES</h2>
<p> If a crash happened on another box, you could run: </p>
<dl>
<dt>
<dd>
<pre>
$ trace-cmd restore -c -o box-partial.dat
</pre>
</dl>
<p> Then on the server that has the cpu files: </p>
<dl>
<dt>
<dd>
<pre>
$ trace-cmd restore -i box-partial.dat trace.dat.cpu0 trace.dat.cpu1
</pre>
</dl>
<p> This would create a trace.dat file for the embedded box.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-trace-cmd/">trace-cmd</a>(1), <a href="/docs/linux/man/1-trace-cmd-record/">trace-cmd-record</a>(1), <a href="/docs/linux/man/1-trace-cmd-report/">trace-cmd-report</a>(1), <a href="/docs/linux/man/1-trace-cmd-start/">trace-cmd-start</a>(1), <a href="/docs/linux/man/1-trace-cmd-stop/">trace-cmd-stop</a>(1), <a href="/docs/linux/man/1-trace-cmd-extract/">trace-cmd-extract</a>(1), <a href="/docs/linux/man/1-trace-cmd-reset/">trace-cmd-reset</a>(1), <a href="/docs/linux/man/1-trace-cmd-split/">trace-cmd-split</a>(1), <a href="/docs/linux/man/1-trace-cmd-list/">trace-cmd-list</a>(1), <a href="/docs/linux/man/1-trace-cmd-listen/">trace-cmd-listen</a>(1)</p>
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
