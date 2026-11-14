---
title: "mm2gv(1)"
name: "mm2gv"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mm2gv/"
description: "mm2gv – Matrix Market-DOT converters"
---

<h2 class="name">NAME</h2>
<p> mm2gv &#8211; Matrix Market-DOT converters </p>
<h2>SYNOPSIS</h2>
<p> <code>mm2gv</code> [ <code>-cluv?</code> ] [ <code>-U</code><i>i</i> ] [ <code>-o</code><i>outfile</i> ] [ <i>file</i> ] </p>
<h2>DESCRIPTION</h2>
<p> <code>mm2gv</code> converts a sparse matrix of the Matrix Market format to a graph in the GV (formerly DOT) format. If the matrix <i>M</i> is not square, the graph is considered bipartite and the matrix is viewed as a bipartite graph adjacency matrix, with the rows and columns of the matrix specifying the two sets of vertices. Equivalently, the matrix is converted into a symmetric square matrix </p>
<table>
<tr VALIGN=top>
<td ALIGN=center>0</td>
<td ALIGN=center><i>M</i>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>$<i>M</i> sup <i>T</i>$</td>
<td ALIGN=center>0
</td>
</tr>
</table>
<p> a block matrix with square blocks of 0&#8217;s in the upper left and lower right, the upper right block being <i>M</i> and the lower left block being the transpose of <i>M</i>. This matrix is then viewed as the adjacency matrix of the graph. </p>
<p> For a square matrix, <code>mm2gv</code> uses it directly as an adjacency matrix if its pattern of non-zero entries is symmetric; otherwise, it will treat it as a bipartite graph as with the case of non-square matrices. This behavior can be modified by the <code>-U</code> flag.</p>
<h2>OPTIONS</h2>
<p> The following options are supported:</p>
<dl>
<dt><code>-c</code></p>
<dd> This flag causes <code>mm2gv</code> to assign colors to the edges. The matrix element is scaled to the range [0,1] depending on where it lies between the minimum and maximum set matrix values. This scaled value is used as the <i>&quot;wt&quot;</i> attribute of the corresponding edge. In addition, this scalar value is mapped to an RGB value, which is stored as the edge <i>&quot;color&quot;</i>.</p>
<dt><code>-l</code></p>
<dd> If set, <code>mm2gv</code> attaches a label to the graph indicating the base name of the input file, and the number of nodes and edges.</p>
<dt><code>-u</code></p>
<dd> If specified, the graph is assumed to be undirected. By default, the graph generated is directed.</p>
<dt><code>-v</code></p>
<dd> This flag causes <code>mm2gv</code> to store the matrix values as the <i>&quot;len&quot;</i> attribute of the corresponding edge.</p>
<dt><code>-U</code><i>bflag</i></p>
<dd> Specifies how square matrices are handled. If <i>bflag</i> is 0, a square matrix will always be treated as an adjacency matrix. If <i>bflag</i> is 1 (the default), a square matrix with a symmetric pattern of non-zero entries will be used as an adjacency matrix; otherwise, it will be used a bipartite graph. If <i>bflag</i> is 2, a symmetric matrix will be used as an adjacency matrix; otherwise, it will be used a bipartite graph. If <i>bflag</i> is 3, any input matrix will be treated like a bipartite graph.</p>
<dt><code>-o</code><i>outfile</i></p>
<dd> Prints output to the file <i>outfile</i>. If not given, <code>mm2gv</code> uses stdout.</p>
<dt></dl>
<h2>OPERANDS</h2>
<dd> The following operand is supported:</p>
<dl>
<dt><i>file</i></p>
<dd> Name of the file in MatrixMarket format. If no <i>file</i> operand is specified, the standard input will be used.</dl>
<h2>RETURN CODES</h2>
<p> Return <code>0</code> if there were no problems during conversion; and non-zero if any error occurred.</p>
<h2>AUTHORS</h2>
<p> Yifan Hu &lt;yifanhu [at] yahoo.com&gt;<br />
 Emden R. Gansner &lt;erg [at] graphviz.com&gt;</p>
<h2>ADDITIONAL INFO</h2>
<p> See <a rel="nofollow" href="http://math.nist.gov/MatrixMarket/">http://math.nist.gov/MatrixMarket/</a> for description of the format and <a rel="nofollow" href="http://www.cise.ufl.edu/research/sparse/matrices/">http://www.cise.ufl.edu/research/sparse/matrices/</a> for a large collection of sparse matrices in this format. </p>
<h2>Index</h2>
