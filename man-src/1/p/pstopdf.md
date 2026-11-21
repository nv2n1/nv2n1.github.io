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
<p> <code>pstopdf</code> [ <i>OPTION</i> &#8230; ] <i>FILE</i> [ &#8230; ] </p>
<p>&nbsp;<wbr> <code>pstopdf</code> converts EPS (encapsulated PostScript) to PDF. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></dt>
<dd> Print usage and version information.</dd>
<dt><code>&#8211;convert</code></dt>
<dd> Convert EPS to PDF. This option is assumed if none is given.</dd>
<dt><code>&#8211;method=</code><i>string</i></dt>
<dd> What method to use for bounding boxes when converting to PDF. Specify one of <code>crop</code>, <code>bounded</code> (the default), or <code>raw</code>. Older versions of ConTeXt used numerical methods (1, 2, or 3).</dd>
<dt><code>&#8211;resolution=</code><i>string</i></dt>
<dd> The resolution to use when when converting to pdf. Specify one of <code>low</code>, <code>normal</code>, <code>medium</code>, <code>high</code>, <code>printer</code>, <code>print</code>, <code>screen</code>, <code>ebook</code>, or <code>default</code>.</dd>
<dt><code>&#8211;request</code></dt>
<dd> Handle exa request file.</dd>
<dt><code>&#8211;watch</code></dt>
<dd> Watch folders for conversions (<i>untested</i>). </dd>
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
