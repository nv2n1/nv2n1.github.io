---
title: "rcvpack(1)"
name: "rcvpack"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rcvpack/"
description: "rcvpack – append message to file"
---

<h2 class="name">NAME</h2>
<p> rcvpack &#8211; append message to file </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>/usr/libexec/nmh/rcvpack</code> <i>file</i> [<code>-mbox</code>] [<code>-mmdf</code>] [<code>-version</code>] [<code>-help</code>]</dl>
<h2>DESCRIPTION</h2>
<dd>The <code>rcvpack</code> program will append a copy of the message to the file listed on its command line. </p>
<p> If the <code>-mbox</code> switch is given (the default), then the messages are separated using mbox (uucp) style delimiters. This is the format used by most mail clients (elm, mailx, etc.). </p>
<p> If the <code>-mmdf</code> switch is given, then the messages are separated by mmdf style delimiters. Each message in the file is separated by four CTRL-A&#8217;s and a newline. </p>
<p> <code>rcvpack</code> will correctly lock and unlock the file to serialize access to the file, when running multiple copies of <code>rcvpack</code>. </p>
<p> In general, its use is obsoleted by the <code>file</code> action of <code>slocal</code>, although it might still have occasional uses in various shell scripts.</p>
<h2>FILES</h2>
<pre>
^/etc/nmh/mts.conf~^nmh mts configuration file
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-rcvdist/">rcvdist</a></i>(1), <i><a href="/docs/linux/man/1-rcvstore/">rcvstore</a></i>(1), <i><a href="/docs/linux/man/1-rcvtty/">rcvtty</a></i>(1), <i><a href="/docs/linux/man/1-slocal/">slocal</a></i>(1)</p>
<h2>BUGS</h2>
<p> Only two return codes are meaningful, others should be. </p>
<h2>Index</h2>
