---
title: "dijkstra(1)"
name: "dijkstra"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dijkstra/"
description: "dijkstra – single-source distance filter for Graphviz"
---

<h2 class="name">NAME</h2>
<p> dijkstra &#8211; single-source distance filter for Graphviz </p>
<h2>SYNOPSIS</h2>
<p> <code>dijkstra</code> [ <code>-adp?</code> ] [ <i>sourcenode file</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>dijkstra</code> reads a stream of Graphviz formatted graphs and for each computes the distance of every node from <i>sourcenode.</i> Edge length is given in the <i>len</i> attribute, and the default is 1. The <i>dist</i> attribute of every node is set to its distance from <i>sourcenode.</i> If the <code>-p</code> flag is used, the <i>prev</i> attribute of each node reachable from <i>sourcenode</i> is set to the name of the previous node on a shortest path. The graph attribute <i>maxdist</i> is set to the maximum <i>dist</i> of all nodes in the graph. </p>
<p> If the <code>-d</code> flag is used, the graph is treated as directed and only forward edges are used. </p>
<p> By default, if the graph is disconnected, the <i>dist</i> attribute of nodes unreachable from <i>sourcenode</i> are left untouched, and <i>maxdist</i> is set to the maximum of any previous value and the largest distance recorded in this run. On the other hand, if the <code>-a</code> flag is used, the <i>dist</i> attribute of an unreachable node is assigned a very large value, and <i>maxdist</i> records the maximum distance found in the component containing <i>sourcenode.</i> </p>
<p> Any number of <i>sourcenode file</i> pairs may be given. If the last <i>file </i> is missing, <code>stdin</code> is used. All output is written to <code>stdout</code>. </p>
<p> In a typical application, <i>dist</i> and <i>maxdist</i> can drive a downstream calculation of color or some other attribute.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-gvpr/">gvpr</a>(1), <a href="/docs/linux/man/1-gvcolor/">gvcolor</a>(1), <a href="/docs/linux/man/3-libgraph/">libgraph</a>(3) </p>
<h2>Index</h2>
