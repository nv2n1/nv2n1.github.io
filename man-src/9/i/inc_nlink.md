---
title: "inc_nlink(9)"
name: "inc_nlink"
section: "9"
letter: "i"
url: "/docs/linux/man/9-inc_nlink/"
description: "inc_nlink – directly increment an inode’s link count"
---

<p>inc_nlink &#8211; directly increment an inode&#8217;s link count</p>
<h2>Synopsis</h2>
<pre><code>void inc_nlink(struct inode *inode);</code></pre>
<h2>Arguments</h2>
<p><i>inode</i></p>
<dl>
<dd>
<dd>inode</dl>
<h2>Description</h2>
<p>This is a low-level filesystem helper to replace any direct filesystem manipulation of i_nlink. Currently, it is only here for parity with <code>dec_nlink</code>.</p>
<h2>Copyright</h2>
