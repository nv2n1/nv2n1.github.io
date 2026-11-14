---
title: "gvpr(1)"
name: "gvpr"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gvpr/"
description: "gvpr – graph pattern scanning and processing language"
---

<h2 class="name">NAME</h2>
<p> gvpr &#8211; graph pattern scanning and processing language </p>
<h2>SYNOPSIS</h2>
<p> <code>gvpr</code> [<code>-icnqV?</code>] [ <code>-o</code> <i>outfile</i> ] [ <code>-a</code> <i>args</i> ] [ <i>&#8216;prog&#8217;</i> | <code>-f</code> <i>progfile</i> ] [ <i>files </i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>gvpr</code> (previously known as <code>gpr</code>) is a graph stream editor inspired by <code>awk</code>. It copies input graphs to its output, possibly transforming their structure and attributes, creating new graphs, or printing arbitrary information. The graph model is that provided by <i><a href="/docs/linux/man/3-libcgraph/">libcgraph</a></i>(3). In particular, <code>gvpr</code> reads and writes graphs using the dot language. </p>
<p> Basically, <code>gvpr</code> traverses each input graph, denoted by <code>$G</code>, visiting each node and edge, matching it with the predicate-action rules supplied in the input program. The rules are evaluated in order. For each predicate evaluating to true, the corresponding action is performed. During the traversal, the current node or edge being visited is denoted by <code>$</code>. </p>
<p> For each input graph, there is a target subgraph, denoted by <code>$T</code>, initially empty and used to accumulate chosen entities, and an output graph, <code>$O</code>, used for final processing and then written to output. By default, the output graph is the target graph. The output graph can be set in the program or, in a limited sense, on the command line.</p>
<h2>OPTIONS</h2>
<p> The following options are supported:</p>
<dl>
<dt><code>-a</code><i> args</i></p>
<dd> The string <i>args</i> is split into whitespace-separated tokens, with the individual tokens available as strings in the <code>gvpr</code> program as <code>ARGV[</code><i>0</i>],&#8230;,ARGV[ARGC-1]. Whitespace characters within single or double quoted substrings, or preceded by a backslash, are ignored as separators. In general, a backslash character turns off any special meaning of the following character. Note that the tokens derived from multiple <code>-a</code> flags are concatenated.</p>
<dt><code>-c</code></p>
<dd> Use the source graph as the output graph.</p>
<dt><code>-i</code></p>
<dd> Derive the node-induced subgraph extension of the output graph in the context of its root graph.</p>
<dt><code>-o</code><i> outfile</i></p>
<dd> Causes the output stream to be written to the specified file; by default, output is written to <code>stdout</code>.</p>
<dt><code>-f</code><i> progfile</i></p>
<dd> Use the contents of the specified file as the program to execute on the input. If <i>progfile</i> contains a slash character, the name is taken as the pathname of the file. Otherwise, <code>gvpr</code> will use the directories specified in the environment variable <code>GVPRPATH</code> to look for the file. If <code>-f</code> is not given, <code>gvpr</code> will use the first non-option argument as the program.</p>
<dt><code>-q</code></p>
<dd> Turns off warning messages.</p>
<dt><code>-n</code></p>
<dd> Turns off graph read-ahead. By default, the variable <code>$NG</code> is set to the next graph to be processed. This requires a read of the next graph before processing the current graph, which may block if the next graph is only generated in response to some action pertaining to the processing of the current graph.</p>
<dt><code>-V</code></p>
<dd> Causes the program to print version information and exit.</p>
<dt><code>-?</code></p>
<dd> Causes the program to print usage information and exit.</dl>
<h2>OPERANDS</h2>
<p> The following operand is supported:</p>
<dl>
<dt><i>files</i></p>
<dd> Names of files containing 1 or more graphs in the dot language. If no <code>-f</code> option is given, the first name is removed from the list and used as the input program. If the list of files is empty, <code>stdin</code> will be used.</dl>
<h2>PROGRAMS</h2>
<p> A <code>gvpr</code> program consists of a list of predicate-action clauses, having one of the forms:</p>
<dl>
<dt>
<dd> <code>BEGIN { </code><i>action</i><code> }</code></p>
<dt>
<dd> <code>BEG_G { </code><i>action</i><code> }</code></p>
<dt>
<dd> <code>N [ </code><i>predicate</i><code> ] { </code><i>action</i><code> }</code></p>
<dt>
<dd> <code>E [ </code><i>predicate</i><code> ] { </code><i>action</i><code> }</code></p>
<dt>
<dd> <code>END_G { </code><i>action</i><code> }</code></p>
<dt>
<dd> <code>END { </code><i>action</i><code> }</code></dl>
<p> A program can contain at most one of each of the <code>BEGIN</code>, <code>END_G</code> and <code>END</code> clauses. There can be any number of <code>BEG_G</code>, <code>N</code> and <code>E</code> statements, the first applied to graphs, the second to nodes, the third to edges. These are separated into blocks, a block consisting of an optional <code>BEG_G</code> statement and all <code>N</code> and <code>E</code> statements up to the next <code>BEG_G</code> statement, if any. The top-level semantics of a <code>gvpr</code> program are: </p>
<dl>
<dt>
<dd>
<pre><code>
Evaluate the BEGIN clause, if any.For each input graph G
{
    For each block
    {
        Set G as the current graph and current object.Evaluate the BEG_G clause, if any.For each node and edge in G
        {
            Set the node or edge as the current object.Evaluate the N or E clauses, as appropriate.
        }
    }
    Set G as the current object.Evaluate the END_G clause, if any.
}
Evaluate the END clause, if any.
</code></pre>
</dl>
<p> The actions of the <code>BEGIN</code>, <code>BEG_G</code>, <code>END_G</code> and <code>END</code> clauses are performed when the clauses are evaluated. For <code>N</code> or <code>E</code> clauses, either the predicate or action may be omitted. If there is no predicate with an action, the action is performed on every node or edge, as appropriate. If there is no action and the predicate evaluates to true, the associated node or edge is added to the target graph. </p>
<p> The blocks are evaluated in the order in which they occur. Within a block, the <code>N</code> clauses (<code>E</code> clauses, respectively) are evaluated in the order in which the occur. Note, though, that within a block, <code>N</code> or <code>E</code> clauses may be interlaced, depending on the traversal order. </p>
<p> Predicates and actions are sequences of statements in the C dialect supported by the <i><a href="/docs/linux/man/3-expr/">expr</a></i>(3) library. The only difference between predicates and actions is that the former must have a type that may interpreted as either true or false. Here the usual C convention is followed, in which a non-zero value is considered true. This would include non-empty strings and non-empty references to nodes, edges, etc. However, if a string can be converted to an integer, this value is used. </p>
<p> In addition to the usual C base types (<code>void</code>, <code>int</code>, <code>char</code>, <code>float</code>, <code>long</code>, <code>unsigned</code> and <code>double</code>), <code>gvpr</code> provides <code>string</code> as a synonym for <code>char*</code>, and the graph-based types <code>node_t</code>, <code>edge_t</code>, <code>graph_t</code> and <code>obj_t</code>. The <code>obj_t</code> type can be viewed as a supertype of the other 3 concrete types; the correct base type is maintained dynamically. Besides these base types, the only other supported type expressions are (associative) arrays. </p>
<p> Constants follow C syntax, but strings may be quoted with either <code>&quot;&#8230;&quot;</code> or <code>&#8216;&#8230;&#8217;</code>. <code>gvpr</code> accepts C++ comments as well as cpp-type comments. For the latter, if a line begins with a &#8216;#&#8217; character, the rest of the line is ignored. </p>
<p> A statement can be a declaration of a function, a variable or an array, or an executable statement. For declarations, there is a single scope. Array declarations have the form: </p>
<dl>
<dt>
<dd>
<pre>
<i> type array </i><code>[</code> type0 <code>]</code>
</pre>
</dl>
<p> where <i> type0 </i> is optional. If it is supplied, the parser will enforce that all array subscripts have the specified type. If it is not supplied, objects of all types can be used as subscripts. As in C, variables and arrays must be declared. In particular, an undeclared variable will be interpreted as the name of an attribute of a node, edge or graph, depending on the context. </p>
<p> Executable statements can be one of the following:</p>
<dl>
<dt>
<dd>
<table>
<tr VALIGN=top>
<td><code>{</code> [<i> statement &#8230; </i>] <code>}</code></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><i>expression</i></td>
<td>// commonly<i> var </i><code>=</code> expression
</td>
</tr>
<tr VALIGN=top>
<td><code>if(</code><i> expression </i>)<i> statement </i>[ <code>else</code><i> statement </i>]</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>for(</code><i> expression </i>;<i> expression </i>;<i> expression </i>)<i> statement</i></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>for(</code><i> array </i>[<i> var </i>])<i> statement</i></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>forr(</code><i> array </i>[<i> var </i>])<i> statement</i></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>while(</code><i> expression </i>)<i> statement</i></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>switch(</code><i> expression </i>)<i> case statements</i></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>break [</code><i> expression </i>]</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>continue [</code><i> expression </i>]</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>return [</code><i> expression </i>]</td>
<td>
</td>
</tr>
</table>
</dl>
<p> <font SIZE="-1">Items in brackets are optional.</font> </p>
<p> In the second form of the <code>for</code> statement and the <code>forr</code> statement, the variable <i>var</i> is set to each value used as an index in the specified array and then the associated <i>statement</i> is evaluated. For numeric and string indices, the indices are returned in increasing (decreasing) numeric or lexicographic order for <code>for</code> (<code>forr</code>, respectively). This can be used for sorting. </p>
<p> Function definitions can only appear in the <code>BEGIN</code> clause. </p>
<p> Expressions include the usual C expressions. String comparisons using <code>==</code> and <code>!=</code> treat the right hand operand as a pattern for the purpose of regular expression matching. Patterns use <i><a href="/docs/linux/man/1-ksh/">ksh</a></i>(1) file match pattern syntax. (For simple string equality, use the <code>strcmp</code> function. </p>
<p> <code>gvpr</code> will attempt to use an expression as a string or numeric value as appropriate. Both C-like casts and function templates will cause conversions to be performed, if possible. </p>
<p> Expressions of graphical type (i.e., <code>graph_t, node_t, edge_t, obj_t</code>) may be followed by a field reference in the form of <code>.</code><i>name</i>. The resulting value is the value of the attribute named <i>name</i> of the given object. In addition, in certain contexts an undeclared, unmodified identifier is taken to be an attribute name. Specifically, such identifiers denote attributes of the current node or edge, respectively, in <code>N</code> and <code>E</code> clauses, and the current graph in <code>BEG_G</code> and <code>END_G</code> clauses. </p>
<p> As usual in the <i><a href="/docs/linux/man/3-libcgraph/">libcgraph</a></i>(3) model, attributes are string-valued. In addition, <code>gvpr</code> supports certain pseudo-attributes of graph objects, not necessarily string-valued. These reflect intrinsic properties of the graph objects and cannot be set by the user.</p>
<dl>
<dt><code>head</code> : <code>node_t</code></p>
<dd> the head of an edge.</p>
<dt><code>tail</code> : <code>node_t</code></p>
<dd> the tail of an edge.</p>
<dt><code>name</code> : <code>string</code></p>
<dd> the name of an edge, node or graph. The name of an edge has the form &quot;<i>&lt;tail-name&gt;&lt;edge-op&gt;&lt;head-name&gt;</i><code>[</code><i>&lt;key&gt;</i><code>]</code>&quot;, where <i>&lt;edge-op&gt;</i> is &quot;<code>-&gt;</code>&quot; or &quot;<code>&#8212;</code>&quot; depending on whether the graph is directed or not. The bracket part <code>[</code><i>&lt;key&gt;</i><code>]</code> only appears if the edge has a non-trivial key.</p>
<dt><code>indegree</code> : <code>int</code></p>
<dd> the indegree of a node.</p>
<dt><code>outdegree</code> : <code>int</code></p>
<dd> the outdegree of a node.</p>
<dt><code>degree</code> : <code>int</code></p>
<dd> the degree of a node.</p>
<dt><code>X</code> : <code>double</code></p>
<dd> the X coordinate of a node. (Assumes the node has a <i>pos</i> attribute.)</p>
<dt><code>Y</code> : <code>double</code></p>
<dd> the Y coordinate of a node. (Assumes the node has a <i>pos</i> attribute.)</p>
<dt><code>root</code> : <code>graph_t</code></p>
<dd> the root graph of an object. The root of a root graph is itself.</p>
<dt><code>parent</code> : <code>graph_t</code></p>
<dd> the parent graph of a subgraph. The parent of a root graph is <code>NULL</code></p>
<dt><code>n_edges</code> : <code>int</code></p>
<dd> the number of edges in the graph</p>
<dt><code>n_nodes</code> : <code>int</code></p>
<dd> the number of nodes in the graph</p>
<dt><code>directed</code> : <code>int</code></p>
<dd> true (non-zero) if the graph is directed</p>
<dt><code>strict</code> : <code>int</code></p>
<dd> true (non-zero) if the graph is strict</dl>
<h2>BUILT-IN FUNCTIONS</h2>
<p> The following functions are built into <code>gvpr</code>. Those functions returning references to graph objects return <code>NULL</code> in case of failure.</p>
<h3>Graphs and subgraph</h3>
<dl>
<dt><code>graph</code>(<i>s</i> : <code>string</code>, <i>t</i> : <code>string</code>) : <code>graph_t</code></p>
<dd> creates a graph whose name is <i>s</i> and whose type is specified by the string <i>t</i>. Ignoring case, the characters <code>U, D, S, N</code> have the interpretation undirected, directed, strict, and non-strict, respectively. If <i>t</i> is empty, a directed, non-strict graph is generated.</p>
<dt><code>subg</code>(<i>g</i> : <code>graph_t</code>, <i>s</i> : <code>string</code>) : <code>graph_t</code></p>
<dd> creates a subgraph in graph <i>g</i> with name <i>s</i>. If the subgraph already exists, it is returned.</p>
<dt><code>isSubg</code>(<i>g</i> : <code>graph_t</code>, <i>s</i> : <code>string</code>) : <code>graph_t</code></p>
<dd> returns the subgraph in graph <i>g</i> with name <i>s</i>, if it exists, or <code>NULL</code> otherwise.</p>
<dt><code>fstsubg</code>(<i>g</i> : <code>graph_t</code>) : <code>graph_t</code></p>
<dd> returns the first subgraph in graph <i>g</i>, or <code>NULL</code> if none exists.</p>
<dt><code>nxtsubg</code>(<i>sg</i> : <code>graph_t</code>) : <code>graph_t</code></p>
<dd> returns the next subgraph after <i>sg</i>, or <code>NULL</code>.</p>
<dt><code>isDirect</code>(<i>g</i> : <code>graph_t</code>) : <code>int</code></p>
<dd> returns true if and only if <i>g</i> is directed.</p>
<dt><code>isStrict</code>(<i>g</i> : <code>graph_t</code>) : <code>int</code></p>
<dd> returns true if and only if <i>g</i> is strict.</p>
<dt><code>nNodes</code>(<i>g</i> : <code>graph_t</code>) : <code>int</code></p>
<dd> returns the number of nodes in <i>g</i>.</p>
<dt><code>nEdges</code>(<i>g</i> : <code>graph_t</code>) : <code>int</code></p>
<dd> returns the number of edges in <i>g</i>.</dl>
<h3>Nodes</h3>
<dl>
<dt><code>node</code>(<i>sg</i> : <code>graph_t</code>, <i>s</i> : <code>string</code>) : <code>node_t</code></p>
<dd> creates a node in graph <i>g</i> of name <i>s</i>. If such a node already exists, it is returned.</p>
<dt><code>subnode</code>(<i>sg</i> : <code>graph_t</code>, <i>n</i> : <code>node_t</code>) : <code>node_t</code></p>
<dd> inserts the node <i>n</i> into the subgraph <i>g</i>. Returns the node.</p>
<dt><code>fstnode</code>(<i>g</i> : <code>graph_t</code>) : <code>node_t</code></p>
<dd> returns the first node in graph <i>g</i>, or <code>NULL</code> if none exists.</p>
<dt><code>nxtnode</code>(<i>n</i> : <code>node_t</code>) : <code>node_t</code></p>
<dd> returns the next node after <i>n</i> in the root graph, or <code>NULL</code>.</p>
<dt><code>nxtnode_sg</code>(<i>sg</i> : <code>graph_t</code>, <i>n</i> : <code>node_t</code>) : <code>node_t</code></p>
<dd> returns the next node after <i>n</i> in <i>sg</i>, or <code>NULL</code>.</p>
<dt><code>isNode</code>(<i>sg</i> : <code>graph_t</code>, <i>s</i> : <code>string</code>) : <code>node_t</code></p>
<dd> looks for a node in (sub)graph <i>sg</i> of name <i>s</i>. If such a node exists, it is returned. Otherwise, <code>NULL</code> is returned.</p>
<dt><code>isSubnode</code>(<i>sg</i> : <code>graph_t</code>, <i>n</i> : <code>node_t</code>) : <code>int</code></p>
<dd> returns non-zero if node <i>n</i> is in (sub)graph <i>sg</i>, or zero otherwise.</p>
<dt><code>indegreeOf</code>(<i>sg</i> : <code>graph_t</code>, <i>n</i> : <code>node_t</code>) : <code>int</code></p>
<dd> returns the indegree of node <i>n</i> in (sub)graph <i>sg</i>.</p>
<dt><code>outdegreeOf</code>(<i>sg</i> : <code>graph_t</code>, <i>n</i> : <code>node_t</code>) : <code>int</code></p>
<dd> returns the outdegree of node <i>n</i> in (sub)graph <i>sg</i>.</p>
<dt><code>degreeOf</code>(<i>sg</i> : <code>graph_t</code>, <i>n</i> : <code>node_t</code>) : <code>int</code></p>
<dd> returns the degree of node <i>n</i> in (sub)graph <i>sg</i>.</dl>
<h3>Edges</h3>
<dl>
<dt><code>edge</code>(<i>t</i> : <code>node_t</code>, <i>h</i> : <code>node_t</code>, <i>s</i> : <code>string</code>) : <code>edge_t</code></p>
<dd> creates an edge with tail node <i>t</i>, head node <i>h</i> and name <i>s</i> in the root graph. If the graph is undirected, the distinction between head and tail nodes is unimportant. If such an edge already exists, it is returned.</p>
<dt><code>edge_sg</code>(<i>sg</i> : <code>graph_t</code>, <i>t</i> : <code>node_t</code>, <i>h</i> : <code>node_t</code>, <i>s</i> : <code>string</code>) : <code>edge_t</code></p>
<dd> creates an edge with tail node <i>t</i>, head node <i>h</i> and name <i>s</i> in (sub)graph <i>sg</i> (and all parent graphs). If the graph is undirected, the distinction between head and tail nodes is unimportant. If such an edge already exists, it is returned.</p>
<dt><code>subedge</code>(<i>g</i> : <code>graph_t</code>, <i>e</i> : <code>edge_t</code>) : <code>edge_t</code></p>
<dd> inserts the edge <i>e</i> into the subgraph <i>g</i>. Returns the edge.</p>
<dt><code>isEdge</code>(<i>t</i> : <code>node_t</code>, <i>h</i> : <code>node_t</code>, <i>s</i> : <code>string</code>) : <code>edge_t</code></p>
<dd> looks for an edge with tail node <i>t</i>, head node <i>h</i> and name <i>s</i>. If the graph is undirected, the distinction between head and tail nodes is unimportant. If such an edge exists, it is returned. Otherwise, <code>NULL</code> is returned.</p>
<dt><code>isEdge_sg</code>(<i>sg</i> : <code>graph_t</code>, <i>t</i> : <code>node_t</code>, <i>h</i> : <code>node_t</code>, <i>s</i> : <code>string</code>) : <code>edge_t</code></p>
<dd> looks for an edge with tail node <i>t</i>, head node <i>h</i> and name <i>s</i> in (sub)graph <i>sg</i>. If the graph is undirected, the distinction between head and tail nodes is unimportant. If such an edge exists, it is returned. Otherwise, <code>NULL</code> is returned.</p>
<dt><code>isSubedge</code>(<i>g</i> : <code>graph_t</code>, <i>e</i> : <code>edge_t</code>) : <code>int</code></p>
<dd> returns non-zero if edge <i>e</i> is in (sub)graph <i>sg</i>, or zero otherwise.</p>
<dt><code>fstout</code>(<i>n</i> : <code>node_t</code>) : <code>edge_t</code></p>
<dd> returns the first outedge of node <i>n</i> in the root graph.</p>
<dt><code>fstout_sg</code>(<i>sg</i> : <code>graph_t</code>, <i>n</i> : <code>node_t</code>) : <code>edge_t</code></p>
<dd> returns the first outedge of node <i>n</i> in (sub)graph <i>sg</i>.</p>
<dt><code>nxtout</code>(<i>e</i> : <code>edge_t</code>) : <code>edge_t</code></p>
<dd> returns the next outedge after <i>e</i> in the root graph.</p>
<dt><code>nxtout_sg</code>(<i>sg</i> : <code>graph_t</code>, <i>e</i> : <code>edge_t</code>) : <code>edge_t</code></p>
<dd> returns the next outedge after <i>e</i> in graph <i>sg</i>.</p>
<dt><code>fstin</code>(<i>n</i> : <code>node_t</code>) : <code>edge_t</code></p>
<dd> returns the first inedge of node <i>n</i> in the root graph.</p>
<dt><code>fstin_sg</code>(<i>sg</i> : <code>graph_t</code>, <i>n</i> : <code>node_t</code>) : <code>edge_t</code></p>
<dd> returns the first inedge of node <i>n</i> in graph <i>sg</i>.</p>
<dt><code>nxtin</code>(<i>e</i> : <code>edge_t</code>) : <code>edge_t</code></p>
<dd> returns the next inedge after <i>e</i> in the root graph.</p>
<dt><code>nxtin_sg</code>(<i>sg</i> : <code>graph_t</code>, <i>e</i> : <code>edge_t</code>) : <code>edge_t</code></p>
<dd> returns the next inedge after <i>e</i> in graph <i>sg</i>.</p>
<dt><code>fstedge</code>(<i>n</i> : <code>node_t</code>) : <code>edge_t</code></p>
<dd> returns the first edge of node <i>n</i> in the root graph.</p>
<dt><code>fstedge_sg</code>(<i>sg</i> : <code>graph_t</code>, <i>n</i> : <code>node_t</code>) : <code>edge_t</code></p>
<dd> returns the first edge of node <i>n</i> in graph <i>sg</i>.</p>
<dt><code>nxtedge</code>(<i>e</i> : <code>edge_t</code>, <code>node_t</code>) : <code>edge_t</code></p>
<dd> returns the next edge after <i>e</i> in the root graph.</p>
<dt><code>nxtedge_sg</code>(<i>sg</i> : <code>graph_t</code>, <i>e</i> : <code>edge_t</code>, <code>node_t</code>) : <code>edge_t</code></p>
<dd> returns the next edge after <i>e</i> in the graph <i>sg</i>.</p>
<dt><code>opp</code>(<i>e</i> : <code>edge_t</code>, <code>node_t</code>) : <code>node_t</code></p>
<dd> returns the node on the edge <i>e</i> not equal to <i>n</i>. Returns NULL if <i>n</i> is not a node of <i>e</i>. This can be useful when using <code>fstedge</code> and <code>nxtedge</code> to enumerate the neighbors of <i>n</i>.</dl>
<h3>Graph I/O</h3>
<dl>
<dt><code>write</code>(<i>g</i> : <code>graph_t</code>) : <code>void</code></p>
<dd> prints <i>g</i> in dot format onto the output stream.</p>
<dt><code>writeG</code>(<i>g</i> : <code>graph_t</code>, <i>fname</i> : <code>string</code>) : <code>void</code></p>
<dd> prints <i>g</i> in dot format into the file <i>fname</i>.</p>
<dt><code>fwriteG</code>(<i>g</i> : <code>graph_t</code>, <i>fd</i> : <code>int</code>) : <code>void</code></p>
<dd> prints <i>g</i> in dot format onto the open stream denoted by the integer <i>fd</i>.</p>
<dt><code>readG</code>(<i>fname</i> : <code>string</code>) : <code>graph_t</code></p>
<dd> returns a graph read from the file <i>fname</i>. The graph should be in dot format. If no graph can be read, <code>NULL</code> is returned.</p>
<dt><code>freadG</code>(<i>fd</i> : <code>int</code>) : <code>graph_t</code></p>
<dd> returns the next graph read from the open stream <i>fd</i>. Returns <code>NULL</code> at end of file.</dl>
<h3>Graph miscellany</h3>
<dl>
<dt><code>delete</code>(<i>g</i> : <code>graph_t</code>, <i>x</i> : <code>obj_t</code>) : <code>void</code></p>
<dd> deletes object <i>x</i> from graph <i>g</i>. If <i>g</i> is <code>NULL</code>, the function uses the root graph of <i>x</i>. If <i>x</i> is a graph or subgraph, it is closed unless <i>x</i> is locked.</p>
<dt><code>isIn</code>(<i>g</i> : <code>graph_t</code>, <i>x</i> : <code>obj_t</code>) : <code>int</code></p>
<dd> returns true if <i>x</i> is in subgraph <i>g</i>.</p>
<dt><code>cloneG</code>(<i>g</i> : <code>graph_t</code>, <i>s</i> : <code>string</code>) : <code>graph_t</code></p>
<dd> creates a clone of graph <i>g</i> with name of <i>s</i>. If <i>s</i> is &quot;&quot;, the created graph has the same name as <i>g</i>.</p>
<dt><code>clone</code>(<i>g</i> : <code>graph_t</code>, <i>x</i> : <code>obj_t</code>) : <code>obj_t</code></p>
<dd> creates a clone of object <i>x</i> in graph <i>g</i>. In particular, the new object has the same name/value attributes and structure as the original object. If an object with the same key as <i>x</i> already exists, its attributes are overlaid by those of <i>x</i> and the object is returned. If an edge is cloned, both endpoints are implicitly cloned. If a graph is cloned, all nodes, edges and subgraphs are implicitly cloned. If <i>x</i> is a graph, <i>g</i> may be <code>NULL</code>, in which case the cloned object will be a new root graph. In this case, the call is equivalent to <code>cloneG(</code><i>x</i><code>,&quot;&quot;)</code>.</p>
<dt><code>copy</code>(<i>g</i> : <code>graph_t</code>, <i>x</i> : <code>obj_t</code>) : <code>obj_t</code></p>
<dd> creates a copy of object <i>x</i> in graph <i>g</i>, where the new object has the same name/value attributes as the original object. If an object with the same key as <i>x</i> already exists, its attributes are overlaid by those of <i>x</i> and the object is returned. Note that this is a shallow copy. If <i>x</i> is a graph, none of its nodes, edges or subgraphs are copied into the new graph. If <i>x</i> is an edge, the endpoints are created if necessary, but they are not cloned. If <i>x</i> is a graph, <i>g</i> may be <code>NULL</code>, in which case the cloned object will be a new root graph.</p>
<dt><code>copyA</code>(<i>src</i> : <code>obj_t</code>, <i>tgt</i> : <code>obj_t</code>) : <code>int</code></p>
<dd> copies the attributes of object <i>src</i> to object <i>tgt</i>, overwriting any attribute values <i>tgt</i> may initially have.</p>
<dt><code>induce</code>(<i>g</i> : <code>graph_t</code>) : <code>void</code></p>
<dd> extends <i>g</i> to its node-induced subgraph extension in its root graph.</p>
<dt><code>hasAttr</code>(<i>src</i> : <code>obj_t</code>, <i>name</i> : <code>string</code>) : <code>int</code></p>
<dd> returns non-zero if object <i>src</i> has an attribute whose name is <i>name</i>. It returns 0 otherwise.</p>
<dt><code>isAttr</code>(<i>g</i> : <code>graph_t</code>, <i>kind</i> : <code>string</code>, <i>name</i> : <code>string</code>) : <code>int</code></p>
<dd> returns non-zero if an attribute <i>name</i> has been defined in <i>g</i> for objects of the given <i>kind</i>. For nodes, edges, and graphs, <i>kind</i> should be &quot;N&quot;, &quot;E&quot;, and &quot;G&quot;, respectively. It returns 0 otherwise.</p>
<dt><code>aget</code>(<i>src</i> : <code>obj_t</code>, <i>name</i> : <code>string</code>) : <code>string</code></p>
<dd> returns the value of attribute <i>name</i> in object <i>src</i>. This is useful for those cases when <i>name</i> conflicts with one of the keywords such as &quot;head&quot; or &quot;root&quot;. If the attribute has not been declared in the graph, the function will initialize it with a default value of &quot;&quot;. To avoid this, one should use the <code>hasAttr</code> or <code>isAttr</code> function to check that the attribute exists.</p>
<dt><code>aset</code>(<i>src</i> : <code>obj_t</code>, <i>name</i> : <code>string</code>, <i>value</i> : <code>string</code>) : <code>int</code></p>
<dd> sets the value of attribute <i>name</i> in object <i>src</i> to <i>value</i>. Returns 0 on success, non-zero on failure. See <code>aget</code> above.</p>
<dt><code>getDflt</code>(<i>g</i> : <code>graph_t</code>, <i>kind</i> : <code>string</code>, <i>name</i> : <code>string</code>) : <code>string</code></p>
<dd> returns the default value of attribute <i>name</i> in objects in <i>g</i> of the given <i>kind</i>. For nodes, edges, and graphs, <i>kind</i> should be &quot;N&quot;, &quot;E&quot;, and &quot;G&quot;, respectively. If the attribute has not been declared in the graph, the function will initialize it with a default value of &quot;&quot;. To avoid this, one should use the <code>isAttr</code> function to check that the attribute exists.</p>
<dt><code>setDflt</code>(<i>g</i> : <code>graph_t</code>, <i>kind</i> : <code>string</code>, <i>name</i> : <code>string</code>, <i>value</i> : <code>string</code>) : <code>int</code></p>
<dd> sets the default value of attribute <i>name</i> to <i>value</i> in objects in <i>g</i> of the given <i>kind</i>. For nodes, edges, and graphs, <i>kind</i> should be &quot;N&quot;, &quot;E&quot;, and &quot;G&quot;, respectively. Returns 0 on success, non-zero on failure. See <code>getDflt</code> above.</p>
<dt><code>fstAttr</code>(<i>g</i> : <code>graph_t</code>, <i>kind</i> : <code>string</code>) : <code>string</code></p>
<dd> returns the name of the first attribute of objects in <i>g</i> of the given <i>kind</i>. For nodes, edges, and graphs, <i>kind</i> should be &quot;N&quot;, &quot;E&quot;, and &quot;G&quot;, respectively. If there are no attributes, the string &quot;&quot; is returned.</p>
<dt><code>nxtAttr</code>(<i>g</i> : <code>graph_t</code>, <i>kind</i> : <code>string</code>, <i>name</i> : <code>string</code>) : <code>string</code></p>
<dd> returns the name of the next attribute of objects in <i>g</i> of the given <i>kind</i> after the attribute <i>name</i>. The argument <i>name</i> must be the name of an existing attribute; it will typically be the return value of an previous call to <code>fstAttr</code> or <code>nxtAttr</code>. For nodes, edges, and graphs, <i>kind</i> should be &quot;N&quot;, &quot;E&quot;, and &quot;G&quot;, respectively. If there are no attributes left, the string &quot;&quot; is returned.</p>
<dt><code>compOf</code>(<i>g</i> : <code>graph_t</code>, <i>n</i> : <code>node_t</code>) : <code>graph_t</code></p>
<dd> returns the connected component of the graph <i>g</i> containing node <i>n</i>, as a subgraph of <i>g</i>. The subgraph only contains the nodes. One can use <i>induce</i> to add the edges. The function fails and returns <code>NULL</code> if <i>n</i> is not in <i>g</i>. Connectivity is based on the underlying undirected graph of <i>g</i>.</p>
<dt><code>kindOf</code>(<i>obj</i> : <code>obj_t</code>) : <code>string</code></p>
<dd> returns an indication of the type of <i>obj</i>. For nodes, edges, and graphs, it returns &quot;N&quot;, &quot;E&quot;, and &quot;G&quot;, respectively.</p>
<dt><code>lock</code>(<i>g</i> : <code>graph_t</code>, <i>v</i> : <code>int</code>) : <code>int</code></p>
<dd> implements graph locking on root graphs. If the integer <i>v</i> is positive, the graph is set so that future calls to <code>delete</code> have no immediate effect. If <i>v</i> is zero, the graph is unlocked. If there has been a call to delete the graph while it was locked, the graph is closed. If <i>v</i> is negative, nothing is done. In all cases, the previous lock value is returned.</dl>
<h3>Strings</h3>
<dl>
<dt><code>sprintf</code>(<i>fmt</i> : <code>string</code>, <i>&#8230;</i>) : <code>string</code></p>
<dd> returns the string resulting from formatting the values of the expressions occurring after <i>fmt</i> according to the <i><a href="/docs/linux/man/3-printf/">printf</a></i>(3) format <i>fmt</i></p>
<dt><code>gsub</code>(<i>str</i> : <code>string</code>, <i>pat</i> : <code>string</code>) : <code>string</code></p>
<dd>
<dt><code>gsub</code>(<i>str</i> : <code>string</code>, <i>pat</i> : <code>string</code>, <i>repl</i> : <code>string</code>) : <code>string</code></p>
<dd> returns <i>str</i> with all substrings matching <i>pat</i> deleted or replaced by <i>repl</i>, respectively.</p>
<dt><code>sub</code>(<i>str</i> : <code>string</code>, <i>pat</i> : <code>string</code>) : <code>string</code></p>
<dd>
<dt><code>sub</code>(<i>str</i> : <code>string</code>, <i>pat</i> : <code>string</code>, <i>repl</i> : <code>string</code>) : <code>string</code></p>
<dd> returns <i>str</i> with the leftmost substring matching <i>pat</i> deleted or replaced by <i>repl</i>, respectively. The characters &#8216;^&#8217; and &#8216;$&#8217; may be used at the beginning and end, respectively, of <i>pat</i> to anchor the pattern to the beginning or end of <i>str</i>.</p>
<dt><code>substr</code>(<i>str</i> : <code>string</code>, <i>idx</i> : <code>int</code>) : <code>string</code></p>
<dd>
<dt><code>substr</code>(<i>str</i> : <code>string</code>, <i>idx</i> : <code>int</code>, <i>len</i> : <code>int</code>) : <code>string</code></p>
<dd> returns the substring of <i>str</i> starting at position <i>idx</i> to the end of the string or of length <i>len</i>, respectively. Indexing starts at 0. If <i>idx</i> is negative or <i>idx</i> is greater than the length of <i>str</i>, a fatal error occurs. Similarly, in the second case, if <i>len</i> is negative or <i>idx</i> + <i>len</i> is greater than the length of <i>str</i>, a fatal error occurs.</p>
<dt><code>strcmp</code>(<i>s1</i> : <code>string</code>, <i>s2</i> : <code>string</code>) : <code>int</code></p>
<dd> provides the standard C function <i><a href="/docs/linux/man/3-strcmp/">strcmp</a></i>(3).</p>
<dt><code>length</code>(<i>s</i> : <code>string</code>) : <code>int</code></p>
<dd> returns the length of string <i>s</i>.</p>
<dt><code>index</code>(<i>s</i> : <code>string</code>, <i>t</i> : <code>string</code>) : <code>int</code></p>
<dd>
<dt><code>rindex</code>(<i>s</i> : <code>string</code>, <i>t</i> : <code>string</code>) : <code>int</code></p>
<dd> returns the index of the character in string <i>s</i> where the leftmost (rightmost) copy of string <i>t</i> can be found, or -1 if <i>t</i> is not a substring of <i>s</i>.</p>
<dt><code>match</code>(<i>s</i> : <code>string</code>, <i>p</i> : <code>string</code>) : <code>int</code></p>
<dd> returns the index of the character in string <i>s</i> where the leftmost match of pattern <i>p</i> can be found, or -1 if no substring of <i>s</i> matches <i>p</i>.</p>
<dt><code>toupper</code>(<i>s</i> : <code>string</code>) : <code>string</code></p>
<dd> returns a version of <i>s</i> with the alphabetic characters converted to upper-case.</p>
<dt><code>tolower</code>(<i>s</i> : <code>string</code>) : <code>string</code></p>
<dd> returns a version of <i>s</i> with the alphabetic characters converted to lower-case.</p>
<dt><code>canon</code>(<i>s</i> : <code>string</code>) : <code>string</code></p>
<dd> returns a version of <i>s</i> appropriate to be used as an identifier in a dot file.</p>
<dt><code>html</code>(<i>g</i> : <code>graph_t</code>, <i>s</i> : <code>string</code>) : <code>string</code></p>
<dd> returns a &#8220;magic&#8221; version of <i>s</i> as an HTML string. This will typically be used to attach an HTML-like label to a graph object. Note that the returned string lives in <i>g</i>. In particular, it will be freed when <i>g</i> is closed, and to act as an HTML string, it has to be used with an object of <i>g</i>. In addition, note that the angle bracket quotes should not be part of <i>s</i>. These will be added if <i>g</i> is written in concrete DOT format.</p>
<dt><code>ishtml</code>(<i>s</i> : <code>string</code>) : <code>int</code></p>
<dd> returns non-zero if and only if <i>s</i> is an HTML string.</p>
<dt><code>xOf</code>(<i>s</i> : <code>string</code>) : <code>string</code></p>
<dd> returns the string &quot;<i>x</i>&quot; if <i>s</i> has the form &quot;<i>x</i>,<i>y</i>&quot;, where both <i>x</i> and <i>y</i> are numeric.</p>
<dt><code>yOf</code>(<i>s</i> : <code>string</code>) : <code>string</code></p>
<dd> returns the string &quot;<i>y</i>&quot; if <i>s</i> has the form &quot;<i>x</i>,<i>y</i>&quot;, where both <i>x</i> and <i>y</i> are numeric.</p>
<dt><code>llOf</code>(<i>s</i> : <code>string</code>) : <code>string</code></p>
<dd> returns the string &quot;<i>llx</i>,<i>lly</i>&quot; if <i>s</i> has the form &quot;<i>llx</i>,<i>lly</i>,<i>urx</i>,<i>ury</i>&quot;, where all of <i>llx</i>, <i>lly</i>, <i>urx</i>, and <i>ury</i> are numeric.</p>
<dt><code>urOf(</code><i>s</i><code>)</code></p>
<dd> <code>urOf</code>(<i>s</i> : <code>string</code>) : <code>string</code> returns the string &quot;<i>urx</i>,<i>ury</i>&quot; if <i>s</i> has the form &quot;<i>llx</i>,<i>lly</i>,<i>urx</i>,<i>ury</i>&quot;, where all of <i>llx</i>, <i>lly</i>, <i>urx</i>, and <i>ury</i> are numeric.</p>
<dt><code>sscanf</code>(<i>s</i> : <code>string</code>, <i>fmt</i> : <code>string</code>, <i>&#8230;</i>) : <code>int</code></p>
<dd> scans the string <i>s</i>, extracting values according to the <i><a href="/docs/linux/man/3-sscanf/">sscanf</a></i>(3) format <i>fmt</i>. The values are stored in the addresses following <i>fmt</i>, addresses having the form <code>&amp;</code><i>v</i>, where <i>v</i> is some declared variable of the correct type. Returns the number of items successfully scanned.</p>
<dt><code>split</code>(<i>s</i> : <code>string</code>, <i>arr</i> : <code>array</code>, <i>seps</i> : <code>string</code>) : <code>int</code></p>
<dd>
<dt><code>split</code>(<i>s</i> : <code>string</code>, <i>arr</i> : <code>array</code>) : <code>int</code></p>
<dd>
<dt><code>tokens</code>(<i>s</i> : <code>string</code>, <i>arr</i> : <code>array</code>, <i>seps</i> : <code>string</code>) : <code>int</code></p>
<dd>
<dt><code>tokens</code>(<i>s</i> : <code>string</code>, <i>arr</i> : <code>array</code>) : <code>int</code></p>
<dd> The <code>split</code> function breaks the string <i>s</i> into fields, while the <code>tokens</code> function breaks the string into tokens. A field consists of all non-separator characters between two separator characters or the beginning or end of the string. Thus, a field may be the empty string. A token is a maximal, non-empty substring not containing a separator character. The separator characters are those given in the <i>seps</i> argument. If <i>seps</i> is not provided, the default value is &quot; 	
&quot;. The functions return the number of fields or tokens. </p>
<p> The fields and tokens are stored in the argument array. The array must be <code>string</code>-valued and have <code>int</code> as its index type. The entries are indexed by consecutive integers, starting at 0. Any values already stored in the array will be either overwritten, or still be present after the function returns.</dl>
<h3>I/O</h3>
<dl>
<dt><code>print</code>(<i>&#8230;</i>) : <code>void</code></p>
<dd> <code>print(</code><i> expr</i><code>,</code><i> &#8230;</i><code> )</code> prints a string representation of each argument in turn onto <code>stdout</code>, followed by a newline.</p>
<dt><code>printf</code>(<i>fmt</i> : <code>string</code>, <i>&#8230;</i>) : <code>int</code></p>
<dd>
<dt><code>printf</code>(<i>fd</i> : <code>int</code>, <i>fmt</i> : <code>string</code>, <i>&#8230;</i>) : <code>int</code></p>
<dd> prints the string resulting from formatting the values of the expressions following <i>fmt</i> according to the <i><a href="/docs/linux/man/3-printf/">printf</a></i>(3) format <i>fmt</i>. Returns 0 on success. By default, it prints on <code>stdout</code>. If the optional integer <i>fd</i> is given, output is written on the open stream associated with <i>fd</i>.</p>
<dt><code>scanf</code>(<i>fmt</i> : <code>string</code>, <i>&#8230;</i>) : <code>int</code></p>
<dd>
<dt><code>scanf</code>(<i>fd</i> : <code>int</code>, <i>fmt</i> : <code>string</code>, <i>&#8230;</i>) : <code>int</code></p>
<dd> scans in values from an input stream according to the <i><a href="/docs/linux/man/3-scanf/">scanf</a></i>(3) format <i>fmt</i>. The values are stored in the addresses following <i>fmt</i>, addresses having the form <code>&amp;</code><i>v</i>, where <i>v</i> is some declared variable of the correct type. By default, it reads from <code>stdin</code>. If the optional integer <i>fd</i> is given, input is read from the open stream associated with <i>fd</i>. Returns the number of items successfully scanned.</p>
<dt><code>openF</code>(<i>s</i> : <code>string</code>, <i>t</i> : <code>string</code>) : <code>int</code></p>
<dd> opens the file <i>s</i> as an I/O stream. The string argument <i>t</i> specifies how the file is opened. The arguments are the same as for the C function <i><a href="/docs/linux/man/3-fopen/">fopen</a></i>(3). It returns an integer denoting the stream, or -1 on error. </p>
<p> As usual, streams 0, 1 and 2 are already open as <code>stdin</code>, <code>stdout</code>, and <code>stderr</code>, respectively. Since <code>gvpr</code> may use <code>stdin</code> to read the input graphs, the user should avoid using this stream.</p>
<dt><code>closeF</code>(<i>fd</i> : <code>int</code>) : <code>int</code></p>
<dd> closes the open stream denoted by the integer <i>fd</i>. Streams 0, 1 and 2 cannot be closed. Returns 0 on success.</p>
<dt><code>readL</code>(<i>fd</i> : <code>int</code>) : <code>string</code></p>
<dd> returns the next line read from the input stream <i>fd</i>. It returns the empty string &quot;&quot; on end of file. Note that the newline character is left in the returned string.</dl>
<h3>Math</h3>
<dl>
<dt><code>exp</code>(<i>d</i> : <code>double</code>) : <code>double</code></p>
<dd> returns e to the <i>d</i>th power.</p>
<dt><code>log</code>(<i>d</i> : <code>double</code>) : <code>double</code></p>
<dd> returns the natural log of <i>d</i>.</p>
<dt><code>sqrt</code>(<i>d</i> : <code>double</code>) : <code>double</code></p>
<dd> returns the square root of the double <i>d</i>.</p>
<dt><code>pow</code>(<i>d</i> : <code>double</code>, <i>x</i> : <code>double</code>) : <code>double</code></p>
<dd> returns <i>d</i> raised to the <i>x</i>th power.</p>
<dt><code>cos</code>(<i>d</i> : <code>double</code>) : <code>double</code></p>
<dd> returns the cosine of <i>d</i>.</p>
<dt><code>sin</code>(<i>d</i> : <code>double</code>) : <code>double</code></p>
<dd> returns the sine of <i>d</i>.</p>
<dt><code>atan2</code>(<i>y</i> : <code>double</code>, <i>x</i> : <code>double</code>) : <code>double</code></p>
<dd> returns the arctangent of <i>y/x</i> in the range -pi to pi.</p>
<dt><code>MIN</code>(<i>y</i> : <code>double</code>, <i>x</i> : <code>double</code>) : <code>double</code></p>
<dd> returns the minimum of <i>y</i> and <i>x</i>.</p>
<dt><code>MAX</code>(<i>y</i> : <code>double</code>, <i>x</i> : <code>double</code>) : <code>double</code></p>
<dd> returns the maximum of <i>y</i> and <i>x</i>.</dl>
<h3>Associative Arrays</h3>
<dl>
<dt><code>#</code> <i>arr</i> : <code>int</code></p>
<dd> returns the number of elements in the array <i>arr</i>.</p>
<dt><i>idx</i> <code>in</code> <i>arr</i> : <code>int</code></p>
<dd> returns 1 if a value has been set for index <i>idx</i> in the array <i>arr</i>. It returns 0 otherwise.</p>
<dt><code>unset</code>(<i>v</i> : <code>array</code>, <i>idx</i>) : <code>int</code></p>
<dd> removes the item indexed by <i>idx</i>. It returns 1 if the item existed, 0 otherwise.</p>
<dt><code>unset</code>(<i>v</i> : <code>array</code>) : <code>void</code></p>
<dd> re-initializes the array.</dl>
<h3>Miscellaneous</h3>
<dl>
<dt><code>exit</code>(<i>v</i> : <code>int</code>) : <code>void</code></p>
<dd> causes <code>gvpr</code> to exit with the exit code <i>v</i>.</p>
<dt><code>system</code>(<i>cmd</i> : <code>string</code>) : <code>int</code></p>
<dd> provides the standard C function <i><a href="/docs/linux/man/3-system/">system</a></i>(3). It executes <i>cmd</i> in the user&#8217;s shell environment, and returns the exit status of the shell.</p>
<dt><code>rand</code>() : <code>double</code></p>
<dd> returns a pseudo-random double between 0 and 1.</p>
<dt><code>srand</code>() : <code>int</code></p>
<dd>
<dt><code>srand</code>(<i>v</i> : <code>int</code>) : <code>int</code></p>
<dd> sets a seed for the random number generator. The optional argument gives the seed; if it is omitted, the current time is used. The previous seed value is returned. <code>srand</code> should be called before any calls to <code>rand</code>.</p>
<dt><code>colorx</code>(<i>color</i> : <code>string</code>, <i>fmt</i> : <code>string</code>) : <code>string</code></p>
<dd> translates a color from one format to another. The <i>color</i> argument should be a color in one of the recognized string representations. The <i>fmt</i> value should be one of &quot;RGB&quot;, &quot;RGBA&quot;, &quot;HSV&quot;, or &quot;HSVA&quot;. An empty string is returned on error.</dl>
<h2>BUILT-IN VARIABLES</h2>
<p> <code>gvpr</code> provides certain special, built-in variables, whose values are set automatically by <code>gvpr</code> depending on the context. Except as noted, the user cannot modify their values.</p>
<dl>
<dt><code>$</code> : <code>obj_t</code></p>
<dd> denotes the current object (node, edge, graph) depending on the context. It is not available in <code>BEGIN</code> or <code>END</code> clauses.</p>
<dt><code>$F</code> : <code>string</code></p>
<dd> is the name of the current input file.</p>
<dt><code>$G</code> : <code>graph_t</code></p>
<dd> denotes the current graph being processed. It is not available in <code>BEGIN</code> or <code>END</code> clauses.</p>
<dt><code>$NG</code> : <code>graph_t</code></p>
<dd> denotes the next graph to be processed. If <code>$NG</code> is NULL, the current graph <code>$G</code> is the last graph. Note that if the input comes from stdin, the last graph cannot be determined until the input pipe is closed. It is not available in <code>BEGIN</code> or <code>END</code> clauses, or if the <code>-n</code> flag is used.</p>
<dt><code>$O</code> : <code>graph_t</code></p>
<dd> denotes the output graph. Before graph traversal, it is initialized to the target graph. After traversal and any <code>END_G</code> actions, if it refers to a non-empty graph, that graph is printed onto the output stream. It is only valid in <code>N</code>, <code>E</code> and <code>END_G</code> clauses. The output graph may be set by the user.</p>
<dt><code>$T</code> : <code>graph_t</code></p>
<dd> denotes the current target graph. It is a subgraph of <code>$G</code> and is available only in <code>N</code>, <code>E</code> and <code>END_G</code> clauses.</p>
<dt><code>$tgtname</code> : <code>string</code></p>
<dd> denotes the name of the target graph. By default, it is set to <code>&quot;gvpr_result&quot;</code>. If used multiple times during the execution of <code>gvpr</code>, the name will be appended with an integer. This variable may be set by the user.</p>
<dt><code>$tvroot</code> : <code>node_t</code></p>
<dd> indicates the starting node for a (directed or undirected) depth-first or breadth-first traversal of the graph (cf. <code>$tvtype</code> below). The default value is <code>NULL</code> for each input graph. After the traversal at the given root, if the value of <code>$tvroot</code> has changed, a new traversal will begin with the new value of <code>$tvroot</code>. Also, set <code>$tvnext</code> below.</p>
<dt><code>$tvnext</code> : <code>node_t</code></p>
<dd> indicates the next starting node for a (directed or undirected) depth-first or breadth-first traversal of the graph (cf. <code>$tvtype</code> below). If a traversal finishes and the <code>$tvroot</code> has not been reset but the <code>$tvnext</code> has been set but not used, this node will be used as the next choice for <code>$tvroot</code>. The default value is <code>NULL</code> for each input graph.</p>
<dt><code>$tvedge</code> : <code>edge_t</code></p>
<dd> For BFS and DFS traversals, this is set to the edge used to arrive at the current node or edge. At the beginning of a traversal, or for other traversal types, the value is <code>NULL</code>.</p>
<dt><code>$tvtype</code> : <code>tvtype_t</code></p>
<dd> indicates how <code>gvpr</code> traverses a graph. It can only take one of the constant values with the prefix &quot;TV_&quot; described below. <code>TV_flat</code> is the default.</p>
<dt>
<dd> In the underlying graph library <i><a href="/docs/linux/man/3-cgraph/">cgraph</a></i>(3), edges in undirected graphs are given an arbitrary direction. This is used for traversals, such as <code>TV_fwd</code>, requiring directed edges.</p>
<dt><code>ARGC</code> : <code>int</code></p>
<dd> denotes the number of arguments specified by the <code>-a</code> <i>args</i> command-line argument.</p>
<dt><code>ARGV</code> : <code>string array</code></p>
<dd> denotes the array of arguments specified by the <code>-a</code> <i>args</i> command-line argument. The <i>i</i>th argument is given by <code>ARGV[</code><i>i</i>].</dl>
<h2>BUILT-IN CONSTANTS</h2>
<p> There are several symbolic constants defined by <code>gvpr</code>.</p>
<dl>
<dt><code>NULL</code> : <i>obj_t</i></p>
<dd> a null object reference, equivalent to 0.</p>
<dt><code>TV_flat</code> : <i>tvtype_t</i></p>
<dd> a simple, flat traversal, with graph objects visited in seemingly arbitrary order.</p>
<dt><code>TV_ne</code> : <i>tvtype_t</i></p>
<dd> a traversal which first visits all of the nodes, then all of the edges.</p>
<dt><code>TV_en</code> : <i>tvtype_t</i></p>
<dd> a traversal which first visits all of the edges, then all of the nodes.</p>
<dt><code>TV_dfs</code> : <i>tvtype_t</i></p>
<dd>
<dt> <code>TV_postdfs</code> : <i>tvtype_t</i></p>
<dd>
<dt> <code>TV_prepostdfs</code> : <i>tvtype_t</i></p>
<dd>a traversal of the graph using a depth-first search on the underlying undirected graph. To do the traversal, <code>gvpr</code> will check the value of <code>$tvroot</code>. If this has the same value that it had previously (at the start, the previous value is initialized to <code>NULL</code>.), <code>gvpr</code> will simply look for some unvisited node and traverse its connected component. On the other hand, if <code>$tvroot</code> has changed, its connected component will be toured, assuming it has not been previously visited or, if <code>$tvroot</code> is <code>NULL</code>, the traversal will stop. Note that using <code>TV_dfs</code> and <code>$tvroot</code>, it is possible to create an infinite loop.</p>
<dt>
<dd> By default, the traversal is done in pre-order. That is, a node is visited before all of its unvisited edges. For <code>TV_postdfs</code>, all of a node&#8217;s unvisited edges are visited before the node. For <code>TV_prepostdfs</code>, a node is visited twice, before and after all of its unvisited edges.</p>
<dt><code>TV_fwd</code> : <i>tvtype_t</i></p>
<dd>
<dt> <code>TV_postfwd</code> : <i>tvtype_t</i></p>
<dd>
<dt> <code>TV_prepostfwd</code> : <i>tvtype_t</i></p>
<dd>A traversal of the graph using a depth-first search on the graph following only forward arcs. The choice of roots for the traversal is the same as described for <code>TV_dfs</code> above. The different order of visitation specified by <code>TV_fwd</code>, <code>TV_postfwd</code> and <code>TV_prepostfwd</code> are the same as those specified by the analogous traversals <code>TV_dfs</code>, <code>TV_postdfs</code> and <code>TV_prepostdfs</code>.</p>
<dt><code>TV_rev</code> : <i>tvtype_t</i></p>
<dd>
<dt> <code>TV_postrev</code> : <i>tvtype_t</i></p>
<dd>
<dt> <code>TV_prepostrev</code> : <i>tvtype_t</i></p>
<dd>A traversal of the graph using a depth-first search on the graph following only reverse arcs. The choice of roots for the traversal is the same as described for <code>TV_dfs</code> above. The different order of visitation specified by <code>TV_rev</code>, <code>TV_postrev</code> and <code>TV_prepostrev</code> are the same as those specified by the analogous traversals <code>TV_dfs</code>, <code>TV_postdfs</code> and <code>TV_prepostdfs</code>.</p>
<dt><code>TV_bfs</code> : <i>tvtype_t</i></p>
<dd> A traversal of the graph using a breadth-first search on the graph ignoring edge directions. See the item on <code>TV_dfs</code> above for the role of <code>$tvroot</code>.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd>
<pre>
<code>gvpr -i 'N[color==&quot;blue&quot;]' file.gv</code>
</pre>
</dl>
<p> Generate the node-induced subgraph of all nodes with color blue. </p>
<dl>
<dt>
<dd>
gvpr &#8211; c &#8216;N[color==&#8221;blue&#8221;]{color = &#8220;red&#8221;}&#8217; file.gv
</dl>
<p> Make all blue nodes red. </p>
<dl>
<dt>
<dd>
BEGIN<br />
{<br />
    int n, e;<br />
    int tot_n = 0;<br />
    int tot_e = 0;<br />
}<br />
BEG_G<br />
{<br />
    n = nNodes($G);<br />
    e = nEdges($G);<br />
    printf(&#8220;%d nodes %d edges %s
&#8221;, n, e, $G.name);<br />
    tot_n += n;<br />
    tot_e += e;<br />
}<br />
END<br />
{<br />
    printf(&#8220;%d nodes %d edges total
&#8221;, tot_n, tot_e)<br />
}
</dl>
<p> Version of the program <code>gc</code>. </p>
<dl>
<dt>
<dd>
<pre>
<code>gvpr -c &quot;&quot;</code>
</pre>
</dl>
<p> Equivalent to <code>nop</code>. </p>
<dl>
<dt>
<dd>
BEG_G<br />
{<br />
    graph_t g = graph(&#8220;merge&#8221;, &#8220;S&#8221;);<br />
}<br />
E<br />
{<br />
    node_t h = clone(g, $.head);<br />
    node_t t = clone(g, $.tail);<br />
    edge_t e = edge(t, h, &#8220;&#8221;);<br />
    e.weight = e.weight + 1;<br />
}<br />
END_G<br />
{<br />
    $O = g;<br />
}
</dl>
<p> Produces a strict version of the input graph, where the weight attribute of an edge indicates how many edges from the input graph the edge represents. </p>
<dl>
<dt>
<dd>
BEGIN<br />
{<br />
    node_t n;<br />
    int deg[]<br />
}<br />
E<br />
{<br />
    deg[head]++;<br />
    deg[tail]++;<br />
}<br />
END_G<br />
{<br />
    for (deg[n]) {<br />
        printf(&#8220;deg[%s] = %d
&#8221;, n.name, deg[n]);<br />
    }<br />
}
</dl>
<p> Computes the degrees of nodes with edges. </p>
<dl>
<dt>
<dd>
<pre><code>
BEGIN
{
    int i, indent;
    int seen[string];
    void prInd(int cnt)
    {
        for (i = 0; i &lt; cnt; i++)
            printf("  ");
    }
}
BEG_G
{
    $tvtype = TV_prepostfwd;
    $tvroot = node($, ARGV[0]);
}
N
{
    if (seen[$.name])
        indent--;
    else {
        prInd(indent);
        print($.name);
        seen[$.name] = 1;
        indent++;
    }
}
</code></pre>
</dl>
<p> Prints the depth-first traversal of the graph, starting with the node whose name is <code>ARGV[0]</code>, as an indented list.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>GVPRPATH</code></p>
<dd> Colon-separated list of directories to be searched to find the file specified by the -f option. <code>gvpr</code> has a default list built in. If <code>GVPRPATH</code> is not defined, the default list is used. If <code>GVPRPATH</code> starts with colon, the list is formed by appending <code>GVPRPATH</code> to the default list. If <code>GVPRPATH</code> ends with colon, the list is formed by appending the default list to <code>GVPRPATH</code>. Otherwise, <code>GVPRPATH</code> is used for the list.</dl>
<p> On Windows systems, replace &#8220;colon&#8221; with &#8220;semicolon&#8221; in the previous paragraph.</p>
<h2>BUGS AND WARNINGS</h2>
<p> Scripts should be careful deleting nodes during <code>N{}</code> and <code>E{}</code> blocks using BFS and DFS traversals as these rely on stacks and queues of nodes. </p>
<p> When the program is given as a command line argument, the usual shell interpretation takes place, which may affect some of the special names in <code>gvpr</code>. To avoid this, it is best to wrap the program in single quotes. </p>
<p> If string constants contain pattern metacharacters that you want to escape to avoid pattern matching, two backslashes will probably be necessary, as a single backslash will be lost when the string is originally scanned. Usually, it is simpler to use <code>strcmp</code> to avoid pattern matching. </p>
<p> As of 24 April 2008, <code>gvpr</code> switched to using a new, underlying graph library, which uses the simpler model that there is only one copy of a node, not one copy for each subgraph logically containing it. This means that iterators such as <i>nxtnode</i> cannot traverse a subgraph using just a node argument. For this reason, subgraph traversal requires new functions ending in &quot;_sg&quot;, which also take a subgraph argument. The versions without that suffix will always traverse the root graph. </p>
<p> There is a single global scope, except for formal function parameters, and even these can interfere with the type system. Also, the extent of all variables is the entire life of the program. It might be preferable for scope to reflect the natural nesting of the clauses, or for the program to at least reset locally declared variables. For now, it is advisable to use distinct names for all variables. </p>
<p> If a function ends with a complex statement, such as an IF statement, with each branch doing a return, type checking may fail. Functions should use a return at the end. </p>
<p> The expr library does not support string values of (char*)0. This means we can&#8217;t distinguish between &quot;&quot; and (char*)0 edge keys. For the purposes of looking up and creating edges, we translate &quot;&quot; to be (char*)0, since this latter value is necessary in order to look up any edge with a matching head and tail. </p>
<p> Related to this, strings converted to integers act like char pointers, getting the value 0 or 1 depending on whether the string consists solely of zeroes or not. Thus, the ((int)&quot;2&quot;) evaluates to 1. </p>
<p> The language inherits the usual C problems such as dangling references and the confusion between &#8216;=&#8217; and &#8216;==&#8217;.</p>
<h2>AUTHOR</h2>
<p> Emden R. Gansner &lt;erg [at] research.att.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-awk/">awk</a>(1), <a href="/docs/linux/man/1-gc/">gc</a>(1), <a href="/docs/linux/man/1-dot/">dot</a>(1), <a href="/docs/linux/man/1-nop/">nop</a>(1), <a href="/docs/linux/man/3-expr/">expr</a>(3), <a href="/docs/linux/man/3-cgraph/">cgraph</a>(3) </p>
<h2>Index</h2>
