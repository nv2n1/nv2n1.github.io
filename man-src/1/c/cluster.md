---
title: "cluster(1)"
name: "cluster"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cluster/"
description: "cluster – find clusters in a graph and augment the graph with this information."
---

<h2 class="name">NAME</h2>
<p> cluster &#8211; find clusters in a graph and augment the graph with this information. </p>
<h2>SYNOPSIS</h2>
<p> <code>cluster</code> [<code>-v?</code>] [ <code>-C</code><i>k</i> ] [ <code>-c</code><i>k</i> ] [ <code>-o</code> <i>outfile</i> ] [ <i>files</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>cluster</code> takes as input a graph in DOT format, finds node clusters and augments the graph with this information. The clusters are specified by the &quot;cluster&quot; attribute attached to nodes; cluster values are non-negative integers. <code>cluster</code> attempts to maximize the modularity of the clustering. If the edge attribute &quot;weight&quot; is defined, this will be used in computing the clustering.</p>
<h2>OPTIONS</h2>
<p> The following options are supported:</p>
<dl>
<dt><code>-C</code><i>k</i></p>
<dd> specifies a targeted number of clusters that should be generated. The specified number <i>k</i> is only a suggestion and may not be realisable. If <i>k == 0</i>, the default, the number of clusters that approximately optimizes the modularity is returned.</p>
<dt><code>-c</code><i>k</i></p>
<dd> specifies clustering method. If <i>k == 0</i>, the default, modularity clustering will be used. If <i>k == 1</i> modularity quality will be used.</p>
<dt><code>-o</code><i>outfile</i></p>
<dd> Specifies that output should go into the file <i>outfile</i>. By default, <i>stdout</i> is used.</p>
<dt><code>-v</code></p>
<dd> Verbose mode.</dl>
<h2>EXAMPLES</h2>
<p> Applying <code>cluster</code> to the following graph, </p>
<pre><code>
graph
{
    1 --2 [weight = 10.] 2 --3 [weight = 1] 3 --4 [weight = 10.] 4 --5 [weight = 10] 5 --6 [weight = 10] 3 --6 [weight = 0.1] 4 --6 [weight = 10.]
}
</code></pre>
<p> gives </p>
<pre><code>
graph
{
    node[cluster = "-1"];
    1 [cluster = 1];
    2 [cluster = 1];
    3 [cluster = 2];
    4 [cluster = 2];
    5 [cluster = 2];
    6 [cluster = 2];
    1 --2 [weight = "10."];
    2 --3 [weight = 1];
    3 --4 [weight = "10."];
    4 --5 [weight = 10];
    5 --6 [weight = 10];
    3 --6 [weight = "0.1"];
    4 --6 [weight = "10."];
}
</code></pre>
<h2>AUTHOR</h2>
<p> Yifan Hu &lt;yifanhu [at] yahoo.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-gvmap/">gvmap</a>(1) </p>
<p> Blondel, V.D., Guillaume, J.L., Lambiotte, R., Lefebvre, E.: Fast unfolding of communities in large networks. Journal of Statistical Mechanics: Theory and Experiment (2008), P10008. </p>
<h2>Index</h2>
