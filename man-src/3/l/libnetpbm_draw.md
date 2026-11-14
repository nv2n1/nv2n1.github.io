---
title: "libnetpbm_draw(3)"
name: "libnetpbm_draw"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libnetpbm_draw/"
description: "libnetpbm_draw \\- Libnetpbm PPM Drawing Function Manual"
---

<p>Table Of Contents</p>
<h2 class="name">NAME</h2>
<p> libnetpbm_draw \- Libnetpbm PPM Drawing Function Manual </p>
<h2>DESCRIPTION</h2>
<p> This reference manual covers functions in the <code>libnetpbm</code> library for drawing images, using the PPM image format and the <code>libnetpbm</code> in-memory image formats. </p>
<p> We actually have very little information here; this is mainly a framework for adding documentation later if someone becomes interested in this facility. </p>
<h2>The Functions</h2>
<p> The functions are all declared in the <code>ppmdraw.h</code> header file. </p>
<h3><code>ppmd_point_drawproc</code></h3>
<h3><code>ppmd_setlinetype</code></h3>
<h3><code>ppmd_setlineclip</code></h3>
<h3><code>ppmd_line</code></h3>
<h3><code>ppmd_spline3</code></h3>
<h3><code>ppmd_polyspline</code></h3>
<h3><code>ppmd_circle</code></h3>
<h3><code>ppmd_filledrectangle</code></h3>
<h3><code>ppmd_fill_drawproc</code></h3>
<h3><code>ppmd_fill</code></h3>
<h3><code>ppmd_text</code></h3>
<h3><code>ppmd_text_box</code></h3>
<h2>Fonts</h2>
<p> The <code>ppmd_text</code> and <code>ppmd_text_box</code> functions use fonts. You control the fonts using functions described in this section. There is one font that comes with Netpbm, called &#8216;standard&#8217;. It is built into the function library and is the default font. You can create additional fonts and use them instead. </p>
<p> In a program that uses Netpbm drawing facilities, there is a &#8216;current font.&#8217; all drawing of text uses the current font. When the program starts, the current font is &#8216;standard&#8217;; you can change it after that by calling the <code>ppmd_set_font</code> function. </p>
<p> Other than a built-in font, a font lives in file in a format special to Netpbm called Ppmdfont. The file typically has a name that ends in &#8216;.ppmdfont&#8217;. </p>
<p> Use the <code>ppmddumpfont</code> program to dump the contents of a Ppmdfont file in human readable format. </p>
<p> Use the <code>ppmdmkfont</code> program to generate the &#8216;standard&#8217; font as a Ppmdfont file. You don&#8217;t normally need to do this, because &#8216;standard&#8217; is built into <code>libnetpbm</code>. </p>
<p> Use the <code>ppmdcfont</code> program to turn a Ppmdfont file into a C source file that you can compile into a program as a built-in font. Though we don&#8217;t give full instructions here on how to do that, <code>libnetpbm</code>&#8216;s built-in &#8216;standard&#8217; font is a good example. In Netpbm source code, you will find the C source file <code>standardppmdfont.c</code>, which was generated from the file <code>standard.ppmdfont</code> by <code>ppmdcfont</code>. You simply use a pointer to the structure that the C file defines as a font handle, just like one you would get from <code>ppmd_read_font</code>. </p>
<h2>Font File Format</h2>
<p> The font file starts with the characters &#8216;ppmdfont&#8217; (without the quotation marks) in ASCII. </p>
<p> The rest of the format is not yet documented, but it generally describes, for each code point, a sequence of straight line plotting commands to form the glyph for the indicated character. I.e. it is a vector, not raster, font. </p>
<h2>Font Control Functions</h2>
<p> These functions are declared in the header file <code>ppmdfont.h</code>. </p>
<h3><code>ppmd_read_font</code></h3>
<p> This function associates a Ppmdfont file, which you identify by naming the Ppmdfont file, with a handle that you can use to identify the font to other functions. Technically, this function reads the font into memory. </p>
<h3><code>ppmd_free_font</code></h3>
<p> This function releases the handle that you get from <code>ppmd_read_font</code>. It frees resources associated with it; you can&#8217;t use the handle after this. </p>
<h3><code>ppmd_get_font</code></h3>
<p> This function returns the handle of the currently selected font. </p>
<h3><code>ppmd_set_font</code></h3>
<p> This function sets the currently selected font. You identify the font to which to set it with a handle such as you get from <code>ppmd_read_font</code> or <code>ppmd_get_font</code>. </p>
<h2>Index</h2>
<dt><a href="#lbAQ">Fonts</a></p>
<dd>
<dt><a href="#lbAR">Font File Format</a></p>
<dd>
<dt><a href="#lbAS">Font Control Functions</a></p>
<dd>
</dl>
