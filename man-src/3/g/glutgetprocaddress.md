---
title: "glutgetprocaddress(3)"
name: "glutgetprocaddress"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutgetprocaddress/"
description: "glutGetProcAddress – Determine if an OpenGLUT feature or extension is available."
---

<p><code>glutGetProcAddress</code> &#8211; Determine if an OpenGLUT feature or extension is available.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; openglut</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutGetProcAddress const char *procName</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>procName Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Procedure name.</p>
<h2>Description</h2>
<p>Given a function name, searches for the function (or &quot;procedure&quot;, hence &quot;Proc&quot;) in internal tables. If the function is found, a pointer to the function is returned. If the function is not found, Bf Sy<br />
&nbsp;<wbr>NULL Ef<br />
&nbsp;<wbr>is returned. </p>
<p> In addition to an internal OpenGLUT table, this function will also consult glX (on X systems) or wgl (on WIN32 and WINCE), if the OpenGLUT tables do not have the requested function. It should return any OpenGL, glX, or wgl function if those functions are available. </p>
<h2>Caveats</h2>
<p>The code makes no effort towards efficiency. It is advised that you cache the pointer retrieved from this function if you need a certain function repeatedly. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glxgetprocaddress/">glXGetProcAddress</a>(3) <a href="/docs/linux/man/3-wglgetprocaddress/">wglGetProcAddress</a>(3)</p>
