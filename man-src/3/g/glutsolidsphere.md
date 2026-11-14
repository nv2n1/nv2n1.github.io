---
title: "glutsolidsphere(3)"
name: "glutsolidsphere"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutsolidsphere/"
description: "glutSolidSphere – Draw a solid sphere centered at the origin."
---

<p><code>glutSolidSphere</code> &#8211; Draw a solid sphere centered at the origin.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; geometry</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutSolidSphere GLdouble radius GLint slices GLint stacks</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>radius Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Sphere radius. </p>
<p> Bf Em<br />
&nbsp;<wbr>slices Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>The number of divisions around the z axis.&nbsp;<wbr>(latitudal) </p>
<p> Bf Em<br />
&nbsp;<wbr>stacks Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>The number of divisions along the z axis.&nbsp;<wbr>(longitudal)</p>
<h2>Description</h2>
<p>The glutSolidSphere() function draws a shaded sphere centered at the origin. The surface is created from quadrangles (except for triangles as degenerate quads at the poles) in a longitude/latitude pattern. The equatorial great circle lies in the xy-plane and is centered on the origin. </p>
<h2>Caveats</h2>
<p>The number of polygons representing the spherical surface is proportional to (slices*stacks). </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutwiresphere/">glutWireSphere</a>(3)</p>
