---
title: "glutstrokelength(3)"
name: "glutstrokelength"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutstrokelength/"
description: "glutStrokeLength – Returns model space width of a string in a given font."
---

<p><code>glutStrokeLength</code> &#8211; Returns model space width of a string in a given font.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; fonts</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft float Fn glutStrokeLength void *fontID const unsigned char *string</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>fontID Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>A GLUT stroked font identifier. </p>
<p> Bf Em<br />
&nbsp;<wbr>string Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>A C-style&nbsp;<wbr>(NUL-terminated)&nbsp;<wbr>string.</p>
<h2>Description</h2>
<p>This function reports the sum of the widths of the characters in a Bf Sy<br />
&nbsp;<wbr>string, Ef<br />
&nbsp;<wbr>using the font metrics of a given Bf Sy<br />
&nbsp;<wbr>font. Ef<br />
&nbsp;<wbr> </p>
<p> Like glutStrokeString(), glutStrokeLength() respects newlines in the input. </p>
<p> Returns 0 if:<br />
&nbsp;<wbr>&#8211; The&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>fontID Ef<br />
&nbsp;<wbr>is out of range.<br />
&nbsp;<wbr>&#8211; The&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>string Ef<br />
&nbsp;<wbr>is&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>NULL. Ef<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&#8211; All characters in the&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>string Ef<br />
&nbsp;<wbr>are zero-width. </p>
<h2>Caveats</h2>
<p>Refer to glutStrokeWidth() for notes on the nature of this function&#8217;s return value, and for comparisons to old GLUT and freeglut. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutstrokestring/">glutStrokeString</a>(3) <a href="/docs/linux/man/3-glutstrokewidth/">glutStrokeWidth</a>(3) <a href="/docs/linux/man/3-glutstrokeheight/">glutStrokeHeight</a>(3) <a href="/docs/linux/man/3-glutbitmaplength/">glutBitmapLength</a>(3)</p>
