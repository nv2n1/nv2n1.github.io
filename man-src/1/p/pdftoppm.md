---
title: "pdftoppm(1)"
name: "pdftoppm"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdftoppm/"
description: "pdftoppm – Portable Document Format (PDF) to Portable Pixmap (PPM) converter (version 3.03)"
---

<h2 class="name">NAME</h2>
<p> pdftoppm &#8211; Portable Document Format (PDF) to Portable Pixmap (PPM) converter (version 3.03) </p>
<h2>SYNOPSIS</h2>
<p> <code>pdftoppm</code> [options] <i>PDF-file PPM-root</i></p>
<h2>DESCRIPTION</h2>
<p> <code>Pdftoppm</code> converts Portable Document Format (PDF) files to color image files in Portable Pixmap (PPM) format, grayscale image files in Portable Graymap (PGM) format, or monochrome image files in Portable Bitmap (PBM) format. </p>
<p> Pdftoppm reads the PDF file, <i>PDF-file</i>, and writes one PPM file for each page, <i>PPM-root</i>&#8211;<i>number</i>.ppm, where <i>number</i> is the page number. If <i>PDF-file</i> is &#8216;-&#8216;, it reads the PDF file from stdin.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f</code><i> number</i></p>
<dd> Specifies the first page to convert.</p>
<dt><code>-l</code><i> number</i></p>
<dd> Specifies the last page to convert.</p>
<dt><code>-o</code></p>
<dd> Generates only the odd numbered pages.</p>
<dt><code>-e</code></p>
<dd> Generates only the even numbered pages.</p>
<dt><code>-singlefile</code></p>
<dd> Writes only the first page and does not add digits.</p>
<dt><code>-r</code><i> number</i></p>
<dd> Specifies the X and Y resolution, in DPI. The default is 150 DPI.</p>
<dt><code>-rx</code><i> number</i></p>
<dd> Specifies the X resolution, in DPI. The default is 150 DPI.</p>
<dt><code>-ry</code><i> number</i></p>
<dd> Specifies the Y resolution, in DPI. The default is 150 DPI.</p>
<dt><code>-scale-to</code><i> number</i></p>
<dd> Scales the long side of each page (width for landscape pages, height for portrait pages) to fit in scale-to pixels. The size of the short side will be determined by the aspect ratio of the page.</p>
<dt><code>-scale-to-x</code><i> number</i></p>
<dd> Scales each page horizontally to fit in scale-to-x pixels. If scale-to-y is set to -1, the vertical size will determined by the aspect ratio of the page.</p>
<dt><code>-scale-to-y</code><i> number</i></p>
<dd> Scales each page vertically to fit in scale-to-y pixels. If scale-to-x is set to -1, the horizontal size will determined by the aspect ratio of the page.</p>
<dt><code>-scale-dimension-before-rotation</code></p>
<dd> Swaps horizontal and vertical size for a rotated (landscape) pdf before scaling instead of after.</p>
<dt><code>-x</code><i> number</i></p>
<dd> Specifies the x-coordinate of the crop area top left corner</p>
<dt><code>-y</code><i> number</i></p>
<dd> Specifies the y-coordinate of the crop area top left corner</p>
<dt><code>-W</code><i> number</i></p>
<dd> Specifies the width of crop area in pixels (default is 0)</p>
<dt><code>-H</code><i> number</i></p>
<dd> Specifies the height of crop area in pixels (default is 0)</p>
<dt><code>-sz</code><i> number</i></p>
<dd> Specifies the size of crop square in pixels (sets W and H)</p>
<dt><code>-cropbox</code></p>
<dd> Uses the crop box rather than media box when generating the files</p>
<dt><code>-hide-annotations</code></p>
<dd> Do not show annotations</p>
<dt><code>-mono</code></p>
<dd> Generate a monochrome PBM file (instead of a color PPM file).</p>
<dt><code>-gray</code></p>
<dd> Generate a grayscale PGM file (instead of a color PPM file).</p>
<dt><code>-displayprofile</code><i> displayprofilefile</i></p>
<dd> If poppler is compiled with colour management support, this option sets the display profile to the ICC profile stored in displayprofilefile.</p>
<dt><code>-defaultgrayprofile</code><i> defaultgrayprofilefile</i></p>
<dd> If poppler is compiled with colour management support, this option sets the DefaultGray color space to the ICC profile stored in defaultgrayprofilefile.</p>
<dt><code>-defaultrgbprofile</code><i> defaultrgbprofilefile</i></p>
<dd> If poppler is compiled with colour management support, this option sets the DefaultRGB color space to the ICC profile stored in defaultrgbprofilefile.</p>
<dt><code>-defaultcmykprofile</code><i> defaultcmykprofilefile</i></p>
<dd> If poppler is compiled with colour management support, this option sets the DefaultCMYK color space to the ICC profile stored in defaultcmykprofilefile.</p>
<dt><code>-png</code></p>
<dd> Generates a PNG file instead a PPM file.</p>
<dt><code>-jpeg</code></p>
<dd> Generates a JPEG file instead a PPM file.</p>
<dt><code>-jpegopt</code><i> jpeg-options</i></p>
<dd> When used with -jpeg, takes a list of options to control the jpeg compression. See <code>JPEG OPTIONS</code> for the available options.</p>
<dt><code>-tiff</code></p>
<dd> Generates a TIFF file instead a PPM file.</p>
<dt><code>-tiffcompression</code><i> none | packbits | jpeg | lzw | deflate</i></p>
<dd> Specifies the TIFF compression type. This defaults to &quot;none&quot;.</p>
<dt><code>-freetype</code><i> yes | no</i></p>
<dd> Enable or disable FreeType (a TrueType / Type 1 font rasterizer). This defaults to &quot;yes&quot;.</p>
<dt><code>-thinlinemode</code><i> none | solid | shape</i></p>
<dd> Specifies the thin line mode. This defaults to &quot;none&quot;.</p>
<dt>&quot;solid&quot;:</p>
<dd> adjust lines with a width less than one pixel to pixel boundary and paint it with a width of one pixel.</p>
<dt>&quot;shape&quot;:</p>
<dd> adjust lines with a width less than one pixel to pixel boundary and paint it with a width of one pixel but with a shape in proportion to its width.</p>
<dt><code>-aa</code><i> yes | no</i></p>
<dd> Enable or disable font anti-aliasing. This defaults to &quot;yes&quot;.</p>
<dt><code>-aaVector</code><i> yes | no</i></p>
<dd> Enable or disable vector anti-aliasing. This defaults to &quot;yes&quot;.</p>
<dt><code>-opw</code><i> password</i></p>
<dd> Specify the owner password for the PDF file. Providing this will bypass all security restrictions.</p>
<dt><code>-upw</code><i> password</i></p>
<dd> Specify the user password for the PDF file.</p>
<dt><code>-q</code></p>
<dd> Don&#8217;t print any messages or errors.</p>
<dt><code>-progress</code></p>
<dd> Print progress info as each page is generated. Three space-separated fields are printed to STDERR: the number of the current page, the number of the last page that will be generated, and the path to the file written to.</p>
<dt><code>-sep</code><i> char</i></p>
<dd> Specify single character separator between name and page number, default &#8211; .</p>
<dt><code>-forcenum</code></p>
<dd> Force page number even if there is only one page.</p>
<dt><code>-v</code></p>
<dd> Print copyright and version information.</p>
<dt><code>-h</code></p>
<dd> Print usage information. (<code>-help</code> and <code>&#8211;help</code> are equivalent.)</dl>
<h2>EXIT CODES</h2>
<p> The Xpdf tools use the following exit codes:</p>
<dl>
<dt>0</p>
<dd> No error.</p>
<dt>1</p>
<dd> Error opening a PDF file.</p>
<dt>2</p>
<dd> Error opening an output file.</p>
<dt>3</p>
<dd> Error related to PDF permissions.</p>
<dt>99</p>
<dd> Other error.</dl>
<h2>JPEG OPTIONS</h2>
<p> When JPEG output is specified, the -jpegopt option can be used to control the JPEG compression parameters. It takes a string of the form &quot;&lt;opt&gt;=&lt;val&gt;[,&lt;opt&gt;=&lt;val&gt;]&quot;. Currently the available options are:</p>
<dl>
<dt><code>quality</code></p>
<dd> Selects the JPEG quality value. The value must be an integer between 0 and 100.</p>
<dt><code>progressive</code></p>
<dd> Select progressive JPEG output. The possible values are &quot;y&quot;, &quot;n&quot;, indicating progressive (yes) or non-progressive (no), respectively.</p>
<dt><code>optimize</code></p>
<dd> Sets whether to compute optimal Huffman coding tables for the JPEG output, which will create smaller files but make an extra pass over the data. The value must be &quot;y&quot; or &quot;n&quot;, with &quot;y&quot; performing optimization, otherwise the default Huffman tables are used.</dl>
<h2>AUTHOR</h2>
<p> The pdftoppm software and documentation are copyright 1996-2011 Glyph &amp; Cog, LLC.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pdfdetach/">pdfdetach</a></code>(1), <code><a href="/docs/linux/man/1-pdffonts/">pdffonts</a></code>(1), <code><a href="/docs/linux/man/1-pdfimages/">pdfimages</a></code>(1), <code><a href="/docs/linux/man/1-pdfinfo/">pdfinfo</a></code>(1), <code><a href="/docs/linux/man/1-pdftocairo/">pdftocairo</a></code>(1), <code><a href="/docs/linux/man/1-pdftohtml/">pdftohtml</a></code>(1), <code><a href="/docs/linux/man/1-pdftops/">pdftops</a></code>(1), <code><a href="/docs/linux/man/1-pdftotext/">pdftotext</a></code>(1) <code><a href="/docs/linux/man/1-pdfseparate/">pdfseparate</a></code>(1), <code><a href="/docs/linux/man/1-pdfsig/">pdfsig</a></code>(1), <code><a href="/docs/linux/man/1-pdfunite/">pdfunite</a></code>(1) </p>
<h2>Index</h2>
