---
title: "lavrec(1)"
name: "lavrec"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lavrec/"
description: "lavrec – Record MJPEG-video from a zoran/video4linux-device"
---

<h2 class="name">NAME</h2>
<p> lavrec &#8211; Record MJPEG-video from a zoran/video4linux-device</p>
<h2>SYNOPSIS</h2>
<p> <code>lavrec</code> [<i>options</i>] <i>filename(s)</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>lavrec</code> can be used to record video in MJPEG format (either quicktime or AVI) from a zoran video-capture device, such as the Miro/Pinnacle DC10(+), the Iomega Buz or Linux Media Labs&#8217; LML33, or from a generic video4linux device, such as the cheap Bt848 or Bt878 based TV-cards that are being sold in every computer shop around the corner. </p>
<h2>OPTIONS</h2>
<p> <code>lavrec</code> accepts the following options: </p>
<dl>
<dt><code>filename</code></p>
<dd> The file to record to (*.avi, *.qt). Use a % to record to multiple files (using file%02d.avi will record to file00.avi, file01.avi, etc). You can also give more than one filename, which will have the same effect. This will avoid problems resulting from filetype or filesystem size limits. AVI, for example, has a 2 GB limit, as does ext2fs in 2.2.x kernels. </p>
<dt><code>&#8211;software-encoding</code></p>
<dd> By default, lavrec will capture in a mode that is only suitable for recording from hardware MJPEG devices. Using this option will make lavrec use software-JPEG-encoding (using libjpeg) which enables MJPEG-video-capture from many generic video4linux devices (such as Bt848/Bt878-based ones). </p>
<dt><code>&#8211;software-encoding-yuvp</code></p>
<dd> This option adds support for the EM28XX USB driver. As this driver is V4L2. As the original BTTV software implementation assumes that the driver supports V4L it will not work with the EM28XX driver, not even with the V4L1 emulation layer. This option enables two things:<br />
&nbsp;<wbr>&nbsp;<wbr>It enables the V4L2 calls to make interaction with this driver possible<br />
&nbsp;<wbr>&nbsp;<wbr>It select the cards YUV Packed format and converts this in software to YUV Planar The process is after this the same as for the BTTV driver. ome things of note are the fact that the EM28XX driver expects 48KHz audio recording. If you choose slower things will work, but a lot of deleted/inserted frames will occur. The lower the sample rate, the worse this problem gets. Recording at 48KHz is therefore recommended. This code was tested and found working with a DVC100 Pinnacle Dazzle. This option should work with any EM28XX, but this hasnt been tested. It might work for any other V4L2 device that outputs YUV packed format, this has however not been tested. Feedback would be appreciated. </p>
<dt><code>-f/&#8211;format</code> [<code>a</code>|<code>A</code>|<code>q</code>|<code>m</code>]</p>
<dd> The format in which the video should be saved to the harddisk.<br />
&nbsp;<wbr>&nbsp;<wbr>a &#8211; MJPEG AVI<br />
&nbsp;<wbr>&nbsp;<wbr>A &#8211; MJPEG AVI with fields exchanged<br />
&nbsp;<wbr>&nbsp;<wbr>q &#8211; Quicktime<br />
 By default, lavrec will look at the extension of the first file (*.avi, *.qt) and choose a format based on that. </p>
<dt><code>-i/&#8211;input</code> [<code>p</code>|<code>P</code>|<code>n</code>|<code>N</code>|<code>s</code>|<code>S</code>|<code>t</code>|<code>T</code>|<code>f</code>|<code>a</code>]</p>
<dd> or</p>
<dt><code>-i/&#8211;input</code> input[:norm]</p>
<dd> The recording source and the video source standard format.<br />
&nbsp;<wbr>p &#8211; PAL through Composite or 1st Bt8x8 input<br />
&nbsp;<wbr>P &#8211; PAL through SVHS- or 2nd Bt8x8 input<br />
&nbsp;<wbr>t &#8211; PAL through TV-tuner- or 3rd Bt8x8 input<br />
&nbsp;<wbr>n &#8211; NTSC through Composite or 1st Bt8x8 input<br />
&nbsp;<wbr>N &#8211; NTSC through SVHS- or 2nd Bt8x8 input<br />
&nbsp;<wbr>T &#8211; NTSC through TV-tuner- or 3rd Bt8x8 input<br />
&nbsp;<wbr>s &#8211; SECAM through Composite or 1st Bt8x8 input<br />
&nbsp;<wbr>S &#8211; SECAM through SVHS- or 2nd Bt8x8 input<br />
&nbsp;<wbr>f &#8211; SECAM through TV-tuner- or 3rd Bt8x8 input<br />
&nbsp;<wbr>a &#8211;&nbsp;<wbr>(or every other letter)&nbsp;<wbr>Autosense&nbsp;<wbr>(default)<br />
 The input can be specified using either single letters or an input number with an optional norm, where the number specifies the n&#8217;th input of the card, ranging from 1 to 10. Using a numerical input is necessary when using input four or higher with a card that has more than three inputs, for instance the AverMedia 6 Eyes. When using numeric input with the norm it must contain the whole norm name; valid names are pal, ntsc and secam. You can use numeric input selection for cards with only three inputs, too, which most Zoran based cards has. &quot;-i 2:pal&quot; used with a Buz would be equivalent to &quot;-i P&quot;, recording from the S-Video input in PAL format. </p>
<dt><code>-d/&#8211;decimation</code><i> num</i></p>
<dd> Recording decimation, either 1, 2 or 4. This will decimate the size of the recorded video horizontally and vertically. To use different horizontal and vertical decimations, use two numbers, the first one being the horizontal and the second one being the vertical (-d 12). <code>Note:</code> this option can only be used during hardware recording. </p>
<dt><code>-g/&#8211;geometry</code><i> WxH(+X+Y)</i></p>
<dd> <code>For hardware recording:</code> An X-style geometry string, giving the geometry of the undecimated subframe to record. The default is the full frame, so 720&#215;576/480+0+0 for Buz/LML33-users and 640&#215;480+0+0 or 768&#215;576+0+0 for DC10(+)-users. <code>For software recording:</code> The size of the video to be captured. Currently, width and height need to be a multiple of 16. You always capture the full frame since most video4linux devices don&#8217;t support subframe capture. </p>
<dt><code>-q/&#8211;quality</code><i> num</i></p>
<dd> Quality of the JPEG-video to be recorded (in percent). This must be a number between 0 and 100. Lower quality should generally mean lower filesize, higher quality will take more diskspace but will give more detailed perfectness in the resulting recorded video. Default is 50%. </p>
<dt><code>-C/&#8211;channel</code><i> LIST:CHAN</i></p>
<dd> Choose the channel to record from (xawtv-style). By default, lavrec will just use the current TV channel. </p>
<dt><code>-t/&#8211;time</code><i> num</i></p>
<dd> Recording time in seconds. The default is unlimited. To stop capturing video while recording, use Ctrl-C. </p>
<dt><code>-S/&#8211;single-frame</code></p>
<dd> Single-frame capture mode. This means that one can capture individual frames from the capture device. </p>
<dt><code>-T/&#8211;time-lapse</code><i> num</i></p>
<dd> time-lapse factor, which means that only every &lt;num&gt;th frame is saved to the recording file. </p>
<dt><code>-w/&#8211;wait</code></p>
<dd> If this option is given, lavrec will wait for the user to press enter before starting to record. </p>
<dt><code>-B/&#8211;batch</code></p>
<dd> This option turns off all possible interactivity options and limits console output as much as possible. Useful for cron/scheduled recordings. </p>
<dt><code>-a/&#8211;audio-bitsize</code><i> num</i></p>
<dd> Audio size in bits, either 0, 8 or 16 (default). 0 means no audio.</p>
<dt>
<dd> <code>-r/&#8211;audio-bitrate</code><i> num</i> Audio sampling rate in Hz. This must be a sampling rate which is supported by the soundcard. Often-supported audio sampling rate values are 11025, 22050 or 44100 (default). </p>
<dt><code>-s/&#8211;stereo</code></p>
<dd> Capture in stereo. By default, lavrec captures in mono.</p>
<dt>
<dd> <code>-l/&#8211;audio-volume</code><i> num</i> Recording level. This must be a value between 0 (no sound) and 100 (loud recording). -1 (default) means to not touch the mixer settings at all. </p>
<dt><code>-m/&#8211;mute</code></p>
<dd> Mute sound output while recording. This can be useful when recording sound from the microphone to disable echos. This option is disabled by default. </p>
<dt><code>-R/&#8211;audio-source</code> [<code>l</code>|<code>m</code>|<code>c</code>]</p>
<dd> Recording source, either (l)ine-in, (m)icrophone or (c)d-rom. The default is to record from line-in (l). </p>
<dt><code>-U/&#8211;use-read</code></p>
<dd> Use the read() system call rather than the mmap() system call for audio recording. This may fix many audio recording problems. </p>
<dt><code>-c/&#8211;synchronization</code> [<code>0</code>|<code>1</code>|<code>2</code>]</p>
<dd> Audio/video synchronization level efforts. (0) means no synchronization, (1) means that lavrec will replicate frames for lost frames. (2) means that lavrec will replicate frames for lost frames and do sync correction. Default is 2. </p>
<dt><code>-n/&#8211;mjpeg-buffers</code><i> num</i></p>
<dd> Number of MJPEG-buffers. Default is 32. Try changing this number if you have many lost frames. </p>
<dt><code>-b/&#8211;mjpeg-buffer-size</code><i> num</i></p>
<dd> MJPEG buffersize in kilobytes. The default is 256 kB. </p>
<dt><code>&#8211;max-file-size</code><i> num</i></p>
<dd> The maximum file size per JPEG file. By default, lavrec uses the maximum possible size for that specific recording format. </p>
<dt><code>&#8211;max-file-frames</code><i> num</i></p>
<dd> The maximum number of frames per per JPEG file. By default, the number of frames is only limited by other factors, such as maximum file size. </p>
<dt><code>&#8211;file-flush</code><i> num</i></p>
<dd> Flush the file to disk after every num frames captured. </p>
<dt><code>-v/&#8211;verbose</code><i> num</i></p>
<dd> Verbosity level (0, 1 or 2). Default is 0. </p>
</dl>
<h2>ENVIRONMENT</h2>
<p> The following environment variables can be recognized by lavrec:</p>
<dl>
<dt><code>LAV_VIDEO_DEV</code></p>
<dd> The video device. Default is /dev/video</p>
<dt><code>LAV_AUDIO_DEV</code></p>
<dd> The audio device. Default is /dev/dsp</p>
<dt><code>LAV_MIXER_DEV</code></p>
<dd> The mixer device. Default is /dev/mixer </p>
</dl>
<h2>OUTPUT</h2>
<p> Lavrec will output the current recording state. Typically, this looks like:<br />
 0.06.14:22 int: 00040 lst:0 ins:0 del:0 ae:0 td1=0.014 td2=0.029<br />
 The first part is the time that has been spent recording (hours &#8211; minutes &#8211; seconds &#8211; frames). <code>int</code> is the interval (in milliseconds) between two captured frames (this should be around 40 for PAL/SECAM and 33 for NTSC). <code>lst</code> is the number of lost frames. <code>ins</code> and <code>del</code> are the number of frames inserted and deleted for sync correction. <code>ae</code> is the number of audio errors. <code>td1</code> and <code>td2</code> are the audio/video time-difference (out-of-sync&#8217;ness). </p>
<h2>TYPICAL RECORDING SESSIONS</h2>
<p> Okay, that&#8217;s a lot of options. Now how would I normally record video? Let&#8217;s assume you want to record at VCD resolution (352&#215;288) from PAL source. You might want some higher quality than default (80%). You use default audio options and record to an AVI file. That having said, your recording command line would look like:</p>
<dl>
<dt><code>From hardware MJPEG devices (S-video input)</code></p>
<dd> lavrec &#8211;format=a &#8211;input=P &#8211;quality=80 &#8211;decimation=2 /path/to/file.avi</p>
<dt><code>From normal video4linux devices</code></p>
<dd> lavrec &#8211;software-encoding &#8211;format=a &#8211;input=p &#8211;quality=80 &#8211;geometry=352&#215;288 /path/to/file.avi </p>
</dl>
<h2>BUGS</h2>
<p> lavrec should be able to detect automatically whether to use software JPEG encoding or whether to use the card&#8217;s hardware JPEG encoding features (if available). </p>
<p> Besides that, software JPEG encoding seems, for some people, to cause small out-of-sync&#8217;ness. SMP support for JPEG encoding is currently work-in-progress. </p>
<h2>AUTHOR</h2>
<p> This man page was written by Ronald Bultje.<br />
 If you have questions, remarks, problems or you just want to contact the developers, the main mailing list for the MJPEG-tools is: </p>
<p>&nbsp;<wbr><i>mjpeg-users [at] lists.sourceforge.net</i> </p>
<p> For more info, see our website at </p>
<p>&nbsp;<wbr><i><a rel="nofollow" href="http://mjpeg.sourceforge.net/">http://mjpeg.sourceforge.net/</a></i> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mjpegtools/">mjpegtools</a></code>(1), <code><a href="/docs/linux/man/1-lavplay/">lavplay</a></code>(1) </p>
<h2>Index</h2>
