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
<dt><code>dot</code></dt>
<dd>filter for hierarchical layouts of graphs</dd>
<dt><code>neato</code></dt>
<dd>filter for symmetric layouts of graphs</dd>
<dt><code>twopi</code></dt>
<dd>filter for radial layouts of graphs</dd>
<dt><code>circo</code></dt>
<dd>filter for circular layout of graphs</dd>
<dt><code>fdp</code></dt>
<dd>filter for symmetric layouts of graphs</dd></dl>
<p> All of the filters work with either directed or undirected graphs, though <code>dot</code> is typically used for directed graphs and <code>neato</code> for undirected graphs. Note also that <code>neato -n[2]</code> can be used to render layouts produced by the other filters.</p>
<h3>Graph drawing programs</h3>
<dl>
<dt><code>lefty</code></dt>
<dd>A Programmable Graphics Editor</dd>
<dt><code>lneato</code></dt>
<dd>lefty + neato</dd>
<dt><code>dotty</code></dt>
<dd>lefty + dot </dd>
</dl>
<h3>Graph layout enhancement</h3>
<dl>
<dt><code>gvcolor</code></dt>
<dd>flow colors through a ranked digraph</dd>
<dt><code>unflatten</code></dt>
<dd>adjust directed graphs to improve layout aspect ratio</dd>
<dt><code>gvpack</code></dt>
<dd>merge and pack disjoint graphs </dd>
</dl>
<h3>Graph information and transformation</h3>
<dl>
<dt><code>gc</code></dt>
<dd>count graph components</dd>
<dt><code>acyclic</code></dt>
<dd>make directed graph acyclic</dd>
<dt><code>nop</code></dt>
<dd>pretty-print graph file</dd>
<dt><code>ccomps</code></dt>
<dd>connected components filter for graphs</dd>
<dt><code>sccmap</code></dt>
<dd>extract strongly connected components of directed graphs</dd>
<dt><code>tred</code></dt>
<dd>transitive reduction filter for directed graphs</dd>
<dt><code>dijkstra</code></dt>
<dd>single-source distance filter</dd>
<dt><code>bcomps</code></dt>
<dd>biconnected components filter for graphs</dd>
<dt><code>gvpr</code></dt>
<dd>graph pattern scanning and processing language</dd>
<dt><code>prune</code></dt>
<dd>prune directed graphs </dd>
</dl>
<h3>Other</h3>
<dl>
<dt><code>gxl2dot, dot2gxl</code></dt>
<dd>GXL-DOT converters </dd>
</dl>
<h2>Author</h2>
<p>This manual page was written by Cyril Brulebois &lt;cyril.brulebois [at] enst-bretagne.fr&gt; in november 2006, based on an initial documentation effort by Joachim Berdal Haga &lt;jbh [at] lupus.ig3.net&gt;. It can be distributed under the same terms as the graphviz package.</p>
