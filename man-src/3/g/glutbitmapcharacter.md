---
title: "glutbitmapcharacter(3)"
name: "glutbitmapcharacter"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutbitmapcharacter/"
description: "glutBitmapCharacter – Draw a bitmapped character"
---

<p><code>glutBitmapCharacter</code> &#8211; Draw a bitmapped character</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; bitmapfont</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutBitmapCharacter void *font int character</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>font Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>A bitmapped font identifier. </p>
<p> Bf Em<br />
&nbsp;<wbr>character Ef<br />
&nbsp;<wbr>A character code.</p>
<h2>Description</h2>
<p>Draw a Bf Sy<br />
&nbsp;<wbr>character Ef<br />
&nbsp;<wbr>at the current OpenGL raster position using a bitmapped Bf Sy<br />
&nbsp;<wbr>font. Ef<br />
&nbsp;<wbr>&nbsp;<wbr>The raster position is advanced by the width of the character. </p>
<p> Nothing is drawn, and the raster position is unaffected when either:<br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>character Ef<br />
&nbsp;<wbr>is out of range<br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>font Ef<br />
&nbsp;<wbr>is not a valid OpenGLUT bitmap font<br />
&nbsp;<wbr>&#8211; The current OpenGL raster position is invalid </p>
<h2>Caveats</h2>
<p>glutBitmapString() is generally more efficient for strings of characters. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glrasterpos/">glRasterPos</a>(3) <a href="/docs/linux/man/3-glutbitmapstring/">glutBitmapString</a>(3) <a href="/docs/linux/man/3-glutbitmapwidth/">glutBitmapWidth</a>(3) <a href="/docs/linux/man/3-glutbitmapheight/">glutBitmapHeight</a>(3) <a href="/docs/linux/man/3-glutstrokecharacter/">glutStrokeCharacter</a>(3)</p>
