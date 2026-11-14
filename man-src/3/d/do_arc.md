---
title: "do_arc(3)"
name: "do_arc"
section: "3"
letter: "d"
url: "/docs/linux/man/3-do_arc/"
description: "do_arc – Calculates all the points in a circular arc. Allegro game programming library."
---

<h2>NAME</h2>
<p> do_arc &#8211; Calculates all the points in a circular arc. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void do_arc(BITMAP *bmp, int x, int y, fixed a1, fixed a2, int r, int d,</code> <code>void (*proc)(BITMAP *bmp, int x, int y, int d));</code></p>
<h2>DESCRIPTION</h2>
<p> Calculates all the points in a circular arc around point (x, y) with radius r, calling the supplied function for each one. This will be passed a copy of the bmp parameter, the x and y position, and a copy of the d parameter, so it is suitable for use with putpixel(). The arc will be plotted in an anticlockwise direction starting from the angle a1 and ending when it reaches a2. These values are specified in 16.16 fixed point format, with 256 equal to a full circle, 64 a right angle, etc. Zero is to the right of the centre point, and larger values rotate anticlockwise from there. Example: </p>
<pre><code>
void draw_explosion_ring(BITMAP *bmp, int x, int y, int d){
    ...} do_arc(screen, SCREEN_W / 2, SCREEN_H / 2,
                itofix(-21), itofix(43), 50, flame_color,
                draw_explosion_ring);
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-do_circle/">do_circle</a></code>(3), <code><a href="/docs/linux/man/3-do_ellipse/">do_ellipse</a></code>(3), <code><a href="/docs/linux/man/3-do_line/">do_line</a></code>(3), <code><a href="/docs/linux/man/3-arc/">arc</a></code>(3) </p>
<h2>Index</h2>
