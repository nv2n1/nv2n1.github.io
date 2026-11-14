---
title: "gfx_mode_select_filter(3)"
name: "gfx_mode_select_filter"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gfx_mode_select_filter/"
description: "gfx_mode_select_filter – Even more extended version of the graphics mode selection dialog. Allegro game programming library."
---

<h2>NAME</h2>
<p> gfx_mode_select_filter &#8211; Even more extended version of the graphics mode selection dialog. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int gfx_mode_select_filter(int *card, int *w, int *h, int *color_depth,</code> <code>int (*filter)(int, int, int, int));</code></p>
<h2>DESCRIPTION</h2>
<p> Even more extended version of the graphics mode selection dialog, which allows the programmer to customize the contents of the dialog and the user to select the color depth as well as the resolution and hardware driver. `filter&#8217; will be passed (card, w, h, color_depth) quadruplets and must return 0 to let the specified quadruplet be added to the list of displayed modes. </p>
<p> This version of the function reads the initial values from the parameters when it activates so you can specify the default values. In fact, you should be sure not to pass in uninitialised values. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-gfx_mode_select/">gfx_mode_select</a></code>(3), <code><a href="/docs/linux/man/3-gfx_mode_select_ex/">gfx_mode_select_ex</a></code>(3), <code><a href="/docs/linux/man/3-set_color_depth/">set_color_depth</a></code>(3), <code><a href="/docs/linux/man/3-set_gfx_mode/">set_gfx_mode</a></code>(3), <code><a href="/docs/linux/man/3-gui_fg_color/">gui_fg_color</a></code>(3) </p>
<h2>Index</h2>
