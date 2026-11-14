---
title: "get_compiled_sprite(3)"
name: "get_compiled_sprite"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_compiled_sprite/"
description: "get_compiled_sprite – Creates a compiled sprite using a bitmap as source. Allegro game programming library."
---

<h2>NAME</h2>
<p> get_compiled_sprite &#8211; Creates a compiled sprite using a bitmap as source. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>COMPILED_SPRITE *get_compiled_sprite(BITMAP *bitmap, int planar);</code></p>
<h2>DESCRIPTION</h2>
<p> Creates a compiled sprite based on the specified bitmap (which must be a memory bitmap). Compiled sprites are device-dependent, so you have to specify whether to compile it into a linear or planar format. Pass FALSE as the second parameter if you are going to be drawing it onto memory bitmaps or mode 13h and SVGA screen bitmaps, and pass TRUE if you are going to draw it onto mode-X or Xtended mode screen bitmaps. Example: </p>
<pre><code>
COMPILED_SPRITE *cspr;
BITMAP *bmp;
...
    /* Create compiled sprite from an existent bitmap. */
    cspr = get_compiled_sprite(bmp, 0);
if (!cspr)
    abort_on_error("Couldn't create compiled sprite!");

/* We don't need the bitmap any more.*/
destroy_bitmap(bmp);

/* Use the compiled sprite. */
...
    /* Destroy it when we don't need it any more. */
    destroy_compiled_sprite(cspr);
</code></pre>
<p> Returns a pointer to the created compiled sprite, or NULL if the compiled sprite could not be created. Remember to free this compiled sprite later to avoid memory leaks. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-draw_compiled_sprite/">draw_compiled_sprite</a></code>(3), <code><a href="/docs/linux/man/3-destroy_compiled_sprite/">destroy_compiled_sprite</a></code>(3) </p>
<h2>Index</h2>
