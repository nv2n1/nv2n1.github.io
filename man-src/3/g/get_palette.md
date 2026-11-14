---
title: "get_palette(3)"
name: "get_palette"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_palette/"
description: "get_palette – Retrieves the entire palette of 256 colors. Allegro game programming library."
---

<h2>NAME</h2>
<p> get_palette &#8211; Retrieves the entire palette of 256 colors. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void get_palette(PALETTE p);</code></p>
<h2>DESCRIPTION</h2>
<p> Retrieves the entire palette of 256 colors. You should provide an array of 256 RGB structures to store it in. Example: </p>
<pre><code>
PALETTE pal;
... get_palette(pal);
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-get_palette_range/">get_palette_range</a></code>(3), <code><a href="/docs/linux/man/3-get_color/">get_color</a></code>(3), <code><a href="/docs/linux/man/3-set_palette/">set_palette</a></code>(3) </p>
<h2>Index</h2>
