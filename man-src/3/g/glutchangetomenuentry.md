---
title: "glutchangetomenuentry(3)"
name: "glutchangetomenuentry"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutchangetomenuentry/"
description: "glutChangeToMenuEntry – Replace a menu entry with an item."
---

<p><code>glutChangeToMenuEntry</code> &#8211; Replace a menu entry with an item.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; menus</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutChangeToMenuEntry int item const char *label int value</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>item Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Integer position down the list </p>
<p> Bf Em<br />
&nbsp;<wbr>label Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Menu item text </p>
<p> Bf Em<br />
&nbsp;<wbr>value Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Menu item callback value</p>
<h2>Description</h2>
<p>Walks the list of the menu items and replaces the numbered Bf Sy<br />
&nbsp;<wbr>item Ef<br />
&nbsp;<wbr>in the list with the given definition. Except that it replaces a pre-existing Bf Sy<br />
&nbsp;<wbr>item, Ef<br />
&nbsp;<wbr>this function is much like glutAddMenuEntry(). </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutaddmenuentry/">glutAddMenuEntry</a>(3) <a href="/docs/linux/man/3-glutaddsubmenu/">glutAddSubMenu</a>(3) <a href="/docs/linux/man/3-glutchangetosubmenu/">glutChangeToSubMenu</a>(3) <a href="/docs/linux/man/3-glutremovemenuitem/">glutRemoveMenuItem</a>(3)</p>
