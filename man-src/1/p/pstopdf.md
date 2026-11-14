---
title: "pstopdf(1)"
name: "pstopdf"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pstopdf/"
description: "pstopdf – convert EPS to PDF"
---

<h2>NAME</h2>
<p> pstopdf &#8211; convert EPS to PDF </p>
<h2>SYNOPSIS</h2>
<p> <code>pstopdf</code> [ <i>OPTION</i> &#8230; ] <i>FILE</i> [ &#8230; ] </p>
<h2>DESCRIPTION</h2>
<p>&nbsp;<wbr> <code>pstopdf</code> converts EPS (encapsulated PostScript) to PDF. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Print usage and version information.</p>
<dt><code>&#8211;convert</code></p>
<dd> Convert EPS to PDF. This option is assumed if none is given.</p>
<dt><code>&#8211;method=</code><i>string</i></p>
<dd> What method to use for bounding boxes when converting to PDF. Specify one of <code>crop</code>, <code>bounded</code> (the default), or <code>raw</code>. Older versions of ConTeXt used numerical methods (1, 2, or 3).</p>
<dt><code>&#8211;resolution=</code><i>string</i></p>
<dd> The resolution to use when when converting to pdf. Specify one of <code>low</code>, <code>normal</code>, <code>medium</code>, <code>high</code>, <code>printer</code>, <code>print</code>, <code>screen</code>, <code>ebook</code>, or <code>default</code>.</p>
<dt><code>&#8211;request</code></p>
<dd> Handle exa request file.</p>
<dt><code>&#8211;watch</code></p>
<dd> Watch folders for conversions (<i>untested</i>). </p>
</dl>
<h2>EXAMPLES</h2>
<p> To make <i>cow.pdf</i>: </p>
<pre>
pstopdf cow.eps
</pre>
<p> or (one of several equivalents): </p>
<pre>
pstopdf --convert cow.eps cow.pdf
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-epstopdf/">epstopdf</a></code>(1), <code><a href="/docs/linux/man/1-mptopdf/">mptopdf</a></code>(1), <code><a href="/docs/linux/man/1-ps2pdf/">ps2pdf</a></code>(1), <code><a href="/docs/linux/man/1-texexec/">texexec</a></code>(1). </p>
<p> ConTeXt wiki &lt;URL: <a rel="nofollow" href="http://www.contextgarden.net">http://www.contextgarden.net</a> &gt;. </p>
<h2>AUTHOR</h2>
<p> This (incomplete) manual page was written by Sanjoy Mahajan &lt;sanjoy [at] mit.edu&gt;. It is in the public domain. </p>
<h2>Index</h2>
