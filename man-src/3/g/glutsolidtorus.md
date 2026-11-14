---
title: "glutsolidtorus(3)"
name: "glutsolidtorus"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutsolidtorus/"
description: "glutSolidTorus – Draw a solid torus."
---

<p><code>glutSolidTorus</code> &#8211; Draw a solid torus.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; geometry</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutSolidTorus GLdouble dInnerRadius GLdouble dOuterRadius GLint nSides GLint nRings</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>dInnerRadius Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Radius of&nbsp;<wbr>&#8220;tube&#8221; </p>
<p> Bf Em<br />
&nbsp;<wbr>dOuterRadius Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Radius of&nbsp;<wbr>&#8220;path&#8221; </p>
<p> Bf Em<br />
&nbsp;<wbr>nSides Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Facets around&nbsp;<wbr>&#8220;tube&#8221; </p>
<p> Bf Em<br />
&nbsp;<wbr>nRings Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Joints along&nbsp;<wbr>&#8220;path&#8221;</p>
<h2>Description</h2>
<p>This function effectively wraps a cylinder with Bf Sy<br />
&nbsp;<wbr>nSides Ef<br />
&nbsp;<wbr>slats and bends it at Bf Sy<br />
&nbsp;<wbr>nRings Ef<br />
&nbsp;<wbr>facets around a circular path, forming a torus, or &#8220;donut&#8221;. The center is at the origin and the &#8220;path&#8221; rings around the z axis. </p>
<p> The torus parameters can be explored interactively with the OpenGLUT shapes demo. </p>
<h2>Caveats</h2>
<p>Bf Sy<br />
&nbsp;<wbr>dInnerRadius Ef<br />
&nbsp;<wbr>and&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>dOuterRadius Ef<br />
&nbsp;<wbr>are&nbsp;<wbr> Bf Em<br />
&nbsp;<wbr>not Ef<br />
&nbsp;<wbr>&nbsp;<wbr>analogous to similar measurements of an anulus. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutwiretorus/">glutWireTorus</a>(3)</p>
