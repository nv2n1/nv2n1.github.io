---
title: "trace-cmd-listen(1)"
name: "trace-cmd-listen"
section: "1"
letter: "t"
url: "/docs/linux/man/1-trace-cmd-listen/"
description: "trace-cmd-listen – listen for incoming connection to record tracing."
---

<h2 class="name">NAME</h2>
<p> trace-cmd-listen &#8211; listen for incoming connection to record tracing. </p>
<h2>SYNOPSIS</h2>
<p> <code>trace-cmd listen</code> -p <i>port</i> [<i>OPTIONS</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <a href="/docs/linux/man/1-trace-cmd/">trace-cmd</a>(1) listen sets up a port to listen to waiting for connections from other hosts that run <i><a href="/docs/linux/man/1-trace-cmd-record/">trace-cmd-record</a>(1)</i> with the <code>-N</code> option. When a connection is made, and the remote host sends data, it will create a file called <i>trace.HOST:PORT.dat</i>. Where HOST is the name of the remote host, and PORT is the port that the remote host used to connect with.</p>
<h2>OPTIONS</h2>
<p> <code>-p</code> <i>port</i></p>
<dl>
<dt>
<dd> This option will specify the port to listen to.</dl>
<p> <code>-D</code></p>
<dl>
<dt>
<dd> This options causes trace-cmd listen to go into a daemon mode and run in the background.</dl>
<p> <code>-d</code> <i>dir</i></p>
<dl>
<dt>
<dd> This option specifies a directory to write the data files into.</dl>
<p> <code>-o</code> <i>filename</i></p>
<dl>
<dt>
<dd> This option overrides the default <i>trace</i> in the <i>trace.HOST:PORT.dat</i> that is created when a remote host connects.</dl>
<p> <code>-l</code> <i>filename</i></p>
<dl>
<dt>
<dd> This option writes the output messages to a log file instead of standard output.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-trace-cmd/">trace-cmd</a>(1), <a href="/docs/linux/man/1-trace-cmd-record/">trace-cmd-record</a>(1), <a href="/docs/linux/man/1-trace-cmd-report/">trace-cmd-report</a>(1), <a href="/docs/linux/man/1-trace-cmd-start/">trace-cmd-start</a>(1), <a href="/docs/linux/man/1-trace-cmd-stop/">trace-cmd-stop</a>(1), <a href="/docs/linux/man/1-trace-cmd-extract/">trace-cmd-extract</a>(1), <a href="/docs/linux/man/1-trace-cmd-reset/">trace-cmd-reset</a>(1), <a href="/docs/linux/man/1-trace-cmd-split/">trace-cmd-split</a>(1), <a href="/docs/linux/man/1-trace-cmd-list/">trace-cmd-list</a>(1)</p>
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
