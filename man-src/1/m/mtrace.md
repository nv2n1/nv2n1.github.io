---
title: "mtrace(1)"
name: "mtrace"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mtrace/"
description: "mtrace – interpret the malloc trace log"
---

<h2 class="name">NAME</h2>
<p> mtrace &#8211; interpret the malloc trace log </p>
<h2>SYNOPSIS</h2>
<p> <code>mtrace</code> [<i>option</i>]&#8230; [<i>binary</i>] <i>mtracedata</i></p>
<h2>DESCRIPTION</h2>
<p> <code>mtrace</code> is a Perl script used to interpret and provide human readable output of the trace log contained in the file <i>mtracedata</i>, whose contents were produced by <code><a href="/docs/linux/man/3-mtrace/">mtrace</a></code>(3). If <i>binary</i> is provided, the output of <code>mtrace</code> also contains the source file name with line number information for problem locations (assuming that <i>binary</i> was compiled with debugging information). </p>
<p> For more information about the <code><a href="/docs/linux/man/3-mtrace/">mtrace</a></code>(3) function and <code>mtrace</code> script usage, see <code><a href="/docs/linux/man/3-mtrace/">mtrace</a></code>(3).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Print help and exit.</p>
<dt><code>&#8211;version</code></p>
<dd> Print version information and exit.</dl>
<h2>BUGS</h2>
<p> For bug reporting instructions, please see:</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-memusage/">memusage</a></code>(1), <code><a href="/docs/linux/man/3-mtrace/">mtrace</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
