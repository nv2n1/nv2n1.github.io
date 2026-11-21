---
title: "mingle(1)"
name: "mingle"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mingle/"
description: "mingle – fast edge bundling"
---

<h2 class="name">NAME</h2>
<p> mingle &#8211; fast edge bundling </p>
<h2>SYNOPSIS</h2>
<p> <code>mingle</code> [ <i>options</i> ] [ <code>-o</code> <i>outfile</i> ] [ <i>files</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>mingle</code> takes as input a graph in DOT format with node position information (the <i>pos</i> attribute) and bundles the edges.</p>
<h2>OPTIONS</h2>
<p> The following options are supported:</p>
<dl>
<dt><code>-m</code><i> k</i></dt>
<dd> indicates which method to use for bundling. A value of 0 corresponds to a force-directed bundling. A value of 2 uses a cluster plus ink saving approach. If available, a value 1 denotes an agglomerative ink saving method. Normally, the last is the default.</dd>
<dt><code>-a</code><i> k</i></dt>
<dd> specifies the maximum turning angle, in degrees, as a non-negative real. The larger the value, the more edges may bend. If the value is 0, there is no limitation on the turning angle. The default is 40. The parameter is not used in force-directed bundling.</dd>
<dt><code>-c</code><i> v</i></dt>
<dd> specifies which compatability measure to use. The value 0, the default, uses a distance metric, while a value of 1 relies on full compatability. This value is only used in force-directed bundling.</dd>
<dt><code>-i</code><i> k</i></dt>
<dd> gives the maximum number of iterative divisions of edges allowd in force-directed bundling. The default is 4.</dd>
<dt><code>-k</code><i> k</i></dt>
<dd> gives the number of neighbors to be used in forming a nearest neighbor graph. This parameter is only used in the agglomerative method. The default is 10.</dd>
<dt><code>-K</code><i> k</i></dt>
<dd> is a positive real value giving the force constant used in force-directed bundling. By default, the value is determined automatically.</dd>
<dt><code>-o</code><i> file</i></dt>
<dd> puts output in <i>file</i>. Default output is stdout</dd>
<dt><code>-p</code><i> k</i></dt>
<dd> Except for the force-directed method, bundling minimizes $ink * (k &#8211; cos(turning angle))$. The larger the value of <i>k</i>, the less emphasis is put on avoiding sharp turning angles and the faster the bundling. The default value is -1.</dd>
<dt><code>-r</code><i> k</i></dt>
<dd> is a non-negative integer giving the maximum recursion level used in the agglomerative method. The default is 100.</dd>
<dt><code>-T</code><i> fmt</i></dt>
<dd> specifies the output format. At present, the output is always in the DOT format. If <i>fmt</i> is &quot;simple&quot;, the output is a simple, schematic representation of the drawing. Only the node positions and edges are retained from the original graph. If <i>fmt</i> is &quot;gv&quot;, the drawing information is attached to the input graph.</dd>
<dt><code>-v</code><i> k</i></dt>
<dd> determines the verbose level used for tracing the algorithm. The value <i>k</i> is optional; if not provided, the value 1 is used.</dd>
<dt><code>-?</code></dt>
<dd> Print usage and exit. </dd>
</dl>
<h2>BUGS</h2>
<p> At present, <code>mingle</code> does not handle graphs with loops or directed multiedges. So, a graph with edges <i>a -&gt; b</i> and <i>b -&gt; a</i> is acceptable, but not if it has edges <i>a -&gt; b</i> and <i>a -&gt; b</i> or <i>a &#8212; b</i> and <i>a &#8212; b</i>.</p>
<h2>AUTHOR</h2>
<p> Emden R. Gansner &lt;erg [at] graphviz.org&gt;, Yifan Hu &lt;yifanhu [at] yahoo.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-sfdp/">sfdp</a>(1), <a href="/docs/linux/man/1-neato/">neato</a>(1), <a href="/docs/linux/man/1-gvpr/">gvpr</a>(1) </p>
<p> Emden R. Gansner, Yifan Hu, Stephen C. North and Carlos Scheidegger, &#8220;Multilevel Agglomerative Edge Bundling for Visualizing Large Graphs&#8221;, IEEE Pacific Visualization Symposium PacificVis, pp. 187-194, 2011. </p>
