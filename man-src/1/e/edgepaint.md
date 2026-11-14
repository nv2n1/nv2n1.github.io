---
title: "edgepaint(1)"
name: "edgepaint"
section: "1"
letter: "e"
url: "/docs/linux/man/1-edgepaint/"
description: "edgepaint – edge coloring to disambiguate crossing edges"
---

<h2 class="name">NAME</h2>
<p> edgepaint &#8211; edge coloring to disambiguate crossing edges </p>
<h2>SYNOPSIS</h2>
<p> <code>[</code> <i>options</i> ] [ <code>-o</code> <i>outfile</i> ] [ <i>files</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>edgepaint</code> takes as input a graph in DOT format with node position information (the <i>pos</i> attribute) and colors the edges in a manner making it easier to tell them apart.</p>
<h2>OPTIONS</h2>
<p> The following options are supported:</p>
<dl>
<dt><code>-accuracy=</code><i>e</i></p>
<dd> accuracy with which to find the maximally different coloring for each node with regard to its neighbors. Default e = 0.01.</p>
<dt><code>-angle=</code><i>a</i></p>
<dd> color two edges differently if their incidence angle is less than <i>a</i> degrees. Default <i>a</i>=15.</p>
<dt><code>-random_seed=</code><i>s</i></p>
<dd> random seed to use. <i>s</i> must be an integer. If <i>s</i> is negative, we do |<i>s</i>| iterations with different seeds and pick the best.</p>
<dt><code>-lightness=</code><i>l1,l2j</i></p>
<dd> only applies for the &quot;lab&quot; color scheme: <i>l1</i> and <i>l2</i> must integers, with 0 &lt;= <i>l1</i> &lt;= <i>l2 &lt;=100. By default, we use &quot;0,70&quot;</p>
<dt></i><code>-share_endpoint</code></p>
<dd> if this option is specified, edges that shares an node are not considered in conflict if they are close to parallel but are on the opposite sides of the node (around 180 degree).</p>
<dt><code>-o</code><i> f</i></p>
<dd> write output to file f (default: stdout).</p>
<dt><code>-color_scheme=</code><i>c</i></p>
<dd> specifies the color scheme. This can be &quot;rgb&quot;, &quot;gray&quot;, &quot;lab&quot; (default); or a comma-separated list of RGB colors in hex (e.g., &quot;#ff0000,#aabbed,#eeffaa&quot;) representing a palette; or a string specifying a Brewer color scheme (e.g., &quot;accent7&quot;; see <a rel="nofollow" href="http://www.graphviz.org/content/color-names#brewer">http://www.graphviz.org/content/color-names#brewer</a>).</p>
<dt><code>-v </code></p>
<dd> turns on verbose mode.</p>
<dt><code>-?</code></p>
<dd> Print usage and exit. </p>
</dl>
<h2>BUGS</h2>
<p> At present, <code>edgepaint</code> does not handle graphs with loops or directed multiedges. So, a graph with edges <i>a -&gt; b</i> and <i>b -&gt; a</i> is acceptable, but not if it has edges <i>a -&gt; b</i> and <i>a -&gt; b</i> or <i>a &#8212; b</i> and <i>a &#8212; b</i>. Ports are ignored in this analysis, so having <i>a.x -&gt; b</i> and <i>a.y -&gt; b</i> is also not supported.</p>
<h2>AUTHOR</h2>
<p> Yifan Hu &lt;yifanhu [at] yahoo.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-gvmap/">gvmap</a>(1), <a href="/docs/linux/man/1-sfdp/">sfdp</a>(1), neato (1), <a href="/docs/linux/man/1-dot/">dot</a>(1) </p>
<h2>Index</h2>
