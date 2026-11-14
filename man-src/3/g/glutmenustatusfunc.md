---
title: "glutmenustatusfunc(3)"
name: "glutmenustatusfunc"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutmenustatusfunc/"
description: "glutMenuStatusFunc – Modern variant of glutMenuStateFunc()"
---

<p><code>glutMenuStatusFunc</code> &#8211; Modern variant of glutMenuStateFunc()</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; menucallback</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutMenuStatusFunc void( *callback )( int status int x int y )</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>callback Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Client menu status hook.</p>
<h2>Description</h2>
<p>Broadly, OpenGLUT operates in two modes. At any given time, it is either in menu mode (with a popup menu display, possibly with subitems) or it is not. </p>
<p> When moving from non-menu to menu status, Bf Sy<br />
&nbsp;<wbr>callback Ef<br />
&nbsp;<wbr>(if defined)&nbsp;<wbr>will be called with Bf Sy<br />
&nbsp;<wbr>GLUT_MENU_IN_USE Ef<br />
&nbsp;<wbr>.&nbsp;<wbr>&nbsp;<wbr>Conversely, when moving from menu to non-menu status, Bf Sy<br />
&nbsp;<wbr>callback Ef<br />
&nbsp;<wbr>(if defined)&nbsp;<wbr>will be called with Bf Sy<br />
&nbsp;<wbr>GLUT_MENU_NOT_IN_USE Ef<br />
&nbsp;<wbr>. </p>
<p> This differs from glutMenuStateFunc() in that Bf Sy<br />
&nbsp;<wbr>callback Ef<br />
&nbsp;<wbr>is also given the&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>x Ef<br />
&nbsp;<wbr>and&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>y Ef<br />
&nbsp;<wbr> coordinates of the mouse when the menu state transition took place. </p>
<p> This callback is bound to Bf Em<br />
&nbsp;<wbr>both Ef<br />
&nbsp;<wbr>&nbsp;<wbr>the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>&nbsp;<wbr>and the Bf Li<br />
&nbsp;<wbr>current menu Ef<br />
&nbsp;<wbr>. </p>
<h2>Bugs</h2>
<p>Your callback is not actually called presently. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutmenustatefunc/">glutMenuStateFunc</a>(3)</p>
