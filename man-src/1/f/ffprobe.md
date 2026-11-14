---
title: "ffprobe(1)"
name: "ffprobe"
section: "1"
letter: "f"
url: "/docs/linux/man/1-ffprobe/"
description: "ffprobe – ffprobe media prober"
---

<h2 class="name">NAME</h2>
<p> ffprobe &#8211; ffprobe media prober </p>
<h2>SYNOPSIS</h2>
<p> ffprobe [<i>options</i>] [<i>input_url</i>]</p>
<h2>DESCRIPTION</h2>
<p> ffprobe gathers information from multimedia streams and prints it in human- and machine-readable fashion. </p>
<p> For example it can be used to check the format of the container used by a multimedia stream and the format and type of each media stream contained in it. </p>
<p> If a url is specified in input, ffprobe will try to open and probe the url content. If the url cannot be opened or recognized as a multimedia file, a positive exit code is returned. </p>
<p> ffprobe may be employed both as a standalone application or in combination with a textual filter, which may perform more sophisticated processing, e.g. statistical processing or plotting. </p>
<p> Options are used to list some of the formats supported by ffprobe or for specifying which information to display, and for setting how ffprobe will show it. </p>
<p> ffprobe output is designed to be easily parsable by a textual filter, and consists of one or more sections of a form defined by the selected writer, which is specified by the <code>print_format</code> option. </p>
<p> Sections may contain other nested sections, and are identified by a name (which may be shared by other sections), and an unique name. See the output of <code>sections</code>. </p>
<p> Metadata tags stored in the container or in the streams are recognized and printed in the corresponding &#8220;<font SIZE="-1">FORMAT&#8221;, &#8220;STREAM&#8221;</font> or &#8220;<font SIZE="-1">PROGRAM_STREAM&#8221;</font> section.</p>
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
<dt><code>-f</code> <i>format</i></p>
<dd> Force format to use.</p>
<dt><code>-unit</code></p>
<dd> Show the unit of the displayed values.</p>
<dt><code>-prefix</code></p>
<dd> Use <font SIZE="-1">SI</font> prefixes for the displayed values. Unless the &#8220;-byte_binary_prefix&#8221; option is used all the prefixes are decimal.</p>
<dt><code>-byte_binary_prefix</code></p>
<dd> Force the use of binary prefixes for byte values.</p>
<dt><code>-sexagesimal</code></p>
<dd> Use sexagesimal format <font SIZE="-1">HH:MM:SS.MICROSECONDS</font> for time values.</p>
<dt><code>-pretty</code></p>
<dd> Prettify the format of the displayed values, it corresponds to the options &#8220;-unit -prefix -byte_binary_prefix -sexagesimal&#8221;.</p>
<dt><code>-of, -print_format</code> <i>writer_name</i><code>[=</code><i>writer_options</i><code>]</code></p>
<dd> Set the output printing format. </p>
<p> <i>writer_name</i> specifies the name of the writer, and <i>writer_options</i> specifies the options to be passed to the writer. </p>
<p> For example for printing the output in <font SIZE="-1">JSON</font> format, specify: </p>
<pre>
        -print_format json
</pre>
<p> For more details on the available output printing formats, see the Writers section below.</p>
<dt><code>-sections</code></p>
<dd> Print sections structure and section information, and exit. The output is not meant to be parsed by a machine.</p>
<dt><code>-select_streams</code> <i>stream_specifier</i></p>
<dd> Select only the streams specified by <i>stream_specifier</i>. This option affects only the options related to streams (e.g. <tt>&quot;show_streams&quot;</tt>, <tt>&quot;show_packets&quot;</tt>, etc.). </p>
<p> For example to show only audio streams, you can use the command: </p>
<pre>
        ffprobe -show_streams -select_streams a INPUT
</pre>
<p> To show only video packets belonging to the video stream with index 1: </p>
<pre>
        ffprobe -show_packets -select_streams v:1 INPUT
</pre>
<dt><code>-show_data</code></p>
<dd> Show payload data, as a hexadecimal and <font SIZE="-1">ASCII</font> dump. Coupled with <code>-show_packets</code>, it will dump the packets&#8217; data. Coupled with <code>-show_streams</code>, it will dump the codec extradata. </p>
<p> The dump is printed as the &#8220;data&#8221; field. It may contain newlines.</p>
<dt><code>-show_data_hash</code> <i>algorithm</i></p>
<dd> Show a hash of payload data, for packets with <code>-show_packets</code> and for codec extradata with <code>-show_streams</code>.</p>
<dt><code>-show_error</code></p>
<dd> Show information about the error found when trying to probe the input. </p>
<p> The error information is printed within a section with name &#8220;<font SIZE="-1">ERROR&#8221;.</font></p>
<dt><code>-show_format</code></p>
<dd> Show information about the container format of the input multimedia stream. </p>
<p> All the container format information is printed within a section with name &#8220;<font SIZE="-1">FORMAT&#8221;.</font></p>
<dt><code>-show_format_entry</code> <i>name</i></p>
<dd> Like <code>-show_format</code>, but only prints the specified entry of the container format information, rather than all. This option may be given more than once, then all specified entries will be shown. </p>
<p> This option is deprecated, use <tt>&quot;show_entries&quot;</tt> instead.</p>
<dt><code>-show_entries</code> <i>section_entries</i></p>
<dd> Set list of entries to show. </p>
<p> Entries are specified according to the following syntax. <i>section_entries</i> contains a list of section entries separated by <tt>&quot;:&quot;</tt>. Each section entry is composed by a section name (or unique name), optionally followed by a list of entries local to that section, separated by <tt>&quot;,&quot;</tt>. </p>
<p> If section name is specified but is followed by no <tt>&quot;=&quot;</tt>, all entries are printed to output, together with all the contained sections. Otherwise only the entries specified in the local section entries list are printed. In particular, if <tt>&quot;=&quot;</tt> is specified but the list of local entries is empty, then no entries will be shown for that section. </p>
<p> Note that the order of specification of the local section entries is not honored in the output, and the usual display order will be retained. </p>
<p> The formal syntax is given by: </p>
<pre><code>
        &lt;LOCAL_SECTION_ENTRIES&gt; ::= &lt;SECTION_ENTRY_NAME&gt;[,&lt;LOCAL_SECTION_ENTRIES&gt;]
        &lt;SECTION_ENTRY&gt;         ::= &lt;SECTION_NAME&gt;[=[&lt;LOCAL_SECTION_ENTRIES&gt;]]
        &lt;SECTION_ENTRIES&gt;       ::= &lt;SECTION_ENTRY&gt;[:&lt;SECTION_ENTRIES&gt;]
</code></pre>
<p> For example, to show only the index and type of each stream, and the <font SIZE="-1">PTS</font> time, duration time, and stream index of the packets, you can specify the argument: </p>
<pre>
        packet=pts_time,duration_time,stream_index : stream=index,codec_type
</pre>
<p> To show all the entries in the section &#8220;format&#8221;, but only the codec type in the section &#8220;stream&#8221;, specify the argument: </p>
<pre>
        format : stream=codec_type
</pre>
<p> To show all the tags in the stream and format sections: </p>
<pre>
        stream_tags : format_tags
</pre>
<p> To show only the <tt>&quot;title&quot;</tt> tag (if available) in the stream sections: </p>
<pre>
        stream_tags=title
</pre>
<dt><code>-show_packets</code></p>
<dd> Show information about each packet contained in the input multimedia stream. </p>
<p> The information for each single packet is printed within a dedicated section with name &#8220;<font SIZE="-1">PACKET&#8221;.</font></p>
<dt><code>-show_frames</code></p>
<dd> Show information about each frame and subtitle contained in the input multimedia stream. </p>
<p> The information for each single frame is printed within a dedicated section with name &#8220;<font SIZE="-1">FRAME&#8221;</font> or &#8220;<font SIZE="-1">SUBTITLE&#8221;.</font></p>
<dt><code>-show_log</code> <i>loglevel</i></p>
<dd> Show logging information from the decoder about each frame according to the value set in <i>loglevel</i>, (see <tt>&quot;-loglevel&quot;</tt>). This option requires <tt>&quot;-show_frames&quot;</tt>. </p>
<p> The information for each log message is printed within a dedicated section with name &#8220;<font SIZE="-1">LOG&#8221;.</font></p>
<dt><code>-show_streams</code></p>
<dd> Show information about each media stream contained in the input multimedia stream. </p>
<p> Each media stream information is printed within a dedicated section with name &#8220;<font SIZE="-1">STREAM&#8221;.</font></p>
<dt><code>-show_programs</code></p>
<dd> Show information about programs and their streams contained in the input multimedia stream. </p>
<p> Each media stream information is printed within a dedicated section with name &#8220;<font SIZE="-1">PROGRAM_STREAM&#8221;.</font></p>
<dt><code>-show_chapters</code></p>
<dd> Show information about chapters stored in the format. </p>
<p> Each chapter is printed within a dedicated section with name &#8220;<font SIZE="-1">CHAPTER&#8221;.</font></p>
<dt><code>-count_frames</code></p>
<dd> Count the number of frames per stream and report it in the corresponding stream section.</p>
<dt><code>-count_packets</code></p>
<dd> Count the number of packets per stream and report it in the corresponding stream section.</p>
<dt><code>-read_intervals</code> <i>read_intervals</i></p>
<dd> Read only the specified intervals. <i>read_intervals</i> must be a sequence of interval specifications separated by &#8220;,&#8221;. <code>ffprobe</code> will seek to the interval starting point, and will continue reading from that. </p>
<p> Each interval is specified by two optional parts, separated by &#8220;%&#8221;. </p>
<p> The first part specifies the interval start position. It is interpreted as an absolute position, or as a relative offset from the current position if it is preceded by the &#8220;+&#8221; character. If this first part is not specified, no seeking will be performed when reading this interval. </p>
<p> The second part specifies the interval end position. It is interpreted as an absolute position, or as a relative offset from the current position if it is preceded by the &#8220;+&#8221; character. If the offset specification starts with &#8220;#&#8221;, it is interpreted as the number of packets to read (not including the flushing packets) from the interval start. If no second part is specified, the program will read until the end of the input. </p>
<p> Note that seeking is not accurate, thus the actual interval start point may be different from the specified position. Also, when an interval duration is specified, the absolute end time will be computed by adding the duration to the interval start point found by seeking the file, rather than to the specified start value. </p>
<p> The formal syntax is given by: </p>
<p>        &lt;INTERVAL&gt;  ::= [&lt;START&gt;|+&lt;START_OFFSET&gt;][%[&lt;END&gt;|+&lt;END_OFFSET&gt;]]<br />
        &lt;INTERVALS&gt; ::= &lt;INTERVAL&gt;[,&lt;INTERVALS&gt;]</p>
<p> A few examples follow.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Seek to time 10, read packets until 20 seconds after the found seek point, then seek to position <tt>&quot;01:30&quot;</tt> (1 minute and thirty seconds) and read packets until position <tt>&quot;01:45&quot;</tt>. </p>
<pre>
        10%+20,01:30%01:45
</pre>
<dt>&bull;</p>
<dd> Read only 42 packets after seeking to position <tt>&quot;01:23&quot;</tt>: </p>
<pre>
        01:23%+#42
</pre>
<dt>&bull;</p>
<dd> Read only the first 20 seconds from the start: </p>
<pre>
        %+20
</pre>
<dt>&bull;</p>
<dd> Read from the start until position <tt>&quot;02:30&quot;</tt>: </p>
<pre>
        %02:30
</pre>
</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-show_private_data, -private</code></p>
<dd> Show private data, that is data depending on the format of the particular shown element. This option is enabled by default, but you may need to disable it for specific uses, for example when creating XSD-compliant <font SIZE="-1">XML</font> output.</p>
<dt><code>-show_program_version</code></p>
<dd> Show information related to program version. </p>
<p> Version information is printed within a section with name &#8220;<font SIZE="-1">PROGRAM_VERSION&#8221;.</font></p>
<dt><code>-show_library_versions</code></p>
<dd> Show information related to library versions. </p>
<p> Version information for each library is printed within a section with name &#8220;<font SIZE="-1">LIBRARY_VERSION&#8221;.</font></p>
<dt><code>-show_versions</code></p>
<dd> Show information related to program and library versions. This is the equivalent of setting both <code>-show_program_version</code> and <code>-show_library_versions</code> options.</p>
<dt><code>-show_pixel_formats</code></p>
<dd> Show information about all pixel formats supported by FFmpeg. </p>
<p> Pixel format information for each format is printed within a section with name &#8220;<font SIZE="-1">PIXEL_FORMAT&#8221;.</font></p>
<dt><code>-bitexact</code></p>
<dd> Force bitexact output, useful to produce output which is not dependent on the specific build.</p>
<dt><code>-i</code> <i>input_url</i></p>
<dd> Read <i>input_url</i>.</dl>
<h2>WRITERS</h2>
<p> A writer defines the output format adopted by <code>ffprobe</code>, and will be used for printing all the parts of the output. </p>
<p> A writer may accept one or more arguments, which specify the options to adopt. The options are specified as a list of <i>key</i>=<i>value</i> pairs, separated by &#8220;:&#8221;. </p>
<p> All writers support the following options:</p>
<dl>
<dt><code>string_validation, sv</code></p>
<dd> Set string validation mode. </p>
<p> The following values are accepted.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>fail</code></p>
<dd> The writer will fail immediately in case an invalid string (<font SIZE="-1">UTF-8</font>) sequence or code point is found in the input. This is especially useful to validate input metadata.</p>
<dt><code>ignore</code></p>
<dd> Any validation error will be ignored. This will result in possibly broken output, especially with the json or xml writer.</p>
<dt><code>replace</code></p>
<dd> The writer will substitute invalid <font SIZE="-1">UTF-8</font> sequences or code points with the string specified with the <code>string_validation_replacement</code>.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Default value is <code>replace</code>.</dl>
<dt><code>string_validation_replacement, svr</code></p>
<dd> Set replacement string to use in case <code>string_validation</code> is set to <code>replace</code>. </p>
<p> In case the option is not specified, the writer will assume the empty string, that is it will remove the invalid sequences from the input strings.</dl>
<p> A description of the currently available writers follows.</p>
<h3>default</h3>
<p> Default format. </p>
<p> Print each section in the form: </p>
<pre><code>
[SECTION] key1 = val1... keyN = valN
    [/ SECTION]
</code></pre>
<p> Metadata tags are printed as a line in the corresponding <font SIZE="-1">FORMAT, STREAM</font> or <font SIZE="-1">PROGRAM_STREAM</font> section, and are prefixed by the string &#8220;<font SIZE="-1">TAG:&#8221;.</font> </p>
<p> A description of the accepted options follows.</p>
<dl>
<dt><code>nokey, nk</code></p>
<dd> If set to 1 specify not to print the key of each field. Default value is 0.</p>
<dt><code>noprint_wrappers, nw</code></p>
<dd> If set to 1 specify not to print the section header and footer. Default value is 0.</dl>
<h3>compact, csv</h3>
<p> Compact and <font SIZE="-1">CSV</font> format. </p>
<p> The <tt>&quot;csv&quot;</tt> writer is equivalent to <tt>&quot;compact&quot;</tt>, but supports different defaults. </p>
<p> Each section is printed on a single line. If no option is specified, the output has the form: </p>
<pre>
        section|key1=val1| ... |keyN=valN
</pre>
<p> Metadata tags are printed in the corresponding &#8220;format&#8221; or &#8220;stream&#8221; section. A metadata tag key, if printed, is prefixed by the string &#8220;tag:&#8221;. </p>
<p> The description of the accepted options follows.</p>
<dl>
<dt><code>item_sep, s</code></p>
<dd> Specify the character to use for separating fields in the output line. It must be a single printable character, it is &#8220;|&#8221; by default (&#8220;,&#8221; for the <tt>&quot;csv&quot;</tt> writer).</p>
<dt><code>nokey, nk</code></p>
<dd> If set to 1 specify not to print the key of each field. Its default value is 0 (1 for the <tt>&quot;csv&quot;</tt> writer).</p>
<dt><code>escape, e</code></p>
<dd> Set the escape mode to use, default to &#8220;c&#8221; (&#8220;csv&#8221; for the <tt>&quot;csv&quot;</tt> writer). </p>
<p> It can assume one of the following values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>c</code></p>
<dd> Perform C-like escaping. Strings containing a newline (<code>
</code>), carriage return (<code></code>), a tab (<code>	</code>), a form feed (<code></code>), the escaping character (<code>\</code>) or the item separator character <i></i><font SIZE="-1"><i>SEP</i></font><i></i> are escaped using C-like fashioned escaping, so that a newline is converted to the sequence <code>
</code>, a carriage return to <code></code>, <code>\</code> to <code>\</code> and the separator <i></i><font SIZE="-1"><i>SEP</i></font><i></i> is converted to <code>\</code><i></i><font SIZE="-1"><i>SEP</i></font><i></i>.</p>
<dt><code>csv</code></p>
<dd> Perform CSV-like escaping, as described in <font SIZE="-1">RFC4180.</font> Strings containing a newline (<code>
</code>), a carriage return (<code></code>), a double quote (<code>&quot;</code>), or <i></i><font SIZE="-1"><i>SEP</i></font><i></i> are enclosed in double-quotes.</p>
<dt><code>none</code></p>
<dd> Perform no escaping.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>print_section, p</code></p>
<dd> Print the section name at the beginning of each line if the value is <tt>1</tt>, disable it with value set to <tt>0</tt>. Default value is <tt>1</tt>.</dl>
<h3>flat</h3>
<p> Flat format. </p>
<p> A free-form output where each line contains an explicit key=value, such as &#8220;streams.stream.3.tags.foo=bar&#8221;. The output is shell escaped, so it can be directly embedded in sh scripts as long as the separator character is an alphanumeric character or an underscore (see <i>sep_char</i> option). </p>
<p> The description of the accepted options follows.</p>
<dl>
<dt><code>sep_char, s</code></p>
<dd> Separator character used to separate the chapter, the section name, IDs and potential tags in the printed field key. </p>
<p> Default value is <code>.</code>.</p>
<dt><code>hierarchical, h</code></p>
<dd> Specify if the section name specification should be hierarchical. If set to 1, and if there is more than one section in the current chapter, the section name will be prefixed by the name of the chapter. A value of 0 will disable this behavior. </p>
<p> Default value is 1.</dl>
<h3>ini</h3>
<p> <font SIZE="-1">INI</font> format output. </p>
<p> Print output in an <font SIZE="-1">INI</font> based format. </p>
<p> The following conventions are adopted:</p>
<dl>
<dt>&bull;</p>
<dd> all key and values are <font SIZE="-1">UTF-8</font></p>
<dt>&bull;</p>
<dd> <code>.</code> is the subgroup separator</p>
<dt>&bull;</p>
<dd> newline, <code>	</code>, <code></code>, <code></code> and the following characters are escaped</p>
<dt>&bull;</p>
<dd> <code>\</code> is the escape character</p>
<dt>&bull;</p>
<dd> <code>#</code> is the comment indicator</p>
<dt>&bull;</p>
<dd> <code>=</code> is the key/value separator</p>
<dt>&bull;</p>
<dd> <code>:</code> is not used but usually parsed as key/value separator</dl>
<p> This writer accepts options as a list of <i>key</i>=<i>value</i> pairs, separated by <code>:</code>. </p>
<p> The description of the accepted options follows.</p>
<dl>
<dt><code>hierarchical, h</code></p>
<dd> Specify if the section name specification should be hierarchical. If set to 1, and if there is more than one section in the current chapter, the section name will be prefixed by the name of the chapter. A value of 0 will disable this behavior. </p>
<p> Default value is 1.</dl>
<h3>json</h3>
<p> <font SIZE="-1">JSON</font> based format. </p>
<p> Each section is printed using <font SIZE="-1">JSON</font> notation. </p>
<p> The description of the accepted options follows.</p>
<dl>
<dt><code>compact, c</code></p>
<dd> If set to 1 enable compact output, that is each section will be printed on a single line. Default value is 0.</dl>
<p> For more information about <font SIZE="-1">JSON,</font> see &lt;<code><a rel="nofollow" href="http://www.json.org/">http://www.json.org/</a></code>&gt;.</p>
<h3>xml</h3>
<p> <font SIZE="-1">XML</font> based format. </p>
<p> The <font SIZE="-1">XML</font> output is described in the <font SIZE="-1">XML</font> schema description file <i>ffprobe.xsd</i> installed in the FFmpeg datadir. </p>
<p> An updated version of the schema can be retrieved at the url &lt;<code><a rel="nofollow" href="http://www.ffmpeg.org/schema/ffprobe.xsd">http://www.ffmpeg.org/schema/ffprobe.xsd</a></code>&gt;, which redirects to the latest schema committed into the FFmpeg development source code tree. </p>
<p> Note that the output issued will be compliant to the <i>ffprobe.xsd</i> schema only when no special global output options (<code>unit</code>, <code>prefix</code>, <code>byte_binary_prefix</code>, <code>sexagesimal</code> etc.) are specified. </p>
<p> The description of the accepted options follows.</p>
<dl>
<dt><code>fully_qualified, q</code></p>
<dd> If set to 1 specify if the output should be fully qualified. Default value is 0. This is required for generating an <font SIZE="-1">XML</font> file which can be validated through an <font SIZE="-1">XSD</font> file.</p>
<dt><code>xsd_strict, x</code></p>
<dd> If set to 1 perform more checks for ensuring that the output is <font SIZE="-1">XSD</font> compliant. Default value is 0. This option automatically sets <code>fully_qualified</code> to 1.</dl>
<p> For more information about the <font SIZE="-1">XML</font> format, see &lt;<code><a rel="nofollow" href="https://www.w3.org/XML/">https://www.w3.org/XML/</a></code>&gt;.</p>
<h2>TIMECODE</h2>
<p> <code>ffprobe</code> supports Timecode extraction:</p>
<dl>
<dt>&bull;</p>
<dd> <font SIZE="-1">MPEG1/2</font> timecode is extracted from the <font SIZE="-1">GOP,</font> and is available in the video stream details (<code>-show_streams</code>, see <i>timecode</i>).</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">MOV</font> timecode is extracted from tmcd track, so is available in the tmcd stream metadata (<code>-show_streams</code>, see <i>TAG:timecode</i>).</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">DV, GXF</font> and <font SIZE="-1">AVI</font> timecodes are available in format metadata (<code>-show_format</code>, see <i>TAG:timecode</i>).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ffprobe-all/">ffprobe-all</a></code>(1), <code><a href="/docs/linux/man/1-ffmpeg/">ffmpeg</a></code>(1), <code><a href="/docs/linux/man/1-ffplay/">ffplay</a></code>(1), <code><a href="/docs/linux/man/1-ffmpeg-utils/">ffmpeg-utils</a></code>(1), <code><a href="/docs/linux/man/1-ffmpeg-scaler/">ffmpeg-scaler</a></code>(1), <code><a href="/docs/linux/man/1-ffmpeg-resampler/">ffmpeg-resampler</a></code>(1), <code><a href="/docs/linux/man/1-ffmpeg-codecs/">ffmpeg-codecs</a></code>(1), <code><a href="/docs/linux/man/1-ffmpeg-bitstream-filters/">ffmpeg-bitstream-filters</a></code>(1), <code><a href="/docs/linux/man/1-ffmpeg-formats/">ffmpeg-formats</a></code>(1), <code><a href="/docs/linux/man/1-ffmpeg-devices/">ffmpeg-devices</a></code>(1), <code><a href="/docs/linux/man/1-ffmpeg-protocols/">ffmpeg-protocols</a></code>(1), <code><a href="/docs/linux/man/1-ffmpeg-filters/">ffmpeg-filters</a></code>(1)</p>
<h2>AUTHORS</h2>
<p> The FFmpeg developers. </p>
<p> For details about the authorship, see the Git history of the project (<a href="git://source.ffmpeg.org/ffmpeg">git://source.ffmpeg.org/ffmpeg</a>), e.g. by typing the command <code>git log</code> in the FFmpeg source directory, or browsing the online repository at &lt;<code><a rel="nofollow" href="http://source.ffmpeg.org">http://source.ffmpeg.org</a></code>&gt;. </p>
<p> Maintainers for the specific components are listed in the file <i></i><font SIZE="-1"><i>MAINTAINERS</i></font><i></i> in the source code tree. </p>
<h2>Index</h2>
