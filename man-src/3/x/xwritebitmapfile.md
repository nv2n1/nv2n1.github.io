---
title: "xwritebitmapfile(3)"
name: "xwritebitmapfile"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xwritebitmapfile/"
description: "XReadBitmapFile, XReadBitmapFileData, XWriteBitmapFile, XCreatePixmapFromBitmapData, XCreateBitmapFromData – manipulate bitmaps"
---

<p>XReadBitmapFile, XReadBitmapFileData, XWriteBitmapFile, XCreatePixmapFromBitmapData, XCreateBitmapFromData &#8211; manipulate bitmaps </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XReadBitmapFile(Display *<i>display</i>, Drawable <i>d</i>, char *<i>filename</i>, unsigned int *<i>width_return</i>, unsigned int *<i>height_return</i>, Pixmap *<i>bitmap_return</i>, int *<i>x_hot_return</i>, int *<i>y_hot_return</i>);</p>
<dd>int XReadBitmapFileData(char *<i>filename</i>, unsigned int *<i>width_return</i>, unsigned int *<i>height_return</i>, unsigned char *<i>data_return</i>, int *<i>x_hot_return</i>, int *<i>y_hot_return</i>);</p>
<dd>int XWriteBitmapFile(Display *<i>display</i>, char *<i>filename</i>, Pixmap <i>bitmap</i>, unsigned int <i>width</i>, unsigned int <i>height</i>, int <i>x_hot</i>, int <i>y_hot</i>);</p>
<dd>Pixmap XCreatePixmapFromBitmapData(Display *<i>display</i>, Drawable <i>d</i>, char *<i>data</i>, unsigned int <i>width</i>, unsigned int <i>height</i>, unsigned long <i>fg</i>, unsigned long <i>bg</i>, unsigned int <i>depth</i>);</p>
<dd>Pixmap XCreateBitmapFromData(Display *<i>display</i>, Drawable <i>d</i>, char *<i>data</i>, unsigned int <i>width</i>, unsigned int <i>height</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>bitmap</i></p>
<dd>Specifies the bitmap.</p>
<dt><i>bitmap_return</i></p>
<dd>Returns the bitmap that is created.</p>
<dt><i>d</i></p>
<dd>Specifies the drawable that indicates the screen.</p>
<dt><i>data</i></p>
<dd>Specifies the data in bitmap format.</p>
<dt><i>data</i></p>
<dd>Specifies the location of the bitmap data.</p>
<dt><i>data_return</i></p>
<dd>Returns the bitmap data.</p>
<dt><i>depth</i></p>
<dd>Specifies the depth of the pixmap.</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>fg</i></p>
<dd>
<dt><i>bg</i></p>
<dd>Specify the foreground and background pixel values to use.</p>
<dt><i>filename</i></p>
<dd>Specifies the file name to use. The format of the file name is operating-system dependent.</p>
<dt><i>width</i></p>
<dd>
<dt><i>height</i></p>
<dd>Specify the width and height.</p>
<dt><i>width_return</i></p>
<dd>
<dt><i>height_return</i></p>
<dd>Return the width and height values of the read in bitmap file.</p>
<dt><i>x_hot</i></p>
<dd>
<dt><i>y_hot</i></p>
<dd>Specify where to place the hotspot coordinates (or -1,-1 if none are present) in the file.</p>
<dt><i>x_hot_return</i></p>
<dd>
<dt><i>y_hot_return</i></p>
<dd>Return the hotspot coordinates.</dl>
<h2>Description</h2>
<p>The <code>XReadBitmapFile</code> function reads in a file containing a bitmap. The file is parsed in the encoding of the current locale. The ability to read other than the standard format is implementation-dependent. If the file cannot be opened, <code>XReadBitmapFile</code> returns <code>BitmapOpenFailed</code>. If the file can be opened but does not contain valid bitmap data, it returns <code>BitmapFileInvalid</code>. If insufficient working storage is allocated, it returns <code>BitmapNoMemory</code>. If the file is readable and valid, it returns <code>BitmapSuccess</code>. </p>
<p> <code>XReadBitmapFile</code> returns the bitmap&#8217;s height and width, as read from the file, to width_return and height_return. It then creates a pixmap of the appropriate size, reads the bitmap data from the file into the pixmap, and assigns the pixmap to the caller&#8217;s variable bitmap. The caller must free the bitmap using <code>XFreePixmap</code> when finished. If <i>name</i>_x_hot and <i>name</i>_y_hot exist, <code>XReadBitmapFile</code> returns them to x_hot_return and y_hot_return; otherwise, it returns -1,-1. </p>
<p> <code>XReadBitmapFile</code> can generate <code>BadAlloc</code> and <code>BadDrawable</code> errors. </p>
<p> The <code>XReadBitmapFileData</code> function reads in a file containing a bitmap, in the same manner as <code>XReadBitmapFile</code>, but returns the data directly rather than creating a pixmap in the server. The bitmap data is returned in data_return; the client must free this storage when finished with it by calling <code>XFree</code>. The status and other return values are the same as for <code>XReadBitmapFile</code>. </p>
<p> The <code>XWriteBitmapFile</code> function writes a bitmap out to a file in the X Version 11 format. The name used in the output file is derived from the file name by deleting the directory prefix. The file is written in the encoding of the current locale. If the file cannot be opened for writing, it returns <code>BitmapOpenFailed</code>. If insufficient memory is allocated, <code>XWriteBitmapFile</code> returns <code>BitmapNoMemory</code>; otherwise, on no error, it returns <code>BitmapSuccess</code>. If x_hot and y_hot are not -1, -1, <code>XWriteBitmapFile</code> writes them out as the hotspot coordinates for the bitmap. </p>
<p> <code>XWriteBitmapFile</code> can generate <code>BadDrawable</code> and <code>BadMatch</code> errors. </p>
<p> The <code>XCreatePixmapFromBitmapData</code> function creates a pixmap of the given depth and then does a bitmap-format <code>XPutImage</code> of the data into it. The depth must be supported by the screen of the specified drawable, or a <code>BadMatch</code> error results. </p>
<p> <code>XCreatePixmapFromBitmapData</code> can generate <code>BadAlloc</code> and <code>BadMatch</code> errors. </p>
<p> The <code>XCreateBitmapFromData</code> function allows you to include in your C program (using <code>#include</code>) a bitmap file that was written out by <code>XWriteBitmapFile</code> (X version 11 format only) without reading in the bitmap file. The following example creates a gray bitmap: </p>
<p> #include &quot;gray.bitmap&quot; </p>
<p> Pixmap bitmap; bitmap = XCreateBitmapFromData(display, window, gray_bits, gray_width, gray_height); </p>
<p> If insufficient working storage was allocated, <code>XCreateBitmapFromData</code> returns <code>None</code>. It is your responsibility to free the bitmap using <code>XFreePixmap</code> when finished. </p>
<p> <code>XCreateBitmapFromData</code> can generate a <code>BadAlloc</code> error.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>The server failed to allocate the requested resource or server memory.</p>
<dt><code>BadDrawable</code></p>
<dd>A value for a Drawable argument does not name a defined Window or Pixmap.</p>
<dt><code>BadMatch</code></p>
<dd>An <code>InputOnly</code> window is used as a Drawable.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xcreatepixmap/">XCreatePixmap</a>(3), <a href="/docs/linux/man/3-xputimage/">XPutImage</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
