---
title: "glutsolidcone(3)"
name: "glutsolidcone"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutsolidcone/"
description: "glutSolidCone – Draw a solid cone."
---

<p><code>glutSolidCone</code> &#8211; Draw a solid cone.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; geometry</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutSolidCone GLdouble base GLdouble height GLint slices GLint stacks</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>base Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Cone radius at the base in the xy plane. </p>
<p> Bf Em<br />
&nbsp;<wbr>height Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Height of cone in positive z direction. </p>
<p> Bf Em<br />
&nbsp;<wbr>slices Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>The number of divisions around the z axis.&nbsp;<wbr>(latitudal) </p>
<p> Bf Em<br />
&nbsp;<wbr>stacks Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>The number of divisions along the z axis.&nbsp;<wbr>(longitudal)</p>
<h2>Description</h2>
<p>The glutSolidCone() function draws a shaded cone with a base in the xy-plane, oriented in the positive z direction. </p>
<h2>Caveats</h2>
<p>The number of polygons representing the conical surface is proportional to (slices*stacks). </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutwirecone/">glutWireCone</a>(3)</p>
