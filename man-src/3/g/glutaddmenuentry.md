---
title: "glutaddmenuentry(3)"
name: "glutaddmenuentry"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutaddmenuentry/"
description: "glutAddMenuEntry – Append an item to the current menu."
---

<p><code>glutAddMenuEntry</code> &#8211; Append an item to the current menu.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; menus</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutAddMenuEntry const char *label int value</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>label Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Menu item text </p>
<p> Bf Em<br />
&nbsp;<wbr>value Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Menu item callback value</p>
<h2>Description</h2>
<p>Inserts a given ( Bf Sy<br />
&nbsp;<wbr>label, Ef<br />
&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>value) Ef<br />
&nbsp;<wbr>pair into the current menu. Bf Sy<br />
&nbsp;<wbr>label Ef<br />
&nbsp;<wbr>is the text displayed in the menu; Bf Sy<br />
&nbsp;<wbr>value Ef<br />
&nbsp;<wbr>is the identifier received by the callback when the item is selected. </p>
<p> The new entry is added to the end of the menu. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutaddsubmenu/">glutAddSubMenu</a>(3) <a href="/docs/linux/man/3-glutchangetomenuentry/">glutChangeToMenuEntry</a>(3) <a href="/docs/linux/man/3-glutchangetosubmenu/">glutChangeToSubMenu</a>(3) <a href="/docs/linux/man/3-glutremovemenuitem/">glutRemoveMenuItem</a>(3)</p>
