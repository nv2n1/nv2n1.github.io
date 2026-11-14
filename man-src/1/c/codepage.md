---
title: "codepage(1)"
name: "codepage"
section: "1"
letter: "c"
url: "/docs/linux/man/1-codepage/"
description: "codepage – extract a codepage from an MSDOS codepage file"
---

<h2 class="name">NAME</h2>
<p> codepage &#8211; extract a codepage from an MSDOS codepage file</p>
<h2>SYNOPSIS</h2>
<p> <code>codepage </code> [ <i>-c </i> | <i>-l</i> | <i>-L </i> | <i>-a </i> | <i>nnn</i> ] <i>file.cpi</i> </p>
<h2>DESCRIPTION</h2>
<p> The <code>codepage</code> command extracts codepages from an MSDOS codepage file. </p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-c </i></p>
<dd> Input file is a single codepage </p>
<dt><i>-L </i></p>
<dd> Print header info (you don&#8217;t want to see this). </p>
<dt><i>-l </i></p>
<dd> List all codepages contained in the file. </p>
<dt><i>-a</i></p>
<dd> Extract all codepages from the file </p>
<dt><i>nnn</i></p>
<dd> (3 digits): extract codepage <i>nnn</i> from the file. </p>
</dl>
<h2>EXAMPLE</h2>
<p> To create a file 850.cp, with codepage 850 from a file ega.cpi, execute: </p>
<dl>
<dt>
<dd> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>codepage ega.cpi 850
</dl>
<h2>Index</h2>
