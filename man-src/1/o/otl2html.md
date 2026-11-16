---
title: "otl2html(1)"
name: "otl2html"
section: "1"
letter: "o"
url: "/docs/linux/man/1-otl2html/"
description: "otl2html – converts vimoutliner outline to HTML"
---

<h2 class="name">NAME</h2>
<p> otl2html &#8211; converts vimoutliner outline to HTML </p>
<h2>SYNOPSIS</h2>
<p> <code>otl2html</code> [<i>filename</i>]</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>otl2html</code> Python script. </p>
<p> <code>otl2html</code> is a is a <code><a href="/docs/linux/man/1-python/">python</a></code>(1) script that converts a <code>vimoutliner</code>(1) outline to HTML. </p>
<p> <code>otl2html</code> script called just with filename of the processed outline will produce HTML document on standard output.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-p</code></dt>
<dd> Presentation: slide show output for use with HtmlSlides.</dd>
<dt><code>-D</code></dt>
<dd> First-level is divisions (&lt;div&gt; &lt;/div&gt;) for making pretty web pages.</dd>
<dt><code>-s</code></dt>
<dd> <i>sheet</i> Use the specified style sheet with a link.</dd>
<dt><code>-S</code></dt>
<dd> <i>sheet</i> Include the specified style sheet in-line the output. For encapsulated style.</dd>
<dt><code>-T</code></dt>
<dd> The first line is not the title. Treat it as outline data</dd>
<dt><code>-c</code></dt>
<dd> Hide comments (line with [ as the first non-whitespace character. Ending with ] is optional.</dd>
<dt><code>-C</code></dt>
<dd> <i>copyright</i> Override the internal copyright notice with the one supplied in the quoted string following this flag. Single or double quotes can be used.</dd>
<dt><code>-v</code></dt>
<dd> Print version (RCS) information.</dd>
<dt><code>-H</code></dt>
<dd> Show the file syntax help.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-vim/">vim</a></code>(1), <code><a href="/docs/linux/man/1-python/">python</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Matej Cepl &lt;matej [at] ceplovi.cz&gt;, for the Debian GNU/Linux system (but may be used by others). </p>
<h2>Index</h2>
