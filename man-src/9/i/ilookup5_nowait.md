---
title: "ilookup5_nowait(9)"
name: "ilookup5_nowait"
section: "9"
letter: "i"
url: "/docs/linux/man/9-ilookup5_nowait/"
description: "ilookup5_nowait – search for an inode in the inode cache"
---

<p>ilookup5_nowait &#8211; search for an inode in the inode cache</p>
<h2>Synopsis</h2>
<pre><code>struct inode *ilookup5_nowait(struct super_block *sb, unsigned long hashval, int (*test)(struct inode *, void *), void *data);</code></pre>
<h2>Arguments</h2>
<p><i>sb</i></p>
<dl>
<dd>
<dd>super block of file system to search</dl>
<p> <i>hashval</i></p>
<dl>
<dd>hash value (usually inode number) to search for</dl>
<p> <i>test</i></p>
<dl>
<dd>callback used for comparisons between inodes</dl>
<p> <i>data</i></p>
<dl>
<dd>opaque data pointer to pass to <i>test</i></dl>
<h2>Description</h2>
<p>Search for the inode specified by <i>hashval</i> and <i>data</i> in the inode cache. If the inode is in the cache, the inode is returned with an incremented reference count.</p>
<h2>Note</h2>
<p>I_NEW is not waited upon so you have to be very careful what you do with the returned inode. You probably should be using <code>ilookup5</code> instead. </p>
<p> Note2: <i>test</i> is called with the inode_hash_lock held, so can&#8217;t sleep.</p>
<h2>Copyright</h2>
