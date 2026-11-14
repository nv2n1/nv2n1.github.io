---
title: "glutbitmapstring(3)"
name: "glutbitmapstring"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutbitmapstring/"
description: "glutBitmapString – Draw a string of bitmapped characters"
---

<p><code>glutBitmapString</code> &#8211; Draw a string of bitmapped characters</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; bitmapfont</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutBitmapString void *font const unsigned char *string</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>font Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>A bitmapped font identifier. </p>
<p> Bf Em<br />
&nbsp;<wbr>string Ef<br />
&nbsp;<wbr>&nbsp;<wbr>A NUL-terminated ASCII string.</p>
<h2>Description</h2>
<p>Draw a Bf Sy<br />
&nbsp;<wbr>string Ef<br />
&nbsp;<wbr>the current OpenGL raster position using a bitmapped Bf Sy<br />
&nbsp;<wbr>font. Ef<br />
&nbsp;<wbr>&nbsp;<wbr>The raster position is advanced by the width of the string. </p>
<p> The starting raster position is used as the left margin for multi-line strings. Each newline character repositions the raster position at the beginning of the next line. </p>
<p> Nothing is drawn, and the raster position is unaffected when either:<br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>font Ef<br />
&nbsp;<wbr>is not a valid OpenGLUT bitmap font<br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>string Ef<br />
&nbsp;<wbr>is an empty string or NULL pointer<br />
&nbsp;<wbr>&#8211; The current OpenGL raster position is invalid </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glrasterpos/">glRasterPos</a>(3) <a href="/docs/linux/man/3-glutbitmapcharacter/">glutBitmapCharacter</a>(3)</p>
