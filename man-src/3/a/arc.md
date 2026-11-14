---
title: "arc(3)"
name: "arc"
section: "3"
letter: "a"
url: "/docs/linux/man/3-arc/"
description: "arc – Draws a circular arc. Allegro game programming library."
---

<h2>NAME</h2>
<p> arc &#8211; Draws a circular arc. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void arc(BITMAP *bmp, int x, y, fixed ang1, ang2, int r, int color);</code></p>
<h2>DESCRIPTION</h2>
<p> Draws a circular arc with centre x, y and radius r, in an anticlockwise direction starting from the angle a1 and ending when it reaches a2. These values are specified in 16.16 fixed point format, with 256 equal to a full circle, 64 a right angle, etc. Zero is to the right of the centre point, and larger values rotate anticlockwise from there. Example: </p>
<pre>
   /* Draw a black arc from 4 to 1 o'clock. */
   arc(screen, SCREEN_W/2, SCREEN_H/2,
       itofix(-21), itofix(43), 50, makecol(0, 0, 0));
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-circle/">circle</a></code>(3), <code><a href="/docs/linux/man/3-ellipse/">ellipse</a></code>(3), <code><a href="/docs/linux/man/3-drawing_mode/">drawing_mode</a></code>(3), <code><a href="/docs/linux/man/3-makecol/">makecol</a></code>(3) </p>
<h2>Index</h2>
