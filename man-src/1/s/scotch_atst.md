---
title: "scotch_atst(1)"
name: "scotch_atst"
section: "1"
letter: "s"
url: "/docs/linux/man/1-scotch_atst/"
description: "atst – test the consistency of target architectures"
---

<h2>NAME</h2>
<p> <code>atst </code>&#8211; test the consistency of target architectures</p>
<h2>SYNOPSIS</h2>
<pre><code>
atst[options][afile][lfile]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>atst</code> program checks the consistency of a Scotch decomposition-defined target architecture and, in case of success, outputs some statistics regarding the number of target vertices and the length of paths linking them. Target architectures define the topology of the target graphs used by static mapping programs <code><a href="/docs/linux/man/1-gmap/">gmap</a></code>(1) and <code><a href="/docs/linux/man/1-dgmap/">dgmap</a></code>(1). </p>
<p> The resulting statistics are stored in file <i>lfile</i>. When file names are not specified, data is read from standard input and written to standard output. Standard streams can also be explicitly represented by a dash &#8216;-&#8216;. </p>
<p> When the proper libraries have been included at compile time, <code>atst</code> can directly handle compressed files, both as input and output. A stream is treated as compressed whenever its name is postfixed with a compressed file extension, such as in &#8216;brol.tgt.bz2&#8217; or &#8216;-.gz&#8217;. The compression formats which can be supported are the bzip2 format (&#8216;.bz2&#8217;), the gzip format (&#8216;.gz&#8217;), and the lzma format (&#8216;.lzma&#8217;, on input only).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> Display some help.</p>
<dt><code>-V</code></p>
<dd> Display program version and copyright.</dl>
<h2>EXAMPLE</h2>
<p> Test the consistency of architecture arch.tgt: </p>
<pre>
    $ atst arch.tgt
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-amk_grf/">amk_grf</a></code>(1), <code><a href="/docs/linux/man/1-amk_ccc/">amk_ccc</a></code>(1), <code><a href="/docs/linux/man/1-amk_fft2/">amk_fft2</a></code>(1), <code><a href="/docs/linux/man/1-amk_hy/">amk_hy</a></code>(1), <code><a href="/docs/linux/man/1-amk_m2/">amk_m2</a></code>(1), <code><a href="/docs/linux/man/1-amk_p2/">amk_p2</a></code>(1), <code><a href="/docs/linux/man/1-gmap/">gmap</a></code>(1), <code><a href="/docs/linux/man/1-dgmap/">dgmap</a></code>(1). </p>
<p> Scotch user&#8217;s manual.</p>
<h2>AUTHOR</h2>
<p> Francois Pellegrini &lt;francois.pellegrini [at] labri.fr&gt; </p>
<h2>Index</h2>
