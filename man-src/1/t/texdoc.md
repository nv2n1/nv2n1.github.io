---

title: "texdoc(1)"
name: "texdoc"
section: "1"
letter: "t"
url: "/docs/linux/man/1-texdoc/"
description: "texdoc – find & view documentation in TeX Live"
---

<p> <code>texdoc</code> &#8211; find &amp; view documentation in TeX Live </p>
<h2>SYNOPSIS</h2>
<p> <code>texdoc</code> [OPTION]&#8230; NAME&#8230;<br />
 <code>texdoc</code> [OPTION]&#8230; ACTION</p>
<h2>DESCRIPTION</h2>
<p> Try to find appropriate TeX documentation for the specified NAME(s). Alternatively, perform the given ACTION and exit.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-w</code>, <code>&#8211;view</code></dt>
<dd> Use view mode: start a viewer. <code>(default)</code></dd>
<dt><code>-m</code>, <code>&#8211;mixed</code></dt>
<dd> Use mixed mode (view or list).</dd>
<dt><code>-l</code>, <code>&#8211;list</code></dt>
<dd> Use list mode: show a list of results.</dd>
<dt><code>-s</code>, <code>&#8211;showall</code></dt>
<dd> Use showall mode: show also &quot;bad&quot; results.</dd>
<dt><code>-i</code>, <code>&#8211;interact</code></dt>
<dd> Use interactive menus. <code>(default)</code></dd>
<dt><code>-I</code>, <code>&#8211;nointeract</code></dt>
<dd> Use plain lists, no interaction required.</dd>
<dt><code>-M</code>, <code>&#8211;machine</code></dt>
<dd> Machine-readable output for lists (implies -I).</dd>
<dt><code>-q</code>, <code>&#8211;quiet</code></dt>
<dd> Suppress warnings and most error messages.</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> Print additional information (e.g., viewer command).</dd>
<dt><code>-D</code>, <code>&#8211;debug</code></dt>
<dd> Activate all debug output (equal to &quot;&#8211;debug=all&quot;).</dd>
<dt><code>-d</code> LIST, <code>&#8211;debug</code>=LIST</dt>
<dd> Activate debug output restricted to the categories specified in LIST.<br />
 Available categories: <code>config</code>, <code>files</code>, <code>search</code>, <code>score</code>, <code>texdocs</code>, <code>tlpdb</code>, <code>version</code>, <code>view</code>, and <code>all</code> to activate all of these.</dd>
<dt><code>-c</code> NAME=VALUE</dt>
<dd> Set configuration item NAME to VALUE.</dd></dl>
<h2>ACTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Print this help message.</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> Print the version number.</dd>
<dt><code>-f</code>, <code>&#8211;files</code></dt>
<dd> Print the list of configuration files used.</dd>
<dt><code>&#8211;just-view</code> FILE</dt>
<dd> Display FILE, given with full path (no searching).</dd></dl>
<h2>ENVIRONMENT</h2>
<p> The following environment variables can be split by colon and used to set viewers:</p>
<dl>
<dt><code>BROWSER</code>, <code>BROWSER_texdoc</code></dt>
<dd> Set the command to be used for HTML documents.</dd>
<dt><code>DVIVIEWER</code>, <code>DVIVIEWER_texdoc</code></dt>
<dd> Set the command to be used for DVI documents.</dd>
<dt><code>MDVIEWER</code>, <code>MDVIEWER_texdoc</code></dt>
<dd> Set the command to be used for Markdown documents.</dd>
<dt><code>PAGER</code>, <code>PAGER_texdoc</code></dt>
<dd> Set the command to be used for text documents.</dd>
<dt><code>PDFVIEWER</code>, <code>PDFVIEWER_texdoc</code></dt>
<dd> Set the command to be used for PDF documents.</dd>
<dt><code>PSVIEWER</code>, <code>PSVIEWER_texdoc</code></dt>
<dd> Set the command to be used for PS documents.</dd></dl>
<p> The following environment variables are also used:</p>
<dl>
<dt><code>LANG</code>, <code>LC_ALL</code> and so on</dt>
<dd> Set the locale (which will influence on the search results).</dd>
<dt><code>TEXDOCS</code></dt>
<dd> In addition to the documents included in the TeX Live database, Texdoc also searches documentation under TEXMF trees specified by the kpathsea variable <code>TEXDOCS</code>.</dd></dl>
<h2>FILES</h2>
<p> <code>&lt;texmf&gt;/texdoc/texdoc.cnf</code>, see output of the <code>&#8211;files</code> option.</p>
<h2>EXIT STATUS</h2>
<p> The <code>texdoc</code> command exists with one of the following values:</p>
<dl>
<dt>0</dt>
<dd> Success.</dd>
<dt>1</dt>
<dd> Internal error.</dd>
<dt>2</dt>
<dd> Usage error.</dd>
<dt>3</dt>
<dd> No documentation found.</dd></dl>
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
</dt><dd>
<pre>
texdoc texdoc
</pre>
</dd></dl>
<p> should give you access to the complete manual. </p>
