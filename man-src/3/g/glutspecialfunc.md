---
title: "glutspecialfunc(3)"
name: "glutspecialfunc"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutspecialfunc/"
description: "glutSpecialFunc – Sets the Special callback for the current window"
---

<p><code>glutSpecialFunc</code> &#8211; Sets the Special callback for the current window</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; input</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutSpecialFunc void( *callback )( int key int x int y )</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>callback Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Client function for keyboard event.</p>
<h2>Description</h2>
<p>Registers a Bf Sy<br />
&nbsp;<wbr>callback Ef<br />
&nbsp;<wbr>for OpenGLUT to call when the user presses &quot;special&quot; keys on the keyboard. </p>
<p> The special callback handles some additional keys that are not covered under plain &quot;keyboard&quot; events. The Bf Sy<br />
&nbsp;<wbr>key Ef<br />
&nbsp;<wbr>that is passed to the&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>callback Ef<br />
&nbsp;<wbr>is one of an enumerated set. The association to keys on your keyboard should be obvious. Their GLUT symbol names are: </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_KEY_F1 Ef<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_KEY_F2 Ef<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_KEY_F3 Ef<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_KEY_F4 Ef<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_KEY_F5 Ef<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_KEY_F6 Ef<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_KEY_F7 Ef<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_KEY_F8 Ef<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_KEY_F9 Ef<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_KEY_F10 Ef<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_KEY_F11 Ef<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_KEY_F12 Ef<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_KEY_LEFT Ef<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_KEY_UP Ef<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_KEY_RIGHT Ef<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_KEY_DOWN Ef<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_KEY_PAGE_UP Ef<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_KEY_PAGE_DOWN Ef<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_KEY_HOME Ef<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_KEY_END Ef<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_KEY_INSERT Ef<br />
&nbsp;<wbr> </p>
<p> To receive other keys, see glutKeyboardFunc(). </p>
<p> This callback is bound to the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>. </p>
<h2>Caveats</h2>
<p>Many keys are not included; nor is it possible to apply qualifiers such as the Shift or Ctrl key to these keys. </p>
<p> Windows created via glutCreateMenuWindow() always cascade keyboard and mouse events to their parent. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutspecialupfunc/">glutSpecialUpFunc</a>(3) <a href="/docs/linux/man/3-glutkeyboardfunc/">glutKeyboardFunc</a>(3)</p>
