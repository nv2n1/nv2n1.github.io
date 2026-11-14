---
title: "glutwireoctahedron(3)"
name: "glutwireoctahedron"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutwireoctahedron/"
description: "glutWireOctahedron – Draw a wireframe octahedron."
---

<p><code>glutWireOctahedron</code> &#8211; Draw a wireframe octahedron.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; geometry</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutWireOctahedron void</p>
<h2>Description</h2>
<p>This function draws a regular wireframe 8-sided polyhedron centered at the origin. The vertices are at (+/-1, 0, 0), (0, +/-1, 0), (0, 0, +/-1). </p>
<h2>Caveats</h2>
<p>We visit the same vertices the same number of times as for the solid octahedron, but the order is different. </p>
<p> Draws every edge twice. </p>
<p> The lines have normals, but the normals are from the facets, rather than upon the edge. If you squint too hard, the lighting on a wireframe octahedron does not look quite right. </p>
<h2>Todo</h2>
<p>It may be faster (and look better) to draw each edge once, setting the Normal at each edge. (I don&#8217;t think that this matters all that much, but a lineloop was proposed for the wire Cube for speed.) </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutsolidoctahedron/">glutSolidOctahedron</a>(3)</p>
