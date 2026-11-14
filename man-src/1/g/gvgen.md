---
title: "gvgen(1)"
name: "gvgen"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gvgen/"
description: "gvgen – generate graphs"
---

<h2 class="name">NAME</h2>
<p> gvgen &#8211; generate graphs </p>
<h2>SYNOPSIS</h2>
<p> <code>gvgen</code> [ <code>-dv?</code> ] [ <code>-i</code><i>n</i> ] [ <code>-c</code><i>n</i> ] [ <code>-C</code><i>x,y</i> ] [ <code>-g</code><i>[</i><code>f</code>]x,y ] [ <code>-G</code><i>[</i><code>f</code>]x,y ] [ <code>-h</code><i>n</i> ] [ <code>-k</code><i>n</i> ] [ <code>-b</code><i>x,y</i> ] [ <code>-B</code><i>x,y</i> ] [ <code>-m</code><i>n</i> ] [ <code>-M</code><i>x,y</i> ] [ <code>-p</code><i>n</i> ] [ <code>-r</code><i>x,y</i> ] [ <code>-R</code><i>x</i> ] [ <code>-s</code><i>n</i> ] [ <code>-S</code><i>n</i> ] [ <code>-S</code><i>n,d</i> ] [ <code>-t</code><i>n</i> ] [ <code>-t</code><i>d,n</i> ] [ <code>-T</code><i>x,y</i> ] [ <code>-T</code><i>x,y,u,v</i> ] [ <code>-w</code><i>n</i> ] [ <code>-n</code><i>prefix</i> ] [ <code>-N</code><i>name</i> ] [ <code>-o</code><i>outfile</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>gvgen</code> generates a variety of simple, regularly-structured abstract graphs.</p>
<h2>OPTIONS</h2>
<p> The following options are supported:</p>
<dl>
<dt><code>-c</code><i> n</i></p>
<dd> Generate a cycle with <i>n</i> vertices and edges.</p>
<dt><code>-C</code><i> x,y</i></p>
<dd> Generate an <i>x</i> by <i>y</i> cylinder. This will have <i>x*y</i> vertices and <i>2*x*y &#8211; y</i> edges.</p>
<dt><code>-g</code><i> [</i><code>f</code>]x,y</p>
<dd> Generate an <i>x</i> by <i>y</i> grid. If <code>f</code> is given, the grid is folded, with an edge attaching each pair of opposing corner vertices. This will have <i>x*y</i> vertices and <i>2*x*y &#8211; y &#8211; x</i> edges if unfolded and <i>2*x*y &#8211; y &#8211; x + 2</i> edges if folded.</p>
<dt><code>-G</code><i> [</i><code>f</code>]x,y</p>
<dd> Generate an <i>x</i> by <i>y</i> partial grid. If <code>f</code> is given, the grid is folded, with an edge attaching each pair of opposing corner vertices. This will have <i>x*y</i> vertices.</p>
<dt><code>-h</code><i> n</i></p>
<dd> Generate a hypercube of degree <i>n</i>. This will have <i>2^n</i> vertices and <i>n*2^(n-1)</i> edges.</p>
<dt><code>-k</code><i> n</i></p>
<dd> Generate a complete graph on <i>n</i> vertices with <i>n*(n-1)/2</i> edges.</p>
<dt><code>-b</code><i> x,y</i></p>
<dd> Generate a complete <i>x</i> by <i>y</i> bipartite graph. This will have <i>x+y</i> vertices and <i>x*y</i> edges.</p>
<dt><code>-B</code><i> x,y</i></p>
<dd> Generate an <i>x</i> by <i>y</i> ball, i.e., an <i>x</i> by <i>y</i> cylinder with two &quot;cap&quot; nodes closing the ends. This will have <i>x*y + 2</i> vertices and <i>2*x*y + y</i> edges.</p>
<dt><code>-m</code><i> n</i></p>
<dd> Generate a triangular mesh with <i>n</i> vertices on a side. This will have <i>(n+1)*n/2</i> vertices and <i>3*(n-1)*n/2</i> edges.</p>
<dt><code>-M</code><i> x,y</i></p>
<dd> Generate an x by y Moebius strip. This will have <i>x*y</i> vertices and <i>2*x*y &#8211; y</i> edges.</p>
<dt><code>-p</code><i> n</i></p>
<dd> Generate a path on <i>n</i> vertices. This will have <i>n-1</i> edges.</p>
<dt><code>-r</code><i> x,y</i></p>
<dd> Generate a random graph. The number of vertices will be the largest value of the form <i>2^n-1</i> less than or equal to <i>x</i>. Larger values of <i>y</i> increase the density of the graph.</p>
<dt><code>-R</code><i> x</i></p>
<dd> Generate a random rooted tree on <i>x</i> vertices.</p>
<dt><code>-s</code><i> n</i></p>
<dd> Generate a star on <i>n</i> vertices. This will have <i>n-1</i> edges.</p>
<dt><code>-S</code><i> n</i></p>
<dd> Generate a Sierpinski graph of order <i>n</i>. This will have <i>3*(3^(n-1) + 1)/2</i> vertices and <i>3^n</i> edges.</p>
<dt><code>-S</code><i> n,d</i></p>
<dd> Generate a <i>d</i>-dimensional Sierpinski graph of order <i>n</i>. At present, <i>d</i> must be 2 or 3. For d equal to 3, there will be <i>4*(4^(n-1) + 1)/2</i> vertices and <i>6 * 4^(n-1)</i> edges.</p>
<dt><code>-t</code><i> n</i></p>
<dd> Generate a binary tree of height <i>n</i>. This will have <i>2^n-1</i> vertices and <i>2^n-2</i> edges.</p>
<dt><code>-t</code><i> h,n</i></p>
<dd> Generate a n-ary tree of height <i>h</i>.</p>
<dt><code>-T</code><i> x,y</i></p>
<dd>
<dt><code>-T</code><i> x,y,u,v</i></p>
<dd> Generate an <i>x</i> by <i>y</i> torus. This will have <i>x*y</i> vertices and <i>2*x*y</i> edges. If <i>u</i> and <i>v</i> are given, they specify twists of that amount in the horizontal and vertical directions, respectively.</p>
<dt><code>-w</code><i> n</i></p>
<dd> Generate a path on <i>n</i> vertices. This will have <i>n-1</i> edges.</p>
<dt><code>-i</code><i> n</i></p>
<dd> Generate <i>n</i> graphs of the requested type. At present, only available if the <code>-R</code> flag is used.</p>
<dt><code>-n</code><i> prefix</i></p>
<dd> Normally, integers are used as node names. If <i>prefix</i> is specified, this will be prepended to the integer to create the name.</p>
<dt><code>-N</code><i> name</i></p>
<dd> Use <i>name</i> as the name of the graph. By default, the graph is anonymous.</p>
<dt><code>-o</code><i> outfile</i></p>
<dd> If specified, the generated graph is written into the file <i>outfile.</i> Otherwise, the graph is written to standard out.</p>
<dt><code>-d</code></p>
<dd> Make the generated graph directed.</p>
<dt><code>-v</code></p>
<dd> Verbose output.</p>
<dt><code>-?</code></p>
<dd> Print usage information.</dl>
<h2>EXIT STATUS</h2>
<p> <code>gvgen</code> exits with 0 on successful completion, and exits with 1 if given an ill-formed or incorrect flag, or if the specified output file could not be opened.</p>
<h2>AUTHOR</h2>
<p> Emden R. Gansner &lt;erg [at] research.att.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-gc/">gc</a>(1), <a href="/docs/linux/man/1-acyclic/">acyclic</a>(1), <a href="/docs/linux/man/1-gvpr/">gvpr</a>(1), <a href="/docs/linux/man/1-gvcolor/">gvcolor</a>(1), <a href="/docs/linux/man/1-ccomps/">ccomps</a>(1), <a href="/docs/linux/man/1-sccmap/">sccmap</a>(1), <a href="/docs/linux/man/1-tred/">tred</a>(1), <a href="/docs/linux/man/3-libgraph/">libgraph</a>(3) </p>
<h2>Index</h2>
