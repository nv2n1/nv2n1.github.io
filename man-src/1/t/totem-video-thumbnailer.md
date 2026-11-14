---
title: "totem-video-thumbnailer(1)"
name: "totem-video-thumbnailer"
section: "1"
letter: "t"
url: "/docs/linux/man/1-totem-video-thumbnailer/"
description: "totem-video-thumbnailer – video thumbnailer for the GNOME desktop"
---

<h2 class="name">NAME</h2>
<p> totem-video-thumbnailer &#8211; video thumbnailer for the GNOME desktop </p>
<h2>SYNOPSYS</h2>
<p> <code>totem-video-thumbnailer</code> [-j|&#8211;jpeg] [-l|&#8211;no-limit] [-s size] input output [backend options]</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>totem-video-thumbnailer</code> command. This manual page was written for the Debian Project because the original program does not have a manual page. </p>
<p> <code>totem-video-thumbnailer</code> is used internally by <font SIZE="-1">GNOME</font> applications such as <code>nautilus</code> to generate <font SIZE="-1">PNG</font> thumbnails of video files. While it is possible to invoke it manually, it is usually done automatically by <code>nautilus</code>.</p>
<h2>ARGUMENTS</h2>
<dl>
<dt><code>input</code></p>
<dd> The input filename. This can be in any format that <code>totem</code> can play.</p>
<dt><code>output</code></p>
<dd> The output filename, output in <font SIZE="-1">PNG</font> format.</p>
<dt><code>backend options</code></p>
<dd> Options to be passed to the backend (i.e. <code>gstreamer</code>).</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-j</code> <code>&#8211;jpeg</code></p>
<dd> Switch the output format to <font SIZE="-1">JPEG.</font> The default is <font SIZE="-1">PNG.</font></p>
<dt><code>-l</code> <code>&#8211;no-limit</code></p>
<dd> Don&#8217;t limit the thumbnailing time to 30 seconds. For debugging purposes.</p>
<dt><code>-s size</code></p>
<dd> The size of the thumbnail. Example: &#8220;64&#215;64&#8221;. The default is &#8220;128&#215;96&#8221;.</dl>
<h2>AUTHOR</h2>
<p> <code>totem-video-thumbnailer</code> was written by Bastien Nocera &lt;hadess [at] hadess.net&gt;. </p>
<p> This manual page was written by Zack Cerza &lt;zcerza [at] coe.neu.edu&gt; for the Debian Project (but may be used by others).</p>
<h2>SEE ALSO</h2>
<dl>
<dt><code>totem</code>, <code>nautilus</code></p>
<dd>
</dl>
<h2>Index</h2>
