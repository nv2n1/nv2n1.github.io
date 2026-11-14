---
title: "dt2dv(1)"
name: "dt2dv"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dt2dv/"
description: "dt2dv – convert a DTL text representation of a TeX DVI file to a binary DVI file"
---

<h2 class="name">NAME</h2>
<p> dt2dv &#8211; convert a DTL text representation of a TeX DVI file to a binary DVI file </p>
<h2>SYNOPSIS</h2>
<p> <code>dt2dv</code> [<code>-debug</code>] [<code>-group</code>] [<code>-si</code>] [<code>-so</code>] [<i>input-DTL-file</i>] [<i>output-DVI-file</i>] </p>
<p> In the absence of the <code>-si</code> and <code>-so</code> options, both file arguments are <i>required</i> in the order <code>input-DTL-file output-DVI-file</code>. But also see the OPTIONS section below. No default file extensions are supplied.</p>
<h2>DESCRIPTION</h2>
<p> <code>dt2dv</code> converts a text representation of a TeX DVI file, usually produced by the companion <code><a href="/docs/linux/man/1-dv2dt/">dv2dt</a></code>(1) utility, back to a binary DVI file. DTL (<i>DVI Text Language</i>) files can be edited, with care, and then restored to DVI form for processing by any TeX DVI driver program. In DTL files, font directory names and font names are preceded by a length field, which must be updated if the names are modified. </p>
<p> <code><a href="/docs/linux/man/1-dvitype/">dvitype</a></code>(1) can also display a textual representation of DVI files, but in some implementations at least, it cannot be used in batch mode, and its output is not well-suited for conversion back to a DVI file. </p>
<p> The format of TeX DVI files is fully described in Donald E. Knuth, <i>TeX: The Program</i>, Addison-Wesley (1986), ISBN 0-201-13437-3, as well as in the <code><a href="/docs/linux/man/1-dvitype/">dvitype</a></code>(1) literate program source code. Brief descriptions of the DTL and DVI formats are given in <code><a href="/docs/linux/man/1-dv2dt/">dv2dt</a></code>(1).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-debug</code></p>
<dd> Turn on detailed debugging output.</p>
<dt><code>-group</code></p>
<dd> Expect each DTL command to be in parentheses.</p>
<dt><code>-si</code></p>
<dd> Read all DTL commands from standard input.</p>
<dt><code>-so</code></p>
<dd> Write all DVI commands to standard output.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dv2dt/">dv2dt</a></code>(1), <code><a href="/docs/linux/man/1-dvitype/">dvitype</a></code>(1), <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1).</p>
<h2>FILES</h2>
<dl>
<dt><i>*.dvi</i></p>
<dd> binary TeX DVI file.</p>
<dt><i>*.dtl</i></p>
<dd> text representation of a TeX DVI file in <i>DVI Text Language</i> format.</dl>
<h2>AUTHOR</h2>
<p> <code>dt2dv</code> and <code><a href="/docs/linux/man/1-dv2dt/">dv2dt</a></code>(1) were written by</p>
<dl>
<dt>
<dd>
<pre>
Geoffrey Tobin
Department of Electronic Engineering
La Trobe University
Bundoora, Victoria 3083
Australia
Tel: +61 3 479 3736
FAX: +61 3 479 3025
Email: &lt;G.Tobin [at] ee.latrobe.edu.au&gt;
</pre>
</dl>
<p> These manual pages were written primarily by</p>
<dl>
<dt>
<dd>
<pre>
Nelson H. F. Beebe, Ph.D.
Center for Scientific Computing
Department of Mathematics
University of Utah
Salt Lake City, UT 84112
Tel: +1 801 581 5254
FAX: +1 801 581 4148
Email: &lt;beebe [at] math.utah.edu&gt;
</pre>
</dl>
<h2>Index</h2>
