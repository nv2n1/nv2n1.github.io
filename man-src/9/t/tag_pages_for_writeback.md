---
title: "tag_pages_for_writeback(9)"
name: "tag_pages_for_writeback"
section: "9"
letter: "t"
url: "/docs/linux/man/9-tag_pages_for_writeback/"
---

tag_pages_for_writeback - tag pages to be written by write_cache_pages

<h2>Synopsis</h2>

<pre><code>void tag_pages_for_writeback(struct address_space *mapping, pgoff_t start, pgoff_t end);</code></pre>

<h2>Arguments</h2>

<i>mapping</i>
<dl><dd><dd>address space structure to write</dl>
 

 <i>start</i>
<dl><dd>starting page index</dl>
 

 <i>end</i>
<dl><dd>ending page index (inclusive)</dl>

<h2>Description</h2>

This function scans the page range from <i>start</i> to <i>end</i> (inclusive) and tags all pages that have DIRTY tag set with a special TOWRITE tag. The idea is that write_cache_pages (or whoever calls this function) will then use TOWRITE tag to identify pages eligible for writeback. This mechanism is used to avoid livelocking of writeback by a process steadily creating new dirty pages in the file (thus it is important for this function to be quick so that it can tag pages faster than a dirtying process can create them).

<h2>Copyright</h2>


