---
title: "enable_triple_buffer(3)"
name: "enable_triple_buffer"
section: "3"
letter: "e"
url: "/docs/linux/man/3-enable_triple_buffer/"
description: "enable_triple_buffer – Enables triple buffering. Allegro game programming library."
---

<h2>NAME</h2>
<p> enable_triple_buffer &#8211; Enables triple buffering. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int enable_triple_buffer();</code></p>
<h2>DESCRIPTION</h2>
<p> If the GFX_CAN_TRIPLE_BUFFER bit of the gfx_capabilities field is not set, you can attempt to enable it by calling this function. In particular if you are running in mode-X in a clean DOS environment, this routine will enable the timer retrace simulator, which will activate the triple buffering functions.</p>
<h2>RETURN VALUE</h2>
<p> Returns zero if triple buffering is enabled, -1 otherwise. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-gfx_capabilities/">gfx_capabilities</a></code>(3), <code><a href="/docs/linux/man/3-request_scroll/">request_scroll</a></code>(3), <code><a href="/docs/linux/man/3-request_video_bitmap/">request_video_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-ex3buf/">ex3buf</a></code>(3), <code><a href="/docs/linux/man/3-exupdate/">exupdate</a></code>(3) </p>
<h2>Index</h2>
