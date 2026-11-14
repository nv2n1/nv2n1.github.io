---
title: "rotate_sprite(3)"
name: "rotate_sprite"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rotate_sprite/"
description: "rotate_sprite – Rotates a sprite. Allegro game programming library."
---

<p>rotate_sprite &#8211; Rotates a sprite. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void rotate_sprite(BITMAP *bmp, BITMAP *sprite, int x, int y, fixed angle);</code></pre>
<h2>Description</h2>
<p>Draws the sprite image onto the bitmap. It is placed with its top left corner at the specified position, then rotated by the specified angle around its centre. The angle is a fixed point 16.16 number in the same format used by the fixed point trig routines, with 256 equal to a full circle, 64 a right angle, etc. All rotation functions can draw between any two bitmaps, even screen bitmaps or bitmaps of different color depth. Positive increments of the angle will make the sprite rotate clockwise on the screen, as demonstrated by the Allegro example. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-draw_sprite/">draw_sprite</a></code>(3), <code><a href="/docs/linux/man/3-rotate_scaled_sprite/">rotate_scaled_sprite</a></code>(3), <code><a href="/docs/linux/man/3-rotate_sprite_v_flip/">rotate_sprite_v_flip</a></code>(3), <code><a href="/docs/linux/man/3-rotate_scaled_sprite_v_flip/">rotate_scaled_sprite_v_flip</a></code>(3), <code><a href="/docs/linux/man/3-pivot_sprite/">pivot_sprite</a></code>(3), <code><a href="/docs/linux/man/3-pivot_sprite_v_flip/">pivot_sprite_v_flip</a></code>(3), <code><a href="/docs/linux/man/3-pivot_scaled_sprite/">pivot_scaled_sprite</a></code>(3), <code><a href="/docs/linux/man/3-pivot_scaled_sprite_v_flip/">pivot_scaled_sprite_v_flip</a></code>(3), <code><a href="/docs/linux/man/3-itofix/">itofix</a></code>(3), <code><a href="/docs/linux/man/3-exsprite/">exsprite</a></code>(3) </p>
