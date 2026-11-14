---
title: "xnoop(3)"
name: "xnoop"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xnoop/"
description: "XNoOp – No Operation"
---

<p>XNoOp &#8211; No Operation </p>
<h2>Syntax</h2>
<p>int XNoOp(Display *<i>display</i>);</p>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</dl>
<h2>Description</h2>
<p>The <code>XNoOp</code> function sends a <code>NoOperation</code> protocol request to the X server, thereby exercising the connection.</p>
<h2>See Also</h2>
<p><i>Xlib &#8211; C Language X Interface</i></p>
