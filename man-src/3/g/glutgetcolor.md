---
title: "glutgetcolor(3)"
name: "glutgetcolor"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutgetcolor/"
description: "glutGetColor – Gets an indexed color-mode entry’s Red, Green, or Blue value."
---

<p><code>glutGetColor</code> &#8211; Gets an indexed color-mode entry&#8217;s Red, Green, or Blue value.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; colormap</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft GLfloat Fn glutGetColor int color int component</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>color Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>The palette entry to fetch. </p>
<p> Bf Em<br />
&nbsp;<wbr>component Ef<br />
&nbsp;<wbr>Whether to fetch Red, Green, or Blue.</p>
<h2>Description</h2>
<p>Allows you to get individual color-map entries in a Bf Sy<br />
&nbsp;<wbr>GLUT_INDEX Ef<br />
&nbsp;<wbr>type of display.&nbsp;<wbr>&nbsp;<wbr>Respects the current layer setting. </p>
<p> Bf Sy<br />
&nbsp;<wbr>component Ef<br />
&nbsp;<wbr>may be any of: </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_RED Ef<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_GREEN Ef<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_BLUE Ef<br />
&nbsp;<wbr> </p>
<h2>Bugs</h2>
<p>Unimplemented. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutsetcolor/">glutSetColor</a>(3) <a href="/docs/linux/man/3-glutcopycolormap/">glutCopyColorMap</a>(3)</p>
