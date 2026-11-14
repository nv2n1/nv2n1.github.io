---
title: "pnm2ppa(1)"
name: "pnm2ppa"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pnm2ppa/"
description: "pnm2ppa – convert portable anymap (PNM) images to HP’s PPA printer format."
---

<h2 class="name">NAME</h2>
<p> pnm2ppa &#8211; convert portable anymap (PNM) images to HP&#8217;s PPA printer format. </p>
<h2>SYNOPSIS</h2>
<p> pnm2ppa [options] [ -i <i>infile</i> ] [ -o <i>outfile</i> ] </p>
<h2>DESCRIPTION</h2>
<p> Reads portable anymap (PNM) format as input. Binary PNM formats pnmraw = {ppmraw (color pixmap), pgmraw (graymap), and pbmraw (black-and-white bitmap)} are strongly preferred. Output stream can be locally processed by Hewlett-Packard&#8217;s Printing Performance Architecture (PPA) printers (HP DeskJet 710C, 712C, 720C, 722C, 820C, and 1000C series). </p>
<p> (PNM format output can be produced from PostScript(tm) input by the GhostScript output devices &quot;pbmraw&quot;, &quot;pgmraw&quot; or &quot;ppmraw&quot;, or by &quot;pnmraw&quot;, which will choose one of these formats as appropriate for the document.) <code>pnm2ppa</code> assumes the input resolution is 600dpi (or 300dpi if the command-line option <code>&#8211;dpi300</code> is used): input at higher/lower resolutions will result in a correspondingly larger/smaller printed image, provided it is within the printer&#8217;s allowed size range. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b </code><i>bottommargin</i></p>
<dd> Sets the bottom margin <i>bottommargin</i> in units of 1/600 inches (e.g., <code> -b 150</code> corresponds to 0.25&quot;). </p>
<dt><code>-B </code><i>blackness</i></p>
<dd> Sets the black ink density <i>blackness</i> in drops per pixel (0,1,2,3,4). </p>
<dt><code>&#8211;bi</code></p>
<dd> Force bidirectional print sweeps. </p>
<dt><code>&#8211;bw</code></p>
<dd> Disables the color cartridge; will print in grey scale using only the black cartridge. </p>
<dt><code>-d</code></p>
<dd> Displays the current configuration. </p>
<dt><code>&#8211;dpi300</code></p>
<dd> Treat input resolution as 300dpi instead of 600dpi. </p>
<dt><code>&#8211;eco</code></p>
<dd> Econofast mode: lower print quality that is faster and saves ink. </p>
<dt><code>-f </code><i>configFile</i></p>
<dd> Re-reads configuration from <i>configFile</i> (after initially reading it from /etc/pnm2ppa.conf). </p>
<dt><code>-F </code><i>GammaFile</i></p>
<dd> Overrides reading the color-correction table (Gamma curve) from the default file /etc/pnm2ppa.gamma, and uses <i>GammaFile</i> instead. </p>
<dt><code>&#8211;fd</code></p>
<dd> Enable fast ordered dithering instead of using the slower, but beautiful, Floyd-Steinberg dithering. (Has no effect in &#8211;bw mode.) </p>
<dt><code>-g</code></p>
<dd> Prints a page of color intensity samples (for comparison with gamma.ppm data produced by calibrate_ppa). This is part of a <code>color-correction</code> procedure; see COLOR.txt for more details. </p>
<dt><code>-h, &#8211;help</code></p>
<dd> Displays program usage. </p>
<dt><code>-i </code><i>infile</i></p>
<dd> Input file <i>infile</i> is either a path to a PPM file, or &#8216;-&#8216; to indicate stdin (defaults to stdin). </p>
<dt><code>-l </code><i>leftmargin</i></p>
<dd> Sets the left margin <i>leftmargin</i> in units of 1/600 inches (e.g., <code>-l 150</code> corresponds to 0.25&quot;). </p>
<dt><code>&#8211;noGamma</code></p>
<dd> Switches off any color-correction. </p>
<dt><code>-o </code><i>outfile</i> | &#8211;</p>
<dd> Output file <i>outfile</i> is either a path to a file or device, or &#8216;-&#8216; to indicate stdout (defaults to stdout). </p>
<dt><code>-p</code></p>
<dd> Disables the black ink cartridge; i.e., print using only the color ink cartridge, even for printing &quot;black&quot;. This might be useful for printing high-quality color images. </p>
<dt><code>-r </code><i>rightmargin</i></p>
<dd> Sets the right margin <i>rightmargin</i> in units of 1/600 inches (e.g., <code>-r 150</code> corresponds to 0.25&quot;). </p>
<dt><code>-s </code><i>papersize</i></p>
<dd> Sets the default paper size (now used only for color-correction output produced by the <code>-g</code> option). In normal use, pnm2ppa now instead reads the paper dimensions from pnm input file headers, and checks that it is a valid papersize for the given printer model. Possible values for <i>papersize</i> are <code>a4</code> (A4), <code>letter</code> or <code>us</code> (US Letter, 8.5&quot;x11&quot;), <code>legal</code> (US Legal, 8.5&quot;x14&quot;). The default is US Letter. </p>
<dt><code>-t </code><i>topmargin</i></p>
<dd> Sets the top margin <i>topmargin</i> in units of 1/600 inches (ie <code>-t 150</code> corresponds to 0.25&quot;). </p>
<dt><code>&#8211;uni</code></p>
<dd> Force unidirectional (left to right) print sweeps. Useful if &quot;shearing&quot; is a problem for high quality color images. </p>
<dt><code>-v </code><i>printertype</i></p>
<dd> Selects the printer model. Possible values of <i>printertype</i> are: <code>710</code>, <code>712</code>, <code>720</code>, <code>722</code>, <code>820</code> and <code>1000</code>. The default is the HP DeskJet 7X0 Series (710, 712, 720, 722). </p>
<dt><code>&#8211;verbose</code></p>
<dd> Displays the program&#8217;s System Log messages on the standard output, as well. </p>
<dt><code>&#8211;version</code></p>
<dd> Displays the program&#8217;s version information. </p>
<dt><code>-x </code><i>xoffset</i></p>
<dd> Sets the x-offset <i>xoffset</i> from the left of the page. Units are 1/600 inches. </p>
<dt><code>-y </code><i>yoffset</i></p>
<dd> Sets the y-offset <i>yoffset</i> from the top of the page. Units are 1/600 inches. </p>
<p>&nbsp;</dl>
<h2>NOTES</h2>
<p> The default configuration file <i>/etc/pnm2ppa.conf</i> is read in first. Command line arguments then modify the resulting definitions. </p>
<p> The <code>-v</code> option resets all definitions (margins, offsets, etc.) back to the inbuilt defaults for that printer and should be used before subsequent <code>-b</code>, <code>-l</code>, <code>-r</code>, <code>-t</code>, <code>-x</code> and <code>-y</code> arguments.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-pnm/">pnm</a>(5), <a href="/docs/linux/man/5-ppm/">ppm</a>(5), <a href="/docs/linux/man/5-pbm/">pbm</a>(5) </p>
<h2>FILES</h2>
<dl>
<dt><i>/etc/pnm2ppa.conf</i></p>
<dd> Default configuration file. </p>
<dt><i>/etc/pnm2ppa.gamma</i></p>
<dd> Default Gamma (color-correction) file. </p>
</dl>
<h2>AUTHOR</h2>
<p> This code is licensed under the GNU Public License version 2. See LICENSE for details. </p>
<p> (c) 1998-1999<tt>&nbsp;<wbr>&nbsp;</tt>Tim Norman</p>
<p> (c) 1999<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Giorgio Marzano</p>
<p> (c) 1999<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Andrew van der Stock</p>
<p> (c) 1998-2002<tt>&nbsp;<wbr>&nbsp;</tt>Various authors for many, many fixes</p>
<h2>HISTORY</h2>
<p> This program was originally pbm2ppa, written by Tim Norman. It originally supported black and white output on the 820 series. Tim added nascent color support in early 1999. In May 1999, Giorgio Marzano started making real headway in getting color support working properly. Andrew van der Stock has maintained the code since September 1999, and made it available at <a rel="nofollow" href="http://sourceforge.net/projects/pnm2ppa.">http://sourceforge.net/projects/pnm2ppa.</a></p>
<h2>BUGS</h2>
<p> Faint horizontal lines marking boundaries between print sweeps may be visible. You may get better results when printing images, with the options:<br />
&nbsp;<code>&nbsp;-p &#8211;uni&nbsp;</code>&nbsp;(this may no longer apply since recent code improvements). </p>
<h2>Index</h2>
