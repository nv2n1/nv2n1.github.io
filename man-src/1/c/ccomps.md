---
title: "ccomps(1)"
name: "ccomps"
section: "1"
letter: "c"
url: "/docs/linux/man/1-ccomps/"
description: "ccomps – connected components filter for graphs"
---

<h2 class="name">NAME</h2>
<p> ccomps &#8211; connected components filter for graphs </p>
<h2>SYNOPSIS</h2>
<p> <code>ccomps</code> [ <code>-sxvenzC?</code> ] [ <code>-X</code><i>[#%]s[-f]</i> ] [ <code>-o</code><i>outfile</i> ] [ <i>files</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>ccomps</code> decomposes graphs into their connected components, printing the components to standard output.</p>
<h2>OPTIONS</h2>
<p> The following options are supported:</p>
<dl>
<dt><code>-e</code></p>
<dd> Do not induce edges in the connected components.</p>
<dt><code>-s</code></p>
<dd> No output graph is printed. The return value can be used to check if the graph is connected or not.</p>
<dt><code>-x</code></p>
<dd> Only the connected components are printed, as separate graphs.</p>
<dt><code>-v</code></p>
<dd> Counts of nodes, edges and connected components are printed.</p>
<dt><code>-z</code></p>
<dd> Sort components by size, with the largest first. This is only effective if either <code>-x</code> or <code>-X#</code> is present. Thus, <code>-zX#0</code> will cause the largest component to be printed.</p>
<dt><code>-C</code></p>
<dd> Use clusters in computing components in addition to normal edge connectivity. In essence, this gives the connected components of the derived graph in which nodes top-level clusters and nodes in the original graph. This maintains all subgraph structure within a component, even if a subgraph does not contain any nodes.</p>
<dt><code>-n</code></p>
<dd> Do not project subgraph structure. Normally, if <code>ccomps</code> produces components as graphs distinct from the input graph, it will define subgraphs which are projections of subgraphs of the input graph onto the component. (If the projection is empty, no subgraph is produced.) If this flag is set, the component contains only the relevant nodes and edges.</p>
<dt><code>-X</code><i> node_name</i></p>
<dd> Prints only the component containing the node <i>node_name</i>, if any.</p>
<dt><code>-X#</code><i> start</i></p>
<dd>
<dt><code>-X#</code><i> start-</i></p>
<dd>
<dt><code>-X#</code><i> start-last</i></p>
<dd> Prints only components in the given range of indices. In the first form, only the component whose index is <i>start</i>, if any, is printed. In the second form, each component whose index is at least <i>start</i> is printed. In the last form, only those components whose indices are in the range <code>[</code><i>Istart</i><code>,</code><i>last</i><code>]</code> are printed. Thus, the flag <code>-x</code> is equivalent to <code>-X#0-</code>.</p>
<dt><code>-X%</code><i> min</i></p>
<dd>
<dt><code>-X%</code><i> min-</i></p>
<dd>
<dt><code>-X%</code><i> min-max</i></p>
<dd> Prints only components in the given range of sizes. In the first form, only a component whose size is <i>min</i>, if any, is printed. In the second form, each component whose size is at least <i>min</i> is printed. In the last form, only those components whose sizes are in the range <code>[</code><i>Imin</i><code>,</code><i>max</i><code>]</code> are printed.</p>
<dt><code>-o</code><i> outfile</i></p>
<dd> If specified, each graph will be written to a different file with the names derived from <i>outfile</i>. In particular, if both <code>-o</code> and <code>-x</code> flags are used, then each connected component is written to a different file. If <i>outfile</i> does not have a suffix, the first file will have the name <i>outfile</i>; then next <i>outfile_1</i>, then next <i>outfile_2</i>, and so on. If <i>outfile</i> has a suffix, i.e., has the form <i>base.sfx</i>, then the files will be named <i>base.sfx</i>, <i>base_1.sfx</i>, <i>base_2.sfx</i>, etc.</dl>
<p> By default, each input graph is printed, with each connected component given as a subgraph whose name is a concatenation of the name of the input graph, the string &quot;_cc_&quot; and the number of the component.</p>
<h2>OPERANDS</h2>
<p> The following operand is supported:</p>
<dl>
<dt><i>files</i></p>
<dd> Names of files containing 1 or more graphs in dot format. If no <i>files</i> operand is specified, the standard input will be used.</dl>
<h2>RETURN CODES</h2>
<p> Unless used to extract a single connected component, <code>ccomps</code> returns <code>0</code> if all the input graphs are connected; and non-zero if any graph has multiple components, or any error occurred. If just extracting a single component, <code>ccomps</code> returns <code>0</code> on success and non-zero if an error occurred.</p>
<h2>BUGS</h2>
<p> It is possible, though unlikely, that the names used for connected components and their subgraphs may conflict with existing subgraph names.</p>
<h2>AUTHORS</h2>
<p> Stephen C. North &lt;north [at] research.att.com&gt;<br />
 Emden R. Gansner &lt;erg [at] research.att.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-gc/">gc</a>(1), <a href="/docs/linux/man/1-dot/">dot</a>(1), <a href="/docs/linux/man/1-gvpr/">gvpr</a>(1), <a href="/docs/linux/man/1-gvcolor/">gvcolor</a>(1), <a href="/docs/linux/man/1-acyclic/">acyclic</a>(1), <a href="/docs/linux/man/1-sccmap/">sccmap</a>(1), <a href="/docs/linux/man/1-tred/">tred</a>(1), <a href="/docs/linux/man/3-libgraph/">libgraph</a>(3) </p>
<h2>Index</h2>
