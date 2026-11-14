---
title: "idmapd(8)"
name: "idmapd"
section: "8"
letter: "i"
url: "/docs/linux/man/8-idmapd/"
description: "rpc.idmapd – NFSv4 ID <-> Name Mapper"
---

<p><code>rpc.idmapd</code> &#8211; NFSv4 ID &lt;-&gt; Name Mapper</p>
<h2>Synopsis</h2>
<p><code>rpc.idmapd</code> [-<code>h</code> ] [-<code>f</code> ] [-<code>v</code> ] [-<code>C</code> ] [-<code>S</code> ] [-<code>p </code><i>path</i> ] [-<code>c </code><i>path</i> ]</p>
<h2>Description</h2>
<p><code>rpc.idmapd</code> is the NFSv4 ID &lt;-&gt; name mapping daemon. It provides functionality to the NFSv4 kernel client and server, to which it communicates via upcalls, by translating user and group IDs to names, and vice versa. Note that on more recent kernels only the NFSv4 server uses <code>.</code> The NFSv4 client instead uses <a href="/docs/linux/man/8-nfsidmap/">nfsidmap</a>(8), and only falls back to <code>rpc.idmapd</code> if there was a problem running the <a href="/docs/linux/man/8-nfsidmap/">nfsidmap</a>(8) program. The options are as follows:</p>
<dl>
<dt><code>-h</code></p>
<dd>Display usage message.</p>
<dt><code>-v</code></p>
<dd>Increases the verbosity level (can be specified multiple times).</p>
<dt><code>-f</code></p>
<dd>Runs <code>rpc.idmapd</code> in the foreground and prints all output to the terminal.</p>
<dt><code>-p </code><i>path</i></p>
<dd>Specifies the location of the RPC pipefs to be <i>path</i> The default value is &quot;/var/lib/nfs/rpc_pipefs&quot;.</p>
<dt><code>-c </code><i>path</i></p>
<dd>Use configuration file <i>path</i></p>
<dt><code>-C</code></p>
<dd>Client-only: perform no idmapping for any NFS server, even if one is detected.</p>
<dt><code>-S</code></p>
<dd>Server-only: perform no idmapping for any NFS client, even if one is detected.</dl>
<h2>Examples</h2>
<p><code>rpc.idmapd -f -vvv</code> </p>
<p> Runs <code>rpc.idmapd</code> printing all messages to console, and with a verbosity level of 3.</p>
<h2>Files</h2>
<p>/etc/idmapd.conf</p>
<h2>See Also</h2>
<p>idmapd.conf5, <a href="/docs/linux/man/8-nfsidmap/">nfsidmap</a>(8)</p>
<h2>Authors</h2>
<p>The <code>rpc.idmapd</code> software has been developed by Marius Aamodt Eriksen Aq marius [at] citi.umich.edu .</p>
