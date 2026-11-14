---
title: "truncate_setsize(9)"
name: "truncate_setsize"
section: "9"
letter: "t"
url: "/docs/linux/man/9-truncate_setsize/"
---

truncate_setsize - update inode and pagecache for a new file size

<h2>Synopsis</h2>

<pre><code>void truncate_setsize(struct inode *inode, loff_t newsize);</code></pre>

<h2>Arguments</h2>

<i>inode</i>
<dl><dd><dd>inode</dl>
 

 <i>newsize</i>
<dl><dd>new file size</dl>

<h2>Description</h2>

truncate_setsize updates i_size and performs pagecache truncation (if necessary) to <i>newsize</i>. It will be typically be called from the filesystem's setattr function when ATTR_SIZE is passed in. 

 Must be called with a lock serializing truncates and writes (generally i_mutex but e.g. xfs uses a different lock) and before all filesystem specific block truncation has been performed.

<h2>Copyright</h2>


