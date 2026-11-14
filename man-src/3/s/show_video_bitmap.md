---
title: "show_video_bitmap(3)"
name: "show_video_bitmap"
section: "3"
letter: "s"
url: "/docs/linux/man/3-show_video_bitmap/"
description: "show_video_bitmap – Flips the hardware screen to use the specified page. Allegro game programming library."
---

<p>show_video_bitmap &#8211; Flips the hardware screen to use the specified page. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int show_video_bitmap(BITMAP *bitmap);</code></pre>
<h2>Description</h2>
<p>Attempts to page flip the hardware screen to display the specified video bitmap object, which must be the same size as the physical screen, and should have been obtained by calling the create_video_bitmap() function. Allegro will handle any necessary vertical retrace synchronisation when page flipping, so you don&#8217;t need to call vsync() before it. This means that show_video_bitmap() has the same time delay effects as vsync() by default. This can be adjusted with the &quot;disable_vsync&quot; config key in the [graphics] section of allegro.cfg. Example: </p>
<pre><code>int current_page;
BITMAP *video_page[2];
...
    /* Create pages for page flipping */
    video_page[0] = create_video_bitmap(SCREEN_W, SCREEN_H);
video_page[1] = create_video_bitmap(SCREEN_W, SCREEN_H);
current_page = 0;
...
    /* draw the screen and flip pages */
    draw_screen(video_page[current_page]);
show_video_bitmap(video_page[current_page]);
current_page = (current_page + 1) % 2;
...</code></pre>
<h2>Return Value</h2>
<p>Returns zero on success and non-zero on failure. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-scroll_screen/">scroll_screen</a></code>(3), <code><a href="/docs/linux/man/3-create_video_bitmap/">create_video_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-exaccel/">exaccel</a></code>(3), <code><a href="/docs/linux/man/3-exflip/">exflip</a></code>(3), <code><a href="/docs/linux/man/3-exupdate/">exupdate</a></code>(3) </p>
