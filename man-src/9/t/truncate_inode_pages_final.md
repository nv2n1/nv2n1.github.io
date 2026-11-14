---
title: "truncate_inode_pages_final(9)"
name: "truncate_inode_pages_final"
section: "9"
letter: "t"
url: "/docs/linux/man/9-truncate_inode_pages_final/"
---

truncate_inode_pages_final - truncate *all* pages before inode dies

<h2>Synopsis</h2>

<pre><code>void truncate_inode_pages_final(struct address_space *mapping);</code></pre>

<h2>Arguments</h2>

<i>mapping</i>
<dl><dd><dd>mapping to truncate</dl>

<h2>Description</h2>

Called under (and serialized by) inode-&gt;i_mutex. 

 Filesystems have to use this in the .evict_inode path to inform the VM that this is the final truncate and the inode is going away.

<h2>Copyright</h2>


