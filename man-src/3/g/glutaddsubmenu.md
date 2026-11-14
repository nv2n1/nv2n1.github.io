---
title: "glutaddsubmenu(3)"
name: "glutaddsubmenu"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutaddsubmenu/"
description: "glutAddSubMenu – Append a submenu to the current menu."
---

<p><code>glutAddSubMenu</code> &#8211; Append a submenu to the current menu.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; menus</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutAddSubMenu const char *label int subMenuID</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>label Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Submenu item text </p>
<p> Bf Em<br />
&nbsp;<wbr>subMenuID Ef<br />
&nbsp;<wbr>Submenu identifier</p>
<h2>Description</h2>
<p>Attaches an existing menu as a submenu of the current menu. Bf Sy<br />
&nbsp;<wbr>label Ef<br />
&nbsp;<wbr>is the text used for the item in the menu. Bf Sy<br />
&nbsp;<wbr>subMenuID Ef<br />
&nbsp;<wbr>is the identifier of an existing menu to be appended as a submenu. </p>
<p> The submenu is added to the end of the menu. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutcreatemenu/">glutCreateMenu</a>(3) <a href="/docs/linux/man/3-glutaddmenuentry/">glutAddMenuEntry</a>(3)</p>
