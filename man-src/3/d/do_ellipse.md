---
title: "do_ellipse(3)"
name: "do_ellipse"
section: "3"
letter: "d"
url: "/docs/linux/man/3-do_ellipse/"
description: "do_ellipse – Calculates all the points in an ellipse. Allegro game programming library."
---

<h2>NAME</h2>
<p> do_ellipse &#8211; Calculates all the points in an ellipse. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void do_ellipse(BITMAP *bmp, int x, int y, int rx, ry, int d,</code> <code>void (*proc)(BITMAP *bmp, int x, int y, int d));</code></p>
<h2>DESCRIPTION</h2>
<p> Calculates all the points in an ellipse around point (x, y) with radius rx and ry, calling the supplied function for each one. This will be passed a copy of the bmp parameter, the x and y position, and a copy of the d parameter, so it is suitable for use with putpixel(). Example: </p>
<pre><code>
void draw_explosion_ring(BITMAP *bmp, int x, int y, int d){
    ...}

do_ellipse(screen, SCREEN_W / 2, SCREEN_H / 2,
           SCREEN_H / 16, SCREEN_H / 32, flame_color,
           draw_explosion_ring);
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-do_circle/">do_circle</a></code>(3), <code><a href="/docs/linux/man/3-do_arc/">do_arc</a></code>(3), <code><a href="/docs/linux/man/3-do_line/">do_line</a></code>(3), <code><a href="/docs/linux/man/3-ellipse/">ellipse</a></code>(3), <code><a href="/docs/linux/man/3-ellipsefill/">ellipsefill</a></code>(3) </p>
<h2>Index</h2>
