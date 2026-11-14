---
title: "gvmap-sh(1)"
name: "gvmap-sh"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gvmap-sh/"
description: "gvmap.sh – pipeline for running gvmap"
---

<p>gvmap.sh &#8211; pipeline for running gvmap </p>
<h2>Synopsis</h2>
<p><code>gvmap.sh</code> [<code>-vV?</code>] [ <i>options</i> ] [ <code>-o</code> <i>outfile</i> ] [ <i>files</i> ]</p>
<h2>Description</h2>
<p><code>gvmap.sh</code> takes as input a graph in DOT format, performs a layout, runs the output through gvmap and renders the output. At some point, it is hoped to integrate all of these tasks into gvmap.</p>
<h2>Options</h2>
<p>The following options are supported:</p>
<dl>
<dt><code>-a</code><i> k</i></p>
<dd>The integer k specifies the average number of artificial points added along the bounding box of the labels. Such artificial points are added to avoid a country boundary cutting through the boundary box of the labels. Computing time is proportional to k; hence, for large graphs, a small value of k is suggested. If k = -1, a suitable value of k is automatically selected based on the graph size. By default k = -1.</p>
<dt><code>-K</code><i> layout</i></p>
<dd>specifies which program should be use for the initial layout. By default, sfdp is run. Also by default, the layout is passed the flag -Goverlap=prism. This can be overridden using a -g flag.</p>
<dt><code>-T</code><i> format</i></p>
<dd>specifies the final output format. This works the same way as the -T flag for any Graphviz layout program.</p>
<dt><code>-N</code><i> attr=val</i></p>
<dd>specifies the setting of a default node attribute during the rendering phase. This works the same way as the -N flag for any Graphviz layout program.</p>
<dt><code>-G</code><i> attr=val</i></p>
<dd>specifies the setting of a graph attribute during the rendering phase. This works the same way as the -G flag for any Graphviz layout program.</p>
<dt><code>-E</code><i> attr=val</i></p>
<dd>specifies the setting of a default edge attribute during the rendering phase. This works the same way as the -E flag for any Graphviz layout program.</p>
<dt><code>-n</code><i> attr=val</i></p>
<dd>specifies the setting of a default node attribute during the layout phase. This works the same way as the -N flag for any Graphviz layout program.</p>
<dt><code>-g</code><i> attr=val</i></p>
<dd>specifies the setting of a graph attribute during the layout phase. This works the same way as the -G flag for any Graphviz layout program.</p>
<dt><code>-e</code><i> attr=val</i></p>
<dd>specifies the setting of a default edge attribute during the layout phase. This works the same way as the -E flag for any Graphviz layout program.</p>
<dt><code>-A</code><i> flag</i></p>
<dd>specifies a flag to be passed to gvmap. For example, gvmap.sh -Ae -As3 causes gvmap -e -s3 to be run.</p>
<dt><code>-v</code></p>
<dd>Set verbose mode.</p>
<dt><code>-V</code></p>
<dd>Print version information and exit.</p>
<dt><code>-?</code></p>
<dd>Print usage information and exit. </p>
</dl>
<h2>Examples</h2>
<p>The following invocation creates a map with edges in semi-transparent light gray and nodes laid out using sfdp: </p>
<p> gvmap.sh -Ae -Ecolor=#55555522 -Tpng foo.gv &gt; foo.png </p>
<p> It is equivalent to running the pipeline </p>
<p> sfdp -Goverlap=prism foo.gv | gvmap -e | neato -n2 -Ecolor=#55555522 -Tpng &gt; foo.png </p>
<h2>Author</h2>
<p>Emden R. Gansner &lt;erg [at] research.att.com&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-gvmap/">gvmap</a>(1), <a href="/docs/linux/man/1-sfdp/">sfdp</a>(1), <a href="/docs/linux/man/1-neato/">neato</a>(1), <a href="/docs/linux/man/1-gvpr/">gvpr</a>(1) </p>
<p> E. R. Gansner, Y. Hu, S. G. Kobourov, &quot;GMap: Visualizing graphs and clusters as maps,&quot; Proc. Pacific Vis. 2010, pp. 201-208.</p>
