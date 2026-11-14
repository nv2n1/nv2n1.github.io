---
title: "xpr(1)"
name: "xpr"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xpr/"
description: "xpr – print an X window dump"
---

<h2>NAME</h2>
<p> xpr &#8211; print an X window dump</p>
<h2>SYNOPSIS</h2>
<p> <code>xpr</code> [ <code>-device</code> <i>devtype</i> ] [ <code>-scale</code> <i>scale</i> ] [ <code>-height</code> <i>inches</i> ] [ <code>-width</code> <i>inches</i> ] [ <code>-left</code> <i>inches</i> ] [ <code>-top</code> <i>inches</i> ] [ <code>-header</code> <i>string</i> ] [ <code>-trailer</code> <i>string</i> ] [ <code>-landscape</code> ] [ <code>-portrait</code> ] [ <code>-plane</code> <i>number</i> ] [ <code>-gray</code> ] [ <code>-rv</code> ] [ <code>-compact</code> ] [ <code>-output</code> <i>filename</i> ] [ <code>-append</code> <i>filename</i> ] [ <code>-noff</code> ] [ <code>-split</code> <i>n</i> ] [ <code>-psfig</code> ] [ <code>-density</code> <i>dpi</i> ] [ <code>-cutoff</code> <i>level</i> ] [ <code>-noposition</code> ] [ <code>-gamma</code> <i>correction</i> ] [ <code>-render</code> <i>algorithm</i> ] [ <code>-slide</code> ] [ <i>filename</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <i>xpr</i> takes as input a window dump file produced by <i><a href="/docs/linux/man/1-xwd/">xwd</a>(1)</i> and formats it for output on PostScript printers, the Digital LN03 or LA100, the IBM PP3812 page printer, the HP LaserJet (or other PCL printers), or the HP PaintJet. If no file argument is given, the standard input is used. By default, <i>xpr</i> prints the largest possible representation of the window on the output page. Options allow the user to add headers and trailers, specify margins, adjust the scale and orientation, and append multiple window dumps to a single output file. Output is to standard output unless <code>-output</code> is specified. </p>
<p> <code>Command Options</code> </p>
<dl>
<dt><code>-device</code> <i>devtype</i></p>
<dd> Specifies the device on which the file will be printed. Currently supported:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>la100</code></p>
<dd> Digital LA100</p>
<dt><code>ljet</code></p>
<dd> <font SIZE="-1">HP</font> LaserJet series and other monochrome PCL devices such as ThinkJet, QuietJet, RuggedWriter, <font SIZE="-1">HP</font>2560 series, and <font SIZE="-1">HP</font>2930 series printers</p>
<dt><code>ln03</code></p>
<dd> Digital LN03</p>
<dt><code>pjet</code></p>
<dd> HP PaintJet (color mode)</p>
<dt><code>pjetxl</code></p>
<dd> HP HP PaintJet XL Color Graphics Printer (color mode)</p>
<dt><code>pp</code></p>
<dd> IBM PP3812</p>
<dt><code>ps</code></p>
<dd> PostScript printer</dl>
</dl>
<dt>
<dd> The default is PostScript. <code>-device lw</code> (LaserWriter) is equivalent to -device ps and is provided only for backwards compatibility.</p>
<dt><code>-scale</code> <i>scale</i></p>
<dd> Affects the size of the window on the page. The PostScript, LN03, and HP printers are able to translate each bit in a window pixel map into a grid of a specified size. For example each bit might translate into a 3&#215;3 grid. This would be specified by <code>-scale</code> <i>3</i>. By default a window is printed with the largest scale that will fit onto the page for the specified orientation.</p>
<dt><code>-height</code> <i>inches</i></p>
<dd> Specifies the maximum height of the page.</p>
<dt><code>-width</code> <i>inches</i></p>
<dd> Specifies the maximum width of the page.</p>
<dt><code>-left</code> <i>inches</i></p>
<dd> Specifies the left margin in inches. Fractions are allowed. By default the window is centered in the page.</p>
<dt><code>-top</code> <i>inches</i></p>
<dd> Specifies the top margin for the picture in inches. Fractions are allowed.</p>
<dt><code>-header</code> <i>string</i></p>
<dd> Specifies a header string to be printed above the window.</p>
<dt><code>-trailer</code> <i>string</i></p>
<dd> Specifies a trailer string to be printed below the window.</p>
<dt><code>-landscape</code></p>
<dd> Forces the window to printed in landscape mode. By default a window is printed such that its longest side follows the long side of the paper.</p>
<dt><code>-plane</code> <i>number</i></p>
<dd> Specifies which bit plane to use in an image. The default is to use the entire image and map values into black and white based on color intensities.</p>
<dt><code>-gray</code> <i> 2 | 3 | 4</i></p>
<dd> Uses a simple 2&#215;2, 3&#215;3, or 4&#215;4 gray scale conversion on a color image, rather than mapping to strictly black and white. This doubles, triples, or quadruples the effective width and height of the image.</p>
<dt><code>-portrait</code></p>
<dd> Forces the window to be printed in portrait mode. By default a window is printed such that its longest side follows the long side of the paper.</p>
<dt><code>-rv</code></p>
<dd> Forces the window to be printed in reverse video.</p>
<dt><code>-compact</code></p>
<dd> Uses simple run-length encoding for compact representation of windows with lots of white pixels.</p>
<dt><code>-output</code> <i>filename</i></p>
<dd> Specifies an output file name. If this option is not specified, standard output is used.</p>
<dt><code>-append</code> <i>filename</i></p>
<dd> Specifies a filename previously produced by <i>xpr</i> to which the window is to be appended.</p>
<dt><code>-noff</code></p>
<dd> When specified in conjunction with <code>-append</code>, the window will appear on the same page as the previous window.</p>
<dt><code>-split</code> <i>n</i></p>
<dd> This option allows the user to split a window onto several pages. This might be necessary for very large windows that would otherwise cause the printer to overload and print the page in an obscure manner.</p>
<dt><code>-psfig</code></p>
<dd> Suppress translation of the PostScript picture to the center of the page.</p>
<dt><code>-density</code> <i>dpi</i></p>
<dd> Indicates what dot-per-inch density should be used by the HP printer.</p>
<dt><code>-cutoff</code> <i>level</i></p>
<dd> Changes the intensity level where colors are mapped to either black or white for monochrome output on a LaserJet printer. The <i>level</i> is expressed as percentage of full brightness. Fractions are allowed.</p>
<dt><code>-noposition</code></p>
<dd> This option causes header, trailer, and image positioning command generation to be bypassed for LaserJet, PaintJet and PaintJet XL printers.</p>
<dt><code>-gamma</code> <i>correction</i></p>
<dd> This changes the intensity of the colors printed by PaintJet XL printer. The <i>correction</i> is a floating point value in the range 0.00 to 3.00. Consult the operator&#8217;s manual to determine the correct value for the specific printer.</p>
<dt><code>-render</code> <i>algorithm</i></p>
<dd> This allows PaintJet XL printer to render the image with the best quality versus performance tradeoff. Consult the operator&#8217;s manual to determine which <i>algorithm</i>s are available.</p>
<dt><code>-slide</code></p>
<dd> This option allows overhead transparencies to be printed using the PaintJet and PaintJet XL printers. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-xwd/">xwd</a>(1), <a href="/docs/linux/man/1-xwud/">xwud</a>(1), <a href="/docs/linux/man/1-x/">X</a>(1)</p>
<h2>LIMITATIONS</h2>
<p> The current version of <i>xpr</i> can generally print out on the LN03 most X windows that are not larger than two-thirds of the screen. For example, it will be able to print out a large Emacs window, but it will usually fail when trying to print out the entire screen. The LN03 has memory limitations that can cause it to incorrectly print very large or complex windows. The two most common errors encountered are &#8220;band too complex&#8221; and &#8220;page memory exceeded.&#8221; In the first case, a window may have a particular six pixel row that contains too many changes (from black to white to black). This will cause the printer to drop part of the line and possibly parts of the rest of the page. The printer will flash the number `1&#8242; on its front panel when this problem occurs. A possible solution to this problem is to increase the scale of the picture, or to split the picture onto two or more pages. The second problem, &#8220;page memory exceeded,&#8221; will occur if the picture contains too much black, or if the picture contains complex half-tones such as the background color of a display. When this problem occurs the printer will automatically split the picture into two or more pages. It may flash the number `5&#8242; on its from panel. There is no easy solution to this problem. It will probably be necessary to either cut and paste, or to rework the application to produce a less complex picture. </p>
<p> There are several limitations on the LA100 support: the picture will always be printed in portrait mode, there is no scaling, and the aspect ratio will be slightly off. </p>
<p> Support for PostScript output currently cannot handle the <code>-append</code>, <code>-noff</code> or <code>-split</code> options. </p>
<p> The <code>-compact</code> option is <i>only</i> supported for PostScript output. It compresses white space but not black space, so it is not useful for reverse-video windows. </p>
<p> For color images, should map directly to PostScript image support. </p>
<h2>HP PRINTERS</h2>
<p> If no <code>-density</code> is specified on the command line 300 dots per inch will be assumed for <i>ljet</i> and 90 dots per inch for <i>pjet</i>. Allowable <i>density</i> values for a LaserJet printer are 300, 150, 100, and 75 dots per inch. Consult the operator&#8217;s manual to determine densities supported by other printers. </p>
<p> If no <code>-scale</code> is specified the image will be expanded to fit the printable page area. </p>
<p> The default printable page area is 8&#215;10.5 inches. Other paper sizes can be accommodated using the <code>-height</code> and <code>-width</code> options. </p>
<p> Note that a 1024&#215;768 image fits the default printable area when processed at 100 dpi with scale=1, the same image can also be printed using 300 dpi with scale=3 but will require considerably more data be transferred to the printer. </p>
<p> <i>xpr</i> may be tailored for use with monochrome PCL printers other than the LaserJet. To print on a ThinkJet (<font SIZE="-1">HP</font>2225A) <i>xpr</i> could be invoked as: </p>
<dl>
<dt>
<dd> xpr -density 96 -width 6.667 <i>filename</i></dl>
<p> or for black-and-white output to a PaintJet: </p>
<dl>
<dt>
<dd> xpr -density 180 <i>filename</i></dl>
<p> The monochrome intensity of a pixel is computed as 0.30*R + 0.59*G + 0.11*B. If a pixel&#8217;s computed intensity is less than the <code>-cutoff</code> level it will print as white. This maps light-on-dark display images to black-on-white hardcopy. The default cutoff intensity is 50% of full brightness. Example: specifying <code>-cutoff 87.5</code> moves the white/black intensity point to 87.5% of full brightness. </p>
<p> A LaserJet printer must be configured with sufficient memory to handle the image. For a full page at 300 dots per inch approximately 2MB of printer memory is required. </p>
<p> Color images are produced on the PaintJet at 90 dots per inch. The PaintJet is limited to sixteen colors from its 330 color palette on each horizontal print line. <i>xpr</i> will issue a warning message if more than sixteen colors are encountered on a line. <i>xpr</i> will program the PaintJet for the first sixteen colors encountered on each line and use the nearest matching programmed value for other colors present on the line. </p>
<p> Specifying the <code>-rv</code>, reverse video, option for the PaintJet will cause black and white to be interchanged on the output image. No other colors are changed. </p>
<p> Multiplane images must be recorded by <i>xwd</i> in <i>ZPixmap</i> format. Single plane (monochrome) images may be in either <i>XYPixmap</i> or <i>ZPixmap</i> format. </p>
<p> Some PCL printers do not recognize image positioning commands. Output for these printers will not be centered on the page and header and trailer strings may not appear where expected. </p>
<p> The <code>-gamma</code> and <code>-render</code> options are supported only on the PaintJet XL printers. </p>
<p> The <code>-slide</code> option is not supported for LaserJet printers. </p>
<p> The <code>-split</code> option is not supported for HP printers. </p>
<p> The <code>-gray</code> option is not supported for HP or IBM printers.<br />
 Copyright 1986, Marvin Solomon and the University of Wisconsin.<br />
 Copyright 1988, Hewlett Packard Company.<br />
 See <i><a href="/docs/linux/man/1-x/">X</a>(1)</i> for a full statement of rights and permissions.</p>
<h2>AUTHORS</h2>
<p> Michael R. Gretzinger, MIT Project Athena, Jose Capo, MIT Project Athena (PP3812 support), Marvin Solomon, University of Wisconsin, Bob Scheifler, MIT, Angela Bock and E. Mike Durbin, Rich Inc. (grayscale), Larry Rupp, HP (HP printer support). </p>
<h2>Index</h2>
