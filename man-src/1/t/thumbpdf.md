---
title: "thumbpdf(1)"
name: "thumbpdf"
section: "1"
letter: "t"
url: "/docs/linux/man/1-thumbpdf/"
description: "thumbpdf – generate thumbnail images for a PDF file created with pdftex"
---

<h2>NAME</h2>
<p> thumbpdf &#8211; generate thumbnail images for a PDF file created with <code>pdftex</code> </p>
<h2>SYNOPSIS</h2>
<p> <code>thumbpdf</code> [ <i>OPTION</i>&#8230; ] <i>PDF_FILE</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>thumbpdf</code> is used to create thumbnail images of individual pages within a PDF (Portable Document Format) document. </p>
<h2>USAGE</h2>
<p> First run <code><a href="/docs/linux/man/1-pdftex/">pdftex</a></code>(1) on your document to create a PDF file. Then run <code>thumbpdf</code> to generate the thumbnails, a PDF file containing the thumbnails, and a pdfTeX file to include the thumbnails in the PDF file. Finally, run <code><a href="/docs/linux/man/1-pdftex/">pdftex</a></code>(1) on your file again to create the final PDF file. </p>
<p> <code>thumbpdf</code> calls <code><a href="/docs/linux/man/1-gs/">gs</a></code>(1) to generate PNG images of the pages within <i>PDF_FILE</i>, and <code><a href="/docs/linux/man/1-pdftex/">pdftex</a></code>(1) to create a PDF file containing the thumbnail images. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> print usage</p>
<dt><code>&#8211;(no)makepng</code></p>
<dd> make PNG thumbnail images (default: true)</p>
<dt><code>&#8211;(no)makepdf</code></p>
<dd> generate new PDF file containing the thumbnails (default: true)</p>
<dt><code>&#8211;(no)makedef</code></p>
<dd> create a TeX file for <code><a href="/docs/linux/man/1-pdftex/">pdftex</a></code>(1) to read in (default: true)</p>
<dt><code>&#8211;(no)quiet</code></p>
<dd> suppress messages (default: false)</p>
<dt><code>&#8211;(no)verbose</code></p>
<dd> verbose messages (default: false)</p>
<dt><code>&#8211;(no)debug</code></p>
<dd> print debugging information while parsing (default: false)</p>
<dt><code>&#8211;resolution</code> <i>res</i></p>
<dd> resolution for GhostScript step (default: 9)</p>
<dt><code>&#8211;compress</code> <i>n</i></p>
<dd> \pdfcompresslevel for <code>thumbpdf.pdf</code> (0-9; default: 9)</p>
<dt><code>&#8211;device</code> | <code>png</code><i>dev</i></p>
<dd> GhostScript PNG device; <i>dev</i> = `mono&#8217;, `gray&#8217;, `16&#8242;, `256&#8242;, `16m&#8217; (default: `png16m&#8217;)</dl>
<h2>FILES</h2>
<dl>
<dt><i>thumb</i>nn<i>.png</i></p>
<dd> PNG thumbnail images</p>
<dt><i>thumbpdf.pdf</i></p>
<dd> PDF file containing thumbnail images</p>
<dt><i>thumbpdf.tex</i></p>
<dd> A pdfTeX program to include the thumbnails file</p>
<dt><i>thumbpdf.log</i></p>
<dd> pdfTeX log file</p>
<dt><i>thumbpdf.sty</i></p>
<dd> a LaTeX package to be included in files for which a user wants to generate thumbnails</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gs/">gs</a></code>(1), <code><a href="/docs/linux/man/1-pdftex/">pdftex</a></code>(1). </p>
<p> Web page: &lt;<a rel="nofollow" href="http://tug.org/teTeX/">http://tug.org/teTeX/</a>&gt; </p>
<h2>BUGS</h2>
<p> None known, but report any bugs found to the author. </p>
<h2>COPYRIGHT</h2>
<p> version 1, or (at your option) a later version of the LaTeX Project Public License. </p>
<h2>AUTHOR</h2>
<p> <code>thumbpdf</code> was written by Heiko Oberdiek &lt;oberdiek [at] ruf.uni-freiburg.de&gt;. </p>
<p> This manual page was written by C.M. Connelly &lt;c@eskimo.com&gt;, for the Debian GNU/Linux system. It may be used by other distributions without contacting the author. Any mistakes or omissions in the manual page are my fault; inquiries about or corrections to this manual page should be directed to me (and not to the primary author). </p>
<h2>Index</h2>
