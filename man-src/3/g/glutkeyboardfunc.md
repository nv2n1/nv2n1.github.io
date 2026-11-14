---
title: "glutkeyboardfunc(3)"
name: "glutkeyboardfunc"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutkeyboardfunc/"
description: "glutKeyboardFunc – Sets the Keyboard callback for the current window."
---

<p><code>glutKeyboardFunc</code> &#8211; Sets the Keyboard callback for the current window.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; input</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutKeyboardFunc void( * callback )( unsigned char key int x int y )</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>callback Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Client function for keyboard event.</p>
<h2>Description</h2>
<p>This callback registration allows you to handle traditional ASCII keyboard input. A general rule of thumb is that if a key has a common ASCII code, then OpenGLUT assigns that code to the key and calls the Keyboard Bf Sy<br />
&nbsp;<wbr>callback Ef<br />
&nbsp;<wbr>with the ASCII code in the Bf Sy<br />
&nbsp;<wbr>key Ef<br />
&nbsp;<wbr>parameter. For other keys, you must use glutSpecialFunc(). Not all keys can be reported by OpenGLUT. </p>
<p> As a convenience, the mouse coordinates, relative to your window, are also returned. </p>
<p> This callback is bound to the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>. </p>
<h2>Caveats</h2>
<p>This function is not very international-friendly. </p>
<p> Windows created via glutCreateMenuWindow() always cascade keyboard and mouse events to their parent. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutkeyboardupfunc/">glutKeyboardUpFunc</a>(3) <a href="/docs/linux/man/3-glutspecialfunc/">glutSpecialFunc</a>(3)</p>
