---
title: "gvmap(1)"
name: "gvmap"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gvmap/"
description: "gvmap – find clusters and create a geographical map highlighting clusters."
---

<h2 class="name">NAME</h2>
<p> gvmap &#8211; find clusters and create a geographical map highlighting clusters. </p>
<h2>SYNOPSIS</h2>
<p> <code>gvmap</code> [ <i>options</i> ] [ <code>-o</code> <i>outfile</i> ] [ <i>files</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>gvmap</code> takes as input a graph in DOT format, finds node clusters and produces a rendering of the graph as a geographic-style map, with clusters highlighted as countries, in xdot format. </p>
<p> In the input graph, each node must have position, width and height information (pos, width and height attributes, respectively) defined, and nodes must not overlap. </p>
<p> By default, <code>gvmap</code> will generate the clusters from the data. If desired, the input graph can specify cluster information by giving every node a <i>cluster</i> attribute whose value is a small positive integer. (It is works best if <i>cluster</i> values are all integers in the interval [1,K] for some K. Nodes sharing the same <i>cluster</i> attribute value will be put into the same cluster. <code>N.B.</code> For the <i>cluster</i> attribute to be used, all nodes must have a valid value. </p>
<p> If the <i>-D</i> flag is used, <code>gvmap</code> will use the top-level cluster subgraphs to determine the clustering. Any nodes not in such a cluster will be put into a single catch-all cluster. </p>
<p> If the input specifies the desired clustering as described above, it can also specify a desired coloring by having some node in each cluster provide a <i>clustercolor</i> attribute. <code>N.B.</code> Unless one specifies <i>-c0</i>, only the <i>clustercolor</i> of the last node in a cluster has an effect. In addition, unless one uses <i>-O</i>, <code>gvmap</code> may permute the given colors.</p>
<h2>OPTIONS</h2>
<p> The following options are supported:</p>
<dl>
<dt><code>-a</code><i> k</i></p>
<dd> The integer k specifies the average number of artificial points added along the bounding box of the labels. Such artificial points are added to avoid a country boundary cutting through the boundary box of the labels. Computing time is proportional to k; hence, for large graphs, a small value of k is suggested. If k = -1, a suitable value of k is automatically selected based on the graph size. By default k = -1.</p>
<dt><code>-b</code><i> v</i></p>
<dd> The real number v specifies the line width used to draw the polygon boundaries, with v &lt; 0 for no line. By default v = 0.</p>
<dt><code>-c</code><i> k</i></p>
<dd> The integer k specifies color scheme used to color the countries. By default k = 1.</p>
<dt>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Acceptable values are:</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;0 : no polygons<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;1 : pastel<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;2 : blue to yellow<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;3 : white to red<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;4 : light grey to red<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;5 : primary colors<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;6 : sequential single hue red<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;7 : sequential single hue lighter red<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;8 : light grey</p>
<dt><code>-c_opacity=</code><i>xy</i></p>
<dd> Specifies a two-character hexadecimal string specifying the opacity of the polygons.</p>
<dt><code>-C</code><i> d</i></p>
<dd> The integer d specifies the maximum number of clusters (countries) allowed. By default d = 0, which means that there is no limit.</p>
<dt><code>-d</code><i> d</i></p>
<dd> The integer d specifies the random seed used during color assignment optimization that maximize color difference between neighboring countries.</p>
<dt><code>-D</code></p>
<dd> If specified, the graph&#8217;s cluster subgraphs are used to specify the clustering.</p>
<dt><code>-e</code></p>
<dd> If specified, edges will be included in the final output.</p>
<dt><code>-g</code><i> c</i></p>
<dd> Specifies the bounding box color. If not specified, a bounding box is not drawn.</p>
<dt><code>-h</code><i> k</i></p>
<dd> The number of artificial points added to maintain a bridge between endpoints. By default, this is zero.</p>
<dt><code>-highlight=</code><i>k</i></p>
<dd> Only draw cluster <i>k</i>. By default, all clusters are drawn.</p>
<dt><code>-k</code></p>
<dd> If specified, increases the randomness of outer boundary.</p>
<dt><code>-l</code><i> s</i></p>
<dd> Use the string <i>s</i> as a label for the drawing.</p>
<dt><code>-m</code><i> v</i></p>
<dd> Generate a margin of <i>v</i> points around the drawing. By default, this is determined by <code>gvmap</code>.</p>
<dt><code>-O</code></p>
<dd> Do NOT do color assignment optimization that maximizes color differences between neighboring countries</p>
<dt><code>-o</code><i>&lt;file&gt;</i></p>
<dd> Put output in &lt;file&gt;. Default output is stdout</p>
<dt><code>-p</code><i> k</i></p>
<dd> Indicates what level of points should be shown. By default, no points are shown.</p>
<dt>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Acceptable values are:</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;0 : no points<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;1 : all points<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;2 : label points<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;3 : random/artificial points</p>
<dt><code>-Q</code></p>
<dd> Use modularity quality for clustering rather than the default modularity clustering.</p>
<dt><code>-r</code><i> k</i></p>
<dd> The number of random points k (integer) used to define sea and lake boundaries. If 0, auto assigned. By default v = 0</p>
<dt><code>-s</code><i> v</i></p>
<dd> The real number v specifies the depth of the sea and lake shores in points. If 0, auto assigned. By default v = 0.</p>
<dt><code>-t</code><i> n</i></p>
<dd> Make <i>n</i> attempts to improve cluster contiguity.</p>
<dt><code>-v</code></p>
<dd> Verbose mode.</p>
<dt><code>-z</code><i> c</i></p>
<dd> Specified the polygon line color. Default is black.</p>
<dt><code>-?</code></p>
<dd> Print usage and exit.</dl>
<h2>EXAMPLES</h2>
<p> Given a graph foo.gv, one way to generate a layout and highlight the clusters is to first select a layout engine with a suitable overlap removal method, then feed the output to gvmap, and finally render the map using specific graphics format. For example, the following pipeline creates a map with edges in semi-transparent light gray and nodes laid out using sfdp: </p>
<p> sfdp -Goverlap=prism foo.gv | gvmap -e | neato -n2 -Ecolor=#55555522 -Tpng &gt; foo.png </p>
<p> The shell script gvmap.sh provides a shorthand for such pipelines. For example, the above pipeline can be achieved using </p>
<p> gvmap.sh -Ae -Ecolor=#55555522 -Tpng foo.gv &gt; foo.png </p>
<h2>AUTHOR</h2>
<p> Yifan Hu &lt;yifanhu [at] yahoo.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-gvmap-sh/">gvmap.sh</a>(1), <a href="/docs/linux/man/1-sfdp/">sfdp</a>(1), <a href="/docs/linux/man/1-neato/">neato</a>(1), <a href="/docs/linux/man/1-gvpr/">gvpr</a>(1) </p>
<p> E. R. Gansner, Y. Hu, S. G. Kobourov, &quot;GMap: Visualizing graphs and clusters as maps,&quot; Proc. Pacific Vis. 2010, pp. 201-208. </p>
<h2>Index</h2>
