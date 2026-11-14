---
title: "glutsetwindowdata(3)"
name: "glutsetwindowdata"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutsetwindowdata/"
description: "glutSetWindowData – Set the user data for the current window"
---

<p><code>glutSetWindowData</code> &#8211; Set the user data for the current window</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; window</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutSetWindowData void* data</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>data Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Arbitrary client-supplied pointer.</p>
<h2>Description</h2>
<p>This associates an arbitrary Bf Sy<br />
&nbsp;<wbr>void* Ef<br />
&nbsp;<wbr>value with the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>.&nbsp;<wbr>&nbsp;<wbr>This is especially useful in client-side callbacks that service many windows, if the client needs to know more about the window than OpenGLUT normally will provide. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutgetwindowdata/">glutGetWindowData</a>(3)</p>
