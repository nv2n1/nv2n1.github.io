---
title: "graphviz(7)"
name: "graphviz"
section: "7"
letter: "g"
url: "/docs/linux/man/7-graphviz/"
description: "graphviz – rich set of graph drawing tools"
---

<p>graphviz &#8211; rich set of graph drawing tools</p>
<h2>Synopsis</h2>
<p>This manpage has been written to fulfil the need of a centralized documentation presenting all available tools in the graphviz package. </p>
<h2>Available Tools</h2>
<h3>Graph layout programs</h3>
<dl>
<dt><code>dot</code></p>
<dd>filter for hierarchical layouts of graphs</p>
<dt><code>neato</code></p>
<dd>filter for symmetric layouts of graphs</p>
<dt><code>twopi</code></p>
<dd>filter for radial layouts of graphs</p>
<dt><code>circo</code></p>
<dd>filter for circular layout of graphs</p>
<dt><code>fdp</code></p>
<dd>filter for symmetric layouts of graphs</dl>
<p> All of the filters work with either directed or undirected graphs, though <code>dot</code> is typically used for directed graphs and <code>neato</code> for undirected graphs. Note also that <code>neato -n[2]</code> can be used to render layouts produced by the other filters.</p>
<h3>Graph drawing programs</h3>
<dl>
<dt><code>lefty</code></p>
<dd>A Programmable Graphics Editor</p>
<dt><code>lneato</code></p>
<dd>lefty + neato</p>
<dt><code>dotty</code></p>
<dd>lefty + dot </p>
</dl>
<h3>Graph layout enhancement</h3>
<dl>
<dt><code>gvcolor</code></p>
<dd>flow colors through a ranked digraph</p>
<dt><code>unflatten</code></p>
<dd>adjust directed graphs to improve layout aspect ratio</p>
<dt><code>gvpack</code></p>
<dd>merge and pack disjoint graphs </p>
</dl>
<h3>Graph information and transformation</h3>
<dl>
<dt><code>gc</code></p>
<dd>count graph components</p>
<dt><code>acyclic</code></p>
<dd>make directed graph acyclic</p>
<dt><code>nop</code></p>
<dd>pretty-print graph file</p>
<dt><code>ccomps</code></p>
<dd>connected components filter for graphs</p>
<dt><code>sccmap</code></p>
<dd>extract strongly connected components of directed graphs</p>
<dt><code>tred</code></p>
<dd>transitive reduction filter for directed graphs</p>
<dt><code>dijkstra</code></p>
<dd>single-source distance filter</p>
<dt><code>bcomps</code></p>
<dd>biconnected components filter for graphs</p>
<dt><code>gvpr</code></p>
<dd>graph pattern scanning and processing language</p>
<dt><code>prune</code></p>
<dd>prune directed graphs </p>
</dl>
<h3>Other</h3>
<dl>
<dt><code>gxl2dot, dot2gxl</code></p>
<dd>GXL-DOT converters </p>
</dl>
<h2>Author</h2>
<p>This manual page was written by Cyril Brulebois &lt;cyril.brulebois [at] enst-bretagne.fr&gt; in november 2006, based on an initial documentation effort by Joachim Berdal Haga &lt;jbh [at] lupus.ig3.net&gt;. It can be distributed under the same terms as the graphviz package.</p>
