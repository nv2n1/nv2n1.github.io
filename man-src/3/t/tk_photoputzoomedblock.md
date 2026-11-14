---
title: "tk_photoputzoomedblock(3)"
name: "tk_photoputzoomedblock"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_photoputzoomedblock/"
description: "Tk_FindPhoto, Tk_PhotoPutBlock, Tk_PhotoPutZoomedBlock, Tk_PhotoGetImage, Tk_PhotoBlank, Tk_PhotoExpand, Tk_PhotoGetSize, Tk_PhotoSetSize – manipulate the image data stored in a photo image."
---

<p>Tk_FindPhoto, Tk_PhotoPutBlock, Tk_PhotoPutZoomedBlock, Tk_PhotoGetImage, Tk_PhotoBlank, Tk_PhotoExpand, Tk_PhotoGetSize, Tk_PhotoSetSize &#8211; manipulate the image data stored in a photo image. </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
Tk_PhotoHandle
<code>Tk_FindPhoto</code>(<i>interp, imageName</i>)
int
<code>Tk_PhotoPutBlock</code>(<i>interp, handle, blockPtr, x, y, width, height,compRule</i>)
int
<code>Tk_PhotoPutZoomedBlock</code>(<i>interp, handle, blockPtr, x, y, width, height,zoomX, zoomY, subsampleX, subsampleY, compRule</i>)
int
<code>Tk_PhotoGetImage</code>(<i>handle, blockPtr</i>)
void
<code>Tk_PhotoBlank</code>(<i>handle</i>)
int
<code>Tk_PhotoExpand</code>(<i>interp, handle, width, height</i>)
void
<code>Tk_PhotoGetSize</code>(<i>handle, widthPtr, heightPtr</i>)
int
<code>Tk_PhotoSetSize</code>(<i>interp. handle, width, height</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter in which image was created and in which error reporting is to be done.</p>
<dd>const char <i>*imageName</i> (in) Name of the photo image.</p>
<dd>Tk_PhotoHandle <i>handle</i> (in) Opaque handle identifying the photo image to be affected.</p>
<dd>Tk_PhotoImageBlock <i>*blockPtr</i> (in) Specifies the address and storage layout of image data.</p>
<dd>int <i>x</i> (in) Specifies the X coordinate where the top-left corner of the block is to be placed within the image.</p>
<dd>int <i>y</i> (in) Specifies the Y coordinate where the top-left corner of the block is to be placed within the image.</p>
<dd>int <i>width</i> (in) Specifies the width of the image area to be affected (for <code>Tk_PhotoPutBlock</code>) or the desired image width (for <code>Tk_PhotoExpand</code> and <code>Tk_PhotoSetSize</code>).</p>
<dd>int <i>compRule</i> (in) Specifies the compositing rule used when combining transparent pixels in a block of data with a photo image. Must be one of <code>TK_PHOTO_COMPOSITE_OVERLAY</code> (which puts the block of data over the top of the existing photo image, with the previous contents showing through in the transparent bits) or <code>TK_PHOTO_COMPOSITE_SET</code> (which discards the existing photo image contents in the rectangle covered by the data block.)</p>
<dd>int <i>height</i> (in) Specifies the height of the image area to be affected (for <code>Tk_PhotoPutBlock</code>) or the desired image height (for <code>Tk_PhotoExpand</code> and <code>Tk_PhotoSetSize</code>).</p>
<dd>int <i>*widthPtr</i> (out) Pointer to location in which to store the image width.</p>
<dd>int <i>*heightPtr</i> (out) Pointer to location in which to store the image height.</p>
<dd>int <i>subsampleX</i> (in) Specifies the subsampling factor in the X direction for input image data.</p>
<dd>int <i>subsampleY</i> (in) Specifies the subsampling factor in the Y direction for input image data.</p>
<dd>int <i>zoomX</i> (in) Specifies the zoom factor to be applied in the X direction to pixels being written to the photo image.</p>
<dd>int <i>zoomY</i> (in) Specifies the zoom factor to be applied in the Y direction to pixels being written to the photo image. </p>
</dl>
<h2>Description</h2>
<p><code>Tk_FindPhoto</code> returns an opaque handle that is used to identify a particular photo image to the other procedures. The parameter is the name of the image, that is, the name specified to the <code>image create photo</code> command, or assigned by that command if no name was specified. </p>
<p> <code>Tk_PhotoPutBlock</code> is used to supply blocks of image data to be displayed. The call affects an area of the image of size <i>width</i> x <i>height</i> pixels, with its top-left corner at coordinates (<i>x</i>,<i>y</i>). All of <i>width</i>, <i>height</i>, <i>x</i>, and <i>y</i> must be non-negative. If part of this area lies outside the current bounds of the image, the image will be expanded to include the area, unless the user has specified an explicit image size with the <code>-width</code> and/or <code>-height</code> widget configuration options (see <a href="/docs/linux/man/n-photo/">photo</a>(n)); in that case the area is silently clipped to the image boundaries. </p>
<p> The <i>block</i> parameter is a pointer to a <code>Tk_PhotoImageBlock</code> structure, defined as follows:</p>
<dl COMPACT>
<dd>
<pre>typedef struct {
 unsigned char *<i>pixelPtr</i>;
 int <i>width</i>;
 int <i>height</i>;
 int <i>pitch</i>;
 int <i>pixelSize</i>;
 int <i>offset[4]</i>;
} Tk_PhotoImageBlock;</pre>
</dl>
<p> The <i>pixelPtr</i> field points to the first pixel, that is, the top-left pixel in the block. The <i>width</i> and <i>height</i> fields specify the dimensions of the block of pixels. The <i>pixelSize</i> field specifies the address difference between two horizontally adjacent pixels. Often it is 3 or 4, but it can have any value. The <i>pitch</i> field specifies the address difference between two vertically adjacent pixels. The <i>offset</i> array contains the offsets from the address of a pixel to the addresses of the bytes containing the red, green, blue and alpha (transparency) components. These are normally 0, 1, 2 and 3, but can have other values, e.g., for images that are stored as separate red, green and blue planes. </p>
<p> The <i>compRule</i> parameter to <code>Tk_PhotoPutBlock</code> specifies a compositing rule that says what to do with transparent pixels. The value <code>TK_PHOTO_COMPOSITE_OVERLAY</code> says that the previous contents of the photo image should show through, and the value <code>TK_PHOTO_COMPOSITE_SET</code> says that the previous contents of the photo image should be completely ignored, and the values from the block be copied directly across. The behavior in Tk8.3 and earlier was equivalent to having <code>TK_PHOTO_COMPOSITE_OVERLAY</code> as a compositing rule. </p>
<p> The value given for the <i>width</i> and <i>height</i> parameters to <code>Tk_PhotoPutBlock</code> do not have to correspond to the values specified in <i>block</i>. If they are smaller, <code>Tk_PhotoPutBlock</code> extracts a sub-block from the image data supplied. If they are larger, the data given are replicated (in a tiled fashion) to fill the specified area. These rules operate independently in the horizontal and vertical directions. </p>
<p> <code>Tk_PhotoPutBlock</code> normally returns <code>TCL_OK</code>, though if it cannot allocate sufficient memory to hold the resulting image, <code>TCL_ERROR</code> is returned instead and, if the <i>interp</i> argument is non-NULL, an error message is placed in the interpreter&#8217;s result. </p>
<p> <code>Tk_PhotoPutZoomedBlock</code> works like <code>Tk_PhotoPutBlock</code> except that the image can be reduced or enlarged for display. The <i>subsampleX</i> and <i>subsampleY</i> parameters allow the size of the image to be reduced by subsampling. <code>Tk_PhotoPutZoomedBlock</code> will use only pixels from the input image whose X coordinates are multiples of <i>subsampleX</i>, and whose Y coordinates are multiples of <i>subsampleY</i>. For example, an image of 512&#215;512 pixels can be reduced to 256&#215;256 by setting <i>subsampleX</i> and <i>subsampleY</i> to 2. </p>
<p> The <i>zoomX</i> and <i>zoomY</i> parameters allow the image to be enlarged by pixel replication. Each pixel of the (possibly subsampled) input image will be written to a block <i>zoomX</i> pixels wide and <i>zoomY</i> pixels high of the displayed image. Subsampling and zooming can be used together for special effects. </p>
<p> <code>Tk_PhotoGetImage</code> can be used to retrieve image data from a photo image. <code>Tk_PhotoGetImage</code> fills in the structure pointed to by the <i>blockPtr</i> parameter with values that describe the address and layout of the image data that the photo image has stored internally. The values are valid until the image is destroyed or its size is changed. <code>Tk_PhotoGetImage</code> returns 1 for compatibility with the corresponding procedure in the old photo widget. </p>
<p> <code>Tk_PhotoBlank</code> blanks the entire area of the photo image. Blank areas of a photo image are transparent. </p>
<p> <code>Tk_PhotoExpand</code> requests that the widget&#8217;s image be expanded to be at least <i>width</i> x <i>height</i> pixels in size. The width and/or height are unchanged if the user has specified an explicit image width or height with the <code>-width</code> and/or <code>-height</code> configuration options, respectively. If the image data are being supplied in many small blocks, it is more efficient to use <code>Tk_PhotoExpand</code> or <code>Tk_PhotoSetSize</code> at the beginning rather than allowing the image to expand in many small increments as image blocks are supplied. </p>
<p> <code>Tk_PhotoExpand</code> normally returns <code>TCL_OK</code>, though if it cannot allocate sufficient memory to hold the resulting image, <code>TCL_ERROR</code> is returned instead and, if the <i>interp</i> argument is non-NULL, an error message is placed in the interpreter&#8217;s result. </p>
<p> <code>Tk_PhotoSetSize</code> specifies the size of the image, as if the user had specified the given <i>width</i> and <i>height</i> values to the <code>-width</code> and <code>-height</code> configuration options. A value of zero for <i>width</i> or <i>height</i> does not change the image&#8217;s width or height, but allows the width or height to be changed by subsequent calls to <code>Tk_PhotoPutBlock</code>, <code>Tk_PhotoPutZoomedBlock</code> or <code>Tk_PhotoExpand</code>. </p>
<p> <code>Tk_PhotoSetSize</code> normally returns <code>TCL_OK</code>, though if it cannot allocate sufficient memory to hold the resulting image, <code>TCL_ERROR</code> is returned instead and, if the <i>interp</i> argument is non-NULL, an error message is placed in the interpreter&#8217;s result. </p>
<p> <code>Tk_PhotoGetSize</code> returns the dimensions of the image in *<i>widthPtr</i> and *<i>heightPtr</i>. </p>
<h2>Portability</h2>
<p>In Tk 8.3 and earlier, <code>Tk_PhotoPutBlock</code> and <code>Tk_PhotoPutZoomedBlock</code> had different signatures. If you want to compile code that uses the old interface against 8.4 without updating your code, compile it with the flag -DUSE_COMPOSITELESS_PHOTO_PUT_BLOCK. Code linked using Stubs against older versions of Tk will continue to work. </p>
<p> In Tk 8.4, <code>Tk_PhotoPutBlock</code>, <code>Tk_PhotoPutZoomedBlock</code>, <code>Tk_PhotoExpand</code> and <code>Tk_PhotoSetSize</code> did not take an <i>interp</i> argument or return any result code. If insufficient memory was available for an image, Tk would panic. This behaviour is still supported if you compile your extension with the additional flag -DUSE_PANIC_ON_PHOTO_ALLOC_FAILURE. Code linked using Stubs against older versions of Tk will continue to work. </p>
<h2>Credits</h2>
<p>The code for the photo image type was developed by Paul Mackerras, based on his earlier photo widget code. </p>
<h2>Keywords</h2>
<p>photo, image</p>
