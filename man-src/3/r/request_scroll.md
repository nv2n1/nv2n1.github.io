---
title: "request_scroll(3)"
name: "request_scroll"
section: "3"
letter: "r"
url: "/docs/linux/man/3-request_scroll/"
description: "request_scroll – Queues a hardware scroll request with triple buffering. Allegro game programming library."
---

<p>request_scroll &#8211; Queues a hardware scroll request with triple buffering. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int request_scroll(int x, int y);</code></pre>
<h2>Description</h2>
<p>This function is used for triple buffering. It requests a hardware scroll to the specified position, but returns immediately rather than waiting for a retrace. The scroll will then take place during the next vertical retrace, but you can carry on running other code in the meantime and use the poll_scroll() routine to detect when the flip has actually taken place. </p>
<p> Triple buffering is only possible with certain drivers: you can look at the GFX_CAN_TRIPLE_BUFFER bit in the gfx_capabilities flag to see if it will work with the current driver.</p>
<h2>Return Value</h2>
<p>This function returns zero on success, non-zero otherwise. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-poll_scroll/">poll_scroll</a></code>(3), <code><a href="/docs/linux/man/3-request_video_bitmap/">request_video_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-gfx_capabilities/">gfx_capabilities</a></code>(3), <code><a href="/docs/linux/man/3-scroll_screen/">scroll_screen</a></code>(3) </p>
