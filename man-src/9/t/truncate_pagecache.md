---
title: "truncate_pagecache(9)"
name: "truncate_pagecache"
section: "9"
letter: "t"
url: "/docs/linux/man/9-truncate_pagecache/"
---

truncate_pagecache - unmap and remove pagecache that has been truncated

<h2>Synopsis</h2>

<pre><code>void truncate_pagecache(struct inode *inode, loff_t newsize);</code></pre>

<h2>Arguments</h2>

<i>inode</i>
<dl><dd><dd>inode</dl>
 

 <i>newsize</i>
<dl><dd>new file size</dl>

<h2>Description</h2>

inode's new i_size must already be written before truncate_pagecache is called. 

 This function should typically be called before the filesystem releases resources associated with the freed range (eg. deallocates blocks). This way, pagecache will always stay logically coherent with on-disk format, and the filesystem would not have to deal with situations such as writepage being called for a page that has already had its underlying blocks deallocated.

<h2>Copyright</h2>


