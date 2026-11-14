---
title: "glutcopycolormap(3)"
name: "glutcopycolormap"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutcopycolormap/"
description: "glutCopyColormap – Copies a color map between windows."
---

<p><code>glutCopyColormap</code> &#8211; Copies a color map between windows.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; colormap</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutCopyColormap int window</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>window Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>The window to copy&nbsp;<wbr> Bf Li<br />
&nbsp;<wbr>to Ef<br />
&nbsp;<wbr></p>
<h2>Description</h2>
<p>Allows you to copy an entire color map from one window to another. This function copies Bf Em<br />
&nbsp;<wbr>from Ef<br />
&nbsp;<wbr>&nbsp;<wbr>the&nbsp;<wbr> Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>.&nbsp;<wbr>&nbsp;<wbr>It copies Bf Em<br />
&nbsp;<wbr>to Ef<br />
&nbsp;<wbr>&nbsp;<wbr>the indicated&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>window. Ef<br />
&nbsp;<wbr> Respects the current layer setting. </p>
<h2>Bugs</h2>
<p>Unimplemented. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutsetcolor/">glutSetColor</a>(3) <a href="/docs/linux/man/3-glutgetcolor/">glutGetColor</a>(3)</p>
