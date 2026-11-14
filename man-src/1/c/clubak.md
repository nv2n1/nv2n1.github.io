---
title: "clubak(1)"
name: "clubak"
section: "1"
letter: "c"
url: "/docs/linux/man/1-clubak/"
description: "clubak – format output from clush/pdsh-like output and more"
---

<h2>NAME</h2>
<p> clubak &#8211; format output from clush/pdsh-like output and more</p>
<h2>SYNOPSIS</h2>
<p> <code>clubak</code> [ OPTIONS ]</p>
<h2>DESCRIPTION</h2>
<p> <code>clubak</code> formats text from standard input containing lines of the form &quot;<i>node:output</i>&quot;. It is fully backward compatible with <code><a href="/docs/linux/man/1-dshbak/">dshbak</a></code>(1) but provides additional features. For instance, <code>clubak</code> always displays its results sorted by node/nodeset. </p>
<p> You do not need to use <code>clubak</code> when using <code><a href="/docs/linux/man/1-clush/">clush</a></code>(1) as all output formatting features are already included in. It is provided for other usages, like post-processing results of the form &quot;<i>node:output</i>&quot;. </p>
<p> Like <code><a href="/docs/linux/man/1-clush/">clush</a></code>(1), <code>clubak</code> uses the <i>ClusterShell.MsgTree</i> module of the ClusterShell library (see <code>pydoc ClusterShell.MsgTree</code>).</p>
<h2>INVOCATION</h2>
<p> <code>clubak</code> should be started with connected standard input.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd> show <code>clubak</code> version number and exit</p>
<dt><code>-b</code>,<code> -c</code></p>
<dd> gather nodes with same output (-c is provided for <code><a href="/docs/linux/man/1-dshbak/">dshbak</a></code>(1) compatibility)</p>
<dt><code>-d</code>,<code> &#8211;debug</code></p>
<dd> output more messages for debugging purpose</p>
<dt><code>-L</code></p>
<dd> disable header block and order output by nodes</p>
<dt><code>-r</code>,<code> &#8211;regroup</code></p>
<dd> fold nodeset using node groups</p>
<dt><code>-s</code><i>&nbsp;<wbr>GROUPSOURCE</i>,<code>&nbsp;<wbr>&#8211;groupsource=</code><i>GROUPSOURCE</i></p>
<dd> optional <code><a href="/docs/linux/man/5-groups-conf/">groups.conf</a></code>(5) group source to use</p>
<dt><code>-G</code>,<code> &#8211;groupbase</code></p>
<dd> do not display group source prefix (always <i>@groupname</i>)</p>
<dt><code>-S</code><i>&nbsp;<wbr>SEPARATOR</i>,<code>&nbsp;<wbr>&#8211;separator=</code><i>SEPARATOR</i></p>
<dd> node / line content separator string (default: <i>:</i>)</p>
<dt><code>-F</code>,<code> &#8211;fast</code></p>
<dd> faster but memory hungry mode (preload all messages per node)</p>
<dt><code>-T</code>,<code> &#8211;tree</code></p>
<dd> message tree trace mode; switch to enable <code>ClusterShell.MsgTree</code> trace mode, all keys/nodes being kept for each message element of the tree, thus allowing special output gathering</p>
<dt><code>&#8211;color=</code><i>WHENCOLOR</i></p>
<dd> whether to use ANSI colors to surround node or nodeset prefix/header with escape sequences to display them in color on the terminal. <i>WHENCOLOR</i> is <code>never</code>, <code>always</code> or <code>auto</code> (which use color if standard output refers to a terminal). Color is set to [34m (blue foreground text) and cannot be modified.</p>
<dt><code>&#8211;diff</code></p>
<dd> show diff between gathered outputs</dl>
<h2>EXIT STATUS</h2>
<p> An exit status of zero indicates success of the <code>clubak</code> command.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>1.</p>
<dd> <code>clubak</code> can be used to gather some recorded <code><a href="/docs/linux/man/1-clush/">clush</a></code>(1) results:</p>
<dt><code>Record <a href="/docs/linux/man/1-clush/">clush</a></code>(1) results in a file:</p>
<dd>
<pre><code>
#clush - w node[1 - 7] uname - r&gt; / tmp / clush_output
#clush - w node[32 - 159] uname - r&gt;&gt; / tmp / clush_output
</code></pre>
<dt><code>Display file gathered results (in line-mode):</code></p>
<dd>
<pre>
# clubak -bL &lt;/tmp/clush_output
</pre>
<dt>2.</p>
<dd> Another example, iterate over <i>node*</i> text files in current directory and gather characters count for all of them: </p>
<pre><code>
#find - name "node*" - exec wc - c{}; | awk '{ gsub("./","",$2); print $2": "$1 }' | clubak - bL
node[1, 3] : 7 node2 : 9
</code></pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-clush/">clush</a></code>(1), <code><a href="/docs/linux/man/1-nodeset/">nodeset</a></code>(1), <code><a href="/docs/linux/man/5-groups-conf/">groups.conf</a></code>(5).</p>
<h2>BUG REPORTS</h2>
<dl>
<dt><code>Use the following URL to submit a bug report or feedback:</code></p>
<dd> <i><a rel="nofollow" href="https://github.com/cea-hpc/clustershell/issues">https://github.com/cea-hpc/clustershell/issues</a></i></dl>
<h2>AUTHOR</h2>
<p> Stephane Thiell &lt;sthiell [at] stanford.edu&gt;</p>
<h2>COPYRIGHT</h2>
<p> GNU Lesser General Public License version 2.1 or later (LGPLv2.1+) </p>
<h2>Index</h2>
