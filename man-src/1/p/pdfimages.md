---

title: "pdfimages(1)"
name: "pdfimages"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdfimages/"
description: "pdfimages – Portable Document Format (PDF) image extractor (version 3.03)"
---

<p> <code>pdfimages</code> [options] <i>PDF-file image-root</i></p>
<p> <code>Pdfimages</code> saves images from a Portable Document Format (PDF) file as Portable Pixmap (PPM), Portable Bitmap (PBM), Portable Network Graphics (PNG), Tagged Image File Format (TIFF), JPEG, JPEG2000, or JBIG2 files. </p>
<p> Pdfimages reads the PDF file <i>PDF-file</i>, scans one or more pages, and writes one file for each image, <i>image-root</i>&#8211;<i>nnn</i>.<i>xxx</i>, where <i>nnn</i> is the image number and <i>xxx</i> is the image type (.ppm, .pbm, .png, .tif, .jpg, jp2, jb2e, or jb2g). If <i>PDF-file</i> is &#8216;-&#8216;, it reads the PDF file from stdin. </p>
<p> The default output format is PBM (for monochrome images) or PPM for non-monochrome. The -png or -tiff options change to default output to PNG or TIFF respectively. If both -png and -tiff are specified, CMYK images will be written as TIFF and all other images will be written as PNG. In addition the -j, -jp2, and -jbig2 options will cause JPEG, JPEG2000, and JBIG2, respectively, images in the PDF file to be written in their native format.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f</code><i> number</i></dt>
<dd> Specifies the first page to scan.</dd>
<dt><code>-l</code><i> number</i></dt>
<dd> Specifies the last page to scan.</dd>
<dt><code>-png</code></dt>
<dd> Change the default output format to PNG.</dd>
<dt><code>-tiff</code></dt>
<dd> Change the default output format to TIFF.</dd>
<dt><code>-j</code></dt>
<dd> Write images in JPEG format as JPEG files instead of the default format. The JPEG file is identical to the JPEG data stored in the PDF.</dd>
<dt><code>-jp2</code></dt>
<dd> Write images in JPEG2000 format as JP2 files instead of the default format. The JP2 file is identical to the JPEG2000 data stored in the PDF.</dd>
<dt><code>-jbig2</code></dt>
<dd> Write images in JBIG2 format as JBIG2 files instead of the default format. JBIG2 data in PDF is of the embedded type. The embedded type of JBIG2 has an optional separate file containing global data. The embedded data is written with the extension .jb2e and the global data (if available) will be written to the same image number with the extension .jb2g. The content of both these files is identical to the JBIG2 data in the PDF.</dd>
<dt><code>-ccitt</code></dt>
<dd> Write images in CCITT format as CCITT files instead of the default format. The CCITT file is identical to the CCITT data stored in the PDF. PDF files contain additional parameters specifying how to decode the CCITT data. These parameters are translated to fax2tiff input options and written to a .params file with the same image number. The parameters are:</dd>
<dl>
<dl>
<dt><code>-1</code></dt>
<dd> 1D Group 3 encoding</dd>
<dt><code>-2</code></dt>
<dd> 2D Group 3 encoding</dd>
<dt><code>-4</code></dt>
<dd> Group 4 encoding</dd>
<dt><code>-A</code></dt>
<dd> Beginning of line is aligned on a byte boundary</dd>
<dt><code>-P</code></dt>
<dd> Beginning of line is not aligned on a byte boundary</dd>
<dt><code>-X n</code></dt>
<dd> The image width in pixels</dd>
<dt><code>-W</code></dt>
<dd> Encoding uses 1 for black and 0 for white</dd>
<dt><code>-B</code></dt>
<dd> Encoding uses 0 for black and 1 for white</dd>
<dt><code>-M</code></dt>
<dd> Input data fills from most significant bit to least significant bit.</dd></dl>
</dl>
<dt><code>-all</code></dt>
<dd> Write JPEG, JPEG2000, JBIG2, and CCITT images in their native format. CMYK files are written as TIFF files. All other images are written as PNG files. This is equivalent to specifying the options -png -tiff -j -jp2 -jbig2 -ccitt.</dd>
<dt><code>-list</code></dt>
<dd> Instead of writing the images, list the images along with various information for each image. Do not specify an <i>image-root</i> with this option.</dd>
<dt>
</dt><dd> The following information is listed for each image:</dd>
<dl>
<dl>
<dt><code>page</code></dt>
<dd> the page number containing the image</dd>
<dt><code>num</code></dt>
<dd> the image number</dd>
<dt><code>type</code></dt>
<dd> the image type:</dd></dl>
<dl>
<dt>
</dt><dd> image &#8211; an opaque image</dd></dl>
<dl>
<dt>
</dt><dd> mask &#8211; a monochrome mask image</dd></dl>
<dl>
<dt>
</dt><dd> smask &#8211; a soft-mask image</dd></dl>
<dl>
<dt>
</dt><dd> stencil &#8211; a monochrome mask image used for painting a color or pattern</dd></dl>
<p> Note: Tranparency in images is represented in PDF using a separate image for the image and the mask/smask. The mask/smask used as part of a transparent image always immediately follows the image in the image list.</p>
<dl>
<dt><code>width</code></dt>
<dd> image width (in pixels)</dd>
<dt><code>height</code></dt>
<dd> image height (in pixels)</dd></dl>
<p> Note: the image width/height is the size of the embedded image, not the size the image will be rendered at.</p>
<dl>
<dt><code>color</code></dt>
<dd> image color space:</dd></dl>
<dl>
<dt>
</dt><dd> gray &#8211; Gray</dd></dl>
<dl>
<dt>
</dt><dd> rgb &#8211; RGB</dd></dl>
<dl>
<dt>
</dt><dd> cmyk &#8211; CMYK</dd></dl>
<dl>
<dt>
</dt><dd> lab &#8211; L*a*b</dd></dl>
<dl>
<dt>
</dt><dd> icc &#8211; ICC Based</dd></dl>
<dl>
<dt>
</dt><dd> index &#8211; Indexed Color</dd></dl>
<dl>
<dt>
</dt><dd> sep &#8211; Separation</dd></dl>
<dl>
<dt>
</dt><dd> devn &#8211; DeviceN</dd></dl>
<dl>
<dt><code>comp</code></dt>
<dd> number of color components</dd>
<dt><code>bpc</code></dt>
<dd> bits per component</dd>
<dt><code>enc</code></dt>
<dd> encoding:</dd></dl>
<dl>
<dt>
</dt><dd> image &#8211; raster image (may be Flate or LZW compressed but does not use an image encoding)</dd></dl>
<dl>
<dt>
</dt><dd> jpeg &#8211; Joint Photographic Experts Group</dd></dl>
<dl>
<dt>
</dt><dd> jp2 &#8211; JPEG2000</dd></dl>
<dl>
<dt>
</dt><dd> jbig2 &#8211; Joint Bi-Level Image Experts Group</dd></dl>
<dl>
<dt>
</dt><dd> ccitt &#8211; CCITT Group 3 or Group 4 Fax</dd></dl>
<dl>
<dt><code>interp</code></dt>
<dd> &quot;yes&quot; if the interpolation is to be performed when scaling up the image</dd>
<dt><code>object ID</code></dt>
<dd> the image dictionary object ID (number and generation)</dd>
<dt><code>x-ppi</code></dt>
<dd> The horizontal resolution of the image (in pixels per inch) when rendered on the pdf page.</dd>
<dt><code>y-ppi</code></dt>
<dd> The vertical resolution of the image (in pixels per inch) when rendered on the pdf page.</dd>
<dt><code>size</code></dt>
<dd> The size of the embedded image in the pdf file. The following suffixes are used: &#8216;B&#8217; bytes, &#8216;K&#8217; kilobytes, &#8216;M&#8217; megabytes, and &#8216;G&#8217; gigabytes.</dd>
<dt><code>ratio</code></dt>
<dd> The compression ratio of the embedded image.</dd></dl>
</dl>
<dt><code>-opw</code><i> password</i></dt>
<dd> Specify the owner password for the PDF file. Providing this will bypass all security restrictions.</dd>
<dt><code>-upw</code><i> password</i></dt>
<dd> Specify the user password for the PDF file.</dd>
<dt><code>-p</code></dt>
<dd> Include page numbers in output file names.</dd>
<dt><code>-q</code></dt>
<dd> Don&#8217;t print any messages or errors.</dd>
<dt><code>-v</code></dt>
<dd> Print copyright and version information.</dd>
<dt><code>-h</code></dt>
<dd> Print usage information. (<code>-help</code> and <code>&#8211;help</code> are equivalent.)</dd></dl>
<h2>EXIT CODES</h2>
<p> The Xpdf tools use the following exit codes:</p>
<dl>
<dt>0</dt>
<dd> No error.</dd>
<dt>1</dt>
<dd> Error opening a PDF file.</dd>
<dt>2</dt>
<dd> Error opening an output file.</dd>
<dt>3</dt>
<dd> Error related to PDF permissions.</dd>
<dt>99</dt>
<dd> Other error.</dd></dl>
<h2>AUTHOR</h2>
<p> The pdfimages software and documentation are copyright 1998-2011 Glyph &amp; Cog, LLC.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pdfdetach/">pdfdetach</a></code>(1), <code><a href="/docs/linux/man/1-pdffonts/">pdffonts</a></code>(1), <code><a href="/docs/linux/man/1-pdfinfo/">pdfinfo</a></code>(1), <code><a href="/docs/linux/man/1-pdftocairo/">pdftocairo</a></code>(1), <code><a href="/docs/linux/man/1-pdftohtml/">pdftohtml</a></code>(1), <code><a href="/docs/linux/man/1-pdftoppm/">pdftoppm</a></code>(1), <code><a href="/docs/linux/man/1-pdftops/">pdftops</a></code>(1), <code><a href="/docs/linux/man/1-pdftotext/">pdftotext</a></code>(1) <code><a href="/docs/linux/man/1-pdfseparate/">pdfseparate</a></code>(1), <code><a href="/docs/linux/man/1-pdfsig/">pdfsig</a></code>(1), <code><a href="/docs/linux/man/1-pdfunite/">pdfunite</a></code>(1) </p>
