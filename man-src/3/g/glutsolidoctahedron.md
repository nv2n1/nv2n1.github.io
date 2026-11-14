---
title: "glutsolidoctahedron(3)"
name: "glutsolidoctahedron"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutsolidoctahedron/"
description: "glutSolidOctahedron – Draw a solid octahedron."
---

<p><code>glutSolidOctahedron</code> &#8211; Draw a solid octahedron.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; geometry</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutSolidOctahedron void</p>
<h2>Description</h2>
<p>This function draws a regular, solid 8-sided polyhedron centered at the origin. The vertices are at (+/-1, 0, 0), (0, +/-1, 0), (0, 0, +/-1). </p>
<h2>Caveats</h2>
<p>We visit the same vertices the same number of times as in the wire octahedron, but the order is different. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutwireoctahedron/">glutWireOctahedron</a>(3)</p>
