---
title: "glutcreatewindow(3)"
name: "glutcreatewindow"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutcreatewindow/"
description: "glutCreateWindow – Create a new top-level window"
---

<p><code>glutCreateWindow</code> &#8211; Create a new top-level window</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; window</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft int Fn glutCreateWindow const char* title</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>title Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Title for created window</p>
<h2>Description</h2>
<p>This function sends a request for a window to be constructed. OpenGLUT immediately constructs a data structure to track further events with the window, on the theory that eventually the window manager will get back to us with a real window. This allows us to begin registering callbacks immediately. </p>
<p> In fact, you Bf Em<br />
&nbsp;<wbr>must Ef<br />
&nbsp;<wbr>&nbsp;<wbr>register a display callback via glutDisplayFunc() before you enter glutMainLoop(). </p>
<p> For onscreen windows, you should not depend upon the window concretely existing or being visibile until you are told that it exists and is visible via a registered callback. </p>
<p> The return value is an Bf Sy<br />
&nbsp;<wbr>int. Ef<br />
&nbsp;<wbr>&nbsp;<wbr>It should be positive for valid windows or 0 if failure occurred for some reason (Though traditional GLUT tends to bail out and abort rather than returning errors.) The integer is your Bf Li<br />
&nbsp;<wbr>window id Ef<br />
&nbsp;<wbr>.&nbsp;<wbr>&nbsp;<wbr>Old GLUT promises that these integers are &#8220;small&#8221;; we do not reuse old Bf Li<br />
&nbsp;<wbr>id Ef<br />
&nbsp;<wbr>s, but do produce them sequentially. </p>
<p> You can change the title later via glutSetWindowTitle(). </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutdestroywindow/">glutDestroyWindow</a>(3) <a href="/docs/linux/man/3-glutcreatesubwindow/">glutCreateSubWindow</a>(3) <a href="/docs/linux/man/3-glutsetwindowtitle/">glutSetWindowTitle</a>(3) <a href="/docs/linux/man/3-glutcreatemenuwindow/">glutCreateMenuWindow</a>(3)</p>
