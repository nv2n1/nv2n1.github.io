---
title: "glutchangetosubmenu(3)"
name: "glutchangetosubmenu"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutchangetosubmenu/"
description: "glutChangeToSubMenu – Replace a menu entry with a submenu."
---

<p><code>glutChangeToSubMenu</code> &#8211; Replace a menu entry with a submenu.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; menus</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutChangeToSubMenu int item const char *label int subMenuID</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>item Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Integer position down the list </p>
<p> Bf Em<br />
&nbsp;<wbr>label Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Submenu item text </p>
<p> Bf Em<br />
&nbsp;<wbr>subMenuID Ef<br />
&nbsp;<wbr>Submenu identifier</p>
<h2>Description</h2>
<p>Walks the list of the menu items and replaces the numbered Bf Sy<br />
&nbsp;<wbr>item Ef<br />
&nbsp;<wbr>in the list with the given submenu. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutaddmenuentry/">glutAddMenuEntry</a>(3) <a href="/docs/linux/man/3-glutaddsubmenu/">glutAddSubMenu</a>(3) <a href="/docs/linux/man/3-glutchangetomenuentry/">glutChangeToMenuEntry</a>(3) <a href="/docs/linux/man/3-glutremovemenuitem/">glutRemoveMenuItem</a>(3)</p>
