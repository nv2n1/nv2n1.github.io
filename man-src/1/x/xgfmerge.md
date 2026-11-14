---
title: "xgfmerge(1)"
name: "xgfmerge"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xgfmerge/"
description: "xgfmerge – merges two Xgridfit program files"
---

<h2>NAME</h2>
<p> <code>xgfmerge</code> &#8211; merges two Xgridfit program files</p>
<h2>SYNOPSIS</h2>
<p> <code>xgfmerge</code> [options] <i>file-a</i> <i>file-b</i> <i>[&#8230;]</i></p>
<h2>DESCRIPTION</h2>
<p> <code>Xgfmerge</code> merges two or more Xgridfit program files, where file-a is a program generated automatically from an existing font using TTX and ttx2xgf, and file-b and any other files in the list contain other programming for the font. <code>Xgfmerge</code> outputs the merged programming to stdout. To capture the output in a file, use this syntax: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>$xgfmerge -o merged-file.xgf file-a.xgf file-b.xgf </p>
<p> If xmlstarlet is found in the system, xgfmerge uses it to format the output. Otherwise, the output file will be messy but valid.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-c</p>
<dd> Look for a &lt;default type=&quot;compile-globals&quot;/&gt; element in each file after the first in the list. If value=&quot;no&quot; then ignore all &lt;default&gt;, &lt;control-value&gt;, &lt;function&gt;, &lt;macro&gt; and &lt;pre-program&gt; elements in the file.</p>
<dt>-h</p>
<dd> Display a help message.</p>
<dt>-n</p>
<dd> Merge &lt;no-compile&gt; elements from all files. &lt;glyph&gt; elements with duplicate &quot;ps-name&quot; attributes are ignored.</p>
<dt>-o file</p>
<dd> The file to write the output to. If this option is not used, output is written to stdout.</p>
<dt>-p</p>
<dd> When a &lt;pre-program&gt; element in a file other than file-a is available, use it instead of the one from file-a. If this option is not present, xgfmerge merges the programming in the &lt;pre-program&gt; of file-a with that in the &lt;pre-program&gt; of whichever file is being merged at the moment. The result is unlikely to be good if a single run of xgfmerge merges the contents of more than two &lt;pre-program&gt; elements.</p>
<dt>-s</p>
<dd> Sort &lt;glyph&gt; elements in the output file into alphabetical order.</p>
<dt>-v</p>
<dd> Verbose output: xgfmerge tells you what it is doing at each step.</p>
<dt>-x</p>
<dd> Resolve XIncludes before merging all files in the list except for file-a. Any XIncludes from file-a.xgf are stripped out of the files before this operation is performed. If XInclude is used to bring global elements (&lt;control-value&gt;, &lt;function&gt;, etc.) into these files, it is probably a good idea to use the -c option as well.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/usr/local/share/xgridfit/util/merge.xsl</i></p>
<dd> An XSLT script that performs the merge.</p>
<dt><i>/usr/local/share/xgridfit/util/xinclude.xsl</i></p>
<dd> An XSLT script that strips out unwanted XIncludes.</p>
<dt><i>/usr/local/share/xgridfit/util/sort-glyphs.xsl</i></p>
<dd> An XSLT script that sorts glyph elements in a file.</p>
<dt><i>/usr/local/share/xgridfit/utils/add-blanks.sed</i></p>
<dd> Does some formatting of the output.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-xgridfit/">xgridfit</a></code>(1), <code><a href="/docs/linux/man/1-ttx/">ttx</a></code>(1), <code><a href="/docs/linux/man/1-ttx2xgf/">ttx2xgf</a></code>(1), <code><a href="/docs/linux/man/1-xmlstarlet/">xmlstarlet</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> <code>Xgfmerge</code> was written by Peter Baker &lt;psb6m [at] virginia.edu&gt;. </p>
<p> This manual page was written by Peter Baker </p>
<h2>Index</h2>
