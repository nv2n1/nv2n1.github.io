---
title: "prune(1)"
name: "prune"
section: "1"
letter: "p"
url: "/docs/linux/man/1-prune/"
description: "prune – Prune directed graphs"
---

<h2 class="name">NAME</h2>
<p> prune &#8211; Prune directed graphs </p>
<h2>SYNOPSIS</h2>
<p> <code>prune</code> [ <code>-n</code><i> node</i> ] [ <code>-N</code><i> attrspec</i> ] [ <code>-v</code> ] [ <code>&#8211;</code>(<code>h</code>|<code>?</code>) ] [ <i>files &#8230;</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>prune</code> reads directed graphs in the same format used by <code><a href="/docs/linux/man/1-dot/">dot</a>(1)</code> and removes subgraphs rooted at nodes specified on the command line via options. These nodes themselves will not be removed, but can be given attributes so that they can be easily located by a graph stream editor such as <code><a href="/docs/linux/man/1-gvpr/">gvpr</a>(1).</code> <code>prune</code> correctly handles cycles, loops and multi-edges. </p>
<p> Both options can appear multiple times on the command line. All subgraphs rooted at the respective nodes given will then be processed. If a node does not exist, <code>prune</code> will skip it and print a warning message to stderr. If multiple attributes are given, they will be applied to all nodes that have been processed. <code>prune</code> writes the result to the stdout.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-n</code><i> name</i></p>
<dd> Specifies name of node to prune.</p>
<dt><code>-N</code><i> attrspec</i></p>
<dd> Specifies attribute that will be set (or changed if it exists) for any pruned node. <i>attrspec</i> is a string of the form <i>attr</i>=<i>value.</i></p>
<dt><code>-v</code></p>
<dd> Verbose output.</p>
<dt><code>-h</code> -?</p>
<dd> Prints the usage and exits.</dl>
<h2>EXAMPLES</h2>
<p> An input graph <i>test.gv</i> of the form </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>digraph DG {</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt> A -&gt; B;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt> A -&gt; C;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt> B -&gt; D;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt> B -&gt; E;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>}</p>
<p> , processed by the command </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>prune -n B test.gv</p>
<p> would produce the following output (the actual code might be formatted in a slightly different way). </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>digraph DG {</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt> A -&gt; B;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt> A -&gt; C;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>}</p>
<p> Another input graph <i>test.gv</i> of the form </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>digraph DG {</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt> A -&gt; B;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt> A -&gt; C;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt> B -&gt; D;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt> B -&gt; E;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt> C -&gt; E;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>}</p>
<p> (note the additional edge from <i>C</i> to <i>E</i> ), processed by the command </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>prune -n B -N color=red test.gv</p>
<p> results in </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>digraph DG {</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt> B [color=red];</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt> A -&gt; B;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt> A -&gt; C;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt> C -&gt; E;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>}</p>
<p> Node <i>E</i> has not been removed since its second parent <i>C</i> is not being pruned. </p>
<h2>EXIT STATUS</h2>
<p> <code>prune</code> returns 0 on successful completion. It returns 1 if an error occurs.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dot/">dot</a></code>(1), <code><a href="/docs/linux/man/1-gvpr/">gvpr</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> Marcus Harnisch &lt;marcus.harnisch [at] gmx.net&gt; </p>
<h2>Index</h2>
