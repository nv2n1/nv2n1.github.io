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
<pre><code>
gmk_msh[options][mfile][gfile]
</code></pre>
<p> The <code>gmk_msh</code> program creates a source graph from a source mesh. The vertices of the graph are the nodes of the mesh, and all mesh elements are turned into cliques, that is, there exists an edge between two vertices in the graph if there exists at least an element in the mesh which comprises the two associated nodes.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></dt>
<dd> Display some help.</dd>
<dt><code>-V</code></dt>
<dd> Display program version and copyright.</dd></dl>
<h2>EXAMPLE</h2>
<p> Create a source graph brol.grf from a source mesh brol.msh: </p>
<pre>
    $ gmk_msh brol.msh brol.grf
</pre>
<h2>SEE ALSO</h2>
<p> dgmap (1), <code>dgord</code>(1), <code>gmap</code>(1), <code>gord</code>(1), <code>gtst</code>(1), <code>mmk_m2</code>(1), <code>mord</code>(1), <code>mcv</code>(1), <code>mtst</code>(1). </p>
<p> Scotch user&#8217;s manual.</p>
<h2>AUTHOR</h2>
<p> Francois Pellegrini &lt;francois.pellegrini [at] labri.fr&gt; </p>
