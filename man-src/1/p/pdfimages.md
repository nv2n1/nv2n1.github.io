---
title: "pdfimages(1)"
name: "pdfimages"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdfimages/"
description: "pdfimages – Portable Document Format (PDF) image extractor (version 3.03)"
---

<h2 class="name">NAME</h2>
<p> pdfimages &#8211; Portable Document Format (PDF) image extractor (version 3.03) </p>
<h2>SYNOPSIS</h2>
<p> <code>pdfimages</code> [options] <i>PDF-file image-root</i></p>
<h2>DESCRIPTION</h2>
<p> <code>Pdfimages</code> saves images from a Portable Document Format (PDF) file as Portable Pixmap (PPM), Portable Bitmap (PBM), Portable Network Graphics (PNG), Tagged Image File Format (TIFF), JPEG, JPEG2000, or JBIG2 files. </p>
<p> Pdfimages reads the PDF file <i>PDF-file</i>, scans one or more pages, and writes one file for each image, <i>image-root</i>&#8211;<i>nnn</i>.<i>xxx</i>, where <i>nnn</i> is the image number and <i>xxx</i> is the image type (.ppm, .pbm, .png, .tif, .jpg, jp2, jb2e, or jb2g). If <i>PDF-file</i> is &#8216;-&#8216;, it reads the PDF file from stdin. </p>
<p> The default output format is PBM (for monochrome images) or PPM for non-monochrome. The -png or -tiff options change to default output to PNG or TIFF respectively. If both -png and -tiff are specified, CMYK images will be written as TIFF and all other images will be written as PNG. In addition the -j, -jp2, and -jbig2 options will cause JPEG, JPEG2000, and JBIG2, respectively, images in the PDF file to be written in their native format.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f</code><i> number</i></p>
<dd> Specifies the first page to scan.</p>
<dt><code>-l</code><i> number</i></p>
<dd> Specifies the last page to scan.</p>
<dt><code>-png</code></p>
<dd> Change the default output format to PNG.</p>
<dt><code>-tiff</code></p>
<dd> Change the default output format to TIFF.</p>
<dt><code>-j</code></p>
<dd> Write images in JPEG format as JPEG files instead of the default format. The JPEG file is identical to the JPEG data stored in the PDF.</p>
<dt><code>-jp2</code></p>
<dd> Write images in JPEG2000 format as JP2 files instead of the default format. The JP2 file is identical to the JPEG2000 data stored in the PDF.</p>
<dt><code>-jbig2</code></p>
<dd> Write images in JBIG2 format as JBIG2 files instead of the default format. JBIG2 data in PDF is of the embedded type. The embedded type of JBIG2 has an optional separate file containing global data. The embedded data is written with the extension .jb2e and the global data (if available) will be written to the same image number with the extension .jb2g. The content of both these files is identical to the JBIG2 data in the PDF.</p>
<dt><code>-ccitt</code></p>
<dd> Write images in CCITT format as CCITT files instead of the default format. The CCITT file is identical to the CCITT data stored in the PDF. PDF files contain additional parameters specifying how to decode the CCITT data. These parameters are translated to fax2tiff input options and written to a .params file with the same image number. The parameters are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-1</code></p>
<dd> 1D Group 3 encoding</p>
<dt><code>-2</code></p>
<dd> 2D Group 3 encoding</p>
<dt><code>-4</code></p>
<dd> Group 4 encoding</p>
<dt><code>-A</code></p>
<dd> Beginning of line is aligned on a byte boundary</p>
<dt><code>-P</code></p>
<dd> Beginning of line is not aligned on a byte boundary</p>
<dt><code>-X n</code></p>
<dd> The image width in pixels</p>
<dt><code>-W</code></p>
<dd> Encoding uses 1 for black and 0 for white</p>
<dt><code>-B</code></p>
<dd> Encoding uses 0 for black and 1 for white</p>
<dt><code>-M</code></p>
<dd> Input data fills from most significant bit to least significant bit.</dl>
</dl>
<dt><code>-all</code></p>
<dd> Write JPEG, JPEG2000, JBIG2, and CCITT images in their native format. CMYK files are written as TIFF files. All other images are written as PNG files. This is equivalent to specifying the options -png -tiff -j -jp2 -jbig2 -ccitt.</p>
<dt><code>-list</code></p>
<dd> Instead of writing the images, list the images along with various information for each image. Do not specify an <i>image-root</i> with this option.</p>
<dt>
<dd> The following information is listed for each image:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>page</code></p>
<dd> the page number containing the image</p>
<dt><code>num</code></p>
<dd> the image number</p>
<dt><code>type</code></p>
<dd> the image type:</dl>
<dl>
<dt>
<dd> image &#8211; an opaque image</dl>
<dl>
<dt>
<dd> mask &#8211; a monochrome mask image</dl>
<dl>
<dt>
<dd> smask &#8211; a soft-mask image</dl>
<dl>
<dt>
<dd> stencil &#8211; a monochrome mask image used for painting a color or pattern</dl>
<p> Note: Tranparency in images is represented in PDF using a separate image for the image and the mask/smask. The mask/smask used as part of a transparent image always immediately follows the image in the image list.</p>
<dl>
<dt><code>width</code></p>
<dd> image width (in pixels)</p>
<dt><code>height</code></p>
<dd> image height (in pixels)</dl>
<p> Note: the image width/height is the size of the embedded image, not the size the image will be rendered at.</p>
<dl>
<dt><code>color</code></p>
<dd> image color space:</dl>
<dl>
<dt>
<dd> gray &#8211; Gray</dl>
<dl>
<dt>
<dd> rgb &#8211; RGB</dl>
<dl>
<dt>
<dd> cmyk &#8211; CMYK</dl>
<dl>
<dt>
<dd> lab &#8211; L*a*b</dl>
<dl>
<dt>
<dd> icc &#8211; ICC Based</dl>
<dl>
<dt>
<dd> index &#8211; Indexed Color</dl>
<dl>
<dt>
<dd> sep &#8211; Separation</dl>
<dl>
<dt>
<dd> devn &#8211; DeviceN</dl>
<dl>
<dt><code>comp</code></p>
<dd> number of color components</p>
<dt><code>bpc</code></p>
<dd> bits per component</p>
<dt><code>enc</code></p>
<dd> encoding:</dl>
<dl>
<dt>
<dd> image &#8211; raster image (may be Flate or LZW compressed but does not use an image encoding)</dl>
<dl>
<dt>
<dd> jpeg &#8211; Joint Photographic Experts Group</dl>
<dl>
<dt>
<dd> jp2 &#8211; JPEG2000</dl>
<dl>
<dt>
<dd> jbig2 &#8211; Joint Bi-Level Image Experts Group</dl>
<dl>
<dt>
<dd> ccitt &#8211; CCITT Group 3 or Group 4 Fax</dl>
<dl>
<dt><code>interp</code></p>
<dd> &quot;yes&quot; if the interpolation is to be performed when scaling up the image</p>
<dt><code>object ID</code></p>
<dd> the image dictionary object ID (number and generation)</p>
<dt><code>x-ppi</code></p>
<dd> The horizontal resolution of the image (in pixels per inch) when rendered on the pdf page.</p>
<dt><code>y-ppi</code></p>
<dd> The vertical resolution of the image (in pixels per inch) when rendered on the pdf page.</p>
<dt><code>size</code></p>
<dd> The size of the embedded image in the pdf file. The following suffixes are used: &#8216;B&#8217; bytes, &#8216;K&#8217; kilobytes, &#8216;M&#8217; megabytes, and &#8216;G&#8217; gigabytes.</p>
<dt><code>ratio</code></p>
<dd> The compression ratio of the embedded image.</dl>
</dl>
<dt><code>-opw</code><i> password</i></p>
<dd> Specify the owner password for the PDF file. Providing this will bypass all security restrictions.</p>
<dt><code>-upw</code><i> password</i></p>
<dd> Specify the user password for the PDF file.</p>
<dt><code>-p</code></p>
<dd> Include page numbers in output file names.</p>
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
<p> The pdfimages software and documentation are copyright 1998-2011 Glyph &amp; Cog, LLC.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pdfdetach/">pdfdetach</a></code>(1), <code><a href="/docs/linux/man/1-pdffonts/">pdffonts</a></code>(1), <code><a href="/docs/linux/man/1-pdfinfo/">pdfinfo</a></code>(1), <code><a href="/docs/linux/man/1-pdftocairo/">pdftocairo</a></code>(1), <code><a href="/docs/linux/man/1-pdftohtml/">pdftohtml</a></code>(1), <code><a href="/docs/linux/man/1-pdftoppm/">pdftoppm</a></code>(1), <code><a href="/docs/linux/man/1-pdftops/">pdftops</a></code>(1), <code><a href="/docs/linux/man/1-pdftotext/">pdftotext</a></code>(1) <code><a href="/docs/linux/man/1-pdfseparate/">pdfseparate</a></code>(1), <code><a href="/docs/linux/man/1-pdfsig/">pdfsig</a></code>(1), <code><a href="/docs/linux/man/1-pdfunite/">pdfunite</a></code>(1) </p>
<h2>Index</h2>
