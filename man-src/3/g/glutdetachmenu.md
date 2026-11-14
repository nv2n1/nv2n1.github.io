---
title: "glutdetachmenu(3)"
name: "glutdetachmenu"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutdetachmenu/"
description: "glutDetachMenu – Detach menu from the current window."
---

<p><code>glutDetachMenu</code> &#8211; Detach menu from the current window.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; menus</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutDetachMenu int button</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>button Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Mouse button to unbind from.</p>
<h2>Description</h2>
<p>If the given Bf Sy<br />
&nbsp;<wbr>button Ef<br />
&nbsp;<wbr>has a menu bound to it, this breaks the assocation. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutcreatemenu/">glutCreateMenu</a>(3) <a href="/docs/linux/man/3-glutdestroymenu/">glutDestroyMenu</a>(3) <a href="/docs/linux/man/3-glutattachmenu/">glutAttachMenu</a>(3)</p>
