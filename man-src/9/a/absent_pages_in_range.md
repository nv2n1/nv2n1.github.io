---
title: "absent_pages_in_range(9)"
name: "absent_pages_in_range"
section: "9"
letter: "a"
url: "/docs/linux/man/9-absent_pages_in_range/"
---

absent_pages_in_range - Return number of page frames in holes within a range

<h2>Synopsis</h2>

<pre><code>unsigned long absent_pages_in_range(unsigned long start_pfn, unsigned long end_pfn);</code></pre>

<h2>Arguments</h2>

<i>start_pfn</i>
<dl><dd><dd>The start PFN to start searching for holes</dl>
 

 <i>end_pfn</i>
<dl><dd>The end PFN to stop searching for holes</dl>

<h2>Description</h2>

It returns the number of pages frames in memory holes within a range.

<h2>Copyright</h2>


