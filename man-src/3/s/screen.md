---

title: "screen(3)"
name: "screen"
section: "3"
letter: "s"
url: "/docs/linux/man/3-screen/"
description: "screen – Global pointer to the screen hardware video memory. Allegro game programming library."
---

<p> screen - Global pointer to the screen hardware video memory. Allegro game programming library.  </p>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>extern BITMAP *screen;</code>  </p>
<p> Global pointer to a bitmap, sized VIRTUAL_W x VIRTUAL_H. This is created by set_gfx_mode(), and represents the hardware video memory. Only a part of this bitmap will actually be visible, sized SCREEN_W x SCREEN_H. Normally this is the top left corner of the larger virtual screen, so you can ignore the extra invisible virtual size of the bitmap if you aren&#8217;t interested in hardware scrolling or page flipping. To move the visible window to other parts of the screen bitmap, call scroll_screen(). Initially the clipping rectangle will be limited to the physical screen size, so if you want to draw onto a larger virtual screen space outside this rectangle, you will need to adjust the clipping. </p>
<p>For example, to draw a pixel onto the screen you would write: </p>
<pre><code>   putpixel(screen, x, y, color);
</code></pre>
<p> Or to implement a double-buffered system: </p>
<pre><code>   /* Make a bitmap in RAM. */
   BITMAP *bmp = create_bitmap(320, 200);
   /* Clean the memory bitmap. */
   clear_bitmap(bmp);
   /* Draw onto the memory bitmap. */
   putpixel(bmp, x, y, color);
   /* Copy it to the screen. */
   blit(bmp, screen, 0, 0, 0, 0, 320, 200);
</code></pre>
<p>Warning: be very careful when using this pointer at the same time as any bitmaps created by the create_video_bitmap() function (see the description of this function for more detailed information). And never try to destroy it with destroy_bitmap(). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-set_gfx_mode/">set_gfx_mode</a></code>(3), <code>is_screen_bitmap</code>(3), <code><a href="/docs/linux/man/3-create_video_bitmap/">create_video_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-scroll_screen/">scroll_screen</a></code>(3) </p>
