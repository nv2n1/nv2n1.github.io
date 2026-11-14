---
title: "create_scene(3)"
name: "create_scene"
section: "3"
letter: "c"
url: "/docs/linux/man/3-create_scene/"
description: "create_scene – Allocates memory for a 3d scene. Allegro game programming library."
---

<h2>NAME</h2>
<p> create_scene &#8211; Allocates memory for a 3d scene. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int create_scene(int nedge, int npoly);</code></p>
<h2>DESCRIPTION</h2>
<p> Allocates memory for a scene, `nedge&#8217; and `npoly&#8217; are your estimates of how many edges and how many polygons you will render (you cannot get over the limit specified here). If you use same values in successive calls, the space will be reused (no new malloc()). </p>
<p> The memory allocated is a little less than 150 * (nedge + npoly) bytes.</p>
<h2>RETURN VALUE</h2>
<p> Returns zero on success, or a negative number if allocations fail. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-scene_polygon3d/">scene_polygon3d</a></code>(3), <code><a href="/docs/linux/man/3-render_scene/">render_scene</a></code>(3), <code><a href="/docs/linux/man/3-clear_scene/">clear_scene</a></code>(3), <code><a href="/docs/linux/man/3-destroy_scene/">destroy_scene</a></code>(3), <code><a href="/docs/linux/man/3-scene_gap/">scene_gap</a></code>(3), <code><a href="/docs/linux/man/3-create_zbuffer/">create_zbuffer</a></code>(3), <code><a href="/docs/linux/man/3-exscn3d/">exscn3d</a></code>(3) </p>
<h2>Index</h2>
