---
title: "scotch_gmk_hy(1)"
name: "scotch_gmk_hy"
section: "1"
letter: "s"
url: "/docs/linux/man/1-scotch_gmk_hy/"
description: "gmk_hy, gmk_m2, gmk_m3, gmk_ub2 – create source graphs"
---

<h2>NAME</h2>
<p> <code>gmk_hy, gmk_m2, gmk_m3, gmk_ub2 </code>&#8211; create source graphs</p>
<h2>SYNOPSIS</h2>
<pre><code>
gmk_hy[options] dim[ofile] gmk_m2[options][-gcfile] dimX dimY[ofile] gmk_m3[options][-gcfile] dimX dimY dimZ[ofile] gmk_ub2[options] dim
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>gmk_</code>* programs create source graph files for some common, regular topologies. </p>
<p> <code>gmk_hy</code> creates a hypercube of dimension <i>dim</i>. </p>
<p> <code>gmk_m2</code> creates a 2D regular grid of dimensions <i>dimX</i> and <i>dimY</i>. </p>
<p> <code>gmk_m3</code> creates a 3D regular grid of dimensions <i>dimX</i>, <i>dimY</i> and <i>dimZ</i>. </p>
<p> <code>gmk_ub2</code> creates an unoriented de Bruijn graph of dimension <i>dim</i>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code> base</p>
<dd> For <code>gmk_m2</code> and <code>gmk_m3</code> only. Output graphs with base value set to base. Default value is 0.</p>
<dt><code>-e</code></p>
<dd> For <code>gmk_m2</code> only. Build a 8-neighbor grid rather than a 4-neighbor grid.</p>
<dt><code>-g</code><i>cfile</i></p>
<dd> For <code>gmk_m2</code> and <code>gmk_m3</code> only. Output graph vertex coordinates (that is, geometry data to be used by <code><a href="/docs/linux/man/1-gout/">gout</a></code>(1)) in file <i>cfile</i>.</p>
<dt><code>-h</code></p>
<dd> Display some help.</p>
<dt><code>-t</code></p>
<dd> For <code>gmk_m2</code> and <code>gmk_m3</code> only. Create torus graphs, that is, graphs such that there exist loop edges between vertices of rank 0 and (<i>dim</i>-1) in every dimension.</p>
<dt><code>-V</code></p>
<dd> Display program version and copyright.</dl>
<h2>EXAMPLE</h2>
<p> Create a 5&#215;7 grid along with its geometry: </p>
<pre>
    $ gmk_m2 5 7 -g/tmp/m5x7.xyz /tmp/m5x7.grf
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gmk_msh/">gmk_msh</a></code>(1), <code><a href="/docs/linux/man/1-gtst/">gtst</a></code>(1), <code><a href="/docs/linux/man/1-gmap/">gmap</a></code>(1), <code><a href="/docs/linux/man/1-gord/">gord</a></code>(1), <code><a href="/docs/linux/man/1-gout/">gout</a></code>(1), <code><a href="/docs/linux/man/1-amk_grf/">amk_grf</a></code>(1). </p>
<p> Scotch user&#8217;s manual.</p>
<h2>AUTHOR</h2>
<p> Francois Pellegrini &lt;francois.pellegrini [at] labri.fr&gt; </p>
<h2>Index</h2>
