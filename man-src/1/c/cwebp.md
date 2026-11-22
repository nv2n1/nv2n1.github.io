---

title: "cwebp(1)"
name: "cwebp"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cwebp/"
description: "cwebp – compress an image file to a WebP file"
---

<p> cwebp &#8211; compress an image file to a WebP file</p>
<h2>SYNOPSIS</h2>
<p> <code>cwebp</code> [<i>options</i>]<i> input_file -o output_file.webp</i> </p>
<h2>DESCRIPTION</h2>
<p> This manual page documents the <code>cwebp</code> command. </p>
<p> <code>cwebp</code> compresses an image using the WebP format. Input format can be either PNG, JPEG, TIFF or raw Y&#8217;CbCr samples.</p>
<h2>OPTIONS</h2>
<p> The basic options are:</p>
<dl>
<dt><code>-o</code><i> string</i></dt>
<dd> Specify the name of the output WebP file. If omitted, <code>cwebp</code> will perform compression but only report statistics.</dd>
<dt><code>-h, -help</code></dt>
<dd> A short usage summary.</dd>
<dt><code>-H, -longhelp</code></dt>
<dd> A summary of all the possible options.</dd>
<dt><code>-version</code></dt>
<dd> Print the version number (as major.minor.revision) and exit.</dd>
<dt><code>-q</code><i> float</i></dt>
<dd> Specify the compression factor for RGB channels between 0 and 100. The default is 75.<br/>
 In case of lossy compression (default), a small factor produces a smaller file with lower quality. Best quality is achieved by using a value of 100.<br/>
 In case of lossless compression (specified by the -lossless option), a small factor enables faster compression speed, but produces a larger file. Maximum compression is achieved by using a value of 100.</dd>
<dt><code>-alpha_q</code><i> int</i></dt>
<dd> Specify the compression factor for alpha compression between 0 and 100. Lossless compression of alpha is achieved using a value of 100, while the lower values result in a lossy compression. The default is 100.</dd>
<dt><code>-f</code><i> int</i></dt>
<dd> Specify the strength of the deblocking filter, between 0 (no filtering) and 100 (maximum filtering). A value of 0 will turn off any filtering. Higher value will increase the strength of the filtering process applied after decoding the picture. The higher the value the smoother the picture will appear. Typical values are usually in the range of 20 to 50.</dd>
<dt><code>-preset</code><i> string</i></dt>
<dd> Specify a set of pre-defined parameters to suit a particular type of source material. Possible values are: <code>default</code>, <code>photo</code>, <code>picture</code>, <code>drawing</code>, <code>icon</code>, <code>text</code>. Since <code>-preset</code> overwrites the other parameters&#8217; values (except the <code>-q</code> one), this option should preferably appear first in the order of the arguments.</dd>
<dt><code>-sns</code><i> int</i></dt>
<dd> Specify the amplitude of the spatial noise shaping. Spatial noise shaping (or <code>sns</code> for short) refers to a general collection of built-in algorithms used to decide which area of the picture should use relatively less bits, and where else to better transfer these bits. The possible range goes from 0 (algorithm is off) to 100 (the maximal effect). The default value is 80.</dd>
<dt><code>-m</code><i> int</i></dt>
<dd> Specify the compression method to use. This parameter controls the trade off between encoding speed and the compressed file size and quality. Possible values range from 0 to 6. Default value is 4. When higher values are used, the encoder will spend more time inspecting additional encoding possibilities and decide on the quality gain. Lower value can result is faster processing time at the expense of larger file size and lower compression quality.</dd>
<dt><code>-jpeg_like</code></dt>
<dd> Change the internal parameter mapping to better match the expected size of JPEG compression. This flag will generally produce an output file of similar size to its JPEG equivalent (for the same <code>-q</code> setting), but with less visual distortion.</dd>
<dt><code>-mt</code></dt>
<dd> Use multi-threading for encoding, if possible. This option is only effective when using lossy compression on a source with a transparency channel.</dd>
<dt><code>-low_memory</code></dt>
<dd> Reduce memory usage of lossy encoding by saving four times the compressed size (typically). This will make the encoding slower and the output slightly different in size and distortion. This flag is only effective for methods 3 and up, and is off by default. Note that leaving this flag off will have some side effects on the bitstream: it forces certain bitstream features like number of partitions (forced to 1). Note that a more detailed report of bitstream size is printed by <code>cwebp</code> when using this option.</dd>
<dt><code>-af</code></dt>
<dd> Turns auto-filter on. This algorithm will spend additional time optimizing the filtering strength to reach a well-balanced quality. </dd>
</dl>
<h2>ADDITIONAL OPTIONS</h2>
<p> More advanced options are:</p>
<dl>
<dt><code>-sharpness</code><i> int</i></dt>
<dd> Specify the sharpness of the filtering (if used). Range is 0 (sharpest) to 7 (least sharp). Default is 0.</dd>
<dt><code>-strong</code></dt>
<dd> Use strong filtering (if filtering is being used thanks to the <code>-f</code> option). Strong filtering is on by default.</dd>
<dt><code>-nostrong</code></dt>
<dd> Disable strong filtering (if filtering is being used thanks to the <code>-f</code> option) and use simple filtering instead.</dd>
<dt><code>-segments</code><i> int</i></dt>
<dd> Change the number of partitions to use during the segmentation of the sns algorithm. Segments should be in range 1 to 4. Default value is 4. This option has no effect for methods 3 and up, unless <code>-low_memory</code> is used.</dd>
<dt><code>-partition_limit</code><i> int</i></dt>
<dd> Degrade quality by limiting the number of bits used by some macroblocks. Range is 0 (no degradation, the default) to 100 (full degradation). Useful values are usually around 30-70 for moderately large images. In the VP8 format, the so-called control partition has a limit of 512k and is used to store the following information: whether the macroblock is skipped, which segment it belongs to, whether it is coded as intra 4&#215;4 or intra 16&#215;16 mode, and finally the prediction modes to use for each of the sub-blocks. For a very large image, 512k only leaves room to few bits per 16&#215;16 macroblock. The absolute minimum is 4 bits per macroblock. Skip, segment, and mode information can use up almost all these 4 bits (although the case is unlikely), which is problematic for very large images. The partition_limit factor controls how frequently the most bit-costly mode (intra 4&#215;4) will be used. This is useful in case the 512k limit is reached and the following message is displayed: <i>Error code: 6 (PARTITION0_OVERFLOW: Partition #0 is too big to fit 512k)</i>. If using <code>-partition_limit</code> is not enough to meet the 512k constraint, one should use less segments in order to save more header bits per macroblock. See the <code>-segments</code> option.</dd>
<dt><code>-size</code><i> int</i></dt>
<dd> Specify a target size (in bytes) to try and reach for the compressed output. Compressor will make several pass of partial encoding in order to get as close as possible to this target.</dd>
<dt><code>-psnr</code><i> float</i></dt>
<dd> Specify a target PSNR (in dB) to try and reach for the compressed output. Compressor will make several pass of partial encoding in order to get as close as possible to this target.</dd>
<dt><code>-pass</code><i> int</i></dt>
<dd> Set a maximum number of passes to use during the dichotomy used by options <code>-size</code> or <code>-psnr</code>. Maximum value is 10.</dd>
<dt><code>-crop</code><i> x_position y_position width height</i></dt>
<dd> Crop the source to a rectangle with top-left corner at coordinates (<code>x_position</code>, <code>y_position</code>) and size <code>width</code> x <code>height</code>. This cropping area must be fully contained within the source rectangle.</dd>
<dt><code>-s</code><i> width height</i></dt>
<dd> Specify that the input file actually consists of raw Y&#8217;CbCr samples following the ITU-R BT.601 recommendation, in 4:2:0 linear format. The luma plane has size <code>width</code> x <code>height</code>.</dd>
<dt><code>-map</code><i> int</i></dt>
<dd> Output additional ASCII-map of encoding information. Possible map values range from 1 to 6. This is only meant to help debugging.</dd>
<dt><code>-pre</code><i> int</i></dt>
<dd> Specify a pre-processing filter. This option is a placeholder and has currently no effect.</dd>
<dt><code>-alpha_filter</code><i> string</i></dt>
<dd> Specify the predictive filtering method for the alpha plane. One of &#8216;none&#8217;, &#8216;fast&#8217; or &#8216;best&#8217;, in increasing complexity and slowness order. Default is &#8216;fast&#8217;. Internally, alpha filtering is performed using four possible predictions (none, horizontal, vertical, gradient). The &#8216;best&#8217; mode will try each mode in turn and pick the one which gives the smaller size. The &#8216;fast&#8217; mode will just try to form an a-priori guess without testing all modes.</dd>
<dt><code>-alpha_method</code><i> int</i></dt>
<dd> Specify the algorithm used for alpha compression: 0 or 1. Algorithm 0 denotes no compression, 1 uses WebP lossless format for compression. The default is 1.</dd>
<dt><code>-alpha_cleanup</code></dt>
<dd> Modify unseen RGB values under fully transparent area, to help compressibility. The default is off.</dd>
<dt><code>-noalpha</code></dt>
<dd> Using this option will discard the alpha channel.</dd>
<dt><code>-lossless</code></dt>
<dd> Encode the image without any loss.</dd>
<dt><code>-hint</code><i> string</i></dt>
<dd> Specify the hint about input image type. Possible values are: <code>photo</code>, <code>picture</code> or <code>graph</code>.</dd>
<dt><code>-metadata</code><i> string</i></dt>
<dd> A comma separated list of metadata to copy from the input to the output if present. Valid values: <code>all</code>, <code>none</code>, <code>exif</code>, <code>icc</code>, <code>xmp</code>. The default is <code>none</code>. </dd>
<p> Note: each input format may not support all combinations.</p>
<dt><code>-noasm</code></dt>
<dd> Disable all assembly optimizations.</dd>
<dt><code>-v</code></dt>
<dd> Print extra information (encoding time in particular).</dd>
<dt><code>-print_psnr</code></dt>
<dd> Compute and report average PSNR (Peak-Signal-To-Noise ratio).</dd>
<dt><code>-print_ssim</code></dt>
<dd> Compute and report average SSIM (structural similarity metric, see <a rel="nofollow" href="http://en.wikipedia.org/wiki/SSIM">http://en.wikipedia.org/wiki/SSIM</a> for additional details).</dd>
<dt><code>-print_lsim</code></dt>
<dd> Compute and report local similarity metric (sum of lowest error amongst the collocated pixel neighbors).</dd>
<dt><code>-progress</code></dt>
<dd> Report encoding progress in percent.</dd>
<dt><code>-quiet</code></dt>
<dd> Do not print anything.</dd>
<dt><code>-short</code></dt>
<dd> Only print brief information (output file size and PSNR) for testing purpose. </dd>
</dl>
<h2>BUGS</h2>
<p> Please report all bugs to our issue tracker: <a rel="nofollow" href="http://code.google.com/p/webp/issues">http://code.google.com/p/webp/issues</a><br/>
 Patches welcome! See this page to get started: <a rel="nofollow" href="http://www.webmproject.org/code/contribute/submitting-patches/">http://www.webmproject.org/code/contribute/submitting-patches/</a> </p>
<h2>EXAMPLES</h2>
<p> cwebp -q 50 -lossless picture.png -o picture_lossless.webp<br/>
 cwebp -q 70 picture_with_alpha.png -o picture_with_alpha.webp<br/>
 cwebp -sns 70 -f 50 -size 60000 picture.png -o picture.webp </p>
<h2>AUTHORS</h2>
<p> <code>cwebp</code> was written by the WebP team.<br/>
 The latest source tree is available at <a rel="nofollow" href="http://www.webmproject.org/code">http://www.webmproject.org/code</a> </p>
<p> This manual page was written by Pascal Massimino &lt;pascal.massimino [at] gmail.com&gt;, for the Debian project (and may be used by others). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dwebp/">dwebp</a></code>(1), <code><a href="/docs/linux/man/1-gif2webp/">gif2webp</a></code>(1).<br/>
 Please refer to <a rel="nofollow" href="http://developers.google.com/speed/webp/">http://developers.google.com/speed/webp/</a> for additional information. </p>
