---
title: "create_system_bitmap(3)"
name: "create_system_bitmap"
section: "3"
letter: "c"
url: "/docs/linux/man/3-create_system_bitmap/"
description: "create_system_bitmap – Creates a system memory bitmap. Allegro game programming library."
---

<h2>NAME</h2>
<p> create_system_bitmap &#8211; Creates a system memory bitmap. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>BITMAP *create_system_bitmap(int width, int height);</code></p>
<h2>DESCRIPTION</h2>
<p> Allocates a system memory bitmap of the specified size. Read the introduction of this chapter for a comparison with other types of bitmaps and other specific details.</p>
<h2>RETURN VALUE</h2>
<p> Returns a pointer to the bitmap on success, NULL otherwise. Remember to destroy this bitmap before any subsequent call to set_gfx_mode(). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-create_bitmap/">create_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-create_bitmap_ex/">create_bitmap_ex</a></code>(3), <code><a href="/docs/linux/man/3-create_video_bitmap/">create_video_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-create_sub_bitmap/">create_sub_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-destroy_bitmap/">destroy_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-is_system_bitmap/">is_system_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-clear_bitmap/">clear_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-clear_to_color/">clear_to_color</a></code>(3), <code><a href="/docs/linux/man/3-exupdate/">exupdate</a></code>(3) </p>
<h2>Index</h2>
