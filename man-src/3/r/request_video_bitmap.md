---
title: "request_video_bitmap(3)"
name: "request_video_bitmap"
section: "3"
letter: "r"
url: "/docs/linux/man/3-request_video_bitmap/"
description: "request_video_bitmap – Triple buffering page flip request. Allegro game programming library."
---

<p>request_video_bitmap &#8211; Triple buffering page flip request. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int request_video_bitmap(BITMAP *bitmap);</code></pre>
<h2>Description</h2>
<p>This function is used for triple buffering. It requests a page flip to display the specified video bitmap object, but returns immediately rather than waiting for a retrace. The flip will then take place during the next vertical retrace, but you can carry on running other code in the meantime and use the poll_scroll() routine to detect when the flip has actually taken place. Triple buffering is only possible on certain hardware: see the comments about request_scroll(). Example: </p>
<pre><code>int current_page;
BITMAP *video_page[3];
...
    /* Create pages for page flipping */
    video_page[0] = create_video_bitmap(SCREEN_W, SCREEN_H);
video_page[1] = create_video_bitmap(SCREEN_W, SCREEN_H);
video_page[2] = create_video_bitmap(SCREEN_W, SCREEN_H);
current_page = 0;
...
    /* draw the screen and flip pages */
    draw_screen(video_page[current_page]);
do {
} while (poll_scroll());
request_video_bitmap(video_page[current_page]);
current_page = (current_page + 1) % 3;
...</code></pre>
<h2>Return Value</h2>
<p>Returns zero on success and non-zero on failure. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-poll_scroll/">poll_scroll</a></code>(3), <code><a href="/docs/linux/man/3-request_scroll/">request_scroll</a></code>(3), <code><a href="/docs/linux/man/3-gfx_capabilities/">gfx_capabilities</a></code>(3), <code><a href="/docs/linux/man/3-create_video_bitmap/">create_video_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-scroll_screen/">scroll_screen</a></code>(3), <code><a href="/docs/linux/man/3-ex3buf/">ex3buf</a></code>(3), <code><a href="/docs/linux/man/3-exupdate/">exupdate</a></code>(3) </p>
