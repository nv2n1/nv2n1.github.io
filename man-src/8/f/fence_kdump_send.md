---
title: "fence_kdump_send(8)"
name: "fence_kdump_send"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fence_kdump_send/"
description: "fence_kdump_send – send kdump acknowlegement message to cluster nodes"
---

<p>fence_kdump_send &#8211; send kdump acknowlegement message to cluster nodes</p>
<h2>Synopsis</h2>
<p><code>fence_kdump_send</code> [<i>OPTIONS]</i>&#8230; [NODE]&#8230;</p>
<h2>Description</h2>
<p><i>fence_kdump_send</i> is a utility used to send messages that acknowledge that the node has entered the kdump crash recovery service. This utility is intended to be used the the <i>fence_kdump</i> agent as a means detect that a failed node has entered the kdump crash recovery service. The <i>fence_kdump_send</i> utility is typically run from within the kdump kernel after a cluster node has encountered a kernel panic. Once the cluster node has entered the kdump crash recovery service, <i>fence_kdump_send</i> will periodically send messages to all cluster nodes. When the <i>fence_kdump</i> agent receives a valid message from the failed node, fencing is complete.</p>
<h2>Options</h2>
<dl>
<dt><code>-p, &#8211;ipport=</code><i>PORT</i></p>
<dd>IP port number that the <i>fence_kdump</i> agent is using to listen for messages. (default: 7410)</p>
<dt><code>-f, &#8211;family=</code><i>FAMILY</i></p>
<dd>IP network family. Force the <i>fence_kdump_send</i> utility to use a particular network family. Value for <i>FAMILY</i> can be &quot;auto&quot;, &quot;ipv4&quot;, or &quot;ipv6&quot;. (default: auto)</p>
<dt><code>-c, &#8211;count=</code><i>COUNT</i></p>
<dd>Number of messages to send. If <i>COUNT</i> is zero, <i>fence_kdump_send</i> will send messages indefinitely. (default: 0)</p>
<dt><code>-i, &#8211;interval=</code><i>INTERVAL</i></p>
<dd>Time to wait between sending a message. The value for <i>INTERVAL</i> must be greater than zero. (default: 10)</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd>Print verbose output.</p>
<dt><code>-V, &#8211;version</code></p>
<dd>Print version and exit.</p>
<dt><code>-h, &#8211;help</code></p>
<dd>Print usage and exit.</dl>
<h2>Author</h2>
<p>Ryan O&#8217;Hara &lt;rohara [at] redhat.com&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-fence_kdump/">fence_kdump</a>(8), <a href="/docs/linux/man/8-mkdumprd/">mkdumprd</a>(8), <a href="/docs/linux/man/5-kdump-conf/">kdump.conf</a>(5) </p>
