---
title: "glutreporterrors(3)"
name: "glutreporterrors"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutreporterrors/"
description: "glutReportErrors – Reports all available OpenGL errors."
---

<p><code>glutReportErrors</code> &#8211; Reports all available OpenGL errors.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; opengl</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutReportErrors void</p>
<h2>Description</h2>
<p>Displays as an OpenGLUT warning every OpenGL error that OpenGL remembers giving to us and which we have not processed. Uses gluErrorString(). </p>
<p> This is forcibly done by OpenGLUT periodically if &quot;-gldebug&quot; is one of the strings passed into glutInit() via rgv. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-gluerrorstring/">gluErrorString</a>(3) <a href="/docs/linux/man/3-glutinit/">glutInit</a>(3)</p>
