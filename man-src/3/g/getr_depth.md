---
title: "getr_depth(3)"
name: "getr_depth"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getr_depth/"
description: "getr_depth, getg_depth, getb_depth, geta_depth – Extract a color component from a color in a specified pixel format. Allegro game programming library."
---

<h2>NAME</h2>
<p> getr_depth, getg_depth, getb_depth, geta_depth &#8211; Extract a color component from a color in a specified pixel format. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int getr_depth(int color_depth, int c);</code> </p>
<p> <code>int getg_depth(int color_depth, int c);</code> </p>
<p> <code>int getb_depth(int color_depth, int c);</code> </p>
<p> <code>int geta_depth(int color_depth, int c);</code></p>
<h2>DESCRIPTION</h2>
<p> Given a color in the format being used by the specified color depth, these functions extract one of the red, green, blue, or alpha components (ranging 0-255). The alpha part is only meaningful for 32-bit pixels. Example: </p>
<pre><code>
int r, g, b, color_value, bpp;

bpp = bitmap_color_depth(bitmap);
color_value = getpixel(bitmap, 100, 100);
r = getr_depth(bpp, color_value);
g = getg_depth(bpp, color_value);
b = getb_depth(bpp, color_value);
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-getr/">getr</a></code>(3), <code><a href="/docs/linux/man/3-getr8/">getr8</a></code>(3), <code><a href="/docs/linux/man/3-geta32/">geta32</a></code>(3), <code><a href="/docs/linux/man/3-makecol/">makecol</a></code>(3), <code><a href="/docs/linux/man/3-set_color_depth/">set_color_depth</a></code>(3), <code><a href="/docs/linux/man/3-exlights/">exlights</a></code>(3) </p>
<h2>Index</h2>
