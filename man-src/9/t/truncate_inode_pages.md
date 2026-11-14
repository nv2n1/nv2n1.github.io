---
title: "truncate_inode_pages(9)"
name: "truncate_inode_pages"
section: "9"
letter: "t"
url: "/docs/linux/man/9-truncate_inode_pages/"
description: "truncate_inode_pages – truncate *all* the pages from an offset"
---

<p>truncate_inode_pages &#8211; truncate *all* the pages from an offset</p>
<h2>Synopsis</h2>
<pre><code>void truncate_inode_pages(struct address_space *mapping, loff_t lstart);</code></pre>
<h2>Arguments</h2>
<p><i>mapping</i></p>
<dl>
<dd>
<dd>mapping to truncate</dl>
<p> <i>lstart</i></p>
<dl>
<dd>offset from which to truncate</dl>
<h2>Description</h2>
<p>Called under (and serialised by) inode-&gt;i_mutex.</p>
<h2>Note</h2>
<p>When this function returns, there can be a page in the process of deletion (inside <code>__delete_from_page_cache</code>) in the specified range. Thus mapping-&gt;nrpages can be non-zero when this function returns even after truncation of the whole mapping.</p>
<h2>Copyright</h2>
