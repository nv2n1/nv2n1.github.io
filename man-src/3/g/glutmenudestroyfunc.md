---
title: "glutmenudestroyfunc(3)"
name: "glutmenudestroyfunc"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutmenudestroyfunc/"
description: "glutMenuDestroyFunc – Destruction callback for menus."
---

<p><code>glutMenuDestroyFunc</code> &#8211; Destruction callback for menus.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; menucallback</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutMenuDestroyFunc void( *callback )( void )</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>callback Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Client menu destruction hook.</p>
<h2>Description</h2>
<p>When a menu is destroyed, OpenGLUT will call this hook, if defined on that menu. </p>
<p> This callback is Bf Em<br />
&nbsp;<wbr>not Ef<br />
&nbsp;<wbr>&nbsp;<wbr>bound to any window. </p>
<p> This callback Bf Em<br />
&nbsp;<wbr>is Ef<br />
&nbsp;<wbr>&nbsp;<wbr>bound to a specific menu. </p>
<h2>Caveats</h2>
<p>For emphasis, we repeat: This callback does not bind to any window. </p>
<h2>Todo</h2>
<p>What on Earth is rationale for this feature? Menus should only be destroyed when we ask them to be destroyed, or when their window is destroyed. In the former case, we already know that the menu is being destroyed because we requested it. In the latter case, it is easy for the client to track that if they care, via window-destruction callbacks. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutclosefunc/">glutCloseFunc</a>(3) <a href="/docs/linux/man/3-glutcreatemenu/">glutCreateMenu</a>(3) <a href="/docs/linux/man/3-glutdestroymenu/">glutDestroyMenu</a>(3)</p>
