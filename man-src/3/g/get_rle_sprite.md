---
title: "get_rle_sprite(3)"
name: "get_rle_sprite"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_rle_sprite/"
description: "get_rle_sprite – Creates an RLE sprite using a bitmap as source. Allegro game programming library."
---

<h2>NAME</h2>
<p> get_rle_sprite &#8211; Creates an RLE sprite using a bitmap as source. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>RLE_SPRITE *get_rle_sprite(BITMAP *bitmap);</code></p>
<h2>DESCRIPTION</h2>
<p> Creates an RLE sprite based on the specified bitmap (which must be a memory bitmap). Remember to free this RLE sprite later to avoid memory leaks. Example: </p>
<pre><code>
RLE_SPRITE *rle;
BITMAP *bmp;
...
    /* Create RLE sprite from an existent bitmap. */
    rle = get_rle_sprite(bmp);
if (!rle)
    abort_on_error("Couldn't create RLE sprite!");

/* We don't need the bitmap any more.*/
destroy_bitmap(bmp);

/* Use the RLE sprite. */
...
    /* Destroy it when we don't need it any more. */
    destroy_rle_sprite(rle);
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns a pointer to the created RLE sprite, or NULL if the RLE sprite could not be created. Remember to free this RLE sprite later to avoid memory leaks. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-draw_rle_sprite/">draw_rle_sprite</a></code>(3), <code><a href="/docs/linux/man/3-destroy_rle_sprite/">destroy_rle_sprite</a></code>(3) </p>
<h2>Index</h2>
