---
title: "tk_sizeofimage(3)"
name: "tk_sizeofimage"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_sizeofimage/"
description: "Tk_GetImage, Tk_RedrawImage, Tk_SizeOfImage, Tk_FreeImage – use an image in a widget"
---

<p>Tk_GetImage, Tk_RedrawImage, Tk_SizeOfImage, Tk_FreeImage &#8211; use an image in a widget </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
Tk_Image
<code>Tk_GetImage</code>(<i>interp, tkwin, name, changeProc, clientData</i>)
<code>Tk_RedrawImage</code>(<i>image, imageX, imageY, width, height, drawable, drawableX, drawableY</i>)
<code>Tk_SizeOfImage</code>(<i>image, widthPtr, heightPtr</i>)
<code>Tk_FreeImage</code>(<i>image</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Place to leave error message.</p>
<dd>Tk_Window <i>tkwin</i> (in) Window in which image will be used.</p>
<dd>const char <i>*name</i> (in) Name of image.</p>
<dd>Tk_ImageChangedProc <i>*changeProc</i> (in) Procedure for Tk to invoke whenever image content or size changes.</p>
<dd>ClientData <i>clientData</i> (in) One-word value for Tk to pass to <i>changeProc</i>.</p>
<dd>Tk_Image <i>image</i> (in) Token for image instance; must have been returned by a previous call to <code>Tk_GetImage</code>.</p>
<dd>int <i>imageX</i> (in) X-coordinate of upper-left corner of region of image to redisplay (measured in pixels from the image&#8217;s upper-left corner).</p>
<dd>int <i>imageY</i> (in) Y-coordinate of upper-left corner of region of image to redisplay (measured in pixels from the image&#8217;s upper-left corner).</p>
<dd>int <i>width</i> ((in)) Width of region of image to redisplay.</p>
<dd>int <i>height</i> ((in)) Height of region of image to redisplay.</p>
<dd>Drawable <i>drawable</i> (in) Where to display image. Must either be window specified to <code>Tk_GetImage</code> or a pixmap compatible with that window.</p>
<dd>int <i>drawableX</i> (in) Where to display image in <i>drawable</i>: this is the x-coordinate in <i>drawable</i> where x-coordinate <i>imageX</i> of the image should be displayed.</p>
<dd>int <i>drawableY</i> (in) Where to display image in <i>drawable</i>: this is the y-coordinate in <i>drawable</i> where y-coordinate <i>imageY</i> of the image should be displayed.</p>
<dd>int <i>widthPtr</i> (out) Store width of <i>image</i> (in pixels) here.</p>
<dd>int <i>heightPtr</i> (out) Store height of <i>image</i> (in pixels) here. </p>
</dl>
<h2>Description</h2>
<p>These procedures are invoked by widgets that wish to display images. <code>Tk_GetImage</code> is invoked by a widget when it first decides to display an image. <i>name</i> gives the name of the desired image and <i>tkwin</i> identifies the window where the image will be displayed. <code>Tk_GetImage</code> looks up the image in the table of existing images and returns a token for a new instance of the image. If the image does not exist then <code>Tk_GetImage</code> returns NULL and leaves an error message in <i>interp-&gt;result</i>. </p>
<p> When a widget wishes to actually display an image it must call <code>Tk_RedrawImage</code>, identifying the image (<i>image</i>), a region within the image to redisplay (<i>imageX</i>, <i>imageY</i>, <i>width</i>, and <i>height</i>), and a place to display the image (<i>drawable</i>, <i>drawableX</i>, and <i>drawableY</i>). Tk will then invoke the appropriate image manager, which will display the requested portion of the image before returning. </p>
<p> A widget can find out the dimensions of an image by calling <code>Tk_SizeOfImage</code>: the width and height will be stored in the locations given by <i>widthPtr</i> and <i>heightPtr</i>, respectively. </p>
<p> When a widget is finished with an image (e.g., the widget is being deleted or it is going to use a different image instead of the current one), it must call <code>Tk_FreeImage</code> to release the image instance. The widget should never again use the image token after passing it to <code>Tk_FreeImage</code>. There must be exactly one call to <code>Tk_FreeImage</code> for each call to <code>Tk_GetImage</code>. </p>
<p> If the contents or size of an image changes, then any widgets using the image will need to find out about the changes so that they can redisplay themselves. The <i>changeProc</i> and <i>clientData</i> arguments to <code>Tk_GetImage</code> are used for this purpose. <i>changeProc</i> will be called by Tk whenever a change occurs in the image; it must match the following prototype:</p>
<dl COMPACT>
<dd>
<pre>typedef void Tk_ImageChangedProc(
 ClientData <i>clientData</i>,
 int <i>x</i>,
 int <i>y</i>,
 int <i>width</i>,
 int <i>height</i>,
 int <i>imageWidth</i>,
 int <i>imageHeight</i>);</pre>
</dl>
<p> The <i>clientData</i> argument to <i>changeProc</i> is the same as the <i>clientData</i> argument to <code>Tk_GetImage</code>. It is usually a pointer to the widget record for the widget or some other data structure managed by the widget. The arguments <i>x</i>, <i>y</i>, <i>width</i>, and <i>height</i> identify a region within the image that must be redisplayed; they are specified in pixels measured from the upper-left corner of the image. The arguments <i>imageWidth</i> and <i>imageHeight</i> give the image&#8217;s (new) size. </p>
<h2>See Also</h2>
<p>Tk_CreateImageType </p>
<h2>Keywords</h2>
<p>images, redisplay</p>
