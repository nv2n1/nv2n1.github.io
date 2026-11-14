---
title: "gjots2html(1)"
name: "gjots2html"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gjots2html/"
description: "gjots2html – Convert a gjotsfile to HTML (on stdout)"
---

<h2>NAME</h2>
<p> gjots2html &#8211; Convert a gjotsfile to HTML (on <code>stdout</code>)</p>
<h2>SYNOPSIS</h2>
<p> <code>gjots2html</code> { <code>-lc</code> ] [ <code>-t</code><i> title</i> ] [ <code>-i</code><i> level</i> } [ <i>gjotsfile</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>gjots2html</code> converts a gjotsfile into HTML with a table of contents. Presently up to 8 levels of table of contents subject tree are supported. <code>gjotsfile</code> uses <code><a href="/docs/linux/man/1-m4/">m4</a></code>(1) and <code><a href="/docs/linux/man/1-awk/">awk</a></code>(1)</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-l</code></p>
<dd> adds <i>&lt;HR&gt; </i> lines after each section.</p>
<dt><code>-c</code></p>
<dd> adds a link to the TABLE OF CONTENTS after each section.</p>
<dt><code>-t</code><i> title</i></p>
<dd> adds a title to the page</p>
<dt><code>-i</code><i> level</i></p>
<dd> Creates the table of contents down to that level of heading. The default is to include all headings.</dl>
<h2>AUTHOR</h2>
<p> Written by Bob Hepple &lt;bhepple [at] freeshell.org&gt; <a rel="nofollow" href="http://bhepple.freeshell.org/gjots">http://bhepple.freeshell.org/gjots</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2002-2008 Robert Hepple<br />
 This is free software; see the source for copying condi­ tions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gjots/">gjots</a></code>(1), <code><a href="/docs/linux/man/1-gjots2docbook/">gjots2docbook</a></code>(1), <code><a href="/docs/linux/man/1-docbook2gjots/">docbook2gjots</a></code>(1), <code><a href="/docs/linux/man/1-gjots2html-py/">gjots2html.py</a></code>(1) </p>
<h2>Index</h2>
