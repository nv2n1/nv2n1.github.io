---
title: "glutcreatemenu(3)"
name: "glutcreatemenu"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutcreatemenu/"
description: "glutCreateMenu – Create a new menu."
---

<p><code>glutCreateMenu</code> &#8211; Create a new menu.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; menus</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft int Fn glutCreateMenu void( *callback )( int value )</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>callback Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Client hook for the new menu.</p>
<h2>Description</h2>
<p>Create a menu with a callback bound to Bf Sy<br />
&nbsp;<wbr>callback, Ef<br />
&nbsp;<wbr>and return the menu&#8217;s integer id. </p>
<p> When the user makes a selection from this menu, Bf Sy<br />
&nbsp;<wbr>callback Ef<br />
&nbsp;<wbr>is invoked with the parameter&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>value, Ef<br />
&nbsp;<wbr> which comes from the ( Bf Sy<br />
&nbsp;<wbr>label, Ef<br />
&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>value) Ef<br />
&nbsp;<wbr>pair that is defined with glutAddMenuEntry(). </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutaddmenuentry/">glutAddMenuEntry</a>(3) <a href="/docs/linux/man/3-glutaddsubmenu/">glutAddSubMenu</a>(3) <a href="/docs/linux/man/3-glutdestroymenu/">glutDestroyMenu</a>(3)</p>
