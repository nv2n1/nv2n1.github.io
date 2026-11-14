---
title: "v3d(3)"
name: "v3d"
section: "3"
letter: "v"
url: "/docs/linux/man/3-v3d/"
description: "V3D – Fixed point vertex structure used by 3d functions. Allegro game programming library."
---

<p>V3D &#8211; Fixed point vertex structure used by 3d functions. Allegro game programming library.</p>
<h2>Synopsis</h2>
<p><code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>typedef struct V3D</code></p>
<h2>Description</h2>
<pre> fixed x, y, z; - position
 fixed u, v; - texture map coordinates
 int c; - color</pre>
<p>A vertex structure used by polygon3d and other polygon rendering functions. Read the description of polygon3d() for a description on how to obtain/use this structure. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-v3d_f/">V3D_f</a></code>(3), <code><a href="/docs/linux/man/3-polygon3d/">polygon3d</a></code>(3), <code><a href="/docs/linux/man/3-ex3d/">ex3d</a></code>(3)</p>
