---
title: "pdftocairo(1)"
name: "pdftocairo"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdftocairo/"
description: "pdftocairo – Portable Document Format (PDF) to PNG/JPEG/TIFF/PDF/PS/EPS/SVG using cairo"
---

<h2 class="name">NAME</h2>
<p> pdftocairo &#8211; Portable Document Format (PDF) to PNG/JPEG/TIFF/PDF/PS/EPS/SVG using cairo </p>
<h2>SYNOPSIS</h2>
<p> <code>pdftocairo</code> [options] <i>PDF-file</i> [<i>output-file</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>pdftocairo</code> converts Portable Document Format (PDF) files, using the cairo output device of the poppler PDF library, to any of the following output formats:</p>
<dl>
<dt>&bull;</dt>
<dd> Portable Network Graphics (PNG)</dd>
<dt>&bull;</dt>
<dd> JPEG Interchange Format (JPEG)</dd>
<dt>&bull;</dt>
<dd> Tagged Image File Format (TIFF)</dd>
<dt>&bull;</dt>
<dd> Portable Document Format (PDF)</dd>
<dt>&bull;</dt>
<dd> PostScript (PS)</dd>
<dt>&bull;</dt>
<dd> Encapsulated PostScript (EPS)</dd>
<dt>&bull;</dt>
<dd> Scalable Vector Graphics (SVG)</dd>
<dt>&bull;</dt>
<dd> Windows Printer</dd></dl>
<p> <code>pdftocairo</code> reads the PDF file, <i>PDF-file</i>, and writes to <i>output-file</i>. The image formats (PNG, JPEG, and TIFF) generate one file per page with the page number and file type appended to <i>output-file</i>. When -singlefile is used with the image formats, the file type is appended to <i>output-file</i>. When the output format is a vector format (PDF, PS, EPS, and SVG), <i>output-file</i> is the full filename. </p>
<p> If the <i>PDF-file</i> is &#8220;-&#8221; , the PDF is read from stdin. If the <i>output-file</i> is &#8220;-&#8221; , the output file will be written to stdout. Using stdout is not valid with image formats unless -singlefile is used. If <i>output-file</i> is not used, the output filename will be derived from the <i>PDF-file</i> filename. </p>
<p> Not all options are valid with all output formats. One (and only one) of the output format options (-png, -jpeg, -tiff, -pdf, -print, -ps, -eps, or -svg) must be used. </p>
<p> The resolution options (-r, -rx, -ry) set the resolution of the image output formats. The image dimensions will depend on the PDF page size and the resolution. For the vector outputs, regions of the page that can not be represented natively in the output format (eg translucency in PS) will be rasterized at the resolution specified by the resolution options. </p>
<p> The -scale-to options may be used to set a fixed image size. The image resolution will vary with the page size. </p>
<p> The cropping options (-x, -y, -W, and -H) use units of pixels with the image formats and PostScript points (1/72 inch) with the vector formats. When cropping is used with vector output the cropped region is centered unless -nocenter is used in which case the cropped region is at the top left (SVG) or bottom left (PDF, PS, EPS). </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-png</code></dt>
<dd> Generates a PNG file(s)</dd>
<dt><code>-jpeg</code></dt>
<dd> Generates a JPEG file(s). See also -jpegopt.</dd>
<dt><code>-tiff</code></dt>
<dd> Generates a TIFF file(s)</dd>
<dt><code>-pdf</code></dt>
<dd> Generates a PDF file</dd>
<dt><code>-ps</code></dt>
<dd> Generate a PS file</dd>
<dt><code>-eps</code></dt>
<dd> Generate an EPS file. An EPS file contains a single image, so if you use this option with a multi-page PDF file, you must use -f and -l to specify a single page. The page size options (-origpagesizes, -paper, -paperw, -paperh) can not be used with this option.</dd>
<dt><code>-svg</code></dt>
<dd> Generate a SVG (Scalable Vector Graphics) file</dd>
<dt><code>-print</code></dt>
<dd> (Windows only) Prints to a system printer. See also -printer and -printeropt.<br />
&nbsp;If an output file is not specified, the output will be sent to the printer.<br />
&nbsp;The output file&nbsp;&#8216;-&#8216;&nbsp;can not be used with this option.</dd>
<dt><code>-printdlg</code></dt>
<dd> (Windows only) Prints to a system printer. Displays the print dialog to allow the print options to be modified before printing.</dd>
<dt><code>-f</code><i> number</i></dt>
<dd> Specifies the first page to convert.</dd>
<dt><code>-l</code><i> number</i></dt>
<dd> Specifies the last page to convert.</dd>
<dt><code>-o</code></dt>
<dd> Generates only the odd numbered pages.</dd>
<dt><code>-e</code></dt>
<dd> Generates only the even numbered pages.</dd>
<dt><code>-singlefile</code></dt>
<dd> Writes only the first page and does not add digits.</dd>
<dt><code>-r</code><i> number</i></dt>
<dd> Specifies the X and Y resolution, in pixels per inch of image files (or rasterized regions in vector output). The default is 150 PPI.</dd>
<dt><code>-rx</code><i> number</i></dt>
<dd> Specifies the X resolution, in pixels per inch of image files (or rasterized regions in vector output). The default is 150 PPI.</dd>
<dt><code>-ry</code><i> number</i></dt>
<dd> Specifies the Y resolution, in pixels per inch of image files (or rasterized regions in vector output). The default is 150 PPI.</dd>
<dt><code>-scale-to</code><i> number</i></dt>
<dd> Scales the long side of each page (width for landscape pages, height for portrait pages) to fit in scale-to pixels. The size of the short side will be determined by the aspect ratio of the page (PNG/JPEG/TIFF only).</dd>
<dt><code>-scale-to-x</code><i> number</i></dt>
<dd> Scales each page horizontally to fit in scale-to-x pixels. If scale-to-y is set to -1, the vertical size will determined by the aspect ratio of the page (PNG/JPEG/TIFF only).</dd>
<dt><code>-scale-to-y</code><i> number</i></dt>
<dd> Scales each page vertically to fit in scale-to-y pixels. If scale-to-x is set to -1, the horizontal size will determined by the aspect ratio of the page (PNG/JPEG/TIFF only).</dd>
<dt><code>-x</code><i> number</i></dt>
<dd> Specifies the x-coordinate of the crop area top left corner in pixels (image output) or points (vector output)</dd>
<dt><code>-y</code><i> number</i></dt>
<dd> Specifies the y-coordinate of the crop area top left corner in pixels (image output) or points (vector output)</dd>
<dt><code>-W</code><i> number</i></dt>
<dd> Specifies the width of crop area in pixels (image output) or points (vector output) (default is 0)</dd>
<dt><code>-H</code><i> number</i></dt>
<dd> Specifies the height of crop area in pixels (image output) or points (vector output) (default is 0)</dd>
<dt><code>-sz</code><i> number</i></dt>
<dd> Specifies the size of crop square in pixels (image output) or points (vector output) (sets -W and -H)</dd>
<dt><code>-cropbox</code></dt>
<dd> Uses the crop box rather than media box when generating the files (PNG/JPEG/TIFF only)</dd>
<dt><code>-mono</code></dt>
<dd> Generate a monochrome file (PNG and TIFF only).</dd>
<dt><code>-gray</code></dt>
<dd> Generate a grayscale file (PNG, JPEG, and TIFF only).</dd>
<dt><code>-antialias</code></dt>
<dd> Set the cairo antialias option used for text and drawing in image files (or rasterized regions in vector output). The options are:</dd>
<dl>
<dl>
<dt><code>default</code></dt>
<dd> Use the default antialiasing for the target device. This is the default setting if -antialias is not used.</dd>
<dt><code>none</code></dt>
<dd> Antialiasing is disabled.</dd>
<dt><code>gray</code></dt>
<dd> Perform single-color antialiasing using shades of gray.</dd>
<dt><code>subpixel</code></dt>
<dd> Perform antialiasing by taking advantage of the order of subpixel elements on devices such as LCD.</dd>
<dt><code>fast</code></dt>
<dd> Hint that the backend should perform some antialiasing but prefer speed over quality.</dd>
<dt><code>good</code></dt>
<dd> The backend should balance quality against performance.</dd>
<dt><code>best</code></dt>
<dd> Hint that the backend should render at the highest quality, sacrificing speed if necessary.</dd></dl>
</dl>
<dt><code>-transp</code></dt>
<dd> Use a transparent page color instead of white (PNG and TIFF only).</dd>
<dt><code>-icc</code><i> icc-file</i></dt>
<dd> Use the specified ICC file as the output profile (PNG only). The profile will be embedded in the PNG file.</dd>
<dt><code>-jpegopt</code><i> jpeg-options</i></dt>
<dd> When used with -jpeg, takes a list of options to control the jpeg compression. See <code>JPEG OPTIONS</code> for the available options.</dd>
<dt><code>-level2</code></dt>
<dd> Generate Level 2 PostScript (PS only).</dd>
<dt><code>-level3</code></dt>
<dd> Generate Level 3 PostScript (PS only). This enables all Level 2 features plus shading patterns and masked images. This is the default setting.</dd>
<dt><code>-origpagesizes</code></dt>
<dd> This option is the same as &quot;-paper match&quot;.</dd>
<dt><code>-paper</code><i> size</i></dt>
<dd> Set the paper size to one of &quot;letter&quot;, &quot;legal&quot;, &quot;A4&quot;, or &quot;A3&quot; (PS,PDF,SVG only). This can also be set to &quot;match&quot;, which will set the paper size of each page to match the size specified in the PDF file. If none the -paper, -paperw, or -paperh options are specified the default is to match the paper size.</dd>
<dt><code>-paperw</code><i> size</i></dt>
<dd> Set the paper width, in points (PS,PDF,SVG only).</dd>
<dt><code>-paperh</code><i> size</i></dt>
<dd> Set the paper height, in points (PS,PDF,SVG only).</dd>
<dt><code>-nocrop</code></dt>
<dd> By default, printing output is cropped to the CropBox specified in the PDF file. This option disables cropping (PS,PDF,SVG only).</dd>
<dt><code>-expand</code></dt>
<dd> Expand PDF pages smaller than the paper to fill the paper (PS,PDF,SVG only). By default, these pages are not scaled.</dd>
<dt><code>-noshrink</code></dt>
<dd> Don&#8217;t scale PDF pages which are larger than the paper (PS,PDF,SVG only). By default, pages larger than the paper are shrunk to fit.</dd>
<dt><code>-nocenter</code></dt>
<dd> By default, PDF pages smaller than the paper (after any scaling) are centered on the paper. This option causes them to be aligned to the lower-left corner of the paper instead (PS,PDF,SVG only).</dd>
<dt><code>-duplex</code></dt>
<dd> Adds the %%IncludeFeature: *Duplex DuplexNoTumble DSC comment to the PostScript file (PS only). This tells the print manager to enable duplexing.</dd>
<dt><code>-printer</code><i> printer-name</i></dt>
<dd> (Windows only). When used with -print, specifies the name of the printer to be used, instead of the system default.</dd>
<dt><code>-printopt</code><i> printer-options</i></dt>
<dd> (Windows only). When used with -print, takes a list of options to be used to configure the printer. See <code>WINDOWS PRINTER OPTIONS</code> for the available options.</dd>
<dt><code>-setupdlg</code></dt>
<dd> (Windows only). When used with -print, the printer properties dialog is displayed allowing the print settings to be modified before printing. The paper size selected in the print properties dialog will be used except when -origpagesizes is specified.</dd>
<dt><code>-opw</code><i> password</i></dt>
<dd> Specify the owner password for the PDF file. Providing this will bypass all security restrictions.</dd>
<dt><code>-upw</code><i> password</i></dt>
<dd> Specify the user password for the PDF file.</dd>
<dt><code>-q</code></dt>
<dd> Don&#8217;t print any messages or errors.</dd>
<dt><code>-v</code></dt>
<dd> Print copyright and version information.</dd>
<dt><code>-h</code></dt>
<dd> Print usage information. (<code>-help</code> and <code>&#8211;help</code> are equivalent.)</dd></dl>
<h2>EXIT CODES</h2>
<p> The poppler tools use the following exit codes:</p>
<dl>
<dt>0</dt>
<dd> No error.</dd>
<dt>1</dt>
<dd> Error opening a PDF file.</dd>
<dt>2</dt>
<dd> Error opening an output file.</dd>
<dt>3</dt>
<dd> Error related to PDF permissions.</dd>
<dt>4</dt>
<dd> Error related to ICC profile.</dd>
<dt>99</dt>
<dd> Other error.</dd></dl>
<h2>JPEG OPTIONS</h2>
<p> When JPEG output is specified, the -jpegopt option can be used to control the JPEG compression parameters. It takes a string of the form &quot;&lt;opt&gt;=&lt;val&gt;[,&lt;opt&gt;=&lt;val&gt;]&quot;. Currently the available options are:</p>
<dl>
<dt><code>quality</code></dt>
<dd> Selects the JPEG quality value. The value must be an integer between 0 and 100.</dd>
<dt><code>progressive</code></dt>
<dd> Select progressive JPEG output. The possible values are &quot;y&quot;, &quot;n&quot;, indicating progressive (yes) or non-progressive (no), respectively.</dd>
<dt><code>optimize</code></dt>
<dd> Sets whether to compute optimal Huffman coding tables for the JPEG output, which will create smaller files but make an extra pass over the data. The value must be &quot;y&quot; or &quot;n&quot;, with &quot;y&quot; performing optimization, otherwise the default Huffman tables are used.</dd></dl>
<h2>WINDOWS PRINTER OPTIONS</h2>
<p> In Windows, you can use the -print option to print directly to a system printer. Additionally, you can use the -printopt option to configure the printer. It takes a string of the form &quot;&lt;opt&gt;=&lt;val&gt;[,&lt;opt&gt;=&lt;val&gt;]&quot;. Currently the available options are:</p>
<dl>
<dt><code>source</code></dt>
<dd> Selects the source paper tray to be used (bin). The possible values are &quot;upper&quot;, &quot;onlyone&quot;, &quot;lower&quot;, &quot;middle&quot;, &quot;manual&quot;, &quot;envelope&quot;, &quot;envmanual&quot;, &quot;auto&quot;, &quot;tractor&quot;, &quot;smallfmt&quot;, &quot;largefmt&quot;, &quot;largecapacity&quot;, &quot;formsource&quot;, or a numeric value to choose a driver specific source.</dd>
<dt><code>duplex</code></dt>
<dd> Sets the duplex mode of the printer. The possible values are &quot;off&quot;, &quot;short&quot; or &quot;long&quot;, indicating no duplexing, short-edge binding, or long-edge binding, respectively. General option -duplex is a synonym of &quot;duplex=long&quot;. If both options are specified, -printopt has priority.</dd></dl>
<h2>AUTHOR</h2>
<p> The pdftocairo software and documentation are copyright 1996-2004 Glyph &amp; Cog, LLC and copyright 2005-2011 The Poppler Developers.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pdfdetach/">pdfdetach</a></code>(1), <code><a href="/docs/linux/man/1-pdffonts/">pdffonts</a></code>(1), <code><a href="/docs/linux/man/1-pdfimages/">pdfimages</a></code>(1), <code><a href="/docs/linux/man/1-pdfinfo/">pdfinfo</a></code>(1), <code><a href="/docs/linux/man/1-pdftohtml/">pdftohtml</a></code>(1), <code><a href="/docs/linux/man/1-pdftoppm/">pdftoppm</a></code>(1), <code><a href="/docs/linux/man/1-pdftops/">pdftops</a></code>(1), <code><a href="/docs/linux/man/1-pdftotext/">pdftotext</a></code>(1) <code><a href="/docs/linux/man/1-pdfseparate/">pdfseparate</a></code>(1), <code><a href="/docs/linux/man/1-pdfsig/">pdfsig</a></code>(1), <code><a href="/docs/linux/man/1-pdfunite/">pdfunite</a></code>(1) </p>
