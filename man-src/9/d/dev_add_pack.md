---
title: "dev_add_pack(9)"
name: "dev_add_pack"
section: "9"
letter: "d"
url: "/docs/linux/man/9-dev_add_pack/"
---

dev_add_pack - add packet handler

<h2>Synopsis</h2>

<pre><code>void dev_add_pack(struct packet_type *pt);</code></pre>

<h2>Arguments</h2>

<i>pt</i>
<dl><dd><dd>packet type declaration</dl>

<h2>Description</h2>

Add a protocol handler to the networking stack. The passed packet_type is linked into kernel lists and may not be freed until it has been removed from the kernel lists. 

 This call does not sleep therefore it can not guarantee all CPU's that are in middle of receiving packets will see the new packet type (until the next received packet).

<h2>Copyright</h2>


