---
title: "hline(3)"
name: "hline"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hline/"
description: "hline – Draws a horizontal line onto the bitmap. Allegro game programming library."
---

<h2>NAME</h2>
<p> hline &#8211; Draws a horizontal line onto the bitmap. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void hline(BITMAP *bmp, int x1, int y, int x2, int color);</code></p>
<h2>DESCRIPTION</h2>
<p> Draws a horizontal line onto the bitmap, from point (x1, y) to (x2, y). </p>
<p> Note: hline() is implemented as an alias to another function. See ALLEGRO_NO_VHLINE_ALIAS in the `Differences between platforms&#8217; section for details. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-vline/">vline</a></code>(3), <code><a href="/docs/linux/man/3-line/">line</a></code>(3), <code><a href="/docs/linux/man/3-drawing_mode/">drawing_mode</a></code>(3), <code><a href="/docs/linux/man/3-makecol/">makecol</a></code>(3), <code><a href="/docs/linux/man/3-exsprite/">exsprite</a></code>(3) </p>
<h2>Index</h2>
