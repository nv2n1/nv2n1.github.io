---
title: "polytype_ptex_trans(3)"
name: "polytype_ptex_trans"
section: "3"
letter: "p"
url: "/docs/linux/man/3-polytype_ptex_trans/"
description: "POLYTYPE_ATEX_TRANS, POLYTYPE_PTEX_TRANS – Polygon rendering mode type Allegro game programming library."
---

<p>POLYTYPE_ATEX_TRANS, POLYTYPE_PTEX_TRANS &#8211; Polygon rendering mode type Allegro game programming library.</p>
<h2>Synopsis</h2>
<p><code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>#define POLYTYPE_ATEX_TRANS</code> </p>
<p> <code>#define POLYTYPE_PTEX_TRANS</code></p>
<h2>Description</h2>
<p>Render translucent textures. All the general rules for drawing translucent things apply. However, these modes have a major limitation: they only work with memory bitmaps or linear frame buffers (not with banked frame buffers). Don&#8217;t even try, they do not check and your program will die horribly (or at least draw wrong things). </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-polygon3d/">polygon3d</a></code>(3), <code><a href="/docs/linux/man/3-ex3d/">ex3d</a></code>(3)</p>
