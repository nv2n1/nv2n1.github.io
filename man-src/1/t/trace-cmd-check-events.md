---
title: "trace-cmd-check-events(1)"
name: "trace-cmd-check-events"
section: "1"
letter: "t"
url: "/docs/linux/man/1-trace-cmd-check-events/"
description: "trace-cmd-check-events – parse the event formats on local system"
---

<h2 class="name">NAME</h2>
<p> trace-cmd-check-events &#8211; parse the event formats on local system </p>
<h2>SYNOPSIS</h2>
<p> <code>trace-cmd check-events</code> [<i>OPTIONS</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <a href="/docs/linux/man/1-trace-cmd/">trace-cmd</a>(1) check-events parses format strings for all the events on the local system. It returns whether all the format strings can be parsed correctly. It will load plugins unless specified otherwise. </p>
<p> This is useful to check for any trace event format strings which may contain some internal kernel function references which cannot be decoded outside of the kernel. This may mean that either the unparsed format strings of the trace events need to be changed or that a plugin needs to be created to parse them.</p>
<h2>OPTIONS</h2>
<p> <code>-N</code> &#8211; Don&#8217;t load plugins</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-trace-cmd/">trace-cmd</a>(1), <a href="/docs/linux/man/1-trace-cmd-record/">trace-cmd-record</a>(1), <a href="/docs/linux/man/1-trace-cmd-report/">trace-cmd-report</a>(1), <a href="/docs/linux/man/1-trace-cmd-stop/">trace-cmd-stop</a>(1), <a href="/docs/linux/man/1-trace-cmd-extract/">trace-cmd-extract</a>(1), <a href="/docs/linux/man/1-trace-cmd-reset/">trace-cmd-reset</a>(1), <a href="/docs/linux/man/1-trace-cmd-split/">trace-cmd-split</a>(1), <a href="/docs/linux/man/1-trace-cmd-list/">trace-cmd-list</a>(1), <a href="/docs/linux/man/1-trace-cmd-listen/">trace-cmd-listen</a>(1), <a href="/docs/linux/man/1-trace-cmd-start/">trace-cmd-start</a>(1)</p>
<h2>AUTHOR</h2>
<p> Written by Vaibhav Nagarnaik, &lt;m[blue]<code>vnagarnaik [at] google.com</code>m[]<font SIZE="-2">[1]</font>&gt;</p>
<h2>RESOURCES</h2>
<p> <a href="git://git.kernel.org/pub/scm/linux/kernel/git/rostedt/trace-cmd.git">git://git.kernel.org/pub/scm/linux/kernel/git/rostedt/trace-cmd.git</a></p>
<h2>COPYING</h2>
<p> Copyright (C) 2011 Google, Inc. Free use of this software is granted under the terms of the GNU Public License (GPL).</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> vnagarnaik [at] google.com</p>
<dl>
<dt>
<dd> mailto:vnagarnaik [at] google.com</dl>
</dl>
<h2>Index</h2>
