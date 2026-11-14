---
title: "pack_ungetc(3)"
name: "pack_ungetc"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pack_ungetc/"
description: "pack_ungetc – Moves one single character back to the input buffer. Allegro game programming library."
---

<p>pack_ungetc &#8211; Moves one single character back to the input buffer. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int pack_ungetc(int c, PACKFILE *f);</code></pre>
<h2>Description</h2>
<p>Puts a character back to the file&#8217;s input buffer. Like with ungetc from libc, only a single push back is guaranteed. </p>
<p> Note: pack_fgets internally uses pack_ungetc, so never use pack_ungetc directly after using pack_fgets on a PACKFILE.</p>
<h2>Return Value</h2>
<p>Returns c on success, or EOF on error. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pack_getc/">pack_getc</a></code>(3), <code><a href="/docs/linux/man/3-pack_fgets/">pack_fgets</a></code>(3) </p>
