---
title: "pack_fread(3)"
name: "pack_fread"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pack_fread/"
description: "pack_fread – Reads n bytes from the stream. Allegro game programming library."
---

<p>pack_fread &#8211; Reads n bytes from the stream. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

long pack_fread(void *p, long n, PACKFILE *f);</code></pre>
<h2>Description</h2>
<p>Reads `n&#8217; bytes from the stream `f&#8217;, storing them at the memory location pointed to by `p&#8217;. Example: </p>
<pre><code>unsigned char buf[256];
... if (pack_fread(buf, 256, input_file) != 256)
    abort_on_error(&quot;Truncated input file!&quot;);</code></pre>
<h2>Return Value</h2>
<p>Returns the number of bytes read, which will be less than `n&#8217; if EOF is reached or an error occurs. Error codes are stored in errno. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pack_fopen/">pack_fopen</a></code>(3), <code><a href="/docs/linux/man/3-pack_fopen_chunk/">pack_fopen_chunk</a></code>(3), <code><a href="/docs/linux/man/3-pack_feof/">pack_feof</a></code>(3), <code><a href="/docs/linux/man/3-expackf/">expackf</a></code>(3) </p>
