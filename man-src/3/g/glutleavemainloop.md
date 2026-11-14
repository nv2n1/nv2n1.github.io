---
title: "glutleavemainloop(3)"
name: "glutleavemainloop"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutleavemainloop/"
description: "glutLeaveMainLoop – Breaks out of OpenGLUT’s glutMainLoop()"
---

<p><code>glutLeaveMainLoop</code> &#8211; Breaks out of OpenGLUT&#8217;s glutMainLoop()</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; mainloop</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutLeaveMainLoop void</p>
<h2>Description</h2>
<p>This function allows you to unilaterally tell OpenGLUT that you are done and wish to exit. This is useful if you have also told OpenGLUT to return to you rather than to call exit() directly. </p>
<h2>Todo</h2>
<p>Could use longjmp(); see oghTakeActionOnWindowClose(). This would let us terminate the entire loop immediately. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutmainloop/">glutMainLoop</a>(3) <a href="/docs/linux/man/3-exit/">exit</a>(3)</p>
