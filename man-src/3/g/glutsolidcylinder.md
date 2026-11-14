---
title: "glutsolidcylinder(3)"
name: "glutsolidcylinder"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutsolidcylinder/"
description: "glutSolidCylinder – Draw a solid cylinder."
---

<p><code>glutSolidCylinder</code> &#8211; Draw a solid cylinder.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; geometry</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutSolidCylinder GLdouble radius GLdouble height GLint slices GLint stacks</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>radius Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Radius of the cylinder. </p>
<p> Bf Em<br />
&nbsp;<wbr>height Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Z height. </p>
<p> Bf Em<br />
&nbsp;<wbr>slices Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Divisions around z axis. </p>
<p> Bf Em<br />
&nbsp;<wbr>stacks Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Divisions along z axis.</p>
<h2>Description</h2>
<p>glutSolidCylinder() draws a shaded cylinder, the center of whose base is at the origin and whose axis is along the positive z axis. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutwirecylinder/">glutWireCylinder</a>(3)</p>
