---
title: "glutdestroywindow(3)"
name: "glutdestroywindow"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutdestroywindow/"
description: "glutDestroyWindow – Destroy a window and associated subwindows"
---

<p><code>glutDestroyWindow</code> &#8211; Destroy a window and associated subwindows</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; window</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutDestroyWindow int windowID</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>windowID Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Window identifier</p>
<h2>Description</h2>
<p>After this function is invoked, the only further event that may be delivered for your window is the one for its destruction. All other events should be discarded. </p>
<p> Once a window has been destroyed, further attempts to use the window named by Bf Sy<br />
&nbsp;<wbr>windowID Ef<br />
&nbsp;<wbr>are undefined.&nbsp;<wbr>&nbsp;<wbr>OpenGLUT generally tries to be sensible, and should not recycle the dead Bf Sy<br />
&nbsp;<wbr>windowID, Ef<br />
&nbsp;<wbr>but you should treat a destroyed window much like a pointer to deallocated memory and try not to use it. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutcreatewindow/">glutCreateWindow</a>(3)</p>
