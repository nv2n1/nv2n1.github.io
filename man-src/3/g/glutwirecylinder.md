---
title: "glutwirecylinder(3)"
name: "glutwirecylinder"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutwirecylinder/"
description: "glutWireCylinder – Draw a wireframe cylinder."
---

<p><code>glutWireCylinder</code> &#8211; Draw a wireframe cylinder.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; geometry</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutWireCylinder GLdouble radius GLdouble height GLint slices GLint stacks</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>radius Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Radius of cylinder. </p>
<p> Bf Em<br />
&nbsp;<wbr>height Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Z height. </p>
<p> Bf Em<br />
&nbsp;<wbr>slices Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Number of divisions around the z axis. </p>
<p> Bf Em<br />
&nbsp;<wbr>stacks Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Number of divisions along the z axis.</p>
<h2>Description</h2>
<p>glutWireCylinder() draws a wireframe of a cylinder, the center of whose base is at the origin, and whose axis parallels the z axis. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutsolidcylinder/">glutSolidCylinder</a>(3)</p>
