---
title: "set_palette(3)"
name: "set_palette"
section: "3"
letter: "s"
url: "/docs/linux/man/3-set_palette/"
description: "set_palette – Sets the entire palette of 256 colors. Allegro game programming library."
---

<p>set_palette &#8211; Sets the entire palette of 256 colors. Allegro game programming library.</p>
<h2>Synopsis</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void set_palette(const PALETTE p);</code></p>
<h2>Description</h2>
<p> Sets the entire palette of 256 colors. You should provide an array of 256 RGB structures. Unlike set_color(), there is no need to call vsync() before this function. Example: </p>
<pre>
   BITMAP *bmp;
   PALETTE palette;
   ...
   bmp = load_bitmap(filename, palette);
   if (!bmp)
      abort_on_error(&quot;Couldn't load bitmap!&quot;);
   set_palette(palette);
</pre>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/3-set_gfx_mode/">set_gfx_mode</a></code>(3), <code><a href="/docs/linux/man/3-set_palette_range/">set_palette_range</a></code>(3), <code><a href="/docs/linux/man/3-set_color/">set_color</a></code>(3), <code><a href="/docs/linux/man/3-get_palette/">get_palette</a></code>(3), <code><a href="/docs/linux/man/3-select_palette/">select_palette</a></code>(3), <code><a href="/docs/linux/man/3-palette_color/">palette_color</a></code>(3)</p>
