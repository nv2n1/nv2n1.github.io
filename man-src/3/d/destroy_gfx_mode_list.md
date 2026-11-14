---
title: "destroy_gfx_mode_list(3)"
name: "destroy_gfx_mode_list"
section: "3"
letter: "d"
url: "/docs/linux/man/3-destroy_gfx_mode_list/"
description: "destroy_gfx_mode_list – Frees the list created by get_gfx_mode_list(). Allegro game programming library."
---

<h2>NAME</h2>
<p> destroy_gfx_mode_list &#8211; Frees the list created by get_gfx_mode_list(). Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void destroy_gfx_mode_list(GFX_MODE_LIST *mode_list);</code></p>
<h2>DESCRIPTION</h2>
<p> Removes the mode list created by get_gfx_mode_list() from memory. Use this once you are done with the generated mode list to avoid memory leaks in your program. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-get_gfx_mode_list/">get_gfx_mode_list</a></code>(3), <code><a href="/docs/linux/man/3-set_gfx_mode/">set_gfx_mode</a></code>(3), <code><a href="/docs/linux/man/3-set_color_depth/">set_color_depth</a></code>(3) </p>
<h2>Index</h2>
