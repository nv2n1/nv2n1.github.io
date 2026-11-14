---
title: "gdk-pixbuf-csource(1)"
name: "gdk-pixbuf-csource"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdk-pixbuf-csource/"
description: "gdk-pixbuf-csource – C code generation utility for GdkPixbuf images"
---

<h2 class="name">NAME</h2>
<p> gdk-pixbuf-csource &#8211; C code generation utility for GdkPixbuf images </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>gdk-pixbuf-csource</code> [OPTION&#8230;] [IMAGE]</p>
<dt> <code>gdk-pixbuf-csource</code> [OPTION&#8230;] &#8211;build-list [[NAME]&nbsp;[IMAGE]&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>gdk-pixbuf-csource</code></p>
<dd>is a small utility that generates C code containing images, useful for compiling images directly into programs. </p>
<p> <code>gdk-pixbuf-csource</code> either takes as input one image file name to generate code for, or, using the <code>&#8211;build-list</code> option, a list of (<i>name</i>, <i>image</i>) pairs to generate code for a list of images into named variables.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;stream</code></p>
<dl>
<dt>
<dd> Generate pixbuf data stream (a single string containing a serialized GdkPixdata structure in network byte order).</dl>
<p> <code>&#8211;struct</code></p>
<dl>
<dt>
<dd> Generate GdkPixdata structure (needs the GdkPixdata structure definition from gdk-pixdata.h).</dl>
<p> <code>&#8211;macros</code></p>
<dl>
<dt>
<dd> Generate *_ROWSTRIDE, *_WIDTH, *_HEIGHT, *_BYTES_PER_PIXEL and *_RLE_PIXEL_DATA or *_PIXEL_DATA macro definitions for the image.</dl>
<p> <code>&#8211;rle</code></p>
<dl>
<dt>
<dd> Enables run-length encoding for the generated pixel data (default).</dl>
<p> <code>&#8211;raw</code></p>
<dl>
<dt>
<dd> Disables run-length encoding for the generated pixel data.</dl>
<p> <code>&#8211;extern</code></p>
<dl>
<dt>
<dd> Generate extern symbols.</dl>
<p> <code>&#8211;static</code></p>
<dl>
<dt>
<dd> Generate static symbols (default).</dl>
<p> <code>&#8211;decoder</code></p>
<dl>
<dt>
<dd> Provide a *_RUN_LENGTH_DECODE(image_buf, rle_data, size, bpp) macro definition to decode run-length encoded image data.</dl>
<p> <code>&#8211;name=identifier</code></p>
<dl>
<dt>
<dd> Specifies the identifier name (prefix) for the generated variables or macros (useful only if <code>&#8211;build-list</code> was not specified).</dl>
<p> <code>&#8211;build-list</code></p>
<dl>
<dt>
<dd> Enables (<i>name</i>, <i>image</i>) pair parsing mode.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print brief help and exit.</dl>
<p> <code>-v</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print version and exit.</dl>
<p> <code>&#8211;g-fatal-warnings</code></p>
<dl>
<dt>
<dd> Make warnings fatal (causes the program to abort).</dl>
<h2>SEE ALSO</h2>
<p> The GdkPixbuf documentation, shipped with the Gtk+ distribution, available from m[blue]<code><a rel="nofollow" href="http://www.gtk.org">www.gtk.org</a></code>m[]<font SIZE="-2">[1]</font>.</p>
<h2>BUGS</h2>
<p> The runlength encoder gets out of sync with the pixel boundaries, since it includes the rowstride padding in the encoded stream. Furthermore, it generates pixbufs with suboptimal rowstride in some cases.</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> <a rel="nofollow" href="http://www.gtk.org">www.gtk.org</a></p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.gtk.org">http://www.gtk.org</a></dl>
</dl>
<h2>Index</h2>
