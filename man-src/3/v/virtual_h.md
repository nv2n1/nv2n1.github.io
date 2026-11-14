---
title: "virtual_h(3)"
name: "virtual_h"
section: "3"
letter: "v"
url: "/docs/linux/man/3-virtual_h/"
description: "VIRTUAL_W, VIRTUAL_H – Global define to obtain the virtual size of the screen. Allegro game programming library."
---

<p>VIRTUAL_W, VIRTUAL_H &#8211; Global define to obtain the virtual size of the screen. Allegro game programming library.</p>
<h2>Synopsis</h2>
<p><code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>#define VIRTUAL_W;</code> </p>
<p> <code>#define VIRTUAL_H;</code></p>
<h2>Description</h2>
<p>Global defines that return the width and height of the virtual screen, or zero if the screen has not been initialised yet. Example: </p>
<pre> char buf[100];
 ...
 uszprintf(buf, sizeof(buf),
 &quot;The virtual screen size is %d x %d pixels&quot;,
 SCREEN_W, SCREEN_H);</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-screen/">screen</a></code>(3), <code><a href="/docs/linux/man/3-set_gfx_mode/">set_gfx_mode</a></code>(3), <code><a href="/docs/linux/man/3-screen_w/">SCREEN_W</a></code>(3), <code><a href="/docs/linux/man/3-screen_h/">SCREEN_H</a></code>(3)</p>
