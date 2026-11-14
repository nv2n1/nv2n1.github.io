---
title: "do_circle(3)"
name: "do_circle"
section: "3"
letter: "d"
url: "/docs/linux/man/3-do_circle/"
description: "do_circle – Calculates all the points in a circle. Allegro game programming library."
---

<h2>NAME</h2>
<p> do_circle &#8211; Calculates all the points in a circle. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void do_circle(BITMAP *bmp, int x, int y, int radius, int d,</code> <code>void (*proc)(BITMAP *bmp, int x, int y, int d));</code></p>
<h2>DESCRIPTION</h2>
<p> Calculates all the points in a circle around point (x, y) with radius r, calling the supplied function for each one. This will be passed a copy of the bmp parameter, the x and y position, and a copy of the d parameter, so it is suitable for use with putpixel(). Example: </p>
<pre><code>
void draw_explosion_ring(BITMAP *bmp, int x, int y, int d){
    ...}

do_circle(screen, SCREEN_W / 2, SCREEN_H / 2,
          SCREEN_H / 16, flame_color,
          draw_explosion_ring);
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-do_ellipse/">do_ellipse</a></code>(3), <code><a href="/docs/linux/man/3-do_arc/">do_arc</a></code>(3), <code><a href="/docs/linux/man/3-do_line/">do_line</a></code>(3), <code><a href="/docs/linux/man/3-circle/">circle</a></code>(3), <code><a href="/docs/linux/man/3-circlefill/">circlefill</a></code>(3) </p>
<h2>Index</h2>
