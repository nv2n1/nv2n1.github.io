---

title: "ffmpeg-bitstream-filters(1)"
name: "ffmpeg-bitstream-filters"
section: "1"
letter: "f"
url: "/docs/linux/man/1-ffmpeg-bitstream-filters/"
description: "ffmpeg-bitstream-filters – FFmpeg bitstream filters"
---

<p> This document describes the bitstream filters provided by the libavcodec library. </p>
<p> A bitstream filter operates on the encoded stream data, and performs bitstream level modifications without performing decoding.</p>
<h2>BITSTREAM FILTERS</h2>
<p> When you configure your FFmpeg build, all the supported bitstream filters are enabled by default. You can list all available ones using the configure option <tt>&quot;--list-bsfs&quot;</tt>. </p>
<p> You can disable all the bitstream filters using the configure option <tt>&quot;--disable-bsfs&quot;</tt>, and selectively enable any bitstream filter using the option <tt>&quot;--enable-bsf=BSF&quot;</tt>, or you can disable a particular bitstream filter using the option <tt>&quot;--disable-bsf=BSF&quot;</tt>. </p>
<p> The option <tt>&quot;-bsfs&quot;</tt> of the ff* tools will display the list of all the supported bitstream filters included in your build. </p>
<p> The ff* tools have a -bsf option applied per stream, taking a comma-separated list of filters, whose parameters follow the filter name after a &#8216;=&#8217;. </p>
<pre><code>
ffmpeg - i INPUT - c : v copy - bsf : v filter1 [= opt1 = str1:opt2 = str2][, filter2] OUTPUT
</code></pre>
<p> Below is a description of the currently available bitstream filters, with their parameters, if any.</p>
<h3>aac_adtstoasc</h3>
<p> Convert <font SIZE="-1">MPEG-2/4 AAC ADTS</font> to an <font SIZE="-1">MPEG-4</font> Audio Specific Configuration bitstream. </p>
<p> This filter creates an <font SIZE="-1">MPEG-4</font> AudioSpecificConfig from an <font SIZE="-1">MPEG-2/4 ADTS</font> header and removes the <font SIZE="-1">ADTS</font> header. </p>
<p> This filter is required for example when copying an <font SIZE="-1">AAC</font> stream from a raw <font SIZE="-1">ADTS AAC</font> or an MPEG-TS container to <font SIZE="-1">MP4A-LATM,</font> to an <font SIZE="-1">FLV</font> file, or to <font SIZE="-1">MOV/MP4</font> files and related formats such as 3GP or M4A. Please note that it is auto-inserted for <font SIZE="-1">MP4A-LATM</font> and <font SIZE="-1">MOV/MP4</font> and related formats.</p>
<h3>av1_metadata</h3>
<p> Modify metadata embedded in an <font SIZE="-1">AV1</font> stream.</p>
<dl>
<dt><code>td</code></dt>
<dd> Insert or remove temporal delimiter OBUs in all temporal units of the stream.</dd>
<dl>
<dl>
<dt><code>insert</code></dt>
<dd> Insert a <font SIZE="-1">TD</font> at the beginning of every <font SIZE="-1">TU</font> which does not already have one.</dd>
<dt><code>remove</code></dt>
<dd> Remove the <font SIZE="-1">TD</font> from the beginning of every <font SIZE="-1">TU</font> which has one.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>color_primaries</code></dt>
<dd>
</dd><dt><code>transfer_characteristics</code></dt>
<dd>
</dd><dt><code>matrix_coefficients</code></dt>
<dd> Set the color description fields in the stream (see <font SIZE="-1">AV1</font> section 6.4.2).</dd>
<dt><code>color_range</code></dt>
<dd> Set the color range in the stream (see <font SIZE="-1">AV1</font> section 6.4.2; note that this cannot be set for streams using <font SIZE="-1">BT.709</font> primaries, sRGB transfer characteristic and identity (<font SIZE="-1">RGB</font>) matrix coefficients).</dd>
<dl>
<dl>
<dt><code>tv</code></dt>
<dd> Limited range.</dd>
<dt><code>pc</code></dt>
<dd> Full range.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>chroma_sample_position</code></dt>
<dd> Set the chroma sample location in the stream (see <font SIZE="-1">AV1</font> section 6.4.2). This can only be set for 4:2:0 streams.</dd>
<dl>
<dl>
<dt><code>vertical</code></dt>
<dd> Left position (matching the default in <font SIZE="-1">MPEG-2</font> and H.264).</dd>
<dt><code>colocated</code></dt>
<dd> Top-left position.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>tick_rate</code></dt>
<dd> Set the tick rate (<i>num_units_in_display_tick / time_scale</i>) in the timing info in the sequence header.</dd>
<dt><code>num_ticks_per_picture</code></dt>
<dd> Set the number of ticks in each picture, to indicate that the stream has a fixed framerate. Ignored if <code>tick_rate</code> is not also set.</dd>
<dt><code>delete_padding</code></dt>
<dd> Deletes Padding OBUs.</dd></dl>
<h3>chomp</h3>
<p> Remove zero padding at the end of a packet.</p>
<h3>dca_core</h3>
<p> Extract the core from a <font SIZE="-1">DCA/DTS</font> stream, dropping extensions such as DTS-HD.</p>
<h3>dump_extra</h3>
<p> Add extradata to the beginning of the filtered packets except when said packets already exactly begin with the extradata that is intended to be added.</p>
<dl>
<dt><code>freq</code></dt>
<dd> The additional argument specifies which packets should be filtered. It accepts the values:</dd>
<dl>
<dl>
<dt><code>k</code></dt>
<dd>
</dd><dt><code>keyframe</code></dt>
<dd> add extradata to all key packets</dd>
<dt><code>e</code></dt>
<dd>
</dd><dt><code>all</code></dt>
<dd> add extradata to all packets</dd></dl>
</dl>
<dl>
</dl>
</dl>
<p> If not specified it is assumed <code>k</code>. </p>
<p> For example the following <code>ffmpeg</code> command forces a global header (thus disabling individual packet headers) in the H.264 packets generated by the <tt>&quot;libx264&quot;</tt> encoder, but corrects them by adding the header stored in extradata to the key packets: </p>
<pre>
        ffmpeg -i INPUT -map 0 -flags:v +global_header -c:v libx264 -bsf:v dump_extra out.ts
</pre>
<h3>eac3_core</h3>
<p> Extract the core from a E-AC-3 stream, dropping extra channels.</p>
<h3>extract_extradata</h3>
<p> Extract the in-band extradata. </p>
<p> Certain codecs allow the long-term headers (e.g. <font SIZE="-1">MPEG-2</font> sequence headers, or H.264/HEVC (<font SIZE="-1">VPS/</font>)SPS/PPS) to be transmitted either &#8220;in-band&#8221; (i.e. as a part of the bitstream containing the coded frames) or &#8220;out of band&#8221; (e.g. on the container level). This latter form is called &#8220;extradata&#8221; in FFmpeg terminology. </p>
<p> This bitstream filter detects the in-band headers and makes them available as extradata.</p>
<dl>
<dt><code>remove</code></dt>
<dd> When this option is enabled, the long-term headers are removed from the bitstream after extraction.</dd></dl>
<h3>filter_units</h3>
<p> Remove units with types in or not in a given set from the stream.</p>
<dl>
<dt><code>pass_types</code></dt>
<dd> List of unit types or ranges of unit types to pass through while removing all others. This is specified as a &#8216;|&#8217;-separated list of unit type values or ranges of values with &#8216;-&#8216;.</dd>
<dt><code>remove_types</code></dt>
<dd> Identical to <code>pass_types</code>, except the units in the given set removed and all others passed through.</dd></dl>
<p> Extradata is unchanged by this transformation, but note that if the stream contains inline parameter sets then the output may be unusable if they are removed. </p>
<p> For example, to remove all non-VCL <font SIZE="-1">NAL</font> units from an H.264 stream: </p>
<pre>
        ffmpeg -i INPUT -c:v copy -bsf:v 'filter_units=pass_types=1-5' OUTPUT
</pre>
<p> To remove all AUDs, <font SIZE="-1">SEI</font> and filler from an H.265 stream: </p>
<pre>
        ffmpeg -i INPUT -c:v copy -bsf:v 'filter_units=remove_types=35|38-40' OUTPUT
</pre>
<h3>hapqa_extract</h3>
<p> Extract Rgb or Alpha part of an <font SIZE="-1">HAPQA</font> file, without recompression, in order to create an <font SIZE="-1">HAPQ</font> or an HAPAlphaOnly file.</p>
<dl>
<dt><code>texture</code></dt>
<dd> Specifies the texture to keep.</dd>
<dl>
<dl>
<dt><code>color</code></dt>
<dd>
</dd><dt><code>alpha</code></dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
</dl>
<p> Convert <font SIZE="-1">HAPQA</font> to <font SIZE="-1">HAPQ</font> </p>
<pre>
        ffmpeg -i hapqa_inputfile.mov -c copy -bsf:v hapqa_extract=texture=color -tag:v HapY -metadata:s:v:0 encoder=&quot;HAPQ&quot; hapq_file.mov
</pre>
<p> Convert <font SIZE="-1">HAPQA</font> to HAPAlphaOnly </p>
<pre>
        ffmpeg -i hapqa_inputfile.mov -c copy -bsf:v hapqa_extract=texture=alpha -tag:v HapA -metadata:s:v:0 encoder=&quot;HAPAlpha Only&quot; hapalphaonly_file.mov
</pre>
<h3>h264_metadata</h3>
<p> Modify metadata embedded in an H.264 stream.</p>
<dl>
<dt><code>aud</code></dt>
<dd> Insert or remove <font SIZE="-1">AUD NAL</font> units in all access units of the stream.</dd>
<dl>
<dl>
<dt><code>insert</code></dt>
<dd>
</dd><dt><code>remove</code></dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt><code>sample_aspect_ratio</code></dt>
<dd> Set the sample aspect ratio of the stream in the <font SIZE="-1">VUI</font> parameters.</dd>
<dt><code>overscan_appropriate_flag</code></dt>
<dd> Set whether the stream is suitable for display using overscan or not (see H.264 section E.2.1).</dd>
<dt><code>video_format</code></dt>
<dd>
</dd><dt><code>video_full_range_flag</code></dt>
<dd> Set the video format in the stream (see H.264 section E.2.1 and table E-2).</dd>
<dt><code>colour_primaries</code></dt>
<dd>
</dd><dt><code>transfer_characteristics</code></dt>
<dd>
</dd><dt><code>matrix_coefficients</code></dt>
<dd> Set the colour description in the stream (see H.264 section E.2.1 and tables E-3, E-4 and E-5).</dd>
<dt><code>chroma_sample_loc_type</code></dt>
<dd> Set the chroma sample location in the stream (see H.264 section E.2.1 and figure E-1).</dd>
<dt><code>tick_rate</code></dt>
<dd> Set the tick rate (num_units_in_tick / time_scale) in the <font SIZE="-1">VUI</font> parameters. This is the smallest time unit representable in the stream, and in many cases represents the field rate of the stream (double the frame rate).</dd>
<dt><code>fixed_frame_rate_flag</code></dt>
<dd> Set whether the stream has fixed framerate &#8211; typically this indicates that the framerate is exactly half the tick rate, but the exact meaning is dependent on interlacing and the picture structure (see H.264 section E.2.1 and table E-6).</dd>
<dt><code>crop_left</code></dt>
<dd>
</dd><dt><code>crop_right</code></dt>
<dd>
</dd><dt><code>crop_top</code></dt>
<dd>
</dd><dt><code>crop_bottom</code></dt>
<dd> Set the frame cropping offsets in the <font SIZE="-1">SPS.</font> These values will replace the current ones if the stream is already cropped. </dd>
<p> These fields are set in pixels. Note that some sizes may not be representable if the chroma is subsampled or the stream is interlaced (see H.264 section 7.4.2.1.1).</p>
<dt><code>sei_user_data</code></dt>
<dd> Insert a string as <font SIZE="-1">SEI</font> unregistered user data. The argument must be of the form <i>UUID+string</i>, where the <font SIZE="-1">UUID</font> is as hex digits possibly separated by hyphens, and the string can be anything. </dd>
<p> For example, <code>086f3693-b7b3-4f2c-9653-21492feee5b8+hello</code> will insert the string &#8220;hello&#8221; associated with the given <font SIZE="-1">UUID.</font></p>
<dt><code>delete_filler</code></dt>
<dd> Deletes both filler <font SIZE="-1">NAL</font> units and filler <font SIZE="-1">SEI</font> messages.</dd>
<dt><code>level</code></dt>
<dd> Set the level in the <font SIZE="-1">SPS.</font> Refer to H.264 section A.3 and tables A-1 to A-5. </dd>
<p> The argument must be the name of a level (for example, <code>4.2</code>), a level_idc value (for example, <code>42</code>), or the special name <code>auto</code> indicating that the filter should attempt to guess the level from the input stream properties.</dl>
<h3>h264_mp4toannexb</h3>
<p> Convert an H.264 bitstream from length prefixed mode to start code prefixed mode (as defined in the Annex B of the ITU-T H.264 specification). </p>
<p> This is required by some streaming formats, typically the <font SIZE="-1">MPEG-2</font> transport stream format (muxer <tt>&quot;mpegts&quot;</tt>). </p>
<p> For example to remux an <font SIZE="-1">MP4</font> file containing an H.264 stream to mpegts format with <code>ffmpeg</code>, you can use the command: </p>
<pre>
        ffmpeg -i INPUT.mp4 -codec copy -bsf:v h264_mp4toannexb OUTPUT.ts
</pre>
<p> Please note that this filter is auto-inserted for MPEG-TS (muxer <tt>&quot;mpegts&quot;</tt>) and raw H.264 (muxer <tt>&quot;h264&quot;</tt>) output formats.</p>
<h3>h264_redundant_pps</h3>
<p> This applies a specific fixup to some Blu-ray streams which contain redundant PPSs modifying irrelevant parameters of the stream which confuse other transformations which require correct extradata. </p>
<p> A new single global <font SIZE="-1">PPS</font> is created, and all of the redundant PPSs within the stream are removed.</p>
<h3>hevc_metadata</h3>
<p> Modify metadata embedded in an <font SIZE="-1">HEVC</font> stream.</p>
<dl>
<dt><code>aud</code></dt>
<dd> Insert or remove <font SIZE="-1">AUD NAL</font> units in all access units of the stream.</dd>
<dl>
<dl>
<dt><code>insert</code></dt>
<dd>
</dd><dt><code>remove</code></dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt><code>sample_aspect_ratio</code></dt>
<dd> Set the sample aspect ratio in the stream in the <font SIZE="-1">VUI</font> parameters.</dd>
<dt><code>video_format</code></dt>
<dd>
</dd><dt><code>video_full_range_flag</code></dt>
<dd> Set the video format in the stream (see H.265 section E.3.1 and table E.2).</dd>
<dt><code>colour_primaries</code></dt>
<dd>
</dd><dt><code>transfer_characteristics</code></dt>
<dd>
</dd><dt><code>matrix_coefficients</code></dt>
<dd> Set the colour description in the stream (see H.265 section E.3.1 and tables E.3, E.4 and E.5).</dd>
<dt><code>chroma_sample_loc_type</code></dt>
<dd> Set the chroma sample location in the stream (see H.265 section E.3.1 and figure E.1).</dd>
<dt><code>tick_rate</code></dt>
<dd> Set the tick rate in the <font SIZE="-1">VPS</font> and <font SIZE="-1">VUI</font> parameters (num_units_in_tick / time_scale). Combined with <code>num_ticks_poc_diff_one</code>, this can set a constant framerate in the stream. Note that it is likely to be overridden by container parameters when the stream is in a container.</dd>
<dt><code>num_ticks_poc_diff_one</code></dt>
<dd> Set poc_proportional_to_timing_flag in <font SIZE="-1">VPS</font> and <font SIZE="-1">VUI</font> and use this value to set num_ticks_poc_diff_one_minus1 (see H.265 sections 7.4.3.1 and E.3.1). Ignored if <code>tick_rate</code> is not also set.</dd>
<dt><code>crop_left</code></dt>
<dd>
</dd><dt><code>crop_right</code></dt>
<dd>
</dd><dt><code>crop_top</code></dt>
<dd>
</dd><dt><code>crop_bottom</code></dt>
<dd> Set the conformance window cropping offsets in the <font SIZE="-1">SPS.</font> These values will replace the current ones if the stream is already cropped. </dd>
<p> These fields are set in pixels. Note that some sizes may not be representable if the chroma is subsampled (H.265 section 7.4.3.2.1).</p>
<dt><code>level</code></dt>
<dd> Set the level in the <font SIZE="-1">VPS</font> and <font SIZE="-1">SPS.</font> See H.265 section A.4 and tables A.6 and A.7. </dd>
<p> The argument must be the name of a level (for example, <code>5.1</code>), a <i>general_level_idc</i> value (for example, <code>153</code> for level 5.1), or the special name <code>auto</code> indicating that the filter should attempt to guess the level from the input stream properties.</dl>
<h3>hevc_mp4toannexb</h3>
<p> Convert an <font SIZE="-1">HEVC/H.265</font> bitstream from length prefixed mode to start code prefixed mode (as defined in the Annex B of the ITU-T H.265 specification). </p>
<p> This is required by some streaming formats, typically the <font SIZE="-1">MPEG-2</font> transport stream format (muxer <tt>&quot;mpegts&quot;</tt>). </p>
<p> For example to remux an <font SIZE="-1">MP4</font> file containing an <font SIZE="-1">HEVC</font> stream to mpegts format with <code>ffmpeg</code>, you can use the command: </p>
<pre>
        ffmpeg -i INPUT.mp4 -codec copy -bsf:v hevc_mp4toannexb OUTPUT.ts
</pre>
<p> Please note that this filter is auto-inserted for MPEG-TS (muxer <tt>&quot;mpegts&quot;</tt>) and raw <font SIZE="-1">HEVC/H.265</font> (muxer <tt>&quot;h265&quot;</tt> or <tt>&quot;hevc&quot;</tt>) output formats.</p>
<h3>imxdump</h3>
<p> Modifies the bitstream to fit in <font SIZE="-1">MOV</font> and to be usable by the Final Cut Pro decoder. This filter only applies to the mpeg2video codec, and is likely not needed for Final Cut Pro 7 and newer with the appropriate <code>-tag:v</code>. </p>
<p> For example, to remux 30 MB/sec <font SIZE="-1">NTSC IMX</font> to <font SIZE="-1">MOV:</font> </p>
<pre>
        ffmpeg -i input.mxf -c copy -bsf:v imxdump -tag:v mx3n output.mov
</pre>
<h3>mjpeg2jpeg</h3>
<p> Convert <font SIZE="-1">MJPEG/AVI1</font> packets to full <font SIZE="-1">JPEG/JFIF</font> packets. </p>
<p> <font SIZE="-1">MJPEG</font> is a video codec wherein each video frame is essentially a <font SIZE="-1">JPEG</font> image. The individual frames can be extracted without loss, e.g. by </p>
<pre>
        ffmpeg -i ../some_mjpeg.avi -c:v copy frames_%d.jpg
</pre>
<p> Unfortunately, these chunks are incomplete <font SIZE="-1">JPEG</font> images, because they lack the <font SIZE="-1">DHT</font> segment required for decoding. Quoting from &lt;<code><a rel="nofollow" href="http://www.digitalpreservation.gov/formats/fdd/fdd000063.shtml">http://www.digitalpreservation.gov/formats/fdd/fdd000063.shtml</a></code>&gt;: </p>
<p> Avery Lee, writing in the rec.video.desktop newsgroup in 2001, commented that &#8220;<font SIZE="-1">MJPEG,</font> or at least the <font SIZE="-1">MJPEG</font> in AVIs having the <font SIZE="-1">MJPG</font> fourcc, is restricted <font SIZE="-1">JPEG</font> with a fixed &#8212; and *omitted* &#8212; Huffman table. The <font SIZE="-1">JPEG</font> must be YCbCr colorspace, it must be 4:2:2, and it must use basic Huffman encoding, not arithmetic or progressive. . . . You can indeed extract the <font SIZE="-1">MJPEG</font> frames and decode them with a regular <font SIZE="-1">JPEG</font> decoder, but you have to prepend the <font SIZE="-1">DHT</font> segment to them, or else the decoder won&#8217;t have any idea how to decompress the data. The exact table necessary is given in the OpenDML spec.&#8221; </p>
<p> This bitstream filter patches the header of frames extracted from an <font SIZE="-1">MJPEG</font> stream (carrying the <font SIZE="-1">AVI1</font> header <font SIZE="-1">ID</font> and lacking a <font SIZE="-1">DHT</font> segment) to produce fully qualified <font SIZE="-1">JPEG</font> images. </p>
<pre>
        ffmpeg -i mjpeg-movie.avi -c:v copy -bsf:v mjpeg2jpeg frame_%d.jpg
        exiftran -i -9 frame*.jpg
        ffmpeg -i frame_%d.jpg -c:v copy rotated.avi
</pre>
<h3>mjpegadump</h3>
<p> Add an <font SIZE="-1">MJPEG A</font> header to the bitstream, to enable decoding by Quicktime.</p>
<h3>mov2textsub</h3>
<p> Extract a representable text file from <font SIZE="-1">MOV</font> subtitles, stripping the metadata header from each subtitle packet. </p>
<p> See also the <code>text2movsub</code> filter.</p>
<h3>mp3decomp</h3>
<p> Decompress non-standard compressed <font SIZE="-1">MP3</font> audio headers.</p>
<h3>mpeg2_metadata</h3>
<p> Modify metadata embedded in an <font SIZE="-1">MPEG-2</font> stream.</p>
<dl>
<dt><code>display_aspect_ratio</code></dt>
<dd> Set the display aspect ratio in the stream. </dd>
<p> The following fixed values are supported:</p>
<dl>
<dl>
<dt><code>4/3</code></dt>
<dd>
</dd><dt><code>16/9</code></dt>
<dd>
</dd><dt><code>221/100</code></dt>
<dd></dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> Any other value will result in square pixels being signalled instead (see H.262 section 6.3.3 and table 6-3).</dd></dl>
<dt><code>frame_rate</code></dt>
<dd> Set the frame rate in the stream. This is constructed from a table of known values combined with a small multiplier and divisor &#8211; if the supplied value is not exactly representable, the nearest representable value will be used instead (see H.262 section 6.3.3 and table 6-4).</dd>
<dt><code>video_format</code></dt>
<dd> Set the video format in the stream (see H.262 section 6.3.6 and table 6-6).</dd>
<dt><code>colour_primaries</code></dt>
<dd>
</dd><dt><code>transfer_characteristics</code></dt>
<dd>
</dd><dt><code>matrix_coefficients</code></dt>
<dd> Set the colour description in the stream (see H.262 section 6.3.6 and tables 6-7, 6-8 and 6-9).</dd></dl>
<h3>mpeg4_unpack_bframes</h3>
<p> Unpack DivX-style packed B-frames. </p>
<p> DivX-style packed B-frames are not valid <font SIZE="-1">MPEG-4</font> and were only a workaround for the broken Video for Windows subsystem. They use more space, can cause minor <font SIZE="-1">AV</font> sync issues, require more <font SIZE="-1">CPU</font> power to decode (unless the player has some decoded picture queue to compensate the 2,0,2,0 frame per packet style) and cause trouble if copied into a standard container like mp4 or mpeg-ps/ts, because <font SIZE="-1">MPEG-4</font> decoders may not be able to decode them, since they are not valid <font SIZE="-1">MPEG-4.</font> </p>
<p> For example to fix an <font SIZE="-1">AVI</font> file containing an <font SIZE="-1">MPEG-4</font> stream with DivX-style packed B-frames using <code>ffmpeg</code>, you can use the command: </p>
<pre>
        ffmpeg -i INPUT.avi -codec copy -bsf:v mpeg4_unpack_bframes OUTPUT.avi
</pre>
<h3>noise</h3>
<p> Damages the contents of packets or simply drops them without damaging the container. Can be used for fuzzing or testing error resilience/concealment. </p>
<p> Parameters:</p>
<dl>
<dt><code>amount</code></dt>
<dd> A numeral string, whose value is related to how often output bytes will be modified. Therefore, values below or equal to 0 are forbidden, and the lower the more frequent bytes will be modified, with 1 meaning every byte is modified.</dd>
<dt><code>dropamount</code></dt>
<dd> A numeral string, whose value is related to how often packets will be dropped. Therefore, values below or equal to 0 are forbidden, and the lower the more frequent packets will be dropped, with 1 meaning every packet is dropped.</dd></dl>
<p> The following example applies the modification to every byte but does not drop any packets. </p>
<pre>
        ffmpeg -i INPUT -c copy -bsf noise[=1] output.mkv
</pre>
<h3>null</h3>
<p> This bitstream filter passes the packets through unchanged.</p>
<h3>pcm_rechunk</h3>
<p> Repacketize <font SIZE="-1">PCM</font> audio to a fixed number of samples per packet or a fixed packet rate per second. This is similar to the <code>asetnsamples audio filter</code> but works on audio packets instead of audio frames.</p>
<dl>
<dt><code>nb_out_samples, n</code></dt>
<dd> Set the number of samples per each output audio packet. The number is intended as the number of samples <i>per each channel</i>. Default value is 1024.</dd>
<dt><code>pad, p</code></dt>
<dd> If set to 1, the filter will pad the last audio packet with silence, so that it will contain the same number of samples (or roughly the same number of samples, see <code>frame_rate</code>) as the previous ones. Default value is 1.</dd>
<dt><code>frame_rate, r</code></dt>
<dd> This option makes the filter output a fixed number of packets per second instead of a fixed number of samples per packet. If the audio sample rate is not divisible by the frame rate then the number of samples will not be constant but will vary slightly so that each packet will start as close to the frame boundary as possible. Using this option has precedence over <code>nb_out_samples</code>.</dd></dl>
<p> You can generate the well known 1602-1601-1602-1601-1602 pattern of 48kHz audio for <font SIZE="-1">NTSC</font> frame rate using the <code>frame_rate</code> option. </p>
<pre>
        ffmpeg -f lavfi -i sine=r=48000:d=1 -c pcm_s16le -bsf pcm_rechunk=r=30000/1001 -f framecrc -
</pre>
<h3>prores_metadata</h3>
<p> Modify color property metadata embedded in prores stream.</p>
<dl>
<dt><code>color_primaries</code></dt>
<dd> Set the color primaries. Available values are:</dd>
<dl>
<dl>
<dt><code>auto</code></dt>
<dd> Keep the same color primaries property (default).</dd>
<dt><code>unknown</code></dt>
<dd>
</dd><dt><code>bt709</code></dt>
<dd>
</dd><dt><code>bt470bg</code></dt>
<dd> <font SIZE="-1">BT601 625</font></dd>
<dt><code>smpte170m</code></dt>
<dd> <font SIZE="-1">BT601 525</font></dd>
<dt><code>bt2020</code></dt>
<dd>
</dd><dt><code>smpte431</code></dt>
<dd> <font SIZE="-1">DCI P3</font></dd>
<dt><code>smpte432</code></dt>
<dd> P3 D65</dd></dl>
</dl>
<dl>
</dl>
<dt><code>transfer_characteristics</code></dt>
<dd> Set the color transfer. Available values are:</dd>
<dl>
<dl>
<dt><code>auto</code></dt>
<dd> Keep the same transfer characteristics property (default).</dd>
<dt><code>unknown</code></dt>
<dd>
</dd><dt><code>bt709</code></dt>
<dd> <font SIZE="-1">BT 601, BT 709, BT 2020</font></dd>
<dt><code>smpte2084</code></dt>
<dd> <font SIZE="-1">SMPTE ST 2084</font></dd>
<dt><code>arib-std-b67</code></dt>
<dd> <font SIZE="-1">ARIB STD-B67</font></dd></dl>
</dl>
<dl>
</dl>
<dt><code>matrix_coefficients</code></dt>
<dd> Set the matrix coefficient. Available values are:</dd>
<dl>
<dl>
<dt><code>auto</code></dt>
<dd> Keep the same colorspace property (default).</dd>
<dt><code>unknown</code></dt>
<dd>
</dd><dt><code>bt709</code></dt>
<dd>
</dd><dt><code>smpte170m</code></dt>
<dd> <font SIZE="-1">BT 601</font></dd>
<dt><code>bt2020nc</code></dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
</dl>
<p> Set Rec709 colorspace for each frame of the file </p>
<pre>
        ffmpeg -i INPUT -c copy -bsf:v prores_metadata=color_primaries=bt709:color_trc=bt709:colorspace=bt709 output.mov
</pre>
<p> Set Hybrid Log-Gamma parameters for each frame of the file </p>
<pre>
        ffmpeg -i INPUT -c copy -bsf:v prores_metadata=color_primaries=bt2020:color_trc=arib-std-b67:colorspace=bt2020nc output.mov
</pre>
<h3>remove_extra</h3>
<p> Remove extradata from packets. </p>
<p> It accepts the following parameter:</p>
<dl>
<dt><code>freq</code></dt>
<dd> Set which frame types to remove extradata from.</dd>
<dl>
<dl>
<dt><code>k</code></dt>
<dd> Remove extradata from non-keyframes only.</dd>
<dt><code>keyframe</code></dt>
<dd> Remove extradata from keyframes only.</dd>
<dt><code>e, all</code></dt>
<dd> Remove extradata from all frames.</dd></dl>
</dl>
<dl>
</dl>
</dl>
<h3>setts</h3>
<p> Set <font SIZE="-1">PTS</font> and <font SIZE="-1">DTS</font> in packets. </p>
<p> It accepts the following parameters:</p>
<dl>
<dt><code>ts</code></dt>
<dd>
</dd><dt><code>pts</code></dt>
<dd>
</dd><dt><code>dts</code></dt>
<dd> Set expressions for <font SIZE="-1">PTS, DTS</font> or both.</dd></dl>
<p> The expressions are evaluated through the eval <font SIZE="-1">API</font> and can contain the following constants:</p>
<dl>
<dt><code>N</code></dt>
<dd> The count of the input packet. Starting from 0.</dd>
<dt><font SIZE="-1"><code>TS</code></font></dt>
<dd> The demux timestamp in input in case of <tt>&quot;ts&quot;</tt> or <tt>&quot;dts&quot;</tt> option or presentation timestamp in case of <tt>&quot;pts&quot;</tt> option.</dd>
<dt><font SIZE="-1"><code>POS</code></font></dt>
<dd> The original position in the file of the packet, or undefined if undefined for the current packet</dd>
<dt><font SIZE="-1"><code>DTS</code></font></dt>
<dd> The demux timestamp in input.</dd>
<dt><font SIZE="-1"><code>PTS</code></font></dt>
<dd> The presentation timestamp in input.</dd>
<dt><font SIZE="-1"><code>STARTDTS</code></font></dt>
<dd> The <font SIZE="-1">DTS</font> of the first packet.</dd>
<dt><font SIZE="-1"><code>STARTPTS</code></font></dt>
<dd> The <font SIZE="-1">PTS</font> of the first packet.</dd>
<dt><font SIZE="-1"><code>PREV_INDTS</code></font></dt>
<dd> The previous input <font SIZE="-1">DTS.</font></dd>
<dt><font SIZE="-1"><code>PREV_INPTS</code></font></dt>
<dd> The previous input <font SIZE="-1">PTS.</font></dd>
<dt><font SIZE="-1"><code>PREV_OUTDTS</code></font></dt>
<dd> The previous output <font SIZE="-1">DTS.</font></dd>
<dt><font SIZE="-1"><code>PREV_OUTPTS</code></font></dt>
<dd> The previous output <font SIZE="-1">PTS.</font></dd>
<dt><font SIZE="-1"><code>TB</code></font></dt>
<dd> The timebase of stream packet belongs.</dd>
<dt><font SIZE="-1"><code>SR</code></font></dt>
<dd> The sample rate of stream packet belongs.</dd></dl>
<h3>text2movsub</h3>
<p> Convert text subtitles to <font SIZE="-1">MOV</font> subtitles (as used by the <tt>&quot;mov_text&quot;</tt> codec) with metadata headers. </p>
<p> See also the <code>mov2textsub</code> filter.</p>
<h3>trace_headers</h3>
<p> Log trace output containing all syntax elements in the coded stream headers (everything above the level of individual coded blocks). This can be useful for debugging low-level stream issues. </p>
<p> Supports <font SIZE="-1">AV1, H.264, H.265,</font> (M)JPEG, <font SIZE="-1">MPEG-2</font> and <font SIZE="-1">VP9,</font> but depending on the build only a subset of these may be available.</p>
<h3>truehd_core</h3>
<p> Extract the core from a TrueHD stream, dropping <font SIZE="-1">ATMOS</font> data.</p>
<h3>vp9_metadata</h3>
<p> Modify metadata embedded in a <font SIZE="-1">VP9</font> stream.</p>
<dl>
<dt><code>color_space</code></dt>
<dd> Set the color space value in the frame header. Note that any frame set to <font SIZE="-1">RGB</font> will be implicitly set to <font SIZE="-1">PC</font> range and that <font SIZE="-1">RGB</font> is incompatible with profiles 0 and 2.</dd>
<dl>
<dl>
<dt><code>unknown</code></dt>
<dd>
</dd><dt><code>bt601</code></dt>
<dd>
</dd><dt><code>bt709</code></dt>
<dd>
</dd><dt><code>smpte170</code></dt>
<dd>
</dd><dt><code>smpte240</code></dt>
<dd>
</dd><dt><code>bt2020</code></dt>
<dd>
</dd><dt><code>rgb</code></dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt><code>color_range</code></dt>
<dd> Set the color range value in the frame header. Note that any value imposed by the color space will take precedence over this value.</dd>
<dl>
<dl>
<dt><code>tv</code></dt>
<dd>
</dd><dt><code>pc</code></dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
</dl>
<h3>vp9_superframe</h3>
<p> Merge <font SIZE="-1">VP9</font> invisible (alt-ref) frames back into <font SIZE="-1">VP9</font> superframes. This fixes merging of split/segmented <font SIZE="-1">VP9</font> streams where the alt-ref frame was split from its visible counterpart.</p>
<h3>vp9_superframe_split</h3>
<p> Split <font SIZE="-1">VP9</font> superframes into single frames.</p>
<h3>vp9_raw_reorder</h3>
<p> Given a <font SIZE="-1">VP9</font> stream with correct timestamps but possibly out of order, insert additional show-existing-frame packets to correct the ordering.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ffmpeg/">ffmpeg</a></code>(1), <code><a href="/docs/linux/man/1-ffplay/">ffplay</a></code>(1), <code><a href="/docs/linux/man/1-ffprobe/">ffprobe</a></code>(1), <code><a href="/docs/linux/man/3-libavcodec/">libavcodec</a></code>(3)</p>
<h2>AUTHORS</h2>
<p> The FFmpeg developers. </p>
<p> For details about the authorship, see the Git history of the project (<a href="git://source.ffmpeg.org/ffmpeg">git://source.ffmpeg.org/ffmpeg</a>), e.g. by typing the command <code>git log</code> in the FFmpeg source directory, or browsing the online repository at &lt;<code><a rel="nofollow" href="http://source.ffmpeg.org">http://source.ffmpeg.org</a></code>&gt;. </p>
<p> Maintainers for the specific components are listed in the file <i></i><font SIZE="-1"><i>MAINTAINERS</i></font><i></i> in the source code tree. </p>
