---
title: "pagecache_get_page(9)"
name: "pagecache_get_page"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pagecache_get_page/"
description: "pagecache_get_page – find and get a page reference"
---

<p>pagecache_get_page &#8211; find and get a page reference</p>
<h2>Synopsis</h2>
<pre><code>struct page *pagecache_get_page(struct address_space *mapping, pgoff_t offset, int fgp_flags, gfp_t gfp_mask);</code></pre>
<h2>Arguments</h2>
<p><i>mapping</i></p>
<dl>
<dd>
<dd>the address_space to search</dl>
<p> <i>offset</i></p>
<dl>
<dd>the page index</dl>
<p> <i>fgp_flags</i></p>
<dl>
<dd>PCG flags</dl>
<p> <i>gfp_mask</i></p>
<dl>
<dd>gfp mask to use for the page cache data page allocation</dl>
<h2>Description</h2>
<p>Looks up the page cache slot at <i>mapping</i> &amp; <i>offset</i>. </p>
<p> PCG flags modify how the page is returned. </p>
<p> FGP_ACCESSED: the page will be marked accessed FGP_LOCK: Page is return locked FGP_CREAT: If page is not present then a new page is allocated using <i>gfp_mask</i> and added to the page cache and the VM&#8217;s LRU list. The page is returned locked and with an increased refcount. Otherwise, <code>NULL</code> is returned. </p>
<p> If FGP_LOCK or FGP_CREAT are specified then the function may sleep even if the GFP flags specified for FGP_CREAT are atomic. </p>
<p> If there is a page cache page, it is returned with an increased refcount.</p>
<h2>Copyright</h2>
