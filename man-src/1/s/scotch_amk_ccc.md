---
title: "scotch_amk_ccc(1)"
name: "scotch_amk_ccc"
section: "1"
letter: "s"
url: "/docs/linux/man/1-scotch_amk_ccc/"
description: "amk_ccc, amk_fft2, amk_hy, amk_m2, amk_p2 – create target architectures"
---

<h2>NAME</h2>
<p> <code>amk_ccc, amk_fft2, amk_hy, amk_m2, amk_p2 </code>&#8211; create target architectures</p>
<h2>SYNOPSIS</h2>
<pre><code>
amk_ccc[options] dim[tfile] amk_fft2[options] dim[tfile] amk_hy[options] dim[tfile] amk_m2[options] dimX[dimY][tfile] amk_p2[options][wght0][wght1][tfile]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The amk_* programs create target architecture files for some common, regular topologies. </p>
<p> <code>amk_ccc</code> creates a decomposition-defined cube-connected-cycle topology of dimension <i>dim</i>. The decomposition is performed first by bisection along the dimensions of the hypercube, then along the remaining cycle graphs. </p>
<p> <code>amk_fft2</code> creates a decomposition-defined fast-Fourier-transform topology of dimension <i>dim</i>. The decomposition is performed by recursive bisection of the vertices, by descending dimension (that is, bit number in the labeling of the vertices). </p>
<p> <code>amk_hy</code> creates a decomposition-defined hypercube topology of dimension <i>dim</i>. The decomposition is performed by recursive bisection of the vertices, by descending dimension (that is, bit number in the labeling of the vertices). Save for experimentation purposes, this program is deprecated, as the algorithmically-defined &#8216;hcub&#8217; target architecture is a more convenient and efficient way to represent hypercube architectures. </p>
<p> <code>amk_m2</code> creates a decomposition-defined 2D regular grid topology of dimensions <i>dimX</i> and <i>dimY</i>. The decomposition is performed by recursive splitting along the dimensions, either by cutting the longest one, or by one-way dissection, depending on the &#8216;<code>-m</code>&#8216; option flag. Save for experimentation purposes, this program is deprecated, as the algorithmically-defined &#8216;mesh2D&#8217; and &#8216;mesh3D&#8217; target architectures are a more convenient and efficient way to represent 2D and 3D grid architectures. </p>
<p> <code>amk_p2</code> creates a weighted path graph topology comprising only two vertices of weights <i>wght0</i> and <i>wght1</i>. This is just a helper program, which builds a &#8216;wcmplt&#8217; algorithmically-defined complete graph with two vertices. It may be used to compute weighted bisections of a graph.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-m</code><i>meth</i></p>
<dd> For <code>amk_m2</code> only. Perform either recursive dissection or one-way dissection, according to the given method flag:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>n</code></p>
<dd> perform nested dissection (default).</p>
<dt><code>o</code></p>
<dd> perform one-way dissection (cut across Y, then X).</dl>
</dl>
<dt><code>-h</code></p>
<dd> Display some help.</p>
<dt><code>-V</code></p>
<dd> Display program version and copyright.</dl>
<h2>EXAMPLE</h2>
<p> Create a cube-connected-cycle target architecture of dimension 4, and save it to file &#8216;ccc4.tgt&#8217;. </p>
<pre>
    $ amk_ccc 4 ccc4.tgt
</pre>
<p> Run gmap to compute a bisection, into two parts of respective weights 3 and 5, of graph &#8216;brol.grf&#8217; and save the resulting mapping to file &#8216;brol.map&#8217;. The dash &#8216;-&#8216; standard file name is used so that the target architecture description is read from the standard input, through the pipe. </p>
<pre>
    $ amk_p2 3 5 | gmap brol.grf - brol.map
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gmk_msh/">gmk_msh</a></code>(1), <code><a href="/docs/linux/man/1-gtst/">gtst</a></code>(1), <code><a href="/docs/linux/man/1-gmap/">gmap</a></code>(1), <code><a href="/docs/linux/man/1-gord/">gord</a></code>(1), <code><a href="/docs/linux/man/1-gout/">gout</a></code>(1), <code><a href="/docs/linux/man/1-amk_grf/">amk_grf</a></code>(1). </p>
<p> Scotch user&#8217;s manual.</p>
<h2>AUTHOR</h2>
<p> Francois Pellegrini &lt;francois.pellegrini [at] labri.fr&gt; </p>
<h2>Index</h2>
