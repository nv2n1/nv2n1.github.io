---
title: "scotch_gmtst(1)"
name: "scotch_gmtst"
section: "1"
letter: "s"
url: "/docs/linux/man/1-scotch_gmtst/"
description: "gmtst – compute statistics on mappings"
---

<h2>NAME</h2>
<p> <code>gmtst </code>&#8211; compute statistics on mappings</p>
<h2>SYNOPSIS</h2>
<pre><code>
gmtst[options][gfile][tfile][mfile][lfile]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>gmtst</code> program computes, in a sequential way, statistics on a static mapping, such as load imbalance ratio, edge dilation distribution, etc. It yields the same results as the ones produced by the <code>-vm</code> option of the <code><a href="/docs/linux/man/1-gmap/">gmap</a></code>(1) program. </p>
<p> Source graph file <i>gfile</i> can only be a centralized graph file. File <i>tfile</i> represents the target architecture onto which <i>gfile</i> was mapped. If mapping file <i>mfile</i> was produced by <code><a href="/docs/linux/man/1-gpart/">gpart</a></code>(1), the target architecture file to provide <code>gmtst</code> should describe a complete graph with the same number of vertices as the requested number of parts, for instance by means of the &#8216;<code>cmplt</code> <i>num</i>&#8216; algorithmically-described architecture. The resulting statistics are stored in file <i>lfile</i>. When file names are not specified, data is read from standard input and written to standard output. Standard streams can also be explicitly represented by a dash &#8216;-&#8216;. </p>
<p> When the proper libraries have been included at compile time, gtst can directly handle compressed graphs, both as input and output. A stream is treated as compressed whenever its name is postfixed with a compressed file extension, such as in &#8216;brol.grf.bz2&#8217; or &#8216;-.gz&#8217;. The compression formats which can be supported are the bzip2 format (&#8216;.bz2&#8217;), the gzip format (&#8216;.gz&#8217;), and the lzma format (&#8216;.lzma&#8217;, on input only).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> Display some help.</p>
<dt><code>-V</code></p>
<dd> Display program version and copyright.</dl>
<h2>EXAMPLES</h2>
<p> Display statistics on mapping brol.map of graph brol.grf onto target architecture brol.tgt: </p>
<pre>
    $ gmtst brol.grf brol.tgt brol.map
</pre>
<p> Display statistics on partitioning brol.map of graph brol.grf into <i>num</i> parts. Note the use of the complete graph algorithmically-described architecture and of the shell pipe command to provide the complete target architecture description on the standard input of the <code>gmtst</code> command: </p>
<pre>
    $ echo &quot;cmplt num&quot; | gmtst brol.grf - brol.map
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gmap/">gmap</a></code>(1), <code><a href="/docs/linux/man/1-gout/">gout</a></code>(1), <code><a href="/docs/linux/man/1-gtst/">gtst</a></code>(1). </p>
<p> Scotch user&#8217;s manual.</p>
<h2>AUTHOR</h2>
<p> Francois Pellegrini &lt;francois.pellegrini [at] labri.fr&gt; </p>
<h2>Index</h2>
