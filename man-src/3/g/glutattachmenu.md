---
title: "glutattachmenu(3)"
name: "glutattachmenu"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutattachmenu/"
description: "glutAttachMenu – Attach the current menu to the current window."
---

<p><code>glutAttachMenu</code> &#8211; Attach the current menu to the current window.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; menus</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutAttachMenu int button</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>button Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Mouse button to bind to</p>
<h2>Description</h2>
<p>Associates the Bf Sy<br />
&nbsp;<wbr>button Ef<br />
&nbsp;<wbr>with the current menu in the current window. </p>
<h2>Todo</h2>
<p>Assumes 3 mouse buttons. (Actually Bf Sy<br />
&nbsp;<wbr>FREEGLUT_MAX_MENUS Ef<br />
&nbsp;<wbr>holds the assumed number of buttons.)&nbsp;<wbr>&nbsp;<wbr>Cannot bind to more buttons.&nbsp;<wbr>&nbsp;<wbr>Will not issue any warnings or errors if the user does not have enough buttons to reach your menu. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutcreatemenu/">glutCreateMenu</a>(3) <a href="/docs/linux/man/3-glutsetmenu/">glutSetMenu</a>(3) glutDetachMenu,3</p>
