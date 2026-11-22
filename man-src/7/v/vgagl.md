---
title: "vgagl(7)"
name: "vgagl"
section: "7"
letter: "v"
url: "/docs/linux/man/7-vgagl/"
description: "vgagl – a fast framebuffer-level graphics library based on svgalib"
---

<p>vgagl &#8211; a fast framebuffer-level graphics library based on svgalib</p>
<h2>Table Of Contents</h2>
<p><code>0.</code> Introduction<br/>
 <code>1.</code> How to use vgagl<br/>
 <code>2.</code> Description of vgagl functions<br/>
 <code>3.</code> Macros defined in vgagl.h</p>
<h2>0. Introduction</h2>
<p>This is a fast framebuffer-level graphics library for linear 1, 2, 3 and 4 byte-per-pixel modes (256-color, hicolor, truecolor). It uses a limited number of functions from svgalib (libvga) for low-level hardware communication (the library is included in the svgalib shared image). </p>
<p> In particular, <code><a href="/docs/linux/man/7-svgalib/">svgalib</a></code>(7) maps the 64K VGA frame buffer window, and this library directly addresses the buffer. For SVGA modes that use more than 64K of screen memory, SVGA paging is required when writing to the physical screen; this is done automatically for most functions (at a certain cost). </p>
<p> Alternatively, any number of virtual screens of any type in system memory can be used, which can then be copied to the physical screen. There is also support for 4 bytes per pixel framebuffers (and copying them to a 3 bytes per pixel context), and limited planar 256 color mode support (copyscreen, aligned putbox). </p>
<p> The planar 256 color modes (available on all VGA cards) can now be used with a virtual screen, which is copied to the physical screen (with optional page-flipping). </p>
<p> Bitmaps are raw, with one (or more) bytes per pixel (like pixmaps in X), stored in row-major order. They are usually manipulated with the getbox and putbox functions. </p>
<p> <code>vgagl</code> does also make use of the graphic cards accelerator (if it is supported) in some situations. </p>
<p> A graphics context is just a structure that holds the size of the associated graphics screen, how it is organized, clipping status etc. You can define a custom virtual (system memory) graphics context of any size with the setcontextvirtual function. All operations work on the current context. </p>
<p> Any questions, bug-reports, additions, suggestions etc. are welcome.</p>
<h2>1. How To Use Vgagl</h2>
<p>Programs that use <code>vgagl</code> must <code>#include &lt;vgagl.h&gt;</code>. Linking must be done with <code>-lvgagl -lvga</code>. </p>
<p> Functions in the <code>vgagl</code> library have the prefix <code>gl_*</code>. To initialize <code>vgagl</code>, the graphics context must be set. Example: </p>
<dl>
<dd><code>vga_setmode(G320x200x256);</code><br/>
 <code>gl_setcontextvga(G320x200x256);</code></dd></dl>
<p> In this example, the context is set to the physical screen. The context can be saved (only the screen type, not the contents) into a variable, e.g. </p>
<dl>
<dd><code>GraphicsContext physicalscreen;</code><br/>
 <code>gl_getcontext(&amp;physicalscreen).</code></dd></dl>
<p> To define a virtual screen in system memory, use <code>gl_setcontextvgavirtual</code>(3): </p>
<dl>
<dd><code>gl_setcontextvgavirtual(G320x200x256)</code></dd></dl>
<p> which allocates space for a screen identical to 320x200x256 graphics mode, and makes this virtual screen the current graphics context. </p>
<p> The virtual screen can now be copied to the physical screen as follows: </p>
<dl>
<dd><code>gl_copyscreen(&amp;physicalscreen);</code></dd></dl>
<p> Note that with a virtual screen in system memory, it is possible to add fast X-Window support to a program, using MITSHM to copy the framebuffer to the screen window.</p>
<h2>2. Description Of Vgagl Functions</h2>
<h3>Context management</h3>
<dl>
<dt><code>gl_getcontext</code>(3), <code>currentcontext</code>(3)</dt>
<dd>get the current graphics contents..</dd>
<dt><code>gl_setcontext</code>(3)</dt>
<dd>set a previously saved context.</dd>
<dt><code>gl_setcontextvga</code>(3)</dt>
<dd>set the context to the physical screen.</dd>
<dt><code>gl_setcontextvgavirtual</code>(3)</dt>
<dd>set the context to a virtual mode.</dd>
<dt><code>gl_setcontextvirtual</code>(3)</dt>
<dd>define a virtual context.</dd>
<dt><code>gl_allocatecontext</code>(3)</dt>
<dd>allocate a graphics context.</dd>
<dt><code>gl_freecontext</code>(3)</dt>
<dd>free a virtual screen.</dd>
<dt><code>gl_setcontextwidth</code>(3), <code>gl_setcontextheight</code>(3)</dt>
<dd>set the dimension of a context. </dd>
</dl>
<h3>Drawing primitives</h3>
<dl>
<dt><code>gl_clearscreen</code>(3)</dt>
<dd>clear the screen.</dd>
<dt><code>gl_rgbcolor</code>(3)</dt>
<dd>return pixel value corresponding to an rgb color.</dd>
<dt><code>gl_setpixel</code>(3), <code>gl_setpixelrgb</code>(3)</dt>
<dd>draw a pixel.</dd>
<dt><code>gl_getpixel</code>(3)</dt>
<dd>return the color of a pixel.</dd>
<dt><code>gl_getpixelrgb</code>(3)</dt>
<dd>store color components of a pixel.</dd>
<dt><code>gl_hline</code>(3)</dt>
<dd>draw a horizontal line.</dd>
<dt><code>gl_line</code>(3)</dt>
<dd>draw a line.</dd>
<dt><code>gl_circle</code>(3)</dt>
<dd>draw a circle.</dd>
<dt><code>gl_fillbox</code>(3)</dt>
<dd>fill a rectangular area. </dd>
</dl>
<h3>Copying of screen buffers and page flipping</h3>
<dl>
<dt><code>gl_copyscreen</code>(3)</dt>
<dd>copy the screen contents of contexts.</dd>
<dt><code>gl_setscreenoffset</code>(3)</dt>
<dd>set a memory offset for copyscreen.</dd>
<dt><code>gl_setdisplaystart</code>(3)</dt>
<dd>set the start of the screen are displayed.</dd>
<dt><code>gl_enablepageflipping</code>(3)</dt>
<dd>enables automatic page flipping. </dd>
</dl>
<h3>Clipping</h3>
<dl>
<dt><code>gl_disableclipping</code>(3)</dt>
<dd>disables clipping.</dd>
<dt><code>gl_enableclipping</code>(3)</dt>
<dd>enables clipping.</dd>
<dt><code>gl_setclippingwindow</code>(3)</dt>
<dd>set the clipping window. </dd>
</dl>
<h3>Text drawing primitives</h3>
<dl>
<dt><code>gl_setfont</code>(3)</dt>
<dd>set the text font to be used.</dd>
<dt><code>gl_setfontcolors</code>(3)</dt>
<dd>set the font colors.</dd>
<dt><code>gl_expandfont</code>(3)</dt>
<dd>expand a packed pixel font.</dd>
<dt><code>gl_colorfont</code>(3)</dt>
<dd>change the color of a font.</dd>
<dt><code>gl_setwritemode</code>(3)</dt>
<dd>set the font writemode flags.</dd>
<dt><code>gl_write</code>(3), <code>gl_writen</code>(3)</dt>
<dd>write a text string.</dd>
<dt><code>gl_printf</code>(3)</dt>
<dd>formatted output to the graphics screen.</dd>
<dt><code>gl_font8x8</code>(3)</dt>
<dd>a packed 8&#215;8 pixel font. </dd>
</dl>
<h3>Pix- and Bitmap drawing</h3>
<dl>
<dt><code>gl_getbox</code>(3)</dt>
<dd>copy a rectangular pixmap from the screen to a buffer.</dd>
<dt><code>gl_copybox</code>(3)</dt>
<dd>copy a rectangular screen area.</dd>
<dt><code>gl_copyboxfromcontext</code>(3)</dt>
<dd>copy rectangular area from another context.</dd>
<dt><code>gl_copyboxtocontext</code>(3)</dt>
<dd>copy a rectangular area to another context.</dd>
<dt><code>gl_putbox</code>(3)</dt>
<dd>copy a pixmap to a rectangular area.</dd>
<dt><code>gl_putboxpart</code>(3)</dt>
<dd>copy a partial pixmap to a rectangular area.</dd>
<dt><code>gl_putboxmask</code>(3)</dt>
<dd>copy a masked pixmap to a rectangular area.</dd>
<dt><code>gl_putboxmaskcompiled</code>(3)</dt>
<dd>copy a compiled masked pixmap to a rectangular area.</dd>
<dt><code>gl_compileboxmask</code>(3)</dt>
<dd>compress a masked bitmap.</dd>
<dt><code>gl_compiledboxmasksize</code>(3)</dt>
<dd>compute the size of a compiled masked box.</dd>
<dt><code>gl_scalebox</code>(3)</dt>
<dd>scale a pixmap. </dd>
</dl>
<h3>Palette handling</h3>
<dl>
<dt><code>gl_getpalettecolor</code>(3), <code>gl_getpalettecolors</code>(3), <code>gl_getpalette</code>(3)</dt>
<dd>read the color palette.</dd>
<dt><code>gl_setpalettecolor</code>(3), <code>gl_setpalettecolors</code>(3), <code>gl_setpalette</code>(3)</dt>
<dd>set the color palette.</dd>
<dt><code>gl_setrgbpalette</code>(3)</dt>
<dd>set a 256-color RGB palette. </dd>
</dl>
<h3>Triangle primitives from threeDkit</h3>
<dl>
<dt><code>gl_striangle</code>(3)</dt>
<dd>draw a solid colored triangle.</dd>
<dt><code>gl_triangle</code>(3)</dt>
<dd>draw a triangle with interpolated colors.</dd>
<dt><code>gl_swtriangle</code>(3)</dt>
<dd>draw a solid pixmap mapped on a triangle.</dd>
<dt><code>gl_wtriangle</code>(3)</dt>
<dd>draw a shadowed pixmap mapped on a triangle.</dd>
<dt><code>gl_trisetcolorlookup</code>(3), <code>gl_trigetcolorlookup</code>(3)</dt>
<dd>manages a color lookup table for shadowing.</dd>
<dt><code>gl_trisetdrawpoint</code>(3)</dt>
<dd>set a triangle drawing function.</dd></dl>
<h2>3. Macros Defined In Vgagl.H:</h2>
<dl>
<dt><code>WIDTH</code></dt>
<dd>The width in pixels of the current graphics context.</dd>
<dt><code>HEIGHT</code></dt>
<dd>Height in pixels.</dd>
<dt><code>BYTESPERPIXEL</code></dt>
<dd>Number of bytes per pixel (1, 2, 3 or 4).</dd>
<dt><code>BYTEWIDTH</code></dt>
<dd>Width of a scanline in bytes.</dd>
<dt><code>COLORS</code></dt>
<dd>Number of colors.</dd>
<dt><code>BITSPERPIXEL</code></dt>
<dd>Number of significant color bits.</dd>
<dt><code>VBUF</code></dt>
<dd>Address of the framebuffer.</dd>
<dt><code>__clip</code></dt>
<dd>Clipping flag. </dd>
<dt><code>__clipx1</code></dt>
<dd>
</dd><dt><code>__clipy1</code></dt>
<dd>Top-left corner of clipping window. </dd>
<dt><code>__clipx2</code></dt>
<dd>
</dd><dt><code>__clipy2</code></dt>
<dd>Bottom-right corner of clipping window. </dd>
</dl>
<h2>Bugs</h2>
<p>For three bytes per pixel (true color) modes, it is possible that pixels cross a SVGA segment boundary. This should be correctly handled<tt>&nbsp;<wbr></tt>by most functions, but you never know. It can be avoided by using a logical<br/>
 scanline length that is a divisor of 65536 (a power of 2), like 1024 (as opposed to 960) for 320&#215;200 and 2048 (1920) for 640&#215;480. For 800&#215;600, this is impractical (4096 as opposed to 2400 doesn&#8217;t fit in 2MB). Alternatively, avoid those functions by using a virtual screen. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-svgalib/">svgalib</a></code>(7), <code>libvga.config</code>(5), <code>testgl</code>(6), <code><a href="/docs/linux/man/7-threedkit/">threedkit</a></code>(7), <code>currentcontext</code>(3), <code>gl_allocatecontext</code>(3), <code>gl_circle</code>(3), <code>gl_clearscreen</code>(3), <code>gl_colorfont</code>(3), <code>gl_compileboxmask</code>(3), <code>gl_compiledboxmasksize</code>(3), <code>gl_copybox</code>(3), <code>gl_copyboxfromcontext</code>(3), <code>gl_copyboxtocontext</code>(3), <code>gl_copyscreen</code>(3), <code>gl_disableclipping</code>(3), <code>gl_enableclipping</code>(3), <code>gl_enablepageflipping</code>(3), <code>gl_expandfont</code>(3), <code>gl_fillbox</code>(3), <code>gl_font8x8</code>(3), <code>gl_freecontext</code>(3), <code>gl_getbox</code>(3), <code>gl_getcontext</code>(3), <code>gl_getpalette</code>(3), <code>gl_getpalettecolor</code>(3), <code>gl_getpalettecolors</code>(3), <code>gl_getpixel</code>(3), <code>gl_getpixelrgb</code>(3), <code>gl_hline</code>(3), <code>gl_line</code>(3), <code>gl_putbox</code>(3), <code>gl_putboxmask</code>(3), <code>gl_putboxmaskcompiled</code>(3), <code>gl_putboxpart</code>(3), <code>gl_rgbcolor</code>(3), <code>gl_scalebox</code>(3), <code>gl_setclippingwindow</code>(3), <code>gl_setcontext</code>(3), <code>gl_setcontextheight</code>(3), <code>gl_setcontextvga</code>(3), <code>gl_setcontextvgavirtual</code>(3), <code>gl_setcontextvirtual</code>(3), <code>gl_setcontextwidth</code>(3), <code>gl_setdisplaystart</code>(3), <code>gl_setfont</code>(3), <code>gl_setfontcolors</code>(3), <code>gl_setpalette</code>(3), <code>gl_setpalettecolor</code>(3), <code>gl_setpalettecolors</code>(3), <code>gl_setpixel</code>(3), <code>gl_setpixelrgb</code>(3), <code>gl_setrgbpalette</code>(3), <code>gl_setscreenoffset</code>(3), <code>gl_setwritemode</code>(3), <code>gl_striangle</code>(3), <code>gl_swtriangle</code>(3), <code>gl_triangle</code>(3), <code>gl_trigetcolorlookup</code>(3), <code>gl_trisetcolorlookup</code>(3), <code>gl_trisetdrawpoint</code>(3), <code>gl_write</code>(3), <code>gl_writen</code>(3), <code>gl_wtriangle</code>(3). </p>
<h2>Author</h2>
<p>There are many authors of svgalib. This page was edited by Michael Weller &lt;eowmob [at] exp-math.uni-essen.de&gt;. The original documentation and most of <code>vgagl</code> was done by Harm Hanemaayer &lt;H.Hanemaayer [at] inter.nl.net&gt; though.</p>
