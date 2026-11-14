---
title: "optipng(1)"
name: "optipng"
section: "1"
letter: "o"
url: "/docs/linux/man/1-optipng/"
description: "OptiPNG – Optimize Portable Network Graphics files"
---

<h2 class="name">NAME</h2>
<p> <code>OptiPNG</code> &#8211; Optimize Portable Network Graphics files</p>
<h2>SYNOPSIS</h2>
<p> <code>optipng</code> [<code>-?</code> | <code>-h</code> | <code>-help</code>]<br />
 <code>optipng</code> [<i>options&#8230;</i>] <i>files&#8230;</i> </p>
<h2>DESCRIPTION</h2>
<p> The <code>OptiPNG</code> program shall attempt to <i>optimize</i> PNG files, i.e. reduce their size to a minimum, without losing semantic information. In addition, this program shall perform a suite of auxiliary functions like integrity checks, metadata recovery and pixmap-to-PNG conversion. </p>
<p> The optimization attempts are not guaranteed to succeed. Valid PNG files that cannot be optimized by this program are normally left intact; their size will not grow. The user may request to override this default behavior. </p>
<h2>FILES</h2>
<p> The input files are raster image files encoded either in PNG format (the native format), or in an external format. The currently supported external formats are GIF, BMP, PNM and TIFF. </p>
<p> <code>OptiPNG</code> processes each image file given in the command line as follows: </p>
<p> &#8211; If the image is in PNG format:</p>
<dl>
<dt>
<dd> Attempts to optimize the given file in-place. If optimization is successful, or if the option <code>-force</code> is enabled, replaces the original file with its optimized version. The original file is backed up if the option <code>-keep</code> is enabled.</dl>
<p> &#8211; If the image is in an external format:</p>
<dl>
<dt>
<dd> Creates an optimized PNG version of the given file. The output file name is composed from the original file name and the .png extension.</dl>
<p> Existing files are <i>not</i> overwritten, unless the option <code>-clobber</code> is enabled. </p>
<h2>OPTIONS</h2>
<h3>General options</h3>
<dl>
<dt><code>-?</code>, <code>-h</code>, <code>-help</code></p>
<dd> Show a complete summary of options.</p>
<dt><code>-backup</code>, <code>-keep</code></p>
<dd> Keep a backup of the modified files.</p>
<dt><code>-clobber</code></p>
<dd> Overwrite the existing output and backup files.<br />
 Under this option, if the option <code>-backup</code> is not enabled, the old backups of the overwritten files are deleted.</p>
<dt><code>-dir</code> <i>directory</i></p>
<dd> Write the output files to <i>directory</i>.</p>
<dt><code>-fix</code></p>
<dd> Enable error recovery. This option has no effect on valid input files.<br />
 The program will spend a reasonable amount of effort to recover as much data as possible, without increasing the output file size, but the success cannot be generally guaranteed. The program may even increase the file size, e.g., by reconstructing missing critical data. Under this option, integrity shall take precedence over file size.<br />
 When this option is not used, the invalid input files are left unprocessed.</p>
<dt><code>-force</code></p>
<dd> Enforce writing of a new output file.<br />
 This option overrides the program&#8217;s decision not to write such file, e.g. when the PNG input is digitally signed (using dSIG), or when the PNG output becomes larger than the PNG input.</p>
<dt><code>-log</code> <i>file</i></p>
<dd> Log messages to <i>file</i>. For safety reasons, <i>file</i> must have the extension .log.<br />
 This option is deprecated and will be removed eventually. Use shell redirection.</p>
<dt><code>-out</code> <i>file</i></p>
<dd> Write output file to <i>file</i>. The command line must contain exactly one input file.</p>
<dt><code>-preserve</code></p>
<dd> Preserve file attributes (time stamps, file access rights, etc.) where applicable.</p>
<dt><code>-quiet</code>, <code>-silent</code></p>
<dd> Run in quiet mode.<br />
 The messages are still written to the log file if the option <code>-log</code> is enabled.</p>
<dt><code>-simulate</code></p>
<dd> Run in simulation mode: perform the trials, but do not create output files.</p>
<dt><code>-v</code></p>
<dd> Enable the options <code>-verbose</code> and <code>-version</code>.</p>
<dt><code>-verbose</code></p>
<dd> Run in verbose mode.</p>
<dt><code>-version</code></p>
<dd> Show copyright, version and build info.</p>
<dt><code>&#8212;</code></p>
<dd> Stop option switch parsing.</dl>
<h3>PNG encoding and optimization options</h3>
<dl>
<dt><code>-o</code> <i>level</i></p>
<dd> Select the optimization level.<br />
 The optimization level 0 enables a set of optimization operations that require minimal effort. There will be no changes to image attributes like bit depth or color type, and no recompression of existing IDAT datastreams.<br />
 The optimization level 1 enables a single IDAT compression trial. The trial chosen is what <code>OptiPNG</code> <i>thinks</i> it&#8217;s probably the most effective.<br />
 The optimization levels 2 and higher enable multiple IDAT compression trials; the higher the level, the more trials.<br />
 The behavior and the default value of this option may change across different program versions. Use the option <code>-h</code> to see the details pertaining to your specific version.</p>
<dt><code>-f</code> <i>filters</i></p>
<dd> Select the PNG delta filters.<br />
 The <i>filters</i> argument is specified as a rangeset (e.g. <code>-f0-5</code>), and the default <i>filters</i> value depends on the optimization level set by the option <code>-o</code>.<br />
 The filter values 0, 1, 2, 3 and 4 indicate static filtering, and correspond to the standard PNG filter codes (<i>None</i>, <i>Left</i>, <i>Up</i>, <i>Average</i> and <i>Paeth</i>, respectively). The filter value 5 indicates adaptive filtering, whose effect is defined by the <code><a href="/docs/linux/man/3-libpng/">libpng</a></code>(3) library used by <code>OptiPNG</code>.</p>
<dt><code>-full</code></p>
<dd> Produce a full report on IDAT. This option might slow down the trials.</p>
<dt><code>-i</code> <i>type</i></p>
<dd> Select the interlace type (0-1).<br />
 If the interlace type 0 is selected, the output image shall be non-interlaced (i.e. progressive-scanned). If the interlace type 1 is selected, the output image shall be interlaced using the <i>Adam7</i> method.<br />
 By default, the output shall have the same interlace type as the input.</p>
<dt><code>-nb</code></p>
<dd> Do not apply bit depth reduction.</p>
<dt><code>-nc</code></p>
<dd> Do not apply color type reduction.</p>
<dt><code>-np</code></p>
<dd> Do not apply palette reduction.</p>
<dt><code>-nx</code></p>
<dd> Do not apply any lossless image reduction: enable the options <code>-nb</code>, <code>-nc</code> and <code>-np</code>.</p>
<dt><code>-nz</code></p>
<dd> Do not recode IDAT datastreams.<br />
 The IDAT optimization operations that do not require recoding (e.g. IDAT chunk concatenation) are still performed.<br />
 This option has effect on PNG input files only.</p>
<dt><code>-zc</code> <i>levels</i></p>
<dd> Select the zlib compression levels used in IDAT compression.<br />
 The <i>levels</i> argument is specified as a rangeset (e.g. <code>-zc6-9</code>), and the default <i>levels</i> value depends on the optimization level set by the option <code>-o</code>.<br />
 The effect of this option is defined by the <code><a href="/docs/linux/man/3-zlib/">zlib</a></code>(3) library used by <code>OptiPNG</code>.</p>
<dt><code>-zm</code> <i>levels</i></p>
<dd> Select the zlib memory levels used in IDAT compression.<br />
 The <i>levels</i> argument is specified as a rangeset (e.g. <code>-zm8-9</code>), and the default <i>levels</i> value depends on the optimization level set by the option <code>-o</code>.<br />
 The effect of this option is defined by the <code><a href="/docs/linux/man/3-zlib/">zlib</a></code>(3) library used by <code>OptiPNG</code>.</p>
<dt><code>-zs</code> <i>strategies</i></p>
<dd> Select the zlib compression strategies used in IDAT compression.<br />
 The <i>strategies</i> argument is specified as a rangeset (e.g. <code>-zs0-3</code>), and the default <i>strategies</i> value depends on the optimization level set by the option <code>-o</code>.<br />
 The effect of this option is defined by the <code><a href="/docs/linux/man/3-zlib/">zlib</a></code>(3) library used by <code>OptiPNG</code>.</p>
<dt><code>-zw</code> <i>size</i></p>
<dd> Select the zlib window size (32k,16k,8k,4k,2k,1k,512,256) used in IDAT compression.<br />
 The <i>size</i> argument can be specified either in bytes (e.g. 16384) or kilobytes (e.g. 16k). The default <i>size</i> value is set to the lowest window size that yields an IDAT output as big as if yielded by the value 32768.<br />
 The effect of this option is defined by the <code><a href="/docs/linux/man/3-zlib/">zlib</a></code>(3) library used by <code>OptiPNG</code>.</dl>
<h3>Editing options</h3>
<dl>
<dt><code>-snip</code></p>
<dd> Cut one image out of multi-image, animation or video files.<br />
 Depending on the input format, this may be either the first or the most relevant (e.g. the largest) image.</p>
<dt><code>-strip</code> <i>objects</i></p>
<dd> Strip metadata objects from a PNG file.<br />
 PNG metadata is the information stored in any ancillary chunk except tRNS. (tRNS represents the alpha channel, which, even if ignored in rendering, is still a proper image channel in the RGBA color space.)<br />
 The only option currently supported is <code>-strip all</code>.</dl>
<h3>Notes</h3>
<p> Options may come in any order (except for <code>&#8212;</code>), before, after, or alternating with file names. Option names are case-insensitive and may be abbreviated to their shortest unique prefix. </p>
<p> Some options may have arguments that follow the option name, separated by whitespace or the equal sign (&#8216;<code>=</code>&#8216;). If the option argument is a number or a rangeset, the separator may be omitted. For example:</p>
<dl>
<dt>
<dd> <code>-out</code> newfile.png &nbsp;&lt;=&gt; &nbsp;<code>-out=</code>newfile.png<br />
 <code>-o3</code> &nbsp;&lt;=&gt; &nbsp;<code>-o 3</code> &nbsp;&lt;=&gt; &nbsp;<code>-o=3</code><br />
 <code>-f0,3-5</code> &nbsp;&lt;=&gt; &nbsp;<code>-f 0,3-5</code> &nbsp;&lt;=&gt; &nbsp;<code>-f=0,3-5</code></dl>
<p> Rangeset arguments are cumulative; e.g.</p>
<dl>
<dt>
<dd> <code>-f0 -f3-5</code> &nbsp;&lt;=&gt; &nbsp;<code>-f0,3-5</code><br />
 <code>-zs0 -zs1 -zs2-3</code> &nbsp;&lt;=&gt; &nbsp;<code>-zs0,1,2,3</code> &nbsp;&lt;=&gt; &nbsp;<code>-zs0-3</code> </p>
</dl>
<h2>EXTENDED DESCRIPTION</h2>
<p> The PNG optimization algorithm consists of the following steps:</p>
<dl>
<dt>1.</p>
<dd> Reduce the bit depth, the color type and the color palette of the image. This step may reduce the size of the uncompressed image, which, indirectly, may reduce the size of the compressed image (i.e. the size of the output PNG file).</p>
<dt>2.</p>
<dd> Run a suite of compression methods and strategies and select the compression parameters that yield the smallest output file.</p>
<dt>3.</p>
<dd> Store all IDAT contents into a single chunk, eliminating the overhead incurred by repeated IDAT headers and CRCs.</p>
<dt>4.</p>
<dd> Set the zlib window size inside IDAT to a minimum that does not affect the compression ratio, reducing the memory requirements of PNG decoders.</dl>
<p> Not all of the above steps need to be executed. The behavior depends on the actual input files and user options. </p>
<p> Step 1 may be customized via the no-reduce options <code>-nb</code>, <code>-nc</code>, <code>-np</code> and <code>-nx</code>. Step 2 may be customized via the <code>-o</code> option, and may be fine-tuned via the options <code>-zc</code>, <code>-zm</code>, <code>-zs</code> and <code>-zw</code>. Step 3 is always executed. Step 4 is executed only if a new IDAT is being created, and may be fine-tuned via the option <code>-zw</code>. </p>
<p> Extremely exhaustive searches are not generally expected to yield significant improvements in compression ratio, and are recommended to advanced users only. </p>
<h2>EXAMPLES</h2>
<p> optipng file.png &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;# default speed<br />
 optipng -o5 file.png &nbsp;# slow<br />
 optipng -o7 file.png &nbsp;# very slow </p>
<h2>BUGS</h2>
<p> Lossless image reductions are not completely implemented. (This does <i>not</i> affect the integrity of the output files.) Here are the missing pieces:</p>
<dl>
<dt>
<dd> &#8211; The color palette reductions are implemented only partially.<br />
 &#8211; The bit depth reductions below 8, for grayscale images, are not implemented yet.</dl>
<p> Encoding of images whose total IDAT size exceeds 2GB is not supported. </p>
<p> TIFF support is limited to uncompressed, PNG-compatible (grayscale, RGB and RGBA) images. </p>
<p> Metadata is not imported from the external image formats. </p>
<p> There is no support for pipes, streams, extended file attributes or access control lists. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-png/">png</a></code>(5), <code><a href="/docs/linux/man/3-libpng/">libpng</a></code>(3), <code><a href="/docs/linux/man/3-zlib/">zlib</a></code>(3), <code><a href="/docs/linux/man/1-pngcrush/">pngcrush</a></code>(1), <code><a href="/docs/linux/man/1-pngrewrite/">pngrewrite</a></code>(1). </p>
<h2>STANDARDS</h2>
<p> The files produced by <code>OptiPNG</code> are compliant with <code>PNG-2003</code>:<br />
 Glenn Randers-Pehrson et al. <i>Portable Network Graphics (PNG) Specification, Second Edition</i>.<br />
 W3C Recommendation 10 November 2003; ISO/IEC IS 15948:2003 (E).<br />
 <a rel="nofollow" href="http://www.w3.org/TR/PNG/">http://www.w3.org/TR/PNG/</a> </p>
<h2>AUTHOR</h2>
<p> <code>OptiPNG</code> is written and maintained by Cosmin Truta. </p>
<p> This manual page was originally written by Nelson A. de Oliveira for the Debian Project. It was later updated by Cosmin Truta, and is now part of the <code>OptiPNG</code> distribution. </p>
<h2>Index</h2>
