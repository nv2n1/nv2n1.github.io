---
title: "rotate_scaled_sprite(3)"
name: "rotate_scaled_sprite"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rotate_scaled_sprite/"
description: "rotate_scaled_sprite – Rotates and stretches a sprite. Allegro game programming library."
---

<p>rotate_scaled_sprite &#8211; Rotates and stretches a sprite. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void rotate_scaled_sprite(BITMAP *bmp, BITMAP *sprite, int x, int y,

                          fixed angle, fixed scale);</code></pre>
<h2>Description</h2>
<p>Like rotate_sprite(), but stretches or shrinks the image at the same time as rotating it. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-rotate_sprite/">rotate_sprite</a></code>(3), <code><a href="/docs/linux/man/3-rotate_scaled_sprite_v_flip/">rotate_scaled_sprite_v_flip</a></code>(3), <code><a href="/docs/linux/man/3-pivot_scaled_sprite/">pivot_scaled_sprite</a></code>(3), <code><a href="/docs/linux/man/3-pivot_scaled_sprite_v_flip/">pivot_scaled_sprite_v_flip</a></code>(3) </p>
