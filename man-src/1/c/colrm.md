---
title: "colrm(1)"
name: "colrm"
section: "1"
letter: "c"
url: "/docs/linux/man/1-colrm/"
description: "colrm – remove columns from a file"
---

<h2 class="name">NAME</h2>
<p> colrm &#8211; remove columns from a file </p>
<h2>SYNOPSIS</h2>
<p> <code>colrm</code> <i>[first [last]]</i></p>
<h2>DESCRIPTION</h2>
<p> <code>colrm</code> removes selected columns from a file. Input is taken from standard input. Output is sent to standard output. </p>
<p> If called with one parameter the columns of each line will be removed starting with the specified <i>first</i> column. If called with two parameters the columns from the <i>first</i> column to the <i>last</i> column will be removed. </p>
<p> Column numbering starts with column 1.</p>
<h2>OPTIONS</h2>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help text and exit.</dl>
<h2>HISTORY</h2>
<p> The <code>colrm</code> command appeared in 3.0BSD.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="//www.systutorials.com/docs/linux/man/1p-awk/">awk</a></code>(1p), <code><a href="/docs/linux/man/1-column/">column</a></code>(1), <code><a href="/docs/linux/man/1-expand/">expand</a></code>(1), <code><a href="/docs/linux/man/1-paste/">paste</a></code>(1)</p>
<h2>REPORTING BUGS</h2>
<p> For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>AVAILABILITY</h2>
<p> The <code>colrm</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
<h2>Index</h2>
