---
title: "mark_buffer_dirty(9)"
name: "mark_buffer_dirty"
section: "9"
letter: "m"
url: "/docs/linux/man/9-mark_buffer_dirty/"
description: "mark_buffer_dirty – mark a buffer_head as needing writeout"
---

<p>mark_buffer_dirty &#8211; mark a buffer_head as needing writeout</p>
<h2>Synopsis</h2>
<pre><code>void mark_buffer_dirty(struct buffer_head *bh);</code></pre>
<h2>Arguments</h2>
<p><i>bh</i></p>
<dl>
<dd>
<dd>the buffer_head to mark dirty</dl>
<h2>Description</h2>
<p><code>mark_buffer_dirty</code> will set the dirty bit against the buffer, then set its backing page dirty, then tag the page as dirty in its address_space&#8217;s radix tree and then attach the address_space&#8217;s inode to its superblock&#8217;s dirty inode list. </p>
<p> <code>mark_buffer_dirty</code> is atomic. It takes bh-&gt;b_page-&gt;mapping-&gt;private_lock, mapping-&gt;tree_lock and mapping-&gt;host-&gt;i_lock.</p>
<h2>Copyright</h2>
