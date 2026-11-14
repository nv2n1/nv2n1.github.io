---
title: "glutwiresphere(3)"
name: "glutwiresphere"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutwiresphere/"
description: "glutWireSphere – Draw a wireframe sphere centered at the origin."
---

<p><code>glutWireSphere</code> &#8211; Draw a wireframe sphere centered at the origin.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; geometry</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutWireSphere GLdouble radius GLint slices GLint stacks</p>
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
<p>The glutWireSphere() function draws a wireframe sphere centered at the origin. The &quot;equatorial&quot; great circle lies in the xy-plane. </p>
<h2>Caveats</h2>
<p>The number of line segments representing the spherical surface is proportional to (slices*stacks). </p>
<h2>See Also</h2>
<p>glutSolidSphere.3</p>
