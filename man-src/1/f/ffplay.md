---
title: "ffplay(1)"
name: "ffplay"
section: "1"
letter: "f"
url: "/docs/linux/man/1-ffplay/"
description: "ffplay – FFplay media player"
---

<h2 class="name">NAME</h2>
<p> ffplay &#8211; FFplay media player </p>
<h2>SYNOPSIS</h2>
<p> ffplay [<i>options</i>] [<i>input_url</i>]</p>
<h2>DESCRIPTION</h2>
<p> FFplay is a very simple and portable media player using the FFmpeg libraries and the <font SIZE="-1">SDL</font> library. It is mostly used as a testbed for the various FFmpeg APIs.</p>
<h2>OPTIONS</h2>
<p> All the numerical options, if not specified otherwise, accept a string representing a number as input, which may be followed by one of the <font SIZE="-1">SI</font> unit prefixes, for example: &#8216;K&#8217;, &#8216;M&#8217;, or &#8216;G&#8217;. </p>
<p> If &#8216;i&#8217; is appended to the <font SIZE="-1">SI</font> unit prefix, the complete prefix will be interpreted as a unit prefix for binary multiples, which are based on powers of 1024 instead of powers of 1000. Appending &#8216;B&#8217; to the <font SIZE="-1">SI</font> unit prefix multiplies the value by 8. This allows using, for example: &#8216;<font SIZE="-1">KB</font>&#8216;, &#8216;MiB&#8217;, &#8216;G&#8217; and &#8216;B&#8217; as number suffixes. </p>
<p> Options which do not take arguments are boolean options, and set the corresponding value to true. They can be set to false by prefixing the option name with &#8220;no&#8221;. For example using &#8220;-nofoo&#8221; will set the boolean option with name &#8220;foo&#8221; to false.</p>
<h3>Stream specifiers</h3>
<p> Some options are applied per-stream, e.g. bitrate or codec. Stream specifiers are used to precisely specify which stream(s) a given option belongs to. </p>
<p> A stream specifier is a string generally appended to the option name and separated from it by a colon. E.g. <tt>&quot;-codec:a:1 ac3&quot;</tt> contains the <tt>&quot;a:1&quot;</tt> stream specifier, which matches the second audio stream. Therefore, it would select the ac3 codec for the second audio stream. </p>
<p> A stream specifier can match several streams, so that the option is applied to all of them. E.g. the stream specifier in <tt>&quot;-b:a 128k&quot;</tt> matches all audio streams. </p>
<p> An empty stream specifier matches all streams. For example, <tt>&quot;-codec copy&quot;</tt> or <tt>&quot;-codec: copy&quot;</tt> would copy all the streams without reencoding. </p>
<p> Possible forms of stream specifiers are:</p>
<dl>
<dt><i>stream_index</i></p>
<dd> Matches the stream with this index. E.g. <tt>&quot;-threads:1 4&quot;</tt> would set the thread count for the second stream to 4. If <i>stream_index</i> is used as an additional stream specifier (see below), then it selects stream number <i>stream_index</i> from the matching streams. Stream numbering is based on the order of the streams as detected by libavformat except when a program <font SIZE="-1">ID</font> is also specified. In this case it is based on the ordering of the streams in the program.</p>
<dt><i>stream_type</i><code>[:</code><i>additional_stream_specifier</i><code>]</code></p>
<dd> <i>stream_type</i> is one of following: &#8216;v&#8217; or &#8216;V&#8217; for video, &#8216;a&#8217; for audio, &#8216;s&#8217; for subtitle, &#8216;d&#8217; for data, and &#8216;t&#8217; for attachments. &#8216;v&#8217; matches all video streams, &#8216;V&#8217; only matches video streams which are not attached pictures, video thumbnails or cover arts. If <i>additional_stream_specifier</i> is used, then it matches streams which both have this type and match the <i>additional_stream_specifier</i>. Otherwise, it matches all streams of the specified type.</p>
<dt><code>p:</code><i>program_id</i><code>[:</code><i>additional_stream_specifier</i><code>]</code></p>
<dd> Matches streams which are in the program with the id <i>program_id</i>. If <i>additional_stream_specifier</i> is used, then it matches streams which both are part of the program and match the <i>additional_stream_specifier</i>.</p>
<dt><code>#</code><i>stream_id</i> <code>or i:</code><i>stream_id</i></p>
<dd> Match the stream by stream id (e.g. <font SIZE="-1">PID</font> in MPEG-TS container).</p>
<dt><code>m:</code><i>key</i><code>[:</code><i>value</i><code>]</code></p>
<dd> Matches streams with the metadata tag <i>key</i> having the specified value. If <i>value</i> is not given, matches streams that contain the given tag with any value.</p>
<dt><code>u</code></p>
<dd> Matches streams with usable configuration, the codec must be defined and the essential information such as video dimension or audio sample rate must be present. </p>
<p> Note that in <code>ffmpeg</code>, matching by metadata will only work properly for input files.</dl>
<h3>Generic options</h3>
<p> These options are shared amongst the ff* tools.</p>
<dl>
<dt><code>-L</code></p>
<dd> Show license.</p>
<dt><code>-h, -?, -help, &#8211;help [</code><i>arg</i><code>]</code></p>
<dd> Show help. An optional parameter may be specified to print help about a specific item. If no argument is specified, only basic (non advanced) tool options are shown. </p>
<p> Possible values of <i>arg</i> are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>long</code></p>
<dd> Print advanced tool options in addition to the basic tool options.</p>
<dt><code>full</code></p>
<dd> Print complete list of options, including shared and private options for encoders, decoders, demuxers, muxers, filters, etc.</p>
<dt><code>decoder=</code><i>decoder_name</i></p>
<dd> Print detailed information about the decoder named <i>decoder_name</i>. Use the <code>-decoders</code> option to get a list of all decoders.</p>
<dt><code>encoder=</code><i>encoder_name</i></p>
<dd> Print detailed information about the encoder named <i>encoder_name</i>. Use the <code>-encoders</code> option to get a list of all encoders.</p>
<dt><code>demuxer=</code><i>demuxer_name</i></p>
<dd> Print detailed information about the demuxer named <i>demuxer_name</i>. Use the <code>-formats</code> option to get a list of all demuxers and muxers.</p>
<dt><code>muxer=</code><i>muxer_name</i></p>
<dd> Print detailed information about the muxer named <i>muxer_name</i>. Use the <code>-formats</code> option to get a list of all muxers and demuxers.</p>
<dt><code>filter=</code><i>filter_name</i></p>
<dd> Print detailed information about the filter named <i>filter_name</i>. Use the <code>-filters</code> option to get a list of all filters.</p>
<dt><code>bsf=</code><i>bitstream_filter_name</i></p>
<dd> Print detailed information about the bitstream filter named <i>bitstream_filter_name</i>. Use the <code>-bsfs</code> option to get a list of all bitstream filters.</p>
<dt><code>protocol=</code><i>protocol_name</i></p>
<dd> Print detailed information about the protocol named <i>protocol_name</i>. Use the <code>-protocols</code> option to get a list of all protocols.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-version</code></p>
<dd> Show version.</p>
<dt><code>-buildconf</code></p>
<dd> Show the build configuration, one option per line.</p>
<dt><code>-formats</code></p>
<dd> Show available formats (including devices).</p>
<dt><code>-demuxers</code></p>
<dd> Show available demuxers.</p>
<dt><code>-muxers</code></p>
<dd> Show available muxers.</p>
<dt><code>-devices</code></p>
<dd> Show available devices.</p>
<dt><code>-codecs</code></p>
<dd> Show all codecs known to libavcodec. </p>
<p> Note that the term &#8216;codec&#8217; is used throughout this documentation as a shortcut for what is more correctly called a media bitstream format.</p>
<dt><code>-decoders</code></p>
<dd> Show available decoders.</p>
<dt><code>-encoders</code></p>
<dd> Show all available encoders.</p>
<dt><code>-bsfs</code></p>
<dd> Show available bitstream filters.</p>
<dt><code>-protocols</code></p>
<dd> Show available protocols.</p>
<dt><code>-filters</code></p>
<dd> Show available libavfilter filters.</p>
<dt><code>-pix_fmts</code></p>
<dd> Show available pixel formats.</p>
<dt><code>-sample_fmts</code></p>
<dd> Show available sample formats.</p>
<dt><code>-layouts</code></p>
<dd> Show channel names and standard channel layouts.</p>
<dt><code>-colors</code></p>
<dd> Show recognized color names.</p>
<dt><code>-sources</code> <i>device</i><code>[,</code><i>opt1</i><code>=</code><i>val1</i><code>[,</code><i>opt2</i><code>=</code><i>val2</i><code>]&#8230;]</code></p>
<dd> Show autodetected sources of the input device. Some devices may provide system-dependent source names that cannot be autodetected. The returned list cannot be assumed to be always complete. </p>
<pre>
        ffmpeg -sources pulse,server=192.168.0.4
</pre>
<dt><code>-sinks</code> <i>device</i><code>[,</code><i>opt1</i><code>=</code><i>val1</i><code>[,</code><i>opt2</i><code>=</code><i>val2</i><code>]&#8230;]</code></p>
<dd> Show autodetected sinks of the output device. Some devices may provide system-dependent sink names that cannot be autodetected. The returned list cannot be assumed to be always complete. </p>
<pre>
        ffmpeg -sinks pulse,server=192.168.0.4
</pre>
<dt><code>-loglevel [</code><i>flags</i><code>+]</code><i>loglevel</i> <code>| -v [</code><i>flags</i><code>+]</code><i>loglevel</i></p>
<dd> Set logging level and flags used by the library. </p>
<p> The optional <i>flags</i> prefix can consist of the following values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>repeat</code></p>
<dd> Indicates that repeated log output should not be compressed to the first line and the &#8220;Last message repeated n times&#8221; line will be omitted.</p>
<dt><code>level</code></p>
<dd> Indicates that log output should add a <tt>&quot;[level]&quot;</tt> prefix to each message line. This can be used as an alternative to log coloring, e.g. when dumping the log to file.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Flags can also be used alone by adding a &#8216;+&#8217;/&#8217;-&#8216; prefix to set/reset a single flag without affecting other <i>flags</i> or changing <i>loglevel</i>. When setting both <i>flags</i> and <i>loglevel</i>, a &#8216;+&#8217; separator is expected between the last <i>flags</i> value and before <i>loglevel</i>. </p>
<p> <i>loglevel</i> is a string or a number containing one of the following values:</p>
<dl>
<dt><code>quiet, -8</code></p>
<dd> Show nothing at all; be silent.</p>
<dt><code>panic, 0</code></p>
<dd> Only show fatal errors which could lead the process to crash, such as an assertion failure. This is not currently used for anything.</p>
<dt><code>fatal, 8</code></p>
<dd> Only show fatal errors. These are errors after which the process absolutely cannot continue.</p>
<dt><code>error, 16</code></p>
<dd> Show all errors, including ones which can be recovered from.</p>
<dt><code>warning, 24</code></p>
<dd> Show all warnings and errors. Any message related to possibly incorrect or unexpected events will be shown.</p>
<dt><code>info, 32</code></p>
<dd> Show informative messages during processing. This is in addition to warnings and errors. This is the default value.</p>
<dt><code>verbose, 40</code></p>
<dd> Same as <tt>&quot;info&quot;</tt>, except more verbose.</p>
<dt><code>debug, 48</code></p>
<dd> Show everything, including debugging information.</p>
<dt><code>trace, 56</code></p>
<dd></dl>
</dl>
<dl>
<dt>
<dd>
<p> For example to enable repeated log output, add the <tt>&quot;level&quot;</tt> prefix, and set <i>loglevel</i> to <tt>&quot;verbose&quot;</tt>: </p>
<pre>
        ffmpeg -loglevel repeat+level+verbose -i input output
</pre>
<p> Another example that enables repeated log output without affecting current state of <tt>&quot;level&quot;</tt> prefix flag or <i>loglevel</i>: </p>
<pre>
        ffmpeg [...] -loglevel +repeat
</pre>
<p> By default the program logs to stderr. If coloring is supported by the terminal, colors are used to mark errors and warnings. Log coloring can be disabled setting the environment variable <font SIZE="-1"><code>AV_LOG_FORCE_NOCOLOR</code></font>, or can be forced setting the environment variable <font SIZE="-1"><code>AV_LOG_FORCE_COLOR</code></font>.</dl>
<dt><code>-report</code></p>
<dd> Dump full command line and log output to a file named <tt>&quot;</tt>program<tt>-</tt>YYYYMMDD<tt>-</tt>HHMMSS<tt>.log&quot;</tt> in the current directory. This file can be useful for bug reports. It also implies <tt>&quot;-loglevel debug&quot;</tt>. </p>
<p> Setting the environment variable <font SIZE="-1"><code>FFREPORT</code></font> to any value has the same effect. If the value is a &#8216;:&#8217;-separated key=value sequence, these options will affect the report; option values must be escaped if they contain special characters or the options delimiter &#8216;:&#8217; (see the &#8220;Quoting and escaping&#8221; section in the ffmpeg-utils manual). </p>
<p> The following options are recognized:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>file</code></p>
<dd> set the file name to use for the report; <tt>%p</tt> is expanded to the name of the program, <tt>%t</tt> is expanded to a timestamp, <tt>&quot;%%&quot;</tt> is expanded to a plain <tt>&quot;%&quot;</tt></p>
<dt><code>level</code></p>
<dd> set the log verbosity level using a numerical value (see <tt>&quot;-loglevel&quot;</tt>).</dl>
</dl>
<dl>
<dt>
<dd>
<p> For example, to output a report to a file named <i>ffreport.log</i> using a log level of <tt>32</tt> (alias for log level <tt>&quot;info&quot;</tt>): </p>
<pre>
        FFREPORT=file=ffreport.log:level=32 ffmpeg -i input output
</pre>
<p> Errors in parsing the environment variable are not fatal, and will not appear in the report.</dl>
<dt><code>-hide_banner</code></p>
<dd> Suppress printing banner. </p>
<p> All FFmpeg tools will normally show a copyright notice, build options and library versions. This option can be used to suppress printing this information.</p>
<dt><code>-cpuflags flags (</code><i>global</i><code>)</code></p>
<dd> Allows setting and clearing cpu flags. This option is intended for testing. Do not use it unless you know what you&#8217;re doing. </p>
<pre>
        ffmpeg -cpuflags -sse+mmx ...
        ffmpeg -cpuflags mmx ...
        ffmpeg -cpuflags 0 ...
</pre>
<p> Possible flags for this option are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>x86</code></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>mmx</code></p>
<dd>
<dt><code>mmxext</code></p>
<dd>
<dt><code>sse</code></p>
<dd>
<dt><code>sse2</code></p>
<dd>
<dt><code>sse2slow</code></p>
<dd>
<dt><code>sse3</code></p>
<dd>
<dt><code>sse3slow</code></p>
<dd>
<dt><code>ssse3</code></p>
<dd>
<dt><code>atom</code></p>
<dd>
<dt><code>sse4.1</code></p>
<dd>
<dt><code>sse4.2</code></p>
<dd>
<dt><code>avx</code></p>
<dd>
<dt><code>avx2</code></p>
<dd>
<dt><code>xop</code></p>
<dd>
<dt><code>fma3</code></p>
<dd>
<dt><code>fma4</code></p>
<dd>
<dt><code>3dnow</code></p>
<dd>
<dt><code>3dnowext</code></p>
<dd>
<dt><code>bmi1</code></p>
<dd>
<dt><code>bmi2</code></p>
<dd>
<dt><code>cmov</code></p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><font SIZE="-1"><code>ARM</code></font></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>armv5te</code></p>
<dd>
<dt><code>armv6</code></p>
<dd>
<dt><code>armv6t2</code></p>
<dd>
<dt><code>vfp</code></p>
<dd>
<dt><code>vfpv3</code></p>
<dd>
<dt><code>neon</code></p>
<dd>
<dt><code>setend</code></p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>AArch64</code></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>armv8</code></p>
<dd>
<dt><code>vfp</code></p>
<dd>
<dt><code>neon</code></p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>PowerPC</code></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>altivec</code></p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>Specific Processors</code></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>pentium2</code></p>
<dd>
<dt><code>pentium3</code></p>
<dd>
<dt><code>pentium4</code></p>
<dd>
<dt><code>k6</code></p>
<dd>
<dt><code>k62</code></p>
<dd>
<dt><code>athlon</code></p>
<dd>
<dt><code>athlonxp</code></p>
<dd>
<dt><code>k8</code></p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-max_alloc</code> <i>bytes</i></p>
<dd> Set the maximum size limit for allocating a block on the heap by ffmpeg&#8217;s family of malloc functions. Exercise <code>extreme caution</code> when using this option. Don&#8217;t use if you do not understand the full consequence of doing so. Default is <font SIZE="-1">INT_MAX.</font></dl>
<h3>AVOptions</h3>
<p> These options are provided directly by the libavformat, libavdevice and libavcodec libraries. To see the list of available AVOptions, use the <code>-help</code> option. They are separated into two categories:</p>
<dl>
<dt><code>generic</code></p>
<dd> These options can be set for any container, codec or device. Generic options are listed under AVFormatContext options for containers/devices and under AVCodecContext options for codecs.</p>
<dt><code>private</code></p>
<dd> These options are specific to the given container, device or codec. Private options are listed under their corresponding containers/devices/codecs.</dl>
<p> For example to write an ID3v2.3 header instead of a default ID3v2.4 to an <font SIZE="-1">MP3</font> file, use the <code>id3v2_version</code> private option of the <font SIZE="-1">MP3</font> muxer: </p>
<pre>
        ffmpeg -i input.flac -id3v2_version 3 out.mp3
</pre>
<p> All codec AVOptions are per-stream, and thus a stream specifier should be attached to them: </p>
<pre>
        ffmpeg -i multichannel.mxf -map 0:v:0 -map 0:a:0 -map 0:a:0 -c:a:0 ac3 -b:a:0 640k -ac:a:1 2 -c:a:1 aac -b:2 128k out.mp4
</pre>
<p> In the above example, a multichannel audio stream is mapped twice for output. The first instance is encoded with codec ac3 and bitrate 640k. The second instance is downmixed to 2 channels and encoded with codec aac. A bitrate of 128k is specified for it using absolute index of the output stream. </p>
<p> Note: the <code>-nooption</code> syntax cannot be used for boolean AVOptions, use <code>-option 0</code>/<code>-option 1</code>. </p>
<p> Note: the old undocumented way of specifying per-stream AVOptions by prepending v/a/s to the options name is now obsolete and will be removed soon.</p>
<h3>Main options</h3>
<dl>
<dt><code>-x</code> <i>width</i></p>
<dd> Force displayed width.</p>
<dt><code>-y</code> <i>height</i></p>
<dd> Force displayed height.</p>
<dt><code>-s</code> <i>size</i></p>
<dd> Set frame size (WxH or abbreviation), needed for videos which do not contain a header with the frame size like raw <font SIZE="-1">YUV.</font> This option has been deprecated in favor of private options, try -video_size.</p>
<dt><code>-fs</code></p>
<dd> Start in fullscreen mode.</p>
<dt><code>-an</code></p>
<dd> Disable audio.</p>
<dt><code>-vn</code></p>
<dd> Disable video.</p>
<dt><code>-sn</code></p>
<dd> Disable subtitles.</p>
<dt><code>-ss</code> <i>pos</i></p>
<dd> Seek to <i>pos</i>. Note that in most formats it is not possible to seek exactly, so <code>ffplay</code> will seek to the nearest seek point to <i>pos</i>. </p>
<p> <i>pos</i> must be a time duration specification, see <code>the Time duration section in the <a href="/docs/linux/man/1-ffmpeg-utils/">ffmpeg-utils</a>(1) manual</code>.</p>
<dt><code>-t</code> <i>duration</i></p>
<dd> Play <i>duration</i> seconds of audio/video. </p>
<p> <i>duration</i> must be a time duration specification, see <code>the Time duration section in the <a href="/docs/linux/man/1-ffmpeg-utils/">ffmpeg-utils</a>(1) manual</code>.</p>
<dt><code>-bytes</code></p>
<dd> Seek by bytes.</p>
<dt><code>-seek_interval</code></p>
<dd> Set custom interval, in seconds, for seeking using left/right keys. Default is 10 seconds.</p>
<dt><code>-nodisp</code></p>
<dd> Disable graphical display.</p>
<dt><code>-noborder</code></p>
<dd> Borderless window.</p>
<dt><code>-alwaysontop</code></p>
<dd> Window always on top. Available on: X11 with <font SIZE="-1">SDL</font> &gt;= 2.0.5, Windows <font SIZE="-1">SDL</font> &gt;= 2.0.6.</p>
<dt><code>-volume</code></p>
<dd> Set the startup volume. 0 means silence, 100 means no volume reduction or amplification. Negative values are treated as 0, values above 100 are treated as 100.</p>
<dt><code>-f</code> <i>fmt</i></p>
<dd> Force format.</p>
<dt><code>-window_title</code> <i>title</i></p>
<dd> Set window title (default is the input filename).</p>
<dt><code>-left</code> <i>title</i></p>
<dd> Set the x position for the left of the window (default is a centered window).</p>
<dt><code>-top</code> <i>title</i></p>
<dd> Set the y position for the top of the window (default is a centered window).</p>
<dt><code>-loop</code> <i>number</i></p>
<dd> Loops movie playback &lt;number&gt; times. 0 means forever.</p>
<dt><code>-showmode</code> <i>mode</i></p>
<dd> Set the show mode to use. Available values for <i>mode</i> are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>0, video</code></p>
<dd> show video</p>
<dt><code>1, waves</code></p>
<dd> show audio waves</p>
<dt><code>2, rdft</code></p>
<dd> show audio frequency band using <font SIZE="-1">RDFT</font> ((Inverse) Real Discrete Fourier Transform)</dl>
</dl>
<dl>
<dt>
<dd>
<p> Default value is &#8220;video&#8221;, if video is not present or cannot be played &#8220;rdft&#8221; is automatically selected. </p>
<p> You can interactively cycle through the available show modes by pressing the key <code>w</code>.</dl>
<dt><code>-vf</code> <i>filtergraph</i></p>
<dd> Create the filtergraph specified by <i>filtergraph</i> and use it to filter the video stream. </p>
<p> <i>filtergraph</i> is a description of the filtergraph to apply to the stream, and must have a single video input and a single video output. In the filtergraph, the input is associated to the label <tt>&quot;in&quot;</tt>, and the output to the label <tt>&quot;out&quot;</tt>. See the ffmpeg-filters manual for more information about the filtergraph syntax. </p>
<p> You can specify this parameter multiple times and cycle through the specified filtergraphs along with the show modes by pressing the key <code>w</code>.</p>
<dt><code>-af</code> <i>filtergraph</i></p>
<dd> <i>filtergraph</i> is a description of the filtergraph to apply to the input audio. Use the option &#8220;-filters&#8221; to show all the available filters (including sources and sinks).</p>
<dt><code>-i</code> <i>input_url</i></p>
<dd> Read <i>input_url</i>.</dl>
<h3>Advanced options</h3>
<dl>
<dt><code>-pix_fmt</code> <i>format</i></p>
<dd> Set pixel format. This option has been deprecated in favor of private options, try -pixel_format.</p>
<dt><code>-stats</code></p>
<dd> Print several playback statistics, in particular show the stream duration, the codec parameters, the current position in the stream and the audio/video synchronisation drift. It is shown by default, unless the log level is lower than <tt>&quot;info&quot;</tt>. Its display can be forced by manually specifying this option. To disable it, you need to specify <tt>&quot;-nostats&quot;</tt>.</p>
<dt><code>-fast</code></p>
<dd> Non-spec-compliant optimizations.</p>
<dt><code>-genpts</code></p>
<dd> Generate pts.</p>
<dt><code>-sync</code> <i>type</i></p>
<dd> Set the master clock to audio (<tt>&quot;type=audio&quot;</tt>), video (<tt>&quot;type=video&quot;</tt>) or external (<tt>&quot;type=ext&quot;</tt>). Default is audio. The master clock is used to control audio-video synchronization. Most media players use audio as master clock, but in some cases (streaming or high quality broadcast) it is necessary to change that. This option is mainly used for debugging purposes.</p>
<dt><code>-ast</code> <i>audio_stream_specifier</i></p>
<dd> Select the desired audio stream using the given stream specifier. The stream specifiers are described in the <code>Stream specifiers</code> chapter. If this option is not specified, the &#8220;best&#8221; audio stream is selected in the program of the already selected video stream.</p>
<dt><code>-vst</code> <i>video_stream_specifier</i></p>
<dd> Select the desired video stream using the given stream specifier. The stream specifiers are described in the <code>Stream specifiers</code> chapter. If this option is not specified, the &#8220;best&#8221; video stream is selected.</p>
<dt><code>-sst</code> <i>subtitle_stream_specifier</i></p>
<dd> Select the desired subtitle stream using the given stream specifier. The stream specifiers are described in the <code>Stream specifiers</code> chapter. If this option is not specified, the &#8220;best&#8221; subtitle stream is selected in the program of the already selected video or audio stream.</p>
<dt><code>-autoexit</code></p>
<dd> Exit when video is done playing.</p>
<dt><code>-exitonkeydown</code></p>
<dd> Exit if any key is pressed.</p>
<dt><code>-exitonmousedown</code></p>
<dd> Exit if any mouse button is pressed.</p>
<dt><code>-codec:</code><i>media_specifier</i><i>codec_name</i></p>
<dd> Force a specific decoder implementation for the stream identified by <i>media_specifier</i>, which can assume the values <tt>&quot;a&quot;</tt> (audio), <tt>&quot;v&quot;</tt> (video), and <tt>&quot;s&quot;</tt> subtitle.</p>
<dt><code>-acodec</code> <i>codec_name</i></p>
<dd> Force a specific audio decoder.</p>
<dt><code>-vcodec</code> <i>codec_name</i></p>
<dd> Force a specific video decoder.</p>
<dt><code>-scodec</code> <i>codec_name</i></p>
<dd> Force a specific subtitle decoder.</p>
<dt><code>-autorotate</code></p>
<dd> Automatically rotate the video according to file metadata. Enabled by default, use <code>-noautorotate</code> to disable it.</p>
<dt><code>-framedrop</code></p>
<dd> Drop video frames if video is out of sync. Enabled by default if the master clock is not set to video. Use this option to enable frame dropping for all master clock sources, use <code>-noframedrop</code> to disable it.</p>
<dt><code>-infbuf</code></p>
<dd> Do not limit the input buffer size, read as much data as possible from the input as soon as possible. Enabled by default for realtime streams, where data may be dropped if not read in time. Use this option to enable infinite buffers for all inputs, use <code>-noinfbuf</code> to disable it.</p>
<dt><code>-filter_threads</code> <i>nb_threads</i></p>
<dd> Defines how many threads are used to process a filter pipeline. Each pipeline will produce a thread pool with this many threads available for parallel processing. The default is 0 which means that the thread count will be determined by the number of available CPUs.</dl>
<h3>While playing</h3>
<dl>
<dt><code>q, </code><font SIZE="-1"><code>ESC</code></font></p>
<dd> Quit.</p>
<dt><code>f</code></p>
<dd> Toggle full screen.</p>
<dt><code>p, </code><font SIZE="-1"><code>SPC</code></font></p>
<dd> Pause.</p>
<dt><code>m</code></p>
<dd> Toggle mute.</p>
<dt><code>9, 0</code></p>
<dd> Decrease and increase volume respectively.</p>
<dt><code>/, *</code></p>
<dd> Decrease and increase volume respectively.</p>
<dt><code>a</code></p>
<dd> Cycle audio channel in the current program.</p>
<dt><code>v</code></p>
<dd> Cycle video channel.</p>
<dt><code>t</code></p>
<dd> Cycle subtitle channel in the current program.</p>
<dt><code>c</code></p>
<dd> Cycle program.</p>
<dt><code>w</code></p>
<dd> Cycle video filters or show modes.</p>
<dt><code>s</code></p>
<dd> Step to the next frame. </p>
<p> Pause if the stream is not already paused, step to the next video frame, and pause.</p>
<dt><code>left/right</code></p>
<dd> Seek backward/forward 10 seconds.</p>
<dt><code>down/up</code></p>
<dd> Seek backward/forward 1 minute.</p>
<dt><code>page down/page up</code></p>
<dd> Seek to the previous/next chapter. or if there are no chapters Seek backward/forward 10 minutes.</p>
<dt><code>right mouse click</code></p>
<dd> Seek to percentage in file corresponding to fraction of width.</p>
<dt><code>left mouse double-click</code></p>
<dd> Toggle full screen.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ffplay-all/">ffplay-all</a></code>(1), <code><a href="/docs/linux/man/1-ffmpeg/">ffmpeg</a></code>(1), <code><a href="/docs/linux/man/1-ffprobe/">ffprobe</a></code>(1), <code><a href="/docs/linux/man/1-ffmpeg-utils/">ffmpeg-utils</a></code>(1), <code><a href="/docs/linux/man/1-ffmpeg-scaler/">ffmpeg-scaler</a></code>(1), <code><a href="/docs/linux/man/1-ffmpeg-resampler/">ffmpeg-resampler</a></code>(1), <code><a href="/docs/linux/man/1-ffmpeg-codecs/">ffmpeg-codecs</a></code>(1), <code><a href="/docs/linux/man/1-ffmpeg-bitstream-filters/">ffmpeg-bitstream-filters</a></code>(1), <code><a href="/docs/linux/man/1-ffmpeg-formats/">ffmpeg-formats</a></code>(1), <code><a href="/docs/linux/man/1-ffmpeg-devices/">ffmpeg-devices</a></code>(1), <code><a href="/docs/linux/man/1-ffmpeg-protocols/">ffmpeg-protocols</a></code>(1), <code><a href="/docs/linux/man/1-ffmpeg-filters/">ffmpeg-filters</a></code>(1)</p>
<h2>AUTHORS</h2>
<p> The FFmpeg developers. </p>
<p> For details about the authorship, see the Git history of the project (<a href="git://source.ffmpeg.org/ffmpeg">git://source.ffmpeg.org/ffmpeg</a>), e.g. by typing the command <code>git log</code> in the FFmpeg source directory, or browsing the online repository at &lt;<code><a rel="nofollow" href="http://source.ffmpeg.org">http://source.ffmpeg.org</a></code>&gt;. </p>
<p> Maintainers for the specific components are listed in the file <i></i><font SIZE="-1"><i>MAINTAINERS</i></font><i></i> in the source code tree. </p>
<h2>Index</h2>
