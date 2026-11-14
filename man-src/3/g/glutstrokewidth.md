---
title: "glutstrokewidth(3)"
name: "glutstrokewidth"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutstrokewidth/"
description: "glutStrokeWidth – Returns the width in pixels of a character in a given font."
---

<p><code>glutStrokeWidth</code> &#8211; Returns the width in pixels of a character in a given font.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; fonts</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft float Fn glutStrokeWidth void *fontID int character</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>fontID Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>A GLUT stroked font identifier. </p>
<p> Bf Em<br />
&nbsp;<wbr>character Ef<br />
&nbsp;<wbr>A character code.</p>
<h2>Description</h2>
<p>This function reports how far the model space origin will advance if you putput this Bf Sy<br />
&nbsp;<wbr>character Ef<br />
&nbsp;<wbr>in the font named by&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>fontID. Ef<br />
&nbsp;<wbr> Not all letters will use their full width, especially in fixed-width fonts. </p>
<p> Returns 0 if Bf Sy<br />
&nbsp;<wbr>character Ef<br />
&nbsp;<wbr>is out of range or if the Bf Sy<br />
&nbsp;<wbr>fontID Ef<br />
&nbsp;<wbr>is invalid. </p>
<h2>Caveats</h2>
<p>Historically, this function has been described as returning a pixel-width, but was implemented to return the width in model-space units, rounded to integers. GLUT never resolved this, and freeglut duplicated the confusion. OpenGLUT has decided to stay in model-space and to return the unrounded floating point value. An unreleased GLUT 3.8 was supposed to include glutStrokeWidthf() and glutStrokeLengthf() (note the *f suffixes), but that is not in wide use. </p>
<h2>Todo</h2>
<p>Determine if any glyphs are either wider than this function or if they render outside of the bounding box given by Bf Li<br />
&nbsp;<wbr>(0,-descent) Ef<br />
&nbsp;<wbr>&nbsp;<wbr>by&nbsp;<wbr> Bf Li<br />
&nbsp;<wbr>(width,height-descent) Ef<br />
&nbsp;<wbr>. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutstrokecharacter/">glutStrokeCharacter</a>(3) <a href="/docs/linux/man/3-glutstrokelength/">glutStrokeLength</a>(3) glutStrokeHeightglutBitmapWidth3</p>
