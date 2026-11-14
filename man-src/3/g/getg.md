---
title: "getg(3)"
name: "getg"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getg/"
description: "getr, getg, getb, geta – Extract a color component from the current pixel format. Allegro game programming library."
---

<h2>NAME</h2>
<p> getr, getg, getb, geta &#8211; Extract a color component from the current pixel format. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int getr(int c);</code> </p>
<p> <code>int getg(int c);</code> </p>
<p> <code>int getb(int c);</code> </p>
<p> <code>int geta(int c);</code></p>
<h2>DESCRIPTION</h2>
<p> Given a color in the format being used by the current video mode, these functions extract one of the red, green, blue, or alpha components (ranging 0-255), calling the preceding 8, 15, 16, 24, or 32-bit get functions as appropriate. The alpha part is only meaningful for 32-bit pixels. Example: </p>
<pre><code>
int r, g, b, color_value;

color_value = getpixel(screen, 100, 100);
r = getr(color_value);
g = getg(color_value);
b = getb(color_value);
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-getr8/">getr8</a></code>(3), <code><a href="/docs/linux/man/3-getr_depth/">getr_depth</a></code>(3), <code><a href="/docs/linux/man/3-makecol/">makecol</a></code>(3), <code><a href="/docs/linux/man/3-set_color_depth/">set_color_depth</a></code>(3), <code><a href="/docs/linux/man/3-exalpha/">exalpha</a></code>(3) </p>
<h2>Index</h2>
