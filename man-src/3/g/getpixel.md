---
title: "getpixel(3)"
name: "getpixel"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getpixel/"
description: "getpixel – Reads a pixel from a bitmap. Allegro game programming library."
---

<h2>NAME</h2>
<p> getpixel &#8211; Reads a pixel from a bitmap. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int getpixel(BITMAP *bmp, int x, int y);</code></p>
<h2>DESCRIPTION</h2>
<p> Reads a pixel from point (x, y) in the bitmap.</p>
<h2>RETURN VALUE</h2>
<p> Returns -1 if the point lies outside the bitmap (ignoring the clipping rectangle), otherwise the value of the pixel in the color format of the bitmap. </p>
<p> Warning: -1 is also a valid value for pixels contained in 32-bit bitmaps with alpha channel (when R,G,B,A are all equal to 255) so you can&#8217;t use the test against -1 as a predicate for such bitmaps. In this cases, the only reliable predicate is is_inside_bitmap(). </p>
<p> To extract the individual color components, use the getr() / getg() / getb() / geta() family of functions. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-putpixel/">putpixel</a></code>(3), <code><a href="/docs/linux/man/3-_getpixel/">_getpixel</a></code>(3), <code><a href="/docs/linux/man/3-is_inside_bitmap/">is_inside_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-getr/">getr</a></code>(3), <code><a href="/docs/linux/man/3-getg/">getg</a></code>(3), <code><a href="/docs/linux/man/3-getb/">getb</a></code>(3), <code><a href="/docs/linux/man/3-geta/">geta</a></code>(3), <code><a href="/docs/linux/man/3-ex12bit/">ex12bit</a></code>(3), <code><a href="/docs/linux/man/3-exalpha/">exalpha</a></code>(3), <code><a href="/docs/linux/man/3-exflame/">exflame</a></code>(3), <code><a href="/docs/linux/man/3-exlights/">exlights</a></code>(3) </p>
<h2>Index</h2>
