---
title: "glutstrokecharacter(3)"
name: "glutstrokecharacter"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutstrokecharacter/"
description: "glutStrokeCharacter – Draw a stroked character."
---

<p><code>glutStrokeCharacter</code> &#8211; Draw a stroked character.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; fonts</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutStrokeCharacter void *fontID int character</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>fontID Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>A GLUT stroked font identifier. </p>
<p> Bf Em<br />
&nbsp;<wbr>character Ef<br />
&nbsp;<wbr>An ASCII character other than NUL.</p>
<h2>Description</h2>
<p>This function draws one Bf Sy<br />
&nbsp;<wbr>character Ef<br />
&nbsp;<wbr>from one stroked font (selected by Bf Sy<br />
&nbsp;<wbr>fontID) Ef<br />
&nbsp;<wbr> using OpenGL Bf Sy<br />
&nbsp;<wbr>GL_LINE_STRIP. Ef<br />
&nbsp;<wbr>&nbsp;<wbr>These characters are drawn at the origin in model space. The the model space origin is translated at the end, according to the Bf Sy<br />
&nbsp;<wbr>character Ef<br />
&nbsp;<wbr>width in&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>fontID. Ef<br />
&nbsp;<wbr> </p>
<p> Does nothing if:<br />
&nbsp;<wbr>&#8211; The&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>fontID Ef<br />
&nbsp;<wbr>is invalid.<br />
&nbsp;<wbr>&#8211; The&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>character Ef<br />
&nbsp;<wbr>is out of the font&#8217;s range. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glbegin/">glBegin</a>(3) <a href="/docs/linux/man/3-gltranslatef/">glTranslatef</a>(3) <a href="/docs/linux/man/3-glutstrokewidth/">glutStrokeWidth</a>(3) <a href="/docs/linux/man/3-glutstrokestring/">glutStrokeString</a>(3) <a href="/docs/linux/man/3-glutstrokeheight/">glutStrokeHeight</a>(3) <a href="/docs/linux/man/3-glutbitmapcharacter/">glutBitmapCharacter</a>(3)</p>
