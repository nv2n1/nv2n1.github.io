---
title: "glutwiretetrahedron(3)"
name: "glutwiretetrahedron"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutwiretetrahedron/"
description: "glutWireTetrahedron – Draw a wireframe tetrahedron."
---

<p><code>glutWireTetrahedron</code> &#8211; Draw a wireframe tetrahedron.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; geometry</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutWireTetrahedron void</p>
<h2>Description</h2>
<p>This function draws a regular, wireframe 4-sided polyhedron centered at the origin. The distance from the origin to the vertices is 1. </p>
<h2>Todo</h2>
<p>Merge Bf Sy<br />
&nbsp;<wbr>r0 Ef<br />
&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>r1 Ef<br />
&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>r2 Ef<br />
&nbsp;<wbr>and&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>r3 Ef<br />
&nbsp;<wbr>into one array. </p>
<p> Put the normals into the (or an) array. </p>
<p> Make the array static const, with file scope, and share with glutSolidTetrahedron(). </p>
<p> Maybe consolidate with the SierpinskySponge? </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutsolidtetrahedron/">glutSolidTetrahedron</a>(3)</p>
