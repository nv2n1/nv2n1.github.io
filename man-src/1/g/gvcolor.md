---
title: "gvcolor(1)"
name: "gvcolor"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gvcolor/"
description: "gvcolor – flow colors through a ranked digraph"
---

<h2 class="name">NAME</h2>
<p> gvcolor &#8211; flow colors through a ranked digraph </p>
<h2>SYNOPSIS</h2>
<p> <code>gvcolor</code> [ <i>files </i> ]</p>
<h2>USAGE</h2>
<p> dot file.gv | gvcolor | dot -T<i>&lt;format&gt;</i></p>
<h2>DESCRIPTION</h2>
<p> <code>gvcolor</code> (previously known as <code>colorize)</code> is a filter that sets node colors from initial seed values. Colors flow along edges from tail to head, and are averaged (as HSB vectors) at nodes. <i>The graph must already have been processed by dot.</i> Appropriate choice of initial colors yields drawings in which node colors help to emphasize logical relationships between nodes, even when they are spread far apart in the layout. </p>
<p> Initial colors must be set externally, using the <code>color</code> attribute of a node. It is often effective to assign colors to a few key source or sink nodes, manually setting their colors by editing the graph file. Color names are as in <i><a href="/docs/linux/man/1-dot/">dot</a>(1)</i>: symbolic names or RGB triples. It is best to choose some easily-distinguished but related colors; not necessarily spaced evenly around the color wheel. For example, blue_green, green, and light_yellow looks better than red, green, blue. </p>
<p> Certain graph attributes control the <i>gvcolor</i> algorithm. <code>flow=back</code> reverses the flow of colors from heads to tails. <code>saturation=.1,.9</code> (or any two numbers between 0 and 1) adjusts the color saturation linearly from least to greatest rank. If <code>Defcolor</code> is set, this color value is applied to any node not otherwise colored.</p>
<h2>EXIT STATUS</h2>
<p> The following exit values are returned:</p>
<dl>
<dt><code>0</code></p>
<dd> Successful completion.</p>
<dt><code>1</code></p>
<dd> If nodes of the graph do not possess a &#8220;pos&#8221; attribute.</dl>
<h2>BUGS</h2>
<p> It would be nice to make the program work without relying on an initial pass through <code>dot</code>.</p>
<h2>AUTHORS</h2>
<p> Stephen C. North &lt;north [at] research.att.com&gt;<br />
 Emden R. Gansner &lt;erg [at] research.att.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-gc/">gc</a>(1), <a href="/docs/linux/man/1-dot/">dot</a>(1), <a href="/docs/linux/man/1-gvpr/">gvpr</a>(1), <a href="/docs/linux/man/1-ccomps/">ccomps</a>(1), <a href="/docs/linux/man/1-sccmap/">sccmap</a>(1), <a href="/docs/linux/man/1-tred/">tred</a>(1), <a href="/docs/linux/man/3-libgraph/">libgraph</a>(3) </p>
<h2>Index</h2>
