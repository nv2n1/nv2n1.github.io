---
title: "transcode_export(1)"
name: "transcode_export"
section: "1"
letter: "t"
url: "/docs/linux/man/1-transcode_export/"
description: "transcode – export modules collection"
---

<h2>NAME</h2>
<p> transcode &#8211; export modules collection</p>
<h2>SYNOPSIS</h2>
<p> <code>transcode -y module[,module[,module]] [other options]</code></p>
<h2>COPYRIGHT</h2>
<p> <code>transcode</code> is Copyright (C) 2001-2003 by Thomas Oestreich, 2003-2004 Tilmann Bitterberg, 2004-2010 Transcode Team</p>
<h2>ENCODER PARAMETERS STRING</h2>
<p> Module-dependent parameters can be passed to encoder using the -F <a href="/docs/linux/man/1-transcode/">transcode</a>(1) option: </p>
<dl>
<dt>
<dd> <code>transcode -F </code><i>codec_string</i></dl>
<p> Those parameters tune the general behaviour of the export module. More specific settings can fine-tune the export settings. Those settings are passed to export modules through <code>module options</code> or through the <code>module configuration file</code>; both configuration file and options can be present at same time: in that case, the options overrides the configuration file. Passing option strings to export modules is done like to pass options to filter modules: The syntax is: </p>
<dl>
<dt>
<dd> <code>transcode -y vmod=options,amod=options</code></dl>
<p> see <a href="/docs/linux/man/1-transcode_filter/">transcode_filter</a>(1) for full reference and examples. </p>
<p> The -F parameter has different meanings for different export modules, as documented on section below. </p>
<h2>ENCODER MODULES PARAMETERS</h2>
<dl>
<dt><i>ffmpeg</i>:</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>The codec String for the codec you want to encode. Example values are -F mpeg4 or -F mpeg1video or -F huffyuv. To get a list of valid codecs, use -F list </p>
<dt><i>im</i>:</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>The name of the image format you want to export. Example values are&nbsp;<wbr>&#8216;-F jpg&#8217;&nbsp;<wbr>(default)&nbsp;<wbr>or&nbsp;<wbr>&#8216;-F png&#8217;&nbsp;<wbr>or -F&nbsp;<wbr>&#8216;gif&#8217;. With -F jpg, -w gives quality in percent. With -F png, the first digit of -w gives compression level, the second one gives quality, so -w 95 selects best compression level&nbsp;<wbr>(9)&nbsp;<wbr>and 5 means PNG adaptive filtering. </p>
<dt><i>jpg</i>:</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>The quality of the JPEG encode in percent. Example values are&nbsp;<wbr>&#8216;-F 75&#8217;&nbsp;<wbr>(default)&nbsp;<wbr>or&nbsp;<wbr>&#8216;-F 100&#8217; </p>
<dt><i>mov</i>:</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>Syntax: -F&nbsp;<wbr>&quot;&lt;vcodec&gt;,&lt;acodec&gt;[,&lt;parameters&gt;]&quot;<br />
&nbsp;<wbr>&lt;vcodec&gt;&nbsp;<wbr>=&nbsp;<wbr>Videocodec to encode with. Default:&nbsp;<wbr>&quot;mjpa&quot;<br />
&nbsp;<wbr>&lt;acodec&gt;&nbsp;<wbr>=&nbsp;<wbr>Audiocodec to encode with. Default:&nbsp;<wbr>&quot;ima4&quot;<br />
&nbsp;<wbr>&lt;parameters&gt;&nbsp;<wbr>=&nbsp;<wbr>A comma seperated list of parameters<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>to be passed to the codec. </p>
<p> Note: You can use &quot;list&quot; instead of a video/audiocodec or parameter to get a list of supported options. </p>
<dt><i>mpeg</i>:</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>Syntax: -F&nbsp;<wbr>&quot;&lt;base-profile&gt;[,&lt;resizer-mode&gt;[,user-profile]]&quot;<br />
&nbsp;<wbr>&lt;base-profile&gt;&nbsp;<wbr>can be one of<br />
&#8216;1&#8217;&nbsp;<wbr>=&nbsp;<wbr>MPEG 1&nbsp;<wbr>(default)<br />
&#8216;b&#8217;&nbsp;<wbr>=&nbsp;<wbr>big MPEG 1&nbsp;<wbr>(experimental)<br />
&#8216;v&#8217;&nbsp;<wbr>=&nbsp;<wbr>VCD<br />
&#8216;s&#8217;&nbsp;<wbr>=&nbsp;<wbr>SVCD<br />
&#8216;2&#8217;&nbsp;<wbr>=&nbsp;<wbr>MPEG2<br />
&#8216;d&#8217;&nbsp;<wbr>=&nbsp;<wbr>DVD compliant<br />
&nbsp;<wbr>&lt;resizer-mode&gt;&nbsp;<wbr>can be one of<br />
&nbsp;<wbr>0&nbsp;<wbr>=&nbsp;<wbr>disable resizer&nbsp;<wbr>(default)<br />
&nbsp;<wbr>1&nbsp;<wbr>=&nbsp;<wbr>352&#215;288<br />
&nbsp;<wbr>2&nbsp;<wbr>=&nbsp;<wbr>480&#215;480<br />
&nbsp;<wbr>3&nbsp;<wbr>=&nbsp;<wbr>480&#215;576<br />
&nbsp;<wbr>4&nbsp;<wbr>=&nbsp;<wbr>352&#215;240<br />
&nbsp;<wbr>&lt;user-profile&gt;&nbsp;<wbr>is a filename of the profile file. You can either specify the absolute path to the file or if you transcode will look for it in the directory where you started transcode. </p>
<dt><i>mpeg2enc</i>:</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>Syntax: -F&nbsp;<wbr>&quot;&lt;base-profile&gt;[,&lt;options_string&gt;]&quot;<br />
&nbsp;<wbr>&lt;base-profile&gt;&nbsp;<wbr>can be one of<br />
&#8216;0&#8217;&nbsp;<wbr>=&nbsp;<wbr>Generic MPEG1&nbsp;<wbr>(default)<br />
&#8216;1&#8217;&nbsp;<wbr>=&nbsp;<wbr>Standard VCD<br />
&#8216;2&#8217;&nbsp;<wbr>=&nbsp;<wbr>User VCD<br />
&#8216;3&#8217;&nbsp;<wbr>=&nbsp;<wbr>Generic MPEG2<br />
&#8216;4&#8217;&nbsp;<wbr>=&nbsp;<wbr>Standard SVCD<br />
&#8216;5&#8217;&nbsp;<wbr>=&nbsp;<wbr>User SVCD<br />
&#8216;6&#8217;&nbsp;<wbr>=&nbsp;<wbr>Manual parameter mode<br />
&#8216;8&#8217;&nbsp;<wbr>=&nbsp;<wbr>DVD<br />
&nbsp;<wbr>&lt;options_string&gt;&nbsp;<wbr>will be passed down to mpeg2enc untouched by transcode. Have a look at the manpage for mpeg2enc. </p>
<dt><i>raw</i>:</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>The name of the image format to use for uncompressed video. Examples are I420&nbsp;<wbr>(YUV 4:2:0 planar), YV12&nbsp;<wbr>(the same thing with U and V reversed), or UYVY&nbsp;<wbr>(YUV 4:2:2 packed). Use&nbsp;<wbr>&quot;-F help&quot;&nbsp;<wbr>to get a list of formats. </p>
</dl>
<h2>EXPORT MODULES</h2>
<p> If no module is specified through the <i>-y</i> option, transcode will use the <i>null</i> module for both audio and video export. If a multiplex module is given, by giving <code>three</code> export module names instead the usual two, transcode will use the new-style encode/multiplex modules (still under development, see the encode and multiplex directories); if no multiplex module is given, the traditional export modules will be used.<br />
 To see what export modules are avalaible for your transcode installation, do a </p>
<dl>
<dt>
<dd> <code>ls -1 $( tcmodinfo -p )/export*.so</code></dl>
<p> A complete transcode installation has the following export modules:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>ac3</code> &#8211; (video) null | (audio) ac3</p>
<dd>
 This module has no compile-time dependencies. At run-time ffmpeg must be present. Support for this module is good.</p>
<dl>
<dt>
<dd> Encodes audio (raw PCM) to AC3 via the ffmpeg binary.<br />
 Supported processing formats: audio &#8211; PCM, video &#8211; none</dl>
<dt><code>af6</code> &#8211; (video) Win32 dll | (audio) MPEG/AC3/PCM</p>
<dd>
 At compile-time libavifile must be available. At run-time libavifile and win32codecs must be present. Support for this module is good.</p>
<dl>
<dt>
<dd> Interface to the avifile library which allows the use of win32codec on the linux-x86 platform.<br />
 Supported processing formats: audio &#8211; RAW (pass-through) PCM AC3, video &#8211; RGB YUV</dl>
<dt><code>divx5</code> &#8211; (video) DivX 5.xx | (audio) MPEG/AC3/PCM</p>
<dd>
 At compile-time libmp3lame (only for MPEG audio layer III) must be available. At run-time divx4linux (new) and libdivxencore.so must be present. Support for this module is good.</p>
<dl>
<dt>
<dd> Encodes MPEG4 video using the closed-source binaries from divx.com to an AVI container.<br />
 Supported processing formats: audio &#8211; RAW (pass-through) PCM AC3, video &#8211; RGB YUV</dl>
<dt><code>dv</code> &#8211; (video) Digital Video | (audio) MPEG/AC3/PCM</p>
<dd>
 At compile-time libdv and libmp3lame (only for MPEG audio layer III) must be available. At run-time libdv must be present. Support for this module is good.</p>
<dl>
<dt>
<dd> Encodes DV into an AVI container. DV is a codec developed by Sony and is often used in digital camcorders.<br />
 Supported processing formats: audio &#8211; PCM AC3, video &#8211; RGB YUV</dl>
<dt><code>dvraw</code> &#8211; (video) Digital Video | (audio) PCM</p>
<dd>
 At compile-time libdv must be available. At run-time libdv must be present. Support for this module is good.</p>
<dl>
<dt>
<dd> Encodes DV into a DV file. DV is a codec developed by Sony and is often used in digital camcorders. A raw DV file can be played back into the camcorder.<br />
 Supported processing formats: audio &#8211; PCM, video &#8211; RAW (pass-through) RGB YUV YUV422</dl>
<dt><code>ffmpeg</code> &#8211; (video) * | (audio) MPEG/AC3/PCM</p>
<dd>
 At compile-time libmp3lame (only for MPEG audio layer III) must be available. This module has no run-time dependencies. Support for this module is good.</p>
<dl>
<dt>
<dd> Encodes many different formats to both AVI and raw. Supported are mpeg1video, mpeg2video, mpeg4, mjpeg, h263, h263p, wmv1, wmv2, rv10, msmpeg4, msmpeg4v2, huffyuv and dvvideo.<br />
 Supported processing formats: audio RAW (pass-through) PCM AC3, video &#8211; RGB YUV YUV422</dl>
<dt><code>im</code> &#8211; (video) * | (audio) MPEG/AC3/PCM</p>
<dd>
 At compile-time libImageMagick must be available. This module has no run-time dependencies. Support for this module is good.</p>
<dl>
<dt>
<dd> Encodes image sequences by using the ImageMagick library. ImageMagick is able to handle a lot of different image formats such as png, jpg, miff, tiff, etc. Use -F to select the desired format.<br />
 Supported processing formats: audio &#8211; RAW (pass-through) PCM, video &#8211; RGB YUV</dl>
<dt><code>jpg</code> &#8211; (video) * | (audio) MPEG/AC3/PCM</p>
<dd>
 At compile-time libjpeg must be available. This module has no run-time dependencies. Support for this module is good.</p>
<dl>
<dt>
<dd> Encodes jpg image sequences using libjpeg. Faster than ImageMagick. Use -F to select the compression quality.<br />
 Supported processing formats: audio &#8211; RAW (pass-through) PCM, video &#8211; RGB YUV</dl>
<dt><code>lame</code> &#8211; (audio) MPEG 1/2</p>
<dd>
 At compile-time libmp3lame (only for MPEG audio layer III) must be available. At run-time lame and sox must be present. Support for this module is good.</p>
<dl>
<dt>
<dd> An audio-only encoder which drives the lame binary. The tool sox is used to do resampling if required. Encodes to a MP3 file.<br />
 Supported processing formats: audio &#8211; PCM, video &#8211; none</dl>
<dt><code>lzo</code> &#8211; (video) LZO real-time compression | (audio) MPEG/AC3/PCM</p>
<dd>
 At compile-time liblzo and libmp3lame (only for MPEG audio layer III) must be available. This module has no run-time dependencies. Support for this module is good.</p>
<dl>
<dt>
<dd> Encodes video using a loss-less real-time LZO codec. This codec is a homegrown invention of transcode and is intended as an intermediate storage format. MPlayer can playback LZO-based AVI files as well.<br />
 Supported processing formats: audio &#8211; RAW (pass-through) PCM AC3, video &#8211; RAW (pass-through) RGB YUV DV</dl>
<dt><code>mov</code> &#8211; (video) * | (audio) *</p>
<dd>
 At compile-time libquicktime must be available. At run-time libquicktime must be present. Support for this module is fair.</p>
<dl>
<dt>
<dd> Interface to the quicktime library.<br />
 Supported processing formats: audio &#8211; PCM, video &#8211; RAW (pass-through) RGB YUV YUV422 YUY2</dl>
<dt><code>mp2</code> &#8211; (video) null | (audio) MPEG 1/2</p>
<dd>
 This module has no compile-time dependencies. At run-time ffmpeg and sox must be present. Support for this module is good.</p>
<dl>
<dt>
<dd> Encodes audio (raw PCM) to MPEG 1 Layer 2 audio aka mp2. Additionaly it can change the speed of the audio stream by a factor you can specify. See docs/export_mp2.txt.<br />
 Supported processing formats: audio &#8211; PCM, video &#8211; none</dl>
<dt><code>mp2enc</code> &#8211; (audio) MPEG 1/2</p>
<dd>
 At compile-time mjpegtools must be available. At run-time mp2enc must be present. Support for this module is good.</p>
<dl>
<dt>
<dd> Drives the mp2enc binary and writes an MP2 (MPEG1-Layer2) file. Useful for when encoding to SVCD to be multiplexed with mplex after encoding.<br />
 Supported processing formats: audio &#8211; PCM, video &#8211; none</dl>
<dt><code>mpeg2enc</code> &#8211; (video) MPEG 1/2</p>
<dd>
 At compile-time mjpegtools must be available. At run-time mpeg2enc must be present. Support for this module is good.</p>
<dl>
<dt>
<dd> Drives the mpeg2enc binary. mpeg2enc is a very feature rich MPEG encoder, have a look at its manpage. Encodes generic mpeg1, VCD, SVCD, MPEG2 and DVD type video.<br />
 Supported processing formats: audio &#8211; none, video &#8211; RGB YUV</dl>
<dt><code>null</code> &#8211; (video) null | (audio) null</p>
<dd>
 This module has no compile-time dependencies. This module has no run-time dependencies. Support for this module is good.</p>
<dl>
<dt>
<dd> Data sink. Does nothing else than discarding data.<br />
 Supported processing formats: audio &#8211; none, video &#8211; none</dl>
<dt><code>ogg</code> &#8211; (video) null | (audio) ogg</p>
<dd>
 This module has no compile-time dependencies. At run-time oggenc must be present. Support for this module is good.</p>
<dl>
<dt>
<dd> Drives the oggenc binary. Encodes an Ogg/Vorbis file. Resamples.<br />
 Supported processing formats: audio &#8211; PCM, video &#8211; none</dl>
<dt><code>ppm</code> &#8211; (video) PPM/PGM | (audio) MPEG/AC3/PCM</p>
<dd>
 This module has no compile-time dependencies. This module has no run-time dependencies. Support for this module is good.</p>
<dl>
<dt>
<dd> Writes an image sequence of PGM or PPM files. PPM is an old format and there are several tools around to manipulate such files.<br />
 Supported processing formats: audio &#8211; RAW (pass-through) PCM AC3, video &#8211; RGB YUV</dl>
<dt><code>pvm</code> &#8211; (video) * | (audio) *</p>
<dd>
 At compile-time libpvm3 must be available. At run-time pvm must be present. Support for this module is good.</p>
<dl>
<dt>
<dd> Meta module. It allows transcode to be used in a PVM cluster. See docs/export_pvm.txt<br />
 Supported processing formats: audio &#8211; RAW (pass-through) PCM AC3, video &#8211; RAW (pass-through) RGB YUV DV YUV422 YUY2</dl>
<dt><code>raw</code> &#8211; (video) * | (audio) MPEG/AC3/PCM</p>
<dd>
 This module has no compile-time dependencies. This module has no run-time dependencies. Support for this module is good.</p>
<dl>
<dt>
<dd> Can write uncompressed streams to an AVI file as well as raw mpeg2 files in pass-through mode. The image format for uncompressed streams can be selected with -F (use -F help to see available formats).<br />
 Supported processing formats: audio &#8211; RAW (pass-through) PCM AC3, video &#8211; RAW (pass-through) RGB YUV DV YUV422</dl>
<dt><code>toolame</code> &#8211; (audio) MPEG 1/2</p>
<dd>
 This module has no compile-time dependencies. At run-time toolame and sox must be present. Support for this module is good.</p>
<dl>
<dt>
<dd> Drives the toolame binary to create MP2 audio tracks. Sox is used for resampling if requested.<br />
 Supported processing formats: audio &#8211; PCM, video &#8211; none</dl>
<dt><code>wav</code> &#8211; (audio) WAVE PCM</p>
<dd>
 This module has no compile-time dependencies. This module has no run-time dependencies. Support for this module is good.</p>
<dl>
<dt>
<dd> Creates WAVE PCM files with interleaved audio for stereo.<br />
 Supported processing formats: audio &#8211; PCM, video &#8211; RAW (pass-through) RGB YUV</dl>
<dt><code>xvid4</code> &#8211; (video) XviD 1.0.x series (aka API 4.0) | (audio) MPEG/AC3/PCM</p>
<dd>
 At compile-time libmp3lame (only for MPEG audio layer III) must be available. At run-time libxvidcore.so.4 must be present. Support for this module is good.</p>
<dl>
<dt>
<dd> Encodes MPEG4 video using the library available from xvid.org. Check out the library from xvidcvs using cvs -d :pserver:anonymous [at] cvs.xvid.org:/xvid co -rdev-api-4 xvidcore. There is also a tool available to create configuration files for this xvid version at <a rel="nofollow" href="http://zebra.fh-weingarten.de/transcode/xvid4conf.">http://zebra.fh-weingarten.de/transcode/xvid4conf.</a> The output can either be an AVI file or a MPEG4 elementary stream (with -F raw).<br />
 Supported processing formats: audio &#8211; RAW (pass-through) PCM AC3, video &#8211; RGB YUV YUV422</dl>
<dt><code>yuv4mpeg</code> &#8211; (video) YUV4MPEG2 | (audio) MPEG/AC3/PCM</p>
<dd>
 At compile-time mjpegtools must be available. This module has no run-time dependencies. Support for this module is good.</p>
<dl>
<dt>
<dd> Writes the uncompressed raw YUV data in a YUV4MPEG format as used by the lav* and mjpeg* tools.<br />
 Supported processing formats: audio &#8211; RAW (pass-through) PCM AC3, video &#8211; RGB YUV</dl>
</dl>
</dl>
<dl>
<dt>
<dd>
</dl>
<h2>AUTHORS</h2>
<p> <code>transcode</code> was written by Thomas Oestreich<br />
 &lt;ostreich [at] theorie.physik.uni-goettingen.de&gt; with contributions from many others. See AUTHORS for details. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-transcode/">transcode</a></code>(1), <code><a href="/docs/linux/man/1-tcmodinfo/">tcmodinfo</a></code>(1), <code><a href="/docs/linux/man/1-transcode_import/">transcode_import</a>(1),</code> <code><a href="/docs/linux/man/1-transcode_filter/">transcode_filter</a>(1),</code> </p>
<h2>Index</h2>
