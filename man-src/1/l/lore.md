---

title: "lore(1)"
name: "lore"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lore/"
description: "lore – convert documentations formats"
---

<p> lore &#8211; convert documentations formats</p>
<h2>SYNOPSIS</h2>
<p> <code>lore [-l </code><i>linkrel</i>] [-d <i>docsdir</i>] [-i <i>input</i>] [-o <i>output</i>] [&#8211;config attribute[=value] [&#8230;]] [-p] [file [&#8230;]] </p>
<p> <code>lore &#8211;help</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>&#8211;help</code> prints out a usage message to standard output.</p>
<dl>
<dt><code>-p</code>, <code>&#8211;plain</code></dt>
<dd> Use non-flashy progress bar &#8211; one file per line.</dd>
<dt><code>-n</code>, <code>&#8211;null</code></dt>
<dd> Do not report progress at all.</dd>
<dt><code>-N</code>, <code>&#8211;number</code></dt>
<dd> Add chapter/section numbers to section headings.</dd>
<dt><i>-l</i>, <i>&#8211;linkrel</i></dt>
<dd> Where non-document links should be relative to.</dd>
<dt><i>-d</i>, <i>&#8211;docsdir</i></dt>
<dd> Where to look for <code>.html</code> files if no files are given.</dd>
<dt><i>-e</i>, <i>&#8211;inputext</i> &lt;extension&gt;</dt>
<dd> The extension that your Lore input files have (default: .xhtml)</dd>
<dt><i>-i</i>, <i>&#8211;input</i></dt>
<dd> Input format. New input formats can be dynamically registered. Lore itself comes with &quot;lore&quot; (the standard format), &quot;mlore&quot; (allows LaTeX equations) and &quot;man&quot; (man page format). If the input format is not registered as a plugin, a module of the named input will be searched. For example, <code>&#8211;i twisted.lore.default</code> is equivalent to using the default Lore input.</dd>
<dt><i>-o</i>, <i>&#8211;output</i></dt>
<dd> Output format. Available output formats depend on the input. For the core formats, lore and mlore support html, latex and lint, while man allows lore.</dd>
<dt><i>-x</i>, <i>&#8211;index</i> &lt;filename&gt;</dt>
<dd> The base filename you want to give your index file.</dd>
<dt><i>-b</i>, <i>&#8211;book</i> &lt;filename&gt;</dt>
<dd> The book file to generate a book from.</dd>
<dt><i>&#8211;prefixurl</i> &lt;prefix&gt;</dt>
<dd> The prefix to stick on to relative links; only useful when processing directories.</dd>
<dt><i>&#8211;version</i></dt>
<dd> Display version information and exit.</dd>
<dt><i>&#8211;config</i></dt>
<dd> Add input/output-specific information. HTML output allows for &#8216;ext=&lt;extension&gt;&#8217;, output allows for &#8216;section&#8217; or &#8216;chapter&#8217; in Lore, and nothing in Math-Lore. Lore output allows for &#8216;ext=&lt;extension&gt;&#8217;. Lint output allows nothing. Note that disallowed <i>&#8211;config</i> options are merely ignored, and do not cause errors.</dd></dl>
<h2>DESCRIPTION</h2>
<p> If no files are given, all *.html documents in docsdir are processed.</p>
<h2>AUTHOR</h2>
<p> Written by Moshe Zadka</p>
<h2>REPORTING BUGS</h2>
<p> To report a bug, visit <i><a rel="nofollow" href="http://twistedmatrix.com/bugs/">http://twistedmatrix.com/bugs/</a></i></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2003-2008 Twisted Matrix Laboratories.<br/>
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
