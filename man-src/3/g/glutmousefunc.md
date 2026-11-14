---
title: "glutmousefunc(3)"
name: "glutmousefunc"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutmousefunc/"
description: "glutMouseFunc – Sets the mouse-button callback for the current window."
---

<p><code>glutMouseFunc</code> &#8211; Sets the mouse-button callback for the current window.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; input</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutMouseFunc void( *callback )( int button int state int x int y )</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>callback Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Client hook for mouse-buttons.</p>
<h2>Description</h2>
<p>Whenever a mouse button is pressed or released in an OpenGLUT window, OpenGLUT checks if that window has a mouse-button (Mouse) callback registered. If so, OpenGLUT gives the event to the handler. Bf Sy<br />
&nbsp;<wbr>button Ef<br />
&nbsp;<wbr>is the button number, starting from 0. Bf Sy<br />
&nbsp;<wbr>state Ef<br />
&nbsp;<wbr>is&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_UP Ef<br />
&nbsp;<wbr>or&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_DOWN Ef<br />
&nbsp;<wbr> to indicate the button&#8217;s new state. The other parameters are the mouse coordinates. </p>
<p> Mouse wheel motion can be reported as buttons. If you do not request otherwise, a wheel spun forward will act like a button clicking down, immediately followed by clicking up. Spinning the same wheel backward will act like a different button clicking. Mouse wheel pseudo-buttons are added after all real buttons. </p>
<p> While the button is held and the mouse is dragged, you receive mouse-motion events (glutMotionFunc()), even if the mouse is dragged out of the window. </p>
<p> This callback is bound to the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>. </p>
<h2>Caveats</h2>
<p>Reporting the wheel as buttons is actually inherited from X. freeglut added code to support this on WIN32. OpenGLUT inherited that support from freeglut. </p>
<p> Old GLUT defines the symbols Bf Sy<br />
&nbsp;<wbr>GLUT_LEFT_BUTTON, Ef<br />
&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_RIGHT_BUTTON, Ef<br />
&nbsp;<wbr>and&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_MIDDLE_BUTTON. Ef<br />
&nbsp;<wbr>However, mice can have more than 3 buttons, so these symbols are deprecated. </p>
<p> Windows created via glutCreateMenuWindow() always cascade keyboard and mouse events to their parent. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutmotionfunc/">glutMotionFunc</a>(3) <a href="/docs/linux/man/3-glutpassivemotionfunc/">glutPassiveMotionFunc</a>(3) <a href="/docs/linux/man/3-glutmousewheelfunc/">glutMouseWheelFunc</a>(3)</p>
