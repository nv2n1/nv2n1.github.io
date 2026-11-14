---
title: "ilookup5(9)"
name: "ilookup5"
section: "9"
letter: "i"
url: "/docs/linux/man/9-ilookup5/"
description: "ilookup5 – search for an inode in the inode cache"
---

<p>ilookup5 &#8211; search for an inode in the inode cache</p>
<h2>Synopsis</h2>
<pre><code>struct inode *ilookup5(struct super_block *sb, unsigned long hashval, int (*test)(struct inode *, void *), void *data);</code></pre>
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
<p>Search for the inode specified by <i>hashval</i> and <i>data</i> in the inode cache, and if the inode is in the cache, return the inode with an incremented reference count. Waits on I_NEW before returning the inode. returned with an incremented reference count. </p>
<p> This is a generalized version of <code>ilookup</code> for file systems where the inode number is not sufficient for unique identification of an inode.</p>
<h2>Note</h2>
<p><i>test</i> is called with the inode_hash_lock held, so can&#8217;t sleep.</p>
<h2>Copyright</h2>
