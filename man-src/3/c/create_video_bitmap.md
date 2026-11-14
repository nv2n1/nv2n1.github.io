---
title: "create_video_bitmap(3)"
name: "create_video_bitmap"
section: "3"
letter: "c"
url: "/docs/linux/man/3-create_video_bitmap/"
description: "create_video_bitmap – Creates a video memory bitmap. Allegro game programming library."
---

<h2>NAME</h2>
<p> create_video_bitmap &#8211; Creates a video memory bitmap. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>BITMAP *create_video_bitmap(int width, int height);</code></p>
<h2>DESCRIPTION</h2>
<p> Allocates a video memory bitmap of the specified size. This can be used to allocate offscreen video memory for storing source graphics ready for a hardware accelerated blitting operation, or to create multiple video memory pages which can then be displayed by calling show_video_bitmap(). Read the introduction of this chapter for a comparison with other types of bitmaps and other specific details. </p>
<p> Warning: video memory bitmaps are usually allocated from the same space as the screen bitmap, so they may overlap with it; it is therefore not a good idea to use the global screen at the same time as any surfaces returned by this function.</p>
<h2>RETURN VALUE</h2>
<p> Returns a pointer to the bitmap on success, or NULL if you have run out of video ram. Remember to destroy this bitmap before any subsequent call to set_gfx_mode(). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-create_bitmap/">create_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-create_bitmap_ex/">create_bitmap_ex</a></code>(3), <code><a href="/docs/linux/man/3-create_system_bitmap/">create_system_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-create_sub_bitmap/">create_sub_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-destroy_bitmap/">destroy_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-screen/">screen</a></code>(3), <code><a href="/docs/linux/man/3-show_video_bitmap/">show_video_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-gfx_capabilities/">gfx_capabilities</a></code>(3), <code><a href="/docs/linux/man/3-is_video_bitmap/">is_video_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-clear_bitmap/">clear_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-clear_to_color/">clear_to_color</a></code>(3), <code><a href="/docs/linux/man/3-ex3buf/">ex3buf</a></code>(3), <code><a href="/docs/linux/man/3-exaccel/">exaccel</a></code>(3), <code><a href="/docs/linux/man/3-exflip/">exflip</a></code>(3), <code><a href="/docs/linux/man/3-exupdate/">exupdate</a></code>(3) </p>
<h2>Index</h2>
