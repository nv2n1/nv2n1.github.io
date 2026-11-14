---
title: "mkbitmap(1)"
name: "mkbitmap"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mkbitmap/"
description: "mkbitmap – transform images into bitmaps with scaling and filtering"
---

<h2>NAME</h2>
<p> mkbitmap &#8211; transform images into bitmaps with scaling and filtering</p>
<h2>SYNOPSIS</h2>
<pre><code>
mkbitmap[options][filename...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>mkbitmap</code> reads an image, and applies one or more of the following operations to it, in this order: inversion, highpass filtering, scaling, and thresholding. Each operation can be individually controlled and turned on or off. </p>
<p> The principal use of <code>mkbitmap</code> is to convert color or greyscale images into a format suitable as input for other programs, particularly the tracing program <code><a href="/docs/linux/man/1-potrace/">potrace</a></code>(1). It is particularly useful for converting scanned line art, such as cartoons, handwritten text, etc., to high-resolution bilevel images. </p>
<p> <i>Highpass filtering</i> can be used to ensure that foreground features such as lines and text are preserved, while at the same time compensating for uneven background. Optional <i>blurring</i> can be applied to smooth out the image and remove visual noise. <i>Scaling</i> is important because a scanned greyscale image contains more visual detail than a bilevel image at the same resolution. By scaling the image to a higher resolution (using interpolation) before thresholding it, some of this detail is preserved. <i>Thresholding</i> means converting a greyscale image to a bilevel image using only black and white pixels. Pixels that are darker than a certain threshold value are converted to black. Optional <i>inversion</i> is useful if the input image shows bright features on dark background, such as a picture of chalk drawings on a blackboard. </p>
<p> Supported input formats are PNM (PBM, PGM, PPM) and BMP. The output formats are PBM for bitmaps, and PGM for greymaps.</p>
<h2>OPTIONS</h2>
<h3>General options:</h3>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> print help message and exit.</p>
<dt><code>-v, &#8211;version</code></p>
<dd> print version info and exit.</p>
<dt><code>-l, &#8211;license</code></p>
<dd> print license info and exit.</dl>
<h3>Input/output options:</h3>
<dl>
<dt><i>filename</i></p>
<dd> If filename arguments are given, then <code>mkbitmap</code> will by default create one output file for each input filename given. The name of the output file is obtained from the input filename by changing its suffix to &quot;.pbm&quot; or &quot;.pgm&quot;. If the name of the input file and output file would be identical, then an additional suffix &quot;-out&quot; is appended to the output filename. If no filename arguments are given, then <code>mkbitmap</code> acts as a filter, reading from standard input and writing to standard output. A filename of &quot;-&quot; may be given to specify reading from standard input; the output for this argument will then be written to standard output. Each input file may contain one or more images.</p>
<dt><code>-o </code><i>filename</i>, &#8211;output <i>filename</i></p>
<dd> write output to this file. All output is concatenated and directed to the specified file. This overrides the default behavior of creating one output file for each input file. A filename of &quot;-&quot; may be given to specify writing to standard output.</dl>
<h3>Image processing options:</h3>
<dl>
<dt><code>-x, &#8211;nodefaults</code></p>
<dd> Turn off default options. Normally, the following options are preselected by default: <code>-f 4 -s 2 -3 -t 0.45</code>. The <code>-x</code> option disables these defaults; thus, <code>mkbitmap -x</code> does nothing but copy a greyscale image from the input to the output. Other processing options can then be added one by one; e.g., <code>mkbitmap -xf10</code> does only highpass filtering, <code>mkbitmap -xt0.5</code> does only thresholding, etc.</p>
<dt><code>-i, &#8211;invert</code></p>
<dd> Invert the input image. If this option is chosen, it is applied to the image before any other operation. It is used to deal with white-on-black images, such as photographs of chalk drawings on a blackboard. Note that the behavior of this option is not in general the same as inverting the <i>output</i> bitmap, unless the thresholding value is also inverted.</p>
<dt><code>-f </code><i>n</i>, &#8211;filter <i>n</i></p>
<dd> Apply a highpass filter to the image. This filter is approximately Gaussian and non-directional. The effect is to preserve small detail while compensating for background gradients. The parameter <i>n</i> is a radius (in pixels) which corresponds approximately to the size of details which should be preserved. More precisely, the filter is implemented by subtracting a blurred version of the image from the original image. The parameter <i>n</i> is equal to the standard deviation of the blur. The output of the filtering step is a normalized image whose average brightness is exactly 0.5. The default filter radius is 4.</p>
<dt><code>-n, &#8211;nofilter</code></p>
<dd> Turn off highpass filtering.</p>
<dt><code>-b </code><i>n</i>, &#8211;blur <i>n</i></p>
<dd> Blur the image. The effect is to smooth out fine details and to reduce visual noise in the image. The parameter <i>n</i> is the blurring radius, and should be chosen small (1 is a good value to start with). This is implemented as an approximately Gaussian, non-directional blur with standard deviation proportional to <i>n</i>. Blurring is applied after the highpass filter, but before scaling and thresholding. If this option is not given, the default is not to apply any blurring.</p>
<dt><code>-s </code><i>n</i>, &#8211;scale <i>n</i></p>
<dd> Scale the image by an integer factor <i>n</i>&gt;0. Scaling is done after highpass filtering, but before the thresholding step. A scaling factor of 1 indicates that no scaling is to be done. Otherwise, interpolation is used to fill in the in-between pixels. If the output of <code>mkbitmap</code> is to be used as input to a tracing program such as <code>potrace</code>, a scaling factor of 2 is recommended. This preserved the right amount of detail for the tracing algorithm to work well. If a scaling factor of 1 is used, too much detail is lost. If a scaling factor of 3 or higher is used, the interpolation tends to &quot;invent&quot; detail which was not present in the original image, thus preventing <code>potrace</code> from doing a good job.</p>
<dt><code>-1, &#8211;linear</code></p>
<dd> Use linear interpolation when scaling to a higher resolution. This is slightly faster, but less nice, than the default cubic interpolation.</p>
<dt><code>-3, &#8211;cubic</code></p>
<dd> Use cubic interpolation when scaling to a higher resolution. This is the default. It is slower than linear interpolation, but leads to better results.</p>
<dt><code>-t </code><i>n</i>, &#8211;threshold <i>n</i></p>
<dd> Set the threshold grey value for bilevel conversion. The parameter <i>n</i> is a brightness value between 0 for black and 1 for white. Any pixels below this brightness will be converted to black (thus, smaller values of <i>n</i> will lead to whiter output).</p>
<dt><code>-g, &#8211;grey</code></p>
<dd> Disable bilevel conversion. If this option is given, processing stops after the scaling step and a greymap is output.</dl>
<h2>EXIT STATUS</h2>
<p> The exit status is 0 on successful completion, 1 if the command line was invalid, and 2 on any other error.</p>
<h2>VERSION</h2>
<p> 1.13</p>
<h2>AUTHOR</h2>
<p> Peter Selinger &lt;selinger at users.sourceforge.net&gt;</p>
<h2>WEB SITE AND SUPPORT</h2>
<p> <code>mkbitmap</code> is distributed as part of the <code>potrace</code> package, and the latest version is available from <a rel="nofollow" href="http://potrace.sourceforge.net/.">http://potrace.sourceforge.net/.</a> This site also contains documentation and information on how to obtain support.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-potrace/">potrace</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2001-2015 Peter Selinger </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA. See also <a rel="nofollow" href="http://www.gnu.org/.">http://www.gnu.org/.</a> </p>
<h2>Index</h2>
