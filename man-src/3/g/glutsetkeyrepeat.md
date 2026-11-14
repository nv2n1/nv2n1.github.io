---
title: "glutsetkeyrepeat(3)"
name: "glutsetkeyrepeat"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutsetkeyrepeat/"
description: "glutSetKeyRepeat – Sets autorepeat behavior for all OpenGLUT windows."
---

<p><code>glutSetKeyRepeat</code> &#8211; Sets autorepeat behavior for all OpenGLUT windows.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; inputstate</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutSetKeyRepeat int repeatMode</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>repeatMode Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>On, Off or Default.</p>
<h2>Description</h2>
<p>glutSetKeyRepeat() is similar to glutIgnoreKeyRepeat() but sets the behavior for OpenGLUT in general, rather than for a particular window. The options for Bf Sy<br />
&nbsp;<wbr>repeatMode Ef<br />
&nbsp;<wbr>are: </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_KEY_REPEAT_OFF Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
 Turn off repeat for all windows.<br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_KEY_REPEAT_ON Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
 Turn on repeat for all windows.<br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_KEY_REPEAT_DEFAULT Ef<br />
&nbsp;<wbr><br />
 Respect the window&#8217;s setting. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutignorekeyrepeat/">glutIgnoreKeyRepeat</a>(3)</p>
