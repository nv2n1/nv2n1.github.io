---
title: "do_line(3)"
name: "do_line"
section: "3"
letter: "d"
url: "/docs/linux/man/3-do_line/"
description: "do_line – Calculates all the points along a line. Allegro game programming library."
---

<h2>NAME</h2>
<p> do_line &#8211; Calculates all the points along a line. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void do_line(BITMAP *bmp, int x1, y1, x2, y2, int d, </code> <code>void (*proc)(BITMAP *bmp, int x, int y, int d));</code></p>
<h2>DESCRIPTION</h2>
<p> Calculates all the points along a line from point (x1, y1) to (x2, y2), calling the supplied function for each one. This will be passed a copy of the bmp parameter, the x and y position, and a copy of the d parameter, so it is suitable for use with putpixel(). Example: </p>
<pre><code>
void draw_dust_particle(BITMAP *bmp, int x, int y, int d){
    ...}

do_line(screen, 0, 0, SCREEN_W - 1, SCREEN_H - 2,
        dust_strength, draw_dust_particle);
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-do_circle/">do_circle</a></code>(3), <code><a href="/docs/linux/man/3-do_ellipse/">do_ellipse</a></code>(3), <code><a href="/docs/linux/man/3-do_arc/">do_arc</a></code>(3), <code><a href="/docs/linux/man/3-line/">line</a></code>(3) </p>
<h2>Index</h2>
