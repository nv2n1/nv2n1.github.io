---

title: "totem-video-thumbnailer(1)"
name: "totem-video-thumbnailer"
section: "1"
letter: "t"
url: "/docs/linux/man/1-totem-video-thumbnailer/"
description: "totem-video-thumbnailer – video thumbnailer for the GNOME desktop"
---

<p> totem-video-thumbnailer &#8211; video thumbnailer for the GNOME desktop </p>
<h2>SYNOPSYS</h2>
<p> <code>totem-video-thumbnailer</code> [-j|&#8211;jpeg] [-l|&#8211;no-limit] [-s size] input output [backend options]</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>totem-video-thumbnailer</code> command. This manual page was written for the Debian Project because the original program does not have a manual page. </p>
<p> <code>totem-video-thumbnailer</code> is used internally by GNOME applications such as <code>nautilus</code> to generate PNG thumbnails of video files. While it is possible to invoke it manually, it is usually done automatically by <code>nautilus</code>.</p>
<h2>ARGUMENTS</h2>
<dl>
<dt><code>input</code></dt>
<dd> The input filename. This can be in any format that <code>totem</code> can play.</dd>
<dt><code>output</code></dt>
<dd> The output filename, output in PNG format.</dd>
<dt><code>backend options</code></dt>
<dd> Options to be passed to the backend (i.e. <code>gstreamer</code>).</dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-j</code> <code>&#8211;jpeg</code></dt>
<dd> Switch the output format to JPEG. The default is PNG.</dd>
<dt><code>-l</code> <code>&#8211;no-limit</code></dt>
<dd> Don&#8217;t limit the thumbnailing time to 30 seconds. For debugging purposes.</dd>
<dt><code>-s size</code></dt>
<dd> The size of the thumbnail. Example: &#8220;64&#215;64&#8221;. The default is &#8220;128&#215;96&#8221;.</dd></dl>
<h2>AUTHOR</h2>
<p> <code>totem-video-thumbnailer</code> was written by Bastien Nocera &lt;hadess [at] hadess.net&gt;. </p>
<p> This manual page was written by Zack Cerza &lt;zcerza [at] coe.neu.edu&gt; for the Debian Project (but may be used by others).</p>
<h2>SEE ALSO</h2>
<dl>
<dt><code>totem</code>, <code>nautilus</code></dt>
<dd>
</dd></dl>
