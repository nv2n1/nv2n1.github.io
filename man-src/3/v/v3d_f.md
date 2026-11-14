---
title: "v3d_f(3)"
name: "v3d_f"
section: "3"
letter: "v"
url: "/docs/linux/man/3-v3d_f/"
description: "V3D_f – Floating point vertex structure used by 3d functions. Allegro game programming library."
---

<p>V3D_f &#8211; Floating point vertex structure used by 3d functions. Allegro game programming library.</p>
<h2>Synopsis</h2>
<p><code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>typedef struct V3D_f</code></p>
<h2>Description</h2>
<pre> float x, y, z; - position
 float u, v; - texture map coordinates
 int c; - color</pre>
<p>Like V3D but using float values instead of fixed ones. Read the description of polygon3d_f() for a description on how to obtain/use this structure. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-v3d/">V3D</a></code>(3), <code><a href="/docs/linux/man/3-polygon3d_f/">polygon3d_f</a></code>(3), <code><a href="/docs/linux/man/3-excamera/">excamera</a></code>(3), <code><a href="/docs/linux/man/3-exscn3d/">exscn3d</a></code>(3), <code><a href="/docs/linux/man/3-exzbuf/">exzbuf</a></code>(3)</p>
