---
title: "polygon(3)"
name: "polygon"
section: "3"
letter: "p"
url: "/docs/linux/man/3-polygon/"
description: "polygon – Draws a filled polygon. Allegro game programming library."
---

<p>polygon &#8211; Draws a filled polygon. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void polygon(BITMAP *bmp, int vertices, const int *points, int color);</code></pre>
<h2>Description</h2>
<p>Draws a filled polygon with an arbitrary number of corners. Pass the number of vertices and an array containing a series of x, y points (a total of vertices*2 values). Example: </p>
<pre><code>int points[12] = {50, 50, 100, 100, 100, 150,
                  50, 200, 0, 150, 0, 100};
... clear_to_color(screen, makecol(255, 255, 255));
polygon(screen, 6, points, makecol(0, 0, 0));
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-triangle/">triangle</a></code>(3), <code><a href="/docs/linux/man/3-polygon3d/">polygon3d</a></code>(3), <code><a href="/docs/linux/man/3-drawing_mode/">drawing_mode</a></code>(3), <code><a href="/docs/linux/man/3-makecol/">makecol</a></code>(3), <code><a href="/docs/linux/man/3-excamera/">excamera</a></code>(3) </p>
