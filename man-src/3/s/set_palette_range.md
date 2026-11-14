---
title: "set_palette_range(3)"
name: "set_palette_range"
section: "3"
letter: "s"
url: "/docs/linux/man/3-set_palette_range/"
description: "set_palette_range – Sets a specific range of the palette. Allegro game programming library."
---

<p>set_palette_range &#8211; Sets a specific range of the palette. Allegro game programming library.</p>
<h2>Synopsis</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void set_palette_range(const PALETTE p, int from, int to, int vsync);</code></p>
<h2>Description</h2>
<p> Sets the palette entries between from and to (inclusive: pass 0 and 255 to set the entire palette). If vsync is set it waits for the vertical retrace, otherwise it sets the colors immediately. Example: </p>
<pre>
   PALETTE palette;
   ...
   /* Modify the first 16 entries. */
   change_first_16_colors(palette);
   /* Now update them waiting for vsync. */
   set_palette_range(palette, 0, 15, 1);
</pre>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/3-set_palette/">set_palette</a></code>(3), <code><a href="/docs/linux/man/3-get_palette_range/">get_palette_range</a></code>(3), <code><a href="/docs/linux/man/3-exzbuf/">exzbuf</a></code>(3)</p>
