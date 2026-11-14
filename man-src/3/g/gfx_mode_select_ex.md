---
title: "gfx_mode_select_ex(3)"
name: "gfx_mode_select_ex"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gfx_mode_select_ex/"
description: "gfx_mode_select_ex – Extended version of the graphics mode selection dialog. Allegro game programming library."
---

<h2>NAME</h2>
<p> gfx_mode_select_ex &#8211; Extended version of the graphics mode selection dialog. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int gfx_mode_select_ex(int *card, int *w, int *h, int *color_depth);</code></p>
<h2>DESCRIPTION</h2>
<p> Extended version of the graphics mode selection dialog, which allows the user to select the color depth as well as the resolution and hardware driver. </p>
<p> This version of the function reads the initial values from the parameters when it activates so you can specify the default values. In fact, you should be sure not to pass in uninitialised values. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-gfx_mode_select/">gfx_mode_select</a></code>(3), <code><a href="/docs/linux/man/3-gfx_mode_select_filter/">gfx_mode_select_filter</a></code>(3), <code><a href="/docs/linux/man/3-set_color_depth/">set_color_depth</a></code>(3), <code><a href="/docs/linux/man/3-set_gfx_mode/">set_gfx_mode</a></code>(3), <code><a href="/docs/linux/man/3-gui_fg_color/">gui_fg_color</a></code>(3), <code><a href="/docs/linux/man/3-ex3d/">ex3d</a></code>(3), <code><a href="/docs/linux/man/3-exscn3d/">exscn3d</a></code>(3), <code><a href="/docs/linux/man/3-exswitch/">exswitch</a></code>(3), <code><a href="/docs/linux/man/3-exupdate/">exupdate</a></code>(3), <code><a href="/docs/linux/man/3-exzbuf/">exzbuf</a></code>(3) </p>
<h2>Index</h2>
