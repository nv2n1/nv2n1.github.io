---
title: "whatsup(1)"
name: "whatsup"
section: "1"
letter: "w"
url: "/docs/linux/man/1-whatsup/"
description: "whatsup – list up and/or down nodes in a cluster"
---

<h2>NAME</h2>
<p> whatsup &#8211; list up and/or down nodes in a cluster</p>
<h2>SYNOPSIS</h2>
<p> <code>whatsup</code> [<i>OPTION</i>]&#8230; [<i>NODES</i>]&#8230; </p>
<h2>DESCRIPTION</h2>
<p> <code>whatsup</code> lists which nodes are currently up or down in a cluster. It determines which nodes are up or down based on information provided by the <code><a href="/docs/linux/man/3-nodeupdown/">nodeupdown</a>(3)</code> library. Configuration of backend components or clusterlists for the <code><a href="/docs/linux/man/3-nodeupdown/">nodeupdown</a>(3)</code> library may be needed. Please see <code><a href="/docs/linux/man/3-libnodeupdown/">libnodeupdown</a>(3).</code> </p>
<p> <code>whatsup</code> will check on the status of every node in the cluster unless specific nodes are listed at the command line. If the first node listed is &quot;-&quot;, nodes will be read in from standard input. The nodes can be listed in hostrange format, comma separated lists, or space separated lists. See the section below on HOST RANGES for instructions on how to list hosts in hostrange format. The hostnames listed must be the shortened names of hostnames. </p>
<p> The exit value of <code>whatsup</code> depends on the options performed on the command line. If the default &#8211;updown option is used, the exit value will be 0 if the command succeeds without error. If the &#8211;up option is used and no nodes are specified via the command line or standard input, the exit value will be 0 if all cluster nodes are up. If nodes are specified via the command line or standard input, the exit value wil be 0 if all the specified nodes are up. The behavior is similar for the &#8211;down option. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Print help and exit</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Print version and exit</p>
<dt><code>-o </code><i>STRING</i>, <code>&#8211;hostname</code>=<i>STRING</i></p>
<dd> server hostname (default=localhost)</p>
<dt><code>-p </code><i>INT</i>, <code>&#8211;port</code>=<i>INT</i></p>
<dd> server port (default=8649)</p>
<dt><code>-b, &#8211;updown</code></p>
<dd> List both up and down nodes (default)</p>
<dt><code>-u, &#8211;up</code></p>
<dd> List only up nodes</p>
<dt><code>-d, &#8211;down</code></p>
<dd> List only down nodes</p>
<dt><code>-t, &#8211;count</code></p>
<dd> List only node counts</p>
<dt><code>-q, &#8211;hostrange</code></p>
<dd> List nodes in hostrange format (default)</p>
<dt><code>-c, &#8211;comma</code></p>
<dd> List nodes in comma separated list</p>
<dt><code>-n, &#8211;newline</code></p>
<dd> List nodes in newline separated list</p>
<dt><code>-s, &#8211;space</code></p>
<dd> List nodes in space separated list</p>
<dt><code>-m, &#8211;module</code></p>
<dd> Use a specific backend module for up-down calculations.</p>
<dt><code>-r, &#8211;last-up-time</code></p>
<dd> Output last known up time of nodes and their current up or down state. This option may not be available on some configurations.</p>
<dt><code>-l, &#8211;log</code></p>
<dd> Enter <code>whatsup</code> logging mode. <code>Whatsup </code> will regularly poll the backend tool to calculate up-down state changes and output them to the appropriate output.</p>
<dt><code>-f, &#8211;log-file</code></p>
<dd> Specify the log file <code>Whatsup</code> should output logging information to. If not specified, defaults to stdout.</p>
<dt><code>-e, &#8211;log-poll</code></p>
<dd> Specify the length in seconds the log mode of <code>whatsup</code> should regularly poll. Default is 30 seconds.</p>
<dt><code>-M, &#8211;monitor</code></p>
<dd> Monitor up-down state changes through event monitoring.</dl>
<h2>HOST RANGES</h2>
<p> As noted in sections above, <code>whatsup</code> accepts ranges of hostnames in the general form: prefix[n-m,l-k,&#8230;], where n &lt; m and l &lt; k, etc., as an alternative to explicit lists of hosts. This form should not be confused with regular expression character classes (also denoted by &#8220;[]&#8221;). For example, foo[19] does not represent foo1 or foo9, but rather represents a degenerate range: foo19. </p>
<p> This range syntax is meant only as a convenience on clusters with a prefixNN naming convention and specification of ranges should not be considered necessary &#8212; the list foo1,foo9 could be specified as such, or by the range foo[1,9]. </p>
<p> Some examples of range usage follow: </p>
<p> List all nodes among foo01,foo02,&#8230;,foo05 that are up and down<br />
&nbsp;<wbr>whatsup foo[01-05] </p>
<p> List all nodes among foo7,foo9,foo10 that are up and down<br />
&nbsp;<wbr>whatsup foo[7,9-10] </p>
<p> As a reminder to the reader, some shells will interpret brackets (&#8216;[&#8216; and &#8216;]&#8217;) for pattern matching. Depending on your shell, it may be necessary to enclose ranged lists within quotes. For example, in tcsh, the above two examples should be executed as: </p>
<p>&nbsp;<wbr>whatsup&nbsp;<wbr>&quot;foo[01-05]&quot;<br />
&nbsp;<wbr>whatsup&nbsp;<wbr>&quot;foo[7,9-10]&quot; </p>
<h2>EXAMPLES</h2>
<p> List all nodes that are up and down.<br />
&nbsp;<wbr>&nbsp;<wbr>whatsup </p>
<p> List all nodes that are down<br />
&nbsp;<wbr>&nbsp;<wbr>whatsup -d </p>
<p> List all nodes among foo[0-20] that are down<br />
&nbsp;<wbr>&nbsp;<wbr>whatsup -d foo[0-20] </p>
<p> List all nodes that are up and down by their alternate names<br />
&nbsp;<wbr>&nbsp;<wbr>whatsup -a </p>
<p> List all nodes among foo[5-25] that are up by their alternate names<br />
&nbsp;<wbr>&nbsp;<wbr>whatsup -u -a foo[5-25] </p>
<p> List all nodes that are up in comma separated lists.<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<p>&nbsp;<wbr>&nbsp;<wbr>whatsup -u -c </p>
<p> List all nodes that are up among the nodes foo2, foo4, and foo8<br />
&nbsp;<wbr>&nbsp;<wbr>whatsup -u foo2,foo4,foo8 </p>
<p> Only output the number of nodes that are up and down<br />
&nbsp;<wbr>&nbsp;<wbr>whatsup -t </p>
<p> Only output the number of up nodes<br />
&nbsp;<wbr>&nbsp;<wbr>whatsup -u -t </p>
<p> Only output the number of up nodes among foo[5-25]<br />
&nbsp;<wbr>&nbsp;<wbr>whatsup -u -t foo[5-25]</p>
<h2>FILES</h2>
<p> /usr/bin/whatsup</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-libnodeupdown/">libnodeupdown</a>(3), <a href="/docs/linux/man/5-nodeupdown-conf/">nodeupdown.conf</a>(5)</p>
<h2>ORIGIN</h2>
<p> Developed by Albert Chu &lt;chu11 [at] llnl.gov&gt; on LLNL&#8217;s Linux clusters. This software is open source and distributed under the terms of the Gnu GPL. </p>
<h2>Index</h2>
