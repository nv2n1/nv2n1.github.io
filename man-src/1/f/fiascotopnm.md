---
title: "fiascotopnm(1)"
name: "fiascotopnm"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fiascotopnm/"
description: "fiascotopnm – Convert compressed FIASCO image to PGM, or PPM"
---

<h2 class="name">NAME</h2>
<p> fiascotopnm &#8211; Convert compressed FIASCO image to PGM, or PPM</p>
<h2>SYNOPSIS</h2>
<p> <code>fiascotopnm </code> [<i>option</i>]&#8230; [<i>filename</i>]&#8230; </p>
<h2>DESCRIPTION</h2>
<p> <code>fiascotopnm</code> decompresses the named FIASCO files, or the Standard Input if no file is named, and writes the images as PGM, or PPM files, depending on whether the FIASCO image is black and white or color. </p>
<h2>OPTIONS</h2>
<p> All option names may be abbreviated; for example, &#8211;output may be written &#8211;outp or &#8211;ou. For all options an one letter short option is provided. Mandatory or optional arguments to long options are mandatory or optional for short options, too. Both short and long options are case sensitive. </p>
<dl>
<dt><code>-o</code>[<i>name</i>], <code>&#8211;output=</code>[<i>name</i>]</p>
<dd> Write decompressed image to the file <i>name</i>.ppm (if PPM) or <i>name</i>.pgm (if PGM). If <i>name</i>=- then produce the image file on the standard output. The optional argument <i>name</i> can be omitted, then the input filename is used as basename with the suffix .ppm or .pgm. In case of video streams, the frames are stored in the files <i>name</i>.<code>N</code>.ppm where <code>N</code> is the frame number (of the form 00..0 &#8211; 99..9); output on the standard output is not possible with video streams. </p>
<p> If <i>name</i> is a relative path and the environment variable <code>FIASCO_IMAGES</code> is a (colon-separated) list of directories, then the output file(s) are written to the first (writable) directory of this list. Otherwise, the current directory is used to store the output file(s). </p>
<dt><code>-z</code>, <code>&#8211;fast</code></p>
<dd> Decompress images in the 4:2:0 format; i.e., each chroma channel is decompressed to an image of halved width and height. Use this option on slow machines when the desired frame rate is not achieved; the output quality is only slightly decreased. </p>
<dt><code>-d</code>, <code>&#8211;double</code></p>
<dd> Double the size of the X11 window both in width and height; no pixel interpolation is used, each pixel is just replaced by four identical pixels.<br />
&nbsp;</p>
<dt><code>-p</code>, <code>&#8211;panel</code></p>
<dd> Show a panel with play, stop, pause, record and exit buttons to control the display of videos. When pressing the record button, all frames are decompressed and stored in memory. The other buttons work in the usual way.<br />
&nbsp;</p>
<dt><code>-m</code> <i>N</i>, <code>&#8211;magnify=</code><i>N</i></p>
<dd> Set magnification of the decompressed image. Positive values enlarge and negative values reduce the image width and height by a factor of 2^|<i>N</i>|. </p>
<dt><code>-s</code> <i>N</i>, <code>&#8211;smooth=</code><i>N</i></p>
<dd> Smooth decompressed image(s) along the partitioning borders by the given amount <i>N</i>. <i>N</i> is 1 (minimum) to 100 (maximum); default is 70. When <i>N</i>=0, then the smoothing amount specified in the FIASCO file is used (defined by the FIASCO coder). </p>
<dt><code>-F</code> <i>N</i>, <code>&#8211;fps=</code><i>N</i></p>
<dd> Set number of frames per second to <i>N</i>. When using this option, the frame rate specified in the FIASCO file is overridden. </p>
<dt><code>-v</code>, <code>&#8211;version</p>
<dd> Print fiascotopnm</code> version number, then exit. </p>
<dt><code>-f</code> <i>name</i>, <code>&#8211;config=</code><i>name</i></p>
<dd> Load parameter file <i>name</i> to initialize the options of <code>fiascotopnm</code>. See file <code>system.fiascorc </code> for an example of the syntax. Options of <code>fiascotopnm </code> are set by any of the following methods (in the specified order): </p>
<p> 1) Global ressource file <code>/etc/system.fiascorc</code> </p>
<p> 2) $HOME<code>/.fiascorc</code> </p>
<p> 3) command line </p>
<p> 4) &#8211;config=<i>name</i> </p>
<dt><code>-h</code>, <code>&#8211;info</p>
<dd> Print brief help, then exit. </p>
<dt>-H</code>, <code>&#8211;help</p>
<dd> Print detailed help, then exit. </p>
</dl>
<p> </code></p>
<h2>EXAMPLES</h2>
<dl>
<dt>fiascotopnm foo.wfa &gt;foo.ppm</p>
<dd> Decompress the FIASCO file &quot;foo.wfa&quot; and store it as &quot;foo.ppm&quot;. </p>
<dt>fiascotopnm -o foo1.wfa foo2.wfa</p>
<dd> Decompress the FIASCO files &quot;foo1.wfa&quot; and &quot;foo2.wfa&quot; and write the frames to the image files &quot;foo1.wfa.ppm&quot; and &quot;foo2.wfa.ppm&quot;. </p>
<dt>fiascotopnm -oimage foo1.wfa</p>
<dd> Decompress the FIASCO file &quot;foo1.wfa&quot; and write all 15 frames to the image files &quot;image.00.ppm&quot;, &#8230; , &quot;image.14.ppm&quot;. </p>
<dt>fiascotopnm &#8211;fast &#8211;magnify=-1 &#8211;double video.wfa &gt;stream.ppm</p>
<dd> Decompress the FIASCO file &quot;video.wfa&quot;. The decompression speed is as fast as possible: the image is decompressed (in 4:2:0 format) at a quarter of its original size; then the image is enlarged again by pixel doubling. </p>
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
<dd> Save path for image files. Default is &quot;./&quot;.</p>
<dt><code>FIASCO_DATA</code></p>
<dd> Search path for FIASCO files. Default is &quot;./&quot;. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pnmtofiasco/">pnmtofiasco</a></code>(1), <code><a href="/docs/linux/man/5-pnm/">pnm</a></code>(5) </p>
<p> Ullrich Hafner, Juergen Albert, Stefan Frank, and Michael Unger. <code>Weighted Finite Automata for Video Compression</code>, IEEE Journal on Selected Areas In Communications, January 1998<br />
 Ullrich Hafner. <code>Low Bit-Rate Image and Video Coding with Weighted Finite Automata</code>, Ph.D. thesis, Mensch &amp; Buch Verlag, ISBN 3-89820-002-7, October 1999. </p>
<h2>AUTHOR</h2>
<p> Ullrich Hafner &lt;hafner [at] bigfoot.de&gt; </p>
<h2>Index</h2>
