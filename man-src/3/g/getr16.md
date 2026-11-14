---
title: "getr16(3)"
name: "getr16"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getr16/"
description: "getr8, getg8, getb8, getr15, getg15, getb15, getr16, getg16, getb16, getr24, getg24, getb24, getr32, getg32, getb32 – Extract a color component from the specified pixel format. Allegro game program..."
---

<h2>NAME</h2>
<p> getr8, getg8, getb8, getr15, getg15, getb15, getr16, getg16, getb16, getr24, getg24, getb24, getr32, getg32, getb32 &#8211; Extract a color component from the specified pixel format. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int getr8(int c);</code> </p>
<p> <code>int getg8(int c);</code> </p>
<p> <code>int getb8(int c);</code> </p>
<p> <code>int getr15(int c);</code> </p>
<p> <code>int getg15(int c);</code> </p>
<p> <code>int getb15(int c);</code> </p>
<p> <code>int getr16(int c);</code> </p>
<p> <code>int getg16(int c);</code> </p>
<p> <code>int getb16(int c);</code> </p>
<p> <code>int getr24(int c);</code> </p>
<p> <code>int getg24(int c);</code> </p>
<p> <code>int getb24(int c);</code> </p>
<p> <code>int getr32(int c);</code> </p>
<p> <code>int getg32(int c);</code> </p>
<p> <code>int getb32(int c);</code></p>
<h2>DESCRIPTION</h2>
<p> Given a color in a display dependent format, these functions extract one of the red, green, or blue components (ranging 0-255). Example: </p>
<pre><code>
int r, g, b, color_value;

color_value = _getpixel15(screen, 100, 100);
r = getr15(color_value);
g = getg15(color_value);
b = getb15(color_value);
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-geta32/">geta32</a></code>(3), <code><a href="/docs/linux/man/3-getr/">getr</a></code>(3), <code><a href="/docs/linux/man/3-getr_depth/">getr_depth</a></code>(3), <code><a href="/docs/linux/man/3-makecol/">makecol</a></code>(3), <code><a href="/docs/linux/man/3-set_color_depth/">set_color_depth</a></code>(3) </p>
<h2>Index</h2>
