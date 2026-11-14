---
title: "iput(9)"
name: "iput"
section: "9"
letter: "i"
url: "/docs/linux/man/9-iput/"
description: "iput – put an inode"
---

<p>iput &#8211; put an inode</p>
<h2>Synopsis</h2>
<pre><code>void iput(struct inode *inode);</code></pre>
<h2>Arguments</h2>
<p><i>inode</i></p>
<dl>
<dd>
<dd>inode to put</dl>
<h2>Description</h2>
<p>Puts an inode, dropping its usage count. If the inode use count hits zero, the inode is then freed and may also be destroyed. </p>
<p> Consequently, <code>iput</code> can sleep.</p>
<h2>Copyright</h2>
