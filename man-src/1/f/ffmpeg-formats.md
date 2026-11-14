---
title: "ffmpeg-formats(1)"
name: "ffmpeg-formats"
section: "1"
letter: "f"
url: "/docs/linux/man/1-ffmpeg-formats/"
description: "ffmpeg-formats – FFmpeg formats"
---

<h2 class="name">NAME</h2>
<p> ffmpeg-formats &#8211; FFmpeg formats </p>
<h2>DESCRIPTION</h2>
<p> This document describes the supported formats (muxers and demuxers) provided by the libavformat library.</p>
<h2>FORMAT OPTIONS</h2>
<p> The libavformat library provides some generic global options, which can be set on all the muxers and demuxers. In addition each muxer or demuxer may support so-called private options, which are specific for that component. </p>
<p> Options may be set by specifying &#8211;<i>option</i> <i>value</i> in the FFmpeg tools, or by setting the value explicitly in the <tt>&quot;AVFormatContext&quot;</tt> options or using the <i>libavutil/opt.h</i> <font SIZE="-1">API</font> for programmatic use. </p>
<p> The list of supported options follows:</p>
<dl>
<dt><code>avioflags</code> <i>flags</i> <code>(</code><i>input/output</i><code>)</code></p>
<dd> Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>direct</code></p>
<dd> Reduce buffering.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>probesize</code> <i>integer</i> <code>(</code><i>input</i><code>)</code></p>
<dd> Set probing size in bytes, i.e. the size of the data to analyze to get stream information. A higher value will enable detecting more information in case it is dispersed into the stream, but will increase latency. Must be an integer not lesser than 32. It is 5000000 by default.</p>
<dt><code>max_probe_packets</code> <i>integer</i> <code>(</code><i>input</i><code>)</code></p>
<dd> Set the maximum number of buffered packets when probing a codec. Default is 2500 packets.</p>
<dt><code>packetsize</code> <i>integer</i> <code>(</code><i>output</i><code>)</code></p>
<dd> Set packet size.</p>
<dt><code>fflags</code> <i>flags</i></p>
<dd> Set format flags. Some are implemented for a limited number of formats. </p>
<p> Possible values for input files:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>discardcorrupt</code></p>
<dd> Discard corrupted packets.</p>
<dt><code>fastseek</code></p>
<dd> Enable fast, but inaccurate seeks for some formats.</p>
<dt><code>genpts</code></p>
<dd> Generate missing <font SIZE="-1">PTS</font> if <font SIZE="-1">DTS</font> is present.</p>
<dt><code>igndts</code></p>
<dd> Ignore <font SIZE="-1">DTS</font> if <font SIZE="-1">PTS</font> is set. Inert when nofillin is set.</p>
<dt><code>ignidx</code></p>
<dd> Ignore index.</p>
<dt><code>keepside (</code><i>deprecated</i><code>,</code><i>inert</i><code>)</code></p>
<dd>
<dt><code>nobuffer</code></p>
<dd> Reduce the latency introduced by buffering during initial input streams analysis.</p>
<dt><code>nofillin</code></p>
<dd> Do not fill in missing values in packet fields that can be exactly calculated.</p>
<dt><code>noparse</code></p>
<dd> Disable AVParsers, this needs <tt>&quot;+nofillin&quot;</tt> too.</p>
<dt><code>sortdts</code></p>
<dd> Try to interleave output packets by <font SIZE="-1">DTS.</font> At present, available only for AVIs with an index.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Possible values for output files:</p>
<dl>
<dt><code>autobsf</code></p>
<dd> Automatically apply bitstream filters as required by the output format. Enabled by default.</p>
<dt><code>bitexact</code></p>
<dd> Only write platform-, build- and time-independent data. This ensures that file and data checksums are reproducible and match between platforms. Its primary use is for regression testing.</p>
<dt><code>flush_packets</code></p>
<dd> Write out packets immediately.</p>
<dt><code>latm (</code><i>deprecated</i><code>,</code><i>inert</i><code>)</code></p>
<dd>
<dt><code>shortest</code></p>
<dd> Stop muxing at the end of the shortest stream. It may be needed to increase max_interleave_delta to avoid flushing the longer streams before <font SIZE="-1">EOF.</font></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>seek2any</code> <i>integer</i> <code>(</code><i>input</i><code>)</code></p>
<dd> Allow seeking to non-keyframes on demuxer level when supported if set to 1. Default is 0.</p>
<dt><code>analyzeduration</code> <i>integer</i> <code>(</code><i>input</i><code>)</code></p>
<dd> Specify how many microseconds are analyzed to probe the input. A higher value will enable detecting more accurate information, but will increase latency. It defaults to 5,000,000 microseconds = 5 seconds.</p>
<dt><code>cryptokey</code> <i>hexadecimal string</i> <code>(</code><i>input</i><code>)</code></p>
<dd> Set decryption key.</p>
<dt><code>indexmem</code> <i>integer</i> <code>(</code><i>input</i><code>)</code></p>
<dd> Set max memory used for timestamp index (per stream).</p>
<dt><code>rtbufsize</code> <i>integer</i> <code>(</code><i>input</i><code>)</code></p>
<dd> Set max memory used for buffering real-time frames.</p>
<dt><code>fdebug</code> <i>flags</i> <code>(</code><i>input/output</i><code>)</code></p>
<dd> Print specific debug info. </p>
<p> Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>ts</code></p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>max_delay</code> <i>integer</i> <code>(</code><i>input/output</i><code>)</code></p>
<dd> Set maximum muxing or demuxing delay in microseconds.</p>
<dt><code>fpsprobesize</code> <i>integer</i> <code>(</code><i>input</i><code>)</code></p>
<dd> Set number of frames used to probe fps.</p>
<dt><code>audio_preload</code> <i>integer</i> <code>(</code><i>output</i><code>)</code></p>
<dd> Set microseconds by which audio packets should be interleaved earlier.</p>
<dt><code>chunk_duration</code> <i>integer</i> <code>(</code><i>output</i><code>)</code></p>
<dd> Set microseconds for each chunk.</p>
<dt><code>chunk_size</code> <i>integer</i> <code>(</code><i>output</i><code>)</code></p>
<dd> Set size in bytes for each chunk.</p>
<dt><code>err_detect, f_err_detect</code> <i>flags</i> <code>(</code><i>input</i><code>)</code></p>
<dd> Set error detection flags. <tt>&quot;f_err_detect&quot;</tt> is deprecated and should be used only via the <code>ffmpeg</code> tool. </p>
<p> Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>crccheck</code></p>
<dd> Verify embedded CRCs.</p>
<dt><code>bitstream</code></p>
<dd> Detect bitstream specification deviations.</p>
<dt><code>buffer</code></p>
<dd> Detect improper bitstream length.</p>
<dt><code>explode</code></p>
<dd> Abort decoding on minor error detection.</p>
<dt><code>careful</code></p>
<dd> Consider things that violate the spec and have not been seen in the wild as errors.</p>
<dt><code>compliant</code></p>
<dd> Consider all spec non compliancies as errors.</p>
<dt><code>aggressive</code></p>
<dd> Consider things that a sane encoder should not do as an error.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>max_interleave_delta</code> <i>integer</i> <code>(</code><i>output</i><code>)</code></p>
<dd> Set maximum buffering duration for interleaving. The duration is expressed in microseconds, and defaults to 10000000 (10 seconds). </p>
<p> To ensure all the streams are interleaved correctly, libavformat will wait until it has at least one packet for each stream before actually writing any packets to the output file. When some streams are &#8220;sparse&#8221; (i.e. there are large gaps between successive packets), this can result in excessive buffering. </p>
<p> This field specifies the maximum difference between the timestamps of the first and the last packet in the muxing queue, above which libavformat will output a packet regardless of whether it has queued a packet for all the streams. </p>
<p> If set to 0, libavformat will continue buffering packets until it has a packet for each stream, regardless of the maximum timestamp difference between the buffered packets.</p>
<dt><code>use_wallclock_as_timestamps</code> <i>integer</i> <code>(</code><i>input</i><code>)</code></p>
<dd> Use wallclock as timestamps if set to 1. Default is 0.</p>
<dt><code>avoid_negative_ts</code> <i>integer</i> <code>(</code><i>output</i><code>)</code></p>
<dd> Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>make_non_negative</code></p>
<dd> Shift timestamps to make them non-negative. Also note that this affects only leading negative timestamps, and not non-monotonic negative timestamps.</p>
<dt><code>make_zero</code></p>
<dd> Shift timestamps so that the first timestamp is 0.</p>
<dt><code>auto (default)</code></p>
<dd> Enables shifting when required by the target format.</p>
<dt><code>disabled</code></p>
<dd> Disables shifting of timestamp.</dl>
</dl>
<dl>
<dt>
<dd>
<p> When shifting is enabled, all output timestamps are shifted by the same amount. Audio, video, and subtitles desynching and relative timestamp differences are preserved compared to how they would have been without shifting.</dl>
<dt><code>skip_initial_bytes</code> <i>integer</i> <code>(</code><i>input</i><code>)</code></p>
<dd> Set number of bytes to skip before reading header and frames if set to 1. Default is 0.</p>
<dt><code>correct_ts_overflow</code> <i>integer</i> <code>(</code><i>input</i><code>)</code></p>
<dd> Correct single timestamp overflows if set to 1. Default is 1.</p>
<dt><code>flush_packets</code> <i>integer</i> <code>(</code><i>output</i><code>)</code></p>
<dd> Flush the underlying I/O stream after each packet. Default is -1 (auto), which means that the underlying protocol will decide, 1 enables it, and has the effect of reducing the latency, 0 disables it and may increase <font SIZE="-1">IO</font> throughput in some cases.</p>
<dt><code>output_ts_offset</code> <i>offset</i> <code>(</code><i>output</i><code>)</code></p>
<dd> Set the output time offset. </p>
<p> <i>offset</i> must be a time duration specification, see <code>the Time duration section in the <a href="/docs/linux/man/1-ffmpeg-utils/">ffmpeg-utils</a>(1) manual</code>. </p>
<p> The offset is added by the muxer to the output timestamps. </p>
<p> Specifying a positive offset means that the corresponding streams are delayed bt the time duration specified in <i>offset</i>. Default value is <tt>0</tt> (meaning that no offset is applied).</p>
<dt><code>format_whitelist</code> <i>list</i> <code>(</code><i>input</i><code>)</code></p>
<dd> &#8220;,&#8221; separated list of allowed demuxers. By default all are allowed.</p>
<dt><code>dump_separator</code> <i>string</i> <code>(</code><i>input</i><code>)</code></p>
<dd> Separator used to separate the fields printed on the command line about the Stream parameters. For example, to separate the fields with newlines and indentation: </p>
<pre>
        ffprobe -dump_separator &quot;
                                  &quot;  -i ~/videos/matrixbench_mpeg2.mpg
</pre>
<dt><code>max_streams</code> <i>integer</i> <code>(</code><i>input</i><code>)</code></p>
<dd> Specifies the maximum number of streams. This can be used to reject files that would require too many resources due to a large number of streams.</p>
<dt><code>skip_estimate_duration_from_pts</code> <i>bool</i> <code>(</code><i>input</i><code>)</code></p>
<dd> Skip estimation of input duration when calculated using <font SIZE="-1">PTS.</font> At present, applicable for MPEG-PS and MPEG-TS.</p>
<dt><code>strict, f_strict</code> <i>integer</i> <code>(</code><i>input/output</i><code>)</code></p>
<dd> Specify how strictly to follow the standards. <tt>&quot;f_strict&quot;</tt> is deprecated and should be used only via the <code>ffmpeg</code> tool. </p>
<p> Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>very</code></p>
<dd> strictly conform to an older more strict version of the spec or reference software</p>
<dt><code>strict</code></p>
<dd> strictly conform to all the things in the spec no matter what consequences</p>
<dt><code>normal</code></p>
<dd>
<dt><code>unofficial</code></p>
<dd> allow unofficial extensions</p>
<dt><code>experimental</code></p>
<dd> allow non standardized experimental things, experimental (unfinished/work in progress/not well tested) decoders and encoders. Note: experimental decoders can pose a security risk, do not use this for decoding untrusted input.</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h3>Format stream specifiers</h3>
<p> Format stream specifiers allow selection of one or more streams that match specific properties. </p>
<p> The exact semantics of stream specifiers is defined by the <tt>&quot;avformat_match_stream_specifier()&quot;</tt> function declared in the <i>libavformat/avformat.h</i> header and documented in the <code>Stream specifiers section in the <a href="/docs/linux/man/1-ffmpeg/">ffmpeg</a>(1) manual</code>.</p>
<h2>DEMUXERS</h2>
<p> Demuxers are configured elements in FFmpeg that can read the multimedia streams from a particular type of file. </p>
<p> When you configure your FFmpeg build, all the supported demuxers are enabled by default. You can list all available ones using the configure option <tt>&quot;--list-demuxers&quot;</tt>. </p>
<p> You can disable all the demuxers using the configure option <tt>&quot;--disable-demuxers&quot;</tt>, and selectively enable a single demuxer with the option <tt>&quot;--enable-demuxer=</tt>DEMUXER<tt>&quot;</tt>, or disable it with the option <tt>&quot;--disable-demuxer=</tt>DEMUXER<tt>&quot;</tt>. </p>
<p> The option <tt>&quot;-demuxers&quot;</tt> of the ff* tools will display the list of enabled demuxers. Use <tt>&quot;-formats&quot;</tt> to view a combined list of enabled demuxers and muxers. </p>
<p> The description of some of the currently available demuxers follows.</p>
<h3>aa</h3>
<p> Audible Format 2, 3, and 4 demuxer. </p>
<p> This demuxer is used to demux Audible Format 2, 3, and 4 (.aa) files.</p>
<h3>apng</h3>
<p> Animated Portable Network Graphics demuxer. </p>
<p> This demuxer is used to demux <font SIZE="-1">APNG</font> files. All headers, but the <font SIZE="-1">PNG</font> signature, up to (but not including) the first fcTL chunk are transmitted as extradata. Frames are then split as being all the chunks between two fcTL ones, or between the last fcTL and <font SIZE="-1">IEND</font> chunks.</p>
<dl>
<dt><code>-ignore_loop</code> <i>bool</i></p>
<dd> Ignore the loop variable in the file if set.</p>
<dt><code>-max_fps</code> <i>int</i></p>
<dd> Maximum framerate in frames per second (0 for no limit).</p>
<dt><code>-default_fps</code> <i>int</i></p>
<dd> Default framerate in frames per second when none is specified in the file (0 meaning as fast as possible).</dl>
<h3>asf</h3>
<p> Advanced Systems Format demuxer. </p>
<p> This demuxer is used to demux <font SIZE="-1">ASF</font> files and <font SIZE="-1">MMS</font> network streams.</p>
<dl>
<dt><code>-no_resync_search</code> <i>bool</i></p>
<dd> Do not try to resynchronize by looking for a certain optional start code.</dl>
<h3>concat</h3>
<p> Virtual concatenation script demuxer. </p>
<p> This demuxer reads a list of files and other directives from a text file and demuxes them one after the other, as if all their packets had been muxed together. </p>
<p> The timestamps in the files are adjusted so that the first file starts at 0 and each next file starts where the previous one finishes. Note that it is done globally and may cause gaps if all streams do not have exactly the same length. </p>
<p> All files must have the same streams (same codecs, same time base, etc.). </p>
<p> The duration of each file is used to adjust the timestamps of the next file: if the duration is incorrect (because it was computed using the bit-rate or because the file is truncated, for example), it can cause artifacts. The <tt>&quot;duration&quot;</tt> directive can be used to override the duration stored in each file. </p>
<p> <i>Syntax</i> </p>
<p> The script is a text file in extended-ASCII, with one directive per line. Empty lines, leading spaces and lines starting with &#8216;#&#8217; are ignored. The following directive is recognized:</p>
<dl>
<dt>&quot;file path&quot;</p>
<dd> Path to a file to read; special characters and spaces must be escaped with backslash or single quotes. </p>
<p> All subsequent file-related directives apply to that file.</p>
<dt>&quot;ffconcat version 1.0&quot;</p>
<dd> Identify the script type and version. It also sets the <code>safe</code> option to 1 if it was -1. </p>
<p> To make FFmpeg recognize the format automatically, this directive must appear exactly as is (no extra space or byte-order-mark) on the very first line of the script.</p>
<dt>&quot;duration dur&quot;</p>
<dd> Duration of the file. This information can be specified from the file; specifying it here may be more efficient or help if the information from the file is not available or accurate. </p>
<p> If the duration is set for all files, then it is possible to seek in the whole concatenated video.</p>
<dt>&quot;inpoint timestamp&quot;</p>
<dd> In point of the file. When the demuxer opens the file it instantly seeks to the specified timestamp. Seeking is done so that all streams can be presented successfully at In point. </p>
<p> This directive works best with intra frame codecs, because for non-intra frame ones you will usually get extra packets before the actual In point and the decoded content will most likely contain frames before In point too. </p>
<p> For each file, packets before the file In point will have timestamps less than the calculated start timestamp of the file (negative in case of the first file), and the duration of the files (if not specified by the <tt>&quot;duration&quot;</tt> directive) will be reduced based on their specified In point. </p>
<p> Because of potential packets before the specified In point, packet timestamps may overlap between two concatenated files.</p>
<dt>&quot;outpoint timestamp&quot;</p>
<dd> Out point of the file. When the demuxer reaches the specified decoding timestamp in any of the streams, it handles it as an end of file condition and skips the current and all the remaining packets from all streams. </p>
<p> Out point is exclusive, which means that the demuxer will not output packets with a decoding timestamp greater or equal to Out point. </p>
<p> This directive works best with intra frame codecs and formats where all streams are tightly interleaved. For non-intra frame codecs you will usually get additional packets with presentation timestamp after Out point therefore the decoded content will most likely contain frames after Out point too. If your streams are not tightly interleaved you may not get all the packets from all streams before Out point and you may only will be able to decode the earliest stream until Out point. </p>
<p> The duration of the files (if not specified by the <tt>&quot;duration&quot;</tt> directive) will be reduced based on their specified Out point.</p>
<dt>&quot;file_packet_metadata key=value&quot;</p>
<dd> Metadata of the packets of the file. The specified metadata will be set for each file packet. You can specify this directive multiple times to add multiple metadata entries.</p>
<dt>&quot;stream&quot;</p>
<dd> Introduce a stream in the virtual file. All subsequent stream-related directives apply to the last introduced stream. Some streams properties must be set in order to allow identifying the matching streams in the subfiles. If no streams are defined in the script, the streams from the first file are copied.</p>
<dt>&quot;exact_stream_id id&quot;</p>
<dd> Set the id of the stream. If this directive is given, the string with the corresponding id in the subfiles will be used. This is especially useful for MPEG-PS (<font SIZE="-1">VOB</font>) files, where the order of the streams is not reliable.</dl>
<p> <i>Options</i> </p>
<p> This demuxer accepts the following option:</p>
<dl>
<dt><code>safe</code></p>
<dd> If set to 1, reject unsafe file paths. A file path is considered safe if it does not contain a protocol specification and is relative and all components only contain characters from the portable character set (letters, digits, period, underscore and hyphen) and have no period at the beginning of a component. </p>
<p> If set to 0, any file name is accepted. </p>
<p> The default is 1. </p>
<p> -1 is equivalent to 1 if the format was automatically probed and 0 otherwise.</p>
<dt><code>auto_convert</code></p>
<dd> If set to 1, try to perform automatic conversions on packet data to make the streams concatenable. The default is 1. </p>
<p> Currently, the only conversion is adding the h264_mp4toannexb bitstream filter to H.264 streams in <font SIZE="-1">MP4</font> format. This is necessary in particular if there are resolution changes.</p>
<dt><code>segment_time_metadata</code></p>
<dd> If set to 1, every packet will contain the <i>lavf.concat.start_time</i> and the <i>lavf.concat.duration</i> packet metadata values which are the start_time and the duration of the respective file segments in the concatenated output expressed in microseconds. The duration metadata is only set if it is known based on the concat file. The default is 0.</dl>
<p> <i>Examples</i></p>
<dl>
<dt>&bull;</p>
<dd> Use absolute filenames and include some comments: </p>
<pre>
        # my first filename
        file /mnt/share/file-1.wav
        # my second filename including whitespace
        file '/mnt/share/file 2.wav'
        # my third filename including whitespace plus single quote
        file '/mnt/share/file 3'\''.wav'
</pre>
<dt>&bull;</p>
<dd> Allow for input format auto-probing, use safe filenames and set the duration of the first file: </p>
<pre>
        ffconcat version 1.0
        
        file file-1.wav
        duration 20.0
        
        file subdir/file-2.wav
</pre>
</dl>
<h3>dash</h3>
<p> Dynamic Adaptive Streaming over <font SIZE="-1">HTTP</font> demuxer. </p>
<p> This demuxer presents all AVStreams found in the manifest. By setting the discard flags on AVStreams the caller can decide which streams to actually receive. Each stream mirrors the <tt>&quot;id&quot;</tt> and <tt>&quot;bandwidth&quot;</tt> properties from the <tt>&quot;&lt;Representation&gt;&quot;</tt> as metadata keys named &#8220;id&#8221; and &#8220;variant_bitrate&#8221; respectively.</p>
<h3>flv, live_flv</h3>
<p> Adobe Flash Video Format demuxer. </p>
<p> This demuxer is used to demux <font SIZE="-1">FLV</font> files and <font SIZE="-1">RTMP</font> network streams. In case of live network streams, if you force format, you may use live_flv option instead of flv to survive timestamp discontinuities. </p>
<pre>
        ffmpeg -f flv -i myfile.flv ...
        ffmpeg -f live_flv -i rtmp://&lt;any.server&gt;/anything/key ....
</pre>
<dl>
<dt><code>-flv_metadata</code> <i>bool</i></p>
<dd> Allocate the streams according to the onMetaData array content.</p>
<dt><code>-flv_ignore_prevtag</code> <i>bool</i></p>
<dd> Ignore the size of previous tag value.</p>
<dt><code>-flv_full_metadata</code> <i>bool</i></p>
<dd> Output all context of the onMetadata.</dl>
<h3>gif</h3>
<p> Animated <font SIZE="-1">GIF</font> demuxer. </p>
<p> It accepts the following options:</p>
<dl>
<dt><code>min_delay</code></p>
<dd> Set the minimum valid delay between frames in hundredths of seconds. Range is 0 to 6000. Default value is 2.</p>
<dt><code>max_gif_delay</code></p>
<dd> Set the maximum valid delay between frames in hundredth of seconds. Range is 0 to 65535. Default value is 65535 (nearly eleven minutes), the maximum value allowed by the specification.</p>
<dt><code>default_delay</code></p>
<dd> Set the default delay between frames in hundredths of seconds. Range is 0 to 6000. Default value is 10.</p>
<dt><code>ignore_loop</code></p>
<dd> <font SIZE="-1">GIF</font> files can contain information to loop a certain number of times (or infinitely). If <code>ignore_loop</code> is set to 1, then the loop setting from the input will be ignored and looping will not occur. If set to 0, then looping will occur and will cycle the number of times according to the <font SIZE="-1">GIF.</font> Default value is 1.</dl>
<p> For example, with the overlay filter, place an infinitely looping <font SIZE="-1">GIF</font> over another video: </p>
<pre>
        ffmpeg -i input.mp4 -ignore_loop 0 -i input.gif -filter_complex overlay=shortest=1 out.mkv
</pre>
<p> Note that in the above example the shortest option for overlay filter is used to end the output video at the length of the shortest input file, which in this case is <i>input.mp4</i> as the <font SIZE="-1">GIF</font> in this example loops infinitely.</p>
<h3>hls</h3>
<p> <font SIZE="-1">HLS</font> demuxer </p>
<p> Apple <font SIZE="-1">HTTP</font> Live Streaming demuxer. </p>
<p> This demuxer presents all AVStreams from all variant streams. The id field is set to the bitrate variant index number. By setting the discard flags on AVStreams (by pressing &#8216;a&#8217; or &#8216;v&#8217; in ffplay), the caller can decide which variant streams to actually receive. The total bitrate of the variant that the stream belongs to is available in a metadata key named &#8220;variant_bitrate&#8221;. </p>
<p> It accepts the following options:</p>
<dl>
<dt><code>live_start_index</code></p>
<dd> segment index to start live streams at (negative values are from the end).</p>
<dt><code>allowed_extensions</code></p>
<dd> &#8216;,&#8217; separated list of file extensions that hls is allowed to access.</p>
<dt><code>max_reload</code></p>
<dd> Maximum number of times a insufficient list is attempted to be reloaded. Default value is 1000.</p>
<dt><code>m3u8_hold_counters</code></p>
<dd> The maximum number of times to load m3u8 when it refreshes without new segments. Default value is 1000.</p>
<dt><code>http_persistent</code></p>
<dd> Use persistent <font SIZE="-1">HTTP</font> connections. Applicable only for <font SIZE="-1">HTTP</font> streams. Enabled by default.</p>
<dt><code>http_multiple</code></p>
<dd> Use multiple <font SIZE="-1">HTTP</font> connections for downloading <font SIZE="-1">HTTP</font> segments. Enabled by default for <font SIZE="-1">HTTP/1.1</font> servers.</p>
<dt><code>http_seekable</code></p>
<dd> Use <font SIZE="-1">HTTP</font> partial requests for downloading <font SIZE="-1">HTTP</font> segments. 0 = disable, 1 = enable, -1 = auto, Default is auto.</dl>
<h3>image2</h3>
<p> Image file demuxer. </p>
<p> This demuxer reads from a list of image files specified by a pattern. The syntax and meaning of the pattern is specified by the option <i>pattern_type</i>. </p>
<p> The pattern may contain a suffix which is used to automatically determine the format of the images contained in the files. </p>
<p> The size, the pixel format, and the format of each image must be the same for all the files in the sequence. </p>
<p> This demuxer accepts the following options:</p>
<dl>
<dt><code>framerate</code></p>
<dd> Set the frame rate for the video stream. It defaults to 25.</p>
<dt><code>loop</code></p>
<dd> If set to 1, loop over the input. Default value is 0.</p>
<dt><code>pattern_type</code></p>
<dd> Select the pattern type used to interpret the provided filename. </p>
<p> <i>pattern_type</i> accepts one of the following values.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>none</code></p>
<dd> Disable pattern matching, therefore the video will only contain the specified image. You should use this option if you do not want to create sequences from multiple images and your filenames may contain special pattern characters.</p>
<dt><code>sequence</code></p>
<dd> Select a sequence pattern type, used to specify a sequence of files indexed by sequential numbers. </p>
<p> A sequence pattern may contain the string &#8220;%d&#8221; or &quot;%0<i>N</i>d&#8220;, which specifies the position of the characters representing a sequential number in each filename matched by the pattern. If the form &#8221;%d0<i>N</i>d&quot; is used, the string representing the number in each filename is 0-padded and <i>N</i> is the total number of 0-padded digits representing the number. The literal character &#8216;%&#8217; can be specified in the pattern with the string &#8220;%%&#8221;. </p>
<p> If the sequence pattern contains &#8220;%d&#8221; or &quot;%0<i>N</i>d&quot;, the first filename of the file list specified by the pattern must contain a number inclusively contained between <i>start_number</i> and <i>start_number</i>+<i>start_number_range</i>-1, and all the following numbers must be sequential. </p>
<p> For example the pattern &#8220;img-%03d.bmp&#8221; will match a sequence of filenames of the form <i>img-001.bmp</i>, <i>img-002.bmp</i>, &#8230;, <i>img-010.bmp</i>, etc.; the pattern &#8220;i%%m%%g-%d.jpg&#8221; will match a sequence of filenames of the form <i>i%m%g-1.jpg</i>, <i>i%m%g-2.jpg</i>, &#8230;, <i>i%m%g-10.jpg</i>, etc. </p>
<p> Note that the pattern must not necessarily contain &#8220;%d&#8221; or &quot;%0<i>N</i>d&quot;, for example to convert a single image file <i>img.jpeg</i> you can employ the command: </p>
<pre>
        ffmpeg -i img.jpeg img.png
</pre>
<dt><code>glob</code></p>
<dd> Select a glob wildcard pattern type. </p>
<p> The pattern is interpreted like a <tt>&quot;glob()&quot;</tt> pattern. This is only selectable if libavformat was compiled with globbing support.</p>
<dt><code>glob_sequence</code> <i>(deprecated, will be removed)</i></p>
<dd> Select a mixed glob wildcard/sequence pattern. </p>
<p> If your version of libavformat was compiled with globbing support, and the provided pattern contains at least one glob meta character among <tt>&quot;%*?[]{}&quot;</tt> that is preceded by an unescaped &#8220;%&#8221;, the pattern is interpreted like a <tt>&quot;glob()&quot;</tt> pattern, otherwise it is interpreted like a sequence pattern. </p>
<p> All glob special characters <tt>&quot;%*?[]{}&quot;</tt> must be prefixed with &#8220;%&#8221;. To escape a literal &#8220;%&#8221; you shall use &#8220;%%&#8221;. </p>
<p> For example the pattern <tt>&quot;foo-%*.jpeg&quot;</tt> will match all the filenames prefixed by &#8220;foo-&#8221; and terminating with &#8220;.jpeg&#8221;, and <tt>&quot;foo-%?%?%?.jpeg&quot;</tt> will match all the filenames prefixed with &#8220;foo-&#8221;, followed by a sequence of three characters, and terminating with &#8220;.jpeg&#8221;. </p>
<p> This pattern type is deprecated in favor of <i>glob</i> and <i>sequence</i>.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Default value is <i>glob_sequence</i>.</dl>
<dt><code>pixel_format</code></p>
<dd> Set the pixel format of the images to read. If not specified the pixel format is guessed from the first image file in the sequence.</p>
<dt><code>start_number</code></p>
<dd> Set the index of the file matched by the image file pattern to start to read from. Default value is 0.</p>
<dt><code>start_number_range</code></p>
<dd> Set the index interval range to check when looking for the first image file in the sequence, starting from <i>start_number</i>. Default value is 5.</p>
<dt><code>ts_from_file</code></p>
<dd> If set to 1, will set frame timestamp to modification time of image file. Note that monotonity of timestamps is not provided: images go in the same order as without this option. Default value is 0. If set to 2, will set frame timestamp to the modification time of the image file in nanosecond precision.</p>
<dt><code>video_size</code></p>
<dd> Set the video size of the images to read. If not specified the video size is guessed from the first image file in the sequence.</p>
<dt><code>export_path_metadata</code></p>
<dd> If set to 1, will add two extra fields to the metadata found in input, making them also available for other filters (see <i>drawtext</i> filter for examples). Default value is 0. The extra fields are described below:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>lavf.image2dec.source_path</code></p>
<dd> Corresponds to the full path to the input file being read.</p>
<dt><code>lavf.image2dec.source_basename</code></p>
<dd> Corresponds to the name of the file being read.</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<p> <i>Examples</i></p>
<dl>
<dt>&bull;</p>
<dd> Use <code>ffmpeg</code> for creating a video from the images in the file sequence <i>img-001.jpeg</i>, <i>img-002.jpeg</i>, &#8230;, assuming an input frame rate of 10 frames per second: </p>
<pre>
        ffmpeg -framerate 10 -i 'img-%03d.jpeg' out.mkv
</pre>
<dt>&bull;</p>
<dd> As above, but start by reading from a file with index 100 in the sequence: </p>
<pre>
        ffmpeg -framerate 10 -start_number 100 -i 'img-%03d.jpeg' out.mkv
</pre>
<dt>&bull;</p>
<dd> Read images matching the &#8220;*.png&#8221; glob pattern , that is all the files terminating with the &#8220;.png&#8221; suffix: </p>
<pre>
        ffmpeg -framerate 10 -pattern_type glob -i &quot;*.png&quot; out.mkv
</pre>
</dl>
<h3>libgme</h3>
<p> The Game Music Emu library is a collection of video game music file emulators. </p>
<p> See &lt;<code><a rel="nofollow" href="https://bitbucket.org/mpyne/game-music-emu/overview">https://bitbucket.org/mpyne/game-music-emu/overview</a></code>&gt; for more information. </p>
<p> It accepts the following options:</p>
<dl>
<dt><code>track_index</code></p>
<dd> Set the index of which track to demux. The demuxer can only export one track. Track indexes start at 0. Default is to pick the first track. Number of tracks is exported as <i>tracks</i> metadata entry.</p>
<dt><code>sample_rate</code></p>
<dd> Set the sampling rate of the exported track. Range is 1000 to 999999. Default is 44100.</p>
<dt><code>max_size</code> <i>(bytes)</i></p>
<dd> The demuxer buffers the entire file into memory. Adjust this value to set the maximum buffer size, which in turn, acts as a ceiling for the size of files that can be read. Default is 50 MiB.</dl>
<h3>libmodplug</h3>
<p> ModPlug based module demuxer </p>
<p> See &lt;<code><a rel="nofollow" href="https://github.com/Konstanty/libmodplug">https://github.com/Konstanty/libmodplug</a></code>&gt; </p>
<p> It will export one 2-channel 16-bit 44.1 kHz audio stream. Optionally, a <tt>&quot;pal8&quot;</tt> 16-color video stream can be exported with or without printed metadata. </p>
<p> It accepts the following options:</p>
<dl>
<dt><code>noise_reduction</code></p>
<dd> Apply a simple low-pass filter. Can be 1 (on) or 0 (off). Default is 0.</p>
<dt><code>reverb_depth</code></p>
<dd> Set amount of reverb. Range 0-100. Default is 0.</p>
<dt><code>reverb_delay</code></p>
<dd> Set delay in ms, clamped to 40-250 ms. Default is 0.</p>
<dt><code>bass_amount</code></p>
<dd> Apply bass expansion a.k.a. XBass or megabass. Range is 0 (quiet) to 100 (loud). Default is 0.</p>
<dt><code>bass_range</code></p>
<dd> Set cutoff i.e. upper-bound for bass frequencies. Range is 10-100 Hz. Default is 0.</p>
<dt><code>surround_depth</code></p>
<dd> Apply a Dolby Pro-Logic surround effect. Range is 0 (quiet) to 100 (heavy). Default is 0.</p>
<dt><code>surround_delay</code></p>
<dd> Set surround delay in ms, clamped to 5-40 ms. Default is 0.</p>
<dt><code>max_size</code></p>
<dd> The demuxer buffers the entire file into memory. Adjust this value to set the maximum buffer size, which in turn, acts as a ceiling for the size of files that can be read. Range is 0 to 100 MiB. 0 removes buffer size limit (not recommended). Default is 5 MiB.</p>
<dt><code>video_stream_expr</code></p>
<dd> String which is evaluated using the eval <font SIZE="-1">API</font> to assign colors to the generated video stream. Variables which can be used are <tt>&quot;x&quot;</tt>, <tt>&quot;y&quot;</tt>, <tt>&quot;w&quot;</tt>, <tt>&quot;h&quot;</tt>, <tt>&quot;t&quot;</tt>, <tt>&quot;speed&quot;</tt>, <tt>&quot;tempo&quot;</tt>, <tt>&quot;order&quot;</tt>, <tt>&quot;pattern&quot;</tt> and <tt>&quot;row&quot;</tt>.</p>
<dt><code>video_stream</code></p>
<dd> Generate video stream. Can be 1 (on) or 0 (off). Default is 0.</p>
<dt><code>video_stream_w</code></p>
<dd> Set video frame width in &#8216;chars&#8217; where one char indicates 8 pixels. Range is 20-512. Default is 30.</p>
<dt><code>video_stream_h</code></p>
<dd> Set video frame height in &#8216;chars&#8217; where one char indicates 8 pixels. Range is 20-512. Default is 30.</p>
<dt><code>video_stream_ptxt</code></p>
<dd> Print metadata on video stream. Includes <tt>&quot;speed&quot;</tt>, <tt>&quot;tempo&quot;</tt>, <tt>&quot;order&quot;</tt>, <tt>&quot;pattern&quot;</tt>, <tt>&quot;row&quot;</tt> and <tt>&quot;ts&quot;</tt> (time in ms). Can be 1 (on) or 0 (off). Default is 1.</dl>
<h3>libopenmpt</h3>
<p> libopenmpt based module demuxer </p>
<p> See &lt;<code><a rel="nofollow" href="https://lib.openmpt.org/libopenmpt/">https://lib.openmpt.org/libopenmpt/</a></code>&gt; for more information. </p>
<p> Some files have multiple subsongs (tracks) this can be set with the <code>subsong</code> option. </p>
<p> It accepts the following options:</p>
<dl>
<dt><code>subsong</code></p>
<dd> Set the subsong index. This can be either &#8216;all&#8217;, &#8216;auto&#8217;, or the index of the subsong. Subsong indexes start at 0. The default is &#8216;auto&#8217;. </p>
<p> The default value is to let libopenmpt choose.</p>
<dt><code>layout</code></p>
<dd> Set the channel layout. Valid values are 1, 2, and 4 channel layouts. The default value is <font SIZE="-1">STEREO.</font></p>
<dt><code>sample_rate</code></p>
<dd> Set the sample rate for libopenmpt to output. Range is from 1000 to <font SIZE="-1">INT_MAX.</font> The value default is 48000.</dl>
<h3>mov/mp4/3gp</h3>
<p> Demuxer for Quicktime File Format &amp; <font SIZE="-1">ISO/IEC</font> Base Media File Format (<font SIZE="-1">ISO/IEC 14496-12</font> or <font SIZE="-1">MPEG-4</font> Part 12, <font SIZE="-1">ISO/IEC 15444-12</font> or <font SIZE="-1">JPEG 2000</font> Part 12). </p>
<p> Registered extensions: mov, mp4, m4a, 3gp, 3g2, mj2, psp, m4b, ism, ismv, isma, f4v </p>
<p> <i>Options</i> </p>
<p> This demuxer accepts the following options:</p>
<dl>
<dt><code>enable_drefs</code></p>
<dd> Enable loading of external tracks, disabled by default. Enabling this can theoretically leak information in some use cases.</p>
<dt><code>use_absolute_path</code></p>
<dd> Allows loading of external tracks via absolute paths, disabled by default. Enabling this poses a security risk. It should only be enabled if the source is known to be non-malicious.</p>
<dt><code>seek_streams_individually</code></p>
<dd> When seeking, identify the closest point in each stream individually and demux packets in that stream from identified point. This can lead to a different sequence of packets compared to demuxing linearly from the beginning. Default is true.</p>
<dt><code>ignore_editlist</code></p>
<dd> Ignore any edit list atoms. The demuxer, by default, modifies the stream index to reflect the timeline described by the edit list. Default is false.</p>
<dt><code>advanced_editlist</code></p>
<dd> Modify the stream index to reflect the timeline described by the edit list. <tt>&quot;ignore_editlist&quot;</tt> must be set to false for this option to be effective. If both <tt>&quot;ignore_editlist&quot;</tt> and this option are set to false, then only the start of the stream index is modified to reflect initial dwell time or starting timestamp described by the edit list. Default is true.</p>
<dt><code>ignore_chapters</code></p>
<dd> Don&#8217;t parse chapters. This includes GoPro &#8216;HiLight&#8217; tags/moments. Note that chapters are only parsed when input is seekable. Default is false.</p>
<dt><code>use_mfra_for</code></p>
<dd> For seekable fragmented input, set fragment&#8217;s starting timestamp from media fragment random access box, if present. </p>
<p> Following options are available:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>auto</code></p>
<dd> Auto-detect whether to set mfra timestamps as <font SIZE="-1">PTS</font> or <font SIZE="-1">DTS</font> <i>(default)</i></p>
<dt><code>dts</code></p>
<dd> Set mfra timestamps as <font SIZE="-1">DTS</font></p>
<dt><code>pts</code></p>
<dd> Set mfra timestamps as <font SIZE="-1">PTS</font></p>
<dt><code>0</code></p>
<dd> Don&#8217;t use mfra box to set timestamps</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>export_all</code></p>
<dd> Export unrecognized boxes within the <i>udta</i> box as metadata entries. The first four characters of the box type are set as the key. Default is false.</p>
<dt><code>export_xmp</code></p>
<dd> Export entire contents of <i></i><font SIZE="-1"><i>XMP_</i></font><i></i> box and <i>uuid</i> box as a string with key <tt>&quot;xmp&quot;</tt>. Note that if <tt>&quot;export_all&quot;</tt> is set and this option isn&#8217;t, the contents of <i></i><font SIZE="-1"><i>XMP_</i></font><i></i> box are still exported but with key <tt>&quot;XMP_&quot;</tt>. Default is false.</p>
<dt><code>activation_bytes</code></p>
<dd> 4-byte key required to decrypt Audible <font SIZE="-1">AAX</font> and <font SIZE="-1">AAX+</font> files. See Audible <font SIZE="-1">AAX</font> subsection below.</p>
<dt><code>audible_fixed_key</code></p>
<dd> Fixed key used for handling Audible <font SIZE="-1">AAX/AAX+</font> files. It has been pre-set so should not be necessary to specify.</p>
<dt><code>decryption_key</code></p>
<dd> 16-byte key, in hex, to decrypt files encrypted using <font SIZE="-1">ISO</font> Common Encryption (<font SIZE="-1">CENC/AES-128 CTR</font>; <font SIZE="-1">ISO/IEC 23001-7</font>).</dl>
<p> <i>Audible </i><font SIZE="-1"><i>AAX</i></font><i></i> </p>
<p> Audible <font SIZE="-1">AAX</font> files are encrypted M4B files, and they can be decrypted by specifying a 4 byte activation secret. </p>
<pre>
        ffmpeg -activation_bytes 1CEB00DA -i test.aax -vn -c:a copy output.mp4
</pre>
<h3>mpegts</h3>
<p> <font SIZE="-1">MPEG-2</font> transport stream demuxer. </p>
<p> This demuxer accepts the following options:</p>
<dl>
<dt><code>resync_size</code></p>
<dd> Set size limit for looking up a new synchronization. Default value is 65536.</p>
<dt><code>skip_unknown_pmt</code></p>
<dd> Skip PMTs for programs not defined in the <font SIZE="-1">PAT.</font> Default value is 0.</p>
<dt><code>fix_teletext_pts</code></p>
<dd> Override teletext packet <font SIZE="-1">PTS</font> and <font SIZE="-1">DTS</font> values with the timestamps calculated from the <font SIZE="-1">PCR</font> of the first program which the teletext stream is part of and is not discarded. Default value is 1, set this option to 0 if you want your teletext packet <font SIZE="-1">PTS</font> and <font SIZE="-1">DTS</font> values untouched.</p>
<dt><code>ts_packetsize</code></p>
<dd> Output option carrying the raw packet size in bytes. Show the detected raw packet size, cannot be set by the user.</p>
<dt><code>scan_all_pmts</code></p>
<dd> Scan and combine all PMTs. The value is an integer with value from -1 to 1 (-1 means automatic setting, 1 means enabled, 0 means disabled). Default value is -1.</p>
<dt><code>merge_pmt_versions</code></p>
<dd> Re-use existing streams when a <font SIZE="-1">PMT</font>&#8216;s version is updated and elementary streams move to different PIDs. Default value is 0.</dl>
<h3>mpjpeg</h3>
<p> <font SIZE="-1">MJPEG</font> encapsulated in multi-part <font SIZE="-1">MIME</font> demuxer. </p>
<p> This demuxer allows reading of <font SIZE="-1">MJPEG,</font> where each frame is represented as a part of multipart/x-mixed-replace stream.</p>
<dl>
<dt><code>strict_mime_boundary</code></p>
<dd> Default implementation applies a relaxed standard to multi-part <font SIZE="-1">MIME</font> boundary detection, to prevent regression with numerous existing endpoints not generating a proper <font SIZE="-1">MIME MJPEG</font> stream. Turning this option on by setting it to 1 will result in a stricter check of the boundary value.</dl>
<h3>rawvideo</h3>
<p> Raw video demuxer. </p>
<p> This demuxer allows one to read raw video data. Since there is no header specifying the assumed video parameters, the user must specify them in order to be able to decode the data correctly. </p>
<p> This demuxer accepts the following options:</p>
<dl>
<dt><code>framerate</code></p>
<dd> Set input video frame rate. Default value is 25.</p>
<dt><code>pixel_format</code></p>
<dd> Set the input video pixel format. Default value is <tt>&quot;yuv420p&quot;</tt>.</p>
<dt><code>video_size</code></p>
<dd> Set the input video size. This value must be specified explicitly.</dl>
<p> For example to read a rawvideo file <i>input.raw</i> with <code>ffplay</code>, assuming a pixel format of <tt>&quot;rgb24&quot;</tt>, a video size of <tt>&quot;320x240&quot;</tt>, and a frame rate of 10 images per second, use the command: </p>
<pre>
        ffplay -f rawvideo -pixel_format rgb24 -video_size 320x240 -framerate 10 input.raw
</pre>
<h3>sbg</h3>
<p> SBaGen script demuxer. </p>
<p> This demuxer reads the script language used by SBaGen &lt;<code><a rel="nofollow" href="http://uazu.net/sbagen/">http://uazu.net/sbagen/</a></code>&gt; to generate binaural beats sessions. A <font SIZE="-1">SBG</font> script looks like that: </p>
<pre><code>
- SE
      a:300 - 2.5 / 3 440 + 4.5 / 0
      b:300 - 2.5 / 0 440 + 4.5 / 3
    off:-NOW == a +
      0:07
       :00 == b +
      0:14
       :00 == a +
      0:21
       :00 == b +
      0:30
       :00 off
</code></pre>
<p> A <font SIZE="-1">SBG</font> script can mix absolute and relative timestamps. If the script uses either only absolute timestamps (including the script start time) or only relative ones, then its layout is fixed, and the conversion is straightforward. On the other hand, if the script mixes both kind of timestamps, then the <i></i><font SIZE="-1"><i>NOW</i></font><i></i> reference for relative timestamps will be taken from the current time of day at the time the script is read, and the script layout will be frozen according to that reference. That means that if the script is directly played, the actual times will match the absolute timestamps up to the sound controller&#8217;s clock accuracy, but if the user somehow pauses the playback or seeks, all times will be shifted accordingly.</p>
<h3>tedcaptions</h3>
<p> <font SIZE="-1">JSON</font> captions used for &lt;<code><a rel="nofollow" href="http://www.ted.com/">http://www.ted.com/</a></code>&gt;. </p>
<p> <font SIZE="-1">TED</font> does not provide links to the captions, but they can be guessed from the page. The file <i>tools/bookmarklets.html</i> from the FFmpeg source tree contains a bookmarklet to expose them. </p>
<p> This demuxer accepts the following option:</p>
<dl>
<dt><code>start_time</code></p>
<dd> Set the start time of the <font SIZE="-1">TED</font> talk, in milliseconds. The default is 15000 (15s). It is used to sync the captions with the downloadable videos, because they include a 15s intro.</dl>
<p> Example: convert the captions to a format most players understand: </p>
<pre>
        ffmpeg -i <a rel="nofollow" href="http://www.ted.com/talks/subtitles/id/1/lang/en">http://www.ted.com/talks/subtitles/id/1/lang/en</a> talk1-en.srt
</pre>
<h3>vapoursynth</h3>
<p> Vapoursynth wrapper. </p>
<p> Due to security concerns, Vapoursynth scripts will not be autodetected so the input format has to be forced. For ff* <font SIZE="-1">CLI</font> tools, add <tt>&quot;-f vapoursynth&quot;</tt> before the input <tt>&quot;-i yourscript.vpy&quot;</tt>. </p>
<p> This demuxer accepts the following option:</p>
<dl>
<dt><code>max_script_size</code></p>
<dd> The demuxer buffers the entire script into memory. Adjust this value to set the maximum buffer size, which in turn, acts as a ceiling for the size of scripts that can be read. Default is 1 MiB.</dl>
<h2>MUXERS</h2>
<p> Muxers are configured elements in FFmpeg which allow writing multimedia streams to a particular type of file. </p>
<p> When you configure your FFmpeg build, all the supported muxers are enabled by default. You can list all available muxers using the configure option <tt>&quot;--list-muxers&quot;</tt>. </p>
<p> You can disable all the muxers with the configure option <tt>&quot;--disable-muxers&quot;</tt> and selectively enable / disable single muxers with the options <tt>&quot;--enable-muxer=</tt>MUXER<tt>&quot;</tt> / <tt>&quot;--disable-muxer=</tt>MUXER<tt>&quot;</tt>. </p>
<p> The option <tt>&quot;-muxers&quot;</tt> of the ff* tools will display the list of enabled muxers. Use <tt>&quot;-formats&quot;</tt> to view a combined list of enabled demuxers and muxers. </p>
<p> A description of some of the currently available muxers follows.</p>
<h3>aiff</h3>
<p> Audio Interchange File Format muxer. </p>
<p> <i>Options</i> </p>
<p> It accepts the following options:</p>
<dl>
<dt><code>write_id3v2</code></p>
<dd> Enable ID3v2 tags writing when set to 1. Default is 0 (disabled).</p>
<dt><code>id3v2_version</code></p>
<dd> Select ID3v2 version to write. Currently only version 3 and 4 (aka. ID3v2.3 and ID3v2.4) are supported. The default is version 4.</dl>
<h3>asf</h3>
<p> Advanced Systems Format muxer. </p>
<p> Note that Windows Media Audio (wma) and Windows Media Video (wmv) use this muxer too. </p>
<p> <i>Options</i> </p>
<p> It accepts the following options:</p>
<dl>
<dt><code>packet_size</code></p>
<dd> Set the muxer packet size. By tuning this setting you may reduce data fragmentation or muxer overhead depending on your source. Default value is 3200, minimum is 100, maximum is 64k.</dl>
<h3>avi</h3>
<p> Audio Video Interleaved muxer. </p>
<p> <i>Options</i> </p>
<p> It accepts the following options:</p>
<dl>
<dt><code>reserve_index_space</code></p>
<dd> Reserve the specified amount of bytes for the OpenDML master index of each stream within the file header. By default additional master indexes are embedded within the data packets if there is no space left in the first master index and are linked together as a chain of indexes. This index structure can cause problems for some use cases, e.g. third-party software strictly relying on the OpenDML index specification or when file seeking is slow. Reserving enough index space in the file header avoids these problems. </p>
<p> The required index space depends on the output file size and should be about 16 bytes per gigabyte. When this option is omitted or set to zero the necessary index space is guessed.</p>
<dt><code>write_channel_mask</code></p>
<dd> Write the channel layout mask into the audio stream header. </p>
<p> This option is enabled by default. Disabling the channel mask can be useful in specific scenarios, e.g. when merging multiple audio streams into one for compatibility with software that only supports a single audio stream in <font SIZE="-1">AVI</font> (see <code>the &#8220;amerge&#8221; section in the ffmpeg-filters manual</code>).</p>
<dt><code>flipped_raw_rgb</code></p>
<dd> If set to true, store positive height for raw <font SIZE="-1">RGB</font> bitmaps, which indicates bitmap is stored bottom-up. Note that this option does not flip the bitmap which has to be done manually beforehand, e.g. by using the vflip filter. Default is <i>false</i> and indicates bitmap is stored top down.</dl>
<h3>chromaprint</h3>
<p> Chromaprint fingerprinter. </p>
<p> This muxer feeds audio data to the Chromaprint library, which generates a fingerprint for the provided audio data. See &lt;<code><a rel="nofollow" href="https://acoustid.org/chromaprint">https://acoustid.org/chromaprint</a></code>&gt; </p>
<p> It takes a single signed native-endian 16-bit raw audio stream of at most 2 channels. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>silence_threshold</code></p>
<dd> Threshold for detecting silence. Range is from -1 to 32767, where -1 disables silence detection. Silence detection can only be used with version 3 of the algorithm. Silence detection must be disabled for use with the AcoustID service. Default is -1.</p>
<dt><code>algorithm</code></p>
<dd> Version of algorithm to fingerprint with. Range is 0 to 4. Version 3 enables silence detection. Default is 1.</p>
<dt><code>fp_format</code></p>
<dd> Format to output the fingerprint as. Accepts the following options:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>raw</code></p>
<dd> Binary raw fingerprint</p>
<dt><code>compressed</code></p>
<dd> Binary compressed fingerprint</p>
<dt><code>base64</code></p>
<dd> Base64 compressed fingerprint <i>(default)</i></dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h3>crc</h3>
<p> <font SIZE="-1">CRC</font> (Cyclic Redundancy Check) testing format. </p>
<p> This muxer computes and prints the Adler-32 <font SIZE="-1">CRC</font> of all the input audio and video frames. By default audio frames are converted to signed 16-bit raw audio and video frames to raw video before computing the <font SIZE="-1">CRC.</font> </p>
<p> The output of the muxer consists of a single line of the form: CRC=0x<i></i><font SIZE="-1"><i>CRC</i></font><i></i>, where <i></i><font SIZE="-1"><i>CRC</i></font><i></i> is a hexadecimal number 0-padded to 8 digits containing the <font SIZE="-1">CRC</font> for all the decoded input frames. </p>
<p> See also the <code>framecrc</code> muxer. </p>
<p> <i>Examples</i> </p>
<p> For example to compute the <font SIZE="-1">CRC</font> of the input, and store it in the file <i>out.crc</i>: </p>
<pre>
        ffmpeg -i INPUT -f crc out.crc
</pre>
<p> You can print the <font SIZE="-1">CRC</font> to stdout with the command: </p>
<pre>
        ffmpeg -i INPUT -f crc -
</pre>
<p> You can select the output format of each frame with <code>ffmpeg</code> by specifying the audio and video codec and format. For example to compute the <font SIZE="-1">CRC</font> of the input audio converted to <font SIZE="-1">PCM</font> unsigned 8-bit and the input video converted to <font SIZE="-1">MPEG-2</font> video, use the command: </p>
<pre>
        ffmpeg -i INPUT -c:a pcm_u8 -c:v mpeg2video -f crc -
</pre>
<h3>flv</h3>
<p> Adobe Flash Video Format muxer. </p>
<p> This muxer accepts the following options:</p>
<dl>
<dt><code>flvflags</code> <i>flags</i></p>
<dd> Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>aac_seq_header_detect</code></p>
<dd> Place <font SIZE="-1">AAC</font> sequence header based on audio stream data.</p>
<dt><code>no_sequence_end</code></p>
<dd> Disable sequence end tag.</p>
<dt><code>no_metadata</code></p>
<dd> Disable metadata tag.</p>
<dt><code>no_duration_filesize</code></p>
<dd> Disable duration and filesize in metadata when they are equal to zero at the end of stream. (Be used to non-seekable living stream).</p>
<dt><code>add_keyframe_index</code></p>
<dd> Used to facilitate seeking; particularly for <font SIZE="-1">HTTP</font> pseudo streaming.</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h3>dash</h3>
<p> Dynamic Adaptive Streaming over <font SIZE="-1">HTTP</font> (<font SIZE="-1">DASH</font>) muxer that creates segments and manifest files according to the MPEG-DASH standard <font SIZE="-1">ISO/IEC 23009-1:2014.</font> </p>
<p> For more information see:</p>
<dl>
<dt>&bull;</p>
<dd> <font SIZE="-1">ISO DASH</font> Specification: &lt;<code><a rel="nofollow" href="http://standards.iso.org/ittf/PubliclyAvailableStandards/c065274_ISO_IEC_23009-1_2014.zip">http://standards.iso.org/ittf/PubliclyAvailableStandards/c065274_ISO_IEC_23009-1_2014.zip</a></code>&gt;</p>
<dt>&bull;</p>
<dd> WebM <font SIZE="-1">DASH</font> Specification: &lt;<code><a rel="nofollow" href="https://sites.google.com/a/webmproject.org/wiki/adaptive-streaming/webm-dash-specification">https://sites.google.com/a/webmproject.org/wiki/adaptive-streaming/webm-dash-specification</a></code>&gt;</dl>
<p> It creates a <font SIZE="-1">MPD</font> manifest file and segment files for each stream. </p>
<p> The segment filename might contain pre-defined identifiers used with SegmentTemplate as defined in section 5.3.9.4.4 of the standard. Available identifiers are &#8220;$RepresentationID$&#8221;, &#8220;$Number$&#8221;, &#8220;$Bandwidth$&#8221; and &#8220;$Time$&#8221;. In addition to the standard identifiers, an ffmpeg-specific &#8220;$ext$&#8221; identifier is also supported. When specified ffmpeg will replace <tt>$ext</tt>$ in the file name with muxing format&#8217;s extensions such as mp4, webm etc., </p>
<pre>
        ffmpeg -re -i &lt;input&gt; -map 0 -map 0 -c:a libfdk_aac -c:v libx264 \
        -b:v:0 800k -b:v:1 300k -s:v:1 320x170 -profile:v:1 baseline \
        -profile:v:0 main -bf 1 -keyint_min 120 -g 120 -sc_threshold 0 \
        -b_strategy 0 -ar:a:1 22050 -use_timeline 1 -use_template 1 \
        -window_size 5 -adaptation_sets &quot;id=0,streams=v id=1,streams=a&quot; \
        -f dash /path/to/out.mpd
</pre>
<dl>
<dt><code>min_seg_duration</code> <i>microseconds</i></p>
<dd> This is a deprecated option to set the segment length in microseconds, use <i>seg_duration</i> instead.</p>
<dt><code>seg_duration</code> <i>duration</i></p>
<dd> Set the segment length in seconds (fractional value can be set). The value is treated as average segment duration when <i>use_template</i> is enabled and <i>use_timeline</i> is disabled and as minimum segment duration for all the other use cases.</p>
<dt><code>frag_duration</code> <i>duration</i></p>
<dd> Set the length in seconds of fragments within segments (fractional value can be set).</p>
<dt><code>frag_type</code> <i>type</i></p>
<dd> Set the type of interval for fragmentation.</p>
<dt><code>window_size</code> <i>size</i></p>
<dd> Set the maximum number of segments kept in the manifest.</p>
<dt><code>extra_window_size</code> <i>size</i></p>
<dd> Set the maximum number of segments kept outside of the manifest before removing from disk.</p>
<dt><code>remove_at_exit</code> <i>remove</i></p>
<dd> Enable (1) or disable (0) removal of all segments when finished.</p>
<dt><code>use_template</code> <i>template</i></p>
<dd> Enable (1) or disable (0) use of SegmentTemplate instead of SegmentList.</p>
<dt><code>use_timeline</code> <i>timeline</i></p>
<dd> Enable (1) or disable (0) use of SegmentTimeline in SegmentTemplate.</p>
<dt><code>single_file</code> <i>single_file</i></p>
<dd> Enable (1) or disable (0) storing all segments in one file, accessed using byte ranges.</p>
<dt><code>single_file_name</code> <i>file_name</i></p>
<dd> DASH-templated name to be used for baseURL. Implies <i>single_file</i> set to &#8220;1&#8221;. In the template, &#8220;$ext$&#8221; is replaced with the file name extension specific for the segment format.</p>
<dt><code>init_seg_name</code> <i>init_name</i></p>
<dd> DASH-templated name to used for the initialization segment. Default is &#8220;init-stream$RepresentationID$.$ext$&#8221;. &#8220;$ext$&#8221; is replaced with the file name extension specific for the segment format.</p>
<dt><code>media_seg_name</code> <i>segment_name</i></p>
<dd> DASH-templated name to used for the media segments. Default is &#8220;chunk-stream$RepresentationID$-$Number%05d$.$ext$&#8221;. &#8220;$ext$&#8221; is replaced with the file name extension specific for the segment format.</p>
<dt><code>utc_timing_url</code> <i>utc_url</i></p>
<dd> <font SIZE="-1">URL</font> of the page that will return the <font SIZE="-1">UTC</font> timestamp in <font SIZE="-1">ISO</font> format. Example: &#8220;<a rel="nofollow" href="https://time.akamai.com/?iso''">https://time.akamai.com/?iso&#8221;</a></p>
<dt><code>method</code> <i>method</i></p>
<dd> Use the given <font SIZE="-1">HTTP</font> method to create output files. Generally set to <font SIZE="-1">PUT</font> or <font SIZE="-1">POST.</font></p>
<dt><code>http_user_agent</code> <i>user_agent</i></p>
<dd> Override User-Agent field in <font SIZE="-1">HTTP</font> header. Applicable only for <font SIZE="-1">HTTP</font> output.</p>
<dt><code>http_persistent</code> <i>http_persistent</i></p>
<dd> Use persistent <font SIZE="-1">HTTP</font> connections. Applicable only for <font SIZE="-1">HTTP</font> output.</p>
<dt><code>hls_playlist</code> <i>hls_playlist</i></p>
<dd> Generate <font SIZE="-1">HLS</font> playlist files as well. The master playlist is generated with the filename <i>hls_master_name</i>. One media playlist file is generated for each stream with filenames media_0.m3u8, media_1.m3u8, etc.</p>
<dt><code>hls_master_name</code> <i>file_name</i></p>
<dd> <font SIZE="-1">HLS</font> master playlist name. Default is &#8220;master.m3u8&#8221;.</p>
<dt><code>streaming</code> <i>streaming</i></p>
<dd> Enable (1) or disable (0) chunk streaming mode of output. In chunk streaming mode, each frame will be a moof fragment which forms a chunk.</p>
<dt><code>adaptation_sets</code> <i>adaptation_sets</i></p>
<dd> Assign streams to AdaptationSets. Syntax is &#8220;id=x,streams=a,b,c id=y,streams=d,e&#8221; with x and y being the IDs of the adaptation sets and a,b,c,d and e are the indices of the mapped streams. </p>
<p> To map all video (or audio) streams to an AdaptationSet, &#8220;v&#8221; (or &#8220;a&#8221;) can be used as stream identifier instead of IDs. </p>
<p> When no assignment is defined, this defaults to an AdaptationSet for each stream. </p>
<p> Optional syntax is &#8220;id=x,seg_duration=x,frag_duration=x,frag_type=type,descriptor=descriptor_string,streams=a,b,c id=y,seg_duration=y,frag_type=type,streams=d,e&#8221; and so on, descriptor is useful to the scheme defined by <font SIZE="-1">ISO/IEC</font> 23009-1:2014/Amd.2:2015. For example, -adaptation_sets &#8220;id=0,descriptor=&lt;SupplementalProperty schemeIdUri=\&#8221;urn:mpeg:dash:srd:2014\&#8220; value=\&#8221;0,0,0,1,1,2,2\&#8220;/&gt;,streams=v&#8221;. Please note that descriptor string should be a self-closing xml tag. seg_duration, frag_duration and frag_type override the global option values for each adaptation set. For example, -adaptation_sets &#8220;id=0,seg_duration=2,frag_duration=1,frag_type=duration,streams=v id=1,seg_duration=2,frag_type=none,streams=a&#8221; type_id marks an adaptation set as containing streams meant to be used for Trick Mode for the referenced adaptation set. For example, -adaptation_sets &#8220;id=0,seg_duration=2,frag_type=none,streams=0 id=1,seg_duration=10,frag_type=none,trick_id=0,streams=1&#8221;</p>
<dt><code>timeout</code> <i>timeout</i></p>
<dd> Set timeout for socket I/O operations. Applicable only for <font SIZE="-1">HTTP</font> output.</p>
<dt><code>index_correction</code> <i>index_correction</i></p>
<dd> Enable (1) or Disable (0) segment index correction logic. Applicable only when <i>use_template</i> is enabled and <i>use_timeline</i> is disabled. </p>
<p> When enabled, the logic monitors the flow of segment indexes. If a streams&#8217;s segment index value is not at the expected real time position, then the logic corrects that index value. </p>
<p> Typically this logic is needed in live streaming use cases. The network bandwidth fluctuations are common during long run streaming. Each fluctuation can cause the segment indexes fall behind the expected real time position.</p>
<dt><code>format_options</code> <i>options_list</i></p>
<dd> Set container format (mp4/webm) options using a <tt>&quot;:&quot;</tt> separated list of key=value parameters. Values containing <tt>&quot;:&quot;</tt> special characters must be escaped.</p>
<dt><code>global_sidx</code> <i>global_sidx</i></p>
<dd> Write global <font SIZE="-1">SIDX</font> atom. Applicable only for single file, mp4 output, non-streaming mode.</p>
<dt><code>dash_segment_type</code> <i>dash_segment_type</i></p>
<dd> Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>auto</code></p>
<dd> If this flag is set, the dash segment files format will be selected based on the stream codec. This is the default mode.</p>
<dt><code>mp4</code></p>
<dd> If this flag is set, the dash segment files will be in in <font SIZE="-1">ISOBMFF</font> format.</p>
<dt><code>webm</code></p>
<dd> If this flag is set, the dash segment files will be in in WebM format.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>ignore_io_errors</code> <i>ignore_io_errors</i></p>
<dd> Ignore <font SIZE="-1">IO</font> errors during open and write. Useful for long-duration runs with network output.</p>
<dt><code>lhls</code> <i>lhls</i></p>
<dd> Enable Low-latency <font SIZE="-1">HLS</font>(<font SIZE="-1">LHLS</font>). Adds #EXT-X-PREFETCH tag with current segment&#8217;s <font SIZE="-1">URI.</font> Apple doesn&#8217;t have an official spec for <font SIZE="-1">LHLS.</font> Meanwhile hls.js player folks are trying to standardize a open <font SIZE="-1">LHLS</font> spec. The draft spec is available in <a rel="nofollow" href="https://github.com/video-dev/hlsjs-rfcs/blob/lhls-spec/proposals/0001-lhls.md">https://github.com/video-dev/hlsjs-rfcs/blob/lhls-spec/proposals/0001-lhls.md</a> This option will also try to comply with the above open spec, till Apple&#8217;s spec officially supports it. Applicable only when <i>streaming</i> and <i>hls_playlist</i> options are enabled. This is an experimental feature.</p>
<dt><code>ldash</code> <i>ldash</i></p>
<dd> Enable Low-latency Dash by constraining the presence and values of some elements.</p>
<dt><code>master_m3u8_publish_rate</code> <i>master_m3u8_publish_rate</i></p>
<dd> Publish master playlist repeatedly every after specified number of segment intervals.</p>
<dt><code>write_prft</code> <i>write_prft</i></p>
<dd> Write Producer Reference Time elements on supported streams. This also enables writing prft boxes in the underlying muxer. Applicable only when the <i>utc_url</i> option is enabled. It&#8217;s set to auto by default, in which case the muxer will attempt to enable it only in modes that require it.</p>
<dt><code>mpd_profile</code> <i>mpd_profile</i></p>
<dd> Set one or more manifest profiles.</p>
<dt><code>http_opts</code> <i>http_opts</i></p>
<dd> A :-separated list of key=value options to pass to the underlying <font SIZE="-1">HTTP</font> protocol. Applicable only for <font SIZE="-1">HTTP</font> output.</p>
<dt><code>target_latency</code> <i>target_latency</i></p>
<dd> Set an intended target latency in seconds (fractional value can be set) for serving. Applicable only when <i>streaming</i> and <i>write_prft</i> options are enabled. This is an informative fields clients can use to measure the latency of the service.</p>
<dt><code>min_playback_rate</code> <i>min_playback_rate</i></p>
<dd> Set the minimum playback rate indicated as appropriate for the purposes of automatically adjusting playback latency and buffer occupancy during normal playback by clients.</p>
<dt><code>max_playback_rate</code> <i>max_playback_rate</i></p>
<dd> Set the maximum playback rate indicated as appropriate for the purposes of automatically adjusting playback latency and buffer occupancy during normal playback by clients.</p>
<dt><code>update_period</code> <i>update_period</i></p>
<dd>
<pre>
 Set the mpd update period ,for dynamic content.
 The unit is second.
</pre>
</dl>
<h3>framecrc</h3>
<p> Per-packet <font SIZE="-1">CRC</font> (Cyclic Redundancy Check) testing format. </p>
<p> This muxer computes and prints the Adler-32 <font SIZE="-1">CRC</font> for each audio and video packet. By default audio frames are converted to signed 16-bit raw audio and video frames to raw video before computing the <font SIZE="-1">CRC.</font> </p>
<p> The output of the muxer consists of a line for each audio and video packet of the form: </p>
<pre>
        &lt;stream_index&gt;, &lt;packet_dts&gt;, &lt;packet_pts&gt;, &lt;packet_duration&gt;, &lt;packet_size&gt;, 0x&lt;CRC&gt;
</pre>
<p> <i></i><font SIZE="-1"><i>CRC</i></font><i></i> is a hexadecimal number 0-padded to 8 digits containing the <font SIZE="-1">CRC</font> of the packet. </p>
<p> <i>Examples</i> </p>
<p> For example to compute the <font SIZE="-1">CRC</font> of the audio and video frames in <i></i><font SIZE="-1"><i>INPUT</i></font><i></i>, converted to raw audio and video packets, and store it in the file <i>out.crc</i>: </p>
<pre>
        ffmpeg -i INPUT -f framecrc out.crc
</pre>
<p> To print the information to stdout, use the command: </p>
<pre>
        ffmpeg -i INPUT -f framecrc -
</pre>
<p> With <code>ffmpeg</code>, you can select the output format to which the audio and video frames are encoded before computing the <font SIZE="-1">CRC</font> for each packet by specifying the audio and video codec. For example, to compute the <font SIZE="-1">CRC</font> of each decoded input audio frame converted to <font SIZE="-1">PCM</font> unsigned 8-bit and of each decoded input video frame converted to <font SIZE="-1">MPEG-2</font> video, use the command: </p>
<pre>
        ffmpeg -i INPUT -c:a pcm_u8 -c:v mpeg2video -f framecrc -
</pre>
<p> See also the <code>crc</code> muxer.</p>
<h3>framehash</h3>
<p> Per-packet hash testing format. </p>
<p> This muxer computes and prints a cryptographic hash for each audio and video packet. This can be used for packet-by-packet equality checks without having to individually do a binary comparison on each. </p>
<p> By default audio frames are converted to signed 16-bit raw audio and video frames to raw video before computing the hash, but the output of explicit conversions to other codecs can also be used. It uses the <font SIZE="-1">SHA-256</font> cryptographic hash function by default, but supports several other algorithms. </p>
<p> The output of the muxer consists of a line for each audio and video packet of the form: </p>
<pre>
        &lt;stream_index&gt;, &lt;packet_dts&gt;, &lt;packet_pts&gt;, &lt;packet_duration&gt;, &lt;packet_size&gt;, &lt;hash&gt;
</pre>
<p> <i>hash</i> is a hexadecimal number representing the computed hash for the packet.</p>
<dl>
<dt><code>hash</code> <i>algorithm</i></p>
<dd> Use the cryptographic hash function specified by the string <i>algorithm</i>. Supported values include <tt>&quot;MD5&quot;</tt>, <tt>&quot;murmur3&quot;</tt>, <tt>&quot;RIPEMD128&quot;</tt>, <tt>&quot;RIPEMD160&quot;</tt>, <tt>&quot;RIPEMD256&quot;</tt>, <tt>&quot;RIPEMD320&quot;</tt>, <tt>&quot;SHA160&quot;</tt>, <tt>&quot;SHA224&quot;</tt>, <tt>&quot;SHA256&quot;</tt> (default), <tt>&quot;SHA512/224&quot;</tt>, <tt>&quot;SHA512/256&quot;</tt>, <tt>&quot;SHA384&quot;</tt>, <tt>&quot;SHA512&quot;</tt>, <tt>&quot;CRC32&quot;</tt> and <tt>&quot;adler32&quot;</tt>.</dl>
<p> <i>Examples</i> </p>
<p> To compute the <font SIZE="-1">SHA-256</font> hash of the audio and video frames in <i></i><font SIZE="-1"><i>INPUT</i></font><i></i>, converted to raw audio and video packets, and store it in the file <i>out.sha256</i>: </p>
<pre>
        ffmpeg -i INPUT -f framehash out.sha256
</pre>
<p> To print the information to stdout, using the <font SIZE="-1">MD5</font> hash function, use the command: </p>
<pre>
        ffmpeg -i INPUT -f framehash -hash md5 -
</pre>
<p> See also the <code>hash</code> muxer.</p>
<h3>framemd5</h3>
<p> Per-packet <font SIZE="-1">MD5</font> testing format. </p>
<p> This is a variant of the <code>framehash</code> muxer. Unlike that muxer, it defaults to using the <font SIZE="-1">MD5</font> hash function. </p>
<p> <i>Examples</i> </p>
<p> To compute the <font SIZE="-1">MD5</font> hash of the audio and video frames in <i></i><font SIZE="-1"><i>INPUT</i></font><i></i>, converted to raw audio and video packets, and store it in the file <i>out.md5</i>: </p>
<pre>
        ffmpeg -i INPUT -f framemd5 out.md5
</pre>
<p> To print the information to stdout, use the command: </p>
<pre>
        ffmpeg -i INPUT -f framemd5 -
</pre>
<p> See also the <code>framehash</code> and <code>md5</code> muxers.</p>
<h3>gif</h3>
<p> Animated <font SIZE="-1">GIF</font> muxer. </p>
<p> It accepts the following options:</p>
<dl>
<dt><code>loop</code></p>
<dd> Set the number of times to loop the output. Use <tt>&quot;-1&quot;</tt> for no loop, <tt>0</tt> for looping indefinitely (default).</p>
<dt><code>final_delay</code></p>
<dd> Force the delay (expressed in centiseconds) after the last frame. Each frame ends with a delay until the next frame. The default is <tt>&quot;-1&quot;</tt>, which is a special value to tell the muxer to re-use the previous delay. In case of a loop, you might want to customize this value to mark a pause for instance.</dl>
<p> For example, to encode a gif looping 10 times, with a 5 seconds delay between the loops: </p>
<pre>
        ffmpeg -i INPUT -loop 10 -final_delay 500 out.gif
</pre>
<p> Note 1: if you wish to extract the frames into separate <font SIZE="-1">GIF</font> files, you need to force the <code>image2</code> muxer: </p>
<pre>
        ffmpeg -i INPUT -c:v gif -f image2 &quot;out%d.gif&quot;
</pre>
<p> Note 2: the <font SIZE="-1">GIF</font> format has a very large time base: the delay between two frames can therefore not be smaller than one centi second.</p>
<h3>hash</h3>
<p> Hash testing format. </p>
<p> This muxer computes and prints a cryptographic hash of all the input audio and video frames. This can be used for equality checks without having to do a complete binary comparison. </p>
<p> By default audio frames are converted to signed 16-bit raw audio and video frames to raw video before computing the hash, but the output of explicit conversions to other codecs can also be used. Timestamps are ignored. It uses the <font SIZE="-1">SHA-256</font> cryptographic hash function by default, but supports several other algorithms. </p>
<p> The output of the muxer consists of a single line of the form: <i>algo</i>=<i>hash</i>, where <i>algo</i> is a short string representing the hash function used, and <i>hash</i> is a hexadecimal number representing the computed hash.</p>
<dl>
<dt><code>hash</code> <i>algorithm</i></p>
<dd> Use the cryptographic hash function specified by the string <i>algorithm</i>. Supported values include <tt>&quot;MD5&quot;</tt>, <tt>&quot;murmur3&quot;</tt>, <tt>&quot;RIPEMD128&quot;</tt>, <tt>&quot;RIPEMD160&quot;</tt>, <tt>&quot;RIPEMD256&quot;</tt>, <tt>&quot;RIPEMD320&quot;</tt>, <tt>&quot;SHA160&quot;</tt>, <tt>&quot;SHA224&quot;</tt>, <tt>&quot;SHA256&quot;</tt> (default), <tt>&quot;SHA512/224&quot;</tt>, <tt>&quot;SHA512/256&quot;</tt>, <tt>&quot;SHA384&quot;</tt>, <tt>&quot;SHA512&quot;</tt>, <tt>&quot;CRC32&quot;</tt> and <tt>&quot;adler32&quot;</tt>.</dl>
<p> <i>Examples</i> </p>
<p> To compute the <font SIZE="-1">SHA-256</font> hash of the input converted to raw audio and video, and store it in the file <i>out.sha256</i>: </p>
<pre>
        ffmpeg -i INPUT -f hash out.sha256
</pre>
<p> To print an <font SIZE="-1">MD5</font> hash to stdout use the command: </p>
<pre>
        ffmpeg -i INPUT -f hash -hash md5 -
</pre>
<p> See also the <code>framehash</code> muxer.</p>
<h3>hls</h3>
<p> Apple <font SIZE="-1">HTTP</font> Live Streaming muxer that segments MPEG-TS according to the <font SIZE="-1">HTTP</font> Live Streaming (<font SIZE="-1">HLS</font>) specification. </p>
<p> It creates a playlist file, and one or more segment files. The output filename specifies the playlist filename. </p>
<p> By default, the muxer creates a file for each segment produced. These files have the same name as the playlist, followed by a sequential number and a .ts extension. </p>
<p> Make sure to require a closed <font SIZE="-1">GOP</font> when encoding and to set the <font SIZE="-1">GOP</font> size to fit your segment time constraint. </p>
<p> For example, to convert an input file with <code>ffmpeg</code>: </p>
<pre>
        ffmpeg -i in.mkv -c:v h264 -flags +cgop -g 30 -hls_time 1 out.m3u8
</pre>
<p> This example will produce the playlist, <i>out.m3u8</i>, and segment files: <i>out0.ts</i>, <i>out1.ts</i>, <i>out2.ts</i>, etc. </p>
<p> See also the <code>segment</code> muxer, which provides a more generic and flexible implementation of a segmenter, and can be used to perform <font SIZE="-1">HLS</font> segmentation. </p>
<p> <i>Options</i> </p>
<p> This muxer supports the following options:</p>
<dl>
<dt><code>hls_init_time</code> <i>duration</i></p>
<dd> Set the initial target segment length. Default value is <i>0</i>. </p>
<p> <i>duration</i> must be a time duration specification, see <code>the Time duration section in the <a href="/docs/linux/man/1-ffmpeg-utils/">ffmpeg-utils</a>(1) manual</code>. </p>
<p> Segment will be cut on the next key frame after this time has passed on the first m3u8 list. After the initial playlist is filled <code>ffmpeg</code> will cut segments at duration equal to <tt>&quot;hls_time&quot;</tt></p>
<dt><code>hls_time</code> <i>duration</i></p>
<dd> Set the target segment length. Default value is 2. </p>
<p> <i>duration</i> must be a time duration specification, see <code>the Time duration section in the <a href="/docs/linux/man/1-ffmpeg-utils/">ffmpeg-utils</a>(1) manual</code>. Segment will be cut on the next key frame after this time has passed.</p>
<dt><code>hls_list_size</code> <i>size</i></p>
<dd> Set the maximum number of playlist entries. If set to 0 the list file will contain all the segments. Default value is 5.</p>
<dt><code>hls_delete_threshold</code> <i>size</i></p>
<dd> Set the number of unreferenced segments to keep on disk before <tt>&quot;hls_flags delete_segments&quot;</tt> deletes them. Increase this to allow continue clients to download segments which were recently referenced in the playlist. Default value is 1, meaning segments older than <tt>&quot;hls_list_size+1&quot;</tt> will be deleted.</p>
<dt><code>hls_ts_options</code> <i>options_list</i></p>
<dd> Set output format options using a :-separated list of key=value parameters. Values containing <tt>&quot;:&quot;</tt> special characters must be escaped.</p>
<dt><code>hls_wrap</code> <i>wrap</i></p>
<dd> This is a deprecated option, you can use <tt>&quot;hls_list_size&quot;</tt> and <tt>&quot;hls_flags delete_segments&quot;</tt> instead it </p>
<p> This option is useful to avoid to fill the disk with many segment files, and limits the maximum number of segment files written to disk to <i>wrap</i>.</p>
<dt><code>hls_start_number_source</code></p>
<dd> Start the playlist sequence number (<tt>&quot;#EXT-X-MEDIA-SEQUENCE&quot;</tt>) according to the specified source. Unless <tt>&quot;hls_flags single_file&quot;</tt> is set, it also specifies source of starting sequence numbers of segment and subtitle filenames. In any case, if <tt>&quot;hls_flags append_list&quot;</tt> is set and read playlist sequence number is greater than the specified start sequence number, then that value will be used as start value. </p>
<p> It accepts the following values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>generic (default)</code></p>
<dd> Set the starting sequence numbers according to <i>start_number</i> option value.</p>
<dt><code>epoch</code></p>
<dd> The start number will be the seconds since epoch (1970-01-01 00:00:00)</p>
<dt><code>epoch_us</code></p>
<dd> The start number will be the microseconds since epoch (1970-01-01 00:00:00)</p>
<dt><code>datetime</code></p>
<dd> The start number will be based on the current date/time as YYYYmmddHHMMSS. e.g. 20161231235759.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>start_number</code> <i>number</i></p>
<dd> Start the playlist sequence number (<tt>&quot;#EXT-X-MEDIA-SEQUENCE&quot;</tt>) from the specified <i>number</i> when <i>hls_start_number_source</i> value is <i>generic</i>. (This is the default case.) Unless <tt>&quot;hls_flags single_file&quot;</tt> is set, it also specifies starting sequence numbers of segment and subtitle filenames. Default value is 0.</p>
<dt><code>hls_allow_cache</code> <i>allowcache</i></p>
<dd> Explicitly set whether the client <font SIZE="-1">MAY</font> (1) or <font SIZE="-1">MUST NOT</font> (0) cache media segments.</p>
<dt><code>hls_base_url</code> <i>baseurl</i></p>
<dd> Append <i>baseurl</i> to every entry in the playlist. Useful to generate playlists with absolute paths. </p>
<p> Note that the playlist sequence number must be unique for each segment and it is not to be confused with the segment filename sequence number which can be cyclic, for example if the <code>wrap</code> option is specified.</p>
<dt><code>hls_segment_filename</code> <i>filename</i></p>
<dd> Set the segment filename. Unless <tt>&quot;hls_flags single_file&quot;</tt> is set, <i>filename</i> is used as a string format with the segment number: </p>
<pre>
        ffmpeg -i in.nut -hls_segment_filename 'file%03d.ts' out.m3u8
</pre>
<p> This example will produce the playlist, <i>out.m3u8</i>, and segment files: <i>file000.ts</i>, <i>file001.ts</i>, <i>file002.ts</i>, etc. </p>
<p> <i>filename</i> may contain full path or relative path specification, but only the file name part without any path info will be contained in the m3u8 segment list. Should a relative path be specified, the path of the created segment files will be relative to the current working directory. When strftime_mkdir is set, the whole expanded value of <i>filename</i> will be written into the m3u8 segment list. </p>
<p> When <tt>&quot;var_stream_map&quot;</tt> is set with two or more variant streams, the <i>filename</i> pattern must contain the string &#8220;%v&#8221;, this string specifies the position of variant stream index in the generated segment file names. </p>
<pre>
        ffmpeg -i in.ts -b:v:0 1000k -b:v:1 256k -b:a:0 64k -b:a:1 32k \
          -map 0:v -map 0:a -map 0:v -map 0:a -f hls -var_stream_map &quot;v:0,a:0 v:1,a:1&quot; \
          -hls_segment_filename 'file_%v_%03d.ts' out_%v.m3u8
</pre>
<p> This example will produce the playlists segment file sets: <i>file_0_000.ts</i>, <i>file_0_001.ts</i>, <i>file_0_002.ts</i>, etc. and <i>file_1_000.ts</i>, <i>file_1_001.ts</i>, <i>file_1_002.ts</i>, etc. </p>
<p> The string &#8220;%v&#8221; may be present in the filename or in the last directory name containing the file, but only in one of them. (Additionally, <tt>%v</tt> may appear multiple times in the last sub-directory or filename.) If the string <tt>%v</tt> is present in the directory name, then sub-directories are created after expanding the directory name pattern. This enables creation of segments corresponding to different variant streams in subdirectories. </p>
<pre>
        ffmpeg -i in.ts -b:v:0 1000k -b:v:1 256k -b:a:0 64k -b:a:1 32k \
          -map 0:v -map 0:a -map 0:v -map 0:a -f hls -var_stream_map &quot;v:0,a:0 v:1,a:1&quot; \
          -hls_segment_filename 'vs%v/file_%03d.ts' vs%v/out.m3u8
</pre>
<p> This example will produce the playlists segment file sets: <i>vs0/file_000.ts</i>, <i>vs0/file_001.ts</i>, <i>vs0/file_002.ts</i>, etc. and <i>vs1/file_000.ts</i>, <i>vs1/file_001.ts</i>, <i>vs1/file_002.ts</i>, etc.</p>
<dt><code>use_localtime</code></p>
<dd> Same as strftime option, will be deprecated.</p>
<dt><code>strftime</code></p>
<dd> Use <code>strftime()</code> on <i>filename</i> to expand the segment filename with localtime. The segment number is also available in this mode, but to use it, you need to specify second_level_segment_index hls_flag and %%d will be the specifier. </p>
<pre>
        ffmpeg -i in.nut -strftime 1 -hls_segment_filename 'file-%Y%m%d-%s.ts' out.m3u8
</pre>
<p> This example will produce the playlist, <i>out.m3u8</i>, and segment files: <i>file-20160215-1455569023.ts</i>, <i>file-20160215-1455569024.ts</i>, etc. Note: On some systems/environments, the <tt>%s</tt> specifier is not available. See<br />
&nbsp;<wbr>&nbsp;<tt>&quot;strftime()&quot;</tt>&nbsp;documentation. </p>
<pre>
        ffmpeg -i in.nut -strftime 1 -hls_flags second_level_segment_index -hls_segment_filename 'file-%Y%m%d-%%04d.ts' out.m3u8
</pre>
<p> This example will produce the playlist, <i>out.m3u8</i>, and segment files: <i>file-20160215-0001.ts</i>, <i>file-20160215-0002.ts</i>, etc.</p>
<dt><code>use_localtime_mkdir</code></p>
<dd> Same as strftime_mkdir option, will be deprecated .</p>
<dt><code>strftime_mkdir</code></p>
<dd> Used together with -strftime_mkdir, it will create all subdirectories which is expanded in <i>filename</i>. </p>
<pre>
        ffmpeg -i in.nut -strftime 1 -strftime_mkdir 1 -hls_segment_filename '%Y%m%d/file-%Y%m%d-%s.ts' out.m3u8
</pre>
<p> This example will create a directory 201560215 (if it does not exist), and then produce the playlist, <i>out.m3u8</i>, and segment files: <i>20160215/file-20160215-1455569023.ts</i>, <i>20160215/file-20160215-1455569024.ts</i>, etc. </p>
<pre>
        ffmpeg -i in.nut -strftime 1 -strftime_mkdir 1 -hls_segment_filename '%Y/%m/%d/file-%Y%m%d-%s.ts' out.m3u8
</pre>
<p> This example will create a directory hierarchy 2016/02/15 (if any of them do not exist), and then produce the playlist, <i>out.m3u8</i>, and segment files: <i>2016/02/15/file-20160215-1455569023.ts</i>, <i>2016/02/15/file-20160215-1455569024.ts</i>, etc.</p>
<dt><code>hls_key_info_file</code> <i>key_info_file</i></p>
<dd> Use the information in <i>key_info_file</i> for segment encryption. The first line of <i>key_info_file</i> specifies the key <font SIZE="-1">URI</font> written to the playlist. The key <font SIZE="-1">URL</font> is used to access the encryption key during playback. The second line specifies the path to the key file used to obtain the key during the encryption process. The key file is read as a single packed array of 16 octets in binary format. The optional third line specifies the initialization vector (<font SIZE="-1">IV</font>) as a hexadecimal string to be used instead of the segment sequence number (default) for encryption. Changes to <i>key_info_file</i> will result in segment encryption with the new key/IV and an entry in the playlist for the new key <font SIZE="-1">URI/IV</font> if <tt>&quot;hls_flags periodic_rekey&quot;</tt> is enabled. </p>
<p> Key info file format: </p>
<pre>
        &lt;key URI&gt;
        &lt;key file path&gt;
        &lt;IV&gt; (optional)
</pre>
<p> Example key URIs: </p>
<pre>
        <a rel="nofollow" href="http://server/file.key">http://server/file.key</a>
        /path/to/file.key
        file.key
</pre>
<p> Example key file paths: </p>
<pre>
        file.key
        /path/to/file.key
</pre>
<p> Example <font SIZE="-1">IV:</font> </p>
<pre>
        0123456789ABCDEF0123456789ABCDEF
</pre>
<p> Key info file example: </p>
<pre>
        <a rel="nofollow" href="http://server/file.key">http://server/file.key</a>
        /path/to/file.key
        0123456789ABCDEF0123456789ABCDEF
</pre>
<p> Example shell script: </p>
<pre>
        #!/bin/sh
        BASE_URL=${1:-'.'}
        openssl rand 16 &gt; file.key
        echo $BASE_URL/file.key &gt; file.keyinfo
        echo file.key &gt;&gt; file.keyinfo
        echo $(openssl rand -hex 16) &gt;&gt; file.keyinfo
        ffmpeg -f lavfi -re -i testsrc -c:v h264 -hls_flags delete_segments \
          -hls_key_info_file file.keyinfo out.m3u8
</pre>
<dt><code>-hls_enc</code> <i>enc</i></p>
<dd> Enable (1) or disable (0) the <font SIZE="-1">AES128</font> encryption. When enabled every segment generated is encrypted and the encryption key is saved as <i>playlist name</i>.key.</p>
<dt><code>-hls_enc_key</code> <i>key</i></p>
<dd> 16-octet key to encrypt the segments, by default it is randomly generated.</p>
<dt><code>-hls_enc_key_url</code> <i>keyurl</i></p>
<dd> If set, <i>keyurl</i> is prepended instead of <i>baseurl</i> to the key filename in the playlist.</p>
<dt><code>-hls_enc_iv</code> <i>iv</i></p>
<dd> 16-octet initialization vector for every segment instead of the autogenerated ones.</p>
<dt><code>hls_segment_type</code> <i>flags</i></p>
<dd> Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>mpegts</code></p>
<dd> Output segment files in <font SIZE="-1">MPEG-2</font> Transport Stream format. This is compatible with all <font SIZE="-1">HLS</font> versions.</p>
<dt><code>fmp4</code></p>
<dd> Output segment files in fragmented <font SIZE="-1">MP4</font> format, similar to MPEG-DASH. fmp4 files may be used in <font SIZE="-1">HLS</font> version 7 and above.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>hls_fmp4_init_filename</code> <i>filename</i></p>
<dd> Set filename to the fragment files header file, default filename is <i>init.mp4</i>. </p>
<p> Use <tt>&quot;-strftime 1&quot;</tt> on <i>filename</i> to expand the segment filename with localtime. </p>
<pre>
        ffmpeg -i in.nut  -hls_segment_type fmp4 -strftime 1 -hls_fmp4_init_filename &quot;%s_init.mp4&quot; out.m3u8
</pre>
<p> This will produce init like this <i>1602678741_init.mp4</i></p>
<dt><code>hls_fmp4_init_resend</code></p>
<dd> Resend init file after m3u8 file refresh every time, default is <i>0</i>. </p>
<p> When <tt>&quot;var_stream_map&quot;</tt> is set with two or more variant streams, the <i>filename</i> pattern must contain the string &#8220;%v&#8221;, this string specifies the position of variant stream index in the generated init file names. The string &#8220;%v&#8221; may be present in the filename or in the last directory name containing the file. If the string is present in the directory name, then sub-directories are created after expanding the directory name pattern. This enables creation of init files corresponding to different variant streams in subdirectories.</p>
<dt><code>hls_flags</code> <i>flags</i></p>
<dd> Possible values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>single_file</code></p>
<dd> If this flag is set, the muxer will store all segments in a single MPEG-TS file, and will use byte ranges in the playlist. <font SIZE="-1">HLS</font> playlists generated with this way will have the version number 4. For example: </p>
<pre>
        ffmpeg -i in.nut -hls_flags single_file out.m3u8
</pre>
<p> Will produce the playlist, <i>out.m3u8</i>, and a single segment file, <i>out.ts</i>.</p>
<dt><code>delete_segments</code></p>
<dd> Segment files removed from the playlist are deleted after a period of time equal to the duration of the segment plus the duration of the playlist.</p>
<dt><code>append_list</code></p>
<dd> Append new segments into the end of old segment list, and remove the <tt>&quot;#EXT-X-ENDLIST&quot;</tt> from the old segment list.</p>
<dt><code>round_durations</code></p>
<dd> Round the duration info in the playlist file segment info to integer values, instead of using floating point.</p>
<dt><code>discont_start</code></p>
<dd> Add the <tt>&quot;#EXT-X-DISCONTINUITY&quot;</tt> tag to the playlist, before the first segment&#8217;s information.</p>
<dt><code>omit_endlist</code></p>
<dd> Do not append the <tt>&quot;EXT-X-ENDLIST&quot;</tt> tag at the end of the playlist.</p>
<dt><code>periodic_rekey</code></p>
<dd> The file specified by <tt>&quot;hls_key_info_file&quot;</tt> will be checked periodically and detect updates to the encryption info. Be sure to replace this file atomically, including the file containing the <font SIZE="-1">AES</font> encryption key.</p>
<dt><code>independent_segments</code></p>
<dd> Add the <tt>&quot;#EXT-X-INDEPENDENT-SEGMENTS&quot;</tt> to playlists that has video segments and when all the segments of that playlist are guaranteed to start with a Key frame.</p>
<dt><code>iframes_only</code></p>
<dd> Add the <tt>&quot;#EXT-X-I-FRAMES-ONLY&quot;</tt> to playlists that has video segments and can play only I-frames in the <tt>&quot;#EXT-X-BYTERANGE&quot;</tt> mode.</p>
<dt><code>split_by_time</code></p>
<dd> Allow segments to start on frames other than keyframes. This improves behavior on some players when the time between keyframes is inconsistent, but may make things worse on others, and can cause some oddities during seeking. This flag should be used with the <tt>&quot;hls_time&quot;</tt> option.</p>
<dt><code>program_date_time</code></p>
<dd> Generate <tt>&quot;EXT-X-PROGRAM-DATE-TIME&quot;</tt> tags.</p>
<dt><code>second_level_segment_index</code></p>
<dd> Makes it possible to use segment indexes as %%d in hls_segment_filename expression besides date/time values when strftime is on. To get fixed width numbers with trailing zeroes, %%0xd format is available where x is the required width.</p>
<dt><code>second_level_segment_size</code></p>
<dd> Makes it possible to use segment sizes (counted in bytes) as %%s in hls_segment_filename expression besides date/time values when strftime is on. To get fixed width numbers with trailing zeroes, %%0xs format is available where x is the required width.</p>
<dt><code>second_level_segment_duration</code></p>
<dd> Makes it possible to use segment duration (calculated in microseconds) as %%t in hls_segment_filename expression besides date/time values when strftime is on. To get fixed width numbers with trailing zeroes, %%0xt format is available where x is the required width. </p>
<pre>
        ffmpeg -i sample.mpeg \
           -f hls -hls_time 3 -hls_list_size 5 \
           -hls_flags second_level_segment_index+second_level_segment_size+second_level_segment_duration \
           -strftime 1 -strftime_mkdir 1 -hls_segment_filename &quot;segment_%Y%m%d%H%M%S_%%04d_%%08s_%%013t.ts&quot; stream.m3u8
</pre>
<p> This will produce segments like this: <i>segment_20170102194334_0003_00122200_0000003000000.ts</i>, <i>segment_20170102194334_0004_00120072_0000003000000.ts</i> etc.</p>
<dt><code>temp_file</code></p>
<dd> Write segment data to filename.tmp and rename to filename only once the segment is complete. A webserver serving up segments can be configured to reject requests to *.tmp to prevent access to in-progress segments before they have been added to the m3u8 playlist. This flag also affects how m3u8 playlist files are created. If this flag is set, all playlist files will written into temporary file and renamed after they are complete, similarly as segments are handled. But playlists with <tt>&quot;file&quot;</tt> protocol and with type (<tt>&quot;hls_playlist_type&quot;</tt>) other than <tt>&quot;vod&quot;</tt> are always written into temporary file regardless of this flag. Master playlist files (<tt>&quot;master_pl_name&quot;</tt>), if any, with <tt>&quot;file&quot;</tt> protocol, are always written into temporary file regardless of this flag if <tt>&quot;master_pl_publish_rate&quot;</tt> value is other than zero.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>hls_playlist_type event</code></p>
<dd> Emit <tt>&quot;#EXT-X-PLAYLIST-TYPE:EVENT&quot;</tt> in the m3u8 header. Forces <code>hls_list_size</code> to 0; the playlist can only be appended to.</p>
<dt><code>hls_playlist_type vod</code></p>
<dd> Emit <tt>&quot;#EXT-X-PLAYLIST-TYPE:VOD&quot;</tt> in the m3u8 header. Forces <code>hls_list_size</code> to 0; the playlist must not change.</p>
<dt><code>method</code></p>
<dd> Use the given <font SIZE="-1">HTTP</font> method to create the hls files. </p>
<pre>
        ffmpeg -re -i in.ts -f hls -method PUT <a rel="nofollow" href="http://example.com/live/out.m3u8">http://example.com/live/out.m3u8</a>
</pre>
<p> This example will upload all the mpegts segment files to the <font SIZE="-1">HTTP</font> server using the <font SIZE="-1">HTTP PUT</font> method, and update the m3u8 files every <tt>&quot;refresh&quot;</tt> times using the same method. Note that the <font SIZE="-1">HTTP</font> server must support the given method for uploading files.</p>
<dt><code>http_user_agent</code></p>
<dd> Override User-Agent field in <font SIZE="-1">HTTP</font> header. Applicable only for <font SIZE="-1">HTTP</font> output.</p>
<dt><code>var_stream_map</code></p>
<dd> Map string which specifies how to group the audio, video and subtitle streams into different variant streams. The variant stream groups are separated by space. Expected string format is like this &#8220;a:0,v:0 a:1,v:1 &#8230;.&#8221;. Here a:, v:, s: are the keys to specify audio, video and subtitle streams respectively. Allowed values are 0 to 9 (limited just based on practical usage). </p>
<p> When there are two or more variant streams, the output filename pattern must contain the string &#8220;%v&#8221;, this string specifies the position of variant stream index in the output media playlist filenames. The string &#8220;%v&#8221; may be present in the filename or in the last directory name containing the file. If the string is present in the directory name, then sub-directories are created after expanding the directory name pattern. This enables creation of variant streams in subdirectories. </p>
<pre>
        ffmpeg -re -i in.ts -b:v:0 1000k -b:v:1 256k -b:a:0 64k -b:a:1 32k \
          -map 0:v -map 0:a -map 0:v -map 0:a -f hls -var_stream_map &quot;v:0,a:0 v:1,a:1&quot; \
          <a rel="nofollow" href="http://example.com/live/out_%v.m3u8">http://example.com/live/out_%v.m3u8</a>
</pre>
<p> This example creates two hls variant streams. The first variant stream will contain video stream of bitrate 1000k and audio stream of bitrate 64k and the second variant stream will contain video stream of bitrate 256k and audio stream of bitrate 32k. Here, two media playlist with file names out_0.m3u8 and out_1.m3u8 will be created. If you want something meaningful text instead of indexes in result names, you may specify names for each or some of the variants as in the following example. </p>
<pre>
        ffmpeg -re -i in.ts -b:v:0 1000k -b:v:1 256k -b:a:0 64k -b:a:1 32k \
          -map 0:v -map 0:a -map 0:v -map 0:a -f hls -var_stream_map &quot;v:0,a:0,name:my_hd v:1,a:1,name:my_sd&quot; \
          <a rel="nofollow" href="http://example.com/live/out_%v.m3u8">http://example.com/live/out_%v.m3u8</a>
</pre>
<p> This example creates two hls variant streams as in the previous one. But here, the two media playlist with file names out_my_hd.m3u8 and out_my_sd.m3u8 will be created. </p>
<pre>
        ffmpeg -re -i in.ts -b:v:0 1000k -b:v:1 256k -b:a:0 64k \
          -map 0:v -map 0:a -map 0:v -f hls -var_stream_map &quot;v:0 a:0 v:1&quot; \
          <a rel="nofollow" href="http://example.com/live/out_%v.m3u8">http://example.com/live/out_%v.m3u8</a>
</pre>
<p> This example creates three hls variant streams. The first variant stream will be a video only stream with video bitrate 1000k, the second variant stream will be an audio only stream with bitrate 64k and the third variant stream will be a video only stream with bitrate 256k. Here, three media playlist with file names out_0.m3u8, out_1.m3u8 and out_2.m3u8 will be created. </p>
<pre>
        ffmpeg -re -i in.ts -b:v:0 1000k -b:v:1 256k -b:a:0 64k -b:a:1 32k \
          -map 0:v -map 0:a -map 0:v -map 0:a -f hls -var_stream_map &quot;v:0,a:0 v:1,a:1&quot; \
          <a rel="nofollow" href="http://example.com/live/vs_%v/out.m3u8">http://example.com/live/vs_%v/out.m3u8</a>
</pre>
<p> This example creates the variant streams in subdirectories. Here, the first media playlist is created at <i><a rel="nofollow" href="http://example.com/live/vs_0/out.m3u8">http://example.com/live/vs_0/out.m3u8</a></i> and the second one at <i><a rel="nofollow" href="http://example.com/live/vs_1/out.m3u8">http://example.com/live/vs_1/out.m3u8</a></i>. </p>
<pre>
        ffmpeg -re -i in.ts -b:a:0 32k -b:a:1 64k -b:v:0 1000k -b:v:1 3000k  \
          -map 0:a -map 0:a -map 0:v -map 0:v -f hls \
          -var_stream_map &quot;a:0,agroup:aud_low a:1,agroup:aud_high v:0,agroup:aud_low v:1,agroup:aud_high&quot; \
          -master_pl_name master.m3u8 \
          <a rel="nofollow" href="http://example.com/live/out_%v.m3u8">http://example.com/live/out_%v.m3u8</a>
</pre>
<p> This example creates two audio only and two video only variant streams. In addition to the #EXT-X-STREAM-INF tag for each variant stream in the master playlist, #EXT-X-MEDIA tag is also added for the two audio only variant streams and they are mapped to the two video only variant streams with audio group names &#8216;aud_low&#8217; and &#8216;aud_high&#8217;. </p>
<p> By default, a single hls variant containing all the encoded streams is created. </p>
<pre>
        ffmpeg -re -i in.ts -b:a:0 32k -b:a:1 64k -b:v:0 1000k \
          -map 0:a -map 0:a -map 0:v -f hls \
          -var_stream_map &quot;a:0,agroup:aud_low,default:yes a:1,agroup:aud_low v:0,agroup:aud_low&quot; \
          -master_pl_name master.m3u8 \
          <a rel="nofollow" href="http://example.com/live/out_%v.m3u8">http://example.com/live/out_%v.m3u8</a>
</pre>
<p> This example creates two audio only and one video only variant streams. In addition to the #EXT-X-STREAM-INF tag for each variant stream in the master playlist, #EXT-X-MEDIA tag is also added for the two audio only variant streams and they are mapped to the one video only variant streams with audio group name &#8216;aud_low&#8217;, and the audio group have default stat is <font SIZE="-1">NO</font> or <font SIZE="-1">YES.</font> </p>
<p> By default, a single hls variant containing all the encoded streams is created. </p>
<pre>
        ffmpeg -re -i in.ts -b:a:0 32k -b:a:1 64k -b:v:0 1000k \
          -map 0:a -map 0:a -map 0:v -f hls \
          -var_stream_map &quot;a:0,agroup:aud_low,default:yes,language:ENG a:1,agroup:aud_low,language:CHN v:0,agroup:aud_low&quot; \
          -master_pl_name master.m3u8 \
          <a rel="nofollow" href="http://example.com/live/out_%v.m3u8">http://example.com/live/out_%v.m3u8</a>
</pre>
<p> This example creates two audio only and one video only variant streams. In addition to the #EXT-X-STREAM-INF tag for each variant stream in the master playlist, #EXT-X-MEDIA tag is also added for the two audio only variant streams and they are mapped to the one video only variant streams with audio group name &#8216;aud_low&#8217;, and the audio group have default stat is <font SIZE="-1">NO</font> or <font SIZE="-1">YES,</font> and one audio have and language is named <font SIZE="-1">ENG,</font> the other audio language is named <font SIZE="-1">CHN.</font> </p>
<p> By default, a single hls variant containing all the encoded streams is created. </p>
<pre>
        ffmpeg -y -i input_with_subtitle.mkv \
         -b:v:0 5250k -c:v h264 -pix_fmt yuv420p -profile:v main -level 4.1 \
         -b:a:0 256k \
         -c:s webvtt -c:a mp2 -ar 48000 -ac 2 -map 0:v -map 0:a:0 -map 0:s:0 \
         -f hls -var_stream_map &quot;v:0,a:0,s:0,sgroup:subtitle&quot; \
         -master_pl_name master.m3u8 -t 300 -hls_time 10 -hls_init_time 4 -hls_list_size \
         10 -master_pl_publish_rate 10  -hls_flags \
         delete_segments+discont_start+split_by_time ./tmp/video.m3u8
</pre>
<p> This example adds <tt>&quot;#EXT-X-MEDIA&quot;</tt> tag with <tt>&quot;TYPE=SUBTITLES&quot;</tt> in the master playlist with webvtt subtitle group name &#8216;subtitle&#8217;. Please make sure the input file has one text subtitle stream at least.</p>
<dt><code>cc_stream_map</code></p>
<dd> Map string which specifies different closed captions groups and their attributes. The closed captions stream groups are separated by space. Expected string format is like this &#8220;ccgroup:&lt;group name&gt;,instreamid:&lt;<font SIZE="-1">INSTREAM-ID</font>&gt;,language:&lt;language code&gt; &#8230;.&#8221;. &#8216;ccgroup&#8217; and &#8216;instreamid&#8217; are mandatory attributes. &#8216;language&#8217; is an optional attribute. The closed captions groups configured using this option are mapped to different variant streams by providing the same &#8216;ccgroup&#8217; name in the <tt>&quot;var_stream_map&quot;</tt> string. If <tt>&quot;var_stream_map&quot;</tt> is not set, then the first available ccgroup in <tt>&quot;cc_stream_map&quot;</tt> is mapped to the output variant stream. The examples for these two use cases are given below. </p>
<pre>
        ffmpeg -re -i in.ts -b:v 1000k -b:a 64k -a53cc 1 -f hls \
          -cc_stream_map &quot;ccgroup:cc,instreamid:CC1,language:en&quot; \
          -master_pl_name master.m3u8 \
          <a rel="nofollow" href="http://example.com/live/out.m3u8">http://example.com/live/out.m3u8</a>
</pre>
<p> This example adds <tt>&quot;#EXT-X-MEDIA&quot;</tt> tag with <tt>&quot;TYPE=CLOSED-CAPTIONS&quot;</tt> in the master playlist with group name &#8216;cc&#8217;, language &#8216;en&#8217; (english) and INSTREAM-ID &#8216;<font SIZE="-1">CC1</font>&#8216;. Also, it adds <tt>&quot;CLOSED-CAPTIONS&quot;</tt> attribute with group name &#8216;cc&#8217; for the output variant stream. </p>
<pre>
        ffmpeg -re -i in.ts -b:v:0 1000k -b:v:1 256k -b:a:0 64k -b:a:1 32k \
          -a53cc:0 1 -a53cc:1 1\
          -map 0:v -map 0:a -map 0:v -map 0:a -f hls \
          -cc_stream_map &quot;ccgroup:cc,instreamid:CC1,language:en ccgroup:cc,instreamid:CC2,language:sp&quot; \
          -var_stream_map &quot;v:0,a:0,ccgroup:cc v:1,a:1,ccgroup:cc&quot; \
          -master_pl_name master.m3u8 \
          <a rel="nofollow" href="http://example.com/live/out_%v.m3u8">http://example.com/live/out_%v.m3u8</a>
</pre>
<p> This example adds two <tt>&quot;#EXT-X-MEDIA&quot;</tt> tags with <tt>&quot;TYPE=CLOSED-CAPTIONS&quot;</tt> in the master playlist for the INSTREAM-IDs &#8216;<font SIZE="-1">CC1</font>&#8216; and &#8216;<font SIZE="-1">CC2</font>&#8216;. Also, it adds <tt>&quot;CLOSED-CAPTIONS&quot;</tt> attribute with group name &#8216;cc&#8217; for the two output variant streams.</p>
<dt><code>master_pl_name</code></p>
<dd> Create <font SIZE="-1">HLS</font> master playlist with the given name. </p>
<pre>
        ffmpeg -re -i in.ts -f hls -master_pl_name master.m3u8 <a rel="nofollow" href="http://example.com/live/out.m3u8">http://example.com/live/out.m3u8</a>
</pre>
<p> This example creates <font SIZE="-1">HLS</font> master playlist with name master.m3u8 and it is published at <a rel="nofollow" href="http://example.com/live/">http://example.com/live/</a></p>
<dt><code>master_pl_publish_rate</code></p>
<dd> Publish master play list repeatedly every after specified number of segment intervals. </p>
<pre>
        ffmpeg -re -i in.ts -f hls -master_pl_name master.m3u8 \
        -hls_time 2 -master_pl_publish_rate 30 <a rel="nofollow" href="http://example.com/live/out.m3u8">http://example.com/live/out.m3u8</a>
</pre>
<p> This example creates <font SIZE="-1">HLS</font> master playlist with name master.m3u8 and keep publishing it repeatedly every after 30 segments i.e. every after 60s.</p>
<dt><code>http_persistent</code></p>
<dd> Use persistent <font SIZE="-1">HTTP</font> connections. Applicable only for <font SIZE="-1">HTTP</font> output.</p>
<dt><code>timeout</code></p>
<dd> Set timeout for socket I/O operations. Applicable only for <font SIZE="-1">HTTP</font> output.</p>
<dt><code>-ignore_io_errors</code></p>
<dd> Ignore <font SIZE="-1">IO</font> errors during open, write and delete. Useful for long-duration runs with network output.</p>
<dt><code>headers</code></p>
<dd> Set custom <font SIZE="-1">HTTP</font> headers, can override built in default headers. Applicable only for <font SIZE="-1">HTTP</font> output.</dl>
<h3>ico</h3>
<p> <font SIZE="-1">ICO</font> file muxer. </p>
<p> Microsoft&#8217;s icon file format (<font SIZE="-1">ICO</font>) has some strict limitations that should be noted:</p>
<dl>
<dt>&bull;</p>
<dd> Size cannot exceed 256 pixels in any dimension</p>
<dt>&bull;</p>
<dd> Only <font SIZE="-1">BMP</font> and <font SIZE="-1">PNG</font> images can be stored</p>
<dt>&bull;</p>
<dd> If a <font SIZE="-1">BMP</font> image is used, it must be one of the following pixel formats: </p>
<pre>
        BMP Bit Depth      FFmpeg Pixel Format
        1bit               pal8
        4bit               pal8
        8bit               pal8
        16bit              rgb555le
        24bit              bgr24
        32bit              bgra
</pre>
<dt>&bull;</p>
<dd> If a <font SIZE="-1">BMP</font> image is used, it must use the <font SIZE="-1">BITMAPINFOHEADER DIB</font> header</p>
<dt>&bull;</p>
<dd> If a <font SIZE="-1">PNG</font> image is used, it must use the rgba pixel format</dl>
<h3>image2</h3>
<p> Image file muxer. </p>
<p> The image file muxer writes video frames to image files. </p>
<p> The output filenames are specified by a pattern, which can be used to produce sequentially numbered series of files. The pattern may contain the string &#8220;%d&#8221; or &quot;%0<i>N</i>d&#8220;, this string specifies the position of the characters representing a numbering in the filenames. If the form &#8221;%0<i>N</i>d&quot; is used, the string representing the number in each filename is 0-padded to <i>N</i> digits. The literal character &#8216;%&#8217; can be specified in the pattern with the string &#8220;%%&#8221;. </p>
<p> If the pattern contains &#8220;%d&#8221; or &quot;%0<i>N</i>d&quot;, the first filename of the file list specified will contain the number 1, all the following numbers will be sequential. </p>
<p> The pattern may contain a suffix which is used to automatically determine the format of the image files to write. </p>
<p> For example the pattern &#8220;img-%03d.bmp&#8221; will specify a sequence of filenames of the form <i>img-001.bmp</i>, <i>img-002.bmp</i>, &#8230;, <i>img-010.bmp</i>, etc. The pattern &#8220;img%%-%d.jpg&#8221; will specify a sequence of filenames of the form <i>img%-1.jpg</i>, <i>img%-2.jpg</i>, &#8230;, <i>img%-10.jpg</i>, etc. </p>
<p> The image muxer supports the .Y.U.V image file format. This format is special in that that each image frame consists of three files, for each of the <font SIZE="-1">YUV420P</font> components. To read or write this image file format, specify the name of the &#8216;.Y&#8217; file. The muxer will automatically open the &#8216;.U&#8217; and &#8216;.V&#8217; files as required. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>frame_pts</code></p>
<dd> If set to 1, expand the filename with pts from pkt-&gt;pts. Default value is 0.</p>
<dt><code>start_number</code></p>
<dd> Start the sequence from the specified number. Default value is 1.</p>
<dt><code>update</code></p>
<dd> If set to 1, the filename will always be interpreted as just a filename, not a pattern, and the corresponding file will be continuously overwritten with new images. Default value is 0.</p>
<dt><code>strftime</code></p>
<dd> If set to 1, expand the filename with date and time information from <tt>&quot;strftime()&quot;</tt>. Default value is 0.</p>
<dt><code>protocol_opts</code> <i>options_list</i></p>
<dd> Set protocol options as a :-separated list of key=value parameters. Values containing the <tt>&quot;:&quot;</tt> special character must be escaped.</dl>
<p> <i>Examples</i> </p>
<p> The following example shows how to use <code>ffmpeg</code> for creating a sequence of files <i>img-001.jpeg</i>, <i>img-002.jpeg</i>, &#8230;, taking one image every second from the input video: </p>
<pre>
        ffmpeg -i in.avi -vsync cfr -r 1 -f image2 'img-%03d.jpeg'
</pre>
<p> Note that with <code>ffmpeg</code>, if the format is not specified with the <tt>&quot;-f&quot;</tt> option and the output filename specifies an image file format, the image2 muxer is automatically selected, so the previous command can be written as: </p>
<pre>
        ffmpeg -i in.avi -vsync cfr -r 1 'img-%03d.jpeg'
</pre>
<p> Note also that the pattern must not necessarily contain &#8220;%d&#8221; or &quot;%0<i>N</i>d&quot;, for example to create a single image file <i>img.jpeg</i> from the start of the input video you can employ the command: </p>
<pre>
        ffmpeg -i in.avi -f image2 -frames:v 1 img.jpeg
</pre>
<p> The <code>strftime</code> option allows you to expand the filename with date and time information. Check the documentation of the <tt>&quot;strftime()&quot;</tt> function for the syntax. </p>
<p> For example to generate image files from the <tt>&quot;strftime()&quot;</tt> &#8220;%Y-%m-%d_%H-%M-%S&#8221; pattern, the following <code>ffmpeg</code> command can be used: </p>
<pre>
        ffmpeg -f v4l2 -r 1 -i /dev/video0 -f image2 -strftime 1 &quot;%Y-%m-%d_%H-%M-%S.jpg&quot;
</pre>
<p> You can set the file name with current frame&#8217;s <font SIZE="-1">PTS:</font> </p>
<pre>
        ffmpeg -f v4l2 -r 1 -i /dev/video0 -copyts -f image2 -frame_pts true %d.jpg&quot;
</pre>
<p> A more complex example is to publish contents of your desktop directly to a WebDAV server every second: </p>
<pre>
        ffmpeg -f x11grab -framerate 1 -i :0.0 -q:v 6 -update 1 -protocol_opts method=PUT <a rel="nofollow" href="http://example.com/desktop.jpg">http://example.com/desktop.jpg</a>
</pre>
<h3>matroska</h3>
<p> Matroska container muxer. </p>
<p> This muxer implements the matroska and webm container specs. </p>
<p> <i>Metadata</i> </p>
<p> The recognized metadata settings in this muxer are:</p>
<dl>
<dt><code>title</code></p>
<dd> Set title name provided to a single track. This gets mapped to the FileDescription element for a stream written as attachment.</p>
<dt><code>language</code></p>
<dd> Specify the language of the track in the Matroska languages form. </p>
<p> The language can be either the 3 letters bibliographic <font SIZE="-1">ISO-639-2</font> (<font SIZE="-1">ISO 639-2/B</font>) form (like &#8220;fre&#8221; for French), or a language code mixed with a country code for specialities in languages (like &#8220;fre-ca&#8221; for Canadian French).</p>
<dt><code>stereo_mode</code></p>
<dd> Set stereo 3D video layout of two views in a single video track. </p>
<p> The following values are recognized:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>mono</code></p>
<dd> video is not stereo</p>
<dt><code>left_right</code></p>
<dd> Both views are arranged side by side, Left-eye view is on the left</p>
<dt><code>bottom_top</code></p>
<dd> Both views are arranged in top-bottom orientation, Left-eye view is at bottom</p>
<dt><code>top_bottom</code></p>
<dd> Both views are arranged in top-bottom orientation, Left-eye view is on top</p>
<dt><code>checkerboard_rl</code></p>
<dd> Each view is arranged in a checkerboard interleaved pattern, Left-eye view being first</p>
<dt><code>checkerboard_lr</code></p>
<dd> Each view is arranged in a checkerboard interleaved pattern, Right-eye view being first</p>
<dt><code>row_interleaved_rl</code></p>
<dd> Each view is constituted by a row based interleaving, Right-eye view is first row</p>
<dt><code>row_interleaved_lr</code></p>
<dd> Each view is constituted by a row based interleaving, Left-eye view is first row</p>
<dt><code>col_interleaved_rl</code></p>
<dd> Both views are arranged in a column based interleaving manner, Right-eye view is first column</p>
<dt><code>col_interleaved_lr</code></p>
<dd> Both views are arranged in a column based interleaving manner, Left-eye view is first column</p>
<dt><code>anaglyph_cyan_red</code></p>
<dd> All frames are in anaglyph format viewable through red-cyan filters</p>
<dt><code>right_left</code></p>
<dd> Both views are arranged side by side, Right-eye view is on the left</p>
<dt><code>anaglyph_green_magenta</code></p>
<dd> All frames are in anaglyph format viewable through green-magenta filters</p>
<dt><code>block_lr</code></p>
<dd> Both eyes laced in one Block, Left-eye view is first</p>
<dt><code>block_rl</code></p>
<dd> Both eyes laced in one Block, Right-eye view is first</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<p> For example a 3D WebM clip can be created using the following command line: </p>
<pre>
        ffmpeg -i sample_left_right_clip.mpg -an -c:v libvpx -metadata stereo_mode=left_right -y stereo_clip.webm
</pre>
<p> <i>Options</i> </p>
<p> This muxer supports the following options:</p>
<dl>
<dt><code>reserve_index_space</code></p>
<dd> By default, this muxer writes the index for seeking (called cues in Matroska terms) at the end of the file, because it cannot know in advance how much space to leave for the index at the beginning of the file. However for some use cases &#8212; e.g. streaming where seeking is possible but slow &#8212; it is useful to put the index at the beginning of the file. </p>
<p> If this option is set to a non-zero value, the muxer will reserve a given amount of space in the file header and then try to write the cues there when the muxing finishes. If the reserved space does not suffice, no Cues will be written, the file will be finalized and writing the trailer will return an error. A safe size for most use cases should be about 50kB per hour of video. </p>
<p> Note that cues are only written if the output is seekable and this option will have no effect if it is not.</p>
<dt><code>default_mode</code></p>
<dd> This option controls how the FlagDefault of the output tracks will be set. It influences which tracks players should play by default. The default mode is <code>infer</code>.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>infer</code></p>
<dd> In this mode, for each type of track (audio, video or subtitle), if there is a track with disposition default of this type, then the first such track (i.e. the one with the lowest index) will be marked as default; if no such track exists, the first track of this type will be marked as default instead (if existing). This ensures that the default flag is set in a sensible way even if the input originated from containers that lack the concept of default tracks.</p>
<dt><code>infer_no_subs</code></p>
<dd> This mode is the same as infer except that if no subtitle track with disposition default exists, no subtitle track will be marked as default.</p>
<dt><code>passthrough</code></p>
<dd> In this mode the FlagDefault is set if and only if the <font SIZE="-1">AV_DISPOSITION_DEFAULT</font> flag is set in the disposition of the corresponding stream.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>flipped_raw_rgb</code></p>
<dd> If set to true, store positive height for raw <font SIZE="-1">RGB</font> bitmaps, which indicates bitmap is stored bottom-up. Note that this option does not flip the bitmap which has to be done manually beforehand, e.g. by using the vflip filter. Default is <i>false</i> and indicates bitmap is stored top down.</dl>
<h3>md5</h3>
<p> <font SIZE="-1">MD5</font> testing format. </p>
<p> This is a variant of the <code>hash</code> muxer. Unlike that muxer, it defaults to using the <font SIZE="-1">MD5</font> hash function. </p>
<p> <i>Examples</i> </p>
<p> To compute the <font SIZE="-1">MD5</font> hash of the input converted to raw audio and video, and store it in the file <i>out.md5</i>: </p>
<pre>
        ffmpeg -i INPUT -f md5 out.md5
</pre>
<p> You can print the <font SIZE="-1">MD5</font> to stdout with the command: </p>
<pre>
        ffmpeg -i INPUT -f md5 -
</pre>
<p> See also the <code>hash</code> and <code>framemd5</code> muxers.</p>
<h3>mov, mp4, ismv</h3>
<p> <font SIZE="-1">MOV/MP4/ISMV</font> (Smooth Streaming) muxer. </p>
<p> The mov/mp4/ismv muxer supports fragmentation. Normally, a <font SIZE="-1">MOV/MP4</font> file has all the metadata about all packets stored in one location (written at the end of the file, it can be moved to the start for better playback by adding <i>faststart</i> to the <i>movflags</i>, or using the <code>qt-faststart</code> tool). A fragmented file consists of a number of fragments, where packets and metadata about these packets are stored together. Writing a fragmented file has the advantage that the file is decodable even if the writing is interrupted (while a normal <font SIZE="-1">MOV/MP4</font> is undecodable if it is not properly finished), and it requires less memory when writing very long files (since writing normal <font SIZE="-1">MOV/MP4</font> files stores info about every single packet in memory until the file is closed). The downside is that it is less compatible with other applications. </p>
<p> <i>Options</i> </p>
<p> Fragmentation is enabled by setting one of the AVOptions that define how to cut the file into fragments:</p>
<dl>
<dt><code>-moov_size</code> <i>bytes</i></p>
<dd> Reserves space for the moov atom at the beginning of the file instead of placing the moov atom at the end. If the space reserved is insufficient, muxing will fail.</p>
<dt><code>-movflags frag_keyframe</code></p>
<dd> Start a new fragment at each video keyframe.</p>
<dt><code>-frag_duration</code> <i>duration</i></p>
<dd> Create fragments that are <i>duration</i> microseconds long.</p>
<dt><code>-frag_size</code> <i>size</i></p>
<dd> Create fragments that contain up to <i>size</i> bytes of payload data.</p>
<dt><code>-movflags frag_custom</code></p>
<dd> Allow the caller to manually choose when to cut fragments, by calling <tt>&quot;av_write_frame(ctx, NULL)&quot;</tt> to write a fragment with the packets written so far. (This is only useful with other applications integrating libavformat, not from <code>ffmpeg</code>.)</p>
<dt><code>-min_frag_duration</code> <i>duration</i></p>
<dd> Don&#8217;t create fragments that are shorter than <i>duration</i> microseconds long.</dl>
<p> If more than one condition is specified, fragments are cut when one of the specified conditions is fulfilled. The exception to this is <tt>&quot;-min_frag_duration&quot;</tt>, which has to be fulfilled for any of the other conditions to apply. </p>
<p> Additionally, the way the output file is written can be adjusted through a few other options:</p>
<dl>
<dt><code>-movflags empty_moov</code></p>
<dd> Write an initial moov atom directly at the start of the file, without describing any samples in it. Generally, an mdat/moov pair is written at the start of the file, as a normal <font SIZE="-1">MOV/MP4</font> file, containing only a short portion of the file. With this option set, there is no initial mdat atom, and the moov atom only describes the tracks but has a zero duration. </p>
<p> This option is implicitly set when writing ismv (Smooth Streaming) files.</p>
<dt><code>-movflags separate_moof</code></p>
<dd> Write a separate moof (movie fragment) atom for each track. Normally, packets for all tracks are written in a moof atom (which is slightly more efficient), but with this option set, the muxer writes one moof/mdat pair for each track, making it easier to separate tracks. </p>
<p> This option is implicitly set when writing ismv (Smooth Streaming) files.</p>
<dt><code>-movflags skip_sidx</code></p>
<dd> Skip writing of sidx atom. When bitrate overhead due to sidx atom is high, this option could be used for cases where sidx atom is not mandatory. When global_sidx flag is enabled, this option will be ignored.</p>
<dt><code>-movflags faststart</code></p>
<dd> Run a second pass moving the index (moov atom) to the beginning of the file. This operation can take a while, and will not work in various situations such as fragmented output, thus it is not enabled by default.</p>
<dt><code>-movflags rtphint</code></p>
<dd> Add <font SIZE="-1">RTP</font> hinting tracks to the output file.</p>
<dt><code>-movflags disable_chpl</code></p>
<dd> Disable Nero chapter markers (chpl atom). Normally, both Nero chapters and a QuickTime chapter track are written to the file. With this option set, only the QuickTime chapter track will be written. Nero chapters can cause failures when the file is reprocessed with certain tagging programs, like mp3Tag 2.61a and iTunes 11.3, most likely other versions are affected as well.</p>
<dt><code>-movflags omit_tfhd_offset</code></p>
<dd> Do not write any absolute base_data_offset in tfhd atoms. This avoids tying fragments to absolute byte positions in the file/streams.</p>
<dt><code>-movflags default_base_moof</code></p>
<dd> Similarly to the omit_tfhd_offset, this flag avoids writing the absolute base_data_offset field in tfhd atoms, but does so by using the new default-base-is-moof flag instead. This flag is new from 14496-12:2012. This may make the fragments easier to parse in certain circumstances (avoiding basing track fragment location calculations on the implicit end of the previous track fragment).</p>
<dt><code>-write_tmcd</code></p>
<dd> Specify <tt>&quot;on&quot;</tt> to force writing a timecode track, <tt>&quot;off&quot;</tt> to disable it and <tt>&quot;auto&quot;</tt> to write a timecode track only for mov and mp4 output (default).</p>
<dt><code>-movflags negative_cts_offsets</code></p>
<dd> Enables utilization of version 1 of the <font SIZE="-1">CTTS</font> box, in which the <font SIZE="-1">CTS</font> offsets can be negative. This enables the initial sample to have <font SIZE="-1">DTS/CTS</font> of zero, and reduces the need for edit lists for some cases such as video tracks with B-frames. Additionally, eases conformance with the DASH-IF interoperability guidelines. </p>
<p> This option is implicitly set when writing ismv (Smooth Streaming) files.</p>
<dt><code>-write_prft</code></p>
<dd> Write producer time reference box (<font SIZE="-1">PRFT</font>) with a specified time source for the <font SIZE="-1">NTP</font> field in the <font SIZE="-1">PRFT</font> box. Set value as <code>wallclock</code> to specify timesource as wallclock time and <code>pts</code> to specify timesource as input packets&#8217; <font SIZE="-1">PTS</font> values. </p>
<p> Setting value to <code>pts</code> is applicable only for a live encoding use case, where <font SIZE="-1">PTS</font> values are set as as wallclock time at the source. For example, an encoding use case with decklink capture source where <code>video_pts</code> and <code>audio_pts</code> are set to <code>abs_wallclock</code>.</dl>
<p> <i>Example</i> </p>
<p> Smooth Streaming content can be pushed in real time to a publishing point on <font SIZE="-1">IIS</font> with this muxer. Example: </p>
<pre>
        ffmpeg -re &lt;&lt;normal input/transcoding options&gt;&gt; -movflags isml+frag_keyframe -f ismv <a rel="nofollow" href="http://server/publishingpoint.isml/Streams(Encoder1)">http://server/publishingpoint.isml/Streams(Encoder1)</a>
</pre>
<h3>mp3</h3>
<p> The <font SIZE="-1">MP3</font> muxer writes a raw <font SIZE="-1">MP3</font> stream with the following optional features:</p>
<dl>
<dt>&bull;</p>
<dd> An ID3v2 metadata header at the beginning (enabled by default). Versions 2.3 and 2.4 are supported, the <tt>&quot;id3v2_version&quot;</tt> private option controls which one is used (3 or 4). Setting <tt>&quot;id3v2_version&quot;</tt> to 0 disables the ID3v2 header completely. </p>
<p> The muxer supports writing attached pictures (<font SIZE="-1">APIC</font> frames) to the ID3v2 header. The pictures are supplied to the muxer in form of a video stream with a single packet. There can be any number of those streams, each will correspond to a single <font SIZE="-1">APIC</font> frame. The stream metadata tags <i>title</i> and <i>comment</i> map to <font SIZE="-1">APIC</font> <i>description</i> and <i>picture type</i> respectively. See &lt;<code><a rel="nofollow" href="http://id3.org/id3v2.4.0-frames">http://id3.org/id3v2.4.0-frames</a></code>&gt; for allowed picture types. </p>
<p> Note that the <font SIZE="-1">APIC</font> frames must be written at the beginning, so the muxer will buffer the audio frames until it gets all the pictures. It is therefore advised to provide the pictures as soon as possible to avoid excessive buffering.</p>
<dt>&bull;</p>
<dd> A Xing/LAME frame right after the ID3v2 header (if present). It is enabled by default, but will be written only if the output is seekable. The <tt>&quot;write_xing&quot;</tt> private option can be used to disable it. The frame contains various information that may be useful to the decoder, like the audio duration or encoder delay.</p>
<dt>&bull;</p>
<dd> A legacy ID3v1 tag at the end of the file (disabled by default). It may be enabled with the <tt>&quot;write_id3v1&quot;</tt> private option, but as its capabilities are very limited, its usage is not recommended.</dl>
<p> Examples: </p>
<p> Write an mp3 with an ID3v2.3 header and an ID3v1 footer: </p>
<pre>
        ffmpeg -i INPUT -id3v2_version 3 -write_id3v1 1 out.mp3
</pre>
<p> To attach a picture to an mp3 file select both the audio and the picture stream with <tt>&quot;map&quot;</tt>: </p>
<pre>
        ffmpeg -i input.mp3 -i cover.png -c copy -map 0 -map 1
        -metadata:s:v title=&quot;Album cover&quot; -metadata:s:v comment=&quot;Cover (Front)&quot; out.mp3
</pre>
<p> Write a &#8220;clean&#8221; <font SIZE="-1">MP3</font> without any extra features: </p>
<pre>
        ffmpeg -i input.wav -write_xing 0 -id3v2_version 0 out.mp3
</pre>
<h3>mpegts</h3>
<p> <font SIZE="-1">MPEG</font> transport stream muxer. </p>
<p> This muxer implements <font SIZE="-1">ISO 13818-1</font> and part of <font SIZE="-1">ETSI EN 300 468.</font> </p>
<p> The recognized metadata settings in mpegts muxer are <tt>&quot;service_provider&quot;</tt> and <tt>&quot;service_name&quot;</tt>. If they are not set the default for <tt>&quot;service_provider&quot;</tt> is <code>FFmpeg</code> and the default for <tt>&quot;service_name&quot;</tt> is <code>Service01</code>. </p>
<p> <i>Options</i> </p>
<p> The muxer options are:</p>
<dl>
<dt><code>mpegts_transport_stream_id</code> <i>integer</i></p>
<dd> Set the <code>transport_stream_id</code>. This identifies a transponder in <font SIZE="-1">DVB.</font> Default is <tt>0x0001</tt>.</p>
<dt><code>mpegts_original_network_id</code> <i>integer</i></p>
<dd> Set the <code>original_network_id</code>. This is unique identifier of a network in <font SIZE="-1">DVB.</font> Its main use is in the unique identification of a service through the path <code>Original_Network_ID, Transport_Stream_ID</code>. Default is <tt>0x0001</tt>.</p>
<dt><code>mpegts_service_id</code> <i>integer</i></p>
<dd> Set the <code>service_id</code>, also known as program in <font SIZE="-1">DVB.</font> Default is <tt>0x0001</tt>.</p>
<dt><code>mpegts_service_type</code> <i>integer</i></p>
<dd> Set the program <code>service_type</code>. Default is <tt>&quot;digital_tv&quot;</tt>. Accepts the following options:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>hex_value</code></p>
<dd> Any hexadecimal value between <tt>0x01</tt> and <tt>0xff</tt> as defined in <font SIZE="-1">ETSI 300 468.</font></p>
<dt><code>digital_tv</code></p>
<dd> Digital <font SIZE="-1">TV</font> service.</p>
<dt><code>digital_radio</code></p>
<dd> Digital Radio service.</p>
<dt><code>teletext</code></p>
<dd> Teletext service.</p>
<dt><code>advanced_codec_digital_radio</code></p>
<dd> Advanced Codec Digital Radio service.</p>
<dt><code>mpeg2_digital_hdtv</code></p>
<dd> <font SIZE="-1">MPEG2</font> Digital <font SIZE="-1">HDTV</font> service.</p>
<dt><code>advanced_codec_digital_sdtv</code></p>
<dd> Advanced Codec Digital <font SIZE="-1">SDTV</font> service.</p>
<dt><code>advanced_codec_digital_hdtv</code></p>
<dd> Advanced Codec Digital <font SIZE="-1">HDTV</font> service.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>mpegts_pmt_start_pid</code> <i>integer</i></p>
<dd> Set the first <font SIZE="-1">PID</font> for PMTs. Default is <tt>0x1000</tt>, minimum is <tt>0x0020</tt>, maximum is <tt>0x1ffa</tt>. This option has no effect in m2ts mode where the <font SIZE="-1">PMT PID</font> is fixed <tt>0x0100</tt>.</p>
<dt><code>mpegts_start_pid</code> <i>integer</i></p>
<dd> Set the first <font SIZE="-1">PID</font> for elementary streams. Default is <tt>0x0100</tt>, minimum is <tt>0x0020</tt>, maximum is <tt>0x1ffa</tt>. This option has no effect in m2ts mode where the elementary stream PIDs are fixed.</p>
<dt><code>mpegts_m2ts_mode</code> <i>boolean</i></p>
<dd> Enable m2ts mode if set to <tt>1</tt>. Default value is <tt>&quot;-1&quot;</tt> which disables m2ts mode.</p>
<dt><code>muxrate</code> <i>integer</i></p>
<dd> Set a constant muxrate. Default is <font SIZE="-1">VBR.</font></p>
<dt><code>pes_payload_size</code> <i>integer</i></p>
<dd> Set minimum <font SIZE="-1">PES</font> packet payload in bytes. Default is <tt>2930</tt>.</p>
<dt><code>mpegts_flags</code> <i>flags</i></p>
<dd> Set mpegts flags. Accepts the following options:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>resend_headers</code></p>
<dd> Reemit <font SIZE="-1">PAT/PMT</font> before writing the next packet.</p>
<dt><code>latm</code></p>
<dd> Use <font SIZE="-1">LATM</font> packetization for <font SIZE="-1">AAC.</font></p>
<dt><code>pat_pmt_at_frames</code></p>
<dd> Reemit <font SIZE="-1">PAT</font> and <font SIZE="-1">PMT</font> at each video frame.</p>
<dt><code>system_b</code></p>
<dd> Conform to System B (<font SIZE="-1">DVB</font>) instead of System A (<font SIZE="-1">ATSC</font>).</p>
<dt><code>initial_discontinuity</code></p>
<dd> Mark the initial packet of each stream as discontinuity.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>mpegts_copyts</code> <i>boolean</i></p>
<dd> Preserve original timestamps, if value is set to <tt>1</tt>. Default value is <tt>&quot;-1&quot;</tt>, which results in shifting timestamps so that they start from 0.</p>
<dt><code>omit_video_pes_length</code> <i>boolean</i></p>
<dd> Omit the <font SIZE="-1">PES</font> packet length for video packets. Default is <tt>1</tt> (true).</p>
<dt><code>pcr_period</code> <i>integer</i></p>
<dd> Override the default <font SIZE="-1">PCR</font> retransmission time in milliseconds. Default is <tt>&quot;-1&quot;</tt> which means that the <font SIZE="-1">PCR</font> interval will be determined automatically: 20 ms is used for <font SIZE="-1">CBR</font> streams, the highest multiple of the frame duration which is less than 100 ms is used for <font SIZE="-1">VBR</font> streams.</p>
<dt><code>pat_period</code> <i>duration</i></p>
<dd> Maximum time in seconds between <font SIZE="-1">PAT/PMT</font> tables. Default is <tt>0.1</tt>.</p>
<dt><code>sdt_period</code> <i>duration</i></p>
<dd> Maximum time in seconds between <font SIZE="-1">SDT</font> tables. Default is <tt>0.5</tt>.</p>
<dt><code>tables_version</code> <i>integer</i></p>
<dd> Set <font SIZE="-1">PAT, PMT</font> and <font SIZE="-1">SDT</font> version (default <tt>0</tt>, valid values are from 0 to 31, inclusively). This option allows updating stream structure so that standard consumer may detect the change. To do so, reopen output <tt>&quot;AVFormatContext&quot;</tt> (in case of <font SIZE="-1">API</font> usage) or restart <code>ffmpeg</code> instance, cyclically changing <code>tables_version</code> value: </p>
<pre>
        ffmpeg -i source1.ts -codec copy -f mpegts -tables_version 0 <a href="udp://1.1.1.1:1111">udp://1.1.1.1:1111</a>
        ffmpeg -i source2.ts -codec copy -f mpegts -tables_version 1 <a href="udp://1.1.1.1:1111">udp://1.1.1.1:1111</a>
        ...
        ffmpeg -i source3.ts -codec copy -f mpegts -tables_version 31 <a href="udp://1.1.1.1:1111">udp://1.1.1.1:1111</a>
        ffmpeg -i source1.ts -codec copy -f mpegts -tables_version 0 <a href="udp://1.1.1.1:1111">udp://1.1.1.1:1111</a>
        ffmpeg -i source2.ts -codec copy -f mpegts -tables_version 1 <a href="udp://1.1.1.1:1111">udp://1.1.1.1:1111</a>
        ...
</pre>
</dl>
<p> <i>Example</i> </p>
<pre>
        ffmpeg -i file.mpg -c copy \
             -mpegts_original_network_id 0x1122 \
             -mpegts_transport_stream_id 0x3344 \
             -mpegts_service_id 0x5566 \
             -mpegts_pmt_start_pid 0x1500 \
             -mpegts_start_pid 0x150 \
             -metadata service_provider=&quot;Some provider&quot; \
             -metadata service_name=&quot;Some Channel&quot; \
             out.ts
</pre>
<h3>mxf, mxf_d10, mxf_opatom</h3>
<p> <font SIZE="-1">MXF</font> muxer. </p>
<p> <i>Options</i> </p>
<p> The muxer options are:</p>
<dl>
<dt><code>store_user_comments</code> <i>bool</i></p>
<dd> Set if user comments should be stored if available or never. <font SIZE="-1">IRT D-10</font> does not allow user comments. The default is thus to write them for mxf and mxf_opatom but not for mxf_d10</dl>
<h3>null</h3>
<p> Null muxer. </p>
<p> This muxer does not generate any output file, it is mainly useful for testing or benchmarking purposes. </p>
<p> For example to benchmark decoding with <code>ffmpeg</code> you can use the command: </p>
<pre>
        ffmpeg -benchmark -i INPUT -f null out.null
</pre>
<p> Note that the above command does not read or write the <i>out.null</i> file, but specifying the output file is required by the <code>ffmpeg</code> syntax. </p>
<p> Alternatively you can write the command as: </p>
<pre>
        ffmpeg -benchmark -i INPUT -f null -
</pre>
<h3>nut</h3>
<dl>
<dt><code>-syncpoints</code> <i>flags</i></p>
<dd> Change the syncpoint usage in nut:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>default</i> <code>use the normal low-overhead seeking aids.</code></p>
<dd>
<dt><i>none</i> <code>do not use the syncpoints at all, reducing the overhead but making the stream non-seekable;</code></p>
<dd>
<pre>
    Use of this option is not recommended, as the resulting files are very damage
    sensitive and seeking is not possible. Also in general the overhead from
    syncpoints is negligible. Note, -C&lt;write_index&gt; 0 can be used to disable
    all growing data tables, allowing to mux endless streams with limited memory
    and without these disadvantages.
</pre>
<dt><i>timestamped</i> <code>extend the syncpoint with a wallclock field.</code></p>
<dd></dl>
</dl>
<dl>
<dt>
<dd>
<p> The <i>none</i> and <i>timestamped</i> flags are experimental.</dl>
<dt><code>-write_index</code> <i>bool</i></p>
<dd> Write index at the end, the default is to write an index.</dl>
<pre>
        ffmpeg -i INPUT -f_strict experimental -syncpoints none - | processor
</pre>
<h3>ogg</h3>
<p> Ogg container muxer.</p>
<dl>
<dt><code>-page_duration</code> <i>duration</i></p>
<dd> Preferred page duration, in microseconds. The muxer will attempt to create pages that are approximately <i>duration</i> microseconds long. This allows the user to compromise between seek granularity and container overhead. The default is 1 second. A value of 0 will fill all segments, making pages as large as possible. A value of 1 will effectively use 1 packet-per-page in most situations, giving a small seek granularity at the cost of additional container overhead.</p>
<dt><code>-serial_offset</code> <i>value</i></p>
<dd> Serial value from which to set the streams serial number. Setting it to different and sufficiently large values ensures that the produced ogg files can be safely chained.</dl>
<h3>segment, stream_segment, ssegment</h3>
<p> Basic stream segmenter. </p>
<p> This muxer outputs streams to a number of separate files of nearly fixed duration. Output filename pattern can be set in a fashion similar to <code>image2</code>, or by using a <tt>&quot;strftime&quot;</tt> template if the <code>strftime</code> option is enabled. </p>
<p> <tt>&quot;stream_segment&quot;</tt> is a variant of the muxer used to write to streaming output formats, i.e. which do not require global headers, and is recommended for outputting e.g. to <font SIZE="-1">MPEG</font> transport stream segments. <tt>&quot;ssegment&quot;</tt> is a shorter alias for <tt>&quot;stream_segment&quot;</tt>. </p>
<p> Every segment starts with a keyframe of the selected reference stream, which is set through the <code>reference_stream</code> option. </p>
<p> Note that if you want accurate splitting for a video file, you need to make the input key frames correspond to the exact splitting times expected by the segmenter, or the segment muxer will start the new segment with the key frame found next after the specified start time. </p>
<p> The segment muxer works best with a single constant frame rate video. </p>
<p> Optionally it can generate a list of the created segments, by setting the option <i>segment_list</i>. The list type is specified by the <i>segment_list_type</i> option. The entry filenames in the segment list are set by default to the basename of the corresponding segment files. </p>
<p> See also the <code>hls</code> muxer, which provides a more specific implementation for <font SIZE="-1">HLS</font> segmentation. </p>
<p> <i>Options</i> </p>
<p> The segment muxer supports the following options:</p>
<dl>
<dt><code>increment_tc</code> <i>1|0</i></p>
<dd> if set to <tt>1</tt>, increment timecode between each segment If this is selected, the input need to have a timecode in the first video stream. Default value is <tt>0</tt>.</p>
<dt><code>reference_stream</code> <i>specifier</i></p>
<dd> Set the reference stream, as specified by the string <i>specifier</i>. If <i>specifier</i> is set to <tt>&quot;auto&quot;</tt>, the reference is chosen automatically. Otherwise it must be a stream specifier (see the &#8220;Stream specifiers&#8221; chapter in the ffmpeg manual) which specifies the reference stream. The default value is <tt>&quot;auto&quot;</tt>.</p>
<dt><code>segment_format</code> <i>format</i></p>
<dd> Override the inner container format, by default it is guessed by the filename extension.</p>
<dt><code>segment_format_options</code> <i>options_list</i></p>
<dd> Set output format options using a :-separated list of key=value parameters. Values containing the <tt>&quot;:&quot;</tt> special character must be escaped.</p>
<dt><code>segment_list</code> <i>name</i></p>
<dd> Generate also a listfile named <i>name</i>. If not specified no listfile is generated.</p>
<dt><code>segment_list_flags</code> <i>flags</i></p>
<dd> Set flags affecting the segment list generation. </p>
<p> It currently supports the following flags:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>cache</code></p>
<dd> Allow caching (only affects M3U8 list files).</p>
<dt><code>live</code></p>
<dd> Allow live-friendly file generation.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>segment_list_size</code> <i>size</i></p>
<dd> Update the list file so that it contains at most <i>size</i> segments. If 0 the list file will contain all the segments. Default value is 0.</p>
<dt><code>segment_list_entry_prefix</code> <i>prefix</i></p>
<dd> Prepend <i>prefix</i> to each entry. Useful to generate absolute paths. By default no prefix is applied.</p>
<dt><code>segment_list_type</code> <i>type</i></p>
<dd> Select the listing format. </p>
<p> The following values are recognized:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>flat</code></p>
<dd> Generate a flat list for the created segments, one segment per line.</p>
<dt><code>csv, ext</code></p>
<dd> Generate a list for the created segments, one segment per line, each line matching the format (comma-separated values): </p>
<pre>
        &lt;segment_filename&gt;,&lt;segment_start_time&gt;,&lt;segment_end_time&gt;
</pre>
<p> <i>segment_filename</i> is the name of the output file generated by the muxer according to the provided pattern. <font SIZE="-1">CSV</font> escaping (according to <font SIZE="-1">RFC4180</font>) is applied if required. </p>
<p> <i>segment_start_time</i> and <i>segment_end_time</i> specify the segment start and end time expressed in seconds. </p>
<p> A list file with the suffix <tt>&quot;.csv&quot;</tt> or <tt>&quot;.ext&quot;</tt> will auto-select this format. </p>
<p> <code>ext</code> is deprecated in favor or <code>csv</code>.</p>
<dt><code>ffconcat</code></p>
<dd> Generate an ffconcat file for the created segments. The resulting file can be read using the FFmpeg <code>concat</code> demuxer. </p>
<p> A list file with the suffix <tt>&quot;.ffcat&quot;</tt> or <tt>&quot;.ffconcat&quot;</tt> will auto-select this format.</p>
<dt><code>m3u8</code></p>
<dd> Generate an extended M3U8 file, version 3, compliant with &lt;<code><a rel="nofollow" href="http://tools.ietf.org/id/draft-pantos-http-live-streaming">http://tools.ietf.org/id/draft-pantos-http-live-streaming</a></code>&gt;. </p>
<p> A list file with the suffix <tt>&quot;.m3u8&quot;</tt> will auto-select this format.</dl>
</dl>
<dl>
<dt>
<dd>
<p> If not specified the type is guessed from the list file name suffix.</dl>
<dt><code>segment_time</code> <i>time</i></p>
<dd> Set segment duration to <i>time</i>, the value must be a duration specification. Default value is &#8220;2&#8221;. See also the <code>segment_times</code> option. </p>
<p> Note that splitting may not be accurate, unless you force the reference stream key-frames at the given time. See the introductory notice and the examples below.</p>
<dt><code>segment_atclocktime</code> <i>1|0</i></p>
<dd> If set to &#8220;1&#8221; split at regular clock time intervals starting from 00:00 o&#8217;clock. The <i>time</i> value specified in <code>segment_time</code> is used for setting the length of the splitting interval. </p>
<p> For example with <code>segment_time</code> set to &#8220;900&#8221; this makes it possible to create files at 12:00 o&#8217;clock, 12:15, 12:30, etc. </p>
<p> Default value is &#8220;0&#8221;.</p>
<dt><code>segment_clocktime_offset</code> <i>duration</i></p>
<dd> Delay the segment splitting times with the specified duration when using <code>segment_atclocktime</code>. </p>
<p> For example with <code>segment_time</code> set to &#8220;900&#8221; and <code>segment_clocktime_offset</code> set to &#8220;300&#8221; this makes it possible to create files at 12:05, 12:20, 12:35, etc. </p>
<p> Default value is &#8220;0&#8221;.</p>
<dt><code>segment_clocktime_wrap_duration</code> <i>duration</i></p>
<dd> Force the segmenter to only start a new segment if a packet reaches the muxer within the specified duration after the segmenting clock time. This way you can make the segmenter more resilient to backward local time jumps, such as leap seconds or transition to standard time from daylight savings time. </p>
<p> Default is the maximum possible duration which means starting a new segment regardless of the elapsed time since the last clock time.</p>
<dt><code>segment_time_delta</code> <i>delta</i></p>
<dd> Specify the accuracy time when selecting the start time for a segment, expressed as a duration specification. Default value is &#8220;0&#8221;. </p>
<p> When delta is specified a key-frame will start a new segment if its <font SIZE="-1">PTS</font> satisfies the relation: </p>
<pre>
        PTS &gt;= start_time - time_delta
</pre>
<p> This option is useful when splitting video content, which is always split at <font SIZE="-1">GOP</font> boundaries, in case a key frame is found just before the specified split time. </p>
<p> In particular may be used in combination with the <i>ffmpeg</i> option <i>force_key_frames</i>. The key frame times specified by <i>force_key_frames</i> may not be set accurately because of rounding issues, with the consequence that a key frame time may result set just before the specified time. For constant frame rate videos a value of 1/(2*<i>frame_rate</i>) should address the worst case mismatch between the specified time and the time set by <i>force_key_frames</i>.</p>
<dt><code>segment_times</code> <i>times</i></p>
<dd> Specify a list of split points. <i>times</i> contains a list of comma separated duration specifications, in increasing order. See also the <code>segment_time</code> option.</p>
<dt><code>segment_frames</code> <i>frames</i></p>
<dd> Specify a list of split video frame numbers. <i>frames</i> contains a list of comma separated integer numbers, in increasing order. </p>
<p> This option specifies to start a new segment whenever a reference stream key frame is found and the sequential number (starting from 0) of the frame is greater or equal to the next value in the list.</p>
<dt><code>segment_wrap</code> <i>limit</i></p>
<dd> Wrap around segment index once it reaches <i>limit</i>.</p>
<dt><code>segment_start_number</code> <i>number</i></p>
<dd> Set the sequence number of the first segment. Defaults to <tt>0</tt>.</p>
<dt><code>strftime</code> <i>1|0</i></p>
<dd> Use the <tt>&quot;strftime&quot;</tt> function to define the name of the new segments to write. If this is selected, the output segment name must contain a <tt>&quot;strftime&quot;</tt> function template. Default value is <tt>0</tt>.</p>
<dt><code>break_non_keyframes</code> <i>1|0</i></p>
<dd> If enabled, allow segments to start on frames other than keyframes. This improves behavior on some players when the time between keyframes is inconsistent, but may make things worse on others, and can cause some oddities during seeking. Defaults to <tt>0</tt>.</p>
<dt><code>reset_timestamps</code> <i>1|0</i></p>
<dd> Reset timestamps at the beginning of each segment, so that each segment will start with near-zero timestamps. It is meant to ease the playback of the generated segments. May not work with some combinations of muxers/codecs. It is set to <tt>0</tt> by default.</p>
<dt><code>initial_offset</code> <i>offset</i></p>
<dd> Specify timestamp offset to apply to the output packet timestamps. The argument must be a time duration specification, and defaults to 0.</p>
<dt><code>write_empty_segments</code> <i>1|0</i></p>
<dd> If enabled, write an empty segment if there are no packets during the period a segment would usually span. Otherwise, the segment will be filled with the next packet written. Defaults to <tt>0</tt>.</dl>
<p> Make sure to require a closed <font SIZE="-1">GOP</font> when encoding and to set the <font SIZE="-1">GOP</font> size to fit your segment time constraint. </p>
<p> <i>Examples</i></p>
<dl>
<dt>&bull;</p>
<dd> Remux the content of file <i>in.mkv</i> to a list of segments <i>out-000.nut</i>, <i>out-001.nut</i>, etc., and write the list of generated segments to <i>out.list</i>: </p>
<pre>
        ffmpeg -i in.mkv -codec hevc -flags +cgop -g 60 -map 0 -f segment -segment_list out.list out%03d.nut
</pre>
<dt>&bull;</p>
<dd> Segment input and set output format options for the output segments: </p>
<pre>
        ffmpeg -i in.mkv -f segment -segment_time 10 -segment_format_options movflags=+faststart out%03d.mp4
</pre>
<dt>&bull;</p>
<dd> Segment the input file according to the split points specified by the <i>segment_times</i> option: </p>
<pre>
        ffmpeg -i in.mkv -codec copy -map 0 -f segment -segment_list out.csv -segment_times 1,2,3,5,8,13,21 out%03d.nut
</pre>
<dt>&bull;</p>
<dd> Use the <code>ffmpeg</code> <code>force_key_frames</code> option to force key frames in the input at the specified location, together with the segment option <code>segment_time_delta</code> to account for possible roundings operated when setting key frame times. </p>
<pre>
        ffmpeg -i in.mkv -force_key_frames 1,2,3,5,8,13,21 -codec:v mpeg4 -codec:a pcm_s16le -map 0 \
        -f segment -segment_list out.csv -segment_times 1,2,3,5,8,13,21 -segment_time_delta 0.05 out%03d.nut
</pre>
<p> In order to force key frames on the input file, transcoding is required.</p>
<dt>&bull;</p>
<dd> Segment the input file by splitting the input file according to the frame numbers sequence specified with the <code>segment_frames</code> option: </p>
<pre>
        ffmpeg -i in.mkv -codec copy -map 0 -f segment -segment_list out.csv -segment_frames 100,200,300,500,800 out%03d.nut
</pre>
<dt>&bull;</p>
<dd> Convert the <i>in.mkv</i> to <font SIZE="-1">TS</font> segments using the <tt>&quot;libx264&quot;</tt> and <tt>&quot;aac&quot;</tt> encoders: </p>
<pre>
        ffmpeg -i in.mkv -map 0 -codec:v libx264 -codec:a aac -f ssegment -segment_list out.list out%03d.ts
</pre>
<dt>&bull;</p>
<dd> Segment the input file, and create an M3U8 live playlist (can be used as live <font SIZE="-1">HLS</font> source): </p>
<pre>
        ffmpeg -re -i in.mkv -codec copy -map 0 -f segment -segment_list playlist.m3u8 \
        -segment_list_flags +live -segment_time 10 out%03d.mkv
</pre>
</dl>
<h3>smoothstreaming</h3>
<p> Smooth Streaming muxer generates a set of files (Manifest, chunks) suitable for serving with conventional web server.</p>
<dl>
<dt><code>window_size</code></p>
<dd> Specify the number of fragments kept in the manifest. Default 0 (keep all).</p>
<dt><code>extra_window_size</code></p>
<dd> Specify the number of fragments kept outside of the manifest before removing from disk. Default 5.</p>
<dt><code>lookahead_count</code></p>
<dd> Specify the number of lookahead fragments. Default 2.</p>
<dt><code>min_frag_duration</code></p>
<dd> Specify the minimum fragment duration (in microseconds). Default 5000000.</p>
<dt><code>remove_at_exit</code></p>
<dd> Specify whether to remove all fragments when finished. Default 0 (do not remove).</dl>
<h3>streamhash</h3>
<p> Per stream hash testing format. </p>
<p> This muxer computes and prints a cryptographic hash of all the input frames, on a per-stream basis. This can be used for equality checks without having to do a complete binary comparison. </p>
<p> By default audio frames are converted to signed 16-bit raw audio and video frames to raw video before computing the hash, but the output of explicit conversions to other codecs can also be used. Timestamps are ignored. It uses the <font SIZE="-1">SHA-256</font> cryptographic hash function by default, but supports several other algorithms. </p>
<p> The output of the muxer consists of one line per stream of the form: <i>streamindex</i>,<i>streamtype</i>,<i>algo</i>=<i>hash</i>, where <i>streamindex</i> is the index of the mapped stream, <i>streamtype</i> is a single character indicating the type of stream, <i>algo</i> is a short string representing the hash function used, and <i>hash</i> is a hexadecimal number representing the computed hash.</p>
<dl>
<dt><code>hash</code> <i>algorithm</i></p>
<dd> Use the cryptographic hash function specified by the string <i>algorithm</i>. Supported values include <tt>&quot;MD5&quot;</tt>, <tt>&quot;murmur3&quot;</tt>, <tt>&quot;RIPEMD128&quot;</tt>, <tt>&quot;RIPEMD160&quot;</tt>, <tt>&quot;RIPEMD256&quot;</tt>, <tt>&quot;RIPEMD320&quot;</tt>, <tt>&quot;SHA160&quot;</tt>, <tt>&quot;SHA224&quot;</tt>, <tt>&quot;SHA256&quot;</tt> (default), <tt>&quot;SHA512/224&quot;</tt>, <tt>&quot;SHA512/256&quot;</tt>, <tt>&quot;SHA384&quot;</tt>, <tt>&quot;SHA512&quot;</tt>, <tt>&quot;CRC32&quot;</tt> and <tt>&quot;adler32&quot;</tt>.</dl>
<p> <i>Examples</i> </p>
<p> To compute the <font SIZE="-1">SHA-256</font> hash of the input converted to raw audio and video, and store it in the file <i>out.sha256</i>: </p>
<pre>
        ffmpeg -i INPUT -f streamhash out.sha256
</pre>
<p> To print an <font SIZE="-1">MD5</font> hash to stdout use the command: </p>
<pre>
        ffmpeg -i INPUT -f streamhash -hash md5 -
</pre>
<p> See also the <code>hash</code> and <code>framehash</code> muxers.</p>
<h3>fifo</h3>
<p> The fifo pseudo-muxer allows the separation of encoding and muxing by using first-in-first-out queue and running the actual muxer in a separate thread. This is especially useful in combination with the <code>tee</code> muxer and can be used to send data to several destinations with different reliability/writing speed/latency. </p>
<p> <font SIZE="-1">API</font> users should be aware that callback functions (interrupt_callback, io_open and io_close) used within its AVFormatContext must be thread-safe. </p>
<p> The behavior of the fifo muxer if the queue fills up or if the output fails is selectable,</p>
<dl>
<dt>&bull;</p>
<dd> output can be transparently restarted with configurable delay between retries based on real time or time of the processed stream.</p>
<dt>&bull;</p>
<dd> encoding can be blocked during temporary failure, or continue transparently dropping packets in case fifo queue fills up.</p>
<dt><code>fifo_format</code></p>
<dd> Specify the format name. Useful if it cannot be guessed from the output name suffix.</p>
<dt><code>queue_size</code></p>
<dd> Specify size of the queue (number of packets). Default value is 60.</p>
<dt><code>format_opts</code></p>
<dd> Specify format options for the underlying muxer. Muxer options can be specified as a list of <i>key</i>=<i>value</i> pairs separated by &#8216;:&#8217;.</p>
<dt><code>drop_pkts_on_overflow</code> <i>bool</i></p>
<dd> If set to 1 (true), in case the fifo queue fills up, packets will be dropped rather than blocking the encoder. This makes it possible to continue streaming without delaying the input, at the cost of omitting part of the stream. By default this option is set to 0 (false), so in such cases the encoder will be blocked until the muxer processes some of the packets and none of them is lost.</p>
<dt><code>attempt_recovery</code> <i>bool</i></p>
<dd> If failure occurs, attempt to recover the output. This is especially useful when used with network output, since it makes it possible to restart streaming transparently. By default this option is set to 0 (false).</p>
<dt><code>max_recovery_attempts</code></p>
<dd> Sets maximum number of successive unsuccessful recovery attempts after which the output fails permanently. By default this option is set to 0 (unlimited).</p>
<dt><code>recovery_wait_time</code> <i>duration</i></p>
<dd> Waiting time before the next recovery attempt after previous unsuccessful recovery attempt. Default value is 5 seconds.</p>
<dt><code>recovery_wait_streamtime</code> <i>bool</i></p>
<dd> If set to 0 (false), the real time is used when waiting for the recovery attempt (i.e. the recovery will be attempted after at least recovery_wait_time seconds). If set to 1 (true), the time of the processed stream is taken into account instead (i.e. the recovery will be attempted after at least <i>recovery_wait_time</i> seconds of the stream is omitted). By default, this option is set to 0 (false).</p>
<dt><code>recover_any_error</code> <i>bool</i></p>
<dd> If set to 1 (true), recovery will be attempted regardless of type of the error causing the failure. By default this option is set to 0 (false) and in case of certain (usually permanent) errors the recovery is not attempted even when <i>attempt_recovery</i> is set to 1.</p>
<dt><code>restart_with_keyframe</code> <i>bool</i></p>
<dd> Specify whether to wait for the keyframe after recovering from queue overflow or failure. This option is set to 0 (false) by default.</p>
<dt><code>timeshift</code> <i>duration</i></p>
<dd> Buffer the specified amount of packets and delay writing the output. Note that <i>queue_size</i> must be big enough to store the packets for timeshift. At the end of the input the fifo buffer is flushed at realtime speed.</dl>
<p> <i>Examples</i></p>
<dl>
<dt>&bull;</p>
<dd> Stream something to rtmp server, continue processing the stream at real-time rate even in case of temporary failure (network outage) and attempt to recover streaming every second indefinitely. </p>
<pre>
        ffmpeg -re -i ... -c:v libx264 -c:a aac -f fifo -fifo_format flv -map 0:v -map 0:a
          -drop_pkts_on_overflow 1 -attempt_recovery 1 -recovery_wait_time 1 <a href="rtmp://example.com/live/stream_name">rtmp://example.com/live/stream_name</a>
</pre>
</dl>
<h3>tee</h3>
<p> The tee muxer can be used to write the same data to several outputs, such as files or streams. It can be used, for example, to stream a video over a network and save it to disk at the same time. </p>
<p> It is different from specifying several outputs to the <code>ffmpeg</code> command-line tool. With the tee muxer, the audio and video data will be encoded only once. With conventional multiple outputs, multiple encoding operations in parallel are initiated, which can be a very expensive process. The tee muxer is not useful when using the libavformat <font SIZE="-1">API</font> directly because it is then possible to feed the same packets to several muxers directly. </p>
<p> Since the tee muxer does not represent any particular output format, ffmpeg cannot auto-select output streams. So all streams intended for output must be specified using <tt>&quot;-map&quot;</tt>. See the examples below. </p>
<p> Some encoders may need different options depending on the output format; the auto-detection of this can not work with the tee muxer, so they need to be explicitly specified. The main example is the <code>global_header</code> flag. </p>
<p> The slave outputs are specified in the file name given to the muxer, separated by &#8216;|&#8217;. If any of the slave name contains the &#8216;|&#8217; separator, leading or trailing spaces or any special character, those must be escaped (see <code>the &#8220;Quoting and escaping&#8221; section in the <a href="/docs/linux/man/1-ffmpeg-utils/">ffmpeg-utils</a>(1) manual</code>). </p>
<p> <i>Options</i></p>
<dl>
<dt><code>use_fifo</code> <i>bool</i></p>
<dd> If set to 1, slave outputs will be processed in separate threads using the <code>fifo</code> muxer. This allows to compensate for different speed/latency/reliability of outputs and setup transparent recovery. By default this feature is turned off.</p>
<dt><code>fifo_options</code></p>
<dd> Options to pass to fifo pseudo-muxer instances. See <code>fifo</code>.</dl>
<p> Muxer options can be specified for each slave by prepending them as a list of <i>key</i>=<i>value</i> pairs separated by &#8216;:&#8217;, between square brackets. If the options values contain a special character or the &#8216;:&#8217; separator, they must be escaped; note that this is a second level escaping. </p>
<p> The following special options are also recognized:</p>
<dl>
<dt><code>f</code></p>
<dd> Specify the format name. Required if it cannot be guessed from the output <font SIZE="-1">URL.</font></p>
<dt><code>bsfs[/</code><i>spec</i><code>]</code></p>
<dd> Specify a list of bitstream filters to apply to the specified output. </p>
<p> It is possible to specify to which streams a given bitstream filter applies, by appending a stream specifier to the option separated by <tt>&quot;/&quot;</tt>. <i>spec</i> must be a stream specifier (see <code>Format stream specifiers</code>). </p>
<p> If the stream specifier is not specified, the bitstream filters will be applied to all streams in the output. This will cause that output operation to fail if the output contains streams to which the bitstream filter cannot be applied e.g. <tt>&quot;h264_mp4toannexb&quot;</tt> being applied to an output containing an audio stream. </p>
<p> Options for a bitstream filter must be specified in the form of <tt>&quot;opt=value&quot;</tt>. </p>
<p> Several bitstream filters can be specified, separated by &#8220;,&#8221;.</p>
<dt><code>use_fifo</code> <i>bool</i></p>
<dd> This allows to override tee muxer use_fifo option for individual slave muxer.</p>
<dt><code>fifo_options</code></p>
<dd> This allows to override tee muxer fifo_options for individual slave muxer. See <code>fifo</code>.</p>
<dt><code>select</code></p>
<dd> Select the streams that should be mapped to the slave output, specified by a stream specifier. If not specified, this defaults to all the mapped streams. This will cause that output operation to fail if the output format does not accept all mapped streams. </p>
<p> You may use multiple stream specifiers separated by commas (<tt>&quot;,&quot;</tt>) e.g.: <tt>&quot;a:0,v&quot;</tt></p>
<dt><code>onfail</code></p>
<dd> Specify behaviour on output failure. This can be set to either <tt>&quot;abort&quot;</tt> (which is default) or <tt>&quot;ignore&quot;</tt>. <tt>&quot;abort&quot;</tt> will cause whole process to fail in case of failure on this slave output. <tt>&quot;ignore&quot;</tt> will ignore failure on this output, so other outputs will continue without being affected.</dl>
<p> <i>Examples</i></p>
<dl>
<dt>&bull;</p>
<dd> Encode something and both archive it in a WebM file and stream it as MPEG-TS over <font SIZE="-1">UDP:</font> </p>
<pre>
        ffmpeg -i ... -c:v libx264 -c:a mp2 -f tee -map 0:v -map 0:a
          &quot;archive-20121107.mkv|[f=mpegts]<a href="udp://10.0.1.255:1234/">udp://10.0.1.255:1234/</a>&quot;
</pre>
<dt>&bull;</p>
<dd> As above, but continue streaming even if output to local file fails (for example local drive fills up): </p>
<p>ffmpeg &#8211; i&#8230; &#8211; c : v libx264 &#8211; c : a mp2 &#8211; f tee &#8211; map 0 : v &#8211; map 0 : a &#8220;[onfail=ignore]archive-20121107.mkv|[f=mpegts]udp://10.0.1.255:1234/&#8221;</p>
<dt>&bull;</p>
<dd> Use <code>ffmpeg</code> to encode the input, and send the output to three different destinations. The <tt>&quot;dump_extra&quot;</tt> bitstream filter is used to add extradata information to all the output video keyframes packets, as requested by the MPEG-TS format. The select option is applied to <i>out.aac</i> in order to make it contain only audio packets. </p>
<p>ffmpeg &#8211; i&#8230; &#8211; map 0 &#8211; flags + global_header &#8211; c : v libx264 &#8211; c : a aac &#8211; f tee &#8220;[bsfs/v=dump_extra=freq=keyframe]out.ts|[movflags=+faststart]out.mp4|[select=a]out.aac&#8221;</p>
<dt>&bull;</p>
<dd> As above, but select only stream <tt>&quot;a:1&quot;</tt> for the audio output. Note that a second level escaping must be performed, as &#8220;:&#8221; is a special character used to separate options. </p>
<p>ffmpeg &#8211; i&#8230; &#8211; map 0 &#8211; flags + global_header &#8211; c : v libx264 &#8211; c : a aac &#8211; f tee &#8220;[bsfs/v=dump_extra=freq=keyframe]out.ts|[movflags=+faststart]out.mp4|[select=\&#8217;a:1\&#8217;]out.aac&#8221;
</dl>
<h3>webm_dash_manifest</h3>
<p> WebM <font SIZE="-1">DASH</font> Manifest muxer. </p>
<p> This muxer implements the WebM <font SIZE="-1">DASH</font> Manifest specification to generate the <font SIZE="-1">DASH</font> manifest <font SIZE="-1">XML.</font> It also supports manifest generation for <font SIZE="-1">DASH</font> live streams. </p>
<p> For more information see:</p>
<dl>
<dt>&bull;</p>
<dd> WebM <font SIZE="-1">DASH</font> Specification: &lt;<code><a rel="nofollow" href="https://sites.google.com/a/webmproject.org/wiki/adaptive-streaming/webm-dash-specification">https://sites.google.com/a/webmproject.org/wiki/adaptive-streaming/webm-dash-specification</a></code>&gt;</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">ISO DASH</font> Specification: &lt;<code><a rel="nofollow" href="http://standards.iso.org/ittf/PubliclyAvailableStandards/c065274_ISO_IEC_23009-1_2014.zip">http://standards.iso.org/ittf/PubliclyAvailableStandards/c065274_ISO_IEC_23009-1_2014.zip</a></code>&gt;</dl>
<p> <i>Options</i> </p>
<p> This muxer supports the following options:</p>
<dl>
<dt><code>adaptation_sets</code></p>
<dd> This option has the following syntax: &#8220;id=x,streams=a,b,c id=y,streams=d,e&#8221; where x and y are the unique identifiers of the adaptation sets and a,b,c,d and e are the indices of the corresponding audio and video streams. Any number of adaptation sets can be added using this option.</p>
<dt><code>live</code></p>
<dd> Set this to 1 to create a live stream <font SIZE="-1">DASH</font> Manifest. Default: 0.</p>
<dt><code>chunk_start_index</code></p>
<dd> Start index of the first chunk. This will go in the <code>startNumber</code> attribute of the <code>SegmentTemplate</code> element in the manifest. Default: 0.</p>
<dt><code>chunk_duration_ms</code></p>
<dd> Duration of each chunk in milliseconds. This will go in the <code>duration</code> attribute of the <code>SegmentTemplate</code> element in the manifest. Default: 1000.</p>
<dt><code>utc_timing_url</code></p>
<dd> <font SIZE="-1">URL</font> of the page that will return the <font SIZE="-1">UTC</font> timestamp in <font SIZE="-1">ISO</font> format. This will go in the <code>value</code> attribute of the <code>UTCTiming</code> element in the manifest. Default: None.</p>
<dt><code>time_shift_buffer_depth</code></p>
<dd> Smallest time (in seconds) shifting buffer for which any Representation is guaranteed to be available. This will go in the <code>timeShiftBufferDepth</code> attribute of the <font SIZE="-1"><code>MPD</code></font> element. Default: 60.</p>
<dt><code>minimum_update_period</code></p>
<dd> Minimum update period (in seconds) of the manifest. This will go in the <code>minimumUpdatePeriod</code> attribute of the <font SIZE="-1"><code>MPD</code></font> element. Default: 0.</dl>
<p> <i>Example</i> </p>
<pre>
        ffmpeg -f webm_dash_manifest -i video1.webm \
               -f webm_dash_manifest -i video2.webm \
               -f webm_dash_manifest -i audio1.webm \
               -f webm_dash_manifest -i audio2.webm \
               -map 0 -map 1 -map 2 -map 3 \
               -c copy \
               -f webm_dash_manifest \
               -adaptation_sets &quot;id=0,streams=0,1 id=1,streams=2,3&quot; \
               manifest.xml
</pre>
<h3>webm_chunk</h3>
<p> WebM Live Chunk Muxer. </p>
<p> This muxer writes out WebM headers and chunks as separate files which can be consumed by clients that support WebM Live streams via <font SIZE="-1">DASH.</font> </p>
<p> <i>Options</i> </p>
<p> This muxer supports the following options:</p>
<dl>
<dt><code>chunk_start_index</code></p>
<dd> Index of the first chunk (defaults to 0).</p>
<dt><code>header</code></p>
<dd> Filename of the header where the initialization data will be written.</p>
<dt><code>audio_chunk_duration</code></p>
<dd> Duration of each audio chunk in milliseconds (defaults to 5000).</dl>
<p> <i>Example</i> </p>
<pre>
        ffmpeg -f v4l2 -i /dev/video0 \
               -f alsa -i hw:0 \
               -map 0:0 \
               -c:v libvpx-vp9 \
               -s 640x360 -keyint_min 30 -g 30 \
               -f webm_chunk \
               -header webm_live_video_360.hdr \
               -chunk_start_index 1 \
               webm_live_video_360_%d.chk \
               -map 1:0 \
               -c:a libvorbis \
               -b:a 128k \
               -f webm_chunk \
               -header webm_live_audio_128.hdr \
               -chunk_start_index 1 \
               -audio_chunk_duration 1000 \
               webm_live_audio_128_%d.chk
</pre>
<h2>METADATA</h2>
<p> FFmpeg is able to dump metadata from media files into a simple UTF-8-encoded INI-like text file and then load it back using the metadata muxer/demuxer. </p>
<p> The file format is as follows:</p>
<dl>
<dt>1.</p>
<dd> A file consists of a header and a number of metadata tags divided into sections, each on its own line.</p>
<dt>2.</p>
<dd> The header is a <code>;FFMETADATA</code> string, followed by a version number (now 1).</p>
<dt>3.</p>
<dd> Metadata tags are of the form <code>key=value</code></p>
<dt>4.</p>
<dd> Immediately after header follows global metadata</p>
<dt>5.</p>
<dd> After global metadata there may be sections with per-stream/per-chapter metadata.</p>
<dt>6.</p>
<dd> A section starts with the section name in uppercase (i.e. <font SIZE="-1">STREAM</font> or <font SIZE="-1">CHAPTER</font>) in brackets (<code>[</code>, <code>]</code>) and ends with next section or end of file.</p>
<dt>7.</p>
<dd> At the beginning of a chapter section there may be an optional timebase to be used for start/end values. It must be in form <code>TIMEBASE=</code><i>num</i><code>/</code><i>den</i>, where <i>num</i> and <i>den</i> are integers. If the timebase is missing then start/end times are assumed to be in nanoseconds. </p>
<p> Next a chapter section must contain chapter start and end times in form <code>START=</code><i>num</i>, <code>END=</code><i>num</i>, where <i>num</i> is a positive integer.</p>
<dt>8.</p>
<dd> Empty lines and lines starting with <code>;</code> or <code>#</code> are ignored.</p>
<dt>9.</p>
<dd> Metadata keys or values containing special characters (<code>=</code>, <code>;</code>, <code>#</code>, <code>\</code> and a newline) must be escaped with a backslash <code>\</code>.</p>
<dt>10.</p>
<dd> Note that whitespace in metadata (e.g. <code>foo = bar</code>) is considered to be a part of the tag (in the example above key is <code>foo</code> , value is<br />
&nbsp;<code>bar</code>).</dl>
<p> A ffmetadata file might look like this: </p>
<pre><code>
;
FFMETADATA1
title = bike\shed;
this is a comment
    artist = FFmpeg troll team

        [CHAPTER] TIMEBASE = 1 / 1000 START = 0
#chapter ends at 0 : 01 : 00
    END = 60000 title = chapter \#1
        [STREAM] title = multi
            line
</code></pre>
<p> By using the ffmetadata muxer and demuxer it is possible to extract metadata from an input file to an ffmetadata file, and then transcode the file into an output file with the edited ffmetadata file. </p>
<p> Extracting an ffmetadata file with <i>ffmpeg</i> goes as follows: </p>
<pre>
        ffmpeg -i INPUT -f ffmetadata FFMETADATAFILE
</pre>
<p> Reinserting edited metadata information from the <font SIZE="-1">FFMETADATAFILE</font> file can be done as: </p>
<pre>
        ffmpeg -i INPUT -i FFMETADATAFILE -map_metadata 1 -codec copy OUTPUT
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ffmpeg/">ffmpeg</a></code>(1), <code><a href="/docs/linux/man/1-ffplay/">ffplay</a></code>(1), <code><a href="/docs/linux/man/1-ffprobe/">ffprobe</a></code>(1), <code><a href="/docs/linux/man/3-libavformat/">libavformat</a></code>(3)</p>
<h2>AUTHORS</h2>
<p> The FFmpeg developers. </p>
<p> For details about the authorship, see the Git history of the project (<a href="git://source.ffmpeg.org/ffmpeg">git://source.ffmpeg.org/ffmpeg</a>), e.g. by typing the command <code>git log</code> in the FFmpeg source directory, or browsing the online repository at &lt;<code><a rel="nofollow" href="http://source.ffmpeg.org">http://source.ffmpeg.org</a></code>&gt;. </p>
<p> Maintainers for the specific components are listed in the file <i></i><font SIZE="-1"><i>MAINTAINERS</i></font><i></i> in the source code tree. </p>
<h2>Index</h2>
