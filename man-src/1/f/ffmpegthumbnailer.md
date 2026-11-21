---

title: "ffmpegthumbnailer(1)"
name: "ffmpegthumbnailer"
section: "1"
letter: "f"
url: "/docs/linux/man/1-ffmpegthumbnailer/"
description: "ffmpegthumbnailer – fast and lightweight video thumbnailer"
---

<p> ffmpegthumbnailer &#8211; fast and lightweight video thumbnailer</p>
<h2>SYNOPSIS</h2>
<p> <code>ffmpegthumbnailer</code> [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> <i>Ffmpegthumbnailer</i> is a lightweight video thumbnailer that can be used by file managers to create thumbnails for your video files. The thumbnailer uses ffmpeg to decode frames from the video files, so supported videoformats depend on the configuration flags of ffmpeg.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i</code>&lt;s&gt;</dt>
<dd> : input file</dd>
<dt><code>-o</code>&lt;s&gt;</dt>
<dd> : output file</dd>
<dt><code>-s</code>&lt;n&gt;</dt>
<dd> : thumbnail size (use 0 for original size) (default: 128)</dd>
<dt><code>-q</code>&lt;n&gt;</dt>
<dd> : image quality (0 = bad, 10 = best) (default: 8) (only for jpeg)</dd>
<dt><code>-c</code>&lt;s&gt;</dt>
<dd> : override image format (jpeg or png) (default: determined by filename)</dd>
<dt><code>-t</code>&lt;n|s&gt;</dt>
<dd> : time to seek to (percentage or absolute time hh:mm:ss) (default: 10%)</dd>
<dt><code>-a</code></dt>
<dd> : ignore aspect ratio and generate square thumbnail</dd>
<dt>
</dt><dd> <code>-f</code> : create a movie strip overlay</dd>
<dt><code>-h</code></dt>
<dd> : display this help</dd></dl>
<h2>AUTHOR</h2>
<p> Written by Dirk Vanden Boer.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;<a rel="nofollow" href="http://code.google.com/p/ffmpegthumbnailer/issues/list">http://code.google.com/p/ffmpegthumbnailer/issues/list</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2008 Dirk Vanden Boer &lt;dirk.vdb [at] gmail.com&gt;<br />
 This is free software. You may redistribute copies of it under the terms of the GNU General Public License (version 2 or later) &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/gpl.html">http://www.gnu.org/licenses/gpl.html</a>&gt;. There is NO WARRANTY, to the extent permitted by law. </p>
