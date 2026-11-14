---
title: "glutmenustatefunc(3)"
name: "glutmenustatefunc"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutmenustatefunc/"
description: "glutMenuStateFunc – Deprecated variant of glutMenuStatusFunc()"
---

<p><code>glutMenuStateFunc</code> &#8211; Deprecated variant of glutMenuStatusFunc()</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; deprecated</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutMenuStateFunc void( *callback )( int status )</p>
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
<p> This callback is bound to Bf Em<br />
&nbsp;<wbr>both Ef<br />
&nbsp;<wbr>&nbsp;<wbr>the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>&nbsp;<wbr>and the Bf Li<br />
&nbsp;<wbr>current menu Ef<br />
&nbsp;<wbr>. </p>
<h2>Caveats</h2>
<p>Obsolete. Depcreated. </p>
<h2>Bugs</h2>
<p>Your callback is not actually called presently. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutmenustatusfunc/">glutMenuStatusFunc</a>(3)</p>
