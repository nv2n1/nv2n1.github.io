---
title: "create_bitmap(3)"
name: "create_bitmap"
section: "3"
letter: "c"
url: "/docs/linux/man/3-create_bitmap/"
description: "create_bitmap – Creates a memory bitmap. Allegro game programming library."
---

<h2>NAME</h2>
<p> create_bitmap &#8211; Creates a memory bitmap. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>BITMAP *create_bitmap(int width, int height);</code></p>
<h2>DESCRIPTION</h2>
<p> Creates a memory bitmap sized width by height. The bitmap will have clipping turned on, and the clipping rectangle set to the full size of the bitmap. The image memory will not be cleared, so it will probably contain garbage: you should clear the bitmap before using it. This routine always uses the global pixel format, as specified by calling set_color_depth(). The minimum height of the BITMAP must be 1 and width can&#8217;t be negative. Example: </p>
<pre><code>
/* Create a 10 pixel tall bitmap, as wide as the screen. */
BITMAP *bmp = create_bitmap(SCREEN_W, 10);
if (!bmp)
    abort_on_error("Couldn't create bitmap!");
/* Use the bitmap. */
...
    /* Destroy it when we don't need it any more. */
    destroy_bitmap(bmp);
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns a pointer to the created bitmap, or NULL if the bitmap could not be created. Remember to free this bitmap later to avoid memory leaks. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-create_bitmap_ex/">create_bitmap_ex</a></code>(3), <code><a href="/docs/linux/man/3-create_sub_bitmap/">create_sub_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-create_video_bitmap/">create_video_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-create_system_bitmap/">create_system_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-destroy_bitmap/">destroy_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-set_color_depth/">set_color_depth</a></code>(3), <code><a href="/docs/linux/man/3-is_memory_bitmap/">is_memory_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-clear_bitmap/">clear_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-clear_to_color/">clear_to_color</a></code>(3) </p>
<h2>Index</h2>
