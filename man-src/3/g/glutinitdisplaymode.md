---
title: "glutinitdisplaymode(3)"
name: "glutinitdisplaymode"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutinitdisplaymode/"
description: "glutInitDisplayMode – Set the window creation display mode."
---

<p><code>glutInitDisplayMode</code> &#8211; Set the window creation display mode.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; window</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutInitDisplayMode unsigned int displayMode</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>displayMode Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Requested display mode bitmask.</p>
<h2>Description</h2>
<p>glutInitDisplayMode() allows you to control the mode for subsequent OpenGLUT windows. </p>
<p> Allowable Bf Sy<br />
&nbsp;<wbr>displayMode Ef<br />
&nbsp;<wbr>is a combination of: </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_RGB Ef<br />
&nbsp;<wbr><br />
 Red, green, blue framebuffer. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_RGBA Ef<br />
&nbsp;<wbr><br />
 Red, green, blue, alpha framebuffer. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_INDEX Ef<br />
&nbsp;<wbr><br />
 Indexed color framebuffer. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_SINGLE Ef<br />
&nbsp;<wbr><br />
 Single-buffered mode. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_DOUBLE Ef<br />
&nbsp;<wbr><br />
 Double-buffered mode. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_ACCUM Ef<br />
&nbsp;<wbr><br />
 Accumulation buffer. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_ALPHA Ef<br />
&nbsp;<wbr><br />
 Alpha channel. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_DEPTH Ef<br />
&nbsp;<wbr><br />
 Depth buffering. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_STENCIL Ef<br />
&nbsp;<wbr><br />
 Stencil buffering. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_MULTISAMPLE Ef<br />
&nbsp;<wbr><br />
 Multisampling mode. (not always available) </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_STEREO Ef<br />
&nbsp;<wbr><br />
 Left and right framebuffers. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_LUMINANCE Ef<br />
&nbsp;<wbr><br />
 Greyscale color mode. </p>
<p> Additionally, the following Bf Li<br />
&nbsp;<wbr>experimental Ef<br />
&nbsp;<wbr>&nbsp;<wbr>features are implemented: </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_OFFSCREEN Ef<br />
&nbsp;<wbr><br />
 Offscreen windows are very much like onscreen windows that have been dragged off of the edge of the screen. The biggest issue is that offscreen windows do not support subwindows. Other than that, onscreen windows that are dragged off of the edge may not store graphics that you render (while Bf Sy<br />
&nbsp;<wbr>GLUT_OFFSCREEN Ef<br />
&nbsp;<wbr> windows do), and there is no way to drag an offscreen window onscreen for user interaction. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_BORDERLESS Ef<br />
&nbsp;<wbr><br />
 Borderless windows are very experimental, and their precise behavior is not set in stone. See also glutCreateMenuWindow(). </p>
<p> The following are Bf Li<br />
&nbsp;<wbr>defaults Ef<br />
&nbsp;<wbr>: </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_RGB Ef<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_SINGLE Ef<br />
&nbsp;<wbr> </p>
<h2>Caveats</h2>
<p>Some display mode features were introduced by OpenGLUT. </p>
<p> Not all features or combinations of features are valid for all platforms. </p>
<p> There is no way to change the display mode of an open window. </p>
<h2>Bugs</h2>
<p>Bf Sy<br />
&nbsp;<wbr>GLUT_OFFSCREEN Ef<br />
&nbsp;<wbr>windows do not work with nVidia cards/drivers.&nbsp;<wbr>&nbsp;<wbr>(Both Win32 and X11) </p>
<p> Bf Sy<br />
&nbsp;<wbr>GLUT_BORDERLESS Ef<br />
&nbsp;<wbr>seems to vary by the window manager on X11, though twm&nbsp;<wbr>(for example)&nbsp;<wbr>performs very similarly to WIN32. But KDE&#8217;s window manager&nbsp;<wbr>(for example)&nbsp;<wbr>does not let you send keystrokes to borderless windows without OpenGLUT hacks. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutcreatemenuwindow/">glutCreateMenuWindow</a>(3) <a href="/docs/linux/man/3-glutinit/">glutInit</a>(3) <a href="/docs/linux/man/3-glutinitwindowsize/">glutInitWindowSize</a>(3) <a href="/docs/linux/man/3-glutinitwindowposition/">glutInitWindowPosition</a>(3) <a href="/docs/linux/man/3-glutinitdisplaystring/">glutInitDisplayString</a>(3) <a href="/docs/linux/man/3-glutswapbuffers/">glutSwapBuffers</a>(3)</p>
