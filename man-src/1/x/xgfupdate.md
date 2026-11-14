---
title: "xgfupdate(1)"
name: "xgfupdate"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xgfupdate/"
description: "xgfupdate – updates an Xgridfit program file to the latest version."
---

<h2>NAME</h2>
<p> <code>xgfupdate </code> &#8211; updates an Xgridfit program file to the latest version.</p>
<h2>SYNOPSIS</h2>
<p> <code>xgfupdate</code> <i>file</i></p>
<h2>DESCRIPTION</h2>
<p> <code>Xgfupdate</code> is a utility that updates an Xgridfit program file so that it validates against the current xgridfit-strict.rnc schema. If XMLStarlet is found in the system, it is used to prettify the output. <code>Xgfupdate</code> outputs the updated file to stdout. To capture the output in a file, use this syntax: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>$xgfupdate infile&nbsp;<wbr>&gt;&nbsp;<wbr>outfile</p>
<h2>FILES</h2>
<dl>
<dt><i>/usr/share/xgridfit/util/xgf-update.xsl</i></p>
<dd> An XSLT script that does the updating.</p>
<dt><i>/usr/share/xgridfit/util/add-blanks.sed</i></p>
<dd> A Sed script that does some formatting of the output.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-xgridfit/">xgridfit</a></code>(1), <code><a href="/docs/linux/man/1-xmlstarlet/">xmlstarlet</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> <code>Xgfupdate</code> was written by Peter Baker &lt;psb6m [at] virginia.edu&gt;. </p>
<p> This manual page was written by Peter Baker </p>
<h2>Index</h2>
