---
title: "glutstrokeheight(3)"
name: "glutstrokeheight"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutstrokeheight/"
description: "glutStrokeHeight – Returns the height of a given font."
---

<p><code>glutStrokeHeight</code> &#8211; Returns the height of a given font.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; fonts</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft GLfloat Fn glutStrokeHeight void *fontID</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>fontID Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>A GLUT stroked font identifier.</p>
<h2>Description</h2>
<p>This function reports the height of a font, given by Bf Sy<br />
&nbsp;<wbr>fontID, Ef<br />
&nbsp;<wbr> as a global characteristic of that font. </p>
<p> Returns 0 if Bf Sy<br />
&nbsp;<wbr>fontID Ef<br />
&nbsp;<wbr>is invalid. </p>
<h2>Caveats</h2>
<p>Does Bf Li<br />
&nbsp;<wbr>not Ef<br />
&nbsp;<wbr>&nbsp;<wbr>report the height used by individual characters.&nbsp;<wbr>&nbsp;<wbr>This may limit its usefulness;&nbsp;<wbr>perhaps we should change it?&nbsp;<wbr>&nbsp;<wbr>(And/or add a new function.) </p>
<h2>Todo</h2>
<p>We have discussed adding a &quot;font descender&quot; query. We should go ahead and do it. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutstrokecharacter/">glutStrokeCharacter</a>(3) <a href="/docs/linux/man/3-glutstrokestring/">glutStrokeString</a>(3) <a href="/docs/linux/man/3-glutstrokewidth/">glutStrokeWidth</a>(3) <a href="/docs/linux/man/3-glutstrokelength/">glutStrokeLength</a>(3) <a href="/docs/linux/man/3-glutbitmapheight/">glutBitmapHeight</a>(3)</p>
