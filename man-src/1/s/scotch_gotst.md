---
title: "scotch_gotst(1)"
name: "scotch_gotst"
section: "1"
letter: "s"
url: "/docs/linux/man/1-scotch_gotst/"
description: "gomtst – compute statistics on sparse matrix orderings"
---

<h2>NAME</h2>
<p> <code>gomtst </code>&#8211; compute statistics on sparse matrix orderings</p>
<h2>SYNOPSIS</h2>
<pre><code>
gotst[options][gfile][ofile][lfile]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>gotst</code> program computes, in a sequential way, statistics on a sparse matrix ordering, such as fill-in, operation count, and separator tree parameters: minimum, maximum, average height and variance of its leaves. </p>
<p> Source graph file <i>gfile</i> can only be a centralized graph file. File <i>ofile</i> represents the ordering of the symmetric sparse matrix the pattern of which is represented by <i>gfile</i>. The resulting statistics are stored in file <i>lfile</i>. When file names are not specified, data is read from standard input and written to standard output. Standard streams can also be explicitly represented by a dash &#8216;-&#8216;. </p>
<p> When the proper libraries have been included at compile time, gtst can directly handle compressed graphs, both as input and output. A stream is treated as compressed whenever its name is postfixed with a compressed file extension, such as in &#8216;brol.grf.bz2&#8217; or &#8216;-.gz&#8217;. The compression formats which can be supported are the bzip2 format (&#8216;.bz2&#8217;), the gzip format (&#8216;.gz&#8217;), and the lzma format (&#8216;.lzma&#8217;, on input only). </p>
<p> Since <code>gotst</code> performs sequentially the symbolic factorization of matrix <i>gfile</i> in order to compute fill-in and operation count numbers, this program can take a long time or even run out of memory, when applied to very large graphs.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> Display some help.</p>
<dt><code>-V</code></p>
<dd> Display program version and copyright.</dl>
<h2>EXAMPLE</h2>
<p> Display statistics on ordering brol.ord of graph brol.grf: </p>
<pre>
    $ gotst brol.grf brol.ord
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gord/">gord</a></code>(1), <code><a href="/docs/linux/man/1-gtst/">gtst</a></code>(1), <code><a href="/docs/linux/man/1-dgord/">dgord</a></code>(1). </p>
<p> Scotch user&#8217;s manual.</p>
<h2>AUTHOR</h2>
<p> Francois Pellegrini &lt;francois.pellegrini [at] labri.fr&gt; </p>
<h2>Index</h2>
