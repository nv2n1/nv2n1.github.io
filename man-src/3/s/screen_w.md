---
title: "screen_w(3)"
name: "screen_w"
section: "3"
letter: "s"
url: "/docs/linux/man/3-screen_w/"
description: "SCREEN_W, SCREEN_H – Global define to obtain the size of the screen. Allegro game programming library."
---

<p>SCREEN_W, SCREEN_H &#8211; Global define to obtain the size of the screen. Allegro game programming library.</p>
<h2>Synopsis</h2>
<p><code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>#define SCREEN_W;</code> </p>
<p> <code>#define SCREEN_H;</code></p>
<h2>Description</h2>
<p>Global defines that return the width and height of the screen, or zero if the screen has not been initialised yet. Example: </p>
<pre> char buf[100];
 ...
 uszprintf(buf, sizeof(buf),
 &quot;The screen size is %d x %d pixels&quot;,
 SCREEN_W, SCREEN_H);</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-screen/">screen</a></code>(3), <code><a href="/docs/linux/man/3-set_gfx_mode/">set_gfx_mode</a></code>(3), <code><a href="/docs/linux/man/3-virtual_w/">VIRTUAL_W</a></code>(3), <code><a href="/docs/linux/man/3-virtual_h/">VIRTUAL_H</a></code>(3)</p>
