---
title: "tk_imagechanged(3)"
name: "tk_imagechanged"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_imagechanged/"
description: "Tk_ImageChanged – notify widgets that image needs to be redrawn"
---

<p>Tk_ImageChanged &#8211; notify widgets that image needs to be redrawn </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
<code>Tk_ImageChanged</code>(<i>imageMaster, x, y, width, height, imageWidth, imageHeight</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tk_ImageMaster <i>imageMaster</i> (in) Token for image, which was passed to image&#8217;s <i>createProc</i> when the image was created.</p>
<dd>int <i>x</i> (in) X-coordinate of upper-left corner of region that needs redisplay (measured from upper-left corner of image).</p>
<dd>int <i>y</i> (in) Y-coordinate of upper-left corner of region that needs redisplay (measured from upper-left corner of image).</p>
<dd>int <i>width</i> (in) Width of region that needs to be redrawn, in pixels.</p>
<dd>int <i>height</i> (in) Height of region that needs to be redrawn, in pixels.</p>
<dd>int <i>imageWidth</i> (in) Current width of image, in pixels.</p>
<dd>int <i>imageHeight</i> (in) Current height of image, in pixels. </p>
</dl>
<h2>Description</h2>
<p>An image manager calls <code>Tk_ImageChanged</code> for an image whenever anything happens that requires the image to be redrawn. As a result of calling <code>Tk_ImageChanged</code>, any widgets using the image are notified so that they can redisplay themselves appropriately. The <i>imageMaster</i> argument identifies the image, and <i>x</i>, <i>y</i>, <i>width</i>, and <i>height</i> specify a rectangular region within the image that needs to be redrawn. <i>imageWidth</i> and <i>imageHeight</i> specify the image&#8217;s (new) size. </p>
<p> An image manager should call <code>Tk_ImageChanged</code> during its <i>createProc</i> to specify the image&#8217;s initial size and to force redisplay if there are existing instances for the image. If any of the pixel values in the image should change later on, <code>Tk_ImageChanged</code> should be called again with <i>x</i>, <i>y</i>, <i>width</i>, and <i>height</i> values that cover all the pixels that changed. If the size of the image should change, then <code>Tk_ImageChanged</code> must be called to indicate the new size, even if no pixels need to be redisplayed. </p>
<h2>See Also</h2>
<p>Tk_CreateImageType </p>
<h2>Keywords</h2>
<p>images, redisplay, image size changes</p>
