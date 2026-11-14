---
title: "pdftops(1)"
name: "pdftops"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdftops/"
description: "pdftops – Portable Document Format (PDF) to PostScript converter (version 3.03)"
---

<h2 class="name">NAME</h2>
<p> pdftops &#8211; Portable Document Format (PDF) to PostScript converter (version 3.03) </p>
<h2>SYNOPSIS</h2>
<p> <code>pdftops</code> [options] &lt;PDF-file&gt; [&lt;PS-file&gt;]</p>
<h2>DESCRIPTION</h2>
<p> <code>Pdftops</code> converts Portable Document Format (PDF) files to PostScript so they can be printed. </p>
<p> Pdftops reads the PDF file, <i>PDF-file</i>, and writes a PostScript file, <i>PS-file</i>. If <i>PS-file</i> is not specified, pdftops converts <i>file.pdf</i> to <i>file.ps</i> (or <i>file.eps</i> with the -eps option). If <i>PS-file</i> is &#8216;-&#8216;, the PostScript is sent to stdout. If <i>PDF-file</i> is &#8216;-&#8216;, Pdftops reads the PDF file from stdin.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f</code><i> number</i></p>
<dd> Specifies the first page to print.</p>
<dt><code>-l</code><i> number</i></p>
<dd> Specifies the last page to print.</p>
<dt><code>-level1</code></p>
<dd> Generate Level 1 PostScript. The resulting PostScript files will be significantly larger (if they contain images), but will print on Level 1 printers. This also converts all images to black and white. No more than one of the PostScript level options (-level1, -level1sep, -level2, -level2sep, -level3, -level3sep) may be given.</p>
<dt><code>-level1sep</code></p>
<dd> Generate Level 1 separable PostScript. All colors are converted to CMYK. Images are written with separate stream data for the four components.</p>
<dt><code>-level2</code></p>
<dd> Generate Level 2 PostScript. Level 2 supports color images and image compression. This is the default setting.</p>
<dt><code>-level2sep</code></p>
<dd> Generate Level 2 separable PostScript. All colors are converted to CMYK. The PostScript separation convention operators are used to handle custom (spot) colors.</p>
<dt><code>-level3</code></p>
<dd> Generate Level 3 PostScript. This enables all Level 2 features plus CID font embedding.</p>
<dt><code>-level3sep</code></p>
<dd> Generate Level 3 separable PostScript. The separation handling is the same as for -level2sep.</p>
<dt><code>-eps</code></p>
<dd> Generate an Encapsulated PostScript (EPS) file. An EPS file contains a single image, so if you use this option with a multi-page PDF file, you must use -f and -l to specify a single page. No more than one of the mode options (-eps, -form) may be given.</p>
<dt><code>-form</code></p>
<dd> Generate a PostScript form which can be imported by software that understands forms. A form contains a single page, so if you use this option with a multi-page PDF file, you must use -f and -l to specify a single page. The -level1 option cannot be used with -form. No more than one of the mode options (-eps, -form) may be given.</p>
<dt><code>-opi</code></p>
<dd> Generate OPI comments for all images and forms which have OPI information. (This option is only available if pdftops was compiled with OPI support.)</p>
<dt><code>-binary</code></p>
<dd> Write binary data in Level 1 PostScript. By default, pdftops writes hex-encoded data in Level 1 PostScript. Binary data is non-standard in Level 1 PostScript but reduces the file size and can be useful when Level 1 PostScript is required only for its restricted use of PostScript operators.</p>
<dt><code>-r</code><i> number</i></p>
<dd> Set the resolution in DPI when pdftops rasterizes images with transparencies or, for Level 1 PostScript, when pdftops rasterizes images with color masks. By default, pdftops rasterizes images to 300 DPI.</p>
<dt><code>-noembt1</code></p>
<dd> By default, any Type 1 fonts which are embedded in the PDF file are copied into the PostScript file. This option causes pdftops to substitute base fonts instead. Embedded fonts make PostScript files larger, but may be necessary for readable output.</p>
<dt><code>-noembtt</code></p>
<dd> By default, any TrueType fonts which are embedded in the PDF file are copied into the PostScript file. This option causes pdftops to substitute base fonts instead. Embedded fonts make PostScript files larger, but may be necessary for readable output. Also, some PostScript interpreters do not have TrueType rasterizers.</p>
<dt><code>-noembcidps</code></p>
<dd> By default, any CID PostScript fonts which are embedded in the PDF file are copied into the PostScript file. This option disables that embedding. No attempt is made to substitute for non-embedded CID PostScript fonts.</p>
<dt><code>-noembcidtt</code></p>
<dd> By default, any CID TrueType fonts which are embedded in the PDF file are copied into the PostScript file. This option disables that embedding. No attempt is made to substitute for non-embedded CID TrueType fonts.</p>
<dt><code>-passfonts</code></p>
<dd> By default, references to non-embedded 8-bit fonts in the PDF file are substituted with the closest &quot;Helvetica&quot;, &quot;Times-Roman&quot;, or &quot;Courier&quot; font. This option passes references to non-embedded fonts through to the PostScript file.</p>
<dt><code>-aaRaster</code><i> yes | no</i></p>
<dd> Enable or disable raster anti-aliasing. This defaults to &quot;no&quot;. pdftops may need to rasterize transparencies and pattern image masks in the PDF. If the PostScript will be printed, leave -aaRaster disabled and set -r to the resolution of the printer. If the PostScript will be viewed, enabling -aaRaster may make rasterized text easier to read.</p>
<dt><code>-rasterize</code><i> always | never | whenneeded</i></p>
<dd> By default, pdftops rasterizes pages as needed, for example, if they contain transparencies. To force rasterization, set -rasterize to &quot;always&quot;. Use this to eliminate fonts. To prevent rasterization, set -rasterize to &quot;never&quot;. This may produce files that display incorrectly.</p>
<dt><code>-processcolorformat</code><i> MONO8 | CMYK8 | RGB8</i></p>
<dd> Sets the process color format as it is used during rasterization and transparency reduction. The default depends on the other settings: For -level1 the default is MONO8, for -level{1,2,3}sep or -overprint the default is CMYK8, and in all other cases RGB8 is the default. If -processcolorprofile is given then -processcolorformat is inferred from the specified ICC profile.</p>
<dt><code>-processcolorprofile</code><i> filename</i></p>
<dd> Sets the ICC profile that is assumed during rasterization and transparency reduction.</p>
<dt><code>-defaultgrayprofile</code><i> defaultgrayprofilefile</i></p>
<dd> If poppler is compiled with colour management support, this option sets the DefaultGray color space to the ICC profile stored in defaultgrayprofilefile.</p>
<dt><code>-defaultrgbprofile</code><i> defaultrgbprofilefile</i></p>
<dd> If poppler is compiled with colour management support, this option sets the DefaultRGB color space to the ICC profile stored in defaultrgbprofilefile.</p>
<dt><code>-defaultcmykprofile</code><i> defaultcmykprofilefile</i></p>
<dd> If poppler is compiled with colour management support, this option sets the DefaultCMYK color space to the ICC profile stored in defaultcmykprofilefile.</p>
<dt><code>-optimizecolorspace</code></p>
<dd> By default, bitmap images in the PDF pass through to the output PostScript in their original color space, which produces predictable results. This option converts RGB and CMYK images into Gray images if every pixel of the image has equal components. This can fix problems when doing color separations of PDFs that contain embedded black and white images encoded as RGB.</p>
<dt><code>-preload</code></p>
<dd> preload images and forms</p>
<dt><code>-paper</code><i> size</i></p>
<dd> Set the paper size to one of &quot;letter&quot;, &quot;legal&quot;, &quot;A4&quot;, or &quot;A3&quot;. This can also be set to &quot;match&quot;, which will set the paper size of each page to match the size specified in the PDF file. If none the -paper, -paperw, or -paperh options are specified the default is to match the paper size.</p>
<dt><code>-paperw</code><i> size</i></p>
<dd> Set the paper width, in points.</p>
<dt><code>-paperh</code><i> size</i></p>
<dd> Set the paper height, in points.</p>
<dt><code>-origpagesizes</code></p>
<dd> This option is the same as &quot;-paper match&quot;.</p>
<dt><code>-nocrop</code></p>
<dd> By default, output is cropped to the CropBox specified in the PDF file. This option disables cropping.</p>
<dt><code>-expand</code></p>
<dd> Expand PDF pages smaller than the paper to fill the paper. By default, these pages are not scaled.</p>
<dt><code>-noshrink</code></p>
<dd> Don&#8217;t scale PDF pages which are larger than the paper. By default, pages larger than the paper are shrunk to fit.</p>
<dt><code>-nocenter</code></p>
<dd> By default, PDF pages smaller than the paper (after any scaling) are centered on the paper. This option causes them to be aligned to the lower-left corner of the paper instead.</p>
<dt><code>-duplex</code></p>
<dd> Set the Duplex pagedevice entry in the PostScript file. This tells duplex-capable printers to enable duplexing.</p>
<dt><code>-opw</code><i> password</i></p>
<dd> Specify the owner password for the PDF file. Providing this will bypass all security restrictions.</p>
<dt><code>-upw</code><i> password</i></p>
<dd> Specify the user password for the PDF file.</p>
<dt><code>-overprint</code></p>
<dd> Enable overprint emulation during rasterization. For -processcolorformat being CMYK8 and the language level being higher than 2, this option is set to true by default. Note: This option requires -processcolorformat to be CMYK8.</p>
<dt><code>-q</code></p>
<dd> Don&#8217;t print any messages or errors.</p>
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
<h2>AUTHOR</h2>
<p> The pdftops software and documentation are copyright 1996-2011 Glyph &amp; Cog, LLC.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pdfdetach/">pdfdetach</a></code>(1), <code><a href="/docs/linux/man/1-pdffonts/">pdffonts</a></code>(1), <code><a href="/docs/linux/man/1-pdfimages/">pdfimages</a></code>(1), <code><a href="/docs/linux/man/1-pdfinfo/">pdfinfo</a></code>(1), <code><a href="/docs/linux/man/1-pdftocairo/">pdftocairo</a></code>(1), <code><a href="/docs/linux/man/1-pdftohtml/">pdftohtml</a></code>(1), <code><a href="/docs/linux/man/1-pdftoppm/">pdftoppm</a></code>(1), <code><a href="/docs/linux/man/1-pdftotext/">pdftotext</a></code>(1) <code><a href="/docs/linux/man/1-pdfseparate/">pdfseparate</a></code>(1), <code><a href="/docs/linux/man/1-pdfsig/">pdfsig</a></code>(1), <code><a href="/docs/linux/man/1-pdfunite/">pdfunite</a></code>(1) </p>
<h2>Index</h2>
