---
title: "nfsiostat(8)"
name: "nfsiostat"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nfsiostat/"
description: "nfsiostat – Emulate iostat for NFS mount points using /proc/self/mountstats"
---

<p>nfsiostat &#8211; Emulate iostat for NFS mount points using /proc/self/mountstats</p>
<h2>Synopsis</h2>
<p><code>nfsiostat [[</code><i>&lt;interval&gt;</i><code>] [</code><i>&lt;count&gt;</i><code>]] [</code><i>&lt;options&gt;</i><code>][&lt;mount_point&gt;</code><i>]</i></p>
<h2>Description</h2>
<p>The <code>nfsiostat</code> command displays NFS client per-mount statisitics.</p>
<dl>
<dt>&lt;interval&gt;</p>
<dd>specifies the amount of time in seconds between each report. The first report contains statistics for the time since each file system was mounted. Each subsequent report contains statistics collected during the interval since the previous report.</p>
<dt>&lt;count&gt;</p>
<dd>If the <i>&lt;count&gt;</i> parameter is specified, the value of <i>&lt;count&gt; </i> determines the number of reports generated at <i>&lt;interval&gt; </i> seconds apart. if the interval parameter is specified without the <i>&lt;count&gt; </i> parameter, the command generates reports continuously.</p>
<dt>&lt;options&gt;</p>
<dd>Define below</p>
<dt>&lt;mount_point&gt;</p>
<dd>If one or more <i>&lt;mount point&gt; </i> names are specified, statistics for only these mount points will be displayed. Otherwise, all NFS mount points on the client are listed.</p>
<dt>The meaning of each column of <code>nfsiostat</code>&#8216;s output is the following:</p>
<dd>
<dl>
<dd>&#8211; <code>op/s</code></p>
<dl>
<dd>This is the number of operations per second.</p>
<dl>
<dd></dl>
</dl>
</dl>
<dl>
<dd>&#8211; <code>rpc bklog</code></p>
<dl>
<dd>This is the length of the backlog queue.</dl>
</dl>
<dl>
<dd>&#8211; <code>kB/s</code></p>
<dl>
<dd>This is the number of kB written/read per second.</dl>
</dl>
<dl>
<dd>&#8211; <code>kB/op</code></p>
<dl>
<dd>This is the number of kB written/read per each operation.</dl>
</dl>
<dl>
<dd>&#8211; <code>retrans</code></p>
<dl>
<dd>This is the number of retransmissions.</dl>
</dl>
<dl>
<dd>&#8211; <code>avg RTT (ms)</code></p>
<dl>
<dd>This is the duration from the time that client&#8217;s kernel sends the RPC request until the time it receives the reply.</dl>
</dl>
<dl>
<dd>&#8211; <code>avg exe (ms)</code></p>
<dl>
<dd>This is the duration from the time that NFS client does the RPC request to its kernel until the RPC request is completed, this includes the RTT time above.</dl>
</dl>
<dt>Note that if an interval is used as argument to <code>nfsiostat</code>, then the diffrence from previous interval will be displayed, otherwise the results will be from the time that the share was mounted.</p>
<dd>
<h2>Options</h2>
<dl>
<dt><code>-a or &#8211;attr</code></p>
<dd>displays statistics related to the attribute cache</p>
<dt><code>-d or &#8211;dir </code></p>
<dd>displays statistics related to directory operations</p>
<dt><code>-h or &#8211;help </code></p>
<dd>shows help message and exit</p>
<dt><code>-l LIST or &#8211;list=LIST </code></p>
<dd>only print stats for first LIST mount points</p>
<dt><code>-p or &#8211;page</code></p>
<dd>displays statistics related to the page cache</p>
<dt><code>-s or &#8211;sort</code></p>
<dd>Sort NFS mount points by ops/second</p>
<dt><code>&#8211;version</code></p>
<dd>show program&#8217;s version number and exit</dl>
<h2>Files</h2>
<dl>
<dt><code>/proc/self/mountstats</code></p>
<dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-iostat/">iostat</a></code>(8), <code><a href="/docs/linux/man/8-mountstats/">mountstats</a></code>(8), <code><a href="/docs/linux/man/8-nfsstat/">nfsstat</a>(8)</code></p>
<h2>Author</h2>
<p>Chuck Lever &lt;chuck.lever [at] oracle.com&gt;</p>
