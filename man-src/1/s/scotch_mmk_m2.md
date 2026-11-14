---
title: "scotch_mmk_m2(1)"
name: "scotch_mmk_m2"
section: "1"
letter: "s"
url: "/docs/linux/man/1-scotch_mmk_m2/"
description: "mmk_m2, mmk_m3 – create source meshes"
---

<h2>NAME</h2>
<p> <code>mmk_m2, mmk_m3 </code>&#8211; create source meshes</p>
<h2>SYNOPSIS</h2>
<pre><code>
mmk_m2[options][-gcfile] dimX dimY[ofile] mmk_m3[options][-gcfile] dimX dimY dimZ[ofile]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>mmk_</code>* programs create source mesh files for some common, regular topologies. </p>
<p> <code>mmk_m2</code> creates a 2D regular mesh of <i>dimX</i> times <i>dimY</i> elements and (<i>dimX</i>+1) times (<i>dimY</i>+1) nodes, such that element (i,j) is connected to nodes (i,j), (i,j+1), (i+1,j) and (i+1,j+1). </p>
<p> <code>mmk_m3</code> creates a 3D regular mesh of <i>dimX</i> times <i>dimY</i> times <i>dimZ</i> elements and (<i>dimX</i>+1) times (<i>dimY</i>+1) times (<i>dimZ</i>+1) nodes, such that element (i,j,k) is connected to nodes (i,j,k), (i,j,k+1), (i,j+1,k), (i,j+1,k+1), (i+1,j,k), (i+1,j,k+1), (i+1,j+1,k) and (i+1,j+1,k+1).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-g</code><i>cfile</i></p>
<dd> Output graph vertex coordinates (that is, geometry data to be used by <code><a href="/docs/linux/man/1-gout/">gout</a></code>(1)) in file <i>cfile</i>.</p>
<dt><code>-h</code></p>
<dd> Display some help.</p>
<dt><code>-V</code></p>
<dd> Display program version and copyright.</dl>
<h2>EXAMPLE</h2>
<p> Create a mesh of 5&#215;7 elements, along with its geometry: </p>
<pre>
    $ mmk_m2 5 7 -g/tmp/m5x7.xyz /tmp/m5x7.msh
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mord/">mord</a></code>(1), <code><a href="/docs/linux/man/1-mtst/">mtst</a></code>(1), <code><a href="/docs/linux/man/1-gmk_msh/">gmk_msh</a></code>(1). </p>
<p> Scotch user&#8217;s manual.</p>
<h2>AUTHOR</h2>
<p> Francois Pellegrini &lt;francois.pellegrini [at] labri.fr&gt; </p>
<h2>Index</h2>
