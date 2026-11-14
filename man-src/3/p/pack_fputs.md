---
title: "pack_fputs(3)"
name: "pack_fputs"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pack_fputs/"
description: "pack_fputs – Writes a string to the stream. Allegro game programming library."
---

<p>pack_fputs &#8211; Writes a string to the stream. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int pack_fputs(const char *p, PACKFILE *f);</code></pre>
<h2>Description</h2>
<p>Writes a string to the stream `f&#8217;. The input string is converted from the current text encoding format to UTF-8 before writing. Newline characters are written as `
&#8217; on DOS and Windows platforms. If you don&#8217;t want this behaviour, use pack_fwrite() and/or pack_putc() instead.</p>
<h2>Return Value</h2>
<p>Returns zero on success or a negative number on error. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pack_fopen/">pack_fopen</a></code>(3), <code><a href="/docs/linux/man/3-pack_fopen_chunk/">pack_fopen_chunk</a></code>(3), <code><a href="/docs/linux/man/3-pack_fwrite/">pack_fwrite</a></code>(3), <code><a href="/docs/linux/man/3-pack_putc/">pack_putc</a></code>(3) </p>
