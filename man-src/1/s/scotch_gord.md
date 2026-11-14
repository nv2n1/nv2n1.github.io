---
title: "scotch_gord(1)"
name: "scotch_gord"
section: "1"
letter: "s"
url: "/docs/linux/man/1-scotch_gord/"
description: "gord – compute sparse matrix orderings of graphs"
---

<h2>NAME</h2>
<p> <code>gord </code>&#8211; compute sparse matrix orderings of graphs</p>
<h2>SYNOPSIS</h2>
<pre><code>
gord[options][gfile][ofile][lfile]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>gord</code> program computes, in a sequential way, an ordering of a Scotch source graph representing the pattern of some symmetric sparse matrix. </p>
<p> Source graph file <i>gfile</i> can only be a centralized graph file. The resulting ordering is stored in file <i>ofile</i>. Eventual logging information (such as the one produced by option <code>-v</code>) is sent to file <i>lfile</i>. When file names are not specified, data is read from standard input and written to standard output. Standard streams can also be explicitely represented by a dash &#8216;-&#8216;. </p>
<p> When the proper libraries have been included at compile time, <code>gord</code> can directly handle compressed graphs, both as input and output. A stream is treated as compressed whenever its name is postfixed with a compressed file extension, such as in &#8216;brol.grf.bz2&#8217; or &#8216;-.gz&#8217;. The compression formats which can be supported are the bzip2 format (&#8216;.bz2&#8217;), the gzip format (&#8216;.gz&#8217;), and the lzma format (&#8216;.lzma&#8217;, on input only).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code>opt</p>
<dd> Choose default ordering strategy according to one or several <i>options</i> among:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>b</code></p>
<dd> enforce load balance as much as possible.</p>
<dt><code>q</code></p>
<dd> privilege quality over speed (default).</p>
<dt><code>s</code></p>
<dd> privilege speed over quality.</p>
<dt><code>t</code></p>
<dd> enforce safety.</dl>
</dl>
<dt><code>-h</code></p>
<dd> Display some help.</p>
<dt><code>-m</code><i>mfile</i></p>
<dd> Save column block mapping data to file <i>mfile</i>. Mapping data specifies, for each vertex, the index of the column block to which this vertex belongs.</p>
<dt><code>-o</code><i>strat</i></p>
<dd> Use sequential graph ordering strategy <i>strat</i> (see Scotch user&#8217;s manual for more information).</p>
<dt><code>-t</code><i>tfile</i></p>
<dd> Save partitioning tree data to file <i>tfile</i>. Partitioning tree data specifies, for each vertex, the index of the first vertex of the parent block of the block to which the vertex belongs. Altogether with the mapping data provided in file <i>mfile</i>, it allows one to rebuild the separator tree of the nested dissection process.</p>
<dt><code>-V</code></p>
<dd> Display program version and copyright.</p>
<dt><code>-v</code><i>verb</i></p>
<dd> Set verbose mode to <i>verb</i>. It is a set of one of more characters which can be:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>s</code></p>
<dd> strategy information.</p>
<dt><code>t</code></p>
<dd> timing information.</dl>
</dl>
</dl>
<h2>EXAMPLE</h2>
<p> Reorder matrix graph brol.grf and save the resulting ordering to file brol.ord using the default sequential graph ordering strategy: </p>
<pre>
    $ gord brol.grf brol.ord
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dgord/">dgord</a></code>(1), <code><a href="/docs/linux/man/1-gmk_hy/">gmk_hy</a></code>(1), <code><a href="/docs/linux/man/1-gtst/">gtst</a></code>(1). </p>
<p> Scotch user&#8217;s manual.</p>
<h2>AUTHOR</h2>
<p> Francois Pellegrini &lt;francois.pellegrini [at] labri.fr&gt; </p>
<h2>Index</h2>
