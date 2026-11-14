---
title: "glutbitmaplength(3)"
name: "glutbitmaplength"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutbitmaplength/"
description: "glutBitmapLength – Return the width of a bitmapped string, in pixels."
---

<p><code>glutBitmapLength</code> &#8211; Return the width of a bitmapped string, in pixels.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; bitmapfont</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft int Fn glutBitmapLength void *font const unsigned char *string</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>font Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>A bitmapped font identifier. </p>
<p> Bf Em<br />
&nbsp;<wbr>string Ef<br />
&nbsp;<wbr>&nbsp;<wbr>A NUL-terminated ASCII string.</p>
<h2>Description</h2>
<p>Returns the maximum horizontal OpenGL raster position offset for a Bf Sy<br />
&nbsp;<wbr>string Ef<br />
&nbsp;<wbr>in a bitmapped&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>font. Ef<br />
&nbsp;<wbr> </p>
<p> As with glutBitmapString(), newlines are taken into consideration. </p>
<p> Returns 0 if the Bf Sy<br />
&nbsp;<wbr>font Ef<br />
&nbsp;<wbr>is invalid or if the Bf Sy<br />
&nbsp;<wbr>string Ef<br />
&nbsp;<wbr>is empty or&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>NULL. Ef<br />
&nbsp;<wbr> </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutbitmapstring/">glutBitmapString</a>(3) <a href="/docs/linux/man/3-glutbitmapwidth/">glutBitmapWidth</a>(3) <a href="/docs/linux/man/3-glutbitmapheight/">glutBitmapHeight</a>(3) <a href="/docs/linux/man/3-glutstrokelength/">glutStrokeLength</a>(3)</p>
