---
title: "transcode(1)"
name: "transcode"
section: "1"
letter: "t"
url: "/docs/linux/man/1-transcode/"
description: "transcode – LINUX video stream processing tool"
---

<h2 class="name">NAME</h2>
<p> transcode &#8211; LINUX video stream processing tool </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>transcode</code> -i&nbsp;<wbr><i>name</i> [-o&nbsp;<wbr><i>name</i>] [-y&nbsp;<wbr><i>vmod,amod</i>] [-w&nbsp;<wbr><i>vbitrate</i>&nbsp;<wbr>[&nbsp;<wbr><i>,vkeyframes</i>&nbsp;<wbr>[&nbsp;<wbr><i>,vcrispness</i>&nbsp;<wbr>]&nbsp;<wbr>]] [-a&nbsp;<wbr><i>atrack</i>&nbsp;<wbr>[&nbsp;<wbr><i>,vtrack</i>&nbsp;<wbr>]] [-b&nbsp;<wbr><i>abitrate</i>&nbsp;<wbr>[&nbsp;<wbr><i>,is_vbr</i>&nbsp;<wbr>[&nbsp;<wbr><i>,quality</i>&nbsp;<wbr>[&nbsp;<wbr><i>,mode</i>&nbsp;<wbr>]&nbsp;<wbr>]&nbsp;<wbr>]] [-M&nbsp;<wbr><i>demuxer_mode</i>] [-F&nbsp;<wbr><i>codec_string</i>] [<i>other</i>&nbsp;<wbr><i>options</i>]</dl>
<h2>QUICK SUMMARY</h2>
<p> <code>transcode</code></p>
<dd>supports a huge range of options, as described in detail in further section. Only one option is mandatory: <code>-i name</code>, for supplying the input main (video) source. All other options are discretionary and they can be skipped. Most commonly needed options are <code>-o</code>, <code>-y</code>, <code>-w</code>, <code>-a</code>, <code>-b</code>, <code>-M</code>, <code>-F</code> and a fair number of transcode session needs a little more than those. See section below for full description of all transcode options. To inspect the properties of a module, such as their parameters or the help text, use the &#8216;tcmodinfo&#8217; tool.</p>
<h2>DESCRIPTION</h2>
<p> <code>transcode</code> is a linux text-console utility for video stream processing, running on a platform that supports shared libraries and threads. </p>
<p> It supports a huge range of options, as described in detail in further section. Only one option is mandatory: <code>-i name</code>, for supplying the input main (video) source. All other options are discretionary and they can be skipped. Most commonly needed options are <code>-o</code>, <code>-y</code>, <code>-w</code>, <code>-a</code>, <code>-b</code>, <code>-M</code>, <code>-F</code> and a fair number of transcode session needs a little more than those. See section below for full description of all transcode options. </p>
<p> Decoding and encoding is done by loading modules that are responsible for feeding transcode with raw video/audio streams (import modules) and encoding the frames (export modules). </p>
<p> It supports elementary video and audio frame transformations, including de-interlacing or fast resizing of video frames and loading of external filters. </p>
<p> A number of modules are included to enable import of DVDs on-the-fly, MPEG elementary (ES) or program streams (VOB), MPEG video, Digital Video (DV), YUV4MPEG streams, NuppelVideo file format, AVI based codecs and raw or compressed (pass-through) video frames and export modules for writing DivX;-), XviD, DivX 4.xx/5.xx or uncompressed AVI and raw files with MPEG, AC3 (pass-through) or PCM audio. </p>
<p> Additional export modules to write single frames (PPM) or YUV4MPEG streams are available, as well as an interface import module to the avifile library. </p>
<p> It&#8217;s modular concept is intended to provide flexibility and easy user extensibility to include other video/audio codecs or filetypes. A set of tools is included to demux (tcdemux), extract (tcextract) and decode (tcdecode) the sources into raw video/audio streams for import, probing (tcprobe) and scanning (tcscan) your sources and to enable post-processing of AVI files, fixing AVI file header information (avifix), merging multiple files (avimerge), splitting large AVI files (avisplit) to fit on a CD and avisync to correct AV-offsyncs.</p>
<h2>OPTIONS</h2>
<p> <code>-A </code></p>
<dl>
<dt>
<dd> use AC3 as internal audio codec [off]. Only pass-through supported.</dl>
<p> <code>-B </code> <i>n[,m[,M]]</i></p>
<dl>
<dt>
<dd> resize to height-<i>n</i>*<i>M</i> rows [,width-<i>m</i>*<i>M</i>] columns [off,32]. <i>M</i> must be one of 8, 16 or 32. It makes no difference which M you use. You might look at the <i>fast</i> flag of the <code>-Z</code> option if you don not want to calculate <i>n</i> and <i>m</i> yourself.</dl>
<p> <code>-C </code> <i>mode</i></p>
<dl>
<dt>
<dd> enable anti-aliasing mode (1-3) [off]. </p>
<p> 1</p>
<dl>
<dt>
<dd> de-interlace effects only</dl>
<p> 2</p>
<dl>
<dt>
<dd> resize effects only</dl>
<p> 3</p>
<dl>
<dt>
<dd> process full frame (slow)</dl>
</dl>
<p> <code>-D </code> <i>num</i></p>
<dl>
<dt>
<dd> sync video start with audio frame num [0].</dl>
<p> <code>-E </code> <i>r[,b[,c]]</i></p>
<dl>
<dt>
<dd> audio output samplerate [Hz], bits per sample and channels [as input]. The option &quot;-J resample&quot; must be provided for export modules not capable of re-sampling. Samplerate and bits per sample can be specified as 0 to mean &quot;same as input&quot;; this allows converting from stereo to mono while leaving the other parameters alone (-E 0,0,1).</dl>
<p> <code>-F </code> <i>codec_string</i></p>
<dl>
<dt>
<dd> encoder parameter strings [module dependent]. The -F parameter has different meanings for different export modules. Those meanings are documented in <i><a href="/docs/linux/man/1-transcode_export/">transcode_export</a>(1)</i> manual page.</dl>
<p> <code>-G </code> <i>val</i></p>
<dl>
<dt>
<dd> Gamma correction (0.0-10.0) [off]. A value of 1.0 does not change anything. A value lower than 1.0 will make the picture &quot;brighter&quot;, a value above 1.0 will make it &quot;darker&quot;.</dl>
<p> <code>-H </code> <i>n</i></p>
<dl>
<dt>
<dd> auto-probe <i>n</i> MB of source (0=disable) default [1]. Use a higher value than the default to detect all subtitles in the VOB.</dl>
<p> <code>-I </code> <i>mode</i></p>
<dl>
<dt>
<dd> enable de-interlacing mode (1-5) [off]. </p>
<p> 1</p>
<dl>
<dt>
<dd>
<p> <i>&quot;interpolate scanlines&quot;</i> linear interpolation (takes the average of the surronding even rows to determine the odd rows), and copies the even rows as is.</dl>
<p> 2</p>
<dl>
<dt>
<dd>
<p> <i>&quot;handled by encoder&quot;</i> tells the encoding code to handle the fact that the frames are interlaced. Most codecs do not handle this.</dl>
<p> 3</p>
<dl>
<dt>
<dd>
<p> <i>&quot;zoom to full frame&quot;</i> drops to to half size, then zooms out. This can cause excessive blurring which is not always unwanted. On the other hand results are quite good.</dl>
<p> 4</p>
<dl>
<dt>
<dd>
<p> <i>&quot;drop field / half height&quot;</i> drop every other field and keep half height.</dl>
<p> 5</p>
<dl>
<dt>
<dd>
<p> <i>&quot;interpolate scanlines / blend frames&quot;</i> linear blend (similar to -vop pp=lb in mplayer) this, like linear blend calculates the odd rows as the average of the surrounding even rows, and also calculates the even rows as an average of the original even rows and also calculates the even rows as an average of the original odd rows and averages the calculated and original rows. Something like avg (avg(row1,row3), avg(row2, row4))</dl>
</dl>
<p> <code>-J </code> <i>filter1[,filter2[,&#8230;]]</i></p>
<dl>
<dt>
<dd> apply external filter plugins [off]. The avalaible import modules and their options are documented into the <i><a href="/docs/linux/man/1-transcode_filter/">transcode_filter</a>(1)</i> manual page. <i>Note:</i> You can specify more than one -J argument. The order of filter arguments specify in which order the filters are applied. Note also, for transcode internally it makes no difference whether you do &quot;-J filter1 -J filter2&quot; or &quot;-J filter1,filter2&quot;. Use &#8216;tcmodinfo -i <i>NAME</i>&#8216; to get more information about the filter_<i>NAME</i>. Not all filters support this but most of them do. Some of the filter plugins have additional documentation in the docs/ directory.</dl>
<p> <code>-L </code> <i>n</i></p>
<dl>
<dt>
<dd> seek to VOB stream offset <i>n</i>x2kB default [0]. This option is usually calculated automatically when giving &#8211;nav_seek and -c.</dl>
<p> <code>-K </code></p>
<dl>
<dt>
<dd> enable black/white by removing colors mode (grayscale) [off]. Please note this does not necessarily lead to a smaller image / better compression. For YUV mode, this is done by emptying the chroma planes, for RGB mode a weightend grayscale value is computed.</dl>
<p> <code>-M </code> <i>mode</i></p>
<dl>
<dt>
<dd> demuxer PES AV sync modes (0-4) [1]. </p>
<p> <i>Overview</i></p>
<dl>
<dt>
<dd> The demuxer takes care that the right video frames go together with the right audio frame. This can sometimes be a complex task and transcode tries to aid you as much as possible. <i>WARNING:</i> It does make a difference if you (the user) specifies a demuxer to use or if transcode resp. <a href="/docs/linux/man/1-tcprobe/">tcprobe</a>(1) chooses the one which it thinks is right for your material. This is done on purpose to avoid mystic side-effects. So think twice, wether you specify a demuxer or let transcode choose one or you might end up with an off-sync result.</dl>
<p> 0</p>
<dl>
<dt>
<dd> Pass-through. Do not mess with the stream, switch off any synchronization/demuxing process.</dl>
<p> 1</p>
<dl>
<dt>
<dd> PTS only (default). Synchronize video and audio by inspecting PTS/DTS time stamps of audio and video. Preferred mode for PAL VOB streams and DVDs.</dl>
<p> 2</p>
<dl>
<dt>
<dd> NTSC VOB stream synchronization feature. This mode generates synchronization information for transcode by analyzing the frame display time.</dl>
<p> 3</p>
<dl>
<dt>
<dd> (like -M 1): sync AV at initial PTS, but invokes &quot;-D/&#8211;av_fine_ms&quot; options internally based on &quot;tcprobe&quot; PTS analysis. PTS stands for Presentation Time Stamp.</dl>
<p> 4</p>
<dl>
<dt>
<dd> (like -M 2): initial PTS / enforce frame rate, with additional frame rate enforcement (for NTSC).</dl>
</dl>
<p> <code>-N </code> <i>format</i></p>
<dl>
<dt>
<dd> select export format. Default is mp3 for audio, and module-dependant format for video. This option has two different behaviours and accepts two different set of options, as side-effect of ongoing export module transition. For old-style modules (current default, as found in 1.0.x series), argument is audio format ID has hexadecimal value: see below for a list of recognized IDs. Default id, so default format for audio exported track, is MP3 (0x55). If you are using, the transcode&#8217;s the new-style encode/multiplex modules (still under development, see the encode and multiplex directories), argument is a comma-separated pair of export format names. Use tcmodinfo tool to check out what new-style export module support what formats. </p>
<p> Available format for old-style behaviour are: </p>
<p> <i>0x1</i></p>
<dl>
<dt>
<dd> PCM uncompressed audio</dl>
<p> <i>0x50</i></p>
<dl>
<dt>
<dd> MPEG layer-2 aka MP2</dl>
<p> <i>0x55</i></p>
<dl>
<dt>
<dd> MPEG layer-3 aka MP3. Also have a look at &#8211;lame_preset if you intend to do VBR audio.</dl>
<p> <i>0x2000</i></p>
<dl>
<dt>
<dd> AC3 audio</dl>
<p> <i>0xfffe</i></p>
<dl>
<dt>
<dd> OGG/Vorbis audio</dl>
</dl>
<p> <code>-O </code></p>
<dl>
<dt>
<dd> skip flushing of buffers at encoder stop [off, do flushing at each stop].</dl>
<p> <code>-P </code> <i>flag</i></p>
<dl>
<dt>
<dd> pass-through flag (0=off|1=V|2=A|3=A+V) [0]. Pass-through for <i>flag</i> != 1 is broken and not a trivial thing to fix. </p>
<p> You can pass-through DV video, AVI files and MPEG2 video. When doing MPEG2 pass-through (together with the -y raw module), you can give a requantization factor by using -w (for example -w 1.5), this will make the MPEG2 stream smaller. </p>
<p> The pass-through mode is useful for reconstruction of a broken index of an AVI file. The -x ffmpeg import-module analyzes the compressed bitstream and can detect a keyframe for DIV3, MPEG4 (DivX, XviD, ..) and other formats. It then sets an internal flag which the export module will respect when writing the frame out.</dl>
<p> <code>-Q </code> <i>n[,m]</i></p>
<dl>
<dt>
<dd> encoding[,decoding] quality (0=fastest-5=best) [5,5].</dl>
<p> <code>-R </code> <i>n[,f1[,f2]]</i></p>
<dl>
<dt>
<dd> enable multi-pass encoding (0-3) [0,divx4.log,pcm.log]. </p>
<p> 0 Constant bitrate (CBR) encoding. [default]</p>
<dl>
<dt>
<dd> The codec tries to achieve constant bitrate output. This means, each encoded frame is mostly the same size. This type of encoding can help in maintaining constant filling of hardware buffer on set top players or smooth streaming over networks. By the way, Constant bitrate is often obtained sacrifying quality during high motion scenes.</dl>
<p> 1 Variable bitrate encoding: First pass.</p>
<dl>
<dt>
<dd> In this mode, the codec analyses the complete sequence in order to collect data that can improve the distribution of bits in a second VBR pass. The collected data is written to second sub argument (default: divx4.log). This data is codec dependant and cannot be used across codecs. It is strongly advised to use the same codec settings for the VBR analysis pass and the VBR encoding pass if you want predictable results. </p>
<p> The video output of the first pass is not of much use and can grow very large. It&#8217;s a good idea to not save the video output to a file but directly to /dev/null. Usually the bitrate is ignored during first pass. </p>
<p> Disabling audio export makes sense too, so use -y codec,null. It is <i>not</i> recommended to disable the audio <i>import</i> because transcode might drop video frames to keep audio and video in sync. This is not possible when the audio import is disabled. It may lead to the fact that the codec will see a different sequence of frames which effectively renders the log file invalid.</dl>
<p> 2 Variable bitrate encoding: Second pass.</p>
<dl>
<dt>
<dd> The first pass allowed the codec collecting data about the complete sequence. During the second pass, the codec will use that data in order to find an efficient bit distribution that respects both the desired bitrate and the natural bitrate curve shape. This ensures a good compromise between quality and desired bitrate. </p>
<p> Make sure you activate both sound and video encoding during this pass.</dl>
<p> 3 Constant quantizer encoding.</p>
<dl>
<dt>
<dd> The quantizer is the &quot;compression level&quot; of the picture. The lower the quantizer is, the higher is the quality of the picture. This mode can help in making sure the sequence is encoded at constant quality, but no prediction can be made on the final bitrate. When using this mode, the <code>-w</code> option changes its meaning, it now takes the quantizer ranging from 1 to 31. Note that constant quantizer encoding is not supported with some codecs (notably mpeg1/2/4 with -y ffmpeg).</dl>
</dl>
<p> <code>-S </code> <i>unit[,s1-s2]</i></p>
<dl>
<dt>
<dd> process program stream unit[,s1-s2] sequences [0,all]. This option is a bit redundant to &#8211;psu*. This option lets you specify which units you want to have decoded or skipped. At a program stream unit boundary, all (internal) mpeg timers are reset to 0. tcprobe will tell you how many units are in one file.</dl>
<p> <code>-T </code> <i>t[,c[,a]]</i></p>
<dl>
<dt>
<dd> select DVD title[,chapter[,angle]] [1,1,1]. Only a single chapter is transcoded. Use <code>-T</code> 1,-1 to trancode all chapters in a row. You can even specify chapter ranges.</dl>
<p> <code>-U </code> <i>base</i></p>
<dl>
<dt>
<dd> process DVD in chapter mode to base-ch%02d.avi [off].</dl>
<p> <code>-V </code> <i>format</i></p>
<dl>
<dt>
<dd> select video layout / colour space for internal processing. Possible values for this options are: yuv420p (default), yuv422p, rgb24 </p>
<p> yuv420p is default because it is most codecs&#8217; internal format so there is no need for conversions. Some modules may not support it though: use rgb in that case. </p>
<p> rgb24 is the old (pre-0.6.13) transcode internal format. Most codecs do not support this format natively and have to convert it to/from YUV first, so only use this option if you&#8217;re really sure or you want to use a module that doesn&#8217;t support YUV. </p>
<p> yuv422p is an experimental feature and a developers playground. Not many import, export and filter modules support this colorspace. A 4:2:2 colorspace offers much more quality than the consumer oriented 4:2:0 colorspaces like I420/YV12. Most equipment in film and video post-production uses YUV422. YUV422 doubles the precision for chroma (color difference) information in the image. </p>
<p> All internal transformations are supported in YUV422 mode (clipping, flipping, zooming, etc).</dl>
<p> <code>-W </code> <i>n,m[,nav_file]</i></p>
<dl>
<dt>
<dd> autosplit and process part <i>n</i> of <i>m</i> (VOB only) [off]</dl>
<p> <code>-X </code> <i>n[,m,[M]]</i></p>
<dl>
<dt>
<dd> resize to height+<i>n</i>*<i>M</i> rows [,width+<i>m</i>*<i>M</i>] columns [off,32]. M must be one of 8, 16 or 32. It makes no difference which M you use. You might look at the <i>fast</i> flag of the <code>-Z</code> option if you do not want to calculate <i>n</i> and <i>m</i> yourself.</dl>
<p> <code>-Y </code> <i>top[,left[,bottom[,right]]]</i></p>
<dl>
<dt>
<dd> select (encoder) frame region by clipping border. Negative values add a border [off].</dl>
<p> <code>-Z </code> <i>widthxheight[,fast|interlaced]</i></p>
<dl>
<dt>
<dd> resize to <i>width</i> columns, <i>height</i> rows with filtering [off,notfast,notinterlaced]. If <i>fast</i> is given, transcode will calculate the parameters for <code>-X</code> and/or <code>-B</code>. The file <code>fast</code> can only be used when the import and export geometry of an image is a multiple of 8. </p>
<p> In fast mode, a faster but less precise resizing algorithm will be used resulting in a slightly less good quality. Beside this (small) drawback, it is worth a try. </p>
<p> If <i>interlaced</i> is given, transcode will assume the frame is interlaced when resizing, and resize each field independently. This will give better results on interlaced video, but is incompatible with fast mode. Also, the height (both old and new) must be a multiple of 4. </p>
<p> It is also possible to omit <i>width</i> OR <i>height</i>. In this case, transcode will calculate the missing value using the import aspect ratio. The new value will be aligned to be a multiple of 8. Using an additional <i>fast</i> or <i>interlaced</i> is also possible. </p>
<p> Examples (assume input is a 16:9 coded file at 720&#215;576): </p>
<dl>
<dt>
<dd>
<pre>
                        -Z 576x328           uses filtered zoom.
                        -Z 576x328,fast      uses fast zoom.
                        -Z 576x,fast         guess 328 and do fast zoom.
                        -Z x328,interlaced   guess 576 and do interlaced zoom.
                    
</pre>
</dl>
<p> If you also set <code>&#8211;export_prof</code>, you can use just &quot;fast&quot; to indicate that fast resizing is wanted (likewise with &quot;interlaced&quot;).</dl>
<p> <code>-a </code> <i>ach[,vch]</i></p>
<dl>
<dt>
<dd> extract audio[,video] track for encoding.</dl>
<p> <code>-b </code> <i>b[,v,[q,[m]]]</i></p>
<dl>
<dt>
<dd> audio encoder bitrate kBits/s[,vbr[,quality[,mode]]] [128,0,5,0] </p>
<p> The <i>mode</i> parameter specifies which modus lame should use for encoding. Available modes are: </p>
<p> 0</p>
<dl>
<dt>
<dd> Joint Stereo (default)</dl>
<p> 1</p>
<dl>
<dt>
<dd> Full stereo</dl>
<p> 2</p>
<dl>
<dt>
<dd> Mono</dl>
</dl>
<p> <code>-c </code> <i>f1-f2[,f3-f4[, &#8230; ] ]</i></p>
<dl>
<dt>
<dd> encode only frames <i>f1-f2</i> [and <i>f3-f4</i>]. Default is to encode all available frames. Use this and you&#8217;ll get statistics about remaining encoding time. The <i>f[N]</i> parameters may also be timecodes in the HH:MM:SS.FRAME format. Example: </p>
<dl>
<dt>
<dd>
<pre>
                        -c 500-0:5:01,:10:20-1:18:02.1
                    
</pre>
</dl>
<p> Will encode only from frame 500 to 5 minutes and 1 second and from 10 min, 20 sec to 1 hour, 18 min, 2 sec and one frame. </p>
<p> Note that transcode starts counting frames at 0 and excludes the last frame specified. That means that &quot;<code>-c</code> 0-100&quot; will encoded 100 frames starting at frame 0 up to frame 99</dl>
<p> <code>-d </code></p>
<dl>
<dt>
<dd> swap bytes in audio stream [off]. In most cases, DVD PCM audio tracks require swapping of audio bytes</dl>
<p> <code>-e </code> <i>r[,b[,c]]</i></p>
<dl>
<dt>
<dd> PCM audio stream parameter. Sample rate [Hz], bits per sample and number of channels [48000,16,2]. Normally this is autodetected.</dl>
<p> <code>-f </code> <i>rate[,frc]</i></p>
<dl>
<dt>
<dd> import video frame rate[,frc] [25.000,0]. If <i>frc</i> (frame rate code) is specified, transcode will calculate the precise frames per second internally. Valid values for <i>frc</i> are: </p>
<p> 1</p>
<dl>
<dt>
<dd> 23.976 (24000/1001.0)</dl>
<p> 2</p>
<dl>
<dt>
<dd> 24</dl>
<p> 3</p>
<dl>
<dt>
<dd> 25</dl>
<p> 4</p>
<dl>
<dt>
<dd> 29.970 (30000/1001.0)</dl>
<p> 5</p>
<dl>
<dt>
<dd> 30</dl>
<p> 6</p>
<dl>
<dt>
<dd> 50</dl>
<p> 7</p>
<dl>
<dt>
<dd> 59.940 (2 * 29.970)</dl>
<p> 8</p>
<dl>
<dt>
<dd> 60</dl>
<p> 9</p>
<dl>
<dt>
<dd> 1</dl>
<p> 10</p>
<dl>
<dt>
<dd> 5</dl>
<p> 11</p>
<dl>
<dt>
<dd> 10</dl>
<p> 12</p>
<dl>
<dt>
<dd> 12</dl>
<p> 13</p>
<dl>
<dt>
<dd> 15</dl>
</dl>
<p> <code>-g </code> <i>WidthxHeight</i></p>
<dl>
<dt>
<dd> video stream frame size [720&#215;576].</dl>
<p> <code>-h</code></p>
<dl>
<dt>
<dd> print out usage information.</dl>
<p> <code>-i </code> <i>name</i></p>
<dl>
<dt>
<dd> input file/directory/device/mountpoint/host name, default is [/dev/zero].</dl>
<p> <code>-j </code> <i>top[,left[,bottom[,right]]]</i></p>
<dl>
<dt>
<dd> select frame region by clipping border. Negative values add a border [off].</dl>
<p> <code>-k </code></p>
<dl>
<dt>
<dd> swap red/blue (Cb/Cr) in video frame [off]. Use if people have blue faces.</dl>
<p> <code>-l </code></p>
<dl>
<dt>
<dd> mirror video frame [off].</dl>
<p> <code>-m </code> <i>file</i></p>
<dl>
<dt>
<dd> write audio stream to separate file [off].</dl>
<p> <code>-n </code> <i>0xnn</i></p>
<dl>
<dt>
<dd> import audio format id [0x2000]. Normally, this is autodetected.</dl>
<p> <code>-o </code> <i>file</i></p>
<dl>
<dt>
<dd> output file name, default is [/dev/null].</dl>
<p> <code>-p </code> <i>file</i></p>
<dl>
<dt>
<dd> read audio stream from separate file [off].</dl>
<p> <code>-q </code> <i>debuglevel</i></p>
<dl>
<dt>
<dd> possible values for debuglevel: </p>
<p> 0</p>
<dl>
<dt>
<dd> QUIET</dl>
<p> 1</p>
<dl>
<dt>
<dd> INFO</dl>
<p> 2</p>
<dl>
<dt>
<dd> DEBUG</dl>
<p> 4</p>
<dl>
<dt>
<dd> STATS</dl>
<p> 8</p>
<dl>
<dt>
<dd> WATCH</dl>
<p> 16</p>
<dl>
<dt>
<dd> FLIST</dl>
<p> 32</p>
<dl>
<dt>
<dd> VIDCORE</dl>
<p> 64</p>
<dl>
<dt>
<dd> SYNC</dl>
<p> 128</p>
<dl>
<dt>
<dd> COUNTER</dl>
<p> 256</p>
<dl>
<dt>
<dd> PRIVATE</dl>
</dl>
<p> <code>-r </code> <i>n[,m]</i></p>
<dl>
<dt>
<dd> reduce video height/width by n[,m] [off]. Example: <code>-r</code> 2 will rescale the framesize of a 720&#215;576 file to 360&#215;288.</dl>
<p> <code>-s </code> <i>gain,[center,[front,[rear]]]</i></p>
<dl>
<dt>
<dd> increase volume of audio stream by gain,[center,front,rear] default [off,1,1,1].</dl>
<p> <code>-t </code> <i>n,base</i></p>
<dl>
<dt>
<dd> split output to <i>base</i>%03d.avi with <i>n</i> frames [off].</dl>
<p> <code>-u </code> <i>m[,n]</i></p>
<dl>
<dt>
<dd> use <i>m</i> framebuffer[,<i>n</i> threads] for AV processing [10,1].</dl>
<p> <code>-v </code></p>
<dl>
<dt>
<dd> print version.</dl>
<p> <code>-w </code> <i>b[,k[,c]]</i></p>
<dl>
<dt>
<dd> encoder bitrate[,keyframes[,crispness]] [(6000 for MPEG 1/2, 1800 for others),250,100].</dl>
<p> <code>&#8211;video_max_bitrate </code> <i>b</i></p>
<dl>
<dt>
<dd> Use <i>b</i> as maximal bitrate (kbps) when encoding variable bitrate streams.</dl>
<p> <code>-x </code> <i>vmod[,amod]</i></p>
<dl>
<dt>
<dd> video[,audio] import modules [auto,auto]. If omitted, transcode will probefor appropriate import modules. The avalaible import modules and their options are documented into the <i><a href="/docs/linux/man/1-transcode_import/">transcode_import</a>(1)</i> manual page.</dl>
<p> <code>-y </code> <i>vmod[,amod[,mmod]]</i></p>
<dl>
<dt>
<dd> video[,audio[,multiplex]] export modules [null]. If omitted, transcode will encode to the <i>null</i> module. If a multiplex module is given, transcode will use the new-style encode/multiplex modules (still under development, see the encode and multiplex directories); if no multiplex module is given, the traditional export modules will be used. The avalaible export, encoder and multiplexor modules and their options are documented into the <i><a href="/docs/linux/man/1-transcode_export/">transcode_export</a>(1)</i> manual page.</dl>
<p> <code>&#8211;accel </code> <i>type</i></p>
<dl>
<dt>
<dd> enforce experimental IA32 acceleration for type [autodetect]. <i>type</i> may be one of </p>
<p> <i>C</i></p>
<dl>
<dt>
<dd> No acceleration</dl>
<p> <i>ia32asm</i></p>
<dl>
<dt>
<dd> plain x86 assembly</dl>
<p> <i>mmx</i></p>
<dl>
<dt>
<dd> MMX instruction set</dl>
<p> <i>3dnow</i></p>
<dl>
<dt>
<dd> 3DNow! instruction set</dl>
<p> <i>sse</i></p>
<dl>
<dt>
<dd> SSE instruction set</dl>
<p> <i>sse2</i></p>
<dl>
<dt>
<dd> SSE2 instruction set</dl>
</dl>
<p> <code>&#8211;avi_limit </code><i>N</i></p>
<dl>
<dt>
<dd> split/rotate output AVI file after N MB [2048].</dl>
<p> <code>&#8211;avi_comments </code> <i>F</i></p>
<dl>
<dt>
<dd> Read AVI header comments from file <i>F</i> [off]. The AVI file format supports so-called tomb-stone data. It can be used to write annotations into the AVI file. </p>
<p> See the file <i>docs/avi_comments.txt</i> for a sample input file with all tags. When the file is read, empty lines and lines starting with &#8216;#&#8217; are ignored. The syntax is: &quot;TAG&lt;space&gt;STRING&quot;. The order of the tags does not matter. If a tag has no string following it, it is ignored. That means, you can use the file docs/avi_comments.txt as input and only fill out the fields you want. </p>
<p> A very simple example is: </p>
<dl>
<dt>
<dd>
<pre><code>
-- -- -- -- -- -- -- --snip-- -- -- -- -- -- -- --INAM My 1st Birthday
                         ISBJ My first steps !IART My proud family-- -- -- -- -- -- -- --snip-- -- -- -- -- -- -- --
</code></pre>
</dl>
<p> Keep in mind that there is no endless space in the AVI header, most likely its around 1000 bytes.</dl>
<p> <code>&#8211;zoom_filter </code> <i>string</i></p>
<dl>
<dt>
<dd> use filter string for video resampling <code>-Z</code> [Lanczos3] The following filters are available: </p>
<p> Bell</p>
<dl>
<dt>
<dd></dl>
<p> Box</p>
<dl>
<dt>
<dd></dl>
<p> Lanczos3 (default)</p>
<dl>
<dt>
<dd></dl>
<p> Mitchell</p>
<dl>
<dt>
<dd></dl>
<p> Hermite</p>
<dl>
<dt>
<dd></dl>
<p> B_spline</p>
<dl>
<dt>
<dd></dl>
<p> Triangle</p>
<dl>
<dt>
<dd></dl>
</dl>
<p> <code>&#8211;cluster_percentage </code></p>
<dl>
<dt>
<dd> use percentage mode for cluster encoding <code>-W</code>&gt; [off]</dl>
<p> <code>&#8211;cluster_chunks </code> <i>a-b</i></p>
<dl>
<dt>
<dd> process chunk range instead of selected chunk [off]</dl>
<p> <code>&#8211;export_asr </code> <i>C</i></p>
<dl>
<dt>
<dd> set export aspect ratio code <i>C</i> [as input] Valid codes for <i>C</i> are: </p>
<p> 1</p>
<dl>
<dt>
<dd> 1:1</dl>
<p> 2</p>
<dl>
<dt>
<dd> 4:3</dl>
<p> 3</p>
<dl>
<dt>
<dd> 16:9</dl>
<p> 4</p>
<dl>
<dt>
<dd> 2.21:1</dl>
</dl>
<p> <code>&#8211;export_prof </code> <i>S</i></p>
<dl>
<dt>
<dd> WARNING: this option will be renamed as <code>&#8211;export_profile</code> in future releases. </p>
<p> Select an export profile {vcd, svcd, xvcd, dvd} [-pal|-ntsc|-secam]. Default is no profile. </p>
<p> If you set this meta option to one of the values below, transcode will adjust some internal paramaters as well as geometry and clipping. If no export modules are specified, mpeg2enc for video and mp2enc for audio are used when compiled with mjpegtools support. </p>
<p> Valid values for <i>S</i> are e.g. vcd, vcd-pal, vcd-ntsc, svcd, svcd-pal, &#8230; </p>
<p> xvcd profile is equal to svcd except that it allows for up to 9000 Kbps video bitrate (default is 5000) and arbitrary audio samplerate. </p>
<p> When one of the above is used, transcode will calculate the needed clipping and resizing values for you based on the import and export aspect ratio. This is especially handy if you want to encode a 16:9 DVD into a 4:3 SVCD for example. Transcode internally then sets &#8211;pre_clip to add the black bars (&quot;letterboxing&quot;). </p>
<p> If you use &quot;vcd&quot; instead of &quot;vcd-pal&quot; or &quot;vcd-ntsc&quot;, transcode will make an educated guess if PAL or NTSC vcd is wanted. The same is true for the other profiles. When the input file has no aspect ratio information at all, transcode guesses it based on the import frame sizes. You can set the import aspect ratio by giving <code>&#8211;import_asr</code> CODE. </p>
<p> Examples (assume input is a 16:9 coded file at 720&#215;576 (PAL)): </p>
<dl>
<dt>
<dd>
&#8211;export_prof svcd clip top / bot &#8211; 96;<br />
resizes to 480&#215;576 &#8211;export_prof vcd &#8211; ntsc clip top / bot &#8211; 96;<br />
resizes to 352&#215;240
</dl>
<p> This enables simpilified commandlines where transcode tries to set sensible values for mpeg export. When you don&#8217;t specify an export module with -y, mpeg2enc will be used. </p>
<dl>
<dt>
<dd>
<pre>
                        transcode -i vob/ --export_prof svcd -Z fast -o test
                    
</pre>
</dl>
<p> The ffmpeg export module `-y ffmpeg&#8217; does support profiles as well. The module tries to be smart and sets internal ffmpeg parameters which are otherwise quite tricky to find out. Usage is similar to the above. </p>
<dl>
<dt>
<dd>
<pre>
                        transcode -i vob/ --export_prof dvd -y ffmpeg -o test -m test.ac3
                        tcmplex -m d -i test.m2v -p test.ac3 -o test.mpg
                    
</pre>
</dl>
</dl>
<p> <code>&#8211;export_par </code> <i>C[,N]</i></p>
<dl>
<dt>
<dd> set export pixel aspect ratio to <i>C</i>[,<i>N</i>]. To encode anamorphic material, transcode can encode the target pixel aspect ratio into the file. This is NOT the actual aspect ratio of the image, but only the amount by which every single pixel is stretched when played with an aspect ratio aware application, like mplayer. </p>
<p> To encode at non standard aspect ratios, set both <i>C</i> and <i>N</i>. E.g. to make every pixel twice as high as it&#8217;s wide (e.g. to scale back to normal size after deinterlacing by dropping every second line). </p>
<p> If <i>C</i> and <i>N</i> are specified, the value set for <i>C</i> does give the pixel aspect ratio of the width and <i>N</i> the one for the height. If only <i>C</i> is specified, the table below applies. </p>
<p> Valid codes for <i>C</i> are </p>
<p> 1</p>
<dl>
<dt>
<dd> 1:1 No stretching</dl>
<p> 2</p>
<dl>
<dt>
<dd> 12:11 5:4 image to 4:3 (ex: 720&#215;576 -&gt; 768&#215;576)</dl>
<p> 3</p>
<dl>
<dt>
<dd> 10:11 3:2 image to 4:3 (ex: 720&#215;480 -&gt; 640&#215;480)</dl>
<p> 4</p>
<dl>
<dt>
<dd> 16:11 5:4 image to 16:9 (ex: 720&#215;576 -&gt; 1024&#215;576)</dl>
<p> 5</p>
<dl>
<dt>
<dd> 40:33 3:2 image to 16:9 (ex: 720&#215;480 -&gt; 872&#215;480)</dl>
</dl>
<p> <code>&#8211;import_asr </code> <i>C</i></p>
<dl>
<dt>
<dd> set import aspect ratio code <i>C</i> [autoprobed] </p>
<p> Valid codes for <i>C</i> are </p>
<p> 1</p>
<dl>
<dt>
<dd> 1:1</dl>
<p> 2</p>
<dl>
<dt>
<dd> 4:3</dl>
<p> 3</p>
<dl>
<dt>
<dd> 16:9</dl>
<p> 4</p>
<dl>
<dt>
<dd> 2.21:1</dl>
</dl>
<p> <code>&#8211;keep_asr </code></p>
<dl>
<dt>
<dd> try to keep aspect ratio (only with -Z) [off] </p>
<p> The <code>&#8211;keep_asr</code> options changes the meaning of <code>-Z</code>. It tries to fit the video into a framesize specified by <code>-Z</code> by keeping the <i>original</i> aspect ratio. </p>
<dl>
<dt>
<dd>
+ &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+ +&#8211; -480 &#8212; &#8212; -+ | | | black |<br />
    | 720&#215;306 = 2.35:1 |-&gt;- Z 480&#215;480 &#8211;keep_asr-&gt;| &#8212; &#8212; &#8212; &#8212; &#8212; -4 | | | 480&#215;204 8 + &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+ | &#8212; &#8212; &#8212; &#8212; &#8212; -0 | black |<br />
                     +&#8211; &#8212; &#8212; &#8212; &#8212; -+
</dl>
<p> Consider <code>&#8211;keep_asr</code> a wrapper for calculating <code>-Y</code> options and <code>-Z</code> options.</dl>
<p> <code>&#8211;mplayer_probe </code></p>
<dl>
<dt>
<dd> use external mplayer binary to probe stream, reset default import modules as mplayer ones [off]. Default is to use internal probing code. Using this option without mplayer import modules (<code>-x</code> mplayer) can lead to unpredictable and possibly wrong results.</dl>
<p> <code>&#8211;quantizers </code> <i>min,max</i></p>
<dl>
<dt>
<dd> set encoder min/max quantizer. This is meaningfull only for video codecs of MPEG family. For other kind of codecs, this options is harmless. [2,31]</dl>
<p> <code>&#8211;divx_rc </code> <i>p,rp,rr</i></p>
<dl>
<dt>
<dd> divx encoder rate control parameter [2000,10,20]</dl>
<p> <code>&#8211;divx_vbv_prof </code> <i>N</i></p>
<dl>
<dt>
<dd> divx5 encoder VBV profile (0=free-5=hiqhq) [3]. Sets a predefined profile for the Video Bitrate Verifier. If <i>N</i> is set to zero, no profile is applied and the user specified values from <code>&#8211;divx_vbv</code> are used. </p>
<p> Valid profiles </p>
<p> 0</p>
<dl>
<dt>
<dd> Free/No profile ( Use supplied values )</dl>
<p> 1</p>
<dl>
<dt>
<dd> Handheld ( 320, 16, 3072 )</dl>
<p> 2</p>
<dl>
<dt>
<dd> Portable ( 1920, 64, 12288 )</dl>
<p> 3</p>
<dl>
<dt>
<dd> Home Theatre ( 10000, 192, 36864 )</dl>
<p> 4</p>
<dl>
<dt>
<dd> High Definition ( 20000, 384, 73728 )</dl>
</dl>
<p> <code>&#8211;divx_vbv </code> <i>br,sz,oc</i></p>
<dl>
<dt>
<dd> divx5 encoder VBV params (bitrate,size,occup.) [10000,192,36864] These parameters are normally set through the profile parameter <code>&#8211;divx_vbv_prof</code>. Do not mess with theses value unless you are absolutely sure of what you are doing. Transcode internally multiplicates vbv_bitrate with 400, vbv_size with 16384 and vbv_occupancy with 64 to ensure the supplied values are multiples of what the encoder library wants.</dl>
<p> <code>&#8211;export_fps </code> <i>rate[,frc]</i></p>
<dl>
<dt>
<dd> set export frame rate (and code) [as input].Valid values for <i>frc</i> are </p>
<p> frc rate </p>
<p> 1</p>
<dl>
<dt>
<dd> 23.976 (24000/1001.0)</dl>
<p> 2</p>
<dl>
<dt>
<dd> 24</dl>
<p> 3</p>
<dl>
<dt>
<dd> 25</dl>
<p> 4</p>
<dl>
<dt>
<dd> 29.970 (30000/1001.0)</dl>
<p> 5</p>
<dl>
<dt>
<dd> 30</dl>
<p> 6</p>
<dl>
<dt>
<dd> 50</dl>
<p> 7</p>
<dl>
<dt>
<dd> 59.940 (2 * 29.970)</dl>
<p> 8</p>
<dl>
<dt>
<dd> 60</dl>
<p> 9</p>
<dl>
<dt>
<dd> 1</dl>
<p> 10</p>
<dl>
<dt>
<dd> 5</dl>
<p> 11</p>
<dl>
<dt>
<dd> 10</dl>
<p> 12</p>
<dl>
<dt>
<dd> 12</dl>
<p> 13</p>
<dl>
<dt>
<dd> 15</dl>
</dl>
<p> <code>&#8211;export_frc </code> <i>F</i></p>
<dl>
<dt>
<dd> set export frame rate code <i>F</i> [as input]. <i>Obsolete</i>, use <code>&#8211;export_fps</code> 0,F</dl>
<p> <code>&#8211;hard_fps </code></p>
<dl>
<dt>
<dd> disable smooth dropping (for variable fps clips) [off]. See /docs/framerate.txt for more information.</dl>
<p> <code>&#8211;pulldown </code></p>
<dl>
<dt>
<dd> set MPEG 3:2 pulldown flags on export [off]</dl>
<p> <code>&#8211;antialias_para </code> <i>w,b</i></p>
<dl>
<dt>
<dd> center pixel weight, xy-bias [0.333,0.500]</dl>
<p> <code>&#8211;no_audio_adjust </code></p>
<dl>
<dt>
<dd> disable internal audio frame sample adjustment [off]</dl>
<p> <code>&#8211;no_bitreservoir </code></p>
<dl>
<dt>
<dd> disable lame bitreservoir for MP3 encoding [off]</dl>
<p> <code>&#8211;config_dir </code> <i>dir</i></p>
<dl>
<dt>
<dd> Assume config files are in this <i>dir</i>. This only affects the -y ffmpeg and -y xvid4 modules. It gives the path where the modules search for their configuration.</dl>
<p> <code>&#8211;lame_preset </code> <i>name[,fast]</i></p>
<dl>
<dt>
<dd> use lame preset with <i>name</i> [off]. Lame features some built-in presets. Those presets are designed to provide the highest possible quality. They have for the most part been subject to and tuned via rigorous listening tests to verify and achieve this objective. These are continually updated to coincide with the latest developments that occur and as a result should provide you with nearly the best quality currently possible from LAME. Any of those VBR presets can also be used in fast mode, using the new vbr algorithm. This mode is faster, but its quality could be a little lower. To enable the fast mode, append &quot;<i>,fast</i>&quot; </p>
<p> <i>&lt;N kbps&gt;</i></p>
<dl>
<dt>
<dd> Using this preset will usually give you good quality at a specified bitrate. Depending on the bitrate entered, this preset will determine the optimal settings for that particular situation. While this approach works, it is not nearly as flexible as VBR, and usually will not reach the same quality level as VBR at higher bitrates. ABR.</dl>
<p> <i>medium</i></p>
<dl>
<dt>
<dd> This preset should provide near transparency to most people on most music. The resulting bitrate should be in the 150-180kbps range, according to music complexity. VBR.</dl>
<p> <i>standard</i></p>
<dl>
<dt>
<dd> This preset should generally be transparent to most people on most music and is already quite high in quality. The resulting bitrate should be in the 170-210kbps range, according to music complexity. VBR.</dl>
<p> <i>extreme</i></p>
<dl>
<dt>
<dd> If you have extremely good hearing and similar equipment, this preset will provide slightly higher quality than the &quot;standard&quot; mode. The resulting bitrate should be in the 200-240kbps range, according to music complexity. VBR.</dl>
<p> <i>insane</i></p>
<dl>
<dt>
<dd> This preset will usually be overkill for most people and most situations, but if you must have the absolute highest quality with no regard to filesize, this is the way to go. This preset is the highest preset quality available. 320kbps CBR.</dl>
<p> (taken from <i><a rel="nofollow" href="http://www.mp3dev.org/mp3/doc/html/presets.html)">http://www.mp3dev.org/mp3/doc/html/presets.html)</a></i>[1]</p>
<dl>
<dt>
<dd></dl>
</dl>
<p> <code>&#8211;av_fine_ms </code> <i>t</i></p>
<dl>
<dt>
<dd> AV fine-tuning shift <i>t</i> in millisecs [autodetect] also see -D.</dl>
<p> <code>&#8211;nav_seek </code> <i>file</i></p>
<dl>
<dt>
<dd> use VOB or AVI navigation file [off]. Generate a nav file with tcdemux -W &gt;nav_log for VOB files or with <a href="/docs/linux/man/1-aviindex/">aviindex</a>(1) for AVI files.</dl>
<p> <code>&#8211;psu_mode </code></p>
<dl>
<dt>
<dd> process VOB in PSU, -o is a filemask incl. %d [off]. PSU means Program Stream Unit and this mode is useful for (mostly) NTSC DVDs which have several program stream units.</dl>
<p> <code>&#8211;psu_chunks </code> <i>a-b</i></p>
<dl>
<dt>
<dd> process only selected units <i>a-b</i> for PSU mode [all]</dl>
<p> <code>&#8211;no_split </code></p>
<dl>
<dt>
<dd> encode to single file in chapter/psu/directory mode [off]. If you don&#8217;t give this option, you&#8217;ll end up with several files in one of the above mentioned modes. It is still possible to merge them with <a href="/docs/linux/man/1-avimerge/">avimerge</a>(1).</dl>
<p> <code>&#8211;multi_input </code></p>
<dl>
<dt>
<dd>
<p> <i>(EXPERIMENTAL)</i> enable multiple input mode: intelligently join input files in import. The inputs can be expressed using standard POSIX globbing. While theorically all input modules are supported, it is safe to use this only when dealing with constant-sized audio (PCM) and intra-frame only video codecs (es: MJPEG). To be safe, use this mode with im, ffmpeg and raw import modules.</dl>
<p> <code>&#8211;pre_clip </code> <i>t[,l[,b[,r]]]</i></p>
<dl>
<dt>
<dd> select initial frame region by clipping border [off]</dl>
<p> <code>&#8211;post_clip </code> <i>t[,l[,b[,r]]]</i></p>
<dl>
<dt>
<dd> select final frame region by clipping border [off]</dl>
<p> <code>&#8211;a52_drc_off </code></p>
<dl>
<dt>
<dd> disable liba52 dynamic range compression [enabled]. If you dont specify this option, liba52 will provide the default behaviour, which is to apply the full dynamic range compression as specified in the A/52 stream. This basically makes the loud sounds softer, and the soft sounds louder, so you can more easily listen to the stream in a noisy environment without disturbing anyone. </p>
<p> If you let it enabled this this will totally disable the dynamic range compression and provide a playback more adapted to a movie theater or a listening room.</dl>
<p> <code>&#8211;a52_demux </code></p>
<dl>
<dt>
<dd> demux AC3/A52 to separate channels [off]</dl>
<p> <code>&#8211;a52_dolby_off </code></p>
<dl>
<dt>
<dd> disable liba52 dolby surround [enabled]. Selects whether the output is plain stereo (if the option is set) or if it is Dolby Pro Logic &#8211; also called Dolby surround or 3:1 &#8211; downmix (if the option is not used).</dl>
<p> <code>&#8211;log_no_color </code></p>
<dl>
<dt>
<dd> disable colored log messages. By default transcode use colors in log messages in order to easily distinguish message classes. That behaviour can be problematic if output of transcode is a file or a pipe, so this option came handful.</dl>
<p> <code>&#8211;dir_mode </code> <i>base</i></p>
<dl>
<dt>
<dd> process directory contents to base-%03d.avi [off]</dl>
<p> <code>&#8211;frame_interval </code> <i>N</i></p>
<dl>
<dt>
<dd> select only every <i>N</i>th frame to be exported [1]</dl>
<p> <code>&#8211;encode_fields </code> <i>C</i></p>
<dl>
<dt>
<dd> enable field based encoding (if supported) [off]. This option takes an argument if given to denote the order of fields. If the option is not given, it defaults to progressive (do not assume the picture is interlaced) </p>
<p> Valid codes for <i>C</i> are: </p>
<p> <i>p</i></p>
<dl>
<dt>
<dd> progressive (default)</dl>
<p> <i>t</i></p>
<dl>
<dt>
<dd> top-field first</dl>
<p> <i>b</i></p>
<dl>
<dt>
<dd> bottom-field first</dl>
</dl>
<p> <code>&#8211;dv_yuy2_mode, &#8211;dv_yv12_mode</code></p>
<dl>
<dt>
<dd> Indicates that libdv decodes Digital Video frames in YUY2 (packed) or YV12 (planar) mode, respectively. Normally transcode figures out the correct mode automatically, but if you try to transcode PAL DV files and the results look strange, try one of these options.</dl>
<p> <code>&#8211;write_pid </code> <i>file</i></p>
<dl>
<dt>
<dd> write pid of signal thread to <i>file</i> [off]. Enables you to terminate transcode cleanly by sending a SIGINT (2) to the pid in <i>file</i>. Please note <i>file</i> will be overwritten. Usage example </p>
<dl>
<dt>
<dd>
<pre>
                        $ transcode ... --write_pid /tmp/transcode.pid &amp;
                        $ kill -2 `cat /tmp/transcode.pid`
                    
</pre>
</dl>
</dl>
<p> <code>&#8211;nice </code> <i>N</i></p>
<dl>
<dt>
<dd> set niceness to <i>N</i> [off]. The option &#8211;nice which renices transcode to the given positive or negative value. -10 sets a high priority; +10 a low priority. This might be useful for cluster mode.</dl>
<p> <code>&#8211;progress_meter </code> <i>N</i></p>
<dl>
<dt>
<dd> select type of progress meter [1]. Selects the type of progress message printed by transcode: </p>
<p> <i>0</i></p>
<dl>
<dt>
<dd> no progress meter</dl>
<p> <i>1</i></p>
<dl>
<dt>
<dd> standard progress meter</dl>
<p> <i>2</i></p>
<dl>
<dt>
<dd> raw progress data (written to standard output)</dl>
<p> Scripts that need progress data should use type 2, since the format of type 1 is subject to change without notice.</dl>
<p> <code>&#8211;progress_rate </code> <i>N</i></p>
<dl>
<dt>
<dd> print progress every <i>N</i> frames [1]. Controls how frequently the status message is printed (every <i>N</i> frames).</dl>
<p> <code>&#8211;socket </code> <i>FILE</i></p>
<dl>
<dt>
<dd> Open a socket to accept commands while running. See <i><a href="/docs/linux/man/1-tcmodinfo/">tcmodinfo</a>(1)</i> and /docs/filter-socket.txt for more information about the protocol.</dl>
<h2>ENVIRONMENT</h2>
<p> <i>TRANSCODE_LOG_NO_COLOR</i></p>
<dl>
<dt>
<dd> if set, forces the colored logging off for all the tools of transcode suite.</dl>
<h2>NOTES</h2>
<p> *</p>
<dl>
<dt>
<dd> Most source material parameter are auto-detected.</dl>
<p> *</p>
<dl>
<dt>
<dd> Clipping region options are expanded symmetrically. Examples: </p>
<p> -j 80 will be expanded to -j 80,0,80,0 </p>
<p> -j 80,8 will be expanded to -j 80,8,80,8 </p>
<p> -j 80,8,10 will be expanded to -j 80,8,10,8</dl>
<p> *</p>
<dl>
<dt>
<dd> maximum image size is 1920&#215;1088.</dl>
<p> *</p>
<dl>
<dt>
<dd> The video frame operations ordering is fixed: &quot;-j -I -X -B -Z -Y -r -z -l -k -K -G -C&quot; (executed from left to right).</dl>
<p> *</p>
<dl>
<dt>
<dd> Shrinking the image with &#8216;-B&#8217; is not possible if the image width/height is not a multiple of 8, 16 or 32.</dl>
<p> *</p>
<dl>
<dt>
<dd> Expanding the image with &#8216;-X&#8217; is not possible if the image width/height is not a multiple of 8, 16 or 32.</dl>
<p> *</p>
<dl>
<dt>
<dd> The final frame width/height should be a multiple of 8. (to avoid encoding problems with some codecs) </p>
<p> 1.</p>
<dl>
<dt>
<dd> Reducing the video height/width by 2,4,8 Option &#8216;-r factor&#8217; can be used to shrink the video image by a constant factor, this factor can be 2,4 or 8.</dl>
<p> 2.</p>
<dl>
<dt>
<dd> Clipping and changing the aspect ratio <code>transcode</code> uses 3 steps to produce the input image for the export modules </p>
<p> 1.</p>
<dl>
<dt>
<dd> Clipping of the input image.</dl>
<p> 2.</p>
<dl>
<dt>
<dd> Changing the aspect ratio of the 1) output.</dl>
<p> 3.</p>
<dl>
<dt>
<dd> Clipping of the 2) output.</dl>
</dl>
</dl>
<p> *</p>
<dl>
<dt>
<dd>
<p> <i>Bits per pixel</i> (bits/pixel) is a value transcode calculates and prints when starting up. It is mainly useful when encoding to MPEG4 (xvid, divx, etc). You&#8217;ll see line like </p>
<p> [transcode] V: bits/pixel | 0.237 </p>
<p> Simplified said, bits/pixel quantifies how good an encode will be. Although this value depends heavily on the used input material, as a general rule of thump it can be said that values greater or close to 0.2 will result in good encodes, encodes with values less than 0.15 will have noticeable artifacts. </p>
<p> <i>Bits per pixel</i> depends on the resolution, bitrate and frames per second. If you have a low value ( &lt; 0.15), you might want to raise the bitrate or encode at a lower resolution. The exact formula is </p>
<dl>
<dt>
<dd>
<pre><code>
bitrate * 1000 bpp = -- -- -- -- -- -- -- -- --width * height * fps
</code></pre>
</dl>
</dl>
<p> *</p>
<dl>
<dt>
<dd>
<p> <i>AC3 / Multiple channels</i> </p>
<p> When you do import an audio stream which has more then two audio channels &#8211; this is usually the case for AC3 audio &#8211; transcode will automagically downmix to two channels (stereo). You&#8217;ll see line like </p>
<p> [transcode] A: downmix | 5 channels -&gt; 2 channels </p>
<p> This is done, because most encoders and audio filters can not handle more than 2 channels correctly. The PCM internal representation does not support more than two channels, audio will be downmixed to stereo <i>No</i> downmix will happen, if you use AC3 as the internal audio codec or use audio pass-through.</dl>
<h2>EXAMPLES</h2>
<p> The following command will read it&#8217;s input from the DVD drive (I assume <i>/dev/dvd</i> is a symbolic link to the actual DVD device) and produce a splitted divx4 movie according to the chapter information on the DVD medium. The output files will be named <i>my_movie-ch00.avi</i>, <i>my_movie-ch01.avi</i> &#8230; </p>
<dl>
<dt>
<dd>
<pre>
            <code>
                transcode -i /dev/dvd/ -x dvd -j 16,0 -B 5,0 -Y 40,8 -s 4.47 -U my_movie -y xvid -w 1618
            </code>
        
</pre>
</dl>
<p> Option <code>-j 16,0</code> will be expanded to <code>-j 16,0,16,0</code> and results in 16 rows from the top and the bottom of the image to be cut off. This may be usefull if the source consists of black top and bottom bars. </p>
<p> Option <code>-B 5,0</code> tells <code>transcode</code> to shrink the resulting image by 5*32=160 rows in height. </p>
<p> Option <code>-Y 40,8</code> will be expanded to <code>-Y 40,8,40,8</code> and tells <code>transcode</code> to &#8230; </p>
<p> Option <code>-s 4.47</code> tells <code>transcode</code> to increase audio volume by a factor 4.47. </p>
<p> Option <code>-U my_movie</code> tells <code>transcode</code> to operate in chapter mode and produce output to files named <i>my_movie-ch00.avi</i>, <i>my_movie-ch01.avi</i>&#8230;. You can either merge the files afterwards with avimerge or add the option &#8211;no_split to the command line. </p>
<p> Option <code>-y xvid</code> tells <code>transcode</code> to use the export module export_xvid.so which in turn uses the XviD encoder to encode the video. </p>
<p> Option <code>-w 1618</code> tells <code>transcode</code> to set the encoder bitrate to 1618 which is lower than the default of 1800 and results in smaller files with the loss of visual quality. </p>
<p> Lets assume that you have an NTSC DVD (720&#215;480) and you want to make an NTSC-SVCD</p>
<dl>
<dt>
<dd> The frame size of the DVD movie is 720&#215;480 @ 16:9. For the purpose of frame resizing, the width 720 is not relavant (that is, it will not be used in the following reasoning). It is not needed because the original frame size is really defined by the frame height and aspect ratio. The _final result_ should be 640&#215;480, encoded as 480&#215;480 @ 4:3 (the height 480 multiplied by the aspect ratio 4:3 gives the width 640). This same frame size (640&#215;480) can also be encoded as 640&#215;360 @ 16:9 (the height 360 by the aspect ratio 16:9 gives the width 640). </p>
<p> As the _original video_ has aspect ratio 16:9, first we resize to 640&#215;360, keeping that aspect ratio. But the aspect ratio has to be changed to 4:3. To find the frame size in the new aspect ratio the height 360 is multiplied by the new aspect ratio, giving the width 480. This is accomplished with the transcode options &quot;<code>&#8211;export_asr</code> 2 -Z 480&#215;360,fast&quot;. </p>
<p> To avoid stretching the video height in this change (because the new aspect ratio is less than the original), black borders should be added at the top and bottom of the video, bringing the frame to the desired 480&#215;480 @ 4:3 size. The transcode option for this is &quot;-Y -60,0,-60,0&quot;. </p>
<p> If for some reason (maybe a subtitle filter) the black borders (of height 60 each) should be added before resizing the frame and changing the aspect ratio to 4:3. One reason for that would be the need of running a _pre_ filter after adding the black borders. Then the options &quot;-j&quot; or &quot;&#8211;pre_clip&quot; can be used instead of &quot;-Y&quot;. In this case the black border height has to be recalculated by applying the aspect ratio 4:3 to the value alreadyfound: 60 * (4/3) = 80. The transcode options &quot;-j -80,0,-80,0&quot; or &quot;&#8211;pre_clip -80,0,-80,0&quot; are then used instead of &quot;-Y -60,0,-60,0&quot;, and &quot;-Z 480&#215;360,fast&quot; is replaced by &quot;-Z 480&#215;480,fast&quot;.</dl>
<h2>AUTHORS</h2>
<p> Written by Thomas Oestreich &lt;ostreich [at] theorie.physik.uni-goettingen.de&gt;, Tilmann Bitterberg and the Transcode-Team </p>
<p> See the <i>AUTHORS</i> file for details.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-transcode_export/">transcode_export</a></code>(1) , <code><a href="/docs/linux/man/1-transcode_filter/">transcode_filter</a></code>(1) , <code><a href="/docs/linux/man/1-transcode_import/">transcode_import</a></code>(1) , <code><a href="/docs/linux/man/1-avifix/">avifix</a></code>(1) , <code><a href="/docs/linux/man/1-avisync/">avisync</a></code>(1) , <code><a href="/docs/linux/man/1-avimerge/">avimerge</a></code>(1) , <code><a href="/docs/linux/man/1-avisplit/">avisplit</a></code>(1) , <code><a href="/docs/linux/man/1-tcprobe/">tcprobe</a></code>(1) , <code><a href="/docs/linux/man/1-tcscan/">tcscan</a></code>(1) , <code><a href="/docs/linux/man/1-tccat/">tccat</a></code>(1) , <code><a href="/docs/linux/man/1-tcdemux/">tcdemux</a></code>(1) , <code><a href="/docs/linux/man/1-tcextract/">tcextract</a></code>(1) , <code><a href="/docs/linux/man/1-tcdecode/">tcdecode</a></code>(1) , <code><a href="/docs/linux/man/1-tcmodinfo/">tcmodinfo</a></code>(1) , <code><a href="/docs/linux/man/1-tcxmlcheck/">tcxmlcheck</a></code>(1) , <code><a href="/docs/linux/man/1-transcode/">transcode</a></code>(1)</p>
<h2>WWW</h2>
<p> Frequently asked questions (FAQ) at <i> <a rel="nofollow" href="http://www.transcoding.org/cgi-bin/transcode?Transcode_FAQ">http://www.transcoding.org/cgi-bin/transcode?Transcode_FAQ</a> </i>[1] Example transcode sessions at <i> <a rel="nofollow" href="http://www.transcoding.org/cgi-bin/transcode?Command_Examples">http://www.transcoding.org/cgi-bin/transcode?Command_Examples</a> </i>[1]</p>
<h2>BUGS</h2>
<p> Yes, there are bugs in transcode! Do your part and report them immediately. </p>
<p> For details, see <i> <a rel="nofollow" href="http://www.transcoding.org/cgi-bin/transcode?Reporting_Problems">http://www.transcoding.org/cgi-bin/transcode?Reporting_Problems</a> </i>[1]</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> <a rel="nofollow" href="http://www.mp3dev.org/mp3/doc/html/presets.html)">http://www.mp3dev.org/mp3/doc/html/presets.html)</a></p>
<dl>
<dt>
<dd> a</dl>
</dl>
<h2>Index</h2>
