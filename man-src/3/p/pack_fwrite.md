---
title: "pack_fwrite(3)"
name: "pack_fwrite"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pack_fwrite/"
description: "pack_fwrite – Writes n bytes to the stream. Allegro game programming library."
---

<p>pack_fwrite &#8211; Writes n bytes to the stream. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

long pack_fwrite(const void *p, long n, PACKFILE *f);</code></pre>
<h2>Description</h2>
<p>Writes `n&#8217; bytes to the stream `f&#8217; from memory location pointed to by `p&#8217;.</p>
<h2>Return Value</h2>
<p>Returns the number of bytes written, which will be less than n if an error occurs. Error codes are stored in errno. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pack_fopen/">pack_fopen</a></code>(3), <code><a href="/docs/linux/man/3-pack_fopen_chunk/">pack_fopen_chunk</a></code>(3), <code><a href="/docs/linux/man/3-pack_feof/">pack_feof</a></code>(3) </p>
