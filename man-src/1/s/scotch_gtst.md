---

title: "scotch_gtst(1)"
name: "scotch_gtst"
section: "1"
letter: "s"
url: "/docs/linux/man/1-scotch_gtst/"
description: "gtst – test the consistency of source graphs"
---

<h2>NAME</h2>
<p> <code>gtst </code>&#8211; test the consistency of source graphs</p>
<pre><code>
gtst[options][gfile][lfile]
</code></pre>
<p> The <code>gtst</code> program checks, in a sequential way, the consistency of a Scotch source graph and, in case of success, outputs some statistics regarding edge weights, vertex weights, and vertex degrees. </p>
<p> It produces the very same results as the <code>dgtst</code>(1) program of the PT-Scotch parallel distribution, but unlike this latter it cannot handle distributed graphs. </p>
<p> Source graph file <i>gfile</i> can only be a centralized graph file. The resulting statistics are stored in file <i>lfile</i>. When file names are not specified, data is read from standard input and written to standard output. Standard streams can also be explicitly represented by a dash &#8216;-&#8216;. </p>
<p> When the proper libraries have been included at compile time, <code>gtst</code> can directly handle compressed graphs, both as input and output. A stream is treated as compressed whenever its name is postfixed with a compressed file extension, such as in &#8216;brol.grf.bz2&#8217; or &#8216;-.gz&#8217;. The compression formats which can be supported are the bzip2 format (&#8216;.bz2&#8217;), the gzip format (&#8216;.gz&#8217;), and the lzma format (&#8216;.lzma&#8217;, on input only).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></dt>
<dd> Display some help.</dd>
<dt><code>-V</code></dt>
<dd> Display program version and copyright.</dd></dl>
<h2>EXAMPLE</h2>
<p> Test the consistency of graph brol.grf: </p>
<pre>
    $ gtst brol.grf
</pre>
<h2>SEE ALSO</h2>
<p> <code>dgtst</code>(1), <code>gmap</code>(1), <code>gord</code>(1), <code>gout</code>(1). </p>
<p> Scotch user&#8217;s manual.</p>
<h2>AUTHOR</h2>
<p> Francois Pellegrini &lt;francois.pellegrini [at] labri.fr&gt; </p>
