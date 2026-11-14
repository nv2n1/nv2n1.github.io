---
title: "unmap_mapping_range(9)"
name: "unmap_mapping_range"
section: "9"
letter: "u"
url: "/docs/linux/man/9-unmap_mapping_range/"
description: "unmap_mapping_range – unmap the portion of all mmaps in the specified address_space corresponding to the specified page range in the underlying file."
---

<p>unmap_mapping_range &#8211; unmap the portion of all mmaps in the specified address_space corresponding to the specified page range in the underlying file.</p>
<h2>Synopsis</h2>
<pre><code>void unmap_mapping_range(struct address_space *mapping, loff_t const holebegin, loff_t const holelen, int even_cows);</code></pre>
<h2>Arguments</h2>
<p><i>mapping</i></p>
<dl>
<dd>
<dd>the address space containing mmaps to be unmapped.</dl>
<p> <i>holebegin</i></p>
<dl>
<dd>byte in first page to unmap, relative to the start of the underlying file. This will be rounded down to a PAGE_SIZE boundary. Note that this is different from <code>truncate_pagecache</code>, which must keep the partial page. In contrast, we must get rid of partial pages.</dl>
<p> <i>holelen</i></p>
<dl>
<dd>size of prospective hole in bytes. This will be rounded up to a PAGE_SIZE boundary. A holelen of zero truncates to the end of the file.</dl>
<p> <i>even_cows</i></p>
<dl>
<dd>1 when truncating a file, unmap even private COWed pages; but 0 when invalidating pagecache, don&#8217;t throw away private data.</dl>
<h2>Copyright</h2>
