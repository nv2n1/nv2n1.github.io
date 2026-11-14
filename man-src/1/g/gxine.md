---
title: "gxine(1)"
name: "gxine"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gxine/"
description: "gxine – a GTK/GNOME frontend to the xine video player"
---

<h2>NAME</h2>
<p> gxine &#8211; a GTK/GNOME frontend to the xine video player </p>
<h2>SYNOPSIS</h2>
<p> <code>gxine</code> [<i>options</i>] [<i>files or MRLs</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>gxine</code> plays MPEG system (audio and video) streams, MPEG elementary streams (e.g. .mp3, .mpa or .mpv files), MPEG transport streams, AVI files, ASF files, Quicktime files, (S)VCDs and DVDs &#8211; anything which xine-lib can handle. </p>
<p> Typical usage looks like</p>
<dl>
<dt>
<dd> <code>gxine some.mpg</code><br />
 <code>gxine -f dvd://</code><br />
 <code>gxine <a href="dvd://home/user/dvd/my.iso">dvd://home/user/dvd/my.iso</a></code></dl>
<p> Some directories and file names are not treated as ordinary files. They are:</p>
<dl>
<dt><code>DVD</code></p>
<dd> A directory containing a DVD filesystem structure; or a UDF filesystem image, identified by file name (&#8220;*.iso&#8221;).</p>
<dt><code>VCD</code></p>
<dd> A cue file, identified by file name.</dl>
<p> You can override this by using <code>file://full/path/to/file</code>. </p>
<h2>OPTIONS</h2>
<p> <code>-A</code><i>&nbsp;<wbr>audio_driver</i><br />
 <code>&#8211;audio</code><i>&nbsp;<wbr>audio_driver</i></p>
<dl>
<dt>
<dd> Select which libxine audio driver to use. This setting is not permanent, but it does prevent selection of other drivers via the preferences window.</dl>
<p> <code>-V</code><i>&nbsp;<wbr>video_driver</i><br />
 <code>&#8211;video</code><i>&nbsp;<wbr>video_driver</i></p>
<dl>
<dt>
<dd> Select which libxine video driver to use. This setting is not permanent, but it does prevent selection of other drivers via the preferences window.</dl>
<p> <code>-S</code><br />
 <code>&#8211;no-splash</code></p>
<dl>
<dt>
<dd> Don&#8217;t show the splash window during startup.</dl>
<p> <code>-a</code><br />
 <code>&#8211;add</code></p>
<dl>
<dt>
<dd> Don&#8217;t clear the playlist before adding any MRLs; start playing the first new MRL.</dl>
<p> <code>-e</code><br />
 <code>&#8211;enqueue</code></p>
<dl>
<dt>
<dd> Don&#8217;t clear the playlist before adding any MRLs; don&#8217;t start playing the first new MRL.</dl>
<p> <code>-f</code><br />
 <code>&#8211;full-screen</code></p>
<dl>
<dt>
<dd> Start in full-screen mode.</dl>
<p> <code>-c</code><i>&nbsp;<wbr>Javascript</i><br />
 <code>&#8211;command</code><i>&nbsp;<wbr>Javascript</i></p>
<dl>
<dt>
<dd> Javascript command(s) to be executed immediately after starting up.</dl>
<p> <code>-C</code><i>&nbsp;<wbr>KEY=VALUE</i><br />
 <code>&#8211;configure</code><i>&nbsp;<wbr>KEY=VALUE</i></p>
<dl>
<dt>
<dd> Set configuration item KEY to VALUE, e.g. &#8220;-c gui.window_size=100%&#8221;.</dl>
<p> <code>-v</code><br />
 <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Verbose mode: output information about plugins, the video stream, commands executed etc. Repeat for more verbosity.</dl>
<h2>FEATURES</h2>
<p> There are a couple of features which aren&#8217;t immediately obvious: in full-screen mode, you can right-click to get access to the menus, or middle-click to show or hide the player controls. </p>
<h2>SEE ALSO</h2>
<p> <i><a rel="nofollow" href="http://www.xine-project.org/,">http://www.xine-project.org/,</a></i> <code><a href="/docs/linux/man/1-xine/">xine</a></code>(1), <code><a href="/docs/linux/man/1-totem/">totem</a></code>(1), <code><a href="/docs/linux/man/1-kaffeine/">kaffeine</a></code>(1).<br />
 <code><a href="/docs/linux/man/5-xine/">xine</a></code>(5) for MRL syntax documentation (libxine &gt;= 1.0.2). </p>
<h2>AUTHOR</h2>
<p> This manual page was written by Darren Salt &lt;linux [at] youmustbejoking.demon.co.uk&gt;. It is based on an older version written by Philipp Matthias Hahn &lt;pmhahn [at] titan.lahn.de&gt; for Debian. </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001-2006 The xine project </p>
<h2>Index</h2>
