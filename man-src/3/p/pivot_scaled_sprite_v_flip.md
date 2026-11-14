---
title: "pivot_scaled_sprite_v_flip(3)"
name: "pivot_scaled_sprite_v_flip"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pivot_scaled_sprite_v_flip/"
description: "pivot_scaled_sprite_v_flip – Rotates, stretches and flips a sprite around a specified point. Allegro game programming library."
---

<p>pivot_scaled_sprite_v_flip &#8211; Rotates, stretches and flips a sprite around a specified point. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void pivot_scaled_sprite_v_flip(BITMAP *bmp, BITMAP *sprite, int x, int y,

                                int cx, int cy, fixed angle, fixed scale);</code></pre>
<h2>Description</h2>
<p>Like rotate_scaled_sprite_v_flip(), but aligns the point in the sprite given by (cx, cy) to (x, y) in the bitmap, then rotates and scales around this point. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-rotate_sprite/">rotate_sprite</a></code>(3), <code><a href="/docs/linux/man/3-rotate_scaled_sprite_v_flip/">rotate_scaled_sprite_v_flip</a></code>(3), <code><a href="/docs/linux/man/3-rotate_sprite_v_flip/">rotate_sprite_v_flip</a></code>(3), <code><a href="/docs/linux/man/3-pivot_sprite/">pivot_sprite</a></code>(3), <code><a href="/docs/linux/man/3-pivot_scaled_sprite/">pivot_scaled_sprite</a></code>(3) </p>
