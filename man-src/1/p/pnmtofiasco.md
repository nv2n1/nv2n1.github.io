---
title: "pnmtofiasco(1)"
name: "pnmtofiasco"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pnmtofiasco/"
description: "pnmtofiasco – Convert a portable anymap to FIASCO compressed file"
---

<h2 class="name">NAME</h2>
<p> pnmtofiasco &#8211; Convert a portable anymap to FIASCO compressed file</p>
<h2>SYNOPSIS</h2>
<p> <code>pnmtofiasco</code> [<i>option</i>]&#8230; [<i>filename</i>]&#8230; </p>
<h2>DESCRIPTION</h2>
<p> <code>pnmtofiasco </code> compresses the named pbm, pgm, or ppm image files, or Standard Input if no file is named, and produces a FIASCO file on Standard Output. </p>
<h2>OPTIONS</h2>
<p> All option names may be abbreviated; for example, &#8211;optimize may be written &#8211;optim or &#8211;opt. For most options a one letter short option is provided. Mandatory or optional arguments to long options are mandatory or optional for short options, too. Both short and long options are case sensitive. </p>
<p> The basic options are: </p>
<dl>
<dt><code>-i</code> <i>name</i>, <code>&#8211;input-name=</code><i>name</i></p>
<dd> Compress the named images, not Standard Input. If <i>name</i> is <code>&#8211;</code>, read Standard Input. <i>name</i> has to be either an image filename or a template of the form: </p>
<p> <center> prefix[start-end{+,-}step]suffix<br />
 </center> </p>
<p> Templates are useful when compressing video streams: e.g., if you specify the template <code>img0[12-01-2].pgm</code>, then <code>pnmtofiasco</code> compresses the images img012.pgm, img010.pgm, &#8230;, img002.pgm. </p>
<p> If <i>name</i> is a relative path, <code>pnmtofiasco </code> searches for the image files in the current directory and in the (colon-separated) list of directories given by the environment variable <code>FIASCO_IMAGES</code>. </p>
<dt><code>-o</code> <i>output-file</i>, <code>&#8211;output-name=</code><i>name</i></p>
<dd> Write FIASCO output to the named file, not to Standard Output. </p>
<p> If <i>name</i> is a relative path and the environment variable <code>FIASCO_DATA</code> is a (colon-separated) list of directories, then <code>pnmtofiasco</code> writes the output file to the first (writable) directory of this list. Otherwise, <code>pnmtofiasco</code> write it to the current directory. </p>
<dt><code>-q</code> <i>N</i>, <code>&#8211;quality=</code><i>N</i></p>
<dd> Set quality of compression to <i>N</i>. Quality is 1 (worst) to 100 (best); default is 20. </p>
<dt><code>-v</code>, <code>&#8211;version</p>
<dd> Print pnmtofiasco</code> version number, then exit. </p>
<dt><code>-V</code> <i>N</i>, <code>&#8211;verbose </code><i>N</i></p>
<dd> Set level of verbosity to <i>N</i>. Level is 0 (no output at all), 1 (show progress meter), or 2 (show detailed compression statistics); default is 1. </p>
<dt><code>-B</code> <i>N</i>, <code>&#8211;progress-meter </code><i>N</i></p>
<dd> Set type of progress-meter to <i>N</i>. The following types are available; default is 1: </p>
<p> <code>0</code>: no progress meter </p>
<p> <code>1</code>: RPM style progress bar using 50 hash marks </p>
<p> <code>2</code>: percentage meter </p>
<dt><code>-f</code> <i>name</i>, <code>&#8211;config=</code><i>name</i></p>
<dd> Load parameter file <i>name </i> to initialize the options of <code>pnmtofiasco</code>. See file <code>system.fiascorc</code> for an example of the syntax. Options of <code>pnmtofiasco</code> are set by any of the following methods (in the specified order): </p>
<p> 1) Global ressource file <code>/etc/system.fiascorc</code> </p>
<p> 2) $HOME/.fiascorc </p>
<p> 3) command line </p>
<p> 4) &#8211;config=<i>name</i> </p>
<dt><code>-h</code>, <code>&#8211;info</p>
<dd> Print brief help, then exit. </p>
<dt>-H</code>, <code>&#8211;help</p>
<dd> Print detailed help, then exit. </p>
<dt>The options for advanced users are:</p>
<dd>
<dt>-b</code> <i>name</i>, <code>&#8211;basis-name=</code><i>name</i></p>
<dd> Preload compression basis <i>name</i> into FIASCO. The basis <i>name</i> provides the initial compression dictionary. Either use one of the files &quot;small.fco&quot;, &quot;medium.fco&quot;, or &quot;large.fco&quot; that come with <code>pnmtofiasco </code> or create a new ASCII basis file.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;</p>
<dt><code>-z</code> <i>N</i>, <code>&#8211;optimize=</code><i>N</i> Set optimization level to</p>
<dd> <i>N</i>. Level is 0 (fastes) to 3 (slowest); default is 1. Be warned, the encoding time dramatically increased when <i>N</i>=<code>2</code> or <i>N</i>=<code>3</code> while the compression performance only slightly improves. </p>
<dt><code>-P</code>, <code>&#8211;prediction</p>
<dd> Use additional predictive coding. If this optimization is enabled then the image is compressed in two steps. In the first step, a coarse approximation of the image is computed using large unichrome blocks. Finally, the delta image is computed and the prediction error is approximated using the standard FIASCO algorithm. </p>
<dt>-D</code> <i>N</i>, <code>&#8211;dictionary-size=</code><i>N</i></p>
<dd> Set size of dictionary that is used when coding the luminance band to <i>N</i>; default is 10000, i.e., the dictionary is not restricted. </p>
<dt><code>-C</code> <i>N</i>, <code>&#8211;chroma-dictionary=</code><i>N</i></p>
<dd> Set size of dictionary that is used when coding chroma bands to <i>N</i>; default is 40. </p>
<dt><code>-Q</code> <i>N</i>, <code>&#8211;chroma-qfactor=</code><i>N</i></p>
<dd> Reduce the quality of chroma band compression <i>N</i>-times with respect to the user defined quality <i>q</i> of the luminance band compression (<code>&#8211;quality</code>=<i>q</i>); default is 2. </p>
<dt><code>-t</code> <i>N</i>, <code>&#8211;tiling-exponent=</code><i>N</i></p>
<dd> Subdivide the image into 2^<i>N</i> tiles prior coding; default is 4, i.e. the image is subdivided into 16 tiles. The processing order of the individual tiles is defined by the option <code>&#8211;tiling-method=</code><i>name</i>. </p>
<dt><code>-T</code> <i>name</i>, <code>&#8211;tiling-method=</code><i>name</i></p>
<dd> Order the individual image tiles (the image is subdivided into; see option <code>&#8211;tiling-exponent=</code><i>N</i>) by method <i>name</i>; default is &quot;desc-variance&quot;. </p>
<p> <code>desc-variance</code>: Tiles with small variances are processed first. </p>
<p> <code>asc-variance</code>: Tiles with large variances are processed first. </p>
<p> <code>desc-spiral</code>: Tiles are process in spiral order starting in the middle. </p>
<p> <code>asc-spiral</code>: Tiles are process in spiral order starting at the border. </p>
<dt><code>&#8211;rpf-mantissa=</code><i>N</i></p>
<dd> Use <i>N</i> mantissa bits for quantized coefficients. </p>
<dt><code>&#8211;dc-rpf-mantissa=</code><i>N</i></p>
<dd> Use <i>N</i> mantissa bits for quantized DC coefficients. </p>
<dt><code>&#8211;rpf-range=</code><i>N</i></p>
<dd> Coefficients outside the quantization interval [-<i>N</i>,+<i>N</i>] are set to zero. </p>
<dt><code>&#8211;dc-rpf-range=</code><i>N</i></p>
<dd> DC coefficients outside the quantization interval [-<i>N</i>,+<i>N</i>] are set to zero. </p>
<dt>Additional options for video compression are:</p>
<dd>
<dt><code>-s</code> <i>N</i>, <code>&#8211;smooth=</code><i>N</i></p>
<dd> Smooth decompressed reference frames along the partitioning borders by the given amount <i>N</i>. <i>N</i> is 0 (no smoothing) to 100; default is 70. This factor is stored in the FIASCO file. </p>
<dt><code>-m</code> <i>N</i>, <code>&#8211;min-level=</code><i>N</i></p>
<dd> Start prediction (motion compensated prediction or additional prediction) on block level <i>N</i>; default is level 6. I.e., motion compensation is applied to all image blocks of at least 8&#215;8 pixels (binary tree level <i>N</i>=6), 16&#215;8 (<i>N</i>=7), 16&#215;16 (<i>N</i>=8), etc. </p>
<dt><code>-M</code> <i>N</i>, <code>&#8211;max-level=</code><i>N</i></p>
<dd> Stop prediction (motion compensated prediction or additional prediction) on block level <i>N</i>; default is level 10. I.e., motion compensation is applied to all image blocks of at most 16&#215;16 pixels (<i>N</i>=8), 32&#215;16 (<i>N</i>=9), 32&#215;32 (<i>N</i>=10), etc. </p>
<dt><code>-2</code>, <code>&#8211;half-pixel</p>
<dd> Use half pixel precise motion compensation. </p>
<dt>-F</code> <i>N</i>, <code>&#8211;fps=</code><i>N</i></p>
<dd> Set number of frames per second to <i>N</i>. This value is stored in the FIASCO output file and is used in the decoder <a href="/docs/linux/man/1-dfiasco/">dfiasco</a>(1) to control the framerate. </p>
<dt><code>-p</code> <i>type</i>, <code>&#8211;pattern=</code><i>type</i></p>
<dd> Defines the type of inter frame compression which should be applied to individual frames of a video stream. <i>type</i> is a sequence of characters; default is &quot;IPPPPPPPPP&quot;. Element <code>N</code> defines the type of predicting which should be used for frame <code>N</code>; the frame type pattern is periodically extended. Valid characters are: </p>
<p> <code>I</code>: intra frame, i.e., no motion compensated prediction is used at all. </p>
<p> <code>P</code>: predicted frame, i.e., a previously encoded frame is used for prediction (forward prediction). </p>
<p> <code>B</code>: bidirectional predicted frame, i.e., not only a previously shown frame but also a frame of the future is used for prediction (forward, backward or interpolated prediction). </p>
<dt><code>&#8211;cross-B-search</p>
<dd> Instead of using exhaustive search the &quot;Cross-B-Search&quot; algorithm is used to find the best interpolated prediction of B-frames. </p>
<dt>&#8211;B-as-past-ref</p>
<dd> Also use previously encoded B-frames when prediction the current frame. If this option is not set, only I- and P-frames are used to predict the current frame. </p>
</dl>
<p> </code></p>
<h2>EXAMPLES</h2>
<dl>
<dt>pnmtofiasco &lt; foo.ppm &gt;foo.wfa</p>
<dd> Compress the still image &quot;foo.ppm&quot; to the FIASCO file &quot;foo.wfa&quot; using the default options. </p>
<dt>pnmtofiasco -2 -p &quot;IBBPBBPBB&quot; -fps 15 -o video.wfa foo0*.ppm</p>
<dd> Compress the video frames &quot;foo0*.ppm&quot; to the FIASCO file &quot;video.wfa&quot; using half pixel precise motion compensation at a frame rate of 15 frames per second. Intra frame 1 is used to predict P-frame 4, frames 1 and 4 are used to predict B-frames 2 and 3, and so on. Frame 10 is again an intra-frame. </p>
</dl>
<h2>FILES</h2>
<dl>
<dt><code>/etc/system.fiascorc</code></p>
<dd> The systemwide initialization file.</p>
<dt>$HOME<code>/.fiascorc</code></p>
<dd> The personal initialization file. </p>
</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>FIASCO_IMAGES</code></p>
<dd> Search path for image files. Default is &quot;./&quot;.</p>
<dt><code>FIASCO_DATA</code></p>
<dd> Search and save path for FIASCO files. Default is &quot;./&quot;. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-fiascotopnm/">fiascotopnm</a></code>(1), <code><a href="/docs/linux/man/1-ppmtojpeg/">ppmtojpeg</a></code>(1), <code><a href="/docs/linux/man/1-pnmtojbig/">pnmtojbig</a></code>(1), <code><a href="/docs/linux/man/1-ppmtogif/">ppmtogif</a></code>(1), <code><a href="/docs/linux/man/5-pnm/">pnm</a></code>(5) </p>
<p> Ullrich Hafner, Juergen Albert, Stefan Frank, and Michael Unger. <code>Weighted Finite Automata for Video Compression</code>, IEEE Journal on Selected Areas In Communications, January 1998<br />
 Ullrich Hafner. <code>Low Bit-Rate Image and Video Coding with Weighted Finite Automata</code>, Ph.D. thesis, Mensch &amp; Buch Verlag, ISBN 3-89820-002-7, October 1999. </p>
<h2>AUTHOR</h2>
<p> Ullrich Hafner &lt;hafner [at] bigfoot.de&gt; </p>
<h2>Index</h2>
