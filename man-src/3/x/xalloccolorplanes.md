---
title: "xalloccolorplanes(3)"
name: "xalloccolorplanes"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xalloccolorplanes/"
description: "XAllocColor, XAllocNamedColor, XAllocColorCells, XAllocColorPlanes, XFreeColors – allocate and free colors"
---

<p>XAllocColor, XAllocNamedColor, XAllocColorCells, XAllocColorPlanes, XFreeColors &#8211; allocate and free colors </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>Status XAllocColor(Display *<i>display</i>, Colormap <i>colormap</i>, XColor *<i>screen_in_out</i>);</dd>
<dd>Status XAllocNamedColor(Display *<i>display</i>, Colormap <i>colormap</i>, char *<i>color_name</i>, XColor *<i>screen_def_return</i>, XColor *<i>exact_def_return</i>);</dd>
<dd>Status XAllocColorCells(Display *<i>display</i>, Colormap <i>colormap</i>, Bool <i>contig</i>, unsigned long <i>plane_masks_return</i>[], unsigned int <i>nplanes</i>, unsigned long <i>pixels_return</i>[], unsigned int <i>npixels</i>);</dd>
<dd>Status XAllocColorPlanes(Display *<i>display</i>, Colormap <i>colormap</i>, Bool <i>contig</i>, unsigned long <i>pixels_return</i>[], int <i>ncolors</i>, int <i>nreds</i>, int <i>ngreens</i>, int <i>nblues</i>, unsigned long *<i>rmask_return</i>, unsigned long *<i>gmask_return</i>, unsigned long *<i>bmask_return</i>);</dd>
<dd>int XFreeColors(Display *<i>display</i>, Colormap <i>colormap</i>, unsigned long <i>pixels</i>[], int <i>npixels</i>, unsigned long <i>planes</i>);</dd>
<dt><i>color_name</i></dt>
<dd>Specifies the color name string (for example, red) whose color definition structure you want returned.</dd>
<dt><i>colormap</i></dt>
<dd>Specifies the colormap.</dd>
<dt><i>contig</i></dt>
<dd>Specifies a Boolean value that indicates whether the planes must be contiguous.</dd>
<dt><i>display</i></dt>
<dd>Specifies the connection to the X server.</dd>
<dt><i>exact_def_return</i></dt>
<dd>Returns the exact RGB values.</dd>
<dt><i>ncolors</i></dt>
<dd>Specifies the number of pixel values that are to be returned in the pixels_return array.</dd>
<dt><i>npixels</i></dt>
<dd>Specifies the number of pixels.</dd>
<dt><i>nplanes</i></dt>
<dd>Specifies the number of plane masks that are to be returned in the plane masks array.</dd>
<dt><i>nreds</i></dt>
<dd>
</dd><dt><i>ngreens</i></dt>
<dd>
</dd><dt><i>nblues</i></dt>
<dd>Specify the number of red, green, and blue planes. The value you pass must be nonnegative.</dd>
<dt><i>pixels</i></dt>
<dd>Specifies an array of pixel values.</dd>
<dt><i>pixels_return</i></dt>
<dd>Returns an array of pixel values.</dd>
<dt><i>plane_mask_return</i></dt>
<dd>Returns an array of plane masks.</dd>
<dt><i>planes</i></dt>
<dd>Specifies the planes you want to free.</dd>
<dt><i>rmask_return</i></dt>
<dd>
</dd><dt><i>gmask_return</i></dt>
<dd>
</dd><dt><i>bmask_return</i></dt>
<dd>Return bit masks for the red, green, and blue planes.</dd>
<dt><i>screen_def_return</i></dt>
<dd>Returns the closest RGB values provided by the hardware.</dd>
<dt><i>screen_in_out</i></dt>
<dd>Specifies and returns the values actually used in the colormap.</dd></dl>
<h2>Description</h2>
<p>The <code>XAllocColor</code> function allocates a read-only colormap entry corresponding to the closest RGB value supported by the hardware. <code>XAllocColor</code> returns the pixel value of the color closest to the specified RGB elements supported by the hardware and returns the RGB value actually used. The corresponding colormap cell is read-only. In addition, <code>XAllocColor</code> returns nonzero if it succeeded or zero if it failed. Multiple clients that request the same effective RGB value can be assigned the same read-only entry, thus allowing entries to be shared. When the last client deallocates a shared cell, it is deallocated. <code>XAllocColor</code> does not use or affect the flags in the <code>XColor</code> structure. </p>
<p> <code>XAllocColor</code> can generate a <code>BadColor</code> error. </p>
<p> The <code>XAllocNamedColor</code> function looks up the named color with respect to the screen that is associated with the specified colormap. It returns both the exact database definition and the closest color supported by the screen. The allocated color cell is read-only. The pixel value is returned in screen_def_return. If the color name is not in the Host Portable Character Encoding, the result is implementation-dependent. Use of uppercase or lowercase does not matter. If screen_def_return and exact_def_return point to the same structure, the pixel field will be set correctly, but the color values are undefined. <code>XAllocNamedColor</code> returns nonzero if a cell is allocated; otherwise, it returns zero. </p>
<p> <code>XAllocNamedColor</code> can generate a <code>BadColor</code> error. </p>
<p> delim %% The <code>XAllocColorCells</code> function allocates read/write color cells. The number of colors must be positive and the number of planes nonnegative, or a <code>BadValue</code> error results. If ncolors and nplanes are requested, then ncolors pixels and nplane plane masks are returned. No mask will have any bits set to 1 in common with any other mask or with any of the pixels. By ORing together each pixel with zero or more masks, ncolors * %2 sup nplanes% distinct pixels can be produced. All of these are allocated writable by the request. For <code>GrayScale</code> or <code>PseudoColor</code>, each mask has exactly one bit set to 1. For <code>DirectColor</code>, each has exactly three bits set to 1. If contig is <code>True</code> and if all masks are ORed together, a single contiguous set of bits set to 1 will be formed for <code>GrayScale</code> or <code>PseudoColor</code> and three contiguous sets of bits set to 1 (one within each pixel subfield) for <code>DirectColor</code>. The RGB values of the allocated entries are undefined. <code>XAllocColorCells</code> returns nonzero if it succeeded or zero if it failed. </p>
<p> <code>XAllocColorCells</code> can generate <code>BadColor</code> and <code>BadValue</code> errors. </p>
<p> delim %% The specified ncolors must be positive; and nreds, ngreens, and nblues must be nonnegative, or a <code>BadValue</code> error results. If ncolors colors, nreds reds, ngreens greens, and nblues blues are requested, ncolors pixels are returned; and the masks have nreds, ngreens, and nblues bits set to 1, respectively. If contig is <code>True</code>, each mask will have a contiguous set of bits set to 1. No mask will have any bits set to 1 in common with any other mask or with any of the pixels. For <code>DirectColor</code>, each mask will lie within the corresponding pixel subfield. By ORing together subsets of masks with each pixel value, ncolors * %2 sup (nreds+ngreens+nblues)% distinct pixel values can be produced. All of these are allocated by the request. However, in the colormap, there are only ncolors * %2 sup nreds% independent red entries, ncolors * %2 sup ngreens% independent green entries, and ncolors * %2 sup nblues% independent blue entries. This is true even for <code>PseudoColor</code>. When the colormap entry of a pixel value is changed (using <code>XStoreColors</code>, <code>XStoreColor</code>, or <code>XStoreNamedColor</code>), the pixel is decomposed according to the masks, and the corresponding independent entries are updated. <code>XAllocColorPlanes</code> returns nonzero if it succeeded or zero if it failed. </p>
<p> <code>XAllocColorPlanes</code> can generate <code>BadColor</code> and <code>BadValue</code> errors. </p>
<p> The <code>XFreeColors</code> function frees the cells represented by pixels whose values are in the pixels array. The planes argument should not have any bits set to 1 in common with any of the pixels. The set of all pixels is produced by ORing together subsets of the planes argument with the pixels. The request frees all of these pixels that were allocated by the client (using <code>XAllocColor</code>, <code>XAllocNamedColor</code>, <code>XAllocColorCells</code>, and <code>XAllocColorPlanes</code>). Note that freeing an individual pixel obtained from <code>XAllocColorPlanes</code> may not actually allow it to be reused until all of its related pixels are also freed. Similarly, a read-only entry is not actually freed until it has been freed by all clients, and if a client allocates the same read-only entry multiple times, it must free the entry that many times before the entry is actually freed. </p>
<p> All specified pixels that are allocated by the client in the colormap are freed, even if one or more pixels produce an error. If a specified pixel is not a valid index into the colormap, a <code>BadValue</code> error results. If a specified pixel is not allocated by the client (that is, is unallocated or is only allocated by another client) or if the colormap was created with all entries writable (by passing <code>AllocAll</code> to <code>XCreateColormap</code>), a <code>BadAccess</code> error results. If more than one pixel is in error, the one that gets reported is arbitrary. </p>
<p> <code>XFreeColors</code> can generate <code>BadAccess</code>, <code>BadColor</code>, and <code>BadValue</code> errors.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAccess</code></dt>
<dd>A client attempted to free a color map entry that it did not already allocate.</dd>
<dt><code>BadAccess</code></dt>
<dd>A client attempted to store into a read-only color map entry.</dd>
<dt><code>BadColor</code></dt>
<dd>A value for a Colormap argument does not name a defined Colormap.</dd>
<dt><code>BadValue</code></dt>
<dd>Some numeric value falls outside the range of values accepted by the request. Unless a specific range is specified for an argument, the full range defined by the argument&#8217;s type is accepted. Any argument defined as a set of alternatives can generate this error.</dd></dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xcreatecolormap/">XCreateColormap</a>(3), <a href="/docs/linux/man/3-xquerycolor/">XQueryColor</a>(3), <a href="/docs/linux/man/3-xstorecolors/">XStoreColors</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
