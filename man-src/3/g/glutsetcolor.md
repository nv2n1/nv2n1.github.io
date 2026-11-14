---
title: "glutsetcolor(3)"
name: "glutsetcolor"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutsetcolor/"
description: "glutSetColor – Sets an indexed color-mode entry."
---

<p><code>glutSetColor</code> &#8211; Sets an indexed color-mode entry.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; colormap</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutSetColor int nColor GLfloat red GLfloat green GLfloat blue</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>nColor Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>The palette entry to change. </p>
<p> Bf Em<br />
&nbsp;<wbr>red Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>New red value for palette entry. </p>
<p> Bf Em<br />
&nbsp;<wbr>green Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>New green value for palette entry. </p>
<p> Bf Em<br />
&nbsp;<wbr>blue Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>New blue value for palette entry.</p>
<h2>Description</h2>
<p>glutSetCursor() allows you to set individual color-map entries in a Bf Sy<br />
&nbsp;<wbr>GLUT_INDEX Ef<br />
&nbsp;<wbr>type of display.&nbsp;<wbr>&nbsp;<wbr>Respects the current overlay setting. </p>
<h2>Bugs</h2>
<p>Unimplemented. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutgetcolor/">glutGetColor</a>(3) <a href="/docs/linux/man/3-glutcopycolormap/">glutCopyColorMap</a>(3)</p>
