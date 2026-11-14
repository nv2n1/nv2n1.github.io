---
title: "ttx2xgf(1)"
name: "ttx2xgf"
section: "1"
letter: "t"
url: "/docs/linux/man/1-ttx2xgf/"
description: "ttx2xgf – extracts instructions from a TTX file and creates an Xgridfit program."
---

<h2>NAME</h2>
<p> <code>ttx2xgf</code> &#8211; extracts instructions from a TTX file and creates an Xgridfit program.</p>
<h2>SYNOPSIS</h2>
<p> <code>ttx2xgf</code> <i>infile[.ttx]</i> <i>[outfile]</i></p>
<h2>DESCRIPTION</h2>
<p> <code>ttx2xgf</code> is a utility that extracts instructions (hints) and other information relating to instructions from a TTX file (an XML representation of a TrueType font) and creates a new Xgridfit program. </p>
<p> If <i>infile</i> lacks the <i>.ttx</i> extension, it is assumed. If <i>outfile</i> is not given, output is written to <i>infile.xgf.</i></p>
<h2>FILES</h2>
<dl>
<dt><i>/usr/share/xgridfit/util/convert-ttx.xsl</i></p>
<dd> An XSLT script that performs the initial conversion.</p>
<dt><i>/usr/share/xgridfit/util/convert-asm.sed</i></p>
<dd> A Sed script that completes the conversion.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-xgridfit/">xgridfit</a></code>(1), <code><a href="/docs/linux/man/1-ttx/">ttx</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> <code>ttx2xgf</code> was written by Peter Baker &lt;psb6m [at] virginia.edu&gt;. </p>
<p> This manual page was written by Peter Baker </p>
<h2>Index</h2>
