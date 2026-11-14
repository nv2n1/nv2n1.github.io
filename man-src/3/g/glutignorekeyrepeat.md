---
title: "glutignorekeyrepeat(3)"
name: "glutignorekeyrepeat"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutignorekeyrepeat/"
description: "glutIgnoreKeyRepeat – Set autorepeat status."
---

<p><code>glutIgnoreKeyRepeat</code> &#8211; Set autorepeat status.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; inputstate</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutIgnoreKeyRepeat int ignore</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>ignore Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Whether to ignore autorepeated keys.</p>
<h2>Description</h2>
<p>If Bf Sy<br />
&nbsp;<wbr>ignore Ef<br />
&nbsp;<wbr>is non-zero, then auto-repeat is disabled for keyboard callbacks for the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutsetkeyrepeat/">glutSetKeyRepeat</a>(3)</p>
