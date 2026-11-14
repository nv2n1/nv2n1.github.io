---
title: "dvigif(1)"
name: "dvigif"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dvigif/"
description: "dvipng – A DVI-to-PNG translator"
---

<h2 class="name">NAME</h2>
<p> dvipng &#8211; A DVI-to-PNG translator </p>
<h2>SYNOPSIS</h2>
<p> dvipng [options] filename </p>
<p> dvipng [options] [filename] &#8211;</p>
<h2>DESCRIPTION</h2>
<p> This program makes <font SIZE="-1">PNG</font> and/or <font SIZE="-1">GIF</font> graphics from <font SIZE="-1">DVI</font> files as obtained from TeX and its relatives. </p>
<p> If <font SIZE="-1">GIF</font> support is enabled, <font SIZE="-1">GIF</font> output is chosen by using the <code>dvigif</code> binary or with the <code>&#8211;gif</code> option. </p>
<p> The benefits of <code>dvipng</code>/<code>dvigif</code> include</p>
<dl>
<dt>*</p>
<dd> Speed. It is a very fast bitmap-rendering code for <font SIZE="-1">DVI</font> files, which makes it suitable for generating large amounts of images on-the-fly, as needed in preview-latex, WeBWorK and others.</p>
<dt>*</p>
<dd> It does not read the postamble, so it can be started before TeX finishes. There is a <code>&#8211;follow</code> switch that makes dvipng wait at end-of-file for further output, unless it finds the <font SIZE="-1">POST</font> marker that indicates the end of the <font SIZE="-1">DVI.</font></p>
<dt>*</p>
<dd> Interactive query of options. dvipng can read options interactively through stdin, and all options are usable. It is even possible to change the input file through this interface.</p>
<dt>*</p>
<dd> Supports <font SIZE="-1">PK, VF,</font> PostScript Type1, and TrueType fonts, subfonts (i.e., as used in CJK-LaTeX), color specials, and inclusion of PostScript, <font SIZE="-1">PNG, JPEG</font> or <font SIZE="-1">GIF</font> images.</p>
<dt>*</p>
<dd> and more&#8230;</dl>
<h2>OPTIONS</h2>
<p> Many of the parameterless options listed here can be turned off by suffixing the option with a zero (<code>0</code>); for instance, to turn off page reversal, use <code>-r0</code>. Such options are marked with a trailing <code>*</code>.</p>
<dl>
<dt><code>&#8211;</code></p>
<dd> Read additional options from standard input after processing the command line.</p>
<dt><code>&#8211;help</code></p>
<dd> Print a usage message and exit.</p>
<dt><code>&#8211;version</code></p>
<dd> Print the version number and exit.</p>
<dt><code>-bd</code> <i>num</i></p>
<dd>
<dt><code>-bd</code> <i>color_spec</i></p>
<dd>
<dt><code>-bd &#8216;</code><i>num</i><i>color_spec</i><code>&#8216;</code></p>
<dd> Set the pixel width of the transparent border (default 0). Using this option will make the image edges transparent, but it only affects pixels with the background color. Giving a <i>color_spec</i> will set the fallback color, to be used in viewers that cannot handle transparency (the default is the background color). The color spec should be in TeX color \special syntax, e.g., &#8216;rgb 1.0 0.0 0.0&#8217;. Setting the fallback color makes the default border width 1 px.</p>
<dt><code>&#8211;bdpi</code> <i>num</i></p>
<dd> This option only has an effect when using bitmapped (<font SIZE="-1">PK</font>) fonts. The option sets the base (Metafont) resolution, both horizontal and vertical, to <i>num</i> dpi (dots per inch). This option is necessary when manually selecting Metafont mode with the &#8211;mode option (see below).</p>
<dt><code>-bg</code> <i>color_spec</i></p>
<dd> Choose background color for the images. This option will be ignored if there is a background color \special in the <font SIZE="-1">DVI.</font> The color spec should be in TeX color \special syntax, e.g., &#8216;rgb 1.0 0.0 0.0&#8217;. You can also specify &#8216;Transparent&#8217; or &#8216;transparent&#8217; which will give you a transparent background with the normal background as a fallback color. A capitalized &#8216;Transparent&#8217; will give a full-alpha transparency, while an all-lowercase &#8216;transparent&#8217; will give a simple fully transparent background with non-transparent antialiased pixels. The latter would be suitable for viewers who cannot cope with a true alpha channel. <font SIZE="-1">GIF</font> images do not support full alpha transparency, so in case of <font SIZE="-1">GIF</font> output, both variants will use the latter behaviour.</p>
<dt><code>-d</code> <i>num</i></p>
<dd> Set the debug flags, showing what dvipng (thinks it) is doing. This will work unless dvipng has been compiled without the <tt>&quot;DEBUG&quot;</tt> option (not recommended). Set the flags as you need them, use <code>-d -1</code> as the first option for maximum output.</p>
<dt><code>-D</code> <i>num</i></p>
<dd> Set the output resolution, both horizontal and vertical, to <i>num</i> dpi (dots per inch). </p>
<p> One may want to adjust this to fit a certain text font size (e.g., on a web page), and for a text font height of <i>font_px</i> pixels (in Mozilla) the correct formula is </p>
<pre>
        &lt;dpi&gt; = &lt;font_px&gt; * 72.27 / 10 [px * TeXpt/in / TeXpt]
</pre>
<p> The last division by ten is due to the standard font height 10pt in your document, if you use 12pt, divide by 12. Unfortunately, some proprietary browsers have font height in pt (points), not pixels. You have to rescale that to pixels, using the screen resolution (default is usually 96 dpi) which means the formula is </p>
<pre>
        &lt;font_px&gt; = &lt;font_pt&gt; * 96 / 72 [pt * px/in / (pt/in)]
</pre>
<p> On some high-res screens, the value is instead 120 dpi. Good luck!</p>
<dt><code>&#8211;depth*</code></p>
<dd> Report the depth of the image. This only works reliably when the LaTeX style <i>preview.sty</i> from preview-latex is used with the <code>active</code> option. It reports the number of pixels from the bottom of the image to the baseline of the image. This can be used for vertical positioning of the image in, e.g., web documents, where one would use (Cascading StyleSheets 1) </p>
<pre>
        &lt;IMG SRC=&quot;&lt;filename.png&gt;&quot; STYLE=&quot;vertical-align: -&lt;depth&gt;px&quot;&gt;
</pre>
<p> The depth is a negative offset in this case, so the minus sign is necessary, and the unit is pixels (px).</p>
<dt><code>&#8211;dvinum*</code></p>
<dd> Set this option to make the output page number be the TeX page numbers rather than the physical page number. See the <code>-o</code> switch.</p>
<dt><code>-fg</code> <i>color_spec</i></p>
<dd> Choose foreground color for the images. This option will be ignored if there is a foreground color \special in the <font SIZE="-1">DVI.</font> The color spec should be in TeX color \special syntax, e.g., &#8216;rgb 1.0 0.0 0.0&#8217;.</p>
<dt><code>&#8211;follow*</code></p>
<dd> Wait for data at end-of-file. One of the benefits of dvipng is that it does not read the postamble, so it can be started before TeX finishes. This switch makes dvipng wait at end-of-file for further output, unless it finds the <font SIZE="-1">POST</font> marker that indicates the end of the <font SIZE="-1">DVI.</font> This is similar to <code>tail -f</code> but for DVI-to-PNG conversion.</p>
<dt><code>&#8211;freetype*</code></p>
<dd> Enable/disable FreeType font rendering (default on). This option is available if the FreeType2 font library was present at compilation time. If this is the case, dvipng will have direct support for PostScript Type1 and TrueType fonts internally, rather than using <code>gsftopk</code> for rendering the fonts. If you have PostScript versions of Computer Modern installed, there will be no need to generate bitmapped (<font SIZE="-1">PK</font>) variants on disk of these. Then, you can render images at different (and unusual) resolutions without cluttering the disk with lots of bitmapped fonts.</p>
<dt><code>&#8211;gamma</code> <i>num</i></p>
<dd> Control the interpolation of colors in the greyscale anti-aliasing color palette. Default value is 1.0. For 0 &lt; <i>num</i> &lt; 1, the fonts will be lighter (more like the background), and for <i>num</i> &gt; 1, the fonts will be darker (more like the foreground).</p>
<dt><code>&#8211;gif*</code></p>
<dd> The images are output in the <font SIZE="-1">GIF</font> format, if <font SIZE="-1">GIF</font> support is enabled. This is the default for the <code>dvigif</code> binary, which only will be available when <font SIZE="-1">GIF</font> support is enabled. <font SIZE="-1">GIF</font> images are palette images (see the <code>&#8211;palette</code> option) and does not support true alpha channels (see the <code>&#8211;bg</code> option). See also the <code>&#8211;png</code> option.</p>
<dt><code>&#8211;height*</code></p>
<dd> Report the height of the image. This only works reliably when the LaTeX style <i>preview.sty</i> from preview-latex is used with the <code>active</code> option. It reports the number of pixels from the top of the image to the baseline of the image. The total height of the image is obtained as the sum of the values reported from <code>&#8211;height</code> and <code>&#8211;depth</code>.</p>
<dt><code>-l [=]</code><i>num</i></p>
<dd> The last page printed will be the first one numbered <i>num</i>. Default is the last page in the document. If <i>num</i> is prefixed by an equals sign, then it (and the argument to the <code>-p</code> option, if specified) is treated as a physical (absolute) page number, rather than a value to compare with the TeX <code>
