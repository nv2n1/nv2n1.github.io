---
title: "scotch_gmk_msh(1)"
name: "scotch_gmk_msh"
section: "1"
letter: "s"
url: "/docs/linux/man/1-scotch_gmk_msh/"
description: "gmk_msh – create source graph from source mesh"
---

<h2>NAME</h2>
<p> <code>gmk_msh </code>&#8211; create source graph from source mesh</p>
<h2>SYNOPSIS</h2>
<pre><code>
gmk_msh[options][mfile][gfile]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>gmk_msh</code> program creates a source graph from a source mesh. The vertices of the graph are the nodes of the mesh, and all mesh elements are turned into cliques, that is, there exists an edge between two vertices in the graph if there exists at least an element in the mesh which comprises the two associated nodes.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> Display some help.</p>
<dt><code>-V</code></p>
<dd> Display program version and copyright.</dl>
<h2>EXAMPLE</h2>
<p> Create a source graph brol.grf from a source mesh brol.msh: </p>
<pre>
    $ gmk_msh brol.msh brol.grf
</pre>
<h2>SEE ALSO</h2>
<p> dgmap (1), <code><a href="/docs/linux/man/1-dgord/">dgord</a></code>(1), <code><a href="/docs/linux/man/1-gmap/">gmap</a></code>(1), <code><a href="/docs/linux/man/1-gord/">gord</a></code>(1), <code><a href="/docs/linux/man/1-gtst/">gtst</a></code>(1), <code><a href="/docs/linux/man/1-mmk_m2/">mmk_m2</a></code>(1), <code><a href="/docs/linux/man/1-mord/">mord</a></code>(1), <code><a href="/docs/linux/man/1-mcv/">mcv</a></code>(1), <code><a href="/docs/linux/man/1-mtst/">mtst</a></code>(1). </p>
<p> Scotch user&#8217;s manual.</p>
<h2>AUTHOR</h2>
<p> Francois Pellegrini &lt;francois.pellegrini [at] labri.fr&gt; </p>
<h2>Index</h2>
