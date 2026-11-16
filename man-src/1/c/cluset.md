---
title: "cluset(1)"
name: "cluset"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cluset/"
description: "cluset – compute advanced cluster node set operations"
---

<h2>NAME</h2>
<p> cluset &#8211; compute advanced cluster node set operations</p>
<h2>SYNOPSIS</h2>
<p> <code>cluset</code> [OPTIONS] [COMMAND] [nodeset1 [OPERATION] nodeset2|&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> Note: <code>cluset</code> and <code>nodeset</code> are the same command. </p>
<p> <code>cluset</code> is an utility command provided with the ClusterShell library which implements some features of ClusterShell&#8217;s NodeSet and RangeSet Python classes. It provides easy manipulation of 1D or nD-indexed cluster nodes and node groups and supports RFC 1123 (except that a node name can&#8217;t be entirely numeric). </p>
<p> Also, <code>cluset</code> is automatically bound to the library node group resolution mechanism. Thus, it is especially useful to enhance cluster aware administration shell scripts.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></dt>
<dd> show program&#8217;s version number and exit</dd>
<dt><code>-h</code>,<code> &#8211;help</code></dt>
<dd> show this help message and exit</dd>
<dt><code>-s</code><i>&nbsp;<wbr>GROUPSOURCE</i>,<code>&nbsp;<wbr>&#8211;groupsource=</code><i>GROUPSOURCE</i></dt>
<dd> optional <code><a href="/docs/linux/man/5-groups-conf/">groups.conf</a></code>(5) group source to use</dd>
<dt><code>Commands:</code></dt>
<dd>
</dd><dt><code>-c</code>,<code> &#8211;count</code></dt>
<dd> show number of nodes in nodeset(s)</dd>
<dt><code>-e</code>,<code> &#8211;expand</code></dt>
<dd> expand nodeset(s) to separate nodes (see also -S <i>SEPARATOR</i>)</dd>
<dt><code>-f</code>,<code> &#8211;fold</code></dt>
<dd> fold nodeset(s) (or separate nodes) into one nodeset</dd>
<dt><code>-l</code>,<code> &#8211;list</code></dt>
<dd> list node groups, list node groups and nodes (<code>-ll</code>) or list node groups, nodes and node count (<code>-lll</code>). When no argument is specified at all, this command will list all node group names found in selected group source (see also -s <i>GROUPSOURCE</i>). If any nodesets are specified as argument, this command will find node groups these nodes belongs to (individually). Optionally for each group, the fraction of these nodes being member of the group may be displayed (with <code>-ll</code>), and also member count/total group node count (with <code>-lll</code>). If a single hyphen-minus (-) is given as a nodeset, it will be read from standard input.</dd>
<dt><code>-r</code>,<code> &#8211;regroup</code></dt>
<dd> fold nodes using node groups (see -s <i>GROUPSOURCE</i>)</dd>
<dt><code>&#8211;groupsources</code></dt>
<dd> list all active group sources (see <code><a href="/docs/linux/man/5-groups-conf/">groups.conf</a></code>(5))</dd>
<dt><code>Operations:</code></dt>
<dd>
</dd><dt><code>-x</code><i>&nbsp;<wbr>SUB_NODES</i>,<code>&nbsp;<wbr>&#8211;exclude=</code><i>SUB_NODES</i></dt>
<dd> exclude specified set</dd>
<dt><code>-i</code><i>&nbsp;<wbr>AND_NODES</i>,<code>&nbsp;<wbr>&#8211;intersection=</code><i>AND_NODES</i></dt>
<dd> calculate sets intersection</dd>
<dt><code>-X</code><i>&nbsp;<wbr>XOR_NODES</i>,<code>&nbsp;<wbr>&#8211;xor=</code><i>XOR_NODES</i></dt>
<dd> calculate symmetric difference between sets</dd>
<dt><code>Options:</code></dt>
<dd>
</dd><dt><code>-a</code>,<code> &#8211;all</code></dt>
<dd> call external node groups support to display all nodes</dd>
<dt><code>&#8211;autostep=</code><i>AUTOSTEP</i></dt>
<dd> enable a-b/step style syntax when folding nodesets, value is min node count threshold (integer &#8216;4&#8217;, percentage &#8216;50%&#8217; or &#8216;auto&#8217;). If not specified, auto step is disabled (best for compatibility with other cluster tools. Example: autostep=4, &quot;node2 node4 node6&quot; folds in node[2,4,6] but autostep=3, &quot;node2 node4 node6&quot; folds in node[2-6/2].</dd>
<dt><code>-d</code>,<code> &#8211;debug</code></dt>
<dd> output more messages for debugging purpose</dd>
<dt><code>-q</code>,<code> &#8211;quiet</code></dt>
<dd> be quiet, print essential output only</dd>
<dt><code>-R</code>,<code> &#8211;rangeset</code></dt>
<dd> switch to RangeSet instead of NodeSet. Useful when working on numerical cluster ranges, eg. 1,5,18-31</dd>
<dt><code>-G</code>,<code> &#8211;groupbase</code></dt>
<dd> hide group source prefix (always <i>@groupname</i>)</dd>
<dt><code>-S</code><i>&nbsp;<wbr>SEPARATOR</i>,<code>&nbsp;<wbr>&#8211;separator=</code><i>SEPARATOR</i></dt>
<dd> separator string to use when expanding nodesets (default: &#8216; &#8216;)</dd>
<dt><code>-O</code><i>&nbsp;<wbr>FORMAT</i>,<code>&nbsp;<wbr>&#8211;output-format=</code><i>FORMAT</i></dt>
<dd> output format (default: &#8216;%s&#8217;)</dd>
<dt><code>-I</code><i>&nbsp;<wbr>SLICE_RANGESET</i>,<code>&nbsp;<wbr>&#8211;slice=</code><i>SLICE_RANGESET</i></dt>
<dd> return sliced off result; examples of SLICE_RANGESET are &quot;0&quot; for simple index selection, or &quot;1-9/2,16&quot; for complex rangeset selection</dd>
<dt><code>&#8211;split=</code><i>MAXSPLIT</i></dt>
<dd> split result into a number of subsets</dd>
<dt><code>&#8211;contiguous</code></dt>
<dd> split result into contiguous subsets (ie. for nodeset, subsets will contain nodes with same pattern name and a contiguous range of indexes, like foobar[1-100]; for rangeset, subsets with consists in contiguous index ranges)&quot;&quot;&quot;</dd>
<dt><code>&#8211;axis=</code><i>RANGESET</i></dt>
<dd> for nD nodesets, fold along provided axis only. Axis are indexed from 1 to n and can be specified here either using the rangeset syntax, eg. &#8216;1&#8217;, &#8216;1-2&#8217;, &#8216;1,3&#8217;, or by a single negative number meaning that the indice is counted from the end. Because some nodesets may have several different dimensions, axis indices are silently truncated to fall in the allowed range.</dd>
<dt><code>&#8211;pick=</code><i>N</i></dt>
<dd> pick N node(s) at random in nodeset </dd>
<p> For a short explanation of these options, see <code>-h, &#8211;help</code>. </p>
<p> If a single hyphen-minus (-) is given as a nodeset, it will be read from standard input.</dl>
<h2>EXTENDED PATTERNS</h2>
<p> The <code>cluset</code> command benefits from ClusterShell NodeSet basic arithmetic addition. This feature extends recognized string patterns by supporting operators matching all Operations seen previously. String patterns are read from left to right, by proceeding any character operators accordingly.</p>
<dl>
<dt><code>Supported character operators</code></dt>
<dd>
</dd><dt><code>,</code></dt>
<dd> indicates that the <i>union</i> of both left and right nodeset should be computed before continuing</dd>
<dt><code>!</code></dt>
<dd> indicates the <i>difference</i> operation</dd>
<dt><code>&amp;</code></dt>
<dd> indicates the <i>intersection</i> operation</dd>
<dt><code>^</code></dt>
<dd> indicates the <i>symmetric difference</i> (XOR) operation </dd>
<p> Care should be taken to escape these characters as needed when the shell does not interpret them literally.</p>
<dt><code>Examples of use of extended patterns</code></dt>
<dd>
</dd><dt><code>$ cluset -f node[0-7],node[8-10]</code></dt>
<dd>
<pre>
node[0-10]
</pre>
</dd><dt><code>$ cluset -f node[0-10]!node[8-10]</code></dt>
<dd>
<pre>
node[0-7]
</pre>
</dd><dt><code>$ cluset -f node[0-10]&amp;node[5-13]</code></dt>
<dd>
<pre>
node[5-10]
</pre>
</dd><dt><code>$ cluset -f node[0-10]^node[5-13]</code></dt>
<dd>
<pre>
node[0-4,11-13]
</pre>
</dd><dt><code>Example of advanced usage</code></dt>
<dd>
</dd><dt><code>$ cluset -f @gpu^@slurm:bigmem!@chassis[1-9/2]</code></dt>
<dd>
<p> This computes a folded nodeset containing nodes found in group @gpu and @slurm:bigmem, but not in both, minus the nodes found in odd chassis groups from 1 to 9.</p>
</dd><dt><code>All nodes extension (v1.7+)</code></dt>
<dd> The <code>@*</code> and <code>@SOURCE:*</code> special notations may be used in extended patterns to represent all nodes (in SOURCE) according to the <i>all</i> external shell command (see <code><a href="/docs/linux/man/5-groups-conf/">groups.conf</a></code>(5)) and are equivalent to:</dd>
<dt><code>$ cluset [-s SOURCE] -a -f</code></dt>
<dd></dd></dl>
<h2>EXIT STATUS</h2>
<p> An exit status of zero indicates success of the <code>cluset</code> command. A non-zero exit status indicates failure.</p>
<h2>EXAMPLES</h2>
<dl>
<dt><code>Getting the node count</code></dt>
<dd>
</dd><dt><code>$ cluset -c node[0-7,32-159]</code></dt>
<dd>
<pre>
136
</pre>
</dd><dt><code>$ cluset -c node[0-7,32-159] node[160-163]</code></dt>
<dd>
<pre>
140
</pre>
</dd><dt><code>$ cluset -c dc[1-2]n[100-199]</code></dt>
<dd>
<pre>
200
</pre>
</dd><dt><code>$ cluset -c @login</code></dt>
<dd>
<pre>
4
</pre>
</dd><dt><code>Folding nodesets</code></dt>
<dd>
</dd><dt><code>$ cluset -f node[0-7,32-159] node[160-163]</code></dt>
<dd>
<pre>
node[0-7,32-163]
</pre>
</dd><dt><code>$ echo node3 node6 node1 node2 node7 node5 | cluset -f</code></dt>
<dd>
<pre>
node[1-3,5-7]
</pre>
</dd><dt><code>$ cluset -f dc1n2 dc2n2 dc1n1 dc2n1</code></dt>
<dd>
<pre><code>
dc[1 - 2] n[1 - 2]
</code></pre>
</dd><dt><code>$ cluset &#8211;axis=1 -f dc1n2 dc2n2 dc1n1 dc2n1</code></dt>
<dd>
dc[1 &#8211; 2] n1, dc[1 &#8211; 2] n2</dd>
<dt><code>Expanding nodesets</code></dt>
<dd>
</dd><dt><code>$ cluset -e node[160-163]</code></dt>
<dd>
<pre>
node160 node161 node162 node163
</pre>
</dd><dt><code>$ echo &#8216;dc[1-2]n[2-6/2]&#8217; | cluset -e</code></dt>
<dd>
<pre>
dc1n2 dc1n4 dc1n6 dc2n2 dc2n4 dc2n6
</pre>
</dd><dt><code>Excluding nodes from nodeset</code></dt>
<dd>
</dd><dt><code>$ cluset -f node[32-159] -x node33</code></dt>
<dd>
<pre>
node[32,34-159]
</pre>
</dd><dt><code>Computing nodesets intersection</code></dt>
<dd>
</dd><dt><code>$ cluset -f node[32-159] -i node[0-7,20-21,32,156-159]</code></dt>
<dd>
<pre>
node[32,156-159]
</pre>
</dd><dt><code>Computing nodesets symmetric difference (xor)</code></dt>
<dd>
</dd><dt><code>$ cluset -f node[33-159] &#8211;xor node[32-33,156-159]</code></dt>
<dd>
<pre>
node[32,34-155]
</pre>
</dd><dt><code>Splitting nodes into several nodesets (expanding results)</code></dt>
<dd>
</dd><dt><code>$ cluset &#8211;split=3 -e node[1-9]</code></dt>
<dd>
<pre>
node1 node2 node3
node4 node5 node6
node7 node8 node9
</pre>
</dd><dt><code>Splitting non-contiguous nodesets (folding results)</code></dt>
<dd>
</dd><dt><code>$ cluset &#8211;contiguous -f node2 node3 node4 node8 node9</code></dt>
<dd>
node[2 &#8211; 4] node[8 &#8211; 9]</dd>
<dt><code>$ cluset &#8211;contiguous -f dc[1,3]n[1-2,4-5]</code></dt>
<dd>
<pre><code>
dc1n[1 - 2] dc1n[4 - 5] dc3n[1 - 2] dc3n[4 - 5]
</code></pre>
</dd></dl>
<h2>HISTORY</h2>
<p> <code>cluset</code> was added in 1.7.3 to avoid a conflict with xCAT&#8217;s <code>nodeset</code> command and also to conform with ClusterShell&#8217;s &quot;clu*&quot; command nomenclature.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-nodeset/">nodeset</a></code>(1), <code><a href="/docs/linux/man/1-clush/">clush</a></code>(1), <code><a href="/docs/linux/man/1-clubak/">clubak</a></code>(1), <code><a href="/docs/linux/man/5-groups-conf/">groups.conf</a></code>(5).</p>
<h2>BUG REPORTS</h2>
<dl>
<dt><code>Use the following URL to submit a bug report or feedback:</code></dt>
<dd> <i><a rel="nofollow" href="https://github.com/cea-hpc/clustershell/issues">https://github.com/cea-hpc/clustershell/issues</a></i></dd></dl>
<h2>AUTHOR</h2>
<p> Stephane Thiell &lt;sthiell [at] stanford.edu&gt;</p>
<h2>COPYRIGHT</h2>
<p> GNU Lesser General Public License version 2.1 or later (LGPLv2.1+) </p>
<h2>Index</h2>
