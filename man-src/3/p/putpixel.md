---
title: "putpixel(3)"
name: "putpixel"
section: "3"
letter: "p"
url: "/docs/linux/man/3-putpixel/"
description: "putpixel – Writes a pixel into a bitmap. Allegro game programming library."
---

<p>putpixel &#8211; Writes a pixel into a bitmap. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void putpixel(BITMAP *bmp, int x, int y, int color);</code></pre>
<h2>Description</h2>
<p>Writes a pixel to the specified position in the bitmap, using the current drawing mode and the bitmap&#8217;s clipping rectangle. Example: </p>
<pre> putpixel(screen, 10, 30, some_color);</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-getpixel/">getpixel</a></code>(3), <code><a href="/docs/linux/man/3-_putpixel/">_putpixel</a></code>(3), <code><a href="/docs/linux/man/3-drawing_mode/">drawing_mode</a></code>(3), <code><a href="/docs/linux/man/3-makecol/">makecol</a></code>(3), <code><a href="/docs/linux/man/3-ex12bit/">ex12bit</a></code>(3), <code><a href="/docs/linux/man/3-exalpha/">exalpha</a></code>(3), <code><a href="/docs/linux/man/3-exflame/">exflame</a></code>(3), <code><a href="/docs/linux/man/3-exjoy/">exjoy</a></code>(3), <code><a href="/docs/linux/man/3-exstars/">exstars</a></code>(3), <code><a href="/docs/linux/man/3-exswitch/">exswitch</a></code>(3) </p>
