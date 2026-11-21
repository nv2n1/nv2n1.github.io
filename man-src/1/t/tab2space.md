---

title: "tab2space(1)"
name: "tab2space"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tab2space/"
description: "tab2space [options] [infile [outfile]] …"
---

<p> <code>tab2space</code> [<i>options</i>] [<i>infile</i> [<i>outfile</i>]] &#8230; </p>
<h2>DESCRIPTION</h2>
<p> Utility to expand tabs and ensure consistent line endings options. </p>
<p> When the <i>infile</i> is not specified or is set to <i>&#8211;</i> (dash) the input file is read from standard input. </p>
<p> This man page is rewritten from <i>-help</i> output. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>-help</code></dt>
<dd> display the help message</dd>
<dt><code>-dos</code>, <code>-crlf</code></dt>
<dd> set line ends to CRLF (PC-DOS/Windows &#8211; default)</dd>
<dt><code>-mac</code>, <code>-cr</code></dt>
<dd> set line ends to CR (classic Mac OS)</dd>
<dt><code>-unix</code>, <code>-lf</code></dt>
<dd> set line ends to LF (Unix)</dd>
<dt><code>-tabs</code></dt>
<dd> preserve tabs, e.g. for Makefile</dd>
<dt><code>-t</code><i>&lt;n&gt;</i></dt>
<dd> set tabs to <i>&lt;n&gt;</i> (default is 4) spaces</dd>
<dt>Note this utility doesn&#8217;t map spaces to tabs!</dt>
<dd>
</dd></dl>
<h2>VERSION</h2>
<p> <code>tab2space</code> for 6th February 2003 </p>
