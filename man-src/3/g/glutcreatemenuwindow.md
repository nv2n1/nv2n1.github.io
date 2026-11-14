---
title: "glutcreatemenuwindow(3)"
name: "glutcreatemenuwindow"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutcreatemenuwindow/"
description: "glutCreateMenuWindow – Create a client-controlled menu window."
---

<p><code>glutCreateMenuWindow</code> &#8211; Create a client-controlled menu window.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; experimental</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft int Fn glutCreateMenuWindow int parentID int x int y int w int h</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>parentID Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Parent window identifier. </p>
<p> Bf Em<br />
&nbsp;<wbr>x Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Horizontal coordinate on the screen. </p>
<p> Bf Em<br />
&nbsp;<wbr>y Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Vertical coordinate on the screen. </p>
<p> Bf Em<br />
&nbsp;<wbr>w Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Width of the new window. </p>
<p> Bf Em<br />
&nbsp;<wbr>h Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Height of the new window.</p>
<h2>Description</h2>
<p>This is a highly experimental function. It creates a menu-like window, of requested dimensions, and at a position relative to your current window. </p>
<p> The documentation for this function is currently the OpenGLUT Menu Window proposal. Variance from that proposal may generally be explained by the fact that this feature is highly experimental. It may also be explained by the fact that the implementation may simply be incomplete. </p>
<h2>Caveats</h2>
<p>Did you notice that this feature is highly experimental? </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutcreatewindow/">glutCreateWindow</a>(3) <a href="/docs/linux/man/3-glutcreatesubwindow/">glutCreateSubWindow</a>(3) <a href="/docs/linux/man/3-glutdestroywindow/">glutDestroyWindow</a>(3) <a href="/docs/linux/man/3-glutkeyboardfunc/">glutKeyboardFunc</a>(3) <a href="/docs/linux/man/3-glutkeyboardupfunc/">glutKeyboardUpFunc</a>(3) <a href="/docs/linux/man/3-glutspecialfunc/">glutSpecialFunc</a>(3) <a href="/docs/linux/man/3-glutspecialupfunc/">glutSpecialUpFunc</a>(3) <a href="/docs/linux/man/3-glutmotionfunc/">glutMotionFunc</a>(3) <a href="/docs/linux/man/3-glutpassivemotionfunc/">glutPassiveMotionFunc</a>(3) <a href="/docs/linux/man/3-glutmousefunc/">glutMouseFunc</a>(3) <a href="/docs/linux/man/3-glutmousewheelfunc/">glutMouseWheelFunc</a>(3)</p>
