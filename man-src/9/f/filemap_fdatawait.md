---
title: "filemap_fdatawait(9)"
name: "filemap_fdatawait"
section: "9"
letter: "f"
url: "/docs/linux/man/9-filemap_fdatawait/"
---

filemap_fdatawait - wait for all under-writeback pages to complete

<h2>Synopsis</h2>

<pre><code>int filemap_fdatawait(struct address_space *mapping);</code></pre>

<h2>Arguments</h2>

<i>mapping</i>
<dl><dd><dd>address space structure to wait for</dl>

<h2>Description</h2>

Walk the list of under-writeback pages of the given address space and wait for all of them. Check error status of the address space and return it. 

 Since the error status of the address space is cleared by this function, callers are responsible for checking the return value and handling and/or reporting the error.

<h2>Copyright</h2>


