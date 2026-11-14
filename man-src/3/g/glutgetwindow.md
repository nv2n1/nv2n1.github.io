---
title: "glutgetwindow(3)"
name: "glutgetwindow"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutgetwindow/"
description: "glutGetWindow – Return the current window identifier, 0 if undefined"
---

<p><code>glutGetWindow</code> &#8211; Return the current window identifier, 0 if undefined</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; window</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft int Fn glutGetWindow void</p>
<h2>Description</h2>
<p>glutGetWindow() returns the Bf Li<br />
&nbsp;<wbr>window id Ef<br />
&nbsp;<wbr>&nbsp;<wbr>of the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>.&nbsp;<wbr>&nbsp;<wbr>This is useful, e.g., if you have a generic function that is used with several windows and it needs to temporarily change to another window. (There is no window stack for you to use with pushes and pops. Do not be confused by glutPushWindow() and glutPopWindow(); those pushes and pops are Bf Em<br />
&nbsp;<wbr>not Ef<br />
&nbsp;<wbr>&nbsp;<wbr>stack-related!) </p>
<p> One cause for the function to return 0 is if you have called glutDestroyWindow() on the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>&nbsp;<wbr>and have done nothing to set a new window as current. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutsetwindow/">glutSetWindow</a>(3)</p>
