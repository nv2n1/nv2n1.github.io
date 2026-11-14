---
title: "draw_character_ex(3)"
name: "draw_character_ex"
section: "3"
letter: "d"
url: "/docs/linux/man/3-draw_character_ex/"
description: "draw_character_ex – Draws non transparent pixels of the sprite with a color. Allegro game programming library."
---

<h2>NAME</h2>
<p> draw_character_ex &#8211; Draws non transparent pixels of the sprite with a color. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void draw_character_ex(BITMAP *bmp, BITMAP *sprite, int x, int y,</code> <code>color, bg);</code></p>
<h2>DESCRIPTION</h2>
<p> Draws a copy of the sprite bitmap onto the destination bitmap at the specified position, drawing transparent pixels in the background color (or skipping them if the background color is -1) and setting all other pixels to the specified color. Transparent pixels are marked by a zero in 256-color modes or bright pink for truecolor data (maximum red and blue, zero green). The sprite must be an 8-bit image, even if the destination is a truecolor bitmap. Example: </p>
<pre>
   BITMAP *logo;
   ...
   /* Draw the logo silhouette in red. */
   draw_character_ex(screen, logo, SCREEN_W / 2, SCREEN_H / 2,
                     makecol(255, 0, 0), -1);
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-draw_sprite/">draw_sprite</a></code>(3), <code><a href="/docs/linux/man/3-bitmap_mask_color/">bitmap_mask_color</a></code>(3) </p>
<h2>Index</h2>
