---
title: "mplex(1)"
name: "mplex"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mplex/"
description: "mplex – MPEG 1/2 program/system stream multiplexer"
---

<h2 class="name">NAME</h2>
<p> mplex &#8211; MPEG 1/2 program/system stream multiplexer </p>
<h2>SYNOPSIS</h2>
<p> <code>mplex</code> [<code>-f|&#8211;format</code> <i>format_code</i>] [<code>-i|&#8211;vdr-index]</code> <i>index_pathname</i> [<code>-v|&#8211;verbose</code> <i>num</i>] [<code>-b|&#8211;video-buffer</code> <i>video_buffer_size_kB</i>[, <i>video_buffer_size_kB</i>&#8230;]<i>]</i> [<code>-L|&#8211;lpcm-params</code> <i>params</i>[, <i>params</i>&#8230;<i>]</i>] [<code>-r|&#8211;mux-bitrate</code> <i>muxed_bitrate_kbps</i>] [<code>-l|&#8211;mux-limit</code> <i>num</i>] [<code>-O|&#8211;sync-offset</code> <i>num[</i><code>ms</code>|<code>s</code>|<code>mpt</code>]] [<code>-d|&#8211;subpicture-delay</code> <i>[</i><code>ms</code>|<code>s</code>|<code>mpt|c</code>][:stream-id]<i>[,</i>delay[:stream-id]<i>]</i> [<code>-R|&#8211;run-in</code> <i>num</i>] [<code>-V|&#8211;vbr]</code> [<code>-C|&#8211;cbr]</code> [<code>-s|&#8211;sector-size</code> <i>sector_size_B</i>] [<code>-p|&#8211;packets-per-pack</code> <i>num</i>] [<code>-h|&#8211;system-headers</code>] [<code>-S|&#8211;max-segment-size</code> <i>output_filesize_limit_MB</i>] [<code>-M|&#8211;split-segment]</code> </p>
<p> [<code>-?|&#8211;help</code>] <code>-o|&#8211;output</code><i>&nbsp;<wbr>output_pathname_pattern</i><code>&nbsp;<wbr>input_file&#8230;</code> </p>
<h2>DESCRIPTION</h2>
<p> Mplex is a general-purpose audio/video multiplexer for MPEG-1/MPEG-2. It accepts one or more MPEG-1/2 video stream, MPEG layer I/II/III, DTS, AC3 and LPCM audio streams and multiplexes them into a combined program/system stream according to the constraints specified. Many different types of output structure are supported along with presets for standard VCD and SVCD streams. These latter can be burned to CD using tools such as <code><a href="/docs/linux/man/1-vcdimager/">vcdimager</a></code>(1) and played in stand-alone players. </p>
<p> It is also capable of automatically splitting the output stream into chunks of a specified size either independently or at sequence end/start points in the input video stream.</p>
<h2>GENERAL FUNCTION LETTERS</h2>
<dl>
<dt><code>-o|&#8211;output</code><i>&nbsp;<wbr>output_filename_pattern</i></p>
<dd> This mandatory option sets the pattern for the name(s) of output files. </p>
<p> An integer format code (e.g. %d) in the name is replaced by the number of the file generated (see <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3)).</p>
<dt><code>-v|&#8211;verbose</code><i>&nbsp;<wbr>num</i></p>
<dd> Set verbosity level to <i>num</i>:<br />
&nbsp;<wbr>0 &#8211; warnings and errors only,<br />
&nbsp;<wbr>1 &#8211; information as well,<br />
&nbsp;<wbr>2 &#8211; really verbose.</p>
<dt><code>-?|&#8211;help</code></p>
<dd> Display a synopsis of the command syntax.
</dl>
<h2>FUNCTION LETTERS</h2>
<dl>
<dt><code>-f|&#8211;format</code><i>&nbsp;<wbr>format_code</i></p>
<dd> This command allows one of a number of convenient preset output formats or generic MPEG1 or MPEG2 output to be selected. For the generic formats other function letters can be used to control many aspects of the multiplexed stream. For VCD/SVCD/DVD compliant output the corresponding formats <i>must</i> be used as the standards require the multiplexer to enforce a variety of special constraints on the structure of the output stream.</p>
<dt>
<dd>
&nbsp;<wbr>0 &#8211; Generic MPEG1.&nbsp;<wbr>&nbsp;<wbr>A simple general-purpose MPEG1 format primarily suitable for software decoders. Buffer sizes and VBR must be specified. Bit-rate can be auto-detected.<br />
&nbsp;<wbr>1 &#8211; VCD.&nbsp;<wbr>&nbsp;<wbr>Standard VCD.&nbsp;<wbr>&nbsp;<wbr>Overrides other option settings.<br />
&nbsp;<wbr>2 &#8211; User VCD.&nbsp;<wbr>&nbsp;<wbr>VCD format but buffer size, bit rate and VBR can be set manually.<br />
&nbsp;<wbr>3 &#8211; Generic MPEG2.&nbsp;<wbr>&nbsp;<wbr>Like 0 except MPEG2.<br />
&nbsp;<wbr>4 &#8211; SVCD.&nbsp;<wbr>&nbsp;<wbr>Standard SVCD.&nbsp;<wbr>&nbsp;<wbr>Overrides other option settings.<br />
&nbsp;<wbr>5 &#8211; User-rate SVCD.&nbsp;<wbr>&nbsp;<wbr>SVCD format but buffer size bit rate and VBR can be set.<br />
&nbsp;<wbr>6 &#8211; VCD Stills stream&nbsp;<wbr>(mixed mode with hi-res and standard-res image streams <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> multiplexed are supported).</p>
<p>&nbsp;<wbr>7 &#8211; SVCD Stills stream.<br />
&nbsp;<wbr>8 &#8211; DVD&nbsp;<wbr>(with NAV sectors). Don&#8217;t get too excited.&nbsp;<wbr>&nbsp;<wbr>This is really a<br />
&nbsp;<wbr>very minimal mux format.&nbsp;<wbr>&nbsp;<wbr>It includes empty versions of the peculiar<br />
&nbsp;<wbr>VOBU start sectors DVD VOB&#8217;s include.&nbsp;<wbr>&nbsp;<wbr>This is enough to persuade some<br />
&nbsp;<wbr>hardware players to play the stream but is a long way from full DVD authoring.<br />
&nbsp;<wbr>9 &#8211; DVD.&nbsp;<wbr>&nbsp;<wbr>As above but without the empty VOBU sectors.</p>
<dt><code>-W|&#8211;workarounds</code><i>&nbsp;<wbr>workaround_flag&nbsp;<wbr></i><i>[,</i><i>workaround_flag</i><i>&#8230;]</i></p>
<dd>
 A comma-seperated list of flags that set special work-arounds for what are suspected to be parser Bugs in widely used players. No workarounds are (currently) implemented but history suggests this may change quickly ;-) <code>-i|&#8211;vdr-index</code><i>&nbsp;<wbr>index_pathname</i> This tells mplex to generate an index file for the output in the format used by the &#8216;vdr&#8217; (video disk recorder package). Useful if you want to write output into vdr&#8217;s recordings directory for playback on your video recorder PC. This probably only useful in combination with -f 9.</p>
<dt><code>-r|&#8211;mux-bitrate</code><i>&nbsp;<wbr>num</i></p>
<dd> The total (non VBR) / peak (VBR) bit-rate of the output stream in k Bits/sec. If unspecified and not set by a preset it is automatically calculated from the input stream.</p>
<dt><code>-b|&#8211;video-buffer</code><i>&nbsp;<wbr>numlist</i></p>
<dd> A comma-seperateed list of video decoder buffer sizes in KB for the video streams (given in the order the video streams appear on the command line). The default is 46KB the (tiny) size specified for VCD. The size to use for SVCD is the (more reasonable) 230KB. If you are encoding for a half-decent software decoder it makes sense to push this up to 500K or more.</p>
<dt><code>-L|&#8211;lpcm-params</code></p>
<dd> <i>samples_per_sec:channels:bits_per_sample</i><br />
 [, <i>samples_per_sec:channels:bits_per_sample</i><br />
&nbsp;<wbr>&#8230;]<br />
 A comma-seperated list of paramter sets for the lpcm audio streams (given in the order the lpcm streams appear on the command line). Each parameter set comprises the sampling rate in Hz, the number of channels, and the number of bits per sample seperated by colons. For example, the default 48kHz two-channel 16-bit audio would be specified as 48000:2:16.</p>
<dt>
<dd>
<p> Note: these parameters are necessary because mplex expects raw LPCM audio data without any headers. That is: for each sample point a group of 16,20, or 24 bit amplitude values, one for each channel. Amplitude values are signed with the constituent bytes in big-endian (most significant bytes first) order. For 20 bit samples I am not sure but what documentation I have suggests such samples are padded at the lsb end so that they byte-align at the most significant bits. </p>
<dt><code>-l|&#8211;mux-limit</code><i>&nbsp;<wbr>num</i></p>
<dd> Multiplex limit. Multiplex only the specified number of seconds. Useful for tuning and debugging.</p>
<dt><code>-O|&#8211;sync-offset</code><i>&nbsp;<wbr>num[</i><code>ms</code>|<code>s</code>|<code>mpt</code>|<code>c</code>]</p>
<dd> Set the presentation timestamp offset of video stream w.r.t. audio stream (video-audio) in mSec. This flag is used to produce a stream with synchronised audio/video when one stream started before/after the other. This is common when transcoding as the synchronisation information is typically lost during the (seperate) decoding/encoding of audio and video.</p>
<dt>
<dd> By appending &#8216;s&#8217;, &#8216;ms&#8217; or &#8216;mpt&#8217; the offset can given in seconds, milliseconds or MPEG clock ticks (1/90000th of a second) respectively. If no suffix is given milliseconds are assumed.</p>
<dt><code>-d|&#8211;subpicture-delay</code><i>&nbsp;<wbr>num</i><code>[ms</code>|<code>s|mpt</code>|<code>c</code>]<i>[:stream-id]</i><code>[,</code><i>delay[:stream-id]]</i></p>
<dd> Specify offset of timestamps (video-subpicture) in msec sec, mpt or clock-ticks. If no suffix is given milliseconds are assumed.</p>
<dt>
<dd> The intention of the adding subtitle support was to enable mplex to mux all streams necessary for a DVD so that the mpeg2 stream created can be used directly for further dvd creation. Currently only ps1 streams (like created by tcextract) are supported</p>
<dt>
<dd> Valid subtitle stream are in a range of 32-63 (including). You may want to specify each stream you mplex, use &quot;,&quot; to delimit each stream.</p>
<dt>
<dd> <code>Example:</code> If you want to mux one video, one audio and two subtitle streams having delays of 500 and 1000 ms, the first shall have id 32, the second is 33 (Subtitle streams 0 and 1):</p>
<dt>
<dd> $ mplex -f 8 -o my_mpeg.mpeg -d 500:32,1000:33 video_in.mpv audio_in.m2a subtitle_0.ps1 subtitle_1.ps1</p>
<dt><code>-R|&#8211;run-in</code><i>&nbsp;<wbr>num</i></p>
<dd> Set a non-default run-in (the time data is preloaded into buffers before decoding is scheduled) at the start of each sequence in video frame intervals. By default a run-in matching the specified size of the video and audio buffers in the decoder and the type of multiplexing (constant or variable bit-rate) is selected automatically.</p>
<dt><code>-V|&#8211;vbr</code></p>
<dd> Force variable bit rate multiplexing even if selected profile defaults to constant-bit-rate.</p>
<dt><code>-C||-cbr</code></p>
<dd> Force constant bit rate multiplexing even if selected profile defaults to variable bit-rate.</p>
<dt><code>-s|&#8211;sector-size</code><i>&nbsp;<wbr>num</i></p>
<dd> This option specifies the sector size of the output stream in bytes.</p>
<dt><code>-p|&#8211;packets-per-pack</code><i>&nbsp;<wbr>num</i></p>
<dd> This option specifies the number of packets per pack in the output stream.</p>
<dt><code>-S|&#8211;max-segment-size</code><i>&nbsp;<wbr>num</i></p>
<dd> This option specifies the maximum size of output files in MBytes (2^10) When the limit is reached a new file is started. The default is (0) unlimited.</p>
<dt>
<dd> Note: This option is <i>not</i> for splitting a long video across multiple VCD&#8217;s or SVCD&#8217;s. </p>
<p> It simply splits a single long sequence into in a way that prevents bits of a video GOP(group of pictures) or audio frame being split between chunks. This is fine for formats like that used for DVDs where all stream parameters appear every GOP. However, for VCD / SVCD it won&#8217;t work as the players expect each file to start a new MPEG sequence. </p>
<p> For VCD / SVCD a different technique is used. If mplex encounters a sequence break (sequence end followed by start) in the input video stream it starts a new output stream and file at the sequence start. Thus to split a long video across VCD&#8217;s/SVCD&#8217;s you have to get the MPEG video encoder to introduce sequence splits at the right points (see <a href="/docs/linux/man/1-mpeg2enc/">mpeg2enc</a>(1) for details of how to do this).</p>
<dt><code>-M|&#8211;ignore-seqend-markers</code></p>
<dd> This flag makes mplex ignore sequence end markers embedded in the first video stream instead of switching to a new output file. This is sometimes useful splitting a long stream in files based on a -S limit that doesn&#8217;t need a run-in/run-out like (S)VCD.</p>
<dt><code>-h|&#8211;system-headers</code></p>
<dd> A system header is generated in every pack rather than just in the first.</dl>
<h2>DIAGNOSTIC OUTPUT</h2>
<p> When multiplexing using mplex you may get warning or error messages complaining about buffer underflow. This means that the bit-rate you have specified is simply too low to permit the video and audio to be played back without skipping. The fix is to either reduce the data-rate of the input material or increased the output stream bit-rate.</p>
<h2>BUGS</h2>
<p> The multiplexer should handle MPEG(5.1) audio.</p>
<h2>AUTHOR</h2>
<p> This man page was written by Andrew Stevens.<br />
 If you have questions, remarks, problems or you just want to contact the developers, the main mailing list for the MJPEG-tools is:<br />
&nbsp;<wbr>&nbsp;<wbr><i>mjpeg-users [at] lists.sourceforge.net</i> </p>
<p> For more info, see our website at<br />
&nbsp;<wbr>&nbsp;<wbr><i><a rel="nofollow" href="http://mjpeg.sourceforge.net">http://mjpeg.sourceforge.net</a></i> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mpeg2enc/">mpeg2enc</a></code>(1), <code><a href="/docs/linux/man/1-mp2enc/">mp2enc</a></code>(1), <code><a href="/docs/linux/man/1-lavrec/">lavrec</a></code>(1), <code><a href="/docs/linux/man/1-lavplay/">lavplay</a></code>(1), <code><a href="/docs/linux/man/1-lav2yuv/">lav2yuv</a></code>(1), <code><a href="/docs/linux/man/1-lav2wav/">lav2wav</a></code>(1), <code><a href="/docs/linux/man/1-yuvscaler/">yuvscaler</a></code>(1) </p>
<h2>Index</h2>
