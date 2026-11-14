---
title: "find_get_pages_contig(9)"
name: "find_get_pages_contig"
section: "9"
letter: "f"
url: "/docs/linux/man/9-find_get_pages_contig/"
description: "find_get_pages_contig – gang contiguous pagecache lookup"
---

<p>find_get_pages_contig &#8211; gang contiguous pagecache lookup</p>
<h2>Synopsis</h2>
<pre><code>unsigned find_get_pages_contig(struct address_space *mapping, pgoff_t index, unsigned int nr_pages, struct page **pages);</code></pre>
<h2>Arguments</h2>
<p><i>mapping</i></p>
<dl>
<dd>
<dd>The address_space to search</dl>
<p> <i>index</i></p>
<dl>
<dd>The starting page index</dl>
<p> <i>nr_pages</i></p>
<dl>
<dd>The maximum number of pages</dl>
<p> <i>pages</i></p>
<dl>
<dd>Where the resulting pages are placed</dl>
<h2>Description</h2>
<p><code>find_get_pages_contig</code> works exactly like <code>find_get_pages</code>, except that the returned number of pages are guaranteed to be contiguous. </p>
<p> <code>find_get_pages_contig</code> returns the number of pages which were found.</p>
<h2>Copyright</h2>
