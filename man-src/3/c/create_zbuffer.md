---
title: "create_zbuffer(3)"
name: "create_zbuffer"
section: "3"
letter: "c"
url: "/docs/linux/man/3-create_zbuffer/"
description: "create_zbuffer – Creates a Z-buffer for a bitmap. Allegro game programming library."
---

<h2>NAME</h2>
<p> create_zbuffer &#8211; Creates a Z-buffer for a bitmap. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>ZBUFFER *create_zbuffer(BITMAP *bmp);</code></p>
<h2>DESCRIPTION</h2>
<p> Creates a Z-buffer using the size of the BITMAP you are planning to draw on. Several Z-buffers can be defined but only one can be used at the same time, so you must call set_zbuffer() to make this Z-buffer active.</p>
<h2>RETURN VALUE</h2>
<p> Returns the pointer to the ZBUFFER or NULL if there was an error. Remember to destroy the ZBUFFER once you are done with it, to avoid having memory leaks. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-create_sub_zbuffer/">create_sub_zbuffer</a></code>(3), <code><a href="/docs/linux/man/3-set_zbuffer/">set_zbuffer</a></code>(3), <code><a href="/docs/linux/man/3-clear_zbuffer/">clear_zbuffer</a></code>(3), <code><a href="/docs/linux/man/3-destroy_zbuffer/">destroy_zbuffer</a></code>(3), <code><a href="/docs/linux/man/3-exzbuf/">exzbuf</a></code>(3) </p>
<h2>Index</h2>
