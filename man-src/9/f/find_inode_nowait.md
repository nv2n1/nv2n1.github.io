---
title: "find_inode_nowait(9)"
name: "find_inode_nowait"
section: "9"
letter: "f"
url: "/docs/linux/man/9-find_inode_nowait/"
description: "find_inode_nowait – find an inode in the inode cache"
---

<p>find_inode_nowait &#8211; find an inode in the inode cache</p>
<h2>Synopsis</h2>
<pre><code>struct inode *find_inode_nowait(struct super_block *sb, unsigned long hashval, int (*match)(struct inode *, unsigned long, void *), void *data);</code></pre>
<h2>Arguments</h2>
<p><i>sb</i></p>
<dl>
<dd>
<dd>super block of file system to search</dl>
<p> <i>hashval</i></p>
<dl>
<dd>hash value (usually inode number) to search for</dl>
<p> <i>match</i></p>
<dl>
<dd>callback used for comparisons between inodes</dl>
<p> <i>data</i></p>
<dl>
<dd>opaque data pointer to pass to <i>match</i></dl>
<h2>Description</h2>
<p>Search for the inode specified by <i>hashval</i> and <i>data</i> in the inode cache, where the helper function <i>match</i> will return 0 if the inode does not match, 1 if the inode does match, and -1 if the search should be stopped. The <i>match</i> function must be responsible for taking the i_lock spin_lock and checking i_state for an inode being freed or being initialized, and incrementing the reference count before returning 1. It also must not sleep, since it is called with the inode_hash_lock spinlock held. </p>
<p> This is a even more generalized version of <code>ilookup5</code> when the function must never block &#8212; <code>find_inode</code> can block in <code>__wait_on_freeing_inode</code> &#8212; or when the caller can not increment the reference count because the resulting <code>iput</code> might cause an inode eviction. The tradeoff is that the <i>match</i> funtion must be very carefully implemented.</p>
<h2>Copyright</h2>
