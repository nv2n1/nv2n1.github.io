---

title: "scotch_gcv(1)"
name: "scotch_gcv"
section: "1"
letter: "s"
url: "/docs/linux/man/1-scotch_gcv/"
description: "gcv – graph file converter"
---

<p> <code>gcv </code>&#8211; graph file converter</p>
<h2>SYNOPSIS</h2>
<pre><code>
gcv[options][igfile][ogfile][oxfile]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>gcv</code> program converts Scotch graph files from and to other external file formats. </p>
<p> File <i>igfile</i> is converted into graph file <i>ogfile</i>, with optional geometry data being put in geometry file <i>oxfile</i>, if it is available. </p>
<p> When file names are not specified, data is read from standard input and written to standard output. Standard streams can also be explicitly represented by a dash &#8216;-&#8216;. </p>
<p> When the proper libraries have been included at compile time, dgtst can directly handle compressed graphs, both as input and output. A stream is treated as compressed whenever its name is postfixed with a compressed file extension, such as in &#8216;brol.grf.bz2&#8217; or &#8216;-.gz&#8217;. The compression formats which can be supported are the bzip2 format (&#8216;.bz2&#8217;), the gzip format (&#8216;.gz&#8217;), and the lzma format (&#8216;.lzma&#8217;, on input only).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></dt>
<dd> Display some help.</dd>
<dt><code>-i</code><i>ifmt</i></dt>
<dd> Set format of input graph file, which can be:</dd>
<dl>
<dl>
<dt><code>b</code><i>num</i></dt>
<dd> Boeing-Harwell format. This is a matrix format. Only square matrices are supported. Square matrices with unsymmetric pattern are symmetrized. In case the file contains several matrices, the <i>num</i> parameter allow the user to provide the index of the matrix to convert, starting from 0. When the <i>num</i> parameter is not set, it is assumed to be 0.</dd>
<dt><code>c</code></dt>
<dd> Chaco format. This is an adjacency graph format, also used by MeTiS.</dd>
<dt><code>m</code></dt>
<dd> Matrix Market format. This is a matrix format describing individual edges. Matrix pattern is symmetrized, such that rectangular matrices are eventually squared.</dd>
<dt><code>s</code></dt>
<dd> Scotch graph format. This is an adjacency graph format.</dd></dl>
</dl>
<dt><code>-o</code><i>ofmt</i></dt>
<dd> Set format of output graph file, which can be:</dd>
<dl>
<dl>
<dt><code>c</code></dt>
<dd> Chaco format.</dd>
<dt><code>m</code></dt>
<dd> Matrix Market symmetric pattern format.</dd>
<dt><code>s</code></dt>
<dd> Scotch format. This is the default.</dd></dl>
</dl>
<dt><code>-V</code></dt>
<dd> Display program version and copyright.</dd></dl>
<h2>EXAMPLE</h2>
<p> Convert a Matrix Market graph into a Scotch graph. Matrix Market files do not comprise geometry data, so no geometry file is needed on output: </p>
<pre>
    $ gcv -im brol.mm brol.grf
</pre>
<h2>SEE ALSO</h2>
<p> <code>gtst</code>(1), <code>gmap</code>(1), <code>gord</code>(1), <code>gout</code>(1). </p>
<p> Scotch user&#8217;s manual.</p>
<h2>AUTHOR</h2>
<p> Francois Pellegrini &lt;francois.pellegrini [at] labri.fr&gt; </p>
