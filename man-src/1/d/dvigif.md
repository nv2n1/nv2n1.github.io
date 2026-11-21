---

title: "dvigif(1)"
name: "dvigif"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dvigif/"
description: "dvipng – A DVI-to-PNG translator"
---

<p> dvipng [options] filename </p>
<p> dvipng [options] [filename] -  </p>
<p> This program makes <font SIZE="-1">PNG</font> and/or <font SIZE="-1">GIF</font> graphics from <font SIZE="-1">DVI</font> files as obtained from TeX and its relatives. </p>
<p> If <font SIZE="-1">GIF</font> support is enabled, <font SIZE="-1">GIF</font> output is chosen by using the <code>dvigif</code> binary or with the <code>--gif</code> option. </p>
<p> The benefits of <code>dvipng</code>/<code>dvigif</code> include </p>
<dl>
<dt>*</dt>
<dd> <p> Speed. It is a very fast bitmap-rendering code for <font SIZE="-1">DVI</font> files, which makes it suitable for generating large amounts of images on-the-fly, as needed in preview-latex, WeBWorK and others. </p>
 </dd>
<dt>*</dt>
<dd> <p> It does not read the postamble, so it can be started before TeX finishes. There is a <code>--follow</code> switch that makes dvipng wait at end-of-file for further output, unless it finds the <font SIZE="-1">POST</font> marker that indicates the end of the <font SIZE="-1">DVI.</font> </p>
 </dd>
<dt>*</dt>
<dd> <p> Interactive query of options. dvipng can read options interactively through stdin, and all options are usable. It is even possible to change the input file through this interface. </p>
 </dd>
<dt>*</dt>
<dd> <p> Supports <font SIZE="-1">PK, VF,</font> PostScript Type1, and TrueType fonts, subfonts (i.e., as used in CJK-LaTeX), color specials, and inclusion of PostScript, <font SIZE="-1">PNG, JPEG</font> or <font SIZE="-1">GIF</font> images. </p>
 </dd>
<dt>*</dt>
<dd> <p> and more... </p>
 </dd></dl>
<h2>OPTIONS</h2>
<p> Many of the parameterless options listed here can be turned off by suffixing the option with a zero (<code>0</code>); for instance, to turn off page reversal, use <code>-r0</code>. Such options are marked with a trailing <code>*</code>. </p>
<dl>
<dt><code>-</code></dt>
<dd> <p> Read additional options from standard input after processing the command line. </p>
 </dd>
<dt><code>--help</code></dt>
<dd> <p> Print a usage message and exit. </p>
 </dd>
<dt><code>--version</code></dt>
<dd> <p> Print the version number and exit. </p>
 </dd>
<dt><code>-bd</code><i>num</i></dt>
<dd>  </dd>
<dt><code>-bd</code><i>color_spec</i></dt>
<dd>  </dd>
<dt><code>-bd &#8216;</code><i>num</i><i>color_spec</i><code>&#8216;</code></dt>
<dd> <p> Set the pixel width of the transparent border (default 0). Using this option will make the image edges transparent, but it only affects pixels with the background color. Giving a <i>color_spec</i> will set the fallback color, to be used in viewers that cannot handle transparency (the default is the background color). The color spec should be in TeX color \special syntax, e.g., &#8216;rgb 1.0 0.0 0.0&#8217;. Setting the fallback color makes the default border width 1 px. </p>
 </dd>
<dt><code>--bdpi</code><i>num</i></dt>
<dd> <p> This option only has an effect when using bitmapped (<font SIZE="-1">PK</font>) fonts. The option sets the base (Metafont) resolution, both horizontal and vertical, to <i>num</i> dpi (dots per inch). This option is necessary when manually selecting Metafont mode with the --mode option (see below). </p>
 </dd>
<dt><code>-bg</code><i>color_spec</i></dt>
<dd> <p> Choose background color for the images. This option will be ignored if there is a background color \special in the <font SIZE="-1">DVI.</font> The color spec should be in TeX color \special syntax, e.g., &#8216;rgb 1.0 0.0 0.0&#8217;. You can also specify &#8216;Transparent&#8217; or &#8216;transparent&#8217; which will give you a transparent background with the normal background as a fallback color. A capitalized &#8216;Transparent&#8217; will give a full-alpha transparency, while an all-lowercase &#8216;transparent&#8217; will give a simple fully transparent background with non-transparent antialiased pixels. The latter would be suitable for viewers who cannot cope with a true alpha channel. <font SIZE="-1">GIF</font> images do not support full alpha transparency, so in case of <font SIZE="-1">GIF</font> output, both variants will use the latter behaviour. </p>
 </dd>
<dt><code>-d</code><i>num</i></dt>
<dd> <p> Set the debug flags, showing what dvipng (thinks it) is doing. This will work unless dvipng has been compiled without the <code>&quot;DEBUG&quot;</code> option (not recommended). Set the flags as you need them, use <code>-d -1</code> as the first option for maximum output. </p>
 </dd>
<dt><code>-D</code><i>num</i></dt>
<dd> <p> Set the output resolution, both horizontal and vertical, to <i>num</i> dpi (dots per inch). </p>
<p> One may want to adjust this to fit a certain text font size (e.g., on a web page), and for a text font height of <i>font_px</i> pixels (in Mozilla) the correct formula is </p>
<pre><code>        &lt;dpi&gt; = &lt;font_px&gt; * 72.27 / 10 [px * TeXpt/in / TeXpt]
</code></pre>
<p> The last division by ten is due to the standard font height 10pt in your document, if you use 12pt, divide by 12. Unfortunately, some proprietary browsers have font height in pt (points), not pixels. You have to rescale that to pixels, using the screen resolution (default is usually 96 dpi) which means the formula is </p>
<pre><code>        &lt;font_px&gt; = &lt;font_pt&gt; * 96 / 72 [pt * px/in / (pt/in)]
</code></pre>
<p> On some high-res screens, the value is instead 120 dpi. Good luck! </p>
 </dd>
<dt><code>--depth*</code></dt>
<dd> <p> Report the depth of the image. This only works reliably when the LaTeX style <i>preview.sty</i> from preview-latex is used with the <code>active</code> option. It reports the number of pixels from the bottom of the image to the baseline of the image. This can be used for vertical positioning of the image in, e.g., web documents, where one would use (Cascading StyleSheets 1) </p>
<pre><code>        &lt;IMG SRC=&quot;&lt;filename.png&gt;&quot; STYLE=&quot;vertical-align: -&lt;depth&gt;px&quot;&gt;
</code></pre>
<p> The depth is a negative offset in this case, so the minus sign is necessary, and the unit is pixels (px). </p>
 </dd>
<dt><code>--dvinum*</code></dt>
<dd> <p> Set this option to make the output page number be the TeX page numbers rather than the physical page number. See the <code>-o</code> switch. </p>
 </dd>
<dt><code>-fg</code><i>color_spec</i></dt>
<dd> <p> Choose foreground color for the images. This option will be ignored if there is a foreground color \special in the <font SIZE="-1">DVI.</font> The color spec should be in TeX color \special syntax, e.g., &#8216;rgb 1.0 0.0 0.0&#8217;. </p>
 </dd>
<dt><code>--follow*</code></dt>
<dd> <p> Wait for data at end-of-file. One of the benefits of dvipng is that it does not read the postamble, so it can be started before TeX finishes. This switch makes dvipng wait at end-of-file for further output, unless it finds the <font SIZE="-1">POST</font> marker that indicates the end of the <font SIZE="-1">DVI.</font> This is similar to <code>tail -f</code> but for DVI-to-PNG conversion. </p>
 </dd>
<dt><code>--freetype*</code></dt>
<dd> <p> Enable/disable FreeType font rendering (default on). This option is available if the FreeType2 font library was present at compilation time. If this is the case, dvipng will have direct support for PostScript Type1 and TrueType fonts internally, rather than using <code>gsftopk</code> for rendering the fonts. If you have PostScript versions of Computer Modern installed, there will be no need to generate bitmapped (<font SIZE="-1">PK</font>) variants on disk of these. Then, you can render images at different (and unusual) resolutions without cluttering the disk with lots of bitmapped fonts. </p>
 </dd>
<dt><code>--gamma</code><i>num</i></dt>
<dd> <p> Control the interpolation of colors in the greyscale anti-aliasing color palette. Default value is 1.0. For 0 &lt; <i>num</i> &lt; 1, the fonts will be lighter (more like the background), and for <i>num</i> &gt; 1, the fonts will be darker (more like the foreground). </p>
 </dd>
<dt><code>--gif*</code></dt>
<dd> <p> The images are output in the <font SIZE="-1">GIF</font> format, if <font SIZE="-1">GIF</font> support is enabled. This is the default for the <code>dvigif</code> binary, which only will be available when <font SIZE="-1">GIF</font> support is enabled. <font SIZE="-1">GIF</font> images are palette images (see the <code>--palette</code> option) and does not support true alpha channels (see the <code>--bg</code> option). See also the <code>--png</code> option. </p>
 </dd>
<dt><code>--height*</code></dt>
<dd> <p> Report the height of the image. This only works reliably when the LaTeX style <i>preview.sty</i> from preview-latex is used with the <code>active</code> option. It reports the number of pixels from the top of the image to the baseline of the image. The total height of the image is obtained as the sum of the values reported from <code>--height</code> and <code>--depth</code>. </p>
 </dd>
<dt><code>-l [=]</code><i>num</i></dt>
<dd> <p> The last page printed will be the first one numbered <i>num</i>. Default is the last page in the document. If <i>num</i> is prefixed by an equals sign, then it (and the argument to the <code>-p</code> option, if specified) is treated as a physical (absolute) page number, rather than a value to compare with the TeX <code>\count0</code> values stored in the <font SIZE="-1">DVI</font> file. Thus, using <code>-l =9</code> will end with the ninth page of the document, no matter what the pages are actually numbered. </p>
 </dd>
<dt><code>--mode</code><i>mode</i></dt>
<dd> <p> This option only has an effect when using bitmapped (<font SIZE="-1">PK</font>) fonts. Use <i>mode</i> as the Metafont device name for the <font SIZE="-1">PK</font> fonts (both for path searching and font generation). This needs to be augmented with the base device resolution, given with the <code>--bdpi</code> option. See the file &lt;<code><a href="ftp://ftp.tug.org/tex/modes.mf">ftp://ftp.tug.org/tex/modes.mf</a></code>&gt; for a list of resolutions and mode names for most devices. </p>
 </dd>
<dt><code>-M*</code></dt>
<dd> <p> This option only has an effect when using bitmapped (<font SIZE="-1">PK</font>) fonts. It turns off automatic <font SIZE="-1">PK</font> font generation (<i>mktexpk</i>). </p>
 </dd>
<dt><code>--nogs*</code></dt>
<dd> <p> This switch prohibits the internal call to GhostScript for displaying PostScript specials. <code>--nogs0</code> turns the call back on. </p>
 </dd>
<dt><code>--nogssafer*</code></dt>
<dd> <p> Normally, if GhostScript is used to render PostScript specials, the GhostScript interpreter is run with the option <code>-dSAFER</code>. The <code>--nogssafer</code> option runs GhostScript without <code>-dSAFER</code>. The <code>-dSAFER</code> option in Ghostscript disables PostScript operators such as deletefile, to prevent possibly malicious PostScript programs from having any effect. </p>
 </dd>
<dt><code>--norawps*</code></dt>
<dd> <p> Some packages generate raw PostScript specials, even non-rendering such specials. This switch turns off the internal call to GhostScript intended to display these raw PostScript specials. <code>--norawps0</code> turns the call back on. </p>
 </dd>
<dt><code>-o</code><i>name</i></dt>
<dd> <p> Send output to the file <i>name</i>. A single occurrence of %d or %01d, ..., %09d will be exchanged for the physical page number (this can be changed, see the <code>--dvinum</code> switch). The default output filename is <i>file</i>%d <code>.png</code> where the input <font SIZE="-1">DVI</font> file was <i>file</i><code>.dvi</code>. </p>
 </dd>
<dt><code>-O</code><i>x-offset</i><code>,</code><i>y-offset</i></dt>
<dd> <p> Move the origin by <i>x-offset</i>,<i>y-offset</i>, a comma-separated pair of dimensions such as <code>.1in,-.3cm</code>. The origin of the page is shifted from the default position (of one inch down, one inch to the right from the upper left corner of the paper) by this amount. </p>
 </dd>
<dt><code>-p [=]</code><i>num</i></dt>
<dd> <p> The first page printed will be the first one numbered <i>num</i>. Default is the first page in the document. If <i>num</i> is prefixed by an equals sign, then it (and the argument to the <code>-l</code> option, if specified) is treated as a physical (absolute) page number, rather than a value to compare with the TeX <code>\count0</code> values stored in the <font SIZE="-1">DVI</font> file. Thus, using <code>-p =3</code> will start with the third page of the document, no matter what the pages are actually numbered. </p>
 </dd>
<dt><code>--palette*</code></dt>
<dd> <p> When an external image is included, <code>dvipng</code> will automatically switch to truecolor mode, to avoid unnecessary delay and quality reduction, and enable the <font SIZE="-1">EPS</font> translator to draw on a transparent background and outside of the boundingbox. This switch will force palette (256-color) output and make <code>dvipng</code> revert to opaque clipped image inclusion. This will also override the <code>--truecolor</code> switch if present. </p>
 </dd>
<dt><code>--picky*</code></dt>
<dd> <p> No images are output when a warning occurs. Normally, dvipng will output an image in spite of a warning, but there may be something missing in this image. One reason to use this option would be if you have a more complete but slower fallback converter. Mainly, this is useful for failed figure inclusion and unknown \special occurrences, but warnings will also occur for missing or unknown color specs and missing <font SIZE="-1">PK</font> fonts. </p>
 </dd>
<dt><code>--png*</code></dt>
<dd> <p> The images are output in the <font SIZE="-1">PNG</font> format. This is the default for the <code>dvipng</code> binary. See also the <code>--gif</code> option. </p>
 </dd>
<dt><code>-pp</code><i>firstpage</i><code>-</code><i>lastpage</i></dt>
<dd> <p> Print pages <i>firstpage</i> through <i>lastpage</i>; but not quite equivalent to <code>-p</code> <i>firstpage</i> <code>-l</code> <i>lastpage</i>. For example, when rendering a book, there may be several instances of a page in the <font SIZE="-1">DVI</font> file (one in <code>&quot;\frontmatter&quot;</code>, one in <code>&quot;\mainmatter&quot;</code>, and one in <code>&quot;\backmatter&quot;</code>). In case of several pages matching, <code>-pp</code> <i>firstpage</i><code>-</code><i>lastpage</i> will render <i>all</i> pages that matches the specified range, while <code>-p</code> <i>firstpage</i> <code>-l</code> <i>lastpage</i> will render the pages from the <i>first</i> occurrence of <i>firstpage</i> to the <i>first</i> occurrence of <i>lastpage</i>. This is the (undocumented) behaviour of dvips. In dvipng you can give both kinds of options, in which case you get all pages that matches the range in <code>-pp</code> between the pages from <code>-p</code> to <code>-l</code>. Also multiple <code>-pp</code> options accumulate, unlike <code>-p</code> and <code>-l</code>. The <code>-</code> separator can also be <code>:</code>. Note that <code>-pp -1</code> will be interpreted as ``all pages up to and including 1&#8217;&#8216;, if you want a page numbered -1 (only the table of contents, say) put <code>-pp -1--1</code>, or more readable, <code>-pp -1:-1</code>. </p>
 </dd>
<dt><code>-q*</code></dt>
<dd> <p> Run quietly. Don&#8217;t chatter about pages converted, etc. to standard output; report no warnings (only errors) to standard error. </p>
 </dd>
<dt><code>-Q</code><i>num</i></dt>
<dd> <p> Set the quality to <i>num</i>. That is, choose the number of antialiasing levels for bitmapped fonts (<font SIZE="-1">PK</font>), to be <i>num</i>*<i>num</i>+1. The default value is 4 which gives 17 levels of antialiasing for antialiased fonts from these two. If FreeType is available, its rendering is unaffected by this option. </p>
 </dd>
<dt><code>-r*</code></dt>
<dd> <p> Toggle output of pages in reverse/forward order. By default, the first page in the <font SIZE="-1">DVI</font> is output first. </p>
 </dd>
<dt><code>--strict*</code></dt>
<dd> <p> The program exits when a warning occurs. Normally, dvipng will output an image in spite of a warning, but there may be something missing in this image. One reason to use this option would be if you have a more complete but slower fallback converter. See the <code>--picky</code> option above for a list of when warnings occur. </p>
 </dd>
<dt><code>-T</code><i>image_size</i></dt>
<dd> <p> Set the image size to <i>image_size</i> which can be either of <code>bbox</code>, <code>tight</code>, or a comma-separated pair of dimensions <i>hsize</i>,<i>vsize</i> such as <code>.1in,.3cm</code>. The default is <code>bbox</code> which produces a <font SIZE="-1">PNG</font> that includes all ink put on the page and in addition the <font SIZE="-1">DVI</font> origin, located 1in from the top and 1in from the left edge of the paper. This usually gives whitespace above and to the left in the produced image. The value <code>tight</code> will make dvipng only include all ink put on the page, producing neat images. </p>
 </dd>
<dt><code>--truecolor*</code></dt>
<dd> <p> This will make <code>dvipng</code> generate truecolor output. Note that truecolor output is automatic if you include an external image in your <font SIZE="-1">DVI,</font> e.g., via a PostScript special (i.e., the <code>graphics</code> or <code>graphicx</code> package). This switch is overridden by the <code>--palette</code> switch. </p>
 </dd>
<dt><code>-v*</code></dt>
<dd> <p> Enable verbose operation. This will currently indicate what fonts is used, in addition to the usual output. </p>
 </dd>
<dt><code>--width*</code></dt>
<dd> <p> Report the width of the image. See also <code>--height</code> and <code>--depth</code>. </p>
 </dd>
<dt><code>-x</code><i>num</i></dt>
<dd> <p> This option is deprecated; it should not be used. It is much better to select the output resolution directly with the <code>-D</code> option. This option sets the magnification ratio to <i>num</i>/1000 and overrides the magnification specified in the <font SIZE="-1">DVI</font> file. Must be between 10 and 100000. It is recommended that you use standard magstep values (1095, 1200, 1440, 1728, 2074, 2488, 2986, and so on) to help reduce the total number of <font SIZE="-1">PK</font> files generated. <i>num</i> may be a real number, not an integer, for increased precision. </p>
 </dd>
<dt><code>-z</code><i>num</i></dt>
<dd> <p> Set the <font SIZE="-1">PNG</font> compression level to <i>num</i>. This option is enabled if your <code>libgd</code> is new enough. The default compression level is 1, which selects maximum speed at the price of slightly larger PNGs. For an older <code>libgd</code>, the hard-soldered value 5 is used. The include file <code>png.h</code> says ``Currently, valid values range from 0 - 9, corresponding directly to the zlib compression levels 0 - 9 (0 - no compression, 9 - &#8216;&#8216;maximal`` compression). Note that tests have shown that zlib compression levels 3-6 usually perform as well as level 9 for <font SIZE="-1">PNG</font> images, and do considerably fewer calculations. In the future, these values may not correspond directly to the zlib compression levels.&#8216;&#8216; </p>
 </dd></dl>
<h2>NOTES</h2>
<p> The full manual is accessible in info format, on most systems by typing </p>
<pre><code>        info dvipng
</code></pre>
<h2>COPYRIGHT</h2>
<p> This program is released under the <font SIZE="-1">GNU</font> Lesser General Public License version 3, see the <font SIZE="-1">COPYING</font> file in the dvipng distribution or &lt;<code><a rel="nofollow" href="http://www.gnu.org/licenses/gpl.html">http://www.gnu.org/licenses/gpl.html</a></code>&gt;. </p>
<p> Copyright (c) 2002-2015 Jan-AAke Larsson </p>
