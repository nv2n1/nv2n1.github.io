---
title: "ddjvu(1)"
name: "ddjvu"
section: "1"
letter: "d"
url: "/docs/linux/man/1-ddjvu/"
description: "ddjvu – Command line DjVu decoder."
---

<h2>NAME</h2>
<p> ddjvu &#8211; Command line DjVu decoder. </p>
<h2>SYNOPSIS</h2>
<p> <code>ddjvu -format=</code><i>fmt</i><code> [</code><i>options</i><code>] [</code><i>djvufile</i><code>] [</code><i>outputfile</i><code>]</code> </p>
<h2>DESCRIPTION</h2>
<p> Decode the DjVu file <i>djvufile</i>, produces the image file <i>outputfile</i>. </p>
<p> The DjVu data is read from the standard input when argument <i>djvufile</i> is not specified or when it is equal to a single dash. Similarly, the output data is written to the standard output when argument <i>outputfile</i> is not specified or equal to a single dash. However a valid output file name is always required when producing a TIFF or PDF file. </p>
<h2>MAIN OPTIONS</h2>
<dl>
<dt><code>-format=</code><i>fmt</i></p>
<dd> Specify the output file formats. The recognized file formats are <code>pbm</code>, <code>pgm</code>, <code>ppm</code>, <code>pnm</code>, <code>rle</code>, <code>tiff</code>, and <code>pdf</code>.</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> Formats <code>pbm</code>, <code>pgm</code>, and <code>ppm</code> respectively produce a Portable Bitmap (PBM), Portable Graymap (PGM), or Portable Pixmap (PPM) file. Format <code>pnm</code> produces a PBM, PGM, or PPM output file according to the color content of the output image.</p>
<dt>*</p>
<dd> Format <code>rle</code> produces a compact run length encoded bitonal file that is understood by the DjVuLibre commands <code>cjb2</code> and <code>csepdjvu</code>.</p>
<dt>*</p>
<dd> Format <code>tiff</code> produces a Tagged Image Format (TIFF) file. The resulting file uses the best available lossless compression model. Enabling lossy JPEG compression (see option <code>-quality</code> below) often produces much smaller files. Commands <code><a href="/docs/linux/man/1-tiffcp/">tiffcp</a></code>(1) and <code><a href="/docs/linux/man/1-tiffsplit/">tiffsplit</a></code>(1) are useful for manipulating the resulting TIFF files.</p>
<dt>*</p>
<dd> Format <code>pdf</code> produces a Portable Document Format (PDF) file. Each page in the resulting file is represented by an image at the specified resolution, using the best available lossless compression model. Enabling lossy JPEG compression (see option <code>-quality</code> below) often produces much smaller files. An alternate way to produce PDF file consists in first using <code><a href="/docs/linux/man/1-djvups/">djvups</a></code>(1) and convert the resulting PostScript file to PDF. Which method gives better results depends on the contents of the DJVU file and on the capabilities of the PS to PDF converter.</dl>
</dl>
<dt>
<dd> When option <code>-format</code> is not specified, the extension of argument <i>outputfile</i> has no influence on the default output format. Instead the program behavior is modified to ensure backward compatibility with previous versions of <code>ddjvu</code>. We recommend to always specify the output format using this option.</p>
<dt><code>-page=</code><i>pagespec</i></p>
<dd> Specify which pages should be decoded. When this option is not specified, all pages of the documents are decoded and concatenated into the output file. The page specification <i>pagespec </i> contains one or more comma-separated page ranges. A page range is either a page number, or two page numbers separated by a dash. For instance, specification <code>1-10</code> outputs pages 1 to 10, and specification <code>1,3,99999-4</code> outputs pages 1 and 3, followed by all the document pages in reverse order up to page 4.</p>
<dt><code>-mode=</code><i>mod</i></p>
<dd> Selects which layers of the DjVu image should be rendered. Valid rendering modes are <code>color</code>, <code>black</code>, <code>mask</code>, <code>foreground</code>, and <code>background</code>.</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> Rendering mode <code>color</code> is the default mode. When the DjVu file is bitonal, bitonal or gray-level output is produced depending on the subsampling factor. Otherwise a color image is produced.</p>
<dt>*</p>
<dd> Rendering mode <code>black</code> is useful to extract a meaningful black and white image. bitonal or gray-level output is produced depending on the subsampling factor.</p>
<dt>*</p>
<dd> Rendering modes <code>mask</code>, <code>foreground</code>, and <code>background</code> select specific layers of a DjVu image. These modes can fail if the DjVu image does not contain the selected layer.</dl>
</dl>
<dt><code>-skip</code></p>
<dd> Instead of aborting when encountering a corrupted page, this option causes <code>ddjvu</code> to simply skip the corrupted page and continue with the next. This is useful for processing certain damaged files. </p>
</dl>
<h2>RESOLUTION OPTIONS</h2>
<p> The following options control the resolution of the output image. The default resolution is the native resolution of the DjVu file, equivalent to selecting <code>-1</code>.</p>
<dl>
<dt><code>&#8211;</code><i>n</i></p>
<dd> Specify an integer sub-sampling factor. The dimensions of the full output image will be <i>n</i> times smaller than the DjVu image size. The legal values for argument <i>n</i> range from 1 to 12. Option <code>-1</code>, for instance, produces an output image whose resolution is equal to the resolution of the input DjVu image file.</p>
<dt><code>-subsample=</code><i>n</i></p>
<dd> This is equivalent to option <i>-n</i>.</p>
<dt><code>-scale=</code><i>mag</i></p>
<dd> Specify a magnification factor relative to the resolution stored in the DjVu image. Specifying magnification of 100 produces an image suitable for displaying on a 100 dpi device such as a computer screen. The magnification factor <i>mag</i> can also be interpreted as the resolution of the output image expressed in dot per inch.</p>
<dt><code>-size=</code><i>w</i><code>x</code><i>h</i></p>
<dd> Specify the size of the full output image. Rendering the full DjVu image would create an output image whose width and height would not exceed <i>w</i> and <i>h</i>. To change the aspect ratio, you must also use option <code>-aspect=no</code>.</p>
<dt><code>-aspect=</code><i>yesno</i></p>
<dd> This option indicates whether the image aspect ratio should be preserved. The defaults is to preserve the aspect ration. This option permits changes in the aspect ratio when used in combination with option <code>-size</code>. </p>
</dl>
<h2>OTHER OPTIONS</h2>
<dl>
<dt><code>-verbose</code></p>
<dd> Display informational messages describing the structure of the DjVu image and the format of the output file.</p>
<dt><code>-segment=</code><i>w</i><code>x</code><i>h</i><code>+</code><i>x</i><code>+</code><i>y</i></p>
<dd> Specify an image segment to render. Program <code>ddjvu</code> conceptually renders the full page using the specified resolution, and then extracts a sub-image of width <i>w </i> and height <i>h</i>, starting at position <i></i>(<i>x</i>,<i>y</i>) relative to the bottom left corner of the page. Both operations of course happen simultaneously. Rendering a small sub-image is much faster than rendering the complete image. The output file will always have size <i>w</i>x<i>h</i> when this option is specified.</p>
<dt><code>-quality=</code><i>factor</i></p>
<dd> Enables lossy compression in TIFF and PDF files. Without this option, TIFF or PDF output files always use lossless compression or no compression. Argument <i>factor</i> specifies a JPEG quantization factor ranging from 25 to 150. See command <code><a href="/docs/linux/man/1-cjpeg/">cjpeg</a></code>(1) for more information on JPEG quantization factors. Value 80 is a good starting point.</p>
<dt><code>-quality=uncompressed</code></p>
<dd> Completely disables compression in TIFF and PDF files. Although the resulting files are often huge, this is sometimes useful for maximal compatibility with hastily written software. </p>
</dl>
<h2>DEPRECATED OPTIONS</h2>
<p> Various options have been maintained to ensure backward compatibility with previous versions of <code>ddjvu.</code> When option <code>-format</code> is not specified, the program only decodes the first page of the document and the default resolution becomes <code>-scale=100</code>. Options <code>-size</code>, <code>-scale</code>, <code>-segment</code>, and <code>-page</code> accept an argument separated by a space. Options <code>-foreground</code>, <code>-background</code>, and <code>-black</code> are shorthands for the <code>-mode=</code><i>mod</i> option. Please do not rely on these features. </p>
<h2>EXAMPLES</h2>
<p> Command</p>
<dl>
<dt>
<dd> <code>ddjvu -format=tiff </code><i>myfile.djvu</i><i>myfile.tif</i></dl>
<p> decodes all pages and produces a multipage TIFF file. </p>
<p> Command</p>
<dl>
<dt>
<dd> <code>ddjvu -format=ppm -page=1 -size=100&#215;100 </code><i>myfile.djvu</i><code> &#8211;</code></dl>
<p> produces a thumbnail for the first page of a document and outputs it as a PPM file on the standard output. </p>
<h2>CREDITS</h2>
<p> The new version of this program was written by L&eacute;on Bottou &lt;leonb [at] users.sourceforge.net&gt;. </p>
<p> This program includes code derived from program <code>tiff2pdf</code>, written by Ross Finlayson and released under a BSD license. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-djvu/">djvu</a></code>(1), <code><a href="/docs/linux/man/1-djview/">djview</a></code>(1), <code><a href="/docs/linux/man/5-pnm/">pnm</a></code>(5), <code><a href="/docs/linux/man/5-pbm/">pbm</a></code>(5), <code><a href="/docs/linux/man/5-pgm/">pgm</a></code>(5), <code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5), <code><a href="/docs/linux/man/1-cjpeg/">cjpeg</a></code>(1), <code><a href="/docs/linux/man/1-tiffsplit/">tiffsplit</a></code>(1), <code><a href="/docs/linux/man/1-tiffcp/">tiffcp</a></code>(1) </p>
<h2>Index</h2>
