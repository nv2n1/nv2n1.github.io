---
title: "valgrind-listener(1)"
name: "valgrind-listener"
section: "1"
letter: "v"
url: "/docs/linux/man/1-valgrind-listener/"
description: "valgrind-listener – listens on a socket for Valgrind commentary"
---

<h2 class="name">NAME</h2>
<p> valgrind-listener &#8211; listens on a socket for Valgrind commentary </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>valgrind-listener</code> [<i>options</i>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>valgrind-listener</code></p>
<dd>accepts (multiple) connections from <code>valgrind</code> processes that use the <code>&#8211;log-socket</code> option on the specified port and copies the commentary it is sent to stdout.</p>
<h2>OPTIONS</h2>
<p> <code>-e &#8211;exit-at-zero</code></p>
<dl>
<dt>
<dd> When the number of connected processes falls back to zero, exit. Without this, it will run forever, that is, until you send it Control-C.</dl>
<p> <code>&#8211;max-connect=INTEGER</code></p>
<dl>
<dt>
<dd> By default, the listener can connect to up to 50 processes. Occasionally, that number is too small. Use this option to provide a different limit. E.g. &#8211;max-connect=100.</dl>
<p> <code>portnumber</code></p>
<dl>
<dt>
<dd> Changes the port it listens on from the default (1500). The specified port must be in the range 1024 to 65535. The same restriction applies to port numbers specified by a <code>&#8211;log-socket</code> to Valgrind itself.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-valgrind/">valgrind</a>(1), $INSTALL/share/doc/valgrind/html/index.html or <a rel="nofollow" href="http://www.valgrind.org/docs/manual/index.html.">http://www.valgrind.org/docs/manual/index.html.</a></p>
<h2>AUTHOR</h2>
<p> Julian Seward. </p>
<h2>Index</h2>
