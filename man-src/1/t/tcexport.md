---
title: "tcexport(1)"
name: "tcexport"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tcexport/"
description: "tcexport – Simple frontend to transcode’s encoding subsystem"
---

<h2 class="name">NAME</h2>
<p> tcexport &#8211; Simple frontend to transcode&#8217;s encoding subsystem</p>
<h2>SYNOPSIS</h2>
<p> <code>tcexport</code> [ <code>-i</code> <i>video_file</i> ] [ <code>-p</code> <i>audio_file</i> ] [ <code>-o</code> <i>output_file</i> ] [ <code>-c</code> <i>f1-f2[,f3-f4[,&#8230;]]</i> ] [ <code>-N</code> <i>fmt,fmt</i> ] [ <code>-R</code> <i>n[,video_log[,audio_log]]</i> ] [ <code>-P</code> <i>profile[,profile]</i> ] [ <code>-y</code> <i>video_mod,audio_mod,mplex_mod</i> ] [ <code>-w</code> <i>bitrate[,keyint[,crisp]]</i> ] [ <code>-b</code> <i>bitrate[,vbr[,quality[,mode]]]</i> ] [ <code>-D</code> ] [ <code>-d</code> <i>verbosity</i> ] [ <code>-m</code> <i>path</i> ] [ <code>-v</code> ] </p>
<h2>COPYRIGHT</h2>
<p> <code>tcexport</code> is Copyright (C) by Francesco Romani </p>
<h2>DESCRIPTION</h2>
<p> <code>tcexport</code> was designed as a debug tool for transcode&#8217;s encoding code: it fits in a very limited range of usage cases; however, it can also be used independently if you like.<br />
 tcexport encodes and multiplexes a raw YUV4MPEG2/WAV V/A stream using given parameters and transcode encoder components. tecexport provides direct and complete access to transcode&#8217;s encoding features and modules, but hasn&#8217;t any of transcode import/extracting/decoding/filtering capabilities. Use some other tc* tool if you need those facilities.<br />
 tcexport&#8217;s options are intentionally made similar, or identical if feasible, to corresponding transcode&#8217;s encoding options. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i</code> <i>video_file</i></p>
<dd> Specify the path of video source. Only regular files on filesystem are supported. <i>video_file</i> must be a YUV4MPEG2 stream, nothing else is supported.</p>
<dt><code>-p</code> <i>audio_file</i></p>
<dd> Specify the path of audio source. Only regular files on filesystem are supported. <i>audio_file</i> must be a WAVE stream, nothing else is supported.</p>
<dt><code>-o</code> <i>output_file</i></p>
<dd> Specify the (base)path of output file. Some multiplexors (es: raw multiplexor) uses value of this option as an hint to make the final output file(s) (i.e. appending different extensions for A/V streams).</p>
<dt><code>-c </code><i>f1</i>&#8211;<i>f2</i>[,<i>f3</i>&#8211;<i>f4</i>[, &#8230; ] ]</p>
<dd> encode only frames <i>f1-f2</i> [and <i>f3-f4</i> and so on]. Default is to encode all available frames. Use this and you will get statistics about remaining encoding time. The <i>f[N]</i> parameters may also be timecodes in the HH:MM:SS.FRAME format. Example:</p>
<dl>
<dt>
<dd>
<pre>
-c 500-0:5:01,:10:20-1:18:02.1
</pre>
<dl>
<dt>
<dd> Will encode only from frame 500 to 5 minutes and 1 second and from 10 min, 20 sec to 1 hour, 18 min, 2 sec and one frame.</dl>
</dl>
<dt>
<dd> Note that tcexport, ad well as transcode, starts counting frames at <i>0</i> and excludes the last frame specified. That means that &quot;-c 0-100&quot; will encoded 100 frames starting at frame <i>0</i> up to frame <i>99</i></p>
<dt><code>-N</code> <i>video_format,audio_format</i></p>
<dd> Setup the desired <i>encoded</i> video and audio format respectively. You <i>must</i> always use this option since there is some encoder modules (notably encode_ffmpeg) that support a lot of codecs, and tcexport nor modules can automatically choose a sane one not have defaults (yet).</p>
<dt><code>-R </code><i>n</i>[<i>,video_log</i>[<i>,audio_log</i>]]</p>
<dd> enable multi-pass encoding (0-3) [0,divx4.log,pcm.log].</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>0</i> Constant bitrate (CBR) encoding. [default]</p>
<dd> The codec tries to achieve constant bitrate output. This means, each encoded frame is mostly the same size. This type of encoding can help in maintaining constant filling of hardware buffer on set top players or smooth streaming over networks. By the way, Constant bitrate is often obtained sacrifying quality during high motion scenes.</p>
<dt><i>1</i> Variable bitrate encoding: First pass.</p>
<dd> In this mode, the codec analyses the complete sequence in order to collect data that can improve the distribution of bits in a second VBR pass. The collected data is written to second sub argument (default: divx4.log). This data is codec dependant and cannot be used across codecs. It is strongly advised to use the same codec settings for the VBR analysis pass and the VBR encoding pass if you want predictable results.</p>
<dt>
<dd> The video output of the first pass is not of much use and can grow very large. It&#8217;s a good idea to not save the video output to a file but directly to /dev/null. Usually the bitrate is ignored during first pass. Disabling audio export makes sense too, so use -y.</p>
<dt><i>2</i> Variable bitrate encoding: Second pass.</p>
<dd> The first pass allowed the codec collecting data about the complete sequence. During the second pass, the codec will use that data in order to find an efficient bit distribution that respects both the desired bitrate and the natural bitrate curve shape. This ensures a good compromise between quality and desired bitrate.</p>
<dt><i>3</i> Constant quantizer encoding.</p>
<dd> The quantizer is the &quot;compression level&quot; of the picture. The lower the quantizer is, the higher is the quality of the picture. This mode can help in making sure the sequence is encoded at constant quality, but no prediction can be made on the final bitrate. When using this mode, the <code>-w</code> option changes its meaning, it now takes the quantizer ranging from 1 to 31. Note that constant quantizer encoding is not supported with some codecs (notably mpeg1/2/4 with -y ffmpeg).</dl>
</dl>
<dt><code>-P </code><i>profile</i>[,<i>profile</i>]</p>
<dd> select export profile(s) to load. An export profile it&#8217;s just a different, already tuned, set of basic values for tcexport&#8217;s options. Even if isn&#8217;t recomended, an user can always overwrite profile settings just using standard options. export profiles are stackable, just requesting to load multiple profiles separated by commas; if some options are set by more than one profile, the last profile determine their value.</p>
<dt><code>-y </code><i>video_mod</i>,<i>audio_mod</i>,<i>mplex_mod</i></p>
<dd> Select export modules: video and audio encoders, and multiplexor module. You <i>always must</i> select both the encoders and multiplexor, there isn&#8217;t implicit modules. The only exception to this rule is if this option isn&#8217;t used at all: in this case tcexport will use <i>null</i> modules.</p>
<dt><code>-w </code><i>bitrate</i>[,<i>keyint</i>[,<i>crisp</i>]]</p>
<dd> encoder bitrate[,keyframes[,crispness]] [(6000 for MPEG 1/2, 1800 for others),250,100].</p>
<dt><code>-b </code><i>bitrate</i>[,<i>vbr</i>[,<i>quality</i>[,<i>mode</i>]]]</p>
<dd> audio encoder bitrate kBits/s[,vbr[,quality[,mode]]] [128,0,5,0]</p>
<dt><code>-D</code></p>
<dd> Select dry run mode: tcexport will probe stream, load selected modules then exit, without doing anything else.</p>
<dt><code>-d</code> <i>verbosity</i></p>
<dd> Select the verbosity of program, support code and modules. See transcode&#8217;s manpage to see supported verbosity levels. Please note that higher verbosity levels include lower ones, so if You select i.e. TC_DEBUG level you will get TC_DEBUG messages <i>and</i> TC_INFO messages. Please also note that high verbosity levels will output <i>a lot</i> of messages.</p>
<dt><code>-m</code> <i>path</i></p>
<dd> Look in <i>Path</i> instead of the compiled-in module path for a module.</p>
<dt><code>-v</code></p>
<dd> Print version information and exit. </p>
</dl>
<h2>RETURN VALUES</h2>
<p> <code>tcexport</code> uses following return values: </p>
<p>&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>successfull </p>
<p>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>bad parameter or command line option </p>
<p>&nbsp;<wbr>2&nbsp;<wbr>&nbsp;<wbr>error while reading/writing from/to a file </p>
<p>&nbsp;<wbr>3&nbsp;<wbr>&nbsp;<wbr>requested an inexistent&nbsp;<wbr>(or unreadable)&nbsp;<wbr>module </p>
<p>&nbsp;<wbr>4&nbsp;<wbr>&nbsp;<wbr>a module raised an internal error </p>
<p>&nbsp;<wbr>5&nbsp;<wbr>&nbsp;<wbr>error while probing input file(s). Make sure they are of right format.<br />
 64 internal error. Please provide a report of what&#8217;s happened on transcode-devel mailing list </p>
<h2>AUTHORS</h2>
<p> <code>tcexport</code> was written by Francesco Romani<br />
 &lt;fromani [at] gmail.com&gt; with contributions from the Transcode Team and many others. See AUTHORS for details. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tccat/">tccat</a></code>(1), <code><a href="/docs/linux/man/1-tcdecode/">tcdecode</a></code>(1), <code><a href="/docs/linux/man/1-tcdemux/">tcdemux</a></code>(1), <code><a href="/docs/linux/man/1-tcextract/">tcextract</a></code>(1), <code><a href="/docs/linux/man/1-tcprobe/">tcprobe</a></code>(1), <code><a href="/docs/linux/man/1-transcode/">transcode</a></code>(1) <code><a href="/docs/linux/man/1-tcmodinfo/">tcmodinfo</a></code>(1) </p>
<h2>Index</h2>
