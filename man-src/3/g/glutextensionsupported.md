---
title: "glutextensionsupported(3)"
name: "glutextensionsupported"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutextensionsupported/"
description: "glutExtensionSupported – Determine if an OpenGL extension is available."
---

<p><code>glutExtensionSupported</code> &#8211; Determine if an OpenGL extension is available.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; opengl</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft int Fn glutExtensionSupported const char *extension</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>extension Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>A string-name of an extension.</p>
<h2>Description</h2>
<p>Returns 0 if OpenGLUT cannot determine that the requested extension is definitely present. Only checks extensions from glGetString(). </p>
<h2>Todo</h2>
<p>Wouldn&#8217;t this be simpler and clearer if we used strtok()? </p>
<p> Consider an ogWarning() if there is no current rendering context. </p>
<p> This is an ugly bit of code with 3 return statements, one of which is never reached. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glgetstring/">glGetString</a>(3)</p>
