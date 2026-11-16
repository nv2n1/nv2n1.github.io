---
title: "tiff2pdf(1)"
name: "tiff2pdf"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tiff2pdf/"
description: "tiff2pdf – convert a TIFF image to a PDF document"
---

<h2>NAME</h2>
<p> tiff2pdf &#8211; convert a TIFF image to a PDF document</p>
<h2>SYNOPSIS</h2>
<p> <code>tiff2pdf</code> [ <i>options </i> ] <i>input.tiff</i></p>
<h2>DESCRIPTION</h2>
<p> <i>tiff2pdf</i> opens a TIFF image and writes a PDF document to standard output. </p>
<p> The program converts one TIFF file to one PDF file, including multiple page TIFF files, tiled TIFF files, black and white. grayscale, and color TIFF files that contain data of TIFF photometric interpretations of bilevel, grayscale, RGB, YCbCr, CMYK separation, and ICC L*a*b* as supported by <i>libtiff </i> and PDF. </p>
<p> If you have multiple TIFF files to convert into one PDF file then use <i>tiffcp </i> or other program to concatenate the files into a multiple page TIFF file. If the input TIFF file is of huge dimensions (greater than 10000 pixels height or width) convert the input image to a tiled TIFF if it is not already. </p>
<p> The standard output is standard output. Set the output file name with the <code>-o</code><i> output.pdf</i> option. </p>
<p> All black and white files are compressed into a single strip CCITT G4 Fax compressed PDF, unless tiled, where tiled black and white images are compressed into tiled CCITT G4 Fax compressed PDF, <i>libtiff </i> CCITT support is assumed. </p>
<p> Color and grayscale data can be compressed using either JPEG compression, ITU-T T.81, or Zip/Deflate LZ77 compression. Set the compression type using the <code>-j</code> or <code>-z</code> options. JPEG compression support requires that <i>libtiff </i> be configured with JPEG support, and Zip/Deflate compression support requires that <i>libtiff </i> be configured with Zip support, in tiffconf.h. Use only one or the other of <code>-j</code> and <code>-z.</code> </p>
<p> If the input TIFF contains single strip CCITT G4 Fax compressed information, then that is written to the PDF file without transcoding, unless the options of no compression and no passthrough are set, <code>-d</code> and <code>-n.</code> </p>
<p> If the input TIFF contains JPEG or single strip Zip/Deflate compressed information, and they are configured, then that is written to the PDF file without transcoding, unless the options of no compression and no passthrough are set. </p>
<p> The default page size upon which the TIFF image is placed is determined by the resolution and extent of the image data. Default values for the TIFF image resolution can be set using the <code>-x</code> and <code>-y</code> options. The page size can be set using the <code>-p</code> option for paper size, or <code>-w</code> and <code>-l</code> for paper width and length, then each page of the TIFF image is centered on its page. The distance unit for default resolution and page width and length can be set by the <code>-u</code> option, the default unit is inch. </p>
<p> Various items of the output document information can be set with the <code>-e</code>, <code>-c</code>, <code>-a</code>, <code>-t</code>, <code>-s</code>, and <code>-k</code> options. Setting the argument of the option to &quot;&quot; for these tags causes the relevant document information field to be not written. Some of the document information values otherwise get their information from the input TIFF image, the software, author, document name, and image description. </p>
<p> The Portable Document Format (PDF) specification is copyrighted by Adobe Systems, Incorporated.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o</code><i> output-file</i></dt>
<dd> Set the output to go to file. <i>output-file</i></dd>
<dt><code>-j </code></dt>
<dd> Compress with JPEG (requires <i>libjpeg</i> configured with <i>libtiff</i>).</dd>
<dt><code>-z </code></dt>
<dd> Compress with Zip/Deflate (requires <i>zlib</i> configured with <i>libtiff</i>).</dd>
<dt><code>-q</code><i> quality</i></dt>
<dd> Set the compression quality, 1-100 for JPEG.</dd>
<dt><code>-n</code></dt>
<dd> Do not allow data to be converted without uncompressing, no compressed data passthrough.</dd>
<dt><code>-b</code></dt>
<dd> Set PDF &#8220;Interpolate&#8221; user preference.</dd>
<dt><code>-d </code></dt>
<dd> Do not compress (decompress).</dd>
<dt><code>-i </code></dt>
<dd> Invert colors.</dd>
<dt><code>-p</code><i> paper-size</i></dt>
<dd> Set paper size, e.g., <code>letter</code>, <code>legal</code>, <code>A4</code>.</dd>
<dt><code>-F</code></dt>
<dd> Cause the tiff to fill the PDF page.</dd>
<dt><code>-u</code> [<code>i</code>|<code>m</code>]</dt>
<dd> Set distance unit, <code>i</code> for inch, <code>m</code> for centimeter.</dd>
<dt><code>-w</code><i> width</i></dt>
<dd> Set width in units.</dd>
<dt><code>-l</code><i> length</i></dt>
<dd> Set length in units.</dd>
<dt><code>-x</code><i> xres</i></dt>
<dd> Set x/width resolution default.</dd>
<dt><code>-y</code><i> yres</i></dt>
<dd> Set y/length resolution default.</dd>
<dt><code>-r</code> [<code>d</code>|<code>o</code>]</dt>
<dd> Set <code>d</code> for resolution default for images without resolution, <code>o</code> for resolution override for all images.</dd>
<dt><code>-f</code></dt>
<dd> Set PDF &#8220;Fit Window&#8221; user preference.</dd>
<dt><code>-e</code><i> YYYYMMDDHHMMSS</i></dt>
<dd> Set document information date, overrides image or current date/time default, <i>YYYYMMDDHHMMSS.</i></dd>
<dt><code>-c</code><i> creator</i></dt>
<dd> Set document information creator, overrides image software default.</dd>
<dt><code>-a</code><i> author</i></dt>
<dd> Set document information author, overrides image artist default.</dd>
<dt><code>-t</code><i> title</i></dt>
<dd> Set document information title, overrides image document name default.</dd>
<dt><code>-s</code><i> subject</i></dt>
<dd> Set document information subject, overrides image image description default.</dd>
<dt><code>-k</code><i> keywords</i></dt>
<dd> Set document information keywords.</dd>
<dt><code>-h </code></dt>
<dd> List usage reminder to stderr and exit.</dd></dl>
<h2>EXAMPLES</h2>
<dl>
<dt>The following example would generate the file output.pdf from input.tiff.</dt>
<dd>
</dd><dl>
<dt>
</dt><dd>
<pre>
tiff2pdf -o output.pdf input.tiff
</pre>
</dd></dl>
</dl>
<p> The following example would generate PDF output from input.tiff and write it to standard output.</p>
<dl>
<dt>
</dt><dd>
<pre>
tiff2pdf input.tiff
</pre>
</dd></dl>
<p> The following example would generate the file output.pdf from input.tiff, putting the image pages on a letter sized page, compressing the output with JPEG, with JPEG quality 75, setting the title to &#8220;Document&#8221;, and setting the &#8220;Fit Window&#8221; option.</p>
<dl>
<dt>
</dt><dd>
<pre>
tiff2pdf -p letter -j -q 75 -t &quot;Document&quot; -f -o output.pdf input.tiff
</pre>
</dd></dl>
<h2>BUGS</h2>
<p> Please report bugs via the web interface at</p>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://bugzilla.remotesensing.org/enter_bug.cgi?product=libtiff">http://bugzilla.remotesensing.org/enter_bug.cgi?product=libtiff</a></dd></dl>
<h2>SEE ALSO</h2>
<p> <code>libtiff</code>(3), <code><a href="/docs/linux/man/1-tiffcp/">tiffcp</a></code>(1), <code><a href="/docs/linux/man/1-tiff2ps/">tiff2ps</a></code>(1) </p>
<p> Libtiff library home page: <code><a rel="nofollow" href="http://www.remotesensing.org/libtiff/">http://www.remotesensing.org/libtiff/</a></code> </p>
<h2>Index</h2>
