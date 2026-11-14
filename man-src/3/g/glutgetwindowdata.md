---
title: "glutgetwindowdata(3)"
name: "glutgetwindowdata"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutgetwindowdata/"
description: "glutGetWindowData – Get the user data for the current window"
---

<p><code>glutGetWindowData</code> &#8211; Get the user data for the current window</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; window</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void* Fn glutGetWindowData void</p>
<h2>Description</h2>
<p>This function will return whatever Bf Sy<br />
&nbsp;<wbr>void* Ef<br />
&nbsp;<wbr>value is associated with the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>&nbsp;<wbr>via glutSetWindowData(). This is Bf Sy<br />
&nbsp;<wbr>NULL Ef<br />
&nbsp;<wbr>if you did not associate a pointer with your window. This can be useful in a situation where you have a single callback function performing services for many windows. You Bf Em<br />
&nbsp;<wbr>could Ef<br />
&nbsp;<wbr>&nbsp;<wbr>keep track of the&nbsp;<wbr> Bf Li<br />
&nbsp;<wbr>window id Ef<br />
&nbsp;<wbr>s in a global list and search for the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>&nbsp;<wbr>in that list. But this is quicker than searching a data structure, and allows you to avoid the use of globals for this. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutsetwindowdata/">glutSetWindowData</a>(3)</p>
