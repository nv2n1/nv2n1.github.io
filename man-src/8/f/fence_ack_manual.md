---
title: "fence_ack_manual(8)"
name: "fence_ack_manual"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fence_ack_manual/"
description: "fence_ack_manual – a program to override fenced fencing operations"
---

<p>fence_ack_manual &#8211; a program to override fenced fencing operations</p>
<h2>Synopsis</h2>
<p><code>fence_ack_manual</code> [OPTIONS] <i>nodename</i> </p>
<h2>Description</h2>
<p>When <code><a href="/docs/linux/man/8-fenced/">fenced</a></code>(8) fails to fence a node, it retries indefinately. <code><a href="/docs/linux/man/8-fence_ack_manual/">fence_ack_manual</a></code>(8) tells fenced to stop retrying and consider the node fenced. It is important that this only be done after the node has been manually turned off or prevented from writing to shared storage. Without this manual action and verification, the storage that fencing protects may become corrupted. When fenced fences a node that has no fence devices defined in the cluster configuration, the fencing operation fails. This failure will be repeated indefinately until fence_ack_manual is run by an operator to indicate the node is in a safe state to proceed. (Defining no fencing devices for node is the equivalent of using the fence_manual agent in previous versions.) </p>
<h2>Options</h2>
<dl>
<dt><code>-h</code></p>
<dd>Print a help message describing available options, then exit. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-fenced/">fenced</a></code>(8) </p>
