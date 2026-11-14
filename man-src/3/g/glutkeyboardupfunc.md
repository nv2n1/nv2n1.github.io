---
title: "glutkeyboardupfunc(3)"
name: "glutkeyboardupfunc"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutkeyboardupfunc/"
description: "glutKeyboardUpFunc – Sets the keyboard key release callback for the current window."
---

<p><code>glutKeyboardUpFunc</code> &#8211; Sets the keyboard key release callback for the current window.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; input</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutKeyboardUpFunc void( *callback )( unsigned char key int x int y )</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>callback Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Client hook for ASCII key releases.</p>
<h2>Description</h2>
<p>This function provides a way to detect the release of a keyboard key. The keys are reported exactly as with glutKeyboardFunc(), save that the Bf Sy<br />
&nbsp;<wbr>callback Ef<br />
&nbsp;<wbr>registered via this function is used to report the event. </p>
<p> This callback is bound to the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>. </p>
<h2>Caveats</h2>
<p>Windows created via glutCreateMenuWindow() always cascade keyboard and mouse events to their parent. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutkeyboardfunc/">glutKeyboardFunc</a>(3) <a href="/docs/linux/man/3-glutspecialupfunc/">glutSpecialUpFunc</a>(3)</p>
