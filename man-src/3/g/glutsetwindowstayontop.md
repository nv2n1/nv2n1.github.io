---
title: "glutsetwindowstayontop(3)"
name: "glutsetwindowstayontop"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutsetwindowstayontop/"
description: "glutSetWindowStayOnTop – Set stay on top mode for current window"
---

<p><code>glutSetWindowStayOnTop</code> &#8211; Set stay on top mode for current window</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; experimental</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutSetWindowStayOnTop int enable</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>enable Ef<br />
&nbsp;<wbr>Either&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GL_TRUE Ef<br />
&nbsp;<wbr>or&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GL_FALSE Ef<br />
&nbsp;<wbr></p>
<h2>Description</h2>
<h2>Caveats</h2>
<p>Does not work on all window managers. </p>
<p> Sends the Icewm style message to all window managers (KDE, twm, blackbox, ratpoison, amiwm, and whatever others you have). Can we detect Icewm reliably and only send the Icewm formatted message for Icewm? Possibbly harmless as it stands, but looks wrong. </p>
<h2>Todo</h2>
<p>Can a glutGet() be defined to tell us whether a window can be made to stay on top? Or whether a window has (successfully) been marked for staying on top? </p>
<p> Should walk the tree of menus and glutPopWindow() (or all windows that are of menu-window type?). </p>
<p> Investigate making a workalike variant using glutPopWindow() to mimic the feature where not directly supported.</p>
