---
title: "stretch_sprite(3)"
name: "stretch_sprite"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stretch_sprite/"
description: "stretch_sprite – Stretches a sprite to the destination bitmap. Allegro game programming library."
---

<p>stretch_sprite &#8211; Stretches a sprite to the destination bitmap. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void stretch_sprite(BITMAP *bmp, BITMAP *sprite, int x, int y, int w, int h);</code></pre>
<h2>Description</h2>
<p>Like draw_sprite(), except it can stretch the sprite image to the specified width and height and requires the sprite image and destination bitmap to be of the same color depth. Moreover, the sprite image must be a memory bitmap. Example: </p>
<pre><code>/* Create tunnel like effect. */
   for (step = 1; step
      int width = SCREEN_W / step;
      int height = SCREEN_H / step;
      stretch_sprite(screen, image, SCREEN_W / 2 - width / 2,
                     SCREEN_H / 2 - height / 2, width, height);
   }
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-draw_sprite/">draw_sprite</a></code>(3), <code><a href="/docs/linux/man/3-stretch_blit/">stretch_blit</a></code>(3), <code><a href="/docs/linux/man/3-bitmap_mask_color/">bitmap_mask_color</a></code>(3) </p>
