---
title: "dvgrab(1)"
name: "dvgrab"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dvgrab/"
description: "dvgrab — Capture DV or MPEG-2 Transport Stream (HDV) video and audio data from FireWire"
---

<h2 class="name">NAME</h2>
<p> dvgrab &#8212; Capture DV or MPEG-2 Transport Stream (HDV) video and audio data from FireWire</p>
<h2>SYNOPSIS</h2>
<p> <code>dvgrab</code> [<i>options</i>] [<i>base</i>] [-] </p>
<h2>DESCRIPTION</h2>
<p> <code>dvgrab</code> is a program that captures DV or HDV (MPEG2-TS) video and audio data from digital camcorders via FireWire (IEEE 1394). The data is stored in one or several files and can later be processed by video editing software. <code>dvgrab</code> can remote control the camcorder but it does not show the video&#8217;s content on screen. </p>
<p> <code>dvgrab</code> also supports UVC (USB Video Class) compliant DV devices using Linux kernel module uvcvideo, which is a V4L2 driver. In this mode, there is no AV/C VTR control and therefore interactive mode is almost useless. interactive feature is </p>
<p> The <i>base</i> argument is used to construct the filename to store video data: <i>base</i>&#8211;<i>num</i>.<i>ext</i>. <i>num</i> is a running number starting from 001, and <i>ext</i> is the file name extension specifying the file format used, e.g. avi. A different naming scheme is used whenever the <code>-timestamp</code>, <code>-timecode</code>, or <code>-timesys</code> is given (see below). If <i>base</i> is a full filename including extension, then <code>dvgrab</code> attempts to determine the output file format from the extension, but it still inserts <i>num</i>. The default value for <i>base</i> is &quot;dvgrab-&quot;. </p>
<p> If you specify a trailing &#8216;-&#8216; then the format is forced to raw DV or HDV and sent to stdout. <code>dvgrab</code> will also output raw DV or HDV to stdout while capturing to a file if stdout is piped or redirected. </p>
<p> You can use <code>dvgrab&#8217;s</code> powerful file writing capabilities with other programs that produce raw DV or HDV. Using the <code>-stdin</code> option and if <code>dvgrab</code> detects that it is on the receiving end of a pipe and it is not in interactive mode, then it will try to read raw DV or HDV on stdin. </p>
<h2>OPTIONS</h2>
<p> Options longer than a single character can be specified with either one or two leading hyphens. Also, you can use a space character or equal sign to separate the option name and its argument value. </p>
<dl>
<dt><code>-a[</code><i>num</i>], -autosplit[=<i>num</i>]</p>
<dd> Try to detect whenever a new recording starts, and store it into a separate file. This can be combined with the <code>-frames</code> and <code>-size</code> options, and a split occurs whenever a specified event arises. Autosplit is off by default.</p>
<dt>
<dd> <i>num</i> is optional. Without it, <code>dvgrab</code> determines when to split using a flag in the stream or a discontinuity in the timecode, where timecode discontinuity is anything backwards or greater than one second. If you set the optional argument <i>num</i> you can set the time sensitivity in seconds and ignore the stream&#8217;s new-recording flag. This basically lets you split on larger time increments such as minutes or hours. For example, <i>-autosplit=3600</i> splits the recording whenever there is a gap in the recording that is an hour or longer. </p>
<dt><code>-buffers </code><i>num</i></p>
<dd> The number of frames to use for buffering device I/O delays. Defaults to 100. </p>
<dt><code>-card </code><i>num</i></p>
<dd> Tells <code>dvgrab</code> to receive data from FireWire card <i>num</i>. The default behaviour is to automatically select the first card containing the first discovered camera If used in conjunction with <code>-noavc</code>, then no bus probing is performed If used in conjunction with <code>-guid</code> <i>hex</i>, then only the specified bus is probed for node with guid <i>hex</i>. </p>
<dt><code>-channel </code><i>num</i></p>
<dd> Isochronous channel to receive data from. Defaults to 63, which is pretty much standard among DV camcorders these days. If you specify anything different, no attempt is made at this time to tell the device which channel to use. You must have some manual way to tell the transmitting device which channel to use.<br />
&nbsp;<wbr></p>
<dt><code>-cmincutsize </code><i>num</i></p>
<dd> This option is used to start the collection if a cut occurs <i>num</i> megabytes (actually, mebibytes) prior to the end of the collection. This option reduces small files being created when using the <code>-csize</code> option. When a new collection is started in this manner, the amount of free space in the previous collection is stored, and while the following clips fit within the previous collection, the new collection starting point is reset. </p>
<dt><code>-csize </code><i>num</i></p>
<dd> This option tells <code>dvgrab</code> to split the files when the collection of files exceeds <i>num</i> . This option is used to create collections of files that fit perfectly into <i>num</i> megabytes (actually, mebibytes) (i.e. for archiving onto DVD). When this occurs, a new collection is started (See also the <code>-cmincutsize</code> option) </p>
<dt><code>-debug </code><i>type</i></p>
<dd> Display HDV debug info, <i>type</i> is one or more of: all,pat,pmt,pids,pid=N,pes,packet,video,sonya1 </p>
<dt><code>-d, -duration </code><i>time</i></p>
<dd> Set the maximum capture duration across all file splits for a single capture session (multiple sessions are possible in interactive mode). The <i>time</i> value is expressed in SMIL2 MediaClipping Time format. See <a rel="nofollow" href="http://w3.org/AudioVideo/">http://w3.org/AudioVideo/</a> for the specification.</p>
<dt>
<dd> Briefly, the formats are:</p>
<dt>
<dd> XXX[.Y]h, XXX[.Y]min, XXX[.Y][s], XXXms,</p>
<dt>
<dd> [[HH:]MM:]SS[.ms], or smpte=[[[HH:]MM:]SS:]FF. </p>
<dt><code>-every </code><i>n</i></p>
<dd> This option tells <code>dvgrab</code> to write every <i>n</i>&#8216;th frame only (default all frames).<br />
&nbsp;<wbr></p>
<dt><code>-f, -format </code><i>dv1</i> | <i>dv2</i> | <i>avi</i> | <i>raw</i> | <i>dif</i> | <i>qt</i> | <i>mov</i> | <i>jpeg</i> | <i>jpg</i> | <i>mpeg2</i> | <i>hdv</i></p>
<dd> Specifies the format of the output file(s). File format can also be determined if you include an extension on the <i>base</i> name. The following extensions are recognizable: avi, dv, dif, mov, jpg, jpeg, and m2t (HDV). </p>
<dt>
<dd> <i>dv1</i> and <i>dv2</i> both are AVI files with slightly different formats. <i>dv2</i> stores a separate audio track in addition to the DV video track, which is more compatible with other applications. <i>dv1</i> only stores a single, integrated DV track since the DV format natively interleaves audio with video. Therefore, while <i>dv1</i> produces smaller output, some applications won&#8217;t grok it and require <i>dv2</i> instead. <code>dvgrab</code> is capable of creating extremely large AVI files&#8212;well over 2 or 4 GB&#8212;however, compatibility with other tools starts to decrease over the 1 GB size.<br />
&nbsp;<wbr></p>
<dt>
<dd> <i>raw</i> stores the data unmodified and have the .dv extension. These files are read by a number of GNU/Linux tools as well as Apple Quicktime.<br />
&nbsp;<wbr></p>
<dt>
<dd> <i>dif</i> is a variation of raw DV that names files with a .dif extension so they can be more immediately loaded into MainConcept MainActor5.<br />
&nbsp;<wbr></p>
<dt>
<dd> <i>qt</i> is Quicktime, but requires that dvgrab be compiled with libquicktime. </p>
<dt>
<dd> <i>jpg</i> or <i>jpeg</i> is for a sequence of JPEG image files if dvgrab was compiled with libdv and jpeglib. This option can only be used with a DV input, not HDV (MPEG2-TS). </p>
<dt>
<dd> <i>mpeg2</i> or <i>hdv</i> is for a MPEG-2 transport stream when using, for example, a HDV camcorder or digital TV settop box. </p>
<dt>
<dd> Defaults to <i>raw</i> </p>
<dt><code>-F, -frames </code><i>num</i></p>
<dd> This option tells <code>dvgrab</code> to store at most <i>num</i> frames per file before splitting to a new file, where <i>num</i> = 0 means ulimited. The corresponding time depends on the video system used. PAL shows 25, NTSC about 30 frames per second.<br />
&nbsp;<wbr></p>
<dt><code>-guid </code><i>hex</i></p>
<dd> If you have more than one DV device, then select one using the node&#8217;s GUID specified in <i>hex</i> (hexadecimal) format. This is the format as displayed in /proc/bus/ieee1394/devices or the new kernel 2.6 /sys filesystem. When you specify a GUID, <code>dvgrab</code> will establish (or overlay) a peer-to-peer connection with the device instead of listening to the device&#8217;s broadcast. If you supply a <i>hex</i> value of 1, then <code>dvgrab</code> attempts to discover the device as well as setup a peer-to-peer connection. This is especially handy with MPEG2-TS settop boxes, which typically require a connection management procedure to start transmitting. </p>
<dt><code>-h, -help</code></p>
<dd> Show summary of options.<br />
&nbsp;<wbr></p>
<dt><code>-I, -input </code><i>file</i></p>
<dd> Read from <i>file</i> instead of FireWire. You can use &#8216;-&#8216; for stdin instead of using <code>-stdin</code>. </p>
<dt><code>-i, -interactive</code></p>
<dd> Make dvgrab interactive where single keypresses on stdin control the camera VTR or start and stop capture. Otherwise, dvgrab runs in session mode, where it immediately starts capture and stops as directed or interrupted (ctrl-c). </p>
<dt><code>-jpeg-deinterlace</code></p>
<dd> If using <code>-format jpeg</code>, deinterlace the output by doubling the lines of the upper field. This is a cheap form of deinterlace that results in an effective 50% loss in resolution. </p>
<dt><code>-jpeg-height </code><i>num</i></p>
<dd> If using <code>-format jpeg</code>, scale the output of the height to <i>num</i> (1 &#8211; 2048). </p>
<dt><code>-jpeg-overwrite </code><i>name</i></p>
<dd> Write to same image file for each frame, instead of creating a sequence of image files. </p>
<dt><code>-jpeg-quality </code><i>num</i></p>
<dd> If using <code>-format jpeg</code>, set the JPEG quality level from 0 (worst) to 100 (best). </p>
<dt><code>-jpeg-temp </code><i>name</i> 10</p>
<dd> Use a temporary file to create the jpeg, rename the file to the target file name when done. Useful when using dvgrab with <code>-jpeg-overwrite</code> for generating a webcam image. </p>
<dt><code>-jpeg-width </code><i>num</i></p>
<dd> If using <code>-format jpeg</code>, scale the output of the width to <i>num</i> (1 &#8211; 2048). </p>
<dt>
<dd> The JPEG scaling width and height must be both either less than or greater than the normal frame size. For example, the scaled size of 700 wide by 525 high yields a nice 4:3 aspect image with square pixels, but it is illegal for NTSC because 700 is less than the normal width of 720 while the height is greater than the normal height of 480. </p>
<dt>
<dd> Since DV uses non-square pixels, it is nice to be able to scale to an image based upon a 4:3 aspect ratio using square pixels. For NTSC, example sizes are 800&#215;600, 640&#215;480, and 320&#215;240. For PAL, example square pixel sizes are 384&#215;270 and 768&#215;540. </p>
<dt><code>-jvc-p25</code></p>
<dd> Remove repeat_first_field flag and set frames per second to 25 to correct a stream recorded in JVC&#8217;s HDV P25 mode. </p>
<dt><code>-lockstep</code></p>
<dd> Align capture to a multiple of <code>-frames</code> based on timecode. This is useful for redundancy, when more than one machine is capturing from the same FireWire device, and you want to ensure each file contains the same footage. To ensure the files from each machine have the same name use the <code>-timecode</code> option and the same <i>base</i> name. </p>
<dt><code>-lockstep_maxdrops </code><i>num</i></p>
<dd> If <i>num</i> frames are dropped consecutively, then close the file and resume capture on the next lockstop interval. If <i>num</i> is -1, then permit an unlimited number of consecutively dropped frames; this is the default. </p>
<dt><code>-lockstep_totaldrops </code><i>num</i></p>
<dd> If <i>num</i> frames are dropped in the current file, then close the file and resume capture on the next lockstep interval. If <i>num</i> is -1, then permit an unlimited number of total dropped frames; this is the default. </p>
<dt><code>-noavc</code></p>
<dd> Disable use of AV/C VTR control. This is useful if you are capturing live video from a camera because in camera mode, an AV/C play command tells the camera to start recording, perhaps over material on the current tape. This applies to either interactive more or non-interactive because non-interactive stills sends a play and stop to the VTR upon capture start and stop. </p>
<dt><code>-nostop</code></p>
<dd> Disables sending the AV/C VTR stop command when exiting <code>dvgrab</code>. </p>
<dt><code>-opendml</code></p>
<dd> If using <code>-format dv2</code>, create an OpenDML-compliant type 2 DV AVI. This is required to support dv2 files &gt;1GB. dv1 always supports files &gt;1GB. </p>
<dt><code>-r, -recordonly</code></p>
<dd> When the camcorder is in record mode, this option causes <code>dvgrab</code> to only capture when the camcorder is recording and not paused. Normally, when in record mode, dvgrab always captures to let you use the camcorder purely as a camera where the computer operator is in control. This option makes dvgrab act like the VCR where the camera operator controls when capture takes place. This is very handy when used with the <code>-autosplit</code> option to automatically create a new file for each shot. This option requires AV/C and will not work with the <code>-noavc</code> option. </p>
<dt><code>-rewind</code></p>
<dd> Rewind the tape completely to the beginning prior to starting capture. Naturally, this requires AV/C; however, perhaps not so obvious is that this does not apply to interactive mode. </p>
<dt><code>-showstatus</code></p>
<dd> Normally, the capture status information is displayed after finished writing to each file. This option makes it show the capture status during capture, updated for each frame. </p>
<dt><code>-s, -size </code><i>num</i></p>
<dd> This option tells <code>dvgrab</code> to store at most <i>num</i> megabytes (actually, mebibytes) per file, where <i>num</i> = 0 means unlimited file size for large files. The default size limit is 1024 MB. </p>
<dt><code>-srt</code></p>
<dd> Generate subtitle files containing the recording date and time in SRT format. For each video file that is created two additional files with the extension .srt0 and .srt1 are created. They contain the recording date and time as subtitles in the SRT format. The .srt0 file contains the subtitles with timing based on the running time from the start of the current file. Use this file if you transcode to a format like AVI. The .srt1 file contains the subtitles with timing based on the time code as delivered by the camera. The mplayer program understands this type of subtitles. </p>
<dt><code>-stdin</code></p>
<dd> Read the DV stream from a pipe on stdin instead of FireWire.<br />
&nbsp;<wbr></p>
<dt><code>-timecode</code></p>
<dd> Put the timecode of the first frame of each file into the file name.<br />
&nbsp;<wbr></p>
<dt><code>-t, -timestamp</code></p>
<dd> Put information on date and time of recording into file name.<br />
&nbsp;<wbr></p>
<dt><code>-timesys</code></p>
<dd> Put system rather than recording date and time into file name. This is useful when using converter devices that do not change the recording date time in the DV stream. </p>
<dt><code>-V, -v4l2</code></p>
<dd> Capture from a USB Video Class (UVC) device that supports DV. This uses the uvcvideo kernel module via V4L2. The default device file is /dev/video. Use the <code>-input</code> option to set a different device file.<br />
&nbsp;<wbr></p>
<dt><code>-v, -version</code></p>
<dd> Show version of program. </p>
<dt><code>-24p</code></p>
<dd> For Quicktime DV, set the frame rate as 24 fps in the Quicktime file. This only works as expected when the video has been shot in 24p mode. </p>
<dt><code>-24pa</code></p>
<dd> For Quicktime, DV, in addition to setting the frame rate to 24 in the Quicktime file, also reverse the 2:3:3:2 pulldown process by removing the interlaced &quot;C&quot; frame. This only works as expected when the video has been shot in 24p Advanced mode. See <a rel="nofollow" href="http://www.adamwilt.com/24p/">http://www.adamwilt.com/24p/</a> </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>dvgrab foo-</code></p>
<dd> Captures video data from the default FireWire source and stores it to files <code>foo-001.avi</code>, <code>foo-002.avi</code>, etc.<br />
&nbsp;<wbr></p>
<dt><code>dvgrab -frames 25 foo-</code></p>
<dd> Assuming a PAL video source, this command records one second&#8217;s worth of video data per file.<br />
&nbsp;<wbr></p>
<dt><code>dvgrab -autosplit -frames 750 -timestamp foo-</code></p>
<dd> Records video data from the default FireWire source, cuts it into chunks of 30 seconds (assuming PAL) or when a new recording starts and names the resulting files according to date and time info in the videostream. </p>
<dt><code>dvgrab -autosplit -size 1998 -csize 4400 -cmincutsize 10 foo-</code></p>
<dd> Records video data from the default FireWire source, cuts it into chunks when a new recording starts or when the current file exceeds 1998 megabytes (actually, mebibytes), or the current collection of files exceeds 4400 megabytes. It also reduces the size of the smallest file made due to a collection size cut to 10 megabytes. </p>
<dt>
<dd> This option is perfect for backing up DV to DVD&#8217;s as 2 Gb is around the maximum file size that (the current) linux implementation of the ISO9660 filesystem can handle! </p>
<dt>
<dd> Warning: It is possible to make ISO9660 filesystems with files greater than 2 Gb, but the current linux IS09660 driver can&#8217;t read them! Newer linux kernels may be able to handle ISO9660 filesystems with filesizes greater than 2 Gb. </p>
<dt><code>dvgrab -format hdv -autosplit</code></p>
<dd> Capture from a HDV camcorder.<br />
&nbsp;<wbr></p>
<dt><code>dvgrab -format mpeg2 -guid 1</code></p>
<dd> Record from a digital TV settop box. </p>
<dt><code>dvgrab -jpeg-over -jpeg-w=320 -jpeg-h=240 -d smpte=1 webcam.jpeg</code></p>
<dd> Capture a single frame, save it as a JPEG named webcam.jpg and exit. This example also demonstrates option handling. You only need to specify enough of a long option name to uniquely identify it. You can use space or equal sign to separate option name and argument. The file format is inferred from the filename extension. Also, since <code>-jpeg-overwrite</code> is used, the filename will be exactly &quot;webcam.jpeg&quot; and not include any numbers.<br />
&nbsp;<wbr></p>
<dt><code>dvgrab -V</code></p>
<dd> Capture over USB from a UVC compliant DV device.<br />
&nbsp;<wbr></p>
<dt><code>dvgrab -v4l -input /dev/video1</code></p>
<dd> Capture over USB from a UVC compliant DV device using device file /dev/video1.<br />
&nbsp;<wbr></p>
<dt><code>dvgrab -format=hdv -autosplit=28800 -srt foo-</code></p>
<dd> Capture from a HDV camcorder, splitting whenever there is a gap in the recording that lasts longer than 8 hours. This will likely generate a separate file for each day (useful for holiday videos). It will also generate subtitle files. Assuming that the files foo-001.m2t and foo-002.m2t are generated, the corresponding subtitle files will be foo-001.srt0, foo-001.srt1 and foo-002.srt0, foo-002.srt1. You can use the subtitle files to show the recording date and time while viewing the video. </p>
</dl>
<h2>AUTHOR</h2>
<p> Dan Dennedy &lt;dan [at] dennedy.org&gt; and Daniel Kobras kobras [at] debian.org&gt; </p>
<p> See <a rel="nofollow" href="http://www.kinodv.org/">http://www.kinodv.org/</a> for more information and support.<br />
&nbsp;<wbr> </p>
<h2>Index</h2>
