---
title: "truncate_pagecache_range(9)"
name: "truncate_pagecache_range"
section: "9"
letter: "t"
url: "/docs/linux/man/9-truncate_pagecache_range/"
---

truncate_pagecache_range - unmap and remove pagecache that is hole-punched

<h2>Synopsis</h2>

<pre><code>void truncate_pagecache_range(struct inode *inode, loff_t lstart, loff_t lend);</code></pre>

<h2>Arguments</h2>

<i>inode</i>
<dl><dd><dd>inode</dl>
 

 <i>lstart</i>
<dl><dd>offset of beginning of hole</dl>
 

 <i>lend</i>
<dl><dd>offset of last byte of hole</dl>

<h2>Description</h2>

This function should typically be called before the filesystem releases resources associated with the freed range (eg. deallocates blocks). This way, pagecache will always stay logically coherent with on-disk format, and the filesystem would not have to deal with situations such as writepage being called for a page that has already had its underlying blocks deallocated.

<h2>Copyright</h2>


