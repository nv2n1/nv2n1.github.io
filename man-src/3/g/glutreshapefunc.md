---
title: "glutreshapefunc(3)"
name: "glutreshapefunc"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutreshapefunc/"
description: "glutReshapeFunc – Sets the Reshape callback for the current window."
---

<p><code>glutReshapeFunc</code> &#8211; Sets the Reshape callback for the current window.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; windowcallback</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutReshapeFunc void( *callback )( int w int h )</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>callback Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Client function for reshape-window event.</p>
<h2>Description</h2>
<p>This registers a function with OpenGLUT, which OpenGLUT will invoke whenever the window is reshaped or resized. Your callback is only invoked when the host window system has actually changed the window size. </p>
<p> The parameters to your callback are the new width and height for your window. </p>
<p> If you do not provide a reshape callback, OpenGLUT will simply call glViewport(0,0, Bf Sy<br />
&nbsp;<wbr>w, Ef<br />
&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>h). Ef<br />
&nbsp;<wbr> </p>
<p> This callback is bound to the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>. </p>
<p> To ask OpenGLUT about the present dimensions of the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>, you can use glutGet(). </p>
<h2>Caveats</h2>
<p>Unlike other callbacks, GLUT has an Bf Em<br />
&nbsp;<wbr>active Ef<br />
&nbsp;<wbr>&nbsp;<wbr>default behavior if you do not set this.&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(Most event types passively do nothing if you do not specify a callback to handle them.) </p>
<p> The reshape callback should always be called, if registered, when your window is first created. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutget/">glutGet</a>(3) <a href="/docs/linux/man/3-glutreshapewindow/">glutReshapeWindow</a>(3)</p>
