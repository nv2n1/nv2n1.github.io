---
title: "dev_remove_pack(9)"
name: "dev_remove_pack"
section: "9"
letter: "d"
url: "/docs/linux/man/9-dev_remove_pack/"
description: "dev_remove_pack – remove packet handler"
---

<p>dev_remove_pack &#8211; remove packet handler</p>
<h2>Synopsis</h2>
<pre><code>void dev_remove_pack(struct packet_type *pt);</code></pre>
<h2>Arguments</h2>
<p><i>pt</i></p>
<dl>
<dd>
<dd>packet type declaration</dl>
<h2>Description</h2>
<p>Remove a protocol handler that was previously added to the kernel protocol handlers by <code>dev_add_pack</code>. The passed packet_type is removed from the kernel lists and can be freed or reused once this function returns. </p>
<p> This call sleeps to guarantee that no CPU is looking at the packet type after return.</p>
<h2>Copyright</h2>
