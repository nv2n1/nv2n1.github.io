---
title: "dev_add_offload(9)"
name: "dev_add_offload"
section: "9"
letter: "d"
url: "/docs/linux/man/9-dev_add_offload/"
---

dev_add_offload - register offload handlers

<h2>Synopsis</h2>

<pre><code>void dev_add_offload(struct packet_offload *po);</code></pre>

<h2>Arguments</h2>

<i>po</i>
<dl><dd><dd>protocol offload declaration</dl>

<h2>Description</h2>

Add protocol offload handlers to the networking stack. The passed proto_offload is linked into kernel lists and may not be freed until it has been removed from the kernel lists. 

 This call does not sleep therefore it can not guarantee all CPU's that are in middle of receiving packets will see the new offload handlers (until the next received packet).

<h2>Copyright</h2>


