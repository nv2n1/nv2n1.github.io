---
title: "glutsetmenudata(3)"
name: "glutsetmenudata"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutsetmenudata/"
description: "glutSetMenuData – Store menu user data pointer"
---

<p><code>glutSetMenuData</code> &#8211; Store menu user data pointer</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; menus</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutSetMenuData void *data</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>data Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Client pointer data</p>
<h2>Description</h2>
<p>glutSetMenuData() associates an arbitrary user data pointer, Bf Sy<br />
&nbsp;<wbr>data, Ef<br />
&nbsp;<wbr>with the&nbsp;<wbr> Bf Li<br />
&nbsp;<wbr>current menu Ef<br />
&nbsp;<wbr>. OpenGLUT does not interpret this pointer in any way, but merely stores it for you in the menu structure. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutgetmenudata/">glutGetMenuData</a>(3)</p>
