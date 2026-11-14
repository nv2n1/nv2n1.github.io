---
title: "bibzbladd(1)"
name: "bibzbladd"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bibzbladd/"
description: "bibzbladd.pl – add Zbl numbers to papers in a given bib file"
---

<h2 class="name">NAME</h2>
<p> bibzbladd.pl &#8211; add Zbl numbers to papers in a given bib file </p>
<h2>SYNOPSIS</h2>
<p> bibzbladd [-d] [<code>-f</code>] [<code>-e</code> 1|0] [<code>-o</code> <i>output</i>] <i>bib_file</i></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code></p>
<dd> Debug mode</p>
<dt><code>-e</code></p>
<dd> If 1 (default), add an empty zblnumber if a zbl cannot be found. This prevents repeated searches for the same entries if you add new entries to the file. Calling <tt>&quot;-e 0&quot;</tt> suppresses this behavior.</p>
<dt><code>-f</code></p>
<dd> Force searching for Zbl numbers even if the entry already has one.</p>
<dt><code>-o</code> <i>output</i></p>
<dd> Output file. If this option is not used, the name for the output file is formed by adding <tt>&quot;_zbl&quot;</tt> to the input file</dl>
<h2>DESCRIPTION</h2>
<p> The script reads a BibTeX file. It checks whether the entries have Zbls. If not, tries to contact internet to get the numbers. The result is a BibTeX file with the fields <tt>&quot;zblnumber=...&quot;</tt> added. </p>
<p> The name of the output file is either set by the <code>-o</code> option or is derived by adding the suffix <tt>&quot;_zbl&quot;</tt> to the output file.</p>
<h2>AUTHOR</h2>
<p> Boris Veytsman</p>
<h2>COPYRIGHT AND LICENSE</h2>
<p> Copyright (C) 2014-2021 Boris Veytsman </p>
<p> This is free software. You may redistribute copies of it under the terms of the <font SIZE="-1">GNU</font> General Public License &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/gpl.html">http://www.gnu.org/licenses/gpl.html</a>&gt;. There is <font SIZE="-1">NO WARRANTY,</font> to the extent permitted by law. </p>
<h2>Index</h2>
