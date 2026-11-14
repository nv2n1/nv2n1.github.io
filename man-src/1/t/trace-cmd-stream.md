---
title: "trace-cmd-stream(1)"
name: "trace-cmd-stream"
section: "1"
letter: "t"
url: "/docs/linux/man/1-trace-cmd-stream/"
description: "trace-cmd-stream – stream a trace to stdout as it is happening"
---

<h2 class="name">NAME</h2>
<p> trace-cmd-stream &#8211; stream a trace to stdout as it is happening </p>
<h2>SYNOPSIS</h2>
<p> <code>trace-cmd stream [</code><i>OPTIONS</i><code>]</code> [<i>command</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <a href="/docs/linux/man/1-trace-cmd/">trace-cmd</a>(1) stream will start tracing just like <a href="/docs/linux/man/1-trace-cmd-record/">trace-cmd-record</a>(1), except it will not record to a file and instead it will read the binary buffer as it is happening, convert it to a human readable format and write it to stdout. </p>
<p> This is basically the same as <a href="/docs/linux/man/1-trace-cmd-start/">trace-cmd-start</a>(1) and then doing a <a href="/docs/linux/man/1-trace-cmd-show/">trace-cmd-show</a>(1) with the <code>-p</code> option. trace-cmd-stream is not as efficient as reading from the pipe file as most of the stream work is done in userspace. This is useful if it is needed to do the work mostly in userspace instead of the kernel, and stream also helps to debug <a href="/docs/linux/man/1-trace-cmd-profile/">trace-cmd-profile</a>(1) which uses the stream code to perform the live data analysis for the profile.</p>
<h2>OPTIONS</h2>
<dl>
<dt>
<dd>
<pre>
These are the same as <a href="//www.systutorials.com/docs/linux/man/1-trace-cmd-record/">trace-cmd-record</a>(1), except that it does not take
the *-o* option.
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-trace-cmd/">trace-cmd</a>(1), <a href="/docs/linux/man/1-trace-cmd-record/">trace-cmd-record</a>(1), <a href="/docs/linux/man/1-trace-cmd-report/">trace-cmd-report</a>(1), <a href="/docs/linux/man/1-trace-cmd-start/">trace-cmd-start</a>(1), <a href="/docs/linux/man/1-trace-cmd-stop/">trace-cmd-stop</a>(1), <a href="/docs/linux/man/1-trace-cmd-reset/">trace-cmd-reset</a>(1), <a href="/docs/linux/man/1-trace-cmd-split/">trace-cmd-split</a>(1), <a href="/docs/linux/man/1-trace-cmd-list/">trace-cmd-list</a>(1), <a href="/docs/linux/man/1-trace-cmd-listen/">trace-cmd-listen</a>(1)</p>
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
