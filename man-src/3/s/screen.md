---
title: "screen(3)"
name: "screen"
section: "3"
letter: "s"
url: "/docs/linux/man/3-screen/"
description: "screen – Global pointer to the screen hardware video memory. Allegro game programming library."
---

<p>screen &#8211; Global pointer to the screen hardware video memory. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;
</code></pre>
<p> <code>extern BITMAP *screen;</code></p>
<h2>Description</h2>
<p>Global pointer to a bitmap, sized VIRTUAL_W x VIRTUAL_H. This is created by set_gfx_mode(), and represents the hardware video memory. Only a part of this bitmap will actually be visible, sized SCREEN_W x SCREEN_H. Normally this is the top left corner of the larger virtual screen, so you can ignore the extra invisible virtual size of the bitmap if you aren&#8217;t interested in hardware scrolling or page flipping. To move the visible window to other parts of the screen bitmap, call scroll_screen(). Initially the clipping rectangle will be limited to the physical screen size, so if you want to draw onto a larger virtual screen space outside this rectangle, you will need to adjust the clipping. For example, to draw a pixel onto the screen you would write: </p>
<pre> putpixel(screen, x, y, color);</pre>
<p>Or to implement a double-buffered system:  Warning: be very careful when using this pointer at the same time as any bitmaps created by the create_video_bitmap() function (see the description of this function for more detailed information). And never try to destroy it with destroy_bitmap(). </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-set_gfx_mode/">set_gfx_mode</a></code>(3), <code><a href="/docs/linux/man/3-is_screen_bitmap/">is_screen_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-create_video_bitmap/">create_video_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-scroll_screen/">scroll_screen</a></code>(3) </p>
