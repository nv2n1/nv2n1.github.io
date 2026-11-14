---
title: "glutmainloop(3)"
name: "glutmainloop"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutmainloop/"
description: "glutMainLoop – The standard GLUT event loop entry point."
---

<p><code>glutMainLoop</code> &#8211; The standard GLUT event loop entry point.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; mainloop</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutMainLoop void</p>
<h2>Description</h2>
<p>This is the main driving force for an event-driven OpenGLUT program. It alternates between calling glutMainLoopEvent() to process pending events and then either sleeping or calling your idle function (see glutIdleFunc()). </p>
<p> This function Bf Li<br />
&nbsp;<wbr>can Ef<br />
&nbsp;<wbr>&nbsp;<wbr>return, but GLUT&#8217;s version of this function never returned. And you must do special things to OpenGLUT to cause OpenGLUT&#8217;s version to return. </p>
<p> The cross-reference section for this function&#8217;s documentation should ideally contain every callback, but the list would be tediously long and prone to omissions. </p>
<h2>Caveats</h2>
<p>For OpenGLUT developers&#8217; internal documentation: Runs until the Bf Sy<br />
&nbsp;<wbr>ExecState Ef<br />
&nbsp;<wbr>changes to&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_EXEC_STATE_STOP. Ef<br />
&nbsp;<wbr> </p>
<h2>Bugs</h2>
<p>Talking to other message systems (e.g., network layers) can be a bit bothersome under the GLUT event model. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutmainloopevent/">glutMainLoopEvent</a>(3) <a href="/docs/linux/man/3-glutleavemainloop/">glutLeaveMainLoop</a>(3) <a href="/docs/linux/man/3-glutidlefunc/">glutIdleFunc</a>(3)</p>
