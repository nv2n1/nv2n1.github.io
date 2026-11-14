---
title: "glutbitmapheight(3)"
name: "glutbitmapheight"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutbitmapheight/"
description: "glutBitmapHeight – Return the height of a given font, in pixels."
---

<p><code>glutBitmapHeight</code> &#8211; Return the height of a given font, in pixels.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; bitmapfont</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft int Fn glutBitmapHeight void *font</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>font Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>A bitmapped font identifier.</p>
<h2>Description</h2>
<p>Return the line-to-line vertical spacing (in pixels) between lines of a bitmapped Bf Sy<br />
&nbsp;<wbr>font. Ef<br />
&nbsp;<wbr> </p>
<p> Returns 0 if Bf Sy<br />
&nbsp;<wbr>font Ef<br />
&nbsp;<wbr>is invalid. </p>
<h2>Caveats</h2>
<p>Does Bf Li<br />
&nbsp;<wbr>not Ef<br />
&nbsp;<wbr>&nbsp;<wbr>report the height used by individual characters.&nbsp;<wbr>&nbsp;<wbr>This may limit its usefulness.&nbsp;<wbr>&nbsp;<wbr>(Compare with other font-metric queries.) </p>
<h2>Todo</h2>
<p>We have discussed adding a &quot;font descender&quot; query. We should go ahead and do it. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutbitmapcharacter/">glutBitmapCharacter</a>(3) <a href="/docs/linux/man/3-glutbitmapstring/">glutBitmapString</a>(3) <a href="/docs/linux/man/3-glutbitmapwidth/">glutBitmapWidth</a>(3) <a href="/docs/linux/man/3-glutbitmaplength/">glutBitmapLength</a>(3) <a href="/docs/linux/man/3-glutstrokeheight/">glutStrokeHeight</a>(3)</p>
