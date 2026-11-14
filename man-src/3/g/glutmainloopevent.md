---
title: "glutmainloopevent(3)"
name: "glutmainloopevent"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutmainloopevent/"
description: "glutMainLoopEvent – Dispatches all pending events."
---

<p><code>glutMainLoopEvent</code> &#8211; Dispatches all pending events.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; mainloop</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutMainLoopEvent void</p>
<h2>Description</h2>
<p>The general outline of this function is to first drain the queue of windowsystem events, in most cases dispatching each as it is found. After the queue is empty, we check for timer-based events, coalesced window events (e.g., redisplays), and windows that need to be closed. </p>
<p> The cross-reference section for this function&#8217;s documentation should ideally contain every callback, but the list would be tediously long and prone to omissions. </p>
<h2>Caveats</h2>
<p>Does not necessarily dispatch events that are received Bf Li<br />
&nbsp;<wbr>after Ef<br />
&nbsp;<wbr>&nbsp;<wbr>this function starts processing. </p>
<p> At first glance, this function may not seem to afford any new capability that you couldn&#8217;t get with an idle callback or glutLeaveMainLoop(). However there are other GLUT-like libraries that may have their own window event processing loops. Having glutMainLoopEvent() allows you to ask OpenGLUT to do its work in a batch, then return to whatever processing the other library (or libraries) require. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutidlefunc/">glutIdleFunc</a>(3) <a href="/docs/linux/man/3-glutleavemainloop/">glutLeaveMainLoop</a>(3) <a href="/docs/linux/man/3-glutmainloop/">glutMainLoop</a>(3)</p>
