---
title: "xinitimage(3)"
name: "xinitimage"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xinitimage/"
description: "XInitImage, XCreateImage, XGetPixel, XPutPixel, XSubImage, XAddPixel, XDestroyImage – image utilities"
---

<p>XInitImage, XCreateImage, XGetPixel, XPutPixel, XSubImage, XAddPixel, XDestroyImage &#8211; image utilities </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>Status XInitImage(XImage *<i>image</i>);</p>
<dd>XImage *XCreateImage(Display *<i>display</i>, Visual *<i>visual</i>, unsigned int <i>depth</i>, int <i>format</i>, int <i>offset</i>, char *<i>data</i>, unsigned int <i>width</i>, unsigned int <i>height</i>, int <i>bitmap_pad</i>, int <i>bytes_per_line</i>);</p>
<dd>unsigned long XGetPixel(XImage *<i>ximage</i>, int <i>x</i>, int <i>y</i>);</p>
<dd>int XPutPixel(XImage *<i>ximage</i>, int <i>x</i>, int <i>y</i>, unsigned long <i>pixel</i>);</p>
<dd>XImage *XSubImage(XImage *<i>ximage</i>, int <i>x</i>, int <i>y</i>, unsigned int <i>subimage_width</i>, unsigned int <i>subimage_height</i>);</p>
<dd>int XAddPixel(XImage *<i>ximage</i>, long <i>value</i>);</p>
<dd>int XDestroyImage(XImage *<i>ximage</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>bitmap_pad</i></p>
<dd>Specifies the quantum of a scanline (8, 16, or 32). In other words, the start of one scanline is separated in client memory from the start of the next scanline by an integer multiple of this many bits.</p>
<dt><i>bytes_per_line</i></p>
<dd>Specifies the number of bytes in the client image between the start of one scanline and the start of the next.</p>
<dt><i>data</i></p>
<dd>Specifies the image data.</p>
<dt><i>depth</i></p>
<dd>Specifies the depth of the image.</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>format</i></p>
<dd>Specifies the format for the image. You can pass <code>XYBitmap</code>, <code>XYPixmap</code>, or <code>ZPixmap</code>.</p>
<dt><i>height</i></p>
<dd>Specifies the height of the image, in pixels.</p>
<dt><i>offset</i></p>
<dd>Specifies the number of pixels to ignore at the beginning of the scanline.</p>
<dt><i>pixel</i></p>
<dd>Specifies the new pixel value.</p>
<dt><i>subimage_height</i></p>
<dd>Specifies the height of the new subimage, in pixels.</p>
<dt><i>subimage_width</i></p>
<dd>Specifies the width of the new subimage, in pixels.</p>
<dt><i>value</i></p>
<dd>Specifies the constant value that is to be added.</p>
<dt><i>visual</i></p>
<dd>Specifies the <code>Visual</code> structure.</p>
<dt><i>width</i></p>
<dd>Specifies the width of the image, in pixels.</p>
<dt><i>ximage</i></p>
<dd>Specifies the image.</p>
<dt><i>x</i></p>
<dd>
<dt><i>y</i></p>
<dd>Specify the x and y coordinates.</dl>
<h2>Description</h2>
<p>The <code>XInitImage</code> function initializes the internal image manipulation routines of an image structure, based on the values of the various structure members. All fields other than the manipulation routines must already be initialized. If the bytes_per_line member is zero, <code>XInitImage</code> will assume the image data is contiguous in memory and set the bytes_per_line member to an appropriate value based on the other members; otherwise, the value of bytes_per_line is not changed. All of the manipulation routines are initialized to functions that other Xlib image manipulation functions need to operate on the type of image specified by the rest of the structure. </p>
<p> This function must be called for any image constructed by the client before passing it to any other Xlib function. Image structures created or returned by Xlib do not need to be initialized in this fashion. </p>
<p> This function returns a nonzero status if initialization of the structure is successful. It returns zero if it detected some error or inconsistency in the structure, in which case the image is not changed. </p>
<p> The <code>XCreateImage</code> function allocates the memory needed for an <code>XImage</code> structure for the specified display but does not allocate space for the image itself. Rather, it initializes the structure byte-order, bit-order, and bitmap-unit values from the display and returns a pointer to the <code>XImage</code> structure. The red, green, and blue mask values are defined for Z format images only and are derived from the <code>Visual</code> structure passed in. Other values also are passed in. The offset permits the rapid displaying of the image without requiring each scanline to be shifted into position. If you pass a zero value in bytes_per_line, Xlib assumes that the scanlines are contiguous in memory and calculates the value of bytes_per_line itself. </p>
<p> Note that when the image is created using <code>XCreateImage</code>, <code>XGetImage</code>, or <code>XSubImage</code>, the destroy procedure that the <code>XDestroyImage</code> function calls frees both the image structure and the data pointed to by the image structure. </p>
<p> The basic functions used to get a pixel, set a pixel, create a subimage, and add a constant value to an image are defined in the image object. The functions in this section are really macro invocations of the functions in the image object and are defined in </p>
<p> The <code>XGetPixel</code> function returns the specified pixel from the named image. The pixel value is returned in normalized format (that is, the least significant byte of the long is the least significant byte of the pixel). The image must contain the x and y coordinates. </p>
<p> The <code>XPutPixel</code> function overwrites the pixel in the named image with the specified pixel value. The input pixel value must be in normalized format (that is, the least significant byte of the long is the least significant byte of the pixel). The image must contain the x and y coordinates. </p>
<p> The <code>XSubImage</code> function creates a new image that is a subsection of an existing one. It allocates the memory necessary for the new <code>XImage</code> structure and returns a pointer to the new image. The data is copied from the source image, and the image must contain the rectangle defined by x, y, subimage_width, and subimage_height. </p>
<p> The <code>XAddPixel</code> function adds a constant value to every pixel in an image. It is useful when you have a base pixel value from allocating color resources and need to manipulate the image to that form. </p>
<p> The <code>XDestroyImage</code> function deallocates the memory associated with the <code>XImage</code> structure.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xputimage/">XPutImage</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
