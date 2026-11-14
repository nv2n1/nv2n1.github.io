---
title: "ffmpeg(1)"
name: "ffmpeg"
section: "1"
letter: "f"
url: "/docs/linux/man/1-ffmpeg/"
description: "ffmpeg – ffmpeg video converter"
---

<h2 class="name">NAME</h2>
<p> ffmpeg &#8211; ffmpeg video converter </p>
<h2>SYNOPSIS</h2>
<p> ffmpeg [<i>global_options</i>] {[<i>input_file_options</i>] -i <i>input_url</i>} &#8230; {[<i>output_file_options</i>] <i>output_url</i>} &#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>ffmpeg</code> is a very fast video and audio converter that can also grab from a live audio/video source. It can also convert between arbitrary sample rates and resize video on the fly with a high quality polyphase filter. </p>
<p> <code>ffmpeg</code> reads from an arbitrary number of input &#8220;files&#8221; (which can be regular files, pipes, network streams, grabbing devices, etc.), specified by the <tt>&quot;-i&quot;</tt> option, and writes to an arbitrary number of output &#8220;files&#8221;, which are specified by a plain output url. Anything found on the command line which cannot be interpreted as an option is considered to be an output url. </p>
<p> Each input or output url can, in principle, contain any number of streams of different types (video/audio/subtitle/attachment/data). The allowed number and/or types of streams may be limited by the container format. Selecting which streams from which inputs will go into which output is either done automatically or with the <tt>&quot;-map&quot;</tt> option (see the Stream selection chapter). </p>
<p> To refer to input files in options, you must use their indices (0-based). E.g. the first input file is <tt>0</tt>, the second is <tt>1</tt>, etc. Similarly, streams within a file are referred to by their indices. E.g. <tt>&quot;2:3&quot;</tt> refers to the fourth stream in the third input file. Also see the Stream specifiers chapter. </p>
<p> As a general rule, options are applied to the next specified file. Therefore, order is important, and you can have the same option on the command line multiple times. Each occurrence is then applied to the next input or output file. Exceptions from this rule are the global options (e.g. verbosity level), which should be specified first. </p>
<p> Do not mix input and output files &#8212; first specify all input files, then all output files. Also do not mix options which belong to different files. All options apply <font SIZE="-1">ONLY</font> to the next input or output file and are reset between files.</p>
<dl>
<dt>&bull;</p>
<dd> To set the video bitrate of the output file to 64 kbit/s: </p>
<pre>
        ffmpeg -i input.avi -b:v 64k -bufsize 64k output.avi
</pre>
<dt>&bull;</p>
<dd> To force the frame rate of the output file to 24 fps: </p>
<pre>
        ffmpeg -i input.avi -r 24 output.avi
</pre>
<dt>&bull;</p>
<dd> To force the frame rate of the input file (valid for raw formats only) to 1 fps and the frame rate of the output file to 24 fps: </p>
<pre>
        ffmpeg -r 1 -i input.m2v -r 24 output.avi
</pre>
</dl>
<p> The format option may be needed for raw input files.</p>
<h2>DETAILED DESCRIPTION</h2>
<p> The transcoding process in <code>ffmpeg</code> for each output can be described by the following diagram: </p>
<pre><code>
_______ ______________ | | | |
    | input | demuxer | encoded data | decoder | file | -- -- -- ---&gt;| packets | -- -- -+ | _______ | | ______________ | |
    v
        _________ |
    |
    | decoded |
    | frames |
    | _________ |
    ________ ______________ |
    | | | | |
    | output | &lt; -- -- -- -- | encoded data | &lt; -- --+ | file | muxer | packets | encoder | ________ | | ______________ |
</code></pre>
<p> <code>ffmpeg</code> calls the libavformat library (containing demuxers) to read input files and get packets containing encoded data from them. When there are multiple input files, <code>ffmpeg</code> tries to keep them synchronized by tracking lowest timestamp on any active input stream. </p>
<p> Encoded packets are then passed to the decoder (unless streamcopy is selected for the stream, see further for a description). The decoder produces uncompressed frames (raw video/PCM audio/&#8230;) which can be processed further by filtering (see next section). After filtering, the frames are passed to the encoder, which encodes them and outputs encoded packets. Finally those are passed to the muxer, which writes the encoded packets to the output file.</p>
<h3>Filtering</h3>
<p> Before encoding, <code>ffmpeg</code> can process raw audio and video frames using filters from the libavfilter library. Several chained filters form a filter graph. <code>ffmpeg</code> distinguishes between two types of filtergraphs: simple and complex. </p>
<p> <i>Simple filtergraphs</i> </p>
<p> Simple filtergraphs are those that have exactly one input and output, both of the same type. In the above diagram they can be represented by simply inserting an additional step between decoding and encoding: </p>
<pre>
         _________                        ______________
        |         |                      |              |
        | decoded |                      | encoded data |
        | frames  |\                   _ | packets      |
        |_________| \                  /||______________|
                     \   __________   /
          simple     _\||          | /  encoder
          filtergraph   | filtered |/
                        | frames   |
                        |__________|
</pre>
<p> Simple filtergraphs are configured with the per-stream <code>-filter</code> option (with <code>-vf</code> and <code>-af</code> aliases for video and audio respectively). A simple filtergraph for video can look for example like this: </p>
<p>_______ _____________ _______ ________ | | | | | | | |<br />
    | input | &#8212;&gt;| deinterlace | &#8212;&gt;| scale | &#8212;&gt;| output |<br />
    | _______ | | _____________ | | _______ | | ________ |</p>
<p> Note that some filters change frame properties but not frame contents. E.g. the <tt>&quot;fps&quot;</tt> filter in the example above changes number of frames, but does not touch the frame contents. Another example is the <tt>&quot;setpts&quot;</tt> filter, which only sets timestamps and otherwise passes the frames unchanged. </p>
<p> <i>Complex filtergraphs</i> </p>
<p> Complex filtergraphs are those which cannot be described as simply a linear processing chain applied to one stream. This is the case, for example, when the graph has more than one input and/or output, or when output stream type is different from input. They can be represented with the following diagram: </p>
<pre>
         _________
        |         |
        | input 0 |\                    __________
        |_________| \                  |          |
                     \   _________    /| output 0 |
                      \ |         |  / |__________|
         _________     \| complex | /
        |         |     |         |/
        | input 1 |----&gt;| filter  |\
        |_________|     |         | \   __________
                       /| graph   |  \ |          |
                      / |         |   \| output 1 |
         _________   /  |_________|    |__________|
        |         | /
        | input 2 |/
        |_________|
</pre>
<p> Complex filtergraphs are configured with the <code>-filter_complex</code> option. Note that this option is global, since a complex filtergraph, by its nature, cannot be unambiguously associated with a single stream or file. </p>
<p> The <code>-lavfi</code> option is equivalent to <code>-filter_complex</code>. </p>
<p> A trivial example of a complex filtergraph is the <tt>&quot;overlay&quot;</tt> filter, which has two video inputs and one video output, containing one video overlaid on top of the other. Its audio counterpart is the <tt>&quot;amix&quot;</tt> filter.</p>
<h3>Stream copy</h3>
<p> Stream copy is a mode selected by supplying the <tt>&quot;copy&quot;</tt> parameter to the <code>-codec</code> option. It makes <code>ffmpeg</code> omit the decoding and encoding step for the specified stream, so it does only demuxing and muxing. It is useful for changing the container format or modifying container-level metadata. The diagram above will, in this case, simplify to this: </p>
<p>_______ ______________ ________ | | | | | |<br />
    | input | demuxer | encoded data | muxer | output |<br />
    | file | &#8212; &#8212; &#8212; &#8212;&gt;| packets | &#8212; &#8212; &#8212;&gt;| file |<br />
    | _______ | | ______________ | | ________ |</p>
<p> Since there is no decoding or encoding, it is very fast and there is no quality loss. However, it might not work in some cases because of many factors. Applying filters is obviously also impossible, since filters work on uncompressed data.</p>
<h2>STREAM SELECTION</h2>
<p> <code>ffmpeg</code> provides the <tt>&quot;-map&quot;</tt> option for manual control of stream selection in each output file. Users can skip <tt>&quot;-map&quot;</tt> and let ffmpeg perform automatic stream selection as described below. The <tt>&quot;-vn / -an / -sn / -dn&quot;</tt> options can be used to skip inclusion of video, audio, subtitle and data streams respectively, whether manually mapped or automatically selected, except for those streams which are outputs of complex filtergraphs.</p>
<h3>Description</h3>
<p> The sub-sections that follow describe the various rules that are involved in stream selection. The examples that follow next show how these rules are applied in practice. </p>
<p> While every effort is made to accurately reflect the behavior of the program, FFmpeg is under continuous development and the code may have changed since the time of this writing. </p>
<p> <i>Automatic stream selection</i> </p>
<p> In the absence of any map options for a particular output file, ffmpeg inspects the output format to check which type of streams can be included in it, viz. video, audio and/or subtitles. For each acceptable stream type, ffmpeg will pick one stream, when available, from among all the inputs. </p>
<p> It will select that stream based upon the following criteria:</p>
<dl>
<dt>&bull;</p>
<dd> for video, it is the stream with the highest resolution,</p>
<dt>&bull;</p>
<dd> for audio, it is the stream with the most channels,</p>
<dt>&bull;</p>
<dd> for subtitles, it is the first subtitle stream found but there&#8217;s a caveat. The output format&#8217;s default subtitle encoder can be either text-based or image-based, and only a subtitle stream of the same type will be chosen.</dl>
<p> In the case where several streams of the same type rate equally, the stream with the lowest index is chosen. </p>
<p> Data or attachment streams are not automatically selected and can only be included using <tt>&quot;-map&quot;</tt>. </p>
<p> <i>Manual stream selection</i> </p>
<p> When <tt>&quot;-map&quot;</tt> is used, only user-mapped streams are included in that output file, with one possible exception for filtergraph outputs described below. </p>
<p> <i>Complex filtergraphs</i> </p>
<p> If there are any complex filtergraph output streams with unlabeled pads, they will be added to the first output file. This will lead to a fatal error if the stream type is not supported by the output format. In the absence of the map option, the inclusion of these streams leads to the automatic stream selection of their types being skipped. If map options are present, these filtergraph streams are included in addition to the mapped streams. </p>
<p> Complex filtergraph output streams with labeled pads must be mapped once and exactly once. </p>
<p> <i>Stream handling</i> </p>
<p> Stream handling is independent of stream selection, with an exception for subtitles described below. Stream handling is set via the <tt>&quot;-codec&quot;</tt> option addressed to streams within a specific <i>output</i> file. In particular, codec options are applied by ffmpeg after the stream selection process and thus do not influence the latter. If no <tt>&quot;-codec&quot;</tt> option is specified for a stream type, ffmpeg will select the default encoder registered by the output file muxer. </p>
<p> An exception exists for subtitles. If a subtitle encoder is specified for an output file, the first subtitle stream found of any type, text or image, will be included. ffmpeg does not validate if the specified encoder can convert the selected stream or if the converted stream is acceptable within the output format. This applies generally as well: when the user sets an encoder manually, the stream selection process cannot check if the encoded stream can be muxed into the output file. If it cannot, ffmpeg will abort and <i>all</i> output files will fail to be processed.</p>
<h3>Examples</h3>
<p> The following examples illustrate the behavior, quirks and limitations of ffmpeg&#8217;s stream selection methods. </p>
<p> They assume the following three input files. </p>
<pre>
        input file 'A.avi'
              stream 0: video 640x360
              stream 1: audio 2 channels
        
        input file 'B.mp4'
              stream 0: video 1920x1080
              stream 1: audio 2 channels
              stream 2: subtitles (text)
              stream 3: audio 5.1 channels
              stream 4: subtitles (text)
        
        input file 'C.mkv'
              stream 0: video 1280x720
              stream 1: audio 2 channels
              stream 2: subtitles (image)
</pre>
<p> Example: automatic stream selection </p>
<pre>
        ffmpeg -i A.avi -i B.mp4 out1.mkv out2.wav -map 1:a -c:a copy out3.mov
</pre>
<p> There are three output files specified, and for the first two, no <tt>&quot;-map&quot;</tt> options are set, so ffmpeg will select streams for these two files automatically. </p>
<p> <i>out1.mkv</i> is a Matroska container file and accepts video, audio and subtitle streams, so ffmpeg will try to select one of each type.For video, it will select <tt>&quot;stream 0&quot;</tt> from <i>B.mp4</i>, which has the highest resolution among all the input video streams.For audio, it will select <tt>&quot;stream 3&quot;</tt> from <i>B.mp4</i>, since it has the greatest number of channels.For subtitles, it will select <tt>&quot;stream 2&quot;</tt> from <i>B.mp4</i>, which is the first subtitle stream from among <i>A.avi</i> and <i>B.mp4</i>. </p>
<p> <i>out2.wav</i> accepts only audio streams, so only <tt>&quot;stream 3&quot;</tt> from <i>B.mp4</i> is selected. </p>
<p> For <i>out3.mov</i>, since a <tt>&quot;-map&quot;</tt> option is set, no automatic stream selection will occur. The <tt>&quot;-map 1:a&quot;</tt> option will select all audio streams from the second input <i>B.mp4</i>. No other streams will be included in this output file. </p>
<p> For the first two outputs, all included streams will be transcoded. The encoders chosen will be the default ones registered by each output format, which may not match the codec of the selected input streams. </p>
<p> For the third output, codec option for audio streams has been set to <tt>&quot;copy&quot;</tt>, so no decoding-filtering-encoding operations will occur, or <i>can</i> occur. Packets of selected streams shall be conveyed from the input file and muxed within the output file. </p>
<p> Example: automatic subtitles selection </p>
<pre>
        ffmpeg -i C.mkv out1.mkv -c:s dvdsub -an out2.mkv
</pre>
<p> Although <i>out1.mkv</i> is a Matroska container file which accepts subtitle streams, only a video and audio stream shall be selected. The subtitle stream of <i>C.mkv</i> is image-based and the default subtitle encoder of the Matroska muxer is text-based, so a transcode operation for the subtitles is expected to fail and hence the stream isn&#8217;t selected. However, in <i>out2.mkv</i>, a subtitle encoder is specified in the command and so, the subtitle stream is selected, in addition to the video stream. The presence of <tt>&quot;-an&quot;</tt> disables audio stream selection for <i>out2.mkv</i>. </p>
<p> Example: unlabeled filtergraph outputs </p>
<pre>
        ffmpeg -i A.avi -i C.mkv -i B.mp4 -filter_complex &quot;overlay&quot; out1.mp4 out2.srt
</pre>
<p> A filtergraph is setup here using the <tt>&quot;-filter_complex&quot;</tt> option and consists of a single video filter. The <tt>&quot;overlay&quot;</tt> filter requires exactly two video inputs, but none are specified, so the first two available video streams are used, those of <i>A.avi</i> and <i>C.mkv</i>. The output pad of the filter has no label and so is sent to the first output file <i>out1.mp4</i>. Due to this, automatic selection of the video stream is skipped, which would have selected the stream in <i>B.mp4</i>. The audio stream with most channels viz. <tt>&quot;stream 3&quot;</tt> in <i>B.mp4</i>, is chosen automatically. No subtitle stream is chosen however, since the <font SIZE="-1">MP4</font> format has no default subtitle encoder registered, and the user hasn&#8217;t specified a subtitle encoder. </p>
<p> The 2nd output file, <i>out2.srt</i>, only accepts text-based subtitle streams. So, even though the first subtitle stream available belongs to <i>C.mkv</i>, it is image-based and hence skipped. The selected stream, <tt>&quot;stream 2&quot;</tt> in <i>B.mp4</i>, is the first text-based subtitle stream. </p>
<p> Example: labeled filtergraph outputs </p>
<p>ffmpeg &#8211; i A.avi &#8211; i B.mp4 &#8211; i C.mkv &#8211; filter_complex &#8220;[1:v]hue=s=0[outv];overlay;aresample&#8221; &#8211; map &#8216;[outv]&#8217; &#8211; an out1.mp4 out2.mkv &#8211; map &#8216;[outv]&#8217; &#8211; map 1 : a : 0 out3.mkv</p>
<p> The above command will fail, as the output pad labelled <tt>&quot;[outv]&quot;</tt> has been mapped twice. None of the output files shall be processed. </p>
<p>ffmpeg &#8211; i A.avi &#8211; i B.mp4 &#8211; i C.mkv &#8211; filter_complex &#8220;[1:v]hue=s=0[outv];overlay;aresample&#8221; &#8211; an out1.mp4 out2.mkv &#8211; map 1 : a : 0 out3.mkv</p>
<p> This command above will also fail as the hue filter output has a label, <tt>&quot;[outv]&quot;</tt>, and hasn&#8217;t been mapped anywhere. </p>
<p> The command should be modified as follows, </p>
<p>ffmpeg &#8211; i A.avi &#8211; i B.mp4 &#8211; i C.mkv &#8211; filter_complex &#8220;[1:v]hue=s=0,split=2[outv1][outv2];overlay;aresample&#8221; &#8211; map &#8216;[outv1]&#8217; &#8211; an out1.mp4 out2.mkv &#8211; map &#8216;[outv2]&#8217; &#8211; map 1 : a : 0 out3.mkv</p>
<p> The video stream from <i>B.mp4</i> is sent to the hue filter, whose output is cloned once using the split filter, and both outputs labelled. Then a copy each is mapped to the first and third output files. </p>
<p> The overlay filter, requiring two video inputs, uses the first two unused video streams. Those are the streams from <i>A.avi</i> and <i>C.mkv</i>. The overlay output isn&#8217;t labelled, so it is sent to the first output file <i>out1.mp4</i>, regardless of the presence of the <tt>&quot;-map&quot;</tt> option. </p>
<p> The aresample filter is sent the first unused audio stream, that of <i>A.avi</i>. Since this filter output is also unlabelled, it too is mapped to the first output file. The presence of <tt>&quot;-an&quot;</tt> only suppresses automatic or manual stream selection of audio streams, not outputs sent from filtergraphs. Both these mapped streams shall be ordered before the mapped stream in <i>out1.mp4</i>. </p>
<p> The video, audio and subtitle streams mapped to <tt>&quot;out2.mkv&quot;</tt> are entirely determined by automatic stream selection. </p>
<p> <i>out3.mkv</i> consists of the cloned video output from the hue filter and the first audio stream from <i>B.mp4</i>.</p>
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
<dt><code>-f</code> <i>fmt</i> <code>(</code><i>input/output</i><code>)</code></p>
<dd> Force input or output file format. The format is normally auto detected for input files and guessed from the file extension for output files, so this option is not needed in most cases.</p>
<dt><code>-i</code> <i>url</i> <code>(</code><i>input</i><code>)</code></p>
<dd> input file url</p>
<dt><code>-y (</code><i>global</i><code>)</code></p>
<dd> Overwrite output files without asking.</p>
<dt><code>-n (</code><i>global</i><code>)</code></p>
<dd> Do not overwrite output files, and exit immediately if a specified output file already exists.</p>
<dt><code>-stream_loop</code> <i>number</i> <code>(</code><i>input</i><code>)</code></p>
<dd> Set number of times input stream shall be looped. Loop 0 means no loop, loop -1 means infinite loop.</p>
<dt><code>-c[:</code><i>stream_specifier</i><code>]</code> <i>codec</i> <code>(</code><i>input/output,per-stream</i><code>)</code></p>
<dd>
<dt><code>-codec[:</code><i>stream_specifier</i><code>]</code> <i>codec</i> <code>(</code><i>input/output,per-stream</i><code>)</code></p>
<dd> Select an encoder (when used before an output file) or a decoder (when used before an input file) for one or more streams. <i>codec</i> is the name of a decoder/encoder or a special value <tt>&quot;copy&quot;</tt> (output only) to indicate that the stream is not to be re-encoded. </p>
<p> For example </p>
<pre>
        ffmpeg -i INPUT -map 0 -c:v libx264 -c:a copy OUTPUT
</pre>
<p> encodes all video streams with libx264 and copies all audio streams. </p>
<p> For each stream, the last matching <tt>&quot;c&quot;</tt> option is applied, so </p>
<pre>
        ffmpeg -i INPUT -map 0 -c copy -c:v:1 libx264 -c:a:137 libvorbis OUTPUT
</pre>
<p> will copy all the streams except the second video, which will be encoded with libx264, and the 138th audio, which will be encoded with libvorbis.</p>
<dt><code>-t</code> <i>duration</i> <code>(</code><i>input/output</i><code>)</code></p>
<dd> When used as an input option (before <tt>&quot;-i&quot;</tt>), limit the <i>duration</i> of data read from the input file. </p>
<p> When used as an output option (before an output url), stop writing the output after its duration reaches <i>duration</i>. </p>
<p> <i>duration</i> must be a time duration specification, see <code>the Time duration section in the <a href="/docs/linux/man/1-ffmpeg-utils/">ffmpeg-utils</a>(1) manual</code>. </p>
<p> -to and -t are mutually exclusive and -t has priority.</p>
<dt><code>-to</code> <i>position</i> <code>(</code><i>input/output</i><code>)</code></p>
<dd> Stop writing the output or reading the input at <i>position</i>. <i>position</i> must be a time duration specification, see <code>the Time duration section in the <a href="/docs/linux/man/1-ffmpeg-utils/">ffmpeg-utils</a>(1) manual</code>. </p>
<p> -to and -t are mutually exclusive and -t has priority.</p>
<dt><code>-fs</code> <i>limit_size</i> <code>(</code><i>output</i><code>)</code></p>
<dd> Set the file size limit, expressed in bytes. No further chunk of bytes is written after the limit is exceeded. The size of the output file is slightly more than the requested file size.</p>
<dt><code>-ss</code> <i>position</i> <code>(</code><i>input/output</i><code>)</code></p>
<dd> When used as an input option (before <tt>&quot;-i&quot;</tt>), seeks in this input file to <i>position</i>. Note that in most formats it is not possible to seek exactly, so <code>ffmpeg</code> will seek to the closest seek point before <i>position</i>. When transcoding and <code>-accurate_seek</code> is enabled (the default), this extra segment between the seek point and <i>position</i> will be decoded and discarded. When doing stream copy or when <code>-noaccurate_seek</code> is used, it will be preserved. </p>
<p> When used as an output option (before an output url), decodes but discards input until the timestamps reach <i>position</i>. </p>
<p> <i>position</i> must be a time duration specification, see <code>the Time duration section in the <a href="/docs/linux/man/1-ffmpeg-utils/">ffmpeg-utils</a>(1) manual</code>.</p>
<dt><code>-sseof</code> <i>position</i> <code>(</code><i>input</i><code>)</code></p>
<dd> Like the <tt>&quot;-ss&quot;</tt> option but relative to the &#8220;end of file&#8221;. That is negative values are earlier in the file, 0 is at <font SIZE="-1">EOF.</font></p>
<dt><code>-itsoffset</code> <i>offset</i> <code>(</code><i>input</i><code>)</code></p>
<dd> Set the input time offset. </p>
<p> <i>offset</i> must be a time duration specification, see <code>the Time duration section in the <a href="/docs/linux/man/1-ffmpeg-utils/">ffmpeg-utils</a>(1) manual</code>. </p>
<p> The offset is added to the timestamps of the input files. Specifying a positive offset means that the corresponding streams are delayed by the time duration specified in <i>offset</i>.</p>
<dt><code>-itsscale</code> <i>scale</i> <code>(</code><i>input,per-stream</i><code>)</code></p>
<dd> Rescale input timestamps. <i>scale</i> should be a floating point number.</p>
<dt><code>-timestamp</code> <i>date</i> <code>(</code><i>output</i><code>)</code></p>
<dd> Set the recording timestamp in the container. </p>
<p> <i>date</i> must be a date specification, see <code>the Date section in the <a href="/docs/linux/man/1-ffmpeg-utils/">ffmpeg-utils</a>(1) manual</code>.</p>
<dt><code>-metadata[:metadata_specifier]</code> <i>key</i><code>=</code><i>value</i> <code>(</code><i>output,per-metadata</i><code>)</code></p>
<dd> Set a metadata key/value pair. </p>
<p> An optional <i>metadata_specifier</i> may be given to set metadata on streams, chapters or programs. See <tt>&quot;-map_metadata&quot;</tt> documentation for details. </p>
<p> This option overrides metadata set with <tt>&quot;-map_metadata&quot;</tt>. It is also possible to delete metadata by using an empty value. </p>
<p> For example, for setting the title in the output file: </p>
<pre>
        ffmpeg -i in.avi -metadata title=&quot;my title&quot; out.flv
</pre>
<p> To set the language of the first audio stream: </p>
<pre>
        ffmpeg -i INPUT -metadata:s:a:0 language=eng OUTPUT
</pre>
<dt><code>-disposition[:stream_specifier]</code> <i>value</i> <code>(</code><i>output,per-stream</i><code>)</code></p>
<dd> Sets the disposition for a stream. </p>
<p> This option overrides the disposition copied from the input stream. It is also possible to delete the disposition by setting it to 0. </p>
<p> The following dispositions are recognized:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>default</code></p>
<dd>
<dt><code>dub</code></p>
<dd>
<dt><code>original</code></p>
<dd>
<dt><code>comment</code></p>
<dd>
<dt><code>lyrics</code></p>
<dd>
<dt><code>karaoke</code></p>
<dd>
<dt><code>forced</code></p>
<dd>
<dt><code>hearing_impaired</code></p>
<dd>
<dt><code>visual_impaired</code></p>
<dd>
<dt><code>clean_effects</code></p>
<dd>
<dt><code>attached_pic</code></p>
<dd>
<dt><code>captions</code></p>
<dd>
<dt><code>descriptions</code></p>
<dd>
<dt><code>dependent</code></p>
<dd>
<dt><code>metadata</code></p>
<dd></dl>
</dl>
<dl>
<dt>
<dd>
<p> For example, to make the second audio stream the default stream: </p>
<pre>
        ffmpeg -i in.mkv -c copy -disposition:a:1 default out.mkv
</pre>
<p> To make the second subtitle stream the default stream and remove the default disposition from the first subtitle stream: </p>
<pre>
        ffmpeg -i in.mkv -c copy -disposition:s:0 0 -disposition:s:1 default out.mkv
</pre>
<p> To add an embedded cover/thumbnail: </p>
<pre>
        ffmpeg -i in.mp4 -i IMAGE -map 0 -map 1 -c copy -c:v:1 png -disposition:v:1 attached_pic out.mp4
</pre>
<p> Not all muxers support embedded thumbnails, and those who do, only support a few formats, like <font SIZE="-1">JPEG</font> or <font SIZE="-1">PNG.</font></dl>
<dt><code>-program [title=</code><i>title</i><code>:][program_num=</code><i>program_num</i><code>:]st=</code><i>stream</i><code>[:st=</code><i>stream</i><code>&#8230;] (</code><i>output</i><code>)</code></p>
<dd> Creates a program with the specified <i>title</i>, <i>program_num</i> and adds the specified <i>stream</i>(s) to it.</p>
<dt><code>-target</code> <i>type</i> <code>(</code><i>output</i><code>)</code></p>
<dd> Specify target file type (<tt>&quot;vcd&quot;</tt>, <tt>&quot;svcd&quot;</tt>, <tt>&quot;dvd&quot;</tt>, <tt>&quot;dv&quot;</tt>, <tt>&quot;dv50&quot;</tt>). <i>type</i> may be prefixed with <tt>&quot;pal-&quot;</tt>, <tt>&quot;ntsc-&quot;</tt> or <tt>&quot;film-&quot;</tt> to use the corresponding standard. All the format options (bitrate, codecs, buffer sizes) are then set automatically. You can just type: </p>
<pre>
        ffmpeg -i myfile.avi -target vcd /tmp/vcd.mpg
</pre>
<p> Nevertheless you can specify additional options as long as you know they do not conflict with the standard, as in: </p>
<pre>
        ffmpeg -i myfile.avi -target vcd -bf 2 /tmp/vcd.mpg
</pre>
<p> The parameters set for each target are as follows. </p>
<p> <font SIZE="-1"><code>VCD</code></font> </p>
<pre>
        &lt;pal&gt;:
        -f vcd -muxrate 1411200 -muxpreload 0.44 -packetsize 2324
        -s 352x288 -r 25
        -codec:v mpeg1video -g 15 -b:v 1150k -maxrate:v 1150v -minrate:v 1150k -bufsize:v 327680
        -ar 44100 -ac 2
        -codec:a mp2 -b:a 224k
        
        &lt;ntsc&gt;:
        -f vcd -muxrate 1411200 -muxpreload 0.44 -packetsize 2324
        -s 352x240 -r 30000/1001
        -codec:v mpeg1video -g 18 -b:v 1150k -maxrate:v 1150v -minrate:v 1150k -bufsize:v 327680
        -ar 44100 -ac 2
        -codec:a mp2 -b:a 224k
        
        &lt;film&gt;:
        -f vcd -muxrate 1411200 -muxpreload 0.44 -packetsize 2324
        -s 352x240 -r 24000/1001
        -codec:v mpeg1video -g 18 -b:v 1150k -maxrate:v 1150v -minrate:v 1150k -bufsize:v 327680
        -ar 44100 -ac 2
        -codec:a mp2 -b:a 224k
</pre>
<p> <font SIZE="-1"><code>SVCD</code></font> </p>
<pre>
        &lt;pal&gt;:
        -f svcd -packetsize 2324
        -s 480x576 -pix_fmt yuv420p -r 25
        -codec:v mpeg2video -g 15 -b:v 2040k -maxrate:v 2516k -minrate:v 0 -bufsize:v 1835008 -scan_offset 1
        -ar 44100
        -codec:a mp2 -b:a 224k
        
        &lt;ntsc&gt;:
        -f svcd -packetsize 2324
        -s 480x480 -pix_fmt yuv420p -r 30000/1001
        -codec:v mpeg2video -g 18 -b:v 2040k -maxrate:v 2516k -minrate:v 0 -bufsize:v 1835008 -scan_offset 1
        -ar 44100
        -codec:a mp2 -b:a 224k
        
        &lt;film&gt;:
        -f svcd -packetsize 2324
        -s 480x480 -pix_fmt yuv420p -r 24000/1001
        -codec:v mpeg2video -g 18 -b:v 2040k -maxrate:v 2516k -minrate:v 0 -bufsize:v 1835008 -scan_offset 1
        -ar 44100
        -codec:a mp2 -b:a 224k
</pre>
<p> <font SIZE="-1"><code>DVD</code></font> </p>
<pre>
        &lt;pal&gt;:
        -f dvd -muxrate 10080k -packetsize 2048
        -s 720x576 -pix_fmt yuv420p -r 25
        -codec:v mpeg2video -g 15 -b:v 6000k -maxrate:v 9000k -minrate:v 0 -bufsize:v 1835008
        -ar 48000
        -codec:a ac3 -b:a 448k
        
        &lt;ntsc&gt;:
        -f dvd -muxrate 10080k -packetsize 2048
        -s 720x480 -pix_fmt yuv420p -r 30000/1001
        -codec:v mpeg2video -g 18 -b:v 6000k -maxrate:v 9000k -minrate:v 0 -bufsize:v 1835008
        -ar 48000
        -codec:a ac3 -b:a 448k
        
        &lt;film&gt;:
        -f dvd -muxrate 10080k -packetsize 2048
        -s 720x480 -pix_fmt yuv420p -r 24000/1001
        -codec:v mpeg2video -g 18 -b:v 6000k -maxrate:v 9000k -minrate:v 0 -bufsize:v 1835008
        -ar 48000
        -codec:a ac3 -b:a 448k
</pre>
<p> <font SIZE="-1"><code>DV</code></font> </p>
<pre>
        &lt;pal&gt;:
        -f dv
        -s 720x576 -pix_fmt yuv420p -r 25
        -ar 48000 -ac 2
        
        &lt;ntsc&gt;:
        -f dv
        -s 720x480 -pix_fmt yuv411p -r 30000/1001
        -ar 48000 -ac 2
        
        &lt;film&gt;:
        -f dv
        -s 720x480 -pix_fmt yuv411p -r 24000/1001
        -ar 48000 -ac 2
</pre>
<p> The <tt>&quot;dv50&quot;</tt> target is identical to the <tt>&quot;dv&quot;</tt> target except that the pixel format set is <tt>&quot;yuv422p&quot;</tt> for all three standards. </p>
<p> Any user-set value for a parameter above will override the target preset value. In that case, the output may not comply with the target standard.</p>
<dt><code>-dn (</code><i>input/output</i><code>)</code></p>
<dd> As an input option, blocks all data streams of a file from being filtered or being automatically selected or mapped for any output. See <tt>&quot;-discard&quot;</tt> option to disable streams individually. </p>
<p> As an output option, disables data recording i.e. automatic selection or mapping of any data stream. For full manual control see the <tt>&quot;-map&quot;</tt> option.</p>
<dt><code>-dframes</code> <i>number</i> <code>(</code><i>output</i><code>)</code></p>
<dd> Set the number of data frames to output. This is an obsolete alias for <tt>&quot;-frames:d&quot;</tt>, which you should use instead.</p>
<dt><code>-frames[:</code><i>stream_specifier</i><code>]</code> <i>framecount</i> <code>(</code><i>output,per-stream</i><code>)</code></p>
<dd> Stop writing to the stream after <i>framecount</i> frames.</p>
<dt><code>-q[:</code><i>stream_specifier</i><code>]</code> <i>q</i> <code>(</code><i>output,per-stream</i><code>)</code></p>
<dd>
<dt><code>-qscale[:</code><i>stream_specifier</i><code>]</code> <i>q</i> <code>(</code><i>output,per-stream</i><code>)</code></p>
<dd> Use fixed quality scale (<font SIZE="-1">VBR</font>). The meaning of <i>q</i>/<i>qscale</i> is codec-dependent. If <i>qscale</i> is used without a <i>stream_specifier</i> then it applies only to the video stream, this is to maintain compatibility with previous behavior and as specifying the same codec specific value to 2 different codecs that is audio and video generally is not what is intended when no stream_specifier is used.</p>
<dt><code>-filter[:</code><i>stream_specifier</i><code>]</code> <i>filtergraph</i> <code>(</code><i>output,per-stream</i><code>)</code></p>
<dd> Create the filtergraph specified by <i>filtergraph</i> and use it to filter the stream. </p>
<p> <i>filtergraph</i> is a description of the filtergraph to apply to the stream, and must have a single input and a single output of the same type of the stream. In the filtergraph, the input is associated to the label <tt>&quot;in&quot;</tt>, and the output to the label <tt>&quot;out&quot;</tt>. See the ffmpeg-filters manual for more information about the filtergraph syntax. </p>
<p> See the <code>-filter_complex option</code> if you want to create filtergraphs with multiple inputs and/or outputs.</p>
<dt><code>-filter_script[:</code><i>stream_specifier</i><code>]</code> <i>filename</i> <code>(</code><i>output,per-stream</i><code>)</code></p>
<dd> This option is similar to <code>-filter</code>, the only difference is that its argument is the name of the file from which a filtergraph description is to be read.</p>
<dt><code>-filter_threads</code> <i>nb_threads</i> <code>(</code><i>global</i><code>)</code></p>
<dd> Defines how many threads are used to process a filter pipeline. Each pipeline will produce a thread pool with this many threads available for parallel processing. The default is the number of available CPUs.</p>
<dt><code>-pre[:</code><i>stream_specifier</i><code>]</code> <i>preset_name</i> <code>(</code><i>output,per-stream</i><code>)</code></p>
<dd> Specify the preset for matching stream(s).</p>
<dt><code>-stats (</code><i>global</i><code>)</code></p>
<dd> Print encoding progress/statistics. It is on by default, to explicitly disable it you need to specify <tt>&quot;-nostats&quot;</tt>.</p>
<dt><code>-stats_period</code> <i>time</i> <code>(</code><i>global</i><code>)</code></p>
<dd> Set period at which encoding progress/statistics are updated. Default is 0.5 seconds.</p>
<dt><code>-progress</code> <i>url</i> <code>(</code><i>global</i><code>)</code></p>
<dd> Send program-friendly progress information to <i>url</i>. </p>
<p> Progress information is written periodically and at the end of the encoding process. It is made of &quot;<i>key</i>=<i>value</i>&quot; lines. <i>key</i> consists of only alphanumeric characters. The last key of a sequence of progress information is always &#8220;progress&#8221;. </p>
<p> The update period is set using <tt>&quot;-stats_period&quot;</tt>.</p>
<dt><code>-stdin</code></p>
<dd> Enable interaction on standard input. On by default unless standard input is used as an input. To explicitly disable interaction you need to specify <tt>&quot;-nostdin&quot;</tt>. </p>
<p> Disabling interaction on standard input is useful, for example, if ffmpeg is in the background process group. Roughly the same result can be achieved with <tt>&quot;ffmpeg ... &lt; /dev/null&quot;</tt> but it requires a shell.</p>
<dt><code>-debug_ts (</code><i>global</i><code>)</code></p>
<dd> Print timestamp information. It is off by default. This option is mostly useful for testing and debugging purposes, and the output format may change from one version to another, so it should not be employed by portable scripts. </p>
<p> See also the option <tt>&quot;-fdebug ts&quot;</tt>.</p>
<dt><code>-attach</code> <i>filename</i> <code>(</code><i>output</i><code>)</code></p>
<dd> Add an attachment to the output file. This is supported by a few formats like Matroska for e.g. fonts used in rendering subtitles. Attachments are implemented as a specific type of stream, so this option will add a new stream to the file. It is then possible to use per-stream options on this stream in the usual way. Attachment streams created with this option will be created after all the other streams (i.e. those created with <tt>&quot;-map&quot;</tt> or automatic mappings). </p>
<p> Note that for Matroska you also have to set the mimetype metadata tag: </p>
<pre>
        ffmpeg -i INPUT -attach DejaVuSans.ttf -metadata:s:2 mimetype=application/x-truetype-font out.mkv
</pre>
<p> (assuming that the attachment stream will be third in the output file).</p>
<dt><code>-dump_attachment[:</code><i>stream_specifier</i><code>]</code> <i>filename</i> <code>(</code><i>input,per-stream</i><code>)</code></p>
<dd> Extract the matching attachment stream into a file named <i>filename</i>. If <i>filename</i> is empty, then the value of the <tt>&quot;filename&quot;</tt> metadata tag will be used. </p>
<p> E.g. to extract the first attachment to a file named &#8216;out.ttf&#8217;: </p>
<pre>
        ffmpeg -dump_attachment:t:0 out.ttf -i INPUT
</pre>
<p> To extract all attachments to files determined by the <tt>&quot;filename&quot;</tt> tag: </p>
<pre>
        ffmpeg -dump_attachment:t &quot;&quot; -i INPUT
</pre>
<p> Technical note &#8212; attachments are implemented as codec extradata, so this option can actually be used to extract extradata from any stream, not just attachments.</dl>
<h3>Video Options</h3>
<dl>
<dt><code>-vframes</code> <i>number</i> <code>(</code><i>output</i><code>)</code></p>
<dd> Set the number of video frames to output. This is an obsolete alias for <tt>&quot;-frames:v&quot;</tt>, which you should use instead.</p>
<dt><code>-r[:</code><i>stream_specifier</i><code>]</code> <i>fps</i> <code>(</code><i>input/output,per-stream</i><code>)</code></p>
<dd> Set frame rate (Hz value, fraction or abbreviation). </p>
<p> As an input option, ignore any timestamps stored in the file and instead generate timestamps assuming constant frame rate <i>fps</i>. This is not the same as the <code>-framerate</code> option used for some input formats like image2 or v4l2 (it used to be the same in older versions of FFmpeg). If in doubt use <code>-framerate</code> instead of the input option <code>-r</code>. </p>
<p> As an output option, duplicate or drop input frames to achieve constant output frame rate <i>fps</i>.</p>
<dt><code>-fpsmax[:</code><i>stream_specifier</i><code>]</code> <i>fps</i> <code>(</code><i>output,per-stream</i><code>)</code></p>
<dd> Set maximum frame rate (Hz value, fraction or abbreviation). </p>
<p> Clamps output frame rate when output framerate is auto-set and is higher than this value. Useful in batch processing or when input framerate is wrongly detected as very high. It cannot be set together with <tt>&quot;-r&quot;</tt>. It is ignored during streamcopy.</p>
<dt><code>-s[:</code><i>stream_specifier</i><code>]</code> <i>size</i> <code>(</code><i>input/output,per-stream</i><code>)</code></p>
<dd> Set frame size. </p>
<p> As an input option, this is a shortcut for the <code>video_size</code> private option, recognized by some demuxers for which the frame size is either not stored in the file or is configurable &#8212; e.g. raw video or video grabbers. </p>
<p> As an output option, this inserts the <tt>&quot;scale&quot;</tt> video filter to the <i>end</i> of the corresponding filtergraph. Please use the <tt>&quot;scale&quot;</tt> filter directly to insert it at the beginning or some other place. </p>
<p> The format is <code>wxh</code> (default &#8211; same as source).</p>
<dt><code>-aspect[:</code><i>stream_specifier</i><code>]</code> <i>aspect</i> <code>(</code><i>output,per-stream</i><code>)</code></p>
<dd> Set the video display aspect ratio specified by <i>aspect</i>. </p>
<p> <i>aspect</i> can be a floating point number string, or a string of the form <i>num</i>:<i>den</i>, where <i>num</i> and <i>den</i> are the numerator and denominator of the aspect ratio. For example &#8220;4:3&#8221;, &#8220;16:9&#8221;, &#8220;1.3333&#8221;, and &#8220;1.7777&#8221; are valid argument values. </p>
<p> If used together with <code>-vcodec copy</code>, it will affect the aspect ratio stored at container level, but not the aspect ratio stored in encoded frames, if it exists.</p>
<dt><code>-vn (</code><i>input/output</i><code>)</code></p>
<dd> As an input option, blocks all video streams of a file from being filtered or being automatically selected or mapped for any output. See <tt>&quot;-discard&quot;</tt> option to disable streams individually. </p>
<p> As an output option, disables video recording i.e. automatic selection or mapping of any video stream. For full manual control see the <tt>&quot;-map&quot;</tt> option.</p>
<dt><code>-vcodec</code> <i>codec</i> <code>(</code><i>output</i><code>)</code></p>
<dd> Set the video codec. This is an alias for <tt>&quot;-codec:v&quot;</tt>.</p>
<dt><code>-pass[:</code><i>stream_specifier</i><code>]</code> <i>n</i> <code>(</code><i>output,per-stream</i><code>)</code></p>
<dd> Select the pass number (1 or 2). It is used to do two-pass video encoding. The statistics of the video are recorded in the first pass into a log file (see also the option -passlogfile), and in the second pass that log file is used to generate the video at the exact requested bitrate. On pass 1, you may just deactivate audio and set output to null, examples for Windows and Unix: </p>
<pre>
        ffmpeg -i foo.mov -c:v libxvid -pass 1 -an -f rawvideo -y NUL
        ffmpeg -i foo.mov -c:v libxvid -pass 1 -an -f rawvideo -y /dev/null
</pre>
<dt><code>-passlogfile[:</code><i>stream_specifier</i><code>]</code> <i>prefix</i> <code>(</code><i>output,per-stream</i><code>)</code></p>
<dd> Set two-pass log file name prefix to <i>prefix</i>, the default file name prefix is &#8220;ffmpeg2pass&#8221;. The complete file name will be <i></i><font SIZE="-1"><i>PREFIX-N</i></font><i>.log</i>, where N is a number specific to the output stream</p>
<dt><code>-vf</code> <i>filtergraph</i> <code>(</code><i>output</i><code>)</code></p>
<dd> Create the filtergraph specified by <i>filtergraph</i> and use it to filter the stream. </p>
<p> This is an alias for <tt>&quot;-filter:v&quot;</tt>, see the <code>-filter option</code>.</p>
<dt><code>-autorotate</code></p>
<dd> Automatically rotate the video according to file metadata. Enabled by default, use <code>-noautorotate</code> to disable it.</p>
<dt><code>-autoscale</code></p>
<dd> Automatically scale the video according to the resolution of first frame. Enabled by default, use <code>-noautoscale</code> to disable it. When autoscale is disabled, all output frames of filter graph might not be in the same resolution and may be inadequate for some encoder/muxer. Therefore, it is not recommended to disable it unless you really know what you are doing. Disable autoscale at your own risk.</dl>
<h3>Advanced Video options</h3>
<dl>
<dt><code>-pix_fmt[:</code><i>stream_specifier</i><code>]</code> <i>format</i> <code>(</code><i>input/output,per-stream</i><code>)</code></p>
<dd> Set pixel format. Use <tt>&quot;-pix_fmts&quot;</tt> to show all the supported pixel formats. If the selected pixel format can not be selected, ffmpeg will print a warning and select the best pixel format supported by the encoder. If <i>pix_fmt</i> is prefixed by a <tt>&quot;+&quot;</tt>, ffmpeg will exit with an error if the requested pixel format can not be selected, and automatic conversions inside filtergraphs are disabled. If <i>pix_fmt</i> is a single <tt>&quot;+&quot;</tt>, ffmpeg selects the same pixel format as the input (or graph output) and automatic conversions are disabled.</p>
<dt><code>-sws_flags</code> <i>flags</i> <code>(</code><i>input/output</i><code>)</code></p>
<dd> Set SwScaler flags.</p>
<dt><code>-rc_override[:</code><i>stream_specifier</i><code>]</code> <i>override</i> <code>(</code><i>output,per-stream</i><code>)</code></p>
<dd> Rate control override for specific intervals, formatted as &#8220;int,int,int&#8221; list separated with slashes. Two first values are the beginning and end frame numbers, last one is quantizer to use if positive, or quality factor if negative.</p>
<dt><code>-ilme</code></p>
<dd> Force interlacing support in encoder (<font SIZE="-1">MPEG-2</font> and <font SIZE="-1">MPEG-4</font> only). Use this option if your input file is interlaced and you want to keep the interlaced format for minimum losses. The alternative is to deinterlace the input stream by use of a filter such as <tt>&quot;yadif&quot;</tt> or <tt>&quot;bwdif&quot;</tt>, but deinterlacing introduces losses.</p>
<dt><code>-psnr</code></p>
<dd> Calculate <font SIZE="-1">PSNR</font> of compressed frames.</p>
<dt><code>-vstats</code></p>
<dd> Dump video coding statistics to <i>vstats_HHMMSS.log</i>.</p>
<dt><code>-vstats_file</code> <i>file</i></p>
<dd> Dump video coding statistics to <i>file</i>.</p>
<dt><code>-vstats_version</code> <i>file</i></p>
<dd> Specifies which version of the vstats format to use. Default is 2. </p>
<p> version = 1 : </p>
<p> <tt>&quot;frame= %5d q= %2.1f PSNR= %6.2f f_size= %6d s_size= %8.0fkB time= %0.3f br= %7.1fkbits/s avg_br= %7.1fkbits/s&quot;</tt> </p>
<p> version &gt; 1: </p>
<p> <tt>&quot;out= %2d st= %2d frame= %5d q= %2.1f PSNR= %6.2f f_size= %6d s_size= %8.0fkB time= %0.3f br= %7.1fkbits/s avg_br= %7.1fkbits/s&quot;</tt></p>
<dt><code>-top[:</code><i>stream_specifier</i><code>]</code> <i>n</i> <code>(</code><i>output,per-stream</i><code>)</code></p>
<dd> top=1/bottom=0/auto=-1 field first</p>
<dt><code>-dc</code> <i>precision</i></p>
<dd> Intra_dc_precision.</p>
<dt><code>-vtag</code> <i>fourcc/tag</i> <code>(</code><i>output</i><code>)</code></p>
<dd> Force video tag/fourcc. This is an alias for <tt>&quot;-tag:v&quot;</tt>.</p>
<dt><code>-qphist (</code><i>global</i><code>)</code></p>
<dd> Show <font SIZE="-1">QP</font> histogram</p>
<dt><code>-vbsf</code> <i>bitstream_filter</i></p>
<dd> Deprecated see -bsf</p>
<dt><code>-force_key_frames[:</code><i>stream_specifier</i><code>]</code> <i>time</i><code>[,</code><i>time</i><code>&#8230;] (</code><i>output,per-stream</i><code>)</code></p>
<dd>
<dt><code>-force_key_frames[:</code><i>stream_specifier</i><code>] expr:</code><i>expr</i> <code>(</code><i>output,per-stream</i><code>)</code></p>
<dd>
<dt><code>-force_key_frames[:</code><i>stream_specifier</i><code>] source (</code><i>output,per-stream</i><code>)</code></p>
<dd> <i>force_key_frames</i> can take arguments of the following form:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>time</i><code>[,</code><i>time</i><code>&#8230;]</code></p>
<dd> If the argument consists of timestamps, ffmpeg will round the specified times to the nearest output timestamp as per the encoder time base and force a keyframe at the first frame having timestamp equal or greater than the computed timestamp. Note that if the encoder time base is too coarse, then the keyframes may be forced on frames with timestamps lower than the specified time. The default encoder time base is the inverse of the output framerate but may be set otherwise via <tt>&quot;-enc_time_base&quot;</tt>. </p>
<p> If one of the times is &quot;<tt>&quot;chapters&quot;</tt>[<i>delta</i>]&quot;, it is expanded into the time of the beginning of all chapters in the file, shifted by <i>delta</i>, expressed as a time in seconds. This option can be useful to ensure that a seek point is present at a chapter mark or any other designated place in the output file. </p>
<p> For example, to insert a key frame at 5 minutes, plus key frames 0.1 second before the beginning of every chapter: </p>
<pre>
        -force_key_frames 0:05:00,chapters-0.1
</pre>
<dt><code>expr:</code><i>expr</i></p>
<dd> If the argument is prefixed with <tt>&quot;expr:&quot;</tt>, the string <i>expr</i> is interpreted like an expression and is evaluated for each frame. A key frame is forced in case the evaluation is non-zero. </p>
<p> The expression in <i>expr</i> can contain the following constants:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>n</code></p>
<dd> the number of current processed frame, starting from 0</p>
<dt><code>n_forced</code></p>
<dd> the number of forced frames</p>
<dt><code>prev_forced_n</code></p>
<dd> the number of the previous forced frame, it is <tt>&quot;NAN&quot;</tt> when no keyframe was forced yet</p>
<dt><code>prev_forced_t</code></p>
<dd> the time of the previous forced frame, it is <tt>&quot;NAN&quot;</tt> when no keyframe was forced yet</p>
<dt><code>t</code></p>
<dd> the time of the current processed frame</dl>
</dl>
<dl>
<dt>
<dd>
<p> For example to force a key frame every 5 seconds, you can specify: </p>
<pre>
        -force_key_frames expr:gte(t,n_forced*5)
</pre>
<p> To force a key frame 5 seconds after the time of the last forced one, starting from second 13: </p>
<pre>
        -force_key_frames expr:if(isnan(prev_forced_t),gte(t,13),gte(t,prev_forced_t+5))
</pre>
</dl>
<dt><code>source</code></p>
<dd> If the argument is <tt>&quot;source&quot;</tt>, ffmpeg will force a key frame if the current frame being encoded is marked as a key frame in its source.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Note that forcing too many keyframes is very harmful for the lookahead algorithms of certain encoders: using fixed-GOP options or similar would be more efficient.</dl>
<dt><code>-copyinkf[:</code><i>stream_specifier</i><code>] (</code><i>output,per-stream</i><code>)</code></p>
<dd> When doing stream copy, copy also non-key frames found at the beginning.</p>
<dt><code>-init_hw_device</code> <i>type</i><code>[=</code><i>name</i><code>][:</code><i>device</i><code>[,</code><i>key=value</i><code>&#8230;]]</code></p>
<dd> Initialise a new hardware device of type <i>type</i> called <i>name</i>, using the given device parameters. If no name is specified it will receive a default name of the form &quot;<i>type</i><tt>%d</tt>&quot;. </p>
<p> The meaning of <i>device</i> and the following arguments depends on the device type:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>cuda</code></p>
<dd> <i>device</i> is the number of the <font SIZE="-1">CUDA</font> device.</p>
<dt><code>dxva2</code></p>
<dd> <i>device</i> is the number of the Direct3D 9 display adapter.</p>
<dt><code>vaapi</code></p>
<dd> <i>device</i> is either an X11 display name or a <font SIZE="-1">DRM</font> render node. If not specified, it will attempt to open the default X11 display (<i></i>$DISPLAY<i></i>) and then the first <font SIZE="-1">DRM</font> render node (<i>/dev/dri/renderD128</i>).</p>
<dt><code>vdpau</code></p>
<dd> <i>device</i> is an X11 display name. If not specified, it will attempt to open the default X11 display (<i></i>$DISPLAY<i></i>).</p>
<dt><code>qsv</code></p>
<dd> <i>device</i> selects a value in <code>MFX_IMPL_*</code>. Allowed values are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>auto</code></p>
<dd>
<dt><code>sw</code></p>
<dd>
<dt><code>hw</code></p>
<dd>
<dt><code>auto_any</code></p>
<dd>
<dt><code>hw_any</code></p>
<dd>
<dt><code>hw2</code></p>
<dd>
<dt><code>hw3</code></p>
<dd>
<dt><code>hw4</code></p>
<dd></dl>
</dl>
<dl>
<dt>
<dd>
<p> If not specified, <code>auto_any</code> is used. (Note that it may be easier to achieve the desired result for <font SIZE="-1">QSV</font> by creating the platform-appropriate subdevice (<code>dxva2</code> or <code>vaapi</code>) and then deriving a <font SIZE="-1">QSV</font> device from that.)</dl>
<dt><code>opencl</code></p>
<dd> <i>device</i> selects the platform and device as <i>platform_index.device_index</i>. </p>
<p> The set of devices can also be filtered using the key-value pairs to find only devices matching particular platform or device strings. </p>
<p> The strings usable as filters are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>platform_profile</code></p>
<dd>
<dt><code>platform_version</code></p>
<dd>
<dt><code>platform_name</code></p>
<dd>
<dt><code>platform_vendor</code></p>
<dd>
<dt><code>platform_extensions</code></p>
<dd>
<dt><code>device_name</code></p>
<dd>
<dt><code>device_vendor</code></p>
<dd>
<dt><code>driver_version</code></p>
<dd>
<dt><code>device_version</code></p>
<dd>
<dt><code>device_profile</code></p>
<dd>
<dt><code>device_extensions</code></p>
<dd>
<dt><code>device_type</code></p>
<dd></dl>
</dl>
<dl>
<dt>
<dd>
<p> The indices and filters must together uniquely select a device. </p>
<p> Examples:</p>
<dl>
<dt><i>-init_hw_device opencl:0.1</i></p>
<dd> Choose the second device on the first platform.</p>
<dt><i>-init_hw_device opencl:,device_name=Foo9000</i></p>
<dd> Choose the device with a name containing the string <i>Foo9000</i>.</p>
<dt><i>-init_hw_device opencl:1,device_type=gpu,device_extensions=cl_khr_fp16</i></p>
<dd> Choose the <font SIZE="-1">GPU</font> device on the second platform supporting the <i>cl_khr_fp16</i> extension.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>vulkan</code></p>
<dd> If <i>device</i> is an integer, it selects the device by its index in a system-dependent list of devices. If <i>device</i> is any other string, it selects the first device with a name containing that string as a substring. </p>
<p> The following options are recognized:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>debug</code></p>
<dd> If set to 1, enables the validation layer, if installed.</p>
<dt><code>linear_images</code></p>
<dd> If set to 1, images allocated by the hwcontext will be linear and locally mappable.</p>
<dt><code>instance_extensions</code></p>
<dd> A plus separated list of additional instance extensions to enable.</p>
<dt><code>device_extensions</code></p>
<dd> A plus separated list of additional device extensions to enable.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Examples:</p>
<dl>
<dt><i>-init_hw_device vulkan:1</i></p>
<dd> Choose the second device on the system.</p>
<dt><i>-init_hw_device vulkan:RADV</i></p>
<dd> Choose the first device with a name containing the string <i></i><font SIZE="-1"><i>RADV</i></font><i></i>.</p>
<dt><i>-init_hw_device vulkan:0,instance_extensions=VK_KHR_wayland_surface+VK_KHR_xcb_surface</i></p>
<dd> Choose the first device and enable the Wayland and <font SIZE="-1">XCB</font> instance extensions.</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-init_hw_device</code> <i>type</i><code>[=</code><i>name</i><code>]@</code><i>source</i></p>
<dd> Initialise a new hardware device of type <i>type</i> called <i>name</i>, deriving it from the existing device with the name <i>source</i>.</p>
<dt><code>-init_hw_device list</code></p>
<dd> List all hardware device types supported in this build of ffmpeg.</p>
<dt><code>-filter_hw_device</code> <i>name</i></p>
<dd> Pass the hardware device called <i>name</i> to all filters in any filter graph. This can be used to set the device to upload to with the <tt>&quot;hwupload&quot;</tt> filter, or the device to map to with the <tt>&quot;hwmap&quot;</tt> filter. Other filters may also make use of this parameter when they require a hardware device. Note that this is typically only required when the input is not already in hardware frames &#8211; when it is, filters will derive the device they require from the context of the frames they receive as input. </p>
<p> This is a global setting, so all filters will receive the same device.</p>
<dt><code>-hwaccel[:</code><i>stream_specifier</i><code>]</code> <i>hwaccel</i> <code>(</code><i>input,per-stream</i><code>)</code></p>
<dd> Use hardware acceleration to decode the matching stream(s). The allowed values of <i>hwaccel</i> are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>none</code></p>
<dd> Do not use any hardware acceleration (the default).</p>
<dt><code>auto</code></p>
<dd> Automatically select the hardware acceleration method.</p>
<dt><code>vdpau</code></p>
<dd> Use <font SIZE="-1">VDPAU</font> (Video Decode and Presentation <font SIZE="-1">API</font> for Unix) hardware acceleration.</p>
<dt><code>dxva2</code></p>
<dd> Use <font SIZE="-1">DXVA2</font> (DirectX Video Acceleration) hardware acceleration.</p>
<dt><code>vaapi</code></p>
<dd> Use <font SIZE="-1">VAAPI</font> (Video Acceleration <font SIZE="-1">API</font>) hardware acceleration.</p>
<dt><code>qsv</code></p>
<dd> Use the Intel QuickSync Video acceleration for video transcoding. </p>
<p> Unlike most other values, this option does not enable accelerated decoding (that is used automatically whenever a qsv decoder is selected), but accelerated transcoding, without copying the frames into the system memory. </p>
<p> For it to work, both the decoder and the encoder must support <font SIZE="-1">QSV</font> acceleration and no filters must be used.</dl>
</dl>
<dl>
<dt>
<dd>
<p> This option has no effect if the selected hwaccel is not available or not supported by the chosen decoder. </p>
<p> Note that most acceleration methods are intended for playback and will not be faster than software decoding on modern CPUs. Additionally, <code>ffmpeg</code> will usually need to copy the decoded frames from the <font SIZE="-1">GPU</font> memory into the system memory, resulting in further performance loss. This option is thus mainly useful for testing.</dl>
<dt><code>-hwaccel_device[:</code><i>stream_specifier</i><code>]</code> <i>hwaccel_device</i> <code>(</code><i>input,per-stream</i><code>)</code></p>
<dd> Select a device to use for hardware acceleration. </p>
<p> This option only makes sense when the <code>-hwaccel</code> option is also specified. It can either refer to an existing device created with <code>-init_hw_device</code> by name, or it can create a new device as if <code>-init_hw_device</code> <i>type</i>:<i>hwaccel_device</i> were called immediately before.</p>
<dt><code>-hwaccels</code></p>
<dd> List all hardware acceleration methods supported in this build of ffmpeg.</dl>
<h3>Audio Options</h3>
<dl>
<dt><code>-aframes</code> <i>number</i> <code>(</code><i>output</i><code>)</code></p>
<dd> Set the number of audio frames to output. This is an obsolete alias for <tt>&quot;-frames:a&quot;</tt>, which you should use instead.</p>
<dt><code>-ar[:</code><i>stream_specifier</i><code>]</code> <i>freq</i> <code>(</code><i>input/output,per-stream</i><code>)</code></p>
<dd> Set the audio sampling frequency. For output streams it is set by default to the frequency of the corresponding input stream. For input streams this option only makes sense for audio grabbing devices and raw demuxers and is mapped to the corresponding demuxer options.</p>
<dt><code>-aq</code> <i>q</i> <code>(</code><i>output</i><code>)</code></p>
<dd> Set the audio quality (codec-specific, <font SIZE="-1">VBR</font>). This is an alias for -q:a.</p>
<dt><code>-ac[:</code><i>stream_specifier</i><code>]</code> <i>channels</i> <code>(</code><i>input/output,per-stream</i><code>)</code></p>
<dd> Set the number of audio channels. For output streams it is set by default to the number of input audio channels. For input streams this option only makes sense for audio grabbing devices and raw demuxers and is mapped to the corresponding demuxer options.</p>
<dt><code>-an (</code><i>input/output</i><code>)</code></p>
<dd> As an input option, blocks all audio streams of a file from being filtered or being automatically selected or mapped for any output. See <tt>&quot;-discard&quot;</tt> option to disable streams individually. </p>
<p> As an output option, disables audio recording i.e. automatic selection or mapping of any audio stream. For full manual control see the <tt>&quot;-map&quot;</tt> option.</p>
<dt><code>-acodec</code> <i>codec</i> <code>(</code><i>input/output</i><code>)</code></p>
<dd> Set the audio codec. This is an alias for <tt>&quot;-codec:a&quot;</tt>.</p>
<dt><code>-sample_fmt[:</code><i>stream_specifier</i><code>]</code> <i>sample_fmt</i> <code>(</code><i>output,per-stream</i><code>)</code></p>
<dd> Set the audio sample format. Use <tt>&quot;-sample_fmts&quot;</tt> to get a list of supported sample formats.</p>
<dt><code>-af</code> <i>filtergraph</i> <code>(</code><i>output</i><code>)</code></p>
<dd> Create the filtergraph specified by <i>filtergraph</i> and use it to filter the stream. </p>
<p> This is an alias for <tt>&quot;-filter:a&quot;</tt>, see the <code>-filter option</code>.</dl>
<h3>Advanced Audio options</h3>
<dl>
<dt><code>-atag</code> <i>fourcc/tag</i> <code>(</code><i>output</i><code>)</code></p>
<dd> Force audio tag/fourcc. This is an alias for <tt>&quot;-tag:a&quot;</tt>.</p>
<dt><code>-absf</code> <i>bitstream_filter</i></p>
<dd> Deprecated, see -bsf</p>
<dt><code>-guess_layout_max</code> <i>channels</i> <code>(</code><i>input,per-stream</i><code>)</code></p>
<dd> If some input channel layout is not known, try to guess only if it corresponds to at most the specified number of channels. For example, 2 tells to <code>ffmpeg</code> to recognize 1 channel as mono and 2 channels as stereo but not 6 channels as 5.1. The default is to always try to guess. Use 0 to disable all guessing.</dl>
<h3>Subtitle options</h3>
<dl>
<dt><code>-scodec</code> <i>codec</i> <code>(</code><i>input/output</i><code>)</code></p>
<dd> Set the subtitle codec. This is an alias for <tt>&quot;-codec:s&quot;</tt>.</p>
<dt><code>-sn (</code><i>input/output</i><code>)</code></p>
<dd> As an input option, blocks all subtitle streams of a file from being filtered or being automatically selected or mapped for any output. See <tt>&quot;-discard&quot;</tt> option to disable streams individually. </p>
<p> As an output option, disables subtitle recording i.e. automatic selection or mapping of any subtitle stream. For full manual control see the <tt>&quot;-map&quot;</tt> option.</p>
<dt><code>-sbsf</code> <i>bitstream_filter</i></p>
<dd> Deprecated, see -bsf</dl>
<h3>Advanced Subtitle options</h3>
<dl>
<dt><code>-fix_sub_duration</code></p>
<dd> Fix subtitles durations. For each subtitle, wait for the next packet in the same stream and adjust the duration of the first to avoid overlap. This is necessary with some subtitles codecs, especially <font SIZE="-1">DVB</font> subtitles, because the duration in the original packet is only a rough estimate and the end is actually marked by an empty subtitle frame. Failing to use this option when necessary can result in exaggerated durations or muxing failures due to non-monotonic timestamps. </p>
<p> Note that this option will delay the output of all data until the next subtitle packet is decoded: it may increase memory consumption and latency a lot.</p>
<dt><code>-canvas_size</code> <i>size</i></p>
<dd> Set the size of the canvas used to render subtitles.</dl>
<h3>Advanced options</h3>
<dl>
<dt><code>-map [-]</code><i>input_file_id</i><code>[:</code><i>stream_specifier</i><code>][?][,</code><i>sync_file_id</i><code>[:</code><i>stream_specifier</i><code>]] |</code> <i>[linklabel]</i> <code>(</code><i>output</i><code>)</code></p>
<dd> Designate one or more input streams as a source for the output file. Each input stream is identified by the input file index <i>input_file_id</i> and the input stream index <i>input_stream_id</i> within the input file. Both indices start at 0. If specified, <i>sync_file_id</i>:<i>stream_specifier</i> sets which input stream is used as a presentation sync reference. </p>
<p> The first <tt>&quot;-map&quot;</tt> option on the command line specifies the source for output stream 0, the second <tt>&quot;-map&quot;</tt> option specifies the source for output stream 1, etc. </p>
<p> A <tt>&quot;-&quot;</tt> character before the stream identifier creates a &#8220;negative&#8221; mapping. It disables matching streams from already created mappings. </p>
<p> A trailing <tt>&quot;?&quot;</tt> after the stream index will allow the map to be optional: if the map matches no streams the map will be ignored instead of failing. Note the map will still fail if an invalid input file index is used; such as if the map refers to a non-existent input. </p>
<p> An alternative <i>[linklabel]</i> form will map outputs from complex filter graphs (see the <code>-filter_complex</code> option) to the output file. <i>linklabel</i> must correspond to a defined output link label in the graph. </p>
<p> For example, to map <font SIZE="-1">ALL</font> streams from the first input file to output </p>
<pre>
        ffmpeg -i INPUT -map 0 output
</pre>
<p> For example, if you have two audio streams in the first input file, these streams are identified by &#8220;0:0&#8221; and &#8220;0:1&#8221;. You can use <tt>&quot;-map&quot;</tt> to select which streams to place in an output file. For example: </p>
<pre>
        ffmpeg -i INPUT -map 0:1 out.wav
</pre>
<p> will map the input stream in <i></i><font SIZE="-1"><i>INPUT</i></font><i></i> identified by &#8220;0:1&#8221; to the (single) output stream in <i>out.wav</i>. </p>
<p> For example, to select the stream with index 2 from input file <i>a.mov</i> (specified by the identifier &#8220;0:2&#8221;), and stream with index 6 from input <i>b.mov</i> (specified by the identifier &#8220;1:6&#8221;), and copy them to the output file <i>out.mov</i>: </p>
<pre>
        ffmpeg -i a.mov -i b.mov -c copy -map 0:2 -map 1:6 out.mov
</pre>
<p> To select all video and the third audio stream from an input file: </p>
<pre>
        ffmpeg -i INPUT -map 0:v -map 0:a:2 OUTPUT
</pre>
<p> To map all the streams except the second audio, use negative mappings </p>
<pre>
        ffmpeg -i INPUT -map 0 -map -0:a:1 OUTPUT
</pre>
<p> To map the video and audio streams from the first input, and using the trailing <tt>&quot;?&quot;</tt>, ignore the audio mapping if no audio streams exist in the first input: </p>
<pre>
        ffmpeg -i INPUT -map 0:v -map 0:a? OUTPUT
</pre>
<p> To pick the English audio stream: </p>
<pre>
        ffmpeg -i INPUT -map 0:m:language:eng OUTPUT
</pre>
<p> Note that using this option disables the default mappings for this output file.</p>
<dt><code>-ignore_unknown</code></p>
<dd> Ignore input streams with unknown type instead of failing if copying such streams is attempted.</p>
<dt><code>-copy_unknown</code></p>
<dd> Allow input streams with unknown type to be copied instead of failing if copying such streams is attempted.</p>
<dt><code>-map_channel [</code><i>input_file_id</i><code>.</code><i>stream_specifier</i><code>.</code><i>channel_id</i><code>|-1][?][:</code><i>output_file_id</i><code>.</code><i>stream_specifier</i><code>]</code></p>
<dd> Map an audio channel from a given input to an output. If <i>output_file_id</i>.<i>stream_specifier</i> is not set, the audio channel will be mapped on all the audio streams. </p>
<p> Using &#8220;-1&#8221; instead of <i>input_file_id</i>.<i>stream_specifier</i>.<i>channel_id</i> will map a muted channel. </p>
<p> A trailing <tt>&quot;?&quot;</tt> will allow the map_channel to be optional: if the map_channel matches no channel the map_channel will be ignored instead of failing. </p>
<p> For example, assuming <i></i><font SIZE="-1"><i>INPUT</i></font><i></i> is a stereo audio file, you can switch the two audio channels with the following command: </p>
<pre>
        ffmpeg -i INPUT -map_channel 0.0.1 -map_channel 0.0.0 OUTPUT
</pre>
<p> If you want to mute the first channel and keep the second: </p>
<pre>
        ffmpeg -i INPUT -map_channel -1 -map_channel 0.0.1 OUTPUT
</pre>
<p> The order of the &#8220;-map_channel&#8221; option specifies the order of the channels in the output stream. The output channel layout is guessed from the number of channels mapped (mono if one &#8220;-map_channel&#8221;, stereo if two, etc.). Using &#8220;-ac&#8221; in combination of &#8220;-map_channel&#8221; makes the channel gain levels to be updated if input and output channel layouts don&#8217;t match (for instance two &#8220;-map_channel&#8221; options and &#8220;-ac 6&#8221;). </p>
<p> You can also extract each channel of an input to specific outputs; the following command extracts two channels of the <i></i><font SIZE="-1"><i>INPUT</i></font><i></i> audio stream (file 0, stream 0) to the respective <i></i><font SIZE="-1"><i>OUTPUT_CH0</i></font><i></i> and <i></i><font SIZE="-1"><i>OUTPUT_CH1</i></font><i></i> outputs: </p>
<pre>
        ffmpeg -i INPUT -map_channel 0.0.0 OUTPUT_CH0 -map_channel 0.0.1 OUTPUT_CH1
</pre>
<p> The following example splits the channels of a stereo input into two separate streams, which are put into the same output file: </p>
<pre>
        ffmpeg -i stereo.wav -map 0:0 -map 0:0 -map_channel 0.0.0:0.0 -map_channel 0.0.1:0.1 -y out.ogg
</pre>
<p> Note that currently each output stream can only contain channels from a single input stream; you can&#8217;t for example use &#8220;-map_channel&#8221; to pick multiple input audio channels contained in different streams (from the same or different files) and merge them into a single output stream. It is therefore not currently possible, for example, to turn two separate mono streams into a single stereo stream. However splitting a stereo stream into two single channel mono streams is possible. </p>
<p> If you need this feature, a possible workaround is to use the <i>amerge</i> filter. For example, if you need to merge a media (here <i>input.mkv</i>) with 2 mono audio streams into one single stereo channel audio stream (and keep the video stream), you can use the following command: </p>
<p>ffmpeg &#8211; i input.mkv &#8211; filter_complex &#8220;[0:1] [0:2] amerge&#8221; &#8211; c : a pcm_s16le &#8211; c : v copy output.mkv</p>
<p> To map the first two audio channels from the first input, and using the trailing <tt>&quot;?&quot;</tt>, ignore the audio channel mapping if the first input is mono instead of stereo: </p>
<pre>
        ffmpeg -i INPUT -map_channel 0.0.0 -map_channel 0.0.1? OUTPUT
</pre>
<dt><code>-map_metadata[:</code><i>metadata_spec_out</i><code>]</code> <i>infile</i><code>[:</code><i>metadata_spec_in</i><code>] (</code><i>output,per-metadata</i><code>)</code></p>
<dd> Set metadata information of the next output file from <i>infile</i>. Note that those are file indices (zero-based), not filenames. Optional <i>metadata_spec_in/out</i> parameters specify, which metadata to copy. A metadata specifier can have the following forms:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>g</i></p>
<dd> global metadata, i.e. metadata that applies to the whole file</p>
<dt><i>s</i><code>[:</code><i>stream_spec</i><code>]</code></p>
<dd> per-stream metadata. <i>stream_spec</i> is a stream specifier as described in the <code>Stream specifiers</code> chapter. In an input metadata specifier, the first matching stream is copied from. In an output metadata specifier, all matching streams are copied to.</p>
<dt><i>c</i><code>:</code><i>chapter_index</i></p>
<dd> per-chapter metadata. <i>chapter_index</i> is the zero-based chapter index.</p>
<dt><i>p</i><code>:</code><i>program_index</i></p>
<dd> per-program metadata. <i>program_index</i> is the zero-based program index.</dl>
</dl>
<dl>
<dt>
<dd>
<p> If metadata specifier is omitted, it defaults to global. </p>
<p> By default, global metadata is copied from the first input file, per-stream and per-chapter metadata is copied along with streams/chapters. These default mappings are disabled by creating any mapping of the relevant type. A negative file index can be used to create a dummy mapping that just disables automatic copying. </p>
<p> For example to copy metadata from the first stream of the input file to global metadata of the output file: </p>
<pre>
        ffmpeg -i in.ogg -map_metadata 0:s:0 out.mp3
</pre>
<p> To do the reverse, i.e. copy global metadata to all audio streams: </p>
<pre>
        ffmpeg -i in.mkv -map_metadata:s:a 0:g out.mkv
</pre>
<p> Note that simple <tt>0</tt> would work as well in this example, since global metadata is assumed by default.</dl>
<dt><code>-map_chapters</code> <i>input_file_index</i> <code>(</code><i>output</i><code>)</code></p>
<dd> Copy chapters from input file with index <i>input_file_index</i> to the next output file. If no chapter mapping is specified, then chapters are copied from the first input file with at least one chapter. Use a negative file index to disable any chapter copying.</p>
<dt><code>-benchmark (</code><i>global</i><code>)</code></p>
<dd> Show benchmarking information at the end of an encode. Shows real, system and user time used and maximum memory consumption. Maximum memory consumption is not supported on all systems, it will usually display as 0 if not supported.</p>
<dt><code>-benchmark_all (</code><i>global</i><code>)</code></p>
<dd> Show benchmarking information during the encode. Shows real, system and user time used in various steps (audio/video encode/decode).</p>
<dt><code>-timelimit</code> <i>duration</i> <code>(</code><i>global</i><code>)</code></p>
<dd> Exit after ffmpeg has been running for <i>duration</i> seconds in <font SIZE="-1">CPU</font> user time.</p>
<dt><code>-dump (</code><i>global</i><code>)</code></p>
<dd> Dump each input packet to stderr.</p>
<dt><code>-hex (</code><i>global</i><code>)</code></p>
<dd> When dumping packets, also dump the payload.</p>
<dt><code>-re (</code><i>input</i><code>)</code></p>
<dd> Read input at native frame rate. Mainly used to simulate a grab device, or live input stream (e.g. when reading from a file). Should not be used with actual grab devices or live input streams (where it can cause packet loss). By default <code>ffmpeg</code> attempts to read the input(s) as fast as possible. This option will slow down the reading of the input(s) to the native frame rate of the input(s). It is useful for real-time output (e.g. live streaming).</p>
<dt><code>-vsync</code> <i>parameter</i></p>
<dd> Video sync method. For compatibility reasons old values can be specified as numbers. Newly added values will have to be specified as strings always.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>0, passthrough</code></p>
<dd> Each frame is passed with its timestamp from the demuxer to the muxer.</p>
<dt><code>1, cfr</code></p>
<dd> Frames will be duplicated and dropped to achieve exactly the requested constant frame rate.</p>
<dt><code>2, vfr</code></p>
<dd> Frames are passed through with their timestamp or dropped so as to prevent 2 frames from having the same timestamp.</p>
<dt><code>drop</code></p>
<dd> As passthrough but destroys all timestamps, making the muxer generate fresh timestamps based on frame-rate.</p>
<dt><code>-1, auto</code></p>
<dd> Chooses between 1 and 2 depending on muxer capabilities. This is the default method.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Note that the timestamps may be further modified by the muxer, after this. For example, in the case that the format option <code>avoid_negative_ts</code> is enabled. </p>
<p> With -map you can select from which stream the timestamps should be taken. You can leave either video or audio unchanged and sync the remaining stream(s) to the unchanged one.</dl>
<dt><code>-frame_drop_threshold</code> <i>parameter</i></p>
<dd> Frame drop threshold, which specifies how much behind video frames can be before they are dropped. In frame rate units, so 1.0 is one frame. The default is -1.1. One possible usecase is to avoid framedrops in case of noisy timestamps or to increase frame drop precision in case of exact timestamps.</p>
<dt><code>-async</code> <i>samples_per_second</i></p>
<dd> Audio sync method. &#8220;Stretches/squeezes&#8221; the audio stream to match the timestamps, the parameter is the maximum samples per second by which the audio is changed. -async 1 is a special case where only the start of the audio stream is corrected without any later correction. </p>
<p> Note that the timestamps may be further modified by the muxer, after this. For example, in the case that the format option <code>avoid_negative_ts</code> is enabled. </p>
<p> This option has been deprecated. Use the <tt>&quot;aresample&quot;</tt> audio filter instead.</p>
<dt><code>-adrift_threshold</code> <i>time</i></p>
<dd> Set the minimum difference between timestamps and audio data (in seconds) to trigger adding/dropping samples to make it match the timestamps. This option effectively is a threshold to select between hard (add/drop) and soft (squeeze/stretch) compensation. <tt>&quot;-async&quot;</tt> must be set to a positive value.</p>
<dt><code>-apad</code> <i>parameters</i> <code>(</code><i>output,per-stream</i><code>)</code></p>
<dd> Pad the output audio stream(s). This is the same as applying <tt>&quot;-af apad&quot;</tt>. Argument is a string of filter parameters composed the same as with the <tt>&quot;apad&quot;</tt> filter. <tt>&quot;-shortest&quot;</tt> must be set for this output for the option to take effect.</p>
<dt><code>-copyts</code></p>
<dd> Do not process input timestamps, but keep their values without trying to sanitize them. In particular, do not remove the initial start time offset value. </p>
<p> Note that, depending on the <code>vsync</code> option or on specific muxer processing (e.g. in case the format option <code>avoid_negative_ts</code> is enabled) the output timestamps may mismatch with the input timestamps even when this option is selected.</p>
<dt><code>-start_at_zero</code></p>
<dd> When used with <code>copyts</code>, shift input timestamps so they start at zero. </p>
<p> This means that using e.g. <tt>&quot;-ss 50&quot;</tt> will make output timestamps start at 50 seconds, regardless of what timestamp the input file started at.</p>
<dt><code>-copytb</code> <i>mode</i></p>
<dd> Specify how to set the encoder timebase when stream copying. <i>mode</i> is an integer numeric value, and can assume one of the following values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>1</code></p>
<dd> Use the demuxer timebase. </p>
<p> The time base is copied to the output encoder from the corresponding input demuxer. This is sometimes required to avoid non monotonically increasing timestamps when copying video streams with variable frame rate.</p>
<dt><code>0</code></p>
<dd> Use the decoder timebase. </p>
<p> The time base is copied to the output encoder from the corresponding input decoder.</p>
<dt><code>-1</code></p>
<dd> Try to make the choice automatically, in order to generate a sane output.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Default value is -1.</dl>
<dt><code>-enc_time_base[:</code><i>stream_specifier</i><code>]</code> <i>timebase</i> <code>(</code><i>output,per-stream</i><code>)</code></p>
<dd> Set the encoder timebase. <i>timebase</i> is a floating point number, and can assume one of the following values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>0</code></p>
<dd> Assign a default value according to the media type. </p>
<p> For video &#8211; use 1/framerate, for audio &#8211; use 1/samplerate.</p>
<dt><code>-1</code></p>
<dd> Use the input stream timebase when possible. </p>
<p> If an input stream is not available, the default timebase will be used.</p>
<dt><code>&gt;0</code></p>
<dd> Use the provided number as the timebase. </p>
<p> This field can be provided as a ratio of two integers (e.g. 1:24, 1:48000) or as a floating point number (e.g. 0.04166, 2.0833e-5)</dl>
</dl>
<dl>
<dt>
<dd>
<p> Default value is 0.</dl>
<dt><code>-bitexact (</code><i>input/output</i><code>)</code></p>
<dd> Enable bitexact mode for (de)muxer and (de/en)coder</p>
<dt><code>-shortest (</code><i>output</i><code>)</code></p>
<dd> Finish encoding when the shortest input stream ends.</p>
<dt><code>-dts_delta_threshold</code></p>
<dd> Timestamp discontinuity delta threshold.</p>
<dt><code>-dts_error_threshold</code> <i>seconds</i></p>
<dd> Timestamp error delta threshold. This threshold use to discard crazy/damaged timestamps and the default is 30 hours which is arbitrarily picked and quite conservative.</p>
<dt><code>-muxdelay</code> <i>seconds</i> <code>(</code><i>output</i><code>)</code></p>
<dd> Set the maximum demux-decode delay.</p>
<dt><code>-muxpreload</code> <i>seconds</i> <code>(</code><i>output</i><code>)</code></p>
<dd> Set the initial demux-decode delay.</p>
<dt><code>-streamid</code> <i>output-stream-index</i><code>:</code><i>new-value</i> <code>(</code><i>output</i><code>)</code></p>
<dd> Assign a new stream-id value to an output stream. This option should be specified prior to the output filename to which it applies. For the situation where multiple output files exist, a streamid may be reassigned to a different value. </p>
<p> For example, to set the stream 0 <font SIZE="-1">PID</font> to 33 and the stream 1 <font SIZE="-1">PID</font> to 36 for an output mpegts file: </p>
<pre>
        ffmpeg -i inurl -streamid 0:33 -streamid 1:36 out.ts
</pre>
<dt><code>-bsf[:</code><i>stream_specifier</i><code>]</code> <i>bitstream_filters</i> <code>(</code><i>output,per-stream</i><code>)</code></p>
<dd> Set bitstream filters for matching streams. <i>bitstream_filters</i> is a comma-separated list of bitstream filters. Use the <tt>&quot;-bsfs&quot;</tt> option to get the list of bitstream filters. </p>
<pre>
        ffmpeg -i h264.mp4 -c:v copy -bsf:v h264_mp4toannexb -an out.h264
        
        ffmpeg -i file.mov -an -vn -bsf:s mov2textsub -c:s copy -f rawvideo sub.txt
</pre>
<dt><code>-tag[:</code><i>stream_specifier</i><code>]</code> <i>codec_tag</i> <code>(</code><i>input/output,per-stream</i><code>)</code></p>
<dd> Force a tag/fourcc for matching streams.</p>
<dt><code>-timecode</code> <i>hh</i><code>:</code><i>mm</i><code>:</code><i>ss</i><font SIZE="-1"><code>SEP</code></font><i>ff</i></p>
<dd> Specify Timecode for writing. <i></i><font SIZE="-1"><i>SEP</i></font><i></i> is &#8216;:&#8217; for non drop timecode and &#8216;;&#8217; (or &#8216;.&#8217;) for drop. </p>
<pre>
        ffmpeg -i input.mpg -timecode 01:02:03.04 -r 30000/1001 -s ntsc output.mpg
</pre>
<dt><code>-filter_complex</code> <i>filtergraph</i> <code>(</code><i>global</i><code>)</code></p>
<dd> Define a complex filtergraph, i.e. one with arbitrary number of inputs and/or outputs. For simple graphs &#8212; those with one input and one output of the same type &#8212; see the <code>-filter</code> options. <i>filtergraph</i> is a description of the filtergraph, as described in the &#8220;Filtergraph syntax&#8221; section of the ffmpeg-filters manual. </p>
<p> Input link labels must refer to input streams using the <tt>&quot;[file_index:stream_specifier]&quot;</tt> syntax (i.e. the same as <code>-map</code> uses). If <i>stream_specifier</i> matches multiple streams, the first one will be used. An unlabeled input will be connected to the first unused input stream of the matching type. </p>
<p> Output link labels are referred to with <code>-map</code>. Unlabeled outputs are added to the first output file. </p>
<p> Note that with this option it is possible to use only lavfi sources without normal input files. </p>
<p> For example, to overlay an image over video </p>
<p>ffmpeg &#8211; i video.mkv &#8211; i image.png &#8211; filter_complex &#8216;[0:v][1:v]overlay[out]&#8217; &#8211; map &#8216;[out]&#8217; out.mkv</p>
<p> Here <tt>&quot;[0:v]&quot;</tt> refers to the first video stream in the first input file, which is linked to the first (main) input of the overlay filter. Similarly the first video stream in the second input is linked to the second (overlay) input of overlay. </p>
<p> Assuming there is only one video stream in each input file, we can omit input labels, so the above is equivalent to </p>
<p>ffmpeg &#8211; i video.mkv &#8211; i image.png &#8211; filter_complex &#8216;overlay[out]&#8217; &#8211; map &#8216;[out]&#8217; out.mkv</p>
<p> Furthermore we can omit the output label and the single output from the filter graph will be added to the output file automatically, so we can simply write </p>
<pre>
        ffmpeg -i video.mkv -i image.png -filter_complex 'overlay' out.mkv
</pre>
<p> As a special exception, you can use a bitmap subtitle stream as input: it will be converted into a video with the same size as the largest video in the file, or 720&#215;576 if no video is present. Note that this is an experimental and temporary solution. It will be removed once libavfilter has proper support for subtitles. </p>
<p> For example, to hardcode subtitles on top of a DVB-T recording stored in MPEG-TS format, delaying the subtitles by 1 second: </p>
<pre><code>
ffmpeg - i input.ts - filter_complex '[#0x2ef] setpts=PTS+1/TB [sub] ; [#0x2d0] [sub] overlay' - sn - map '#0x2dc' output.mkv
</code></pre>
<p> (0x2d0, 0x2dc and 0x2ef are the MPEG-TS PIDs of respectively the video, audio and subtitles streams; 0:0, 0:3 and 0:7 would have worked too) </p>
<p> To generate 5 seconds of pure red video using lavfi <tt>&quot;color&quot;</tt> source: </p>
<pre>
        ffmpeg -filter_complex 'color=c=red' -t 5 out.mkv
</pre>
<dt><code>-filter_complex_threads</code> <i>nb_threads</i> <code>(</code><i>global</i><code>)</code></p>
<dd> Defines how many threads are used to process a filter_complex graph. Similar to filter_threads but used for <tt>&quot;-filter_complex&quot;</tt> graphs only. The default is the number of available CPUs.</p>
<dt><code>-lavfi</code> <i>filtergraph</i> <code>(</code><i>global</i><code>)</code></p>
<dd> Define a complex filtergraph, i.e. one with arbitrary number of inputs and/or outputs. Equivalent to <code>-filter_complex</code>.</p>
<dt><code>-filter_complex_script</code> <i>filename</i> <code>(</code><i>global</i><code>)</code></p>
<dd> This option is similar to <code>-filter_complex</code>, the only difference is that its argument is the name of the file from which a complex filtergraph description is to be read.</p>
<dt><code>-accurate_seek (</code><i>input</i><code>)</code></p>
<dd> This option enables or disables accurate seeking in input files with the <code>-ss</code> option. It is enabled by default, so seeking is accurate when transcoding. Use <code>-noaccurate_seek</code> to disable it, which may be useful e.g. when copying some streams and transcoding the others.</p>
<dt><code>-seek_timestamp (</code><i>input</i><code>)</code></p>
<dd> This option enables or disables seeking by timestamp in input files with the <code>-ss</code> option. It is disabled by default. If enabled, the argument to the <code>-ss</code> option is considered an actual timestamp, and is not offset by the start time of the file. This matters only for files which do not start from timestamp 0, such as transport streams.</p>
<dt><code>-thread_queue_size</code> <i>size</i> <code>(</code><i>input</i><code>)</code></p>
<dd> This option sets the maximum number of queued packets when reading from the file or device. With low latency / high rate live streams, packets may be discarded if they are not read in a timely manner; setting this value can force ffmpeg to use a separate input thread and read packets as soon as they arrive. By default ffmpeg only do this if multiple inputs are specified.</p>
<dt><code>-sdp_file</code> <i>file</i> <code>(</code><i>global</i><code>)</code></p>
<dd> Print sdp information for an output stream to <i>file</i>. This allows dumping sdp information when at least one output isn&#8217;t an rtp stream. (Requires at least one of the output formats to be rtp).</p>
<dt><code>-discard (</code><i>input</i><code>)</code></p>
<dd> Allows discarding specific streams or frames from streams. Any input stream can be fully discarded, using value <tt>&quot;all&quot;</tt> whereas selective discarding of frames from a stream occurs at the demuxer and is not supported by all demuxers.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>none</code></p>
<dd> Discard no frame.</p>
<dt><code>default</code></p>
<dd> Default, which discards no frames.</p>
<dt><code>noref</code></p>
<dd> Discard all non-reference frames.</p>
<dt><code>bidir</code></p>
<dd> Discard all bidirectional frames.</p>
<dt><code>nokey</code></p>
<dd> Discard all frames excepts keyframes.</p>
<dt><code>all</code></p>
<dd> Discard all frames.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-abort_on</code> <i>flags</i> <code>(</code><i>global</i><code>)</code></p>
<dd> Stop and abort on various conditions. The following flags are available:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>empty_output</code></p>
<dd> No packets were passed to the muxer, the output is empty.</p>
<dt><code>empty_output_stream</code></p>
<dd> No packets were passed to the muxer in some of the output streams.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-max_error_rate (</code><i>global</i><code>)</code></p>
<dd> Set fraction of decoding frame failures across all inputs which when crossed ffmpeg will return exit code 69. Crossing this threshold does not terminate processing. Range is a floating-point number between 0 to 1. Default is 2/3.</p>
<dt><code>-xerror (</code><i>global</i><code>)</code></p>
<dd> Stop and exit on error</p>
<dt><code>-max_muxing_queue_size</code> <i>packets</i> <code>(</code><i>output,per-stream</i><code>)</code></p>
<dd> When transcoding audio and/or video streams, ffmpeg will not begin writing into the output until it has one packet for each such stream. While waiting for that to happen, packets for other streams are buffered. This option sets the size of this buffer, in packets, for the matching output stream. </p>
<p> The default value of this option should be high enough for most uses, so only touch this option if you are sure that you need it.</p>
<dt><code>-muxing_queue_data_threshold</code> <i>bytes</i> <code>(</code><i>output,per-stream</i><code>)</code></p>
<dd> This is a minimum threshold until which the muxing queue size is not taken into account. Defaults to 50 megabytes per stream, and is based on the overall size of packets passed to the muxer.</p>
<dt><code>-auto_conversion_filters (</code><i>global</i><code>)</code></p>
<dd> Enable automatically inserting format conversion filters in all filter graphs, including those defined by <code>-vf</code>, <code>-af</code>, <code>-filter_complex</code> and <code>-lavfi</code>. If filter format negotiation requires a conversion, the initialization of the filters will fail. Conversions can still be performed by inserting the relevant conversion filter (scale, aresample) in the graph. On by default, to explicitly disable it you need to specify <tt>&quot;-noauto_conversion_filters&quot;</tt>.</dl>
<h3>Preset files</h3>
<p> A preset file contains a sequence of <i>option</i>=<i>value</i> pairs, one for each line, specifying a sequence of options which would be awkward to specify on the command line. Lines starting with the hash (&#8216;#&#8217;) character are ignored and are used to provide comments. Check the <i>presets</i> directory in the FFmpeg source tree for examples. </p>
<p> There are two types of preset files: ffpreset and avpreset files. </p>
<p> <i>ffpreset files</i> </p>
<p> ffpreset files are specified with the <tt>&quot;vpre&quot;</tt>, <tt>&quot;apre&quot;</tt>, <tt>&quot;spre&quot;</tt>, and <tt>&quot;fpre&quot;</tt> options. The <tt>&quot;fpre&quot;</tt> option takes the filename of the preset instead of a preset name as input and can be used for any kind of codec. For the <tt>&quot;vpre&quot;</tt>, <tt>&quot;apre&quot;</tt>, and <tt>&quot;spre&quot;</tt> options, the options specified in a preset file are applied to the currently selected codec of the same type as the preset option. </p>
<p> The argument passed to the <tt>&quot;vpre&quot;</tt>, <tt>&quot;apre&quot;</tt>, and <tt>&quot;spre&quot;</tt> preset options identifies the preset file to use according to the following rules: </p>
<p> First ffmpeg searches for a file named <i>arg</i>.ffpreset in the directories <i></i>$FFMPEG_DATADIR<i></i> (if set), and <i></i>$HOME<i>/.ffmpeg</i>, and in the datadir defined at configuration time (usually <i>PREFIX/share/ffmpeg</i>) or in a <i>ffpresets</i> folder along the executable on win32, in that order. For example, if the argument is <tt>&quot;libvpx-1080p&quot;</tt>, it will search for the file <i>libvpx-1080p.ffpreset</i>. </p>
<p> If no such file is found, then ffmpeg will search for a file named <i>codec_name</i>&#8211;<i>arg</i>.ffpreset in the above-mentioned directories, where <i>codec_name</i> is the name of the codec to which the preset file options will be applied. For example, if you select the video codec with <tt>&quot;-vcodec libvpx&quot;</tt> and use <tt>&quot;-vpre 1080p&quot;</tt>, then it will search for the file <i>libvpx-1080p.ffpreset</i>. </p>
<p> <i>avpreset files</i> </p>
<p> avpreset files are specified with the <tt>&quot;pre&quot;</tt> option. They work similar to ffpreset files, but they only allow encoder- specific options. Therefore, an <i>option</i>=<i>value</i> pair specifying an encoder cannot be used. </p>
<p> When the <tt>&quot;pre&quot;</tt> option is specified, ffmpeg will look for files with the suffix .avpreset in the directories <i></i>$AVCONV_DATADIR<i></i> (if set), and <i></i>$HOME<i>/.avconv</i>, and in the datadir defined at configuration time (usually <i>PREFIX/share/ffmpeg</i>), in that order. </p>
<p> First ffmpeg searches for a file named <i>codec_name</i>&#8211;<i>arg</i>.avpreset in the above-mentioned directories, where <i>codec_name</i> is the name of the codec to which the preset file options will be applied. For example, if you select the video codec with <tt>&quot;-vcodec libvpx&quot;</tt> and use <tt>&quot;-pre 1080p&quot;</tt>, then it will search for the file <i>libvpx-1080p.avpreset</i>. </p>
<p> If no such file is found, then ffmpeg will search for a file named <i>arg</i>.avpreset in the same directories.</p>
<h2>EXAMPLES</h2>
<h3>Video and Audio grabbing</h3>
<p> If you specify the input format and device then ffmpeg can grab video and audio directly. </p>
<pre>
        ffmpeg -f oss -i /dev/dsp -f video4linux2 -i /dev/video0 /tmp/out.mpg
</pre>
<p> Or with an <font SIZE="-1">ALSA</font> audio source (mono input, card id 1) instead of <font SIZE="-1">OSS:</font> </p>
<pre>
        ffmpeg -f alsa -ac 1 -i hw:1 -f video4linux2 -i /dev/video0 /tmp/out.mpg
</pre>
<p> Note that you must activate the right video source and channel before launching ffmpeg with any <font SIZE="-1">TV</font> viewer such as &lt;<code><a rel="nofollow" href="http://linux.bytesex.org/xawtv/">http://linux.bytesex.org/xawtv/</a></code>&gt; by Gerd Knorr. You also have to set the audio recording levels correctly with a standard mixer.</p>
<h3>X11 grabbing</h3>
<p> Grab the X11 display with ffmpeg via </p>
<pre>
        ffmpeg -f x11grab -video_size cif -framerate 25 -i :0.0 /tmp/out.mpg
</pre>
<p> 0.0 is display.screen number of your X11 server, same as the <font SIZE="-1">DISPLAY</font> environment variable. </p>
<pre>
        ffmpeg -f x11grab -video_size cif -framerate 25 -i :0.0+10,20 /tmp/out.mpg
</pre>
<p> 0.0 is display.screen number of your X11 server, same as the <font SIZE="-1">DISPLAY</font> environment variable. 10 is the x-offset and 20 the y-offset for the grabbing.</p>
<h3>Video and Audio file format conversion</h3>
<p> Any supported file format and protocol can serve as input to ffmpeg: </p>
<p> Examples:</p>
<dl>
<dt>&bull;</p>
<dd> You can use <font SIZE="-1">YUV</font> files as input: </p>
<pre>
        ffmpeg -i /tmp/test%d.Y /tmp/out.mpg
</pre>
<p> It will use the files: </p>
<pre>
        /tmp/test0.Y, /tmp/test0.U, /tmp/test0.V,
        /tmp/test1.Y, /tmp/test1.U, /tmp/test1.V, etc...
</pre>
<p> The Y files use twice the resolution of the U and V files. They are raw files, without header. They can be generated by all decent video decoders. You must specify the size of the image with the <code>-s</code> option if ffmpeg cannot guess it.</p>
<dt>&bull;</p>
<dd> You can input from a raw <font SIZE="-1">YUV420P</font> file: </p>
<pre>
        ffmpeg -i /tmp/test.yuv /tmp/out.avi
</pre>
<p> test.yuv is a file containing raw <font SIZE="-1">YUV</font> planar data. Each frame is composed of the Y plane followed by the U and V planes at half vertical and horizontal resolution.</p>
<dt>&bull;</p>
<dd> You can output to a raw <font SIZE="-1">YUV420P</font> file: </p>
<pre>
        ffmpeg -i mydivx.avi hugefile.yuv
</pre>
<dt>&bull;</p>
<dd> You can set several input files and output files: </p>
<pre>
        ffmpeg -i /tmp/a.wav -s 640x480 -i /tmp/a.yuv /tmp/a.mpg
</pre>
<p> Converts the audio file a.wav and the raw <font SIZE="-1">YUV</font> video file a.yuv to <font SIZE="-1">MPEG</font> file a.mpg.</p>
<dt>&bull;</p>
<dd> You can also do audio and video conversions at the same time: </p>
<pre>
        ffmpeg -i /tmp/a.wav -ar 22050 /tmp/a.mp2
</pre>
<p> Converts a.wav to <font SIZE="-1">MPEG</font> audio at 22050 Hz sample rate.</p>
<dt>&bull;</p>
<dd> You can encode to several formats at the same time and define a mapping from input stream to output streams: </p>
<pre>
        ffmpeg -i /tmp/a.wav -map 0:a -b:a 64k /tmp/a.mp2 -map 0:a -b:a 128k /tmp/b.mp2
</pre>
<p> Converts a.wav to a.mp2 at 64 kbits and to b.mp2 at 128 kbits. &#8216;-map file:index&#8217; specifies which input stream is used for each output stream, in the order of the definition of output streams.</p>
<dt>&bull;</p>
<dd> You can transcode decrypted VOBs: </p>
<pre>
        ffmpeg -i snatch_1.vob -f avi -c:v mpeg4 -b:v 800k -g 300 -bf 2 -c:a libmp3lame -b:a 128k snatch.avi
</pre>
<p> This is a typical <font SIZE="-1">DVD</font> ripping example; the input is a <font SIZE="-1">VOB</font> file, the output an <font SIZE="-1">AVI</font> file with <font SIZE="-1">MPEG-4</font> video and <font SIZE="-1">MP3</font> audio. Note that in this command we use B-frames so the <font SIZE="-1">MPEG-4</font> stream is DivX5 compatible, and <font SIZE="-1">GOP</font> size is 300 which means one intra frame every 10 seconds for 29.97fps input video. Furthermore, the audio stream is MP3-encoded so you need to enable <font SIZE="-1">LAME</font> support by passing <tt>&quot;--enable-libmp3lame&quot;</tt> to configure. The mapping is particularly useful for <font SIZE="-1">DVD</font> transcoding to get the desired audio language. </p>
<p> <font SIZE="-1">NOTE:</font> To see the supported input formats, use <tt>&quot;ffmpeg -demuxers&quot;</tt>.</p>
<dt>&bull;</p>
<dd> You can extract images from a video, or create a video from many images: </p>
<p> For extracting images from a video: </p>
<pre>
        ffmpeg -i foo.avi -r 1 -s WxH -f image2 foo-%03d.jpeg
</pre>
<p> This will extract one video frame per second from the video and will output them in files named <i>foo-001.jpeg</i>, <i>foo-002.jpeg</i>, etc. Images will be rescaled to fit the new WxH values. </p>
<p> If you want to extract just a limited number of frames, you can use the above command in combination with the <tt>&quot;-frames:v&quot;</tt> or <tt>&quot;-t&quot;</tt> option, or in combination with -ss to start extracting from a certain point in time. </p>
<p> For creating a video from many images: </p>
<pre>
        ffmpeg -f image2 -framerate 12 -i foo-%03d.jpeg -s WxH foo.avi
</pre>
<p> The syntax <tt>&quot;foo-%03d.jpeg&quot;</tt> specifies to use a decimal number composed of three digits padded with zeroes to express the sequence number. It is the same syntax supported by the C printf function, but only formats accepting a normal integer are suitable. </p>
<p> When importing an image sequence, -i also supports expanding shell-like wildcard patterns (globbing) internally, by selecting the image2-specific <tt>&quot;-pattern_type glob&quot;</tt> option. </p>
<p> For example, for creating a video from filenames matching the glob pattern <tt>&quot;foo-*.jpeg&quot;</tt>: </p>
<pre>
        ffmpeg -f image2 -pattern_type glob -framerate 12 -i 'foo-*.jpeg' -s WxH foo.avi
</pre>
<dt>&bull;</p>
<dd> You can put many streams of the same type in the output: </p>
<pre>
        ffmpeg -i test1.avi -i test2.avi -map 1:1 -map 1:0 -map 0:1 -map 0:0 -c copy -y test12.nut
</pre>
<p> The resulting output file <i>test12.nut</i> will contain the first four streams from the input files in reverse order.</p>
<dt>&bull;</p>
<dd> To force <font SIZE="-1">CBR</font> video output: </p>
<pre>
        ffmpeg -i myfile.avi -b 4000k -minrate 4000k -maxrate 4000k -bufsize 1835k out.m2v
</pre>
<dt>&bull;</p>
<dd> The four options lmin, lmax, mblmin and mblmax use &#8216;lambda&#8217; units, but you may use the <font SIZE="-1">QP2LAMBDA</font> constant to easily convert from &#8216;q&#8217; units: </p>
<pre>
        ffmpeg -i src.ext -lmax 21*QP2LAMBDA dst.ext
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ffmpeg-all/">ffmpeg-all</a></code>(1), <code><a href="/docs/linux/man/1-ffplay/">ffplay</a></code>(1), <code><a href="/docs/linux/man/1-ffprobe/">ffprobe</a></code>(1), <code><a href="/docs/linux/man/1-ffmpeg-utils/">ffmpeg-utils</a></code>(1), <code><a href="/docs/linux/man/1-ffmpeg-scaler/">ffmpeg-scaler</a></code>(1), <code><a href="/docs/linux/man/1-ffmpeg-resampler/">ffmpeg-resampler</a></code>(1), <code><a href="/docs/linux/man/1-ffmpeg-codecs/">ffmpeg-codecs</a></code>(1), <code><a href="/docs/linux/man/1-ffmpeg-bitstream-filters/">ffmpeg-bitstream-filters</a></code>(1), <code><a href="/docs/linux/man/1-ffmpeg-formats/">ffmpeg-formats</a></code>(1), <code><a href="/docs/linux/man/1-ffmpeg-devices/">ffmpeg-devices</a></code>(1), <code><a href="/docs/linux/man/1-ffmpeg-protocols/">ffmpeg-protocols</a></code>(1), <code><a href="/docs/linux/man/1-ffmpeg-filters/">ffmpeg-filters</a></code>(1)</p>
<h2>AUTHORS</h2>
<p> The FFmpeg developers. </p>
<p> For details about the authorship, see the Git history of the project (<a href="git://source.ffmpeg.org/ffmpeg">git://source.ffmpeg.org/ffmpeg</a>), e.g. by typing the command <code>git log</code> in the FFmpeg source directory, or browsing the online repository at &lt;<code><a rel="nofollow" href="http://source.ffmpeg.org">http://source.ffmpeg.org</a></code>&gt;. </p>
<p> Maintainers for the specific components are listed in the file <i></i><font SIZE="-1"><i>MAINTAINERS</i></font><i></i> in the source code tree. </p>
<h2>Index</h2>
