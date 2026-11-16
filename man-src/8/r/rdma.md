---
title: "rdma(8)"
name: "rdma"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rdma/"
description: "rdma – RDMA tool"
---

<p>rdma &#8211; RDMA tool</p>
<h2>Synopsis</h2>
<pre><code>rdma
[ OPTIONS ] OBJECT { COMMAND |
    help }
</code></pre>
<p> <code>rdma</code> [ <code>-force</code> ] <code>-batch </code><i>filename</i> </p>
<pre><code>OBJECT := {
    dev | link | resource | system | statistic }
OPTIONS := {
    -V[ersion] |
    -d[etails] }
-j[son] }
-p[retty] }
</code></pre>
<h2>Options</h2>
<dl>
<dt><code>-V</code>,<code> -Version</code></dt>
<dd>Print the version of the <code>rdma</code> tool and exit. </dd>
<dt><code>-b,</code> -batch <code>&lt;FILENAME&gt;</code></dt>
<dd>Read commands from provided file or standard input and invoke them. First failure will cause termination of rdma. </dd>
<dt><code>-force</code></dt>
<dd>Don&#8217;t terminate rdma on errors in batch mode. If there were any errors during execution of the commands, the application return code will be non zero. </dd>
<dt><code>-d</code>,<code> &#8211;details</code></dt>
<dd>Output detailed information. Adding a second -d includes driver-specific details. </dd>
<dt><code>-r</code>,<code> &#8211;raw</code></dt>
<dd>Output includes driver-specific details in raw format. </dd>
<dt><code>-p</code>,<code> &#8211;pretty</code></dt>
<dd>When combined with -j generate a pretty JSON output. </dd>
<dt><code>-j</code>,<code> &#8211;json</code></dt>
<dd>Generate JSON output. </dd>
</dl>
<h3><i>OBJECT</i></h3>
<dl>
<dt><code>dev</code></dt>
<dd>&#8211; RDMA device. </dd>
<dt><code>link</code></dt>
<dd>&#8211; RDMA port related. </dd>
<dt><code>resource</code></dt>
<dd>&#8211; RDMA resource configuration. </dd>
<dt><code>sys</code></dt>
<dd>&#8211; RDMA subsystem related. </dd>
<dt><code>statistic</code></dt>
<dd>&#8211; RDMA counter statistic related. </dd>
</dl>
<p> The names of all objects may be written in full or abbreviated form, for example <code>stats</code> can be abbreviated as <code>stat</code> or just <code>s.</code></p>
<h3><i>COMMAND</i></h3>
<p>Specifies the action to perform on the object. The set of possible actions depends on the object type. As a rule, it is possible to <code>show</code> (or <code>list</code> ) objects, but some objects do not allow all of these operations or have some additional commands. The <code>help</code> command is available for all objects. It prints out a list of available commands and argument syntax conventions. </p>
<p> If no command is given, some default command is assumed. Usually it is <code>list</code> or, if the objects of this class cannot be listed, <code>help</code>.</p>
<h2>Exit Status</h2>
<p>Exit status is 0 if command was successful or a positive integer upon failure.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-rdma-dev/">rdma-dev</a></code>(8), <code><a href="/docs/linux/man/8-rdma-link/">rdma-link</a></code>(8), <code><a href="/docs/linux/man/8-rdma-resource/">rdma-resource</a></code>(8), <code><a href="/docs/linux/man/8-rdma-system/">rdma-system</a></code>(8), <code><a href="/docs/linux/man/8-rdma-statistic/">rdma-statistic</a></code>(8), </p>
<h2>Reporting Bugs</h2>
<p>Report any bugs to the Linux RDMA mailing list <code>&lt;linux-rdma [at] vger.kernel.org&gt;</code> where the development and maintenance is primarily done. You do not have to be subscribed to the list to send a message there.</p>
<h2>Author</h2>
<p>Leon Romanovsky &lt;leonro [at] mellanox.com&gt;</p>
