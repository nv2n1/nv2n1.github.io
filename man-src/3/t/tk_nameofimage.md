---
title: "tk_nameofimage(3)"
name: "tk_nameofimage"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_nameofimage/"
description: "Tk_NameOfImage – Return name of image."
---

<p>Tk_NameOfImage &#8211; Return name of image. </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
const char *
<code>Tk_NameOfImage</code>(<i>typePtr</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tk_ImageMaster <i>*masterPtr</i> (in) Token for image, which was passed to image manager&#8217;s <i>createProc</i> when the image was created. </p>
</dl>
<h2>Description</h2>
<p>This procedure is invoked by image managers to find out the name of an image. Given the token for the image, it returns the string name for the image. </p>
<h2>Keywords</h2>
<p>image manager, image name</p>
