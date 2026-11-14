---
title: "draw_sprite_vh_flip(3)"
name: "draw_sprite_vh_flip"
section: "3"
letter: "d"
url: "/docs/linux/man/3-draw_sprite_vh_flip/"
description: "draw_sprite_v_flip, draw_sprite_h_flip, draw_sprite_vh_flip – Draws the sprite transformed to the destination bitmap. Allegro game programming library."
---

<h2>NAME</h2>
<p> draw_sprite_v_flip, draw_sprite_h_flip, draw_sprite_vh_flip &#8211; Draws the sprite transformed to the destination bitmap. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void draw_sprite_v_flip(BITMAP *bmp, BITMAP *sprite, int x, int y);</code> </p>
<p> <code>void draw_sprite_h_flip(BITMAP *bmp, BITMAP *sprite, int x, int y);</code> </p>
<p> <code>void draw_sprite_vh_flip(BITMAP *bmp, BITMAP *sprite, int x, int y);</code></p>
<h2>DESCRIPTION</h2>
<p> These are like draw_sprite(), but they additionally flip the image vertically, horizontally, or both, respectively. Flipping vertically means that the y-axis is reversed, while flipping horizontally means that the x-axis is reversed, between the source and the destination. This produces exact mirror images, which is not the same as rotating the sprite (and it is a lot faster than the rotation routine). The sprite must be a memory bitmap. Example: </p>
<pre><code>
if (key[KEY_RIGHT])
    draw_sprite(screen, hero_right, pos_x, pos_y);
else if (key[KEY_LEFT])
    draw_sprite_h_flip(screen, hero_right, pos_x, pos_y);
else
    draw_sprite(screen, hero_idle, pos_x, pos_y);
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-draw_sprite/">draw_sprite</a></code>(3), <code><a href="/docs/linux/man/3-bitmap_mask_color/">bitmap_mask_color</a></code>(3), <code><a href="/docs/linux/man/3-exsprite/">exsprite</a></code>(3) </p>
<h2>Index</h2>
