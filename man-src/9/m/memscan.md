---
title: "memscan(9)"
name: "memscan"
section: "9"
letter: "m"
url: "/docs/linux/man/9-memscan/"
---

memscan - Find a character in an area of memory.

<h2>Synopsis</h2>

<pre><code>void *memscan(void *addr, int c, size_t size);</code></pre>

<h2>Arguments</h2>

<i>addr</i>
<dl><dd><dd>The memory area</dl>
 

 <i>c</i>
<dl><dd>The byte to search for</dl>
 

 <i>size</i>
<dl><dd>The size of the area.</dl>

<h2>Description</h2>

returns the address of the first occurrence of <i>c</i>, or 1 byte past the area if <i>c</i> is not found

<h2>Copyright</h2>


