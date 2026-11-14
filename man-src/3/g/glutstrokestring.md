---
title: "glutstrokestring(3)"
name: "glutstrokestring"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutstrokestring/"
description: "glutStrokeString – Draw a string of stroked characters."
---

<p><code>glutStrokeString</code> &#8211; Draw a string of stroked characters.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; fonts</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutStrokeString void *fontID const unsigned char *string</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>fontID Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>A GLUT stroked font identifier. </p>
<p> Bf Em<br />
&nbsp;<wbr>string Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>A NUL-terminated ASCII string.</p>
<h2>Description</h2>
<p>This function draws a Bf Sy<br />
&nbsp;<wbr>string Ef<br />
&nbsp;<wbr>in the font indicated by Bf Sy<br />
&nbsp;<wbr>fontID. Ef<br />
&nbsp;<wbr> It is Bf Li<br />
&nbsp;<wbr>almost Ef<br />
&nbsp;<wbr>&nbsp;<wbr>equivalent to calling glutStrokeCharacter() on each character in the Bf Sy<br />
&nbsp;<wbr>string, Ef<br />
&nbsp;<wbr>successively. Mostly, it is a convenience function to hide the loop, and to treat 
 as a special symbol rather than a normal glyph. </p>
<p> The first character displays at the current model space origin, The origin changes by successive translations. </p>
<p> The newline character, 
 (ASCII LF) is treated as a newline and resets the origin horizontally while advancing the line 1 font-height down the y-axis. </p>
<p> Does nothing if:<br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>fontID Ef<br />
&nbsp;<wbr>is out of range.<br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>string Ef<br />
&nbsp;<wbr>is&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>NULL Ef<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>string Ef<br />
&nbsp;<wbr>is empty </p>
<p> Unlike glutBitmapString(), there is little performance advantage to using glutStrokeString() as compared with calling glutStrokeCharacter() yourself for every character. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutstrokelength/">glutStrokeLength</a>(3) <a href="/docs/linux/man/3-glutstrokecharacter/">glutStrokeCharacter</a>(3) <a href="/docs/linux/man/3-glutstrokeheight/">glutStrokeHeight</a>(3) <a href="/docs/linux/man/3-glutbitmapstring/">glutBitmapString</a>(3)</p>
