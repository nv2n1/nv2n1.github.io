---
title: "glutinit(3)"
name: "glutinit"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutinit/"
description: "glutInit – Initialize OpenGLUT data structures."
---

<p><code>glutInit</code> &#8211; Initialize OpenGLUT data structures.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; mainloop</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutInit int *pargc char **argv</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>pargc Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Pointer to something like main()&#8217;s&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>argc. Ef<br />
&nbsp;<wbr> </p>
<p> Bf Em<br />
&nbsp;<wbr>argv Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Something like main()&#8217;s&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>argv. Ef<br />
&nbsp;<wbr></p>
<h2>Description</h2>
<p>This function should be called once, near the start of any GLUT, freeglut, or OpenGLUT program. It serves two vital roles: </p>
<p>&nbsp;<wbr>&#8211; It allows OpenGLUT to initialize internal structures.<br />
&nbsp;<wbr>&#8211; It allows OpenGLUT to process command-line arguments to control the initial window position, etc. </p>
<p> You should take note of the interaction between glutInit() and the related functions such as glutInitWindowPosition(). OpenGLUT always uses the most recent configuration information, so if you call glutInit(), then glutInitWindowPosition(), you prevent the user from controlling the initial window position via a command-line parameter. </p>
<p> glutInit() will remove from Bf Sy<br />
&nbsp;<wbr>pargc, Ef<br />
&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>argv Ef<br />
&nbsp;<wbr> any parameters that it recognizes in the command line. The following command-line parameters are suported: </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>-display Ef<br />
&nbsp;<wbr> Bf Li<br />
&nbsp;<wbr>display-id Ef<br />
&nbsp;<wbr> This allows connection to an alternate X server.<br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>-geometry Ef<br />
&nbsp;<wbr> Bf Li<br />
&nbsp;<wbr>geometry-spec Ef<br />
&nbsp;<wbr> This takes width, height, and window position. The position is given as a signed value (negative values being distance from the far boundary of the screen). For example, a window geometry of 5&#215;7+11-17 is 5 pixels wide, 7 pixels tall, 11 pixels from the left, and 17 pixels from the bottom edge of the screen.<br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>-direct Ef<br />
&nbsp;<wbr>Insist on only OpenGL direct rendering. Direct rendering is normally requested but indirect is normally accepted. Bf Sy<br />
&nbsp;<wbr>-direct Ef<br />
&nbsp;<wbr>is not always available. See Bf Sy<br />
&nbsp;<wbr>-indirect. Ef<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>-indirect Ef<br />
&nbsp;<wbr>Attempt only indirect OpenGL rendering. Bf Sy<br />
&nbsp;<wbr>-indirect Ef<br />
&nbsp;<wbr>is always available. See Bf Sy<br />
&nbsp;<wbr>-direct. Ef<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>-iconic Ef<br />
&nbsp;<wbr>Open the window in iconized form.<br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>-gldebug Ef<br />
&nbsp;<wbr>Print any detected OpenGL errors via glutReportErrors(). Presently done at the bottom of glutMainLoopEvent().<br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>-sync Ef<br />
&nbsp;<wbr>Synchronize the window system communications heavily. </p>
<p> Additionally, this function checks whether the environment variable Bf Sy<br />
&nbsp;<wbr>GLUT_FPS Ef<br />
&nbsp;<wbr>is defined&nbsp;<wbr>(only on UNIX_X11); if so, OpenGLUT will periodically print the average number of times per second that your program calls glutSwapBuffers(). </p>
<h2>Caveats</h2>
<p>You really should always call this, even if you are a WIN32 user. It provides a way for the user to directly inform OpenGLUT about preferences without the application needing to explicitly deal with those issues. This is also where OpenGLUT retrieves your program&#8217;s name to help disambiguate error and warning messages it may be forced to emit. </p>
<p> Option Bf Sy<br />
&nbsp;<wbr>-sync Ef<br />
&nbsp;<wbr>sets a flag, but is not actually used at this time. </p>
<p> Lots of code does XFlush() on the X server, regardless of whether Bf Sy<br />
&nbsp;<wbr>-sync Ef<br />
&nbsp;<wbr>is specified.&nbsp;<wbr>&nbsp;<wbr>Much of that appears to be required in order to support direct client invocation of&nbsp;<wbr>&nbsp;<wbr>glutMainLoopEvent(), regrettably. However, if one calls glutMainLoop(), instead, we might avoid gratuitous XFlush()&nbsp;<wbr>calls.&nbsp;<wbr>&nbsp;<wbr>(That last sentence isn&#8217;t particularly germain to this function, but there&#8217;s no better place to make this remark at this time.)&nbsp;<wbr>Even for glutMainLoopEvent(), we may be able to coalesce many XFlush()&nbsp;<wbr>calls. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutinitwindowposition/">glutInitWindowPosition</a>(3) <a href="/docs/linux/man/3-glutinitwindowsize/">glutInitWindowSize</a>(3) <a href="/docs/linux/man/3-glutinitdisplaymode/">glutInitDisplayMode</a>(3) <a href="/docs/linux/man/3-glutinitdisplaystring/">glutInitDisplayString</a>(3) <a href="/docs/linux/man/3-glutcreatewindow/">glutCreateWindow</a>(3) <a href="/docs/linux/man/3-glutdisplayfunc/">glutDisplayFunc</a>(3) <a href="/docs/linux/man/3-glutmainloop/">glutMainLoop</a>(3) <a href="/docs/linux/man/3-glutmainloopevent/">glutMainLoopEvent</a>(3) <a href="/docs/linux/man/3-glutreporterrors/">glutReportErrors</a>(3) <a href="/docs/linux/man/3-glutswapbuffers/">glutSwapBuffers</a>(3)</p>
