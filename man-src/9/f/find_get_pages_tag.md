---
title: "find_get_pages_tag(9)"
name: "find_get_pages_tag"
section: "9"
letter: "f"
url: "/docs/linux/man/9-find_get_pages_tag/"
---

find_get_pages_tag - find and return pages that match <i>tag</i>

<h2>Synopsis</h2>

<pre><code>unsigned find_get_pages_tag(struct address_space *mapping, pgoff_t *index, int tag, unsigned int nr_pages, struct page **pages);</code></pre>

<h2>Arguments</h2>

<i>mapping</i>
<dl><dd><dd>the address_space to search</dl>
 

 <i>index</i>
<dl><dd>the starting page index</dl>
 

 <i>tag</i>
<dl><dd>the tag index</dl>
 

 <i>nr_pages</i>
<dl><dd>the maximum number of pages</dl>
 

 <i>pages</i>
<dl><dd>where the resulting pages are placed</dl>

<h2>Description</h2>

Like find_get_pages, except we only return pages which are tagged with <i>tag</i>. We update <i>index</i> to index the next page for the traversal.

<h2>Copyright</h2>


