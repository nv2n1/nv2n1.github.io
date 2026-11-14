---
title: "glutbitmapwidth(3)"
name: "glutbitmapwidth"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutbitmapwidth/"
description: "glutBitmapWidth – Return the width of a bitmapped character, in pixels."
---

<p><code>glutBitmapWidth</code> &#8211; Return the width of a bitmapped character, in pixels.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; bitmapfont</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft int Fn glutBitmapWidth void *font int character</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>font Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>A bitmapped font identifier. </p>
<p> Bf Em<br />
&nbsp;<wbr>character Ef<br />
&nbsp;<wbr>A character code.</p>
<h2>Description</h2>
<p>Returns the horizontal OpenGL raster position offset for a Bf Sy<br />
&nbsp;<wbr>character Ef<br />
&nbsp;<wbr>in a bitmapped&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>font. Ef<br />
&nbsp;<wbr> </p>
<p> It is also an upper bound on the width of the bitmapped glyph for Bf Sy<br />
&nbsp;<wbr>character, Ef<br />
&nbsp;<wbr>though not all letters will use their full width, especially fixed-width fonts. </p>
<p> Returns 0 if the Bf Sy<br />
&nbsp;<wbr>character Ef<br />
&nbsp;<wbr>is out of the inclusive range [0,255] or if the Bf Sy<br />
&nbsp;<wbr>font Ef<br />
&nbsp;<wbr>is invalid. </p>
<h2>Caveats</h2>
<p>In GLUT, some glyphs could render to the left of the starting position, in some fonts. OpenGLUT&#8217;s fonts all position all of their glyphs to start at, or to the right of, the initial position. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutbitmapcharacter/">glutBitmapCharacter</a>(3) <a href="/docs/linux/man/3-glutbitmaplength/">glutBitmapLength</a>(3) <a href="/docs/linux/man/3-glutbitmapheight/">glutBitmapHeight</a>(3) <a href="/docs/linux/man/3-glutstrokewidth/">glutStrokeWidth</a>(3)</p>
