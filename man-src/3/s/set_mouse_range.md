---
title: "set_mouse_range(3)"
name: "set_mouse_range"
section: "3"
letter: "s"
url: "/docs/linux/man/3-set_mouse_range/"
description: "set_mouse_range – Sets the area of the screen restricting mouse movement. Allegro game programming library."
---

<p>set_mouse_range &#8211; Sets the area of the screen restricting mouse movement. Allegro game programming library.</p>
<h2>Synopsis</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void set_mouse_range(int x1, int y1, int x2, int y2);</code></p>
<h2>Description</h2>
<p> Sets the area of the screen within which the mouse can move. Pass the top left corner and the bottom right corner (inclusive). If you don&#8217;t call this function the range defaults to (0, 0, SCREEN_W-1, SCREEN_H-1). </p>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/3-install_mouse/">install_mouse</a></code>(3), <code><a href="/docs/linux/man/3-set_mouse_speed/">set_mouse_speed</a></code>(3), <code><a href="/docs/linux/man/3-position_mouse/">position_mouse</a></code>(3)</p>
