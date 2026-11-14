---
title: "glutcreatesubwindow(3)"
name: "glutcreatesubwindow"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutcreatesubwindow/"
description: "glutCreateSubWindow – Create a subwindow"
---

<p><code>glutCreateSubWindow</code> &#8211; Create a subwindow</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; window</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft int Fn glutCreateSubWindow int parentID int x int y int w int h</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>parentID Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Parent window identifier </p>
<p> Bf Em<br />
&nbsp;<wbr>x Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Horizontal position of subwindow </p>
<p> Bf Em<br />
&nbsp;<wbr>y Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Vertical position of subwindow </p>
<p> Bf Em<br />
&nbsp;<wbr>w Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Width of subwindow </p>
<p> Bf Em<br />
&nbsp;<wbr>h Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Height of subwindow</p>
<h2>Description</h2>
<p>In almost every regard that is important to you, a subwindow is like a top-level window. It has a window id; it has its own set of event callbacks; you can render to it; you are notified of its creation; &#8230; </p>
<p> A subwindow lives inside of some other window (possibly a top-level window, possibly another subwindow). Because of this, it generally only interacts with other windows of your own creation, hence it is not subjected to a window manager. This is the primary source for its differences from a top-level window: </p>
<p>&nbsp;<wbr>&#8211; There are no borders or decorations.<br />
&nbsp;<wbr>&#8211; There is no title bar, hence no title.<br />
&nbsp;<wbr>&#8211; Requests tend to be acted on a little more directly, without interference from a window manager.<br />
&nbsp;<wbr>&#8211; The subwindow inherits the display mode of its parent. </p>
<p> Like a top-level window, you Bf Em<br />
&nbsp;<wbr>must Ef<br />
&nbsp;<wbr>&nbsp;<wbr>register a display callback function if you wish to use glutMainloop(). </p>
<p> A notable case where this function can fail is for offscreen windows. A coherent concept of a subwindow of an offscreen window would introduce more complication than is presently believed to be worthwhile. Attempting such a window presently just fails. Failure is denoted by a 0 Bf Li<br />
&nbsp;<wbr>window id Ef<br />
&nbsp;<wbr>&nbsp;<wbr>being returned. </p>
<p> Subwindows can be very useful for partitioning a window into GUI elements: They have their own input callbacks, so you don&#8217;t have to figure out which window an event is for. Graphics are clipped to the boundaries of your subwindows, so you do not need to worry much about where your drawing goes. Because windows and subwindows work almost identically from the perspective of a GLUT program, it is relatively easy to move a cluster of related controls into a separate top-level window&#8212;or, conversely, embed what was a top-level window inside of another window. OpenGLUT can also report some basic statistics about your (sub)window, relieving you of the duty of tracking all of that information for yourself. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutcreatewindow/">glutCreateWindow</a>(3) <a href="/docs/linux/man/3-glutdestroywindow/">glutDestroyWindow</a>(3) <a href="/docs/linux/man/3-glutcreatemenuwindow/">glutCreateMenuWindow</a>(3)</p>
