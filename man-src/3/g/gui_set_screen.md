---
title: "gui_set_screen(3)"
name: "gui_set_screen"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gui_set_screen/"
description: "gui_set_screen – Changes the bitmap surface GUI routines draw to. Allegro game programming library."
---

<h2>NAME</h2>
<p> gui_set_screen &#8211; Changes the bitmap surface GUI routines draw to. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void gui_set_screen(BITMAP *bmp);</code></p>
<h2>DESCRIPTION</h2>
<p> This function can be used to change the bitmap surface the GUI routines draw to. This can be useful if you are using a double buffering or page flipping system. Passing NULL will cause the default surface (screen) to be used again. Example: </p>
<pre><code>
BITMAP *page[2];

/* Allocate two pages of video memory */
page[0] = create_video_bitmap(SCREEN_W, SCREEN_H);
page[1] = create_video_bitmap(SCREEN_W, SCREEN_H);

/* Page flip */
show_video_bitmap(page[0]);
gui_set_screen(page[0]);
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-gui_get_screen/">gui_get_screen</a></code>(3) </p>
<h2>Index</h2>
