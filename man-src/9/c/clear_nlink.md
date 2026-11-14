---
title: "clear_nlink(9)"
name: "clear_nlink"
section: "9"
letter: "c"
url: "/docs/linux/man/9-clear_nlink/"
description: "clear_nlink – directly zero an inode’s link count"
---

<p>clear_nlink &#8211; directly zero an inode&#8217;s link count</p>
<h2>Synopsis</h2>
<pre><code>void clear_nlink(struct inode *inode);</code></pre>
<h2>Arguments</h2>
<p><i>inode</i></p>
<dl>
<dd>
<dd>inode</dl>
<h2>Description</h2>
<p>This is a low-level filesystem helper to replace any direct filesystem manipulation of i_nlink. See <code>drop_nlink</code> for why we care about i_nlink hitting zero.</p>
<h2>Copyright</h2>
