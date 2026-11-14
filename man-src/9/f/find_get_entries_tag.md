---
title: "find_get_entries_tag(9)"
name: "find_get_entries_tag"
section: "9"
letter: "f"
url: "/docs/linux/man/9-find_get_entries_tag/"
---

find_get_entries_tag - find and return entries that match <i>tag</i>

<h2>Synopsis</h2>

<pre><code>unsigned find_get_entries_tag(struct address_space *mapping, pgoff_t start, int tag, unsigned int nr_entries, struct page **entries, pgoff_t *indices);</code></pre>

<h2>Arguments</h2>

<i>mapping</i>
<dl><dd><dd>the address_space to search</dl>
 

 <i>start</i>
<dl><dd>the starting page cache index</dl>
 

 <i>tag</i>
<dl><dd>the tag index</dl>
 

 <i>nr_entries</i>
<dl><dd>the maximum number of entries</dl>
 

 <i>entries</i>
<dl><dd>where the resulting entries are placed</dl>
 

 <i>indices</i>
<dl><dd>the cache indices corresponding to the entries in <i>entries</i></dl>

<h2>Description</h2>

Like find_get_entries, except we only return entries which are tagged with <i>tag</i>.

<h2>Copyright</h2>


