---
title: "filemap_write_and_wait_range(9)"
name: "filemap_write_and_wait_range"
section: "9"
letter: "f"
url: "/docs/linux/man/9-filemap_write_and_wait_range/"
---

filemap_write_and_wait_range - write out &amp; wait on a file range

<h2>Synopsis</h2>

<pre><code>int filemap_write_and_wait_range(struct address_space *mapping, loff_t lstart, loff_t lend);</code></pre>

<h2>Arguments</h2>

<i>mapping</i>
<dl><dd><dd>the address_space for the pages</dl>
 

 <i>lstart</i>
<dl><dd>offset in bytes where the range starts</dl>
 

 <i>lend</i>
<dl><dd>offset in bytes where the range ends (inclusive)</dl>

<h2>Description</h2>

Write out and wait upon file offsets lstart-&gt;lend, inclusive. 

 Note that `lend' is inclusive (describes the last byte to be written) so that this function can be used to write to the very end-of-file (end = -1).

<h2>Copyright</h2>


