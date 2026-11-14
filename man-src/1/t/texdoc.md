---
title: "texdoc(1)"
name: "texdoc"
section: "1"
letter: "t"
url: "/docs/linux/man/1-texdoc/"
description: "texdoc – find & view documentation in TeX Live"
---

<h2 class="name">NAME</h2>
<p> <code>texdoc</code> &#8211; find &amp; view documentation in TeX Live </p>
<h2>SYNOPSIS</h2>
<p> <code>texdoc</code> [OPTION]&#8230; NAME&#8230;<br />
 <code>texdoc</code> [OPTION]&#8230; ACTION</p>
<h2>DESCRIPTION</h2>
<p> Try to find appropriate TeX documentation for the specified NAME(s). Alternatively, perform the given ACTION and exit.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-w</code>, <code>&#8211;view</code></p>
<dd> Use view mode: start a viewer. <code>(default)</code></p>
<dt><code>-m</code>, <code>&#8211;mixed</code></p>
<dd> Use mixed mode (view or list).</p>
<dt><code>-l</code>, <code>&#8211;list</code></p>
<dd> Use list mode: show a list of results.</p>
<dt><code>-s</code>, <code>&#8211;showall</code></p>
<dd> Use showall mode: show also &quot;bad&quot; results.</p>
<dt><code>-i</code>, <code>&#8211;interact</code></p>
<dd> Use interactive menus. <code>(default)</code></p>
<dt><code>-I</code>, <code>&#8211;nointeract</code></p>
<dd> Use plain lists, no interaction required.</p>
<dt><code>-M</code>, <code>&#8211;machine</code></p>
<dd> Machine-readable output for lists (implies -I).</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> Suppress warnings and most error messages.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Print additional information (e.g., viewer command).</p>
<dt><code>-D</code>, <code>&#8211;debug</code></p>
<dd> Activate all debug output (equal to &quot;&#8211;debug=all&quot;).</p>
<dt><code>-d</code> LIST, <code>&#8211;debug</code>=LIST</p>
<dd> Activate debug output restricted to the categories specified in LIST.<br />
 Available categories: <code>config</code>, <code>files</code>, <code>search</code>, <code>score</code>, <code>texdocs</code>, <code>tlpdb</code>, <code>version</code>, <code>view</code>, and <code>all</code> to activate all of these.</p>
<dt><code>-c</code> NAME=VALUE</p>
<dd> Set configuration item NAME to VALUE.</dl>
<h2>ACTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print this help message.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print the version number.</p>
<dt><code>-f</code>, <code>&#8211;files</code></p>
<dd> Print the list of configuration files used.</p>
<dt><code>&#8211;just-view</code> FILE</p>
<dd> Display FILE, given with full path (no searching).</dl>
<h2>ENVIRONMENT</h2>
<p> The following environment variables can be split by colon and used to set viewers:</p>
<dl>
<dt><code>BROWSER</code>, <code>BROWSER_texdoc</code></p>
<dd> Set the command to be used for HTML documents.</p>
<dt><code>DVIVIEWER</code>, <code>DVIVIEWER_texdoc</code></p>
<dd> Set the command to be used for DVI documents.</p>
<dt><code>MDVIEWER</code>, <code>MDVIEWER_texdoc</code></p>
<dd> Set the command to be used for Markdown documents.</p>
<dt><code>PAGER</code>, <code>PAGER_texdoc</code></p>
<dd> Set the command to be used for text documents.</p>
<dt><code>PDFVIEWER</code>, <code>PDFVIEWER_texdoc</code></p>
<dd> Set the command to be used for PDF documents.</p>
<dt><code>PSVIEWER</code>, <code>PSVIEWER_texdoc</code></p>
<dd> Set the command to be used for PS documents.</dl>
<p> The following environment variables are also used:</p>
<dl>
<dt><code>LANG</code>, <code>LC_ALL</code> and so on</p>
<dd> Set the locale (which will influence on the search results).</p>
<dt><code>TEXDOCS</code></p>
<dd> In addition to the documents included in the TeX Live database, Texdoc also searches documentation under TEXMF trees specified by the kpathsea variable <code>TEXDOCS</code>.</dl>
<h2>FILES</h2>
<p> <code>&lt;texmf&gt;/texdoc/texdoc.cnf</code>, see output of the <code>&#8211;files</code> option.</p>
<h2>EXIT STATUS</h2>
<p> The <code>texdoc</code> command exists with one of the following values:</p>
<dl>
<dt>0</p>
<dd> Success.</p>
<dt>1</p>
<dd> Internal error.</p>
<dt>2</p>
<dd> Usage error.</p>
<dt>3</p>
<dd> No documentation found.</dl>
<h2>REPORTING BUGS</h2>
<p> Report bugs to <i>texdoc [at] tug.org</i>.<br />
 Texdoc home page: <i><a rel="nofollow" href="http://tug.org/texdoc/">http://tug.org/texdoc/</a></i><br />
 Source: <i><a rel="nofollow" href="https://github.com/TeX-Live/texdoc">https://github.com/TeX-Live/texdoc</a></i></p>
<h2>COPYRIGHT</h2>
<p> Copyright 2008-2021 Manuel Pe&#8217;gourie&#8217;-Gonnard, Takuto Asakura, the TeX Live Team.<br />
 License: GNU GPL version 3 or later <i><a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a></i>.<br />
 This is free software: you are free to change and redistribute it.</p>
<h2>SEE ALSO</h2>
<p> The full documentation is maintained as a PDF manual. The command</p>
<dl>
<dt>
<dd>
<pre>
texdoc texdoc
</pre>
<dt>
<dd></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
