---
title: "pack_feof(3)"
name: "pack_feof"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pack_feof/"
description: "pack_feof – Returns nonzero as soon as you reach the end of the file. Allegro game programming library."
---

<p>pack_feof &#8211; Returns nonzero as soon as you reach the end of the file. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int pack_feof(PACKFILE *f);</code></pre>
<h2>Description</h2>
<p>Finds out if you have reached the end of the file. It does not wait for you to attempt to read beyond the end of the file, contrary to the ISO C feof() function. The only way to know whether you have read beyond the end of the file is to check the return value of the read operation you use (and be wary of pack_*getl() as EOF is also a valid return value with these functions).</p>
<h2>Return Value</h2>
<p>Returns non-zero if you are at the end of the file, zero otherwise. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pack_fopen/">pack_fopen</a></code>(3), <code><a href="/docs/linux/man/3-pack_fopen_chunk/">pack_fopen_chunk</a></code>(3), <code><a href="/docs/linux/man/3-pack_ferror/">pack_ferror</a></code>(3) </p>
