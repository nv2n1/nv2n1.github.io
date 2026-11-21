---

title: "create_bitmap_ex(3)"
name: "create_bitmap_ex"
section: "3"
letter: "c"
url: "/docs/linux/man/3-create_bitmap_ex/"
description: "create_bitmap_ex – Creates a memory bitmap specifying color depth. Allegro game programming library."
---

<h2>NAME</h2>
<p> create_bitmap_ex &#8211; Creates a memory bitmap specifying color depth. Allegro game programming library.</p>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>BITMAP *create_bitmap_ex(int color_depth, int width, int height);</code></p>
<p> Creates a bitmap in a specific color depth (8, 15, 16, 24 or 32 bits per pixel). Example: </p>
<pre><code>
/* Create screen sized bitmap in 32 bits per pixel. */
BITMAP *bmp = create_bitmap_ex(32, SCREEN_W, SCREEN_H);
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
<p> <code><a href="/docs/linux/man/3-create_bitmap/">create_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-create_sub_bitmap/">create_sub_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-create_video_bitmap/">create_video_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-create_system_bitmap/">create_system_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-destroy_bitmap/">destroy_bitmap</a></code>(3), <code>is_memory_bitmap</code>(3), <code>clear_bitmap</code>(3), <code>clear_to_color</code>(3), <code><a href="/docs/linux/man/3-ex12bit/">ex12bit</a></code>(3), <code><a href="/docs/linux/man/3-exlights/">exlights</a></code>(3), <code><a href="/docs/linux/man/3-exrgbhsv/">exrgbhsv</a></code>(3), <code><a href="/docs/linux/man/3-extrans/">extrans</a></code>(3) </p>
