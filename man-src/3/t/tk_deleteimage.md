---
title: "tk_deleteimage(3)"
name: "tk_deleteimage"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_deleteimage/"
description: "Tk_DeleteImage – Destroy an image."
---

<p>Tk_DeleteImage &#8211; Destroy an image. </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
<code>Tk_DeleteImage</code>(<i>interp, name</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter for which the image was created.</p>
<dd>const char <i>*name</i> (in) Name of the image. </p>
</dl>
<h2>Description</h2>
<p><code>Tk_DeleteImage</code> deletes the image given by <i>interp</i> and <i>name</i>, if there is one. All instances of that image will redisplay as empty regions. If the given image does not exist then the procedure has no effect. </p>
<h2>Keywords</h2>
<p>delete image, image manager</p>
