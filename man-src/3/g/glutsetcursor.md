---
title: "glutsetcursor(3)"
name: "glutsetcursor"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutsetcursor/"
description: "glutSetCursor – Set the cursor image to be used for the current window"
---

<p><code>glutSetCursor</code> &#8211; Set the cursor image to be used for the current window</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; window</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutSetCursor int cursorID</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>cursorID Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Name of desired cursor.</p>
<h2>Description</h2>
<p>For the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>, sets the mouse-cursor to one of a set of predefined images. The GLUT symbolic constant IDs are: </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_CURSOR_RIGHT_ARROW Ef<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_CURSOR_LEFT_ARROW Ef<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_CURSOR_INFO Ef<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_CURSOR_DESTROY Ef<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_CURSOR_HELP Ef<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_CURSOR_CYCLE Ef<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_CURSOR_SPRAY Ef<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_CURSOR_WAIT Ef<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_CURSOR_TEXT Ef<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_CURSOR_CROSSHAIR Ef<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_CURSOR_UP_DOWN Ef<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_CURSOR_LEFT_RIGHT Ef<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_CURSOR_TOP_SIDE Ef<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_CURSOR_BOTTOM_SIDE Ef<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_CURSOR_LEFT_SIDE Ef<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_CURSOR_RIGHT_SIDE Ef<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_CURSOR_TOP_LEFT_CORNER Ef<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_CURSOR_TOP_RIGHT_CORNER Ef<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_CURSOR_BOTTOM_RIGHT_CORNER Ef<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_CURSOR_BOTTOM_LEFT_CORNER Ef<br />
&nbsp;<wbr> </p>
<p> Additionally, there are the following special cases: </p>
<p> Bf Sy<br />
&nbsp;<wbr>GLUT_CURSOR_FULL_CROSSHAIR Ef<br />
&nbsp;<wbr>This cursor, where supported, draws a crosshair the full width and height of the display. It may be mapped by OpenGLUT to the Bf Sy<br />
&nbsp;<wbr>GLUT_CURSOR_CROSSHAIR, Ef<br />
&nbsp;<wbr> however. </p>
<p> Bf Sy<br />
&nbsp;<wbr>GLUT_CURSOR_NONE Ef<br />
&nbsp;<wbr>Turn the mouse cursor invisibile. </p>
<p> Bf Sy<br />
&nbsp;<wbr>GLUT_CURSOR_INHERIT Ef<br />
&nbsp;<wbr>Take the cursor that the parent window provides. </p>
<h2>Caveats</h2>
<p>The X branch of OpenGLUT does not do thorough error checking. </p>
<p> The X branch of OpenGLUT always converts Bf Sy<br />
&nbsp;<wbr>FULL_CROSSHAIR Ef<br />
&nbsp;<wbr>to&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>CROSSHAIR. Ef<br />
&nbsp;<wbr>This is acceptable, but if a host system supports a fullscreen crosshair, it would be nice to support that. </p>
<p> Out of range Bf Sy<br />
&nbsp;<wbr>cursorID Ef<br />
&nbsp;<wbr>values generate warnings. </p>
<p> Has no visible effect if the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>&nbsp;<wbr>is of type&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_OFFSCREEN Ef<br />
&nbsp;<wbr>. </p>
<h2>Bugs</h2>
<p>Some Bf Sy<br />
&nbsp;<wbr>cursorID Ef<br />
&nbsp;<wbr>values are not yet supported on WIN32.</p>
