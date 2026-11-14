---
title: "sotruss(1)"
name: "sotruss"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sotruss/"
description: "sotruss – trace shared library calls through PLT"
---

<h2 class="name">NAME</h2>
<p> sotruss &#8211; trace shared library calls through PLT </p>
<h2>SYNOPSIS</h2>
<p> <code>sotruss</code> [<i>,OPTION/</i>&#8230;] [<i>,&#8211;/</i>] <i>,EXECUTABLE /</i>[<i>,EXECUTABLE-OPTION/</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>sotruss </code> is a small wrapper around <code>ld.so</code> that runs the specified <i>executable</i> until it exits. It intercepts and produce a trace of the dynamic library calls which are called by the executed process via the Procedure Linkage Table (PLT). It outputs the caller, the calle and the parameters as each call is executed.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-F</code>, <code>&#8211;from</code> FROMLIST</p>
<dd> Trace calls from objects on FROMLIST.</p>
<dt><code>-T</code>, <code>&#8211;to</code> TOLIST</p>
<dd> Trace calls to objects on TOLIST.</p>
<dt><code>-e</code>, <code>&#8211;exit</code></p>
<dd> Also show exits from the function calls.</p>
<dt><code>-f</code>, <code>&#8211;follow</code></p>
<dd> Trace child processes as they are created by currently traced processes as a result of the <code><a href="/docs/linux/man/2-fork/">fork</a>(2)</code> system call.</p>
<dt><code>-o</code>, <code>&#8211;output</code> FILENAME</p>
<dd> Write output to FILENAME (or FILENAME. in case <code>-f</code> is also used) instead of standard error.</p>
<dt>-?, <code>&#8211;help</code></p>
<dd> Give this help list</p>
<dt><code>&#8211;usage</code></p>
<dd> Give a short usage message</p>
<dt><code>&#8211;version</code></p>
<dd> Print program version</dl>
<h2>AUTHOR</h2>
<p> Written by Ulrich Drepper.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2013 Free Software Foundation, Inc.<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-ld-so/">ld.so</a>(8).</code> </p>
<h2>Index</h2>
