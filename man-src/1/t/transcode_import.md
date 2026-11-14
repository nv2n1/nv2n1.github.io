---
title: "transcode_import(1)"
name: "transcode_import"
section: "1"
letter: "t"
url: "/docs/linux/man/1-transcode_import/"
description: "transcode_import – transcode import modules collection"
---

<h2 class="name">NAME</h2>
<p> transcode_import &#8211; transcode import modules collection </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>transcode</code> -x&nbsp;<wbr><i>name</i>&nbsp;<wbr>[&nbsp;<wbr><i>,name</i>&nbsp;<wbr>] [<i>other options</i>]</dl>
<h2>COPYRIGHT</h2>
<p> <code>transcode</code></p>
<dd>is Copyright (C) 2001-2003 by Thomas Oestreich, 2003-2004 Tilmann Bitterberg, 2004-2010 Transcode Team</p>
<h2>IMPORT MODULES</h2>
<p> If no module is specified through the -x option, <code>transcode</code> will autodetect them using internal probing code. If just one import module is specified, it is used both for video and audio import; if both modules are specified, the first is used for video import, the second for audio import. To see what import modules are avalaible for your transcode installation, do a </p>
<dl>
<dt>
<dd>
<pre>
           $ ls -1 $( tcmodinfo -p )/import*.so
           
</pre>
</dl>
<p> A complete transcode installation has the following import modules. </p>
<p> <code>alsa</code> <i></i></p>
<dl>
<dt>
<dd> This module reads audio samples from an ALSA device using libalsa. </p>
<p> This module accepts the following options: </p>
<p> device (string)</p>
<dl>
<dt>
<dd> selects ALSA device to use for capturing audio.</dl>
</dl>
<p> <code>bktr</code> <i></i></p>
<dl>
<dt>
<dd> This module reads video frames from an capture device using bktr module. This module is designed to work on *BSD. For linux, use the v4l module. </p>
<p> This module accepts the following options: </p>
<p> tunerdev (string)</p>
<dl>
<dt>
<dd> help: selects tuner device.</dl>
<p> vsource (string)</p>
<dl>
<dt>
<dd> selects video source (device dependant input).</dl>
<p> format (string)</p>
<dl>
<dt>
<dd> selects video normalization.</dl>
<p> asource (string)</p>
<dl>
<dt>
<dd> selects audio source (device dependant input).</dl>
</dl>
<p> <code>dvd</code> <i></i></p>
<dl>
<dt>
<dd> This module provides access to DVD content using libdvdread, directly from DVD device. (e.g. on-the-fly operation, no intermediate disk storage needed). </p>
<p> At run time, this module requires: libdvdread &gt;= 0.9.3 </p>
<p> This module accepts the following options: </p>
<p> delay (integer)</p>
<dl>
<dt>
<dd> set device access delay (seconds).</dl>
</dl>
<p> <code>im</code> <i></i></p>
<dl>
<dt>
<dd> This module reads single images from disk using ImageMagick; a stream of correlated images can be automatically read if their filenames contains a common prefix and a serial number. All formats supported by ImageMagick are supported as well. </p>
<p> At run time, this module requires: libMagick &gt;= 6.2.4.0 </p>
<p> This module accepts the following options: </p>
<p> noseq (flag)</p>
<dl>
<dt>
<dd> disable internal auto loading of images with similar names.</dl>
</dl>
<p> <code>pv3</code> <i></i></p>
<dl>
<dt>
<dd> This module provides access to Earth Soft PV3 audio/video streams using win32 binary codecs and an internal win32 emulation layer (NO wine needed). </p>
<p> At run time, this module requires: PV3 win32 dlls. </p>
<p> This module accepts the following options: </p>
<p> dllpath (string)</p>
<dl>
<dt>
<dd> set path/filename to load dv.dll from</dl>
</dl>
<p> <code>vag</code> <i></i></p>
<dl>
<dt>
<dd> This module decodes VAG-format audio (from PlayStation). </p>
<p> This module accepts the following options: </p>
<p> blocksize (integer)</p>
<dl>
<dt>
<dd> stereo blocking size.</dl>
</dl>
<p> <code>vob</code> <i></i></p>
<dl>
<dt>
<dd> This module imports audio/video from VOB files. If you need direct DVD access, use import_dvd module. </p>
<p> This module accepts the following options: </p>
<p> nodemux (flag)</p>
<dl>
<dt>
<dd> skip demuxing processing stage. This sometimes improves A/V sync.</dl>
</dl>
<p> <code>x11</code> <i></i></p>
<dl>
<dt>
<dd> This module captures video frames from X window system using libX11. </p>
<p> At run time, this module requires: libcx11-6 &gt;= 1.0.0 </p>
<p> This module accepts the following options: </p>
<p> skew_limit (integer)</p>
<dl>
<dt>
<dd> maximum frame A/V skew (ms) before correction attempt</dl>
</dl>
<p> <code>v4l2</code> <i></i></p>
<dl>
<dt>
<dd> This module allow to capture video frames through a V4L2 (V4L api version 2) device. While audio capturing is possible, this kind of usage is discouraged in favour of OSS or ALSA import modules. </p>
<p> This module accepts the following options: </p>
<p> overrun_guard (integer)</p>
<dl>
<dt>
<dd> flag (default off). Toggles the buffer overrun guard, that prevents crash when capture buffers are full.</dl>
<p> resync_margin (integer)</p>
<dl>
<dt>
<dd> threshold audio/video desync (in frames) that triggers resync once reached.</dl>
<p> crop (string)</p>
<dl>
<dt>
<dd> forces cropping into selected window (format: WIDTHxHEIGHT+LEFTxTOP)</dl>
<p> resync_interval (integer)</p>
<dl>
<dt>
<dd> checks the resync_margin every given amount of frames.</dl>
<p> format (integer)</p>
<dl>
<dt>
<dd> forces video frames convertion by using index; use -1 to get a list of supported conversions.</dl>
<p> format (string)</p>
<dl>
<dt>
<dd> forces output format to given one; use &quot;list&quot; to get a list of supported formats.</dl>
<p> convert (integer)</p>
<dl>
<dt>
<dd> forces video frames convertion by using index; use -1 to get a list of supported conversions.</dl>
</dl>
<h2>AUTHORS</h2>
<p> Written by Thomas Oestreich &lt;ostreich [at] theorie.physik.uni-goettingen.de&gt;, Tilmann Bitterberg and the Transcode-Team </p>
<p> See the <i>AUTHORS</i> file for details.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-transcode/">transcode</a></code>(1) , <code><a href="/docs/linux/man/1-tcmodinfo/">tcmodinfo</a></code>(1) , <code><a href="/docs/linux/man/1-transcode_filter/">transcode_filter</a></code>(1) , <code><a href="/docs/linux/man/1-transcode_export/">transcode_export</a></code>(1) </p>
<h2>Index</h2>
