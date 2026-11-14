---
title: "tab2space(1)"
name: "tab2space"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tab2space/"
description: "tab2space [options] [infile [outfile]] …"
---

<h2 class="name">NAME</h2>
<p> <code>tab2space</code> [<i>options</i>] [<i>infile</i> [<i>outfile</i>]] &#8230; </p>
<h2>DESCRIPTION</h2>
<p> Utility to expand tabs and ensure consistent line endings options. </p>
<p> When the <i>infile</i> is not specified or is set to <i>&#8211;</i> (dash) the input file is read from standard input. </p>
<p> This man page is rewritten from <i>-help</i> output. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>-help</code></p>
<dd> display the help message</p>
<dt><code>-dos</code>, <code>-crlf</code></p>
<dd> set line ends to CRLF (PC-DOS/Windows &#8211; default)</p>
<dt><code>-mac</code>, <code>-cr</code></p>
<dd> set line ends to CR (classic Mac OS)</p>
<dt><code>-unix</code>, <code>-lf</code></p>
<dd> set line ends to LF (Unix)</p>
<dt><code>-tabs</code></p>
<dd> preserve tabs, e.g. for Makefile</p>
<dt><code>-t</code><i>&lt;n&gt;</i></p>
<dd> set tabs to <i>&lt;n&gt;</i> (default is 4) spaces</p>
<dt>Note this utility doesn&#8217;t map spaces to tabs!</p>
<dd>
</dl>
<h2>VERSION</h2>
<p> <code>tab2space</code> for 6th February 2003 </p>
<h2>Index</h2>
