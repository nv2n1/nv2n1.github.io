---
title: "glutsetwindow(3)"
name: "glutsetwindow"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutsetwindow/"
description: "glutSetWindow – Select the <i>current window</i>"
---

<p><code>glutSetWindow</code> &#8211; Select the &lt;i&gt;current window&lt;/i&gt;</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; window</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutSetWindow int ID</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>ID Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Window identifier</p>
<h2>Description</h2>
<p>Sets the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>&nbsp;<wbr>to&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>ID. Ef<br />
&nbsp;<wbr> </p>
<p> All OpenGL rendering goes to the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>. Many OpenGLUT functions also implicitly use the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>. </p>
<p> Many OpenGLUT callback operations are tied to a window. When your callback is invoked, OpenGLUT will set that particular window to be the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>. However, some callbacks&#8212;such as that registered via glutIdleFunc()&#8212;do not have associated windows. If a callback is not associated to a particular window, then when OpenGLUT invokes that callback you should Bf Em<br />
&nbsp;<wbr>always Ef<br />
&nbsp;<wbr>&nbsp;<wbr>use glutSetWindow()&nbsp;<wbr>to select the appropriate window before doing any OpenGL rendering or doing any OpenGLUT window-related operations. </p>
<p> There may be cases when you can get away with assuming that the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>&nbsp;<wbr>is unchanged since some prior time, but OpenGLUT has considerable liberaty with respect to when it invokes your functions. Also, your program may add more windows or more operations on other windows as you develop it. </p>
<p> Lastly, this is a convenient way to select among multiple windows for drawing without actually waiting for that window&#8217;s display callback. Simply set the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>&nbsp;<wbr>and draw immediately.&nbsp;<wbr>&nbsp;<wbr>This is not always advisable, but may be practical. </p>
<p> It is an error to set the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>&nbsp;<wbr>to a non-existant window (e.g., one that you have closed). A warning will be printed on Bf Sy<br />
&nbsp;<wbr>stderr Ef<br />
&nbsp;<wbr>if you try to do so, and the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>&nbsp;<wbr>should be unchanged. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutgetwindow/">glutGetWindow</a>(3)</p>
