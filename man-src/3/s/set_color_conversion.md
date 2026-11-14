---
title: "set_color_conversion(3)"
name: "set_color_conversion"
section: "3"
letter: "s"
url: "/docs/linux/man/3-set_color_conversion/"
description: "set_color_conversion – Tells Allegro how to convert images during loading time."
---

<p>set_color_conversion &#8211; Tells Allegro how to convert images during loading time.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void set_color_conversion(int mode);</code></pre>
<h2>Description</h2>
<p>Specifies how to convert images between the various color depths when reading graphics from external bitmap files or datafiles. The mode is a bitmask specifying which types of conversion are allowed. If the appropriate bit is set, data will be converted into the current pixel format (selected by calling the set_color_depth() function), otherwise it will be left in the same format as the disk file, leaving you to convert it manually before the graphic can be displayed. The default mode is total conversion, so that all images will be loaded in the appropriate format for the current video mode. Valid bit flags are: </p>
<pre> COLORCONV_NONE // disable all format
 // conversions
 COLORCONV_8_TO_15 // expand 8-bit to 15-bit
 COLORCONV_8_TO_16 // expand 8-bit to 16-bit
 COLORCONV_8_TO_24 // expand 8-bit to 24-bit
 COLORCONV_8_TO_32 // expand 8-bit to 32-bit
 COLORCONV_15_TO_8 // reduce 15-bit to 8-bit
 COLORCONV_15_TO_16 // expand 15-bit to 16-bit
 COLORCONV_15_TO_24 // expand 15-bit to 24-bit
 COLORCONV_15_TO_32 // expand 15-bit to 32-bit
 COLORCONV_16_TO_8 // reduce 16-bit to 8-bit
 COLORCONV_16_TO_15 // reduce 16-bit to 15-bit
 COLORCONV_16_TO_24 // expand 16-bit to 24-bit
 COLORCONV_16_TO_32 // expand 16-bit to 32-bit
 COLORCONV_24_TO_8 // reduce 24-bit to 8-bit
 COLORCONV_24_TO_15 // reduce 24-bit to 15-bit
 COLORCONV_24_TO_16 // reduce 24-bit to 16-bit
 COLORCONV_24_TO_32 // expand 24-bit to 32-bit
 COLORCONV_32_TO_8 // reduce 32-bit RGB to 8-bit
 COLORCONV_32_TO_15 // reduce 32-bit RGB to 15-bit
 COLORCONV_32_TO_16 // reduce 32-bit RGB to 16-bit
 COLORCONV_32_TO_24 // reduce 32-bit RGB to 24-bit
 COLORCONV_32A_TO_8 // reduce 32-bit RGBA to 8-bit
 COLORCONV_32A_TO_15 // reduce 32-bit RGBA to 15-bit
 COLORCONV_32A_TO_16 // reduce 32-bit RGBA to 16-bit
 COLORCONV_32A_TO_24 // reduce 32-bit RGBA to 24-bit
 COLORCONV_DITHER_PAL // dither when reducing to 8-bit
 COLORCONV_DITHER_HI // dither when reducing to
 // hicolor
 COLORCONV_KEEP_TRANS // keep original transparency</pre>
<p>For convenience, the following macros can be used to select common combinations of these flags: </p>
<pre> COLORCONV_EXPAND_256 // expand 256-color to hi/truecolor
 COLORCONV_REDUCE_TO_256 // reduce hi/truecolor to 256-color
 COLORCONV_EXPAND_15_TO_16 // expand 15-bit hicolor to 16-bit
 COLORCONV_REDUCE_16_TO_15 // reduce 16-bit hicolor to 15-bit
 COLORCONV_EXPAND_HI_TO_TRUE // expand 15/16-bit to 24/32-bit
 COLORCONV_REDUCE_TRUE_TO_HI // reduce 24/32-bit to 15/16-bit
 COLORCONV_24_EQUALS_32 // convert between 24- and 32-bit
 COLORCONV_TOTAL // everything to current format
 COLORCONV_PARTIAL // convert 15 &lt;-&gt; 16-bit and
 // 24 &lt;-&gt; 32-bit
 COLORCONV_MOST // all but hi/truecolor &lt;-&gt; 256
 COLORCONV_DITHER // dither during all color reductions
 COLORCONV_KEEP_ALPHA // convert everything to current format
 // unless it would lose alpha information</pre>
<p>If you enable the COLORCONV_DITHER flag, dithering will be performed whenever truecolor graphics are converted into a hicolor or paletted format, including by the blit() function, and any automatic conversions that take place while reading graphics from disk. This can produce much better looking results, but is obviously slower than a direct conversion. If you intend using converted bitmaps with functions like masked_blit() or draw_sprite(), you should specify the COLORCONV_KEEP_TRANS flag. It will ensure that the masked areas in the bitmap before and after the conversion stay exactly the same, by mapping transparent colors to each other and adjusting colors which would be converted to the transparent color otherwise. It affects every blit() operation between distinct pixel formats and every automatic conversion. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-set_color_depth/">set_color_depth</a></code>(3), <code><a href="/docs/linux/man/3-load_bitmap/">load_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-load_datafile/">load_datafile</a></code>(3), <code><a href="/docs/linux/man/3-fixup_datafile/">fixup_datafile</a></code>(3), <code><a href="/docs/linux/man/3-makecol15_dither/">makecol15_dither</a></code>(3), <code><a href="/docs/linux/man/3-get_color_conversion/">get_color_conversion</a></code>(3), <code><a href="/docs/linux/man/3-exalpha/">exalpha</a></code>(3), <code><a href="/docs/linux/man/3-exblend/">exblend</a></code>(3), <code><a href="/docs/linux/man/3-exdata/">exdata</a></code>(3), <code><a href="/docs/linux/man/3-exexedat/">exexedat</a></code>(3), <code><a href="/docs/linux/man/3-exlights/">exlights</a></code>(3), <code><a href="/docs/linux/man/3-exxfade/">exxfade</a></code>(3) </p>
