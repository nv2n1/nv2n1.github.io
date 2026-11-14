---
title: "render_scene(3)"
name: "render_scene"
section: "3"
letter: "r"
url: "/docs/linux/man/3-render_scene/"
description: "render_scene – Renders all the queued scene polygons. Allegro game programming library."
---

<p>render_scene &#8211; Renders all the queued scene polygons. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void render_scene();</code></pre>
<h2>Description</h2>
<p>Renders all the specified scene_polygon3d()&#8217;s on the bitmap passed to clear_scene(). Rendering is done one scanline at a time, with no pixel being processed more than once. Note that between clear_scene() and render_scene() you shouldn&#8217;t change the clip rectangle of the destination bitmap. For speed reasons, you should set the clip rectangle to the minimum. Note also that all the textures passed to scene_polygon3d() are stored as pointers only and actually used in render_scene(). </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-create_scene/">create_scene</a></code>(3), <code><a href="/docs/linux/man/3-clear_scene/">clear_scene</a></code>(3), <code><a href="/docs/linux/man/3-destroy_scene/">destroy_scene</a></code>(3), <code><a href="/docs/linux/man/3-scene_gap/">scene_gap</a></code>(3), <code><a href="/docs/linux/man/3-scene_polygon3d/">scene_polygon3d</a></code>(3), <code><a href="/docs/linux/man/3-exscn3d/">exscn3d</a></code>(3) </p>
