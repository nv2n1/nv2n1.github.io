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
<p><code>0.</code> Introduction<br />
 <code>1.</code> How to use vgagl<br />
 <code>2.</code> Description of vgagl functions<br />
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
<dd><code>vga_setmode(G320x200x256);</code><br />
 <code>gl_setcontextvga(G320x200x256);</code></dl>
<p> In this example, the context is set to the physical screen. The context can be saved (only the screen type, not the contents) into a variable, e.g. </p>
<dl>
<dd><code>GraphicsContext physicalscreen;</code><br />
 <code>gl_getcontext(&amp;physicalscreen).</code></dl>
<p> To define a virtual screen in system memory, use <code><a href="/docs/linux/man/3-gl_setcontextvgavirtual/">gl_setcontextvgavirtual</a></code>(3): </p>
<dl>
<dd><code>gl_setcontextvgavirtual(G320x200x256)</code></dl>
<p> which allocates space for a screen identical to 320x200x256 graphics mode, and makes this virtual screen the current graphics context. </p>
<p> The virtual screen can now be copied to the physical screen as follows: </p>
<dl>
<dd><code>gl_copyscreen(&amp;physicalscreen);</code></dl>
<p> Note that with a virtual screen in system memory, it is possible to add fast X-Window support to a program, using MITSHM to copy the framebuffer to the screen window.</p>
<h2>2. Description Of Vgagl Functions</h2>
<h3>Context management</h3>
<dl>
<dt><code><a href="/docs/linux/man/3-gl_getcontext/">gl_getcontext</a></code>(3), <code><a href="/docs/linux/man/3-currentcontext/">currentcontext</a></code>(3)</p>
<dd>get the current graphics contents..</p>
<dt><code><a href="/docs/linux/man/3-gl_setcontext/">gl_setcontext</a></code>(3)</p>
<dd>set a previously saved context.</p>
<dt><code><a href="/docs/linux/man/3-gl_setcontextvga/">gl_setcontextvga</a></code>(3)</p>
<dd>set the context to the physical screen.</p>
<dt><code><a href="/docs/linux/man/3-gl_setcontextvgavirtual/">gl_setcontextvgavirtual</a></code>(3)</p>
<dd>set the context to a virtual mode.</p>
<dt><code><a href="/docs/linux/man/3-gl_setcontextvirtual/">gl_setcontextvirtual</a></code>(3)</p>
<dd>define a virtual context.</p>
<dt><code><a href="/docs/linux/man/3-gl_allocatecontext/">gl_allocatecontext</a></code>(3)</p>
<dd>allocate a graphics context.</p>
<dt><code><a href="/docs/linux/man/3-gl_freecontext/">gl_freecontext</a></code>(3)</p>
<dd>free a virtual screen.</p>
<dt><code><a href="/docs/linux/man/3-gl_setcontextwidth/">gl_setcontextwidth</a></code>(3), <code><a href="/docs/linux/man/3-gl_setcontextheight/">gl_setcontextheight</a></code>(3)</p>
<dd>set the dimension of a context. </p>
</dl>
<h3>Drawing primitives</h3>
<dl>
<dt><code><a href="/docs/linux/man/3-gl_clearscreen/">gl_clearscreen</a></code>(3)</p>
<dd>clear the screen.</p>
<dt><code><a href="/docs/linux/man/3-gl_rgbcolor/">gl_rgbcolor</a></code>(3)</p>
<dd>return pixel value corresponding to an rgb color.</p>
<dt><code><a href="/docs/linux/man/3-gl_setpixel/">gl_setpixel</a></code>(3), <code><a href="/docs/linux/man/3-gl_setpixelrgb/">gl_setpixelrgb</a></code>(3)</p>
<dd>draw a pixel.</p>
<dt><code><a href="/docs/linux/man/3-gl_getpixel/">gl_getpixel</a></code>(3)</p>
<dd>return the color of a pixel.</p>
<dt><code><a href="/docs/linux/man/3-gl_getpixelrgb/">gl_getpixelrgb</a></code>(3)</p>
<dd>store color components of a pixel.</p>
<dt><code><a href="/docs/linux/man/3-gl_hline/">gl_hline</a></code>(3)</p>
<dd>draw a horizontal line.</p>
<dt><code><a href="/docs/linux/man/3-gl_line/">gl_line</a></code>(3)</p>
<dd>draw a line.</p>
<dt><code><a href="/docs/linux/man/3-gl_circle/">gl_circle</a></code>(3)</p>
<dd>draw a circle.</p>
<dt><code><a href="/docs/linux/man/3-gl_fillbox/">gl_fillbox</a></code>(3)</p>
<dd>fill a rectangular area. </p>
</dl>
<h3>Copying of screen buffers and page flipping</h3>
<dl>
<dt><code><a href="/docs/linux/man/3-gl_copyscreen/">gl_copyscreen</a></code>(3)</p>
<dd>copy the screen contents of contexts.</p>
<dt><code><a href="/docs/linux/man/3-gl_setscreenoffset/">gl_setscreenoffset</a></code>(3)</p>
<dd>set a memory offset for copyscreen.</p>
<dt><code><a href="/docs/linux/man/3-gl_setdisplaystart/">gl_setdisplaystart</a></code>(3)</p>
<dd>set the start of the screen are displayed.</p>
<dt><code><a href="/docs/linux/man/3-gl_enablepageflipping/">gl_enablepageflipping</a></code>(3)</p>
<dd>enables automatic page flipping. </p>
</dl>
<h3>Clipping</h3>
<dl>
<dt><code><a href="/docs/linux/man/3-gl_disableclipping/">gl_disableclipping</a></code>(3)</p>
<dd>disables clipping.</p>
<dt><code><a href="/docs/linux/man/3-gl_enableclipping/">gl_enableclipping</a></code>(3)</p>
<dd>enables clipping.</p>
<dt><code><a href="/docs/linux/man/3-gl_setclippingwindow/">gl_setclippingwindow</a></code>(3)</p>
<dd>set the clipping window. </p>
</dl>
<h3>Text drawing primitives</h3>
<dl>
<dt><code><a href="/docs/linux/man/3-gl_setfont/">gl_setfont</a></code>(3)</p>
<dd>set the text font to be used.</p>
<dt><code><a href="/docs/linux/man/3-gl_setfontcolors/">gl_setfontcolors</a></code>(3)</p>
<dd>set the font colors.</p>
<dt><code><a href="/docs/linux/man/3-gl_expandfont/">gl_expandfont</a></code>(3)</p>
<dd>expand a packed pixel font.</p>
<dt><code><a href="/docs/linux/man/3-gl_colorfont/">gl_colorfont</a></code>(3)</p>
<dd>change the color of a font.</p>
<dt><code><a href="/docs/linux/man/3-gl_setwritemode/">gl_setwritemode</a></code>(3)</p>
<dd>set the font writemode flags.</p>
<dt><code><a href="/docs/linux/man/3-gl_write/">gl_write</a></code>(3), <code><a href="/docs/linux/man/3-gl_writen/">gl_writen</a></code>(3)</p>
<dd>write a text string.</p>
<dt><code><a href="/docs/linux/man/3-gl_printf/">gl_printf</a></code>(3)</p>
<dd>formatted output to the graphics screen.</p>
<dt><code><a href="/docs/linux/man/3-gl_font8x8/">gl_font8x8</a></code>(3)</p>
<dd>a packed 8&#215;8 pixel font. </p>
</dl>
<h3>Pix- and Bitmap drawing</h3>
<dl>
<dt><code><a href="/docs/linux/man/3-gl_getbox/">gl_getbox</a></code>(3)</p>
<dd>copy a rectangular pixmap from the screen to a buffer.</p>
<dt><code><a href="/docs/linux/man/3-gl_copybox/">gl_copybox</a></code>(3)</p>
<dd>copy a rectangular screen area.</p>
<dt><code><a href="/docs/linux/man/3-gl_copyboxfromcontext/">gl_copyboxfromcontext</a></code>(3)</p>
<dd>copy rectangular area from another context.</p>
<dt><code><a href="/docs/linux/man/3-gl_copyboxtocontext/">gl_copyboxtocontext</a></code>(3)</p>
<dd>copy a rectangular area to another context.</p>
<dt><code><a href="/docs/linux/man/3-gl_putbox/">gl_putbox</a></code>(3)</p>
<dd>copy a pixmap to a rectangular area.</p>
<dt><code><a href="/docs/linux/man/3-gl_putboxpart/">gl_putboxpart</a></code>(3)</p>
<dd>copy a partial pixmap to a rectangular area.</p>
<dt><code><a href="/docs/linux/man/3-gl_putboxmask/">gl_putboxmask</a></code>(3)</p>
<dd>copy a masked pixmap to a rectangular area.</p>
<dt><code><a href="/docs/linux/man/3-gl_putboxmaskcompiled/">gl_putboxmaskcompiled</a></code>(3)</p>
<dd>copy a compiled masked pixmap to a rectangular area.</p>
<dt><code><a href="/docs/linux/man/3-gl_compileboxmask/">gl_compileboxmask</a></code>(3)</p>
<dd>compress a masked bitmap.</p>
<dt><code><a href="/docs/linux/man/3-gl_compiledboxmasksize/">gl_compiledboxmasksize</a></code>(3)</p>
<dd>compute the size of a compiled masked box.</p>
<dt><code><a href="/docs/linux/man/3-gl_scalebox/">gl_scalebox</a></code>(3)</p>
<dd>scale a pixmap. </p>
</dl>
<h3>Palette handling</h3>
<dl>
<dt><code><a href="/docs/linux/man/3-gl_getpalettecolor/">gl_getpalettecolor</a></code>(3), <code><a href="/docs/linux/man/3-gl_getpalettecolors/">gl_getpalettecolors</a></code>(3), <code><a href="/docs/linux/man/3-gl_getpalette/">gl_getpalette</a></code>(3)</p>
<dd>read the color palette.</p>
<dt><code><a href="/docs/linux/man/3-gl_setpalettecolor/">gl_setpalettecolor</a></code>(3), <code><a href="/docs/linux/man/3-gl_setpalettecolors/">gl_setpalettecolors</a></code>(3), <code><a href="/docs/linux/man/3-gl_setpalette/">gl_setpalette</a></code>(3)</p>
<dd>set the color palette.</p>
<dt><code><a href="/docs/linux/man/3-gl_setrgbpalette/">gl_setrgbpalette</a></code>(3)</p>
<dd>set a 256-color RGB palette. </p>
</dl>
<h3>Triangle primitives from threeDkit</h3>
<dl>
<dt><code><a href="/docs/linux/man/3-gl_striangle/">gl_striangle</a></code>(3)</p>
<dd>draw a solid colored triangle.</p>
<dt><code><a href="/docs/linux/man/3-gl_triangle/">gl_triangle</a></code>(3)</p>
<dd>draw a triangle with interpolated colors.</p>
<dt><code><a href="/docs/linux/man/3-gl_swtriangle/">gl_swtriangle</a></code>(3)</p>
<dd>draw a solid pixmap mapped on a triangle.</p>
<dt><code><a href="/docs/linux/man/3-gl_wtriangle/">gl_wtriangle</a></code>(3)</p>
<dd>draw a shadowed pixmap mapped on a triangle.</p>
<dt><code><a href="/docs/linux/man/3-gl_trisetcolorlookup/">gl_trisetcolorlookup</a></code>(3), <code><a href="/docs/linux/man/3-gl_trigetcolorlookup/">gl_trigetcolorlookup</a></code>(3)</p>
<dd>manages a color lookup table for shadowing.</p>
<dt><code><a href="/docs/linux/man/3-gl_trisetdrawpoint/">gl_trisetdrawpoint</a></code>(3)</p>
<dd>set a triangle drawing function.</dl>
<h2>3. Macros Defined In Vgagl.H:</h2>
<dl>
<dt><code>WIDTH</code></p>
<dd>The width in pixels of the current graphics context.</p>
<dt><code>HEIGHT</code></p>
<dd>Height in pixels.</p>
<dt><code>BYTESPERPIXEL</code></p>
<dd>Number of bytes per pixel (1, 2, 3 or 4).</p>
<dt><code>BYTEWIDTH</code></p>
<dd>Width of a scanline in bytes.</p>
<dt><code>COLORS</code></p>
<dd>Number of colors.</p>
<dt><code>BITSPERPIXEL</code></p>
<dd>Number of significant color bits.</p>
<dt><code>VBUF</code></p>
<dd>Address of the framebuffer.</p>
<dt><code>__clip</code></p>
<dd>Clipping flag. </p>
<dt><code>__clipx1</code></p>
<dd>
<dt><code>__clipy1</code></p>
<dd>Top-left corner of clipping window. </p>
<dt><code>__clipx2</code></p>
<dd>
<dt><code>__clipy2</code></p>
<dd>Bottom-right corner of clipping window. </p>
</dl>
<h2>Bugs</h2>
<p>For three bytes per pixel (true color) modes, it is possible that pixels cross a SVGA segment boundary. This should be correctly handled<tt>&nbsp;<wbr></tt>by most functions, but you never know. It can be avoided by using a logical<br />
 scanline length that is a divisor of 65536 (a power of 2), like 1024 (as opposed to 960) for 320&#215;200 and 2048 (1920) for 640&#215;480. For 800&#215;600, this is impractical (4096 as opposed to 2400 doesn&#8217;t fit in 2MB). Alternatively, avoid those functions by using a virtual screen. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-svgalib/">svgalib</a></code>(7), <code><a href="/docs/linux/man/5-libvga-config/">libvga.config</a></code>(5), <code><a href="/docs/linux/man/6-testgl/">testgl</a></code>(6), <code><a href="/docs/linux/man/7-threedkit/">threedkit</a></code>(7), <code><a href="/docs/linux/man/3-currentcontext/">currentcontext</a></code>(3), <code><a href="/docs/linux/man/3-gl_allocatecontext/">gl_allocatecontext</a></code>(3), <code><a href="/docs/linux/man/3-gl_circle/">gl_circle</a></code>(3), <code><a href="/docs/linux/man/3-gl_clearscreen/">gl_clearscreen</a></code>(3), <code><a href="/docs/linux/man/3-gl_colorfont/">gl_colorfont</a></code>(3), <code><a href="/docs/linux/man/3-gl_compileboxmask/">gl_compileboxmask</a></code>(3), <code><a href="/docs/linux/man/3-gl_compiledboxmasksize/">gl_compiledboxmasksize</a></code>(3), <code><a href="/docs/linux/man/3-gl_copybox/">gl_copybox</a></code>(3), <code><a href="/docs/linux/man/3-gl_copyboxfromcontext/">gl_copyboxfromcontext</a></code>(3), <code><a href="/docs/linux/man/3-gl_copyboxtocontext/">gl_copyboxtocontext</a></code>(3), <code><a href="/docs/linux/man/3-gl_copyscreen/">gl_copyscreen</a></code>(3), <code><a href="/docs/linux/man/3-gl_disableclipping/">gl_disableclipping</a></code>(3), <code><a href="/docs/linux/man/3-gl_enableclipping/">gl_enableclipping</a></code>(3), <code><a href="/docs/linux/man/3-gl_enablepageflipping/">gl_enablepageflipping</a></code>(3), <code><a href="/docs/linux/man/3-gl_expandfont/">gl_expandfont</a></code>(3), <code><a href="/docs/linux/man/3-gl_fillbox/">gl_fillbox</a></code>(3), <code><a href="/docs/linux/man/3-gl_font8x8/">gl_font8x8</a></code>(3), <code><a href="/docs/linux/man/3-gl_freecontext/">gl_freecontext</a></code>(3), <code><a href="/docs/linux/man/3-gl_getbox/">gl_getbox</a></code>(3), <code><a href="/docs/linux/man/3-gl_getcontext/">gl_getcontext</a></code>(3), <code><a href="/docs/linux/man/3-gl_getpalette/">gl_getpalette</a></code>(3), <code><a href="/docs/linux/man/3-gl_getpalettecolor/">gl_getpalettecolor</a></code>(3), <code><a href="/docs/linux/man/3-gl_getpalettecolors/">gl_getpalettecolors</a></code>(3), <code><a href="/docs/linux/man/3-gl_getpixel/">gl_getpixel</a></code>(3), <code><a href="/docs/linux/man/3-gl_getpixelrgb/">gl_getpixelrgb</a></code>(3), <code><a href="/docs/linux/man/3-gl_hline/">gl_hline</a></code>(3), <code><a href="/docs/linux/man/3-gl_line/">gl_line</a></code>(3), <code><a href="/docs/linux/man/3-gl_putbox/">gl_putbox</a></code>(3), <code><a href="/docs/linux/man/3-gl_putboxmask/">gl_putboxmask</a></code>(3), <code><a href="/docs/linux/man/3-gl_putboxmaskcompiled/">gl_putboxmaskcompiled</a></code>(3), <code><a href="/docs/linux/man/3-gl_putboxpart/">gl_putboxpart</a></code>(3), <code><a href="/docs/linux/man/3-gl_rgbcolor/">gl_rgbcolor</a></code>(3), <code><a href="/docs/linux/man/3-gl_scalebox/">gl_scalebox</a></code>(3), <code><a href="/docs/linux/man/3-gl_setclippingwindow/">gl_setclippingwindow</a></code>(3), <code><a href="/docs/linux/man/3-gl_setcontext/">gl_setcontext</a></code>(3), <code><a href="/docs/linux/man/3-gl_setcontextheight/">gl_setcontextheight</a></code>(3), <code><a href="/docs/linux/man/3-gl_setcontextvga/">gl_setcontextvga</a></code>(3), <code><a href="/docs/linux/man/3-gl_setcontextvgavirtual/">gl_setcontextvgavirtual</a></code>(3), <code><a href="/docs/linux/man/3-gl_setcontextvirtual/">gl_setcontextvirtual</a></code>(3), <code><a href="/docs/linux/man/3-gl_setcontextwidth/">gl_setcontextwidth</a></code>(3), <code><a href="/docs/linux/man/3-gl_setdisplaystart/">gl_setdisplaystart</a></code>(3), <code><a href="/docs/linux/man/3-gl_setfont/">gl_setfont</a></code>(3), <code><a href="/docs/linux/man/3-gl_setfontcolors/">gl_setfontcolors</a></code>(3), <code><a href="/docs/linux/man/3-gl_setpalette/">gl_setpalette</a></code>(3), <code><a href="/docs/linux/man/3-gl_setpalettecolor/">gl_setpalettecolor</a></code>(3), <code><a href="/docs/linux/man/3-gl_setpalettecolors/">gl_setpalettecolors</a></code>(3), <code><a href="/docs/linux/man/3-gl_setpixel/">gl_setpixel</a></code>(3), <code><a href="/docs/linux/man/3-gl_setpixelrgb/">gl_setpixelrgb</a></code>(3), <code><a href="/docs/linux/man/3-gl_setrgbpalette/">gl_setrgbpalette</a></code>(3), <code><a href="/docs/linux/man/3-gl_setscreenoffset/">gl_setscreenoffset</a></code>(3), <code><a href="/docs/linux/man/3-gl_setwritemode/">gl_setwritemode</a></code>(3), <code><a href="/docs/linux/man/3-gl_striangle/">gl_striangle</a></code>(3), <code><a href="/docs/linux/man/3-gl_swtriangle/">gl_swtriangle</a></code>(3), <code><a href="/docs/linux/man/3-gl_triangle/">gl_triangle</a></code>(3), <code><a href="/docs/linux/man/3-gl_trigetcolorlookup/">gl_trigetcolorlookup</a></code>(3), <code><a href="/docs/linux/man/3-gl_trisetcolorlookup/">gl_trisetcolorlookup</a></code>(3), <code><a href="/docs/linux/man/3-gl_trisetdrawpoint/">gl_trisetdrawpoint</a></code>(3), <code><a href="/docs/linux/man/3-gl_write/">gl_write</a></code>(3), <code><a href="/docs/linux/man/3-gl_writen/">gl_writen</a></code>(3), <code><a href="/docs/linux/man/3-gl_wtriangle/">gl_wtriangle</a></code>(3). </p>
<h2>Author</h2>
<p>There are many authors of svgalib. This page was edited by Michael Weller &lt;eowmob [at] exp-math.uni-essen.de&gt;. The original documentation and most of <code>vgagl</code> was done by Harm Hanemaayer &lt;H.Hanemaayer [at] inter.nl.net&gt; though.</p>
