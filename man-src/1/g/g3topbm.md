---
title: "g3topbm(1)"
name: "g3topbm"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g3topbm/"
description: "g3topbm – convert a Group 3 fax file into a portable bitmap"
---

<h2 class="name">NAME</h2>
<p> g3topbm &#8211; convert a Group 3 fax file into a portable bitmap </p>
<h2>SYNOPSIS</h2>
<p> <code>g3topbm</code> [<code>-kludge</code>] [<code>-reversebits</code>] [<code>-stretch</code>] [<i>g3file</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a Group 3 fax file as input. Produces a portable bitmap as output.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-kludge</code></p>
<dd> Tells <i>g3topbm</i> to ignore the first few lines of the file; sometimes fax files have some junk at the beginning.</p>
<dt><code>-reversebits</code></p>
<dd> Tells <i>g3topbm</i> to interpret bits least-significant first, instead of the default most-significant first. Apparently some fax modems do it one way and others do it the other way. If you get a whole bunch of &quot;bad code word&quot; messages, try using this flag.</p>
<dt><code>-stretch</code></p>
<dd> Tells <i>g3topbm</i> to stretch the image vertically by duplicating each row. This is for the low-quality transmission mode.</dl>
<p> All flags can be abbreviated to their shortest unique prefix.</p>
<h2>REFERENCES</h2>
<p> The standard for Group 3 fax is defined in CCITT Recommendation T.4.</p>
<h2>BUGS</h2>
<p> Probably.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-pbmtog3/">pbmtog3</a>(1), <a href="/docs/linux/man/5-pbm/">pbm</a>(5)</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1989 by Paul Haeberli &lt;paul [at] manray.sgi.com&gt;. </p>
<h2>Index</h2>
