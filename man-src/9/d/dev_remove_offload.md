---
title: "dev_remove_offload(9)"
name: "dev_remove_offload"
section: "9"
letter: "d"
url: "/docs/linux/man/9-dev_remove_offload/"
description: "dev_remove_offload – remove packet offload handler"
---

<p>dev_remove_offload &#8211; remove packet offload handler</p>
<h2>Synopsis</h2>
<pre><code>void dev_remove_offload(struct packet_offload *po);</code></pre>
<h2>Arguments</h2>
<p><i>po</i></p>
<dl>
<dd>
<dd>packet offload declaration</dl>
<h2>Description</h2>
<p>Remove a packet offload handler that was previously added to the kernel offload handlers by <code>dev_add_offload</code>. The passed offload_type is removed from the kernel lists and can be freed or reused once this function returns. </p>
<p> This call sleeps to guarantee that no CPU is looking at the packet type after return.</p>
<h2>Copyright</h2>
