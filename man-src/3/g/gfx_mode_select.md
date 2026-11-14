---
title: "gfx_mode_select(3)"
name: "gfx_mode_select"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gfx_mode_select/"
description: "gfx_mode_select – Displays the Allegro graphics mode selection dialog."
---

<h2>NAME</h2>
<p> gfx_mode_select &#8211; Displays the Allegro graphics mode selection dialog.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int gfx_mode_select(int *card, int *w, int *h);</code></p>
<h2>DESCRIPTION</h2>
<p> Displays the Allegro graphics mode selection dialog, which allows the user to select a screen mode and graphics card. Stores the selection in the three variables, and returns zero if it was closed with the Cancel button or non-zero if it was OK&#8217;d. </p>
<p> The initial values of card, w, h are not used. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-gfx_mode_select_ex/">gfx_mode_select_ex</a></code>(3), <code><a href="/docs/linux/man/3-gfx_mode_select_filter/">gfx_mode_select_filter</a></code>(3), <code><a href="/docs/linux/man/3-set_gfx_mode/">set_gfx_mode</a></code>(3), <code><a href="/docs/linux/man/3-gui_fg_color/">gui_fg_color</a></code>(3) </p>
<h2>Index</h2>
