---
title: "glutsetoption(3)"
name: "glutsetoption"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutsetoption/"
description: "glutSetOption – Allows you to set some general state/option variables."
---

<p><code>glutSetOption</code> &#8211; Allows you to set some general state/option variables.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; state</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutSetOption GLenum eWhat int value</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>eWhat Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Enumerated parameter ID. </p>
<p> Bf Em<br />
&nbsp;<wbr>value Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>New value.</p>
<h2>Description</h2>
<p>Stores the Bf Sy<br />
&nbsp;<wbr>value Ef<br />
&nbsp;<wbr>into a state variable named by Bf Sy<br />
&nbsp;<wbr>eWhat. Ef<br />
&nbsp;<wbr> </p>
<p> Allowable Bf Sy<br />
&nbsp;<wbr>eWhat Ef<br />
&nbsp;<wbr>IDs are: </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_ACTION_ON_WINDOW_CLOSE Ef<br />
&nbsp;<wbr><br />
 Controls what happens when a window is closed by the user or system. Bf Sy<br />
&nbsp;<wbr>GLUT_ACTION_EXIT Ef<br />
&nbsp;<wbr> will immediately exit the application (default). Bf Sy<br />
&nbsp;<wbr>GLUT_ACTION_GLUTMAINLOOP_RETURNS Ef<br />
&nbsp;<wbr> will immediately return from the main loop. Bf Sy<br />
&nbsp;<wbr>GLUT_ACTION_CONTINUE_EXECUTION Ef<br />
&nbsp;<wbr> will contine execution of remaining windows. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_INIT_DISPLAY_MODE Ef<br />
&nbsp;<wbr><br />
 An alternate way to set the display mode for a new window. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_INIT_WINDOW_HEIGHT Ef<br />
&nbsp;<wbr><br />
 An alternate way to set the height of new windows. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_INIT_WINDOW_WIDTH Ef<br />
&nbsp;<wbr><br />
 An alternate way to set the width of new windows. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_INIT_WINDOW_X Ef<br />
&nbsp;<wbr><br />
 An alternate way to set the initial horizontal position of new windows. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_INIT_WINDOW_Y Ef<br />
&nbsp;<wbr><br />
 An alternate way to set the initial vertical position of new windows. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_RENDERING_CONTEXT Ef<br />
&nbsp;<wbr><br />
 Set to either Bf Sy<br />
&nbsp;<wbr>GLUT_CREATE_NEW_CONTEXT Ef<br />
&nbsp;<wbr>or Bf Sy<br />
&nbsp;<wbr>GUT_USE_CURRENT_CONTEXT Ef<br />
&nbsp;<wbr>to indicate whether to share the current OpenGL rendering context with new windows. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_WINDOW_CURSOR Ef<br />
&nbsp;<wbr><br />
 Attempt to set the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>&#8216;s current cursor as if by glutSetCursor(). </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutget/">glutGet</a>(3) <a href="/docs/linux/man/3-glutdeviceget/">glutDeviceGet</a>(3) <a href="/docs/linux/man/3-glutgetmodifiers/">glutGetModifiers</a>(3) <a href="/docs/linux/man/3-glutlayerget/">glutLayerGet</a>(3) <a href="/docs/linux/man/3-glutdestroywindow/">glutDestroyWindow</a>(3) <a href="/docs/linux/man/3-glutmainloop/">glutMainLoop</a>(3) <a href="/docs/linux/man/3-glutinitdisplaymode/">glutInitDisplayMode</a>(3) <a href="/docs/linux/man/3-glutinit/">glutInit</a>(3) <a href="/docs/linux/man/3-glutinitwindowsize/">glutInitWindowSize</a>(3) <a href="/docs/linux/man/3-glutinitwindowposition/">glutInitWindowPosition</a>(3) <a href="/docs/linux/man/3-glutsetcursor/">glutSetCursor</a>(3)</p>
