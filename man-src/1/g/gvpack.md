---
title: "gvpack(1)"
name: "gvpack"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gvpack/"
description: "gvpack – merge and pack disjoint graphs"
---

<h2 class="name">NAME</h2>
<p> gvpack &#8211; merge and pack disjoint graphs </p>
<h2>SYNOPSIS</h2>
<p> <code>gvpack</code> [ <code>-nguv?</code> ] [ <code>-m</code><i>margin</i> ] [ <code>-array</code><i>opts</i> ] [ <code>-o</code><i>outfile</i> ] [ <code>-s</code><i>graph_name</i> ] [ <code>-G</code><i>name</i><code>=</code>value ] [ <i>files</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>gvpack</code> reads in a stream of graphs, combines the graphs into a single layout, and produces a single graph serving as the union of the input graphs. The input graphs must be in dot format, and must have all necessary layout information. Acceptable input is produced by applying a Graphviz layout program, such as <code>dot</code> or <code>neato</code>, with no <code>-T</code> flag. </p>
<p> By default, the packing is done at the cluster level. Thus, parts of one graph will not intrude into any top-level clusters or overlap any nodes or edges of another. </p>
<p> The output of <code>gvpack</code> can be used to produce concrete output by applying <code>neato -s -n2</code> with the desired <code>-T</code> flag.</p>
<h2>OPTIONS</h2>
<p> The following options are supported:</p>
<dl>
<dt><code>-g</code></p>
<dd> Combines the graphs at the graph level. This uses more space, but prevents parts of one graph from occurring between parts of another.</p>
<dt><code>-array</code><i>[_flags][n]</i></p>
<dd> Combines the graphs at the graph level, placing them in an array. By default, the layout is done in row-major order. The number of columns used is roughly the square root of the number of graphs. If the optional integer <i>n</i> is supplied, this indicates the number of columns to use.</p>
<dt>
<dd> If optional flags are supplied, these consist of an underscore followed by any of the letters &quot;c&quot;, &quot;t&quot;, &quot;b&quot;, &quot;l&quot;, &quot;r&quot;, &quot;u&quot; or &quot;i&quot;. If &quot;c&quot; is supplied, the graphs are packed in column-major order, in which case a final integer specifies the number of rows. The flags &quot;t&quot;, &quot;b&quot;, &quot;l&quot;, &quot;r&quot; indicate that components are aligned along the top, bottom, left or right, respectively. By default, the insertion order is determined by sorting the graphs by size, largest to smallest. If the &quot;u&quot; flag is set, the graphs are sorted based on the non-negative integer <i>sortv</i> attribute attached to each graph. The &quot;i&quot; flag indicates that no sorting is done, with the graphs inserted in input order.</p>
<dt><code>-G</code><i>name</i><code>=</code>value</p>
<dd> Specifies attributes to be added to the resulting union graph. For example, this can be used to specify a graph label.</p>
<dt><code>-m</code><i>margin</i></p>
<dd> Packs the graphs allowing a margin of <i>output</i> points around the parts.</p>
<dt><code>-n</code></p>
<dd> Combines the graphs at the node level. Clusters are ignored in the packing.</p>
<dt><code>-o</code><i>output</i></p>
<dd> Prints output to the file <i>output</i>. If not given, <code>gvpack</code> uses stdout.</p>
<dt><code>-s</code><i>graph_name</i></p>
<dd> Use <i>graph_name</i> as the name of the root graph. By default, &quot;root&quot; is used.</p>
<dt><code>-u</code></p>
<dd> Don&#8217;t pack the graphs. Just combine them into a single graph.</p>
<dt><code>-v</code></p>
<dd> Verbose mode.</p>
<dt><code>-?</code></p>
<dd> Prints usage information and exit.</dl>
<h2>OPERANDS</h2>
<p> The following operand is supported:</p>
<dl>
<dt><i>files</i></p>
<dd> Names of files containing 1 or more graphs in dot format. If no <i>files</i> operand is specified, the standard input will be used.</dl>
<h2>RETURN CODES</h2>
<p> <code>gvpack</code> returns <code>0</code> if there were no problems, and non-zero otherwise.</p>
<h2>EXAMPLES</h2>
<p> ccomps -x abc.gv | dot | gvpack | neato -s -n2 -Tps This pipeline decomposes the graph in <i>abc.gv</i> into its connected components, lays out each using <code>dot</code>, packs them all together again, and produces the final drawing in PostScript. Of course, there is nothing to prevent one from using different layouts for each component.</p>
<h2>BUGS</h2>
<p> All the input graphs must be directed or undirected. </p>
<p> An input graph should not have a label, since this will be used in its layout. Since <code>gvpack</code> ignores root graph labels, resulting layout may contain some extra space. </p>
<p> <code>gvpack</code> unsets the bounding box attribute of all non-cluster subgraphs.</p>
<h2>AUTHORS</h2>
<p> Emden R. Gansner &lt;erg [at] research.att.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-gvpr/">gvpr</a>(1), <a href="/docs/linux/man/1-dot/">dot</a>(1), <a href="/docs/linux/man/1-neato/">neato</a>(1), <a href="/docs/linux/man/1-twopi/">twopi</a>(1), <a href="/docs/linux/man/1-ccomps/">ccomps</a>(1), <a href="/docs/linux/man/3-libpack/">libpack</a>(3) </p>
<h2>Index</h2>
