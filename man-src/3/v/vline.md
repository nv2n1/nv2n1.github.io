---
title: "vline(3)"
name: "vline"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vline/"
description: "vline – Draws a vertical line onto the bitmap. Allegro game programming library."
---

<p>vline &#8211; Draws a vertical line onto the bitmap. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void vline(BITMAP *bmp, int x, int y1, int y2, int color);</code></pre>
<h2>Description</h2>
<p>Draws a vertical line onto the bitmap, from point (x, y1) to (x, y2). Note: vline() is implemented as an alias to another function. See ALLEGRO_NO_VHLINE_ALIAS in the `Differences between platforms&#8217; section for details. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-hline/">hline</a></code>(3), <code><a href="/docs/linux/man/3-line/">line</a></code>(3), <code><a href="/docs/linux/man/3-drawing_mode/">drawing_mode</a></code>(3), <code><a href="/docs/linux/man/3-makecol/">makecol</a></code>(3), <code><a href="/docs/linux/man/3-exrgbhsv/">exrgbhsv</a></code>(3), <code><a href="/docs/linux/man/3-exscroll/">exscroll</a></code>(3), <code><a href="/docs/linux/man/3-extruec/">extruec</a></code>(3) </p>
