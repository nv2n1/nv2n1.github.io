---
title: "clear_zbuffer(3)"
name: "clear_zbuffer"
section: "3"
letter: "c"
url: "/docs/linux/man/3-clear_zbuffer/"
description: "clear_zbuffer – Writes a depth value into the given Z-buffer. Allegro game programming library."
---

<h2>NAME</h2>
<p> clear_zbuffer &#8211; Writes a depth value into the given Z-buffer. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void clear_zbuffer(ZBUFFER *zbuf, float z);</code></p>
<h2>DESCRIPTION</h2>
<p> Writes z into the given Z-buffer (0 means far away). This function should be used to initialize the Z-buffer before each frame. Actually, low-level routines compare depth of the current pixel with 1/z: for example, if you want to clip polygons farther than 10, you must call clear_zbuffer(zbuf, 0.1). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-create_zbuffer/">create_zbuffer</a></code>(3), <code><a href="/docs/linux/man/3-set_zbuffer/">set_zbuffer</a></code>(3), <code><a href="/docs/linux/man/3-destroy_zbuffer/">destroy_zbuffer</a></code>(3), <code><a href="/docs/linux/man/3-exzbuf/">exzbuf</a></code>(3) </p>
<h2>Index</h2>
