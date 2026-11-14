---
title: "scotch_gmap(1)"
name: "scotch_gmap"
section: "1"
letter: "s"
url: "/docs/linux/man/1-scotch_gmap/"
description: "gmap, gpart – compute static mappings and partitions sequentially"
---

<h2>NAME</h2>
<p> <code>gmap, gpart </code>&#8211; compute static mappings and partitions sequentially</p>
<h2>SYNOPSIS</h2>
<pre><code>
gmap[options][gfile][tfile][mfile][lfile] gpart[options][nparts][gfile][mfile][lfile]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>gmap</code> program computes, in a sequential way, a static mapping of a source graph onto a target graph. </p>
<p> The <code>gpart</code> program is a shortcut of <code>gmap</code> for computing unweighted partitions of a source graph. </p>
<p> Source graph file <i>gfile</i> can only be a centralized graph file. For <code>gmap</code>, the target architecture file <i>tfile</i> describes either algorithmically-coded topologies such as meshes and hypercubes, or decomposition-defined architectures created by means of the <code><a href="/docs/linux/man/1-amk_grf/">amk_grf</a></code>(1) program. The resulting mapping is stored in file <i>mfile</i>. Eventual logging information (such as the one produced by option <code>-v</code>) is sent to file <i>lfile</i>. When file names are not specified, data is read from standard input and written to standard output. Standard streams can also be explicitely represented by a dash &#8216;-&#8216;. </p>
<p> When the proper libraries have been included at compile time, <code>gmap</code> and <code>gpart</code> can directly handle compressed graphs, both as input and output. A stream is treated as compressed whenever its name is postfixed with a compressed file extension, such as in &#8216;brol.grf.bz2&#8217; or &#8216;-.gz&#8217;. The compression formats which can be supported are the bzip2 format (&#8216;.bz2&#8217;), the gzip format (&#8216;.gz&#8217;), and the lzma format (&#8216;.lzma&#8217;, on input only).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code>opt</p>
<dd> Choose default mapping strategy according to one or several <i>options</i> among:</p>
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
<dt><code>-m</code>strat</p>
<dd> Use sequential mapping strategy strat (see Scotch user&#8217;s manual for more information).</p>
<dt><code>-V</code></p>
<dd> Display program version and copyright.</p>
<dt><code>-v</code>verb</p>
<dd> Set verbose mode to verb. It is a set of one of more characters which can be:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>m</code></p>
<dd> mapping information.</p>
<dt><code>s</code></p>
<dd> strategy information.</p>
<dt><code>t</code></p>
<dd> timing information.</dl>
</dl>
</dl>
<h2>TARGET ARCHITECTURES</h2>
<p> Target architectures represent graphs onto which source graphs are mapped. In order to speed-up the obtainment of target architecture topological properties during the computation of mappings, some classical topologies are algorithmically coded into the mapper itself. These topologies are consequently simply defined by their code name, followed by their dimensional parameters:</p>
<dl>
<dt><code>cmplt </code><i>dim</i></p>
<dd> unweighted complete graph of size <i>dim</i>.</p>
<dt><code>cmpltw </code><i>dim</i> <i>w0</i> <i>w1</i> &#8230; <i>wdim-1</i></p>
<dd> weighted complete graph of size size and of respective loads <i>w0</i>, <i>w1</i>, &#8230;, <i>wdim-1</i>.</p>
<dt><code>hcub </code><i>dim</i></p>
<dd> hypercube of dimension <i>dim</i>.</p>
<dt><code>leaf </code><i>hgt</i> <i>n0</i> <i>w0</i> &#8230; <i>nhgt-1</i> <i>whgt-1</i></p>
<dd> tree-leaf graph of height <i>hgt</i> with (<i>n0</i> times <i>n1</i> times &#8230; <i>nhgt-1</i>) vertices, with inter-cluster link weights of <i>w0</i>, <i>w1</i>, &#8230; <i>whgt-1</i>.</p>
<dt><code>mesh2D </code><i>dimX</i> <i>dimY</i></p>
<dd> 2D mesh of <i>dimX</i> times <i>dimY</i> nodes.</p>
<dt><code>mesh3D </code><i>dimX</i> <i>dimY</i> <i>dimZ</i></p>
<dd> 23 mesh of <i>dimX</i> times <i>dimY</i> times <i>dimZ</i> nodes.</p>
<dt><code>torus2D </code><i>dimX</i> <i>dimY</i></p>
<dd> 2D torus of <i>dimX</i> times <i>dimY</i> nodes.</p>
<dt><code>torus3D </code><i>dimX</i> <i>dimY</i> <i>dimZ</i></p>
<dd> 3D torus of <i>dimX</i> times <i>dimY</i> times <i>dimZ</i> nodes.</dl>
<p> Other target topologies can be created from their source graph description by using the <code><a href="/docs/linux/man/1-amk_grf/">amk_grf</a></code>(1) command. In this case, the target description will begin with the code name <code>deco</code>.</p>
<h2>MAPPINGS</h2>
<p> Mappings are represented by as many lines as there are vertices in the source graph. Each of these lines is made of two figures: the number of the vertex (or its label if source graph vertices are labeled) and the index of the target vertex to which it has been assigned. Target vertex indices range from 0 to the number of vertices in the target architecture (that is, the number of parts) minus one. </p>
<p> This block of lines is always preceded by the number of such lines. In most cases, since full mappings are requested, the number of lines is equal to the number of vertices in the source graph.</p>
<h2>EXAMPLES</h2>
<p> Run <code>gpart</code> to compute a partition into 7 parts of graph &#8216;brol.grf&#8217; and save the resulting ordering to file &#8216;brol.map&#8217;. </p>
<pre>
    $ gpart 7 brol.grf brol.map
</pre>
<p> Run <code>gmap</code> to compute a partition, into 3 parts of respective weights 1, 2 and 4, of graph &#8216;brol.grf&#8217; and save the resulting mapping to file &#8216;brol.map&#8217;. The dash &#8216;-&#8216; standard file name is used so that the target architecture description is read from the standard input, through the pipe, as provided by the &#8216;echo&#8217; shell command. </p>
<pre>
    $ echo &quot;cmpltw 3 1 2 4&quot; | gmap brol.grf - brol.map
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-amk_grf/">amk_grf</a></code>(1), <code><a href="/docs/linux/man/1-acpl/">acpl</a></code>(1), <code><a href="/docs/linux/man/1-gmtst/">gmtst</a></code>(1), <code><a href="/docs/linux/man/1-dgmap/">dgmap</a></code>(1). </p>
<p> Scotch user&#8217;s manual.</p>
<h2>AUTHOR</h2>
<p> Francois Pellegrini &lt;francois.pellegrini [at] labri.fr&gt; </p>
<h2>Index</h2>
