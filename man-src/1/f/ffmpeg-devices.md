---
title: "ffmpeg-devices(1)"
name: "ffmpeg-devices"
section: "1"
letter: "f"
url: "/docs/linux/man/1-ffmpeg-devices/"
description: "ffmpeg-devices – FFmpeg devices"
---

<h2 class="name">NAME</h2>
<p> ffmpeg-devices &#8211; FFmpeg devices </p>
<h2>DESCRIPTION</h2>
<p> This document describes the input and output devices provided by the libavdevice library.</p>
<h2>DEVICE OPTIONS</h2>
<p> The libavdevice library provides the same interface as libavformat. Namely, an input device is considered like a demuxer, and an output device like a muxer, and the interface and generic device options are the same provided by libavformat (see the ffmpeg-formats manual). </p>
<p> In addition each input or output device may support so-called private options, which are specific for that component. </p>
<p> Options may be set by specifying &#8211;<i>option</i> <i>value</i> in the FFmpeg tools, or by setting the value explicitly in the device <tt>&quot;AVFormatContext&quot;</tt> options or using the <i>libavutil/opt.h</i> <font SIZE="-1">API</font> for programmatic use.</p>
<h2>INPUT DEVICES</h2>
<p> Input devices are configured elements in FFmpeg which enable accessing the data coming from a multimedia device attached to your system. </p>
<p> When you configure your FFmpeg build, all the supported input devices are enabled by default. You can list all available ones using the configure option &#8220;&#8211;list-indevs&#8221;. </p>
<p> You can disable all the input devices using the configure option &#8220;&#8211;disable-indevs&#8221;, and selectively enable an input device using the option &quot;&#8211;enable-indev=<i></i><font SIZE="-1"><i>INDEV</i></font><i></i>&#8220;, or you can disable a particular input device using the option &#8221;&#8211;disable-indev=<i></i><font SIZE="-1"><i>INDEV</i></font><i></i>&quot;. </p>
<p> The option &#8220;-devices&#8221; of the ff* tools will display the list of supported input devices. </p>
<p> A description of the currently available input devices follows.</p>
<h3>alsa</h3>
<p> <font SIZE="-1">ALSA</font> (Advanced Linux Sound Architecture) input device. </p>
<p> To enable this input device during configuration you need libasound installed on your system. </p>
<p> This device allows capturing from an <font SIZE="-1">ALSA</font> device. The name of the device to capture has to be an <font SIZE="-1">ALSA</font> card identifier. </p>
<p> An <font SIZE="-1">ALSA</font> identifier has the syntax: </p>
<pre><code>
hw : &lt;CARD&gt;[, &lt;DEV&gt;[, &lt;SUBDEV&gt;]]
</code></pre>
<p> where the <i></i><font SIZE="-1"><i>DEV</i></font><i></i> and <i></i><font SIZE="-1"><i>SUBDEV</i></font><i></i> components are optional. </p>
<p> The three arguments (in order: <i></i><font SIZE="-1"><i>CARD</i></font><i></i>,<i></i><font SIZE="-1"><i>DEV</i></font><i></i>,<i></i><font SIZE="-1"><i>SUBDEV</i></font><i></i>) specify card number or identifier, device number and subdevice number (-1 means any). </p>
<p> To see the list of cards currently recognized by your system check the files <i>/proc/asound/cards</i> and <i>/proc/asound/devices</i>. </p>
<p> For example to capture with <code>ffmpeg</code> from an <font SIZE="-1">ALSA</font> device with card id 0, you may run the command: </p>
<pre>
        ffmpeg -f alsa -i hw:0 alsaout.wav
</pre>
<p> For more information see: &lt;<code><a rel="nofollow" href="http://www.alsa-project.org/alsa-doc/alsa-lib/pcm.html">http://www.alsa-project.org/alsa-doc/alsa-lib/pcm.html</a></code>&gt; </p>
<p> <i>Options</i></p>
<dl>
<dt><code>sample_rate</code></p>
<dd> Set the sample rate in Hz. Default is 48000.</p>
<dt><code>channels</code></p>
<dd> Set the number of channels. Default is 2.</dl>
<h3>android_camera</h3>
<p> Android camera input device. </p>
<p> This input devices uses the Android Camera2 <font SIZE="-1">NDK API</font> which is available on devices with <font SIZE="-1">API</font> level 24+. The availability of android_camera is autodetected during configuration. </p>
<p> This device allows capturing from all cameras on an Android device, which are integrated into the Camera2 <font SIZE="-1">NDK API.</font> </p>
<p> The available cameras are enumerated internally and can be selected with the <i>camera_index</i> parameter. The input file string is discarded. </p>
<p> Generally the back facing camera has index 0 while the front facing camera has index 1. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>video_size</code></p>
<dd> Set the video size given as a string such as 640&#215;480 or hd720. Falls back to the first available configuration reported by Android if requested video size is not available or by default.</p>
<dt><code>framerate</code></p>
<dd> Set the video framerate. Falls back to the first available configuration reported by Android if requested framerate is not available or by default (-1).</p>
<dt><code>camera_index</code></p>
<dd> Set the index of the camera to use. Default is 0.</p>
<dt><code>input_queue_size</code></p>
<dd> Set the maximum number of frames to buffer. Default is 5.</dl>
<h3>avfoundation</h3>
<p> AVFoundation input device. </p>
<p> AVFoundation is the currently recommended framework by Apple for streamgrabbing on <font SIZE="-1">OSX</font> &gt;= 10.7 as well as on iOS. </p>
<p> The input filename has to be given in the following syntax: </p>
<p>&#8211; i &#8220;[[VIDEO]:[AUDIO]]&#8221;</p>
<p> The first entry selects the video input while the latter selects the audio input. The stream has to be specified by the device name or the device index as shown by the device list. Alternatively, the video and/or audio input device can be chosen by index using the </p>
<pre>
    B&lt;-video_device_index E&lt;lt&gt;INDEXE&lt;gt&gt;&gt;
</pre>
<p> and/or </p>
<pre>
    B&lt;-audio_device_index E&lt;lt&gt;INDEXE&lt;gt&gt;&gt;
</pre>
<p> , overriding any device name or index given in the input filename. </p>
<p> All available devices can be enumerated by using <code>-list_devices true</code>, listing all device names and corresponding indices. </p>
<p> There are two device name aliases:</p>
<dl>
<dt>&quot;default&quot;</p>
<dd> Select the AVFoundation default device of the corresponding type.</p>
<dt>&quot;none&quot;</p>
<dd> Do not record the corresponding media type. This is equivalent to specifying an empty device name or index.</dl>
<p> <i>Options</i> </p>
<p> AVFoundation supports the following options:</p>
<dl>
<dt><code>-list_devices &lt;TRUE|FALSE&gt;</code></p>
<dd> If set to true, a list of all available input devices is given showing all device names and indices.</p>
<dt><code>-video_device_index &lt;</code><font SIZE="-1"><code>INDEX</code></font><code>&gt;</code></p>
<dd> Specify the video device by its index. Overrides anything given in the input filename.</p>
<dt><code>-audio_device_index &lt;</code><font SIZE="-1"><code>INDEX</code></font><code>&gt;</code></p>
<dd> Specify the audio device by its index. Overrides anything given in the input filename.</p>
<dt><code>-pixel_format &lt;</code><font SIZE="-1"><code>FORMAT</code></font><code>&gt;</code></p>
<dd> Request the video device to use a specific pixel format. If the specified format is not supported, a list of available formats is given and the first one in this list is used instead. Available pixel formats are: <tt>&quot;monob, rgb555be, rgb555le, rgb565be, rgb565le, rgb24, bgr24, 0rgb, bgr0, 0bgr, rgb0,<br />
&nbsp;bgr48be, uyvy422, yuva444p, yuva444p16le, yuv444p, yuv422p16, yuv422p10, yuv444p10,<br />
&nbsp;yuv420p, nv12, yuyv422, gray&quot;</tt></p>
<dt><code>-framerate</code></p>
<dd> Set the grabbing frame rate. Default is <tt>&quot;ntsc&quot;</tt>, corresponding to a frame rate of <tt>&quot;30000/1001&quot;</tt>.</p>
<dt><code>-video_size</code></p>
<dd> Set the video frame size.</p>
<dt><code>-capture_cursor</code></p>
<dd> Capture the mouse pointer. Default is 0.</p>
<dt><code>-capture_mouse_clicks</code></p>
<dd> Capture the screen mouse clicks. Default is 0.</p>
<dt><code>-capture_raw_data</code></p>
<dd> Capture the raw device data. Default is 0. Using this option may result in receiving the underlying data delivered to the AVFoundation framework. E.g. for muxed devices that sends raw <font SIZE="-1">DV</font> data to the framework (like tape-based camcorders), setting this option to false results in extracted video frames captured in the designated pixel format only. Setting this option to true results in receiving the raw <font SIZE="-1">DV</font> stream untouched.</dl>
<p> <i>Examples</i></p>
<dl>
<dt>&bull;</p>
<dd> Print the list of AVFoundation supported devices and exit: </p>
<pre>
        $ ffmpeg -f avfoundation -list_devices true -i &quot;&quot;
</pre>
<dt>&bull;</p>
<dd> Record video from video device 0 and audio from audio device 0 into out.avi: </p>
<pre>
        $ ffmpeg -f avfoundation -i &quot;0:0&quot; out.avi
</pre>
<dt>&bull;</p>
<dd> Record video from video device 2 and audio from audio device 1 into out.avi: </p>
<pre>
        $ ffmpeg -f avfoundation -video_device_index 2 -i &quot;:1&quot; out.avi
</pre>
<dt>&bull;</p>
<dd> Record video from the system default video device using the pixel format bgr0 and do not record any audio into out.avi: </p>
<pre>
        $ ffmpeg -f avfoundation -pixel_format bgr0 -i &quot;default:none&quot; out.avi
</pre>
<dt>&bull;</p>
<dd> Record raw <font SIZE="-1">DV</font> data from a suitable input device and write the output into out.dv: </p>
<pre>
        $ ffmpeg -f avfoundation -capture_raw_data true -i &quot;zr100:none&quot; out.dv
</pre>
</dl>
<h3>bktr</h3>
<p> <font SIZE="-1">BSD</font> video input device. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>framerate</code></p>
<dd> Set the frame rate.</p>
<dt><code>video_size</code></p>
<dd> Set the video frame size. Default is <tt>&quot;vga&quot;</tt>.</p>
<dt><code>standard</code></p>
<dd> Available values are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>pal</code></p>
<dd>
<dt><code>ntsc</code></p>
<dd>
<dt><code>secam</code></p>
<dd>
<dt><code>paln</code></p>
<dd>
<dt><code>palm</code></p>
<dd>
<dt><code>ntscj</code></p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h3>decklink</h3>
<p> The decklink input device provides capture capabilities for Blackmagic DeckLink devices. </p>
<p> To enable this input device, you need the Blackmagic DeckLink <font SIZE="-1">SDK</font> and you need to configure with the appropriate <tt>&quot;--extra-cflags&quot;</tt> and <tt>&quot;--extra-ldflags&quot;</tt>. On Windows, you need to run the <font SIZE="-1">IDL</font> files through <code>widl</code>. </p>
<p> DeckLink is very picky about the formats it supports. Pixel format of the input can be set with <code>raw_format</code>. Framerate and video size must be determined for your device with <code>-list_formats 1</code>. Audio sample rate is always 48 kHz and the number of channels can be 2, 8 or 16. Note that all audio channels are bundled in one single audio track. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>list_devices</code></p>
<dd> If set to <code>true</code>, print a list of devices and exit. Defaults to <code>false</code>. This option is deprecated, please use the <tt>&quot;-sources&quot;</tt> option of ffmpeg to list the available input devices.</p>
<dt><code>list_formats</code></p>
<dd> If set to <code>true</code>, print a list of supported formats and exit. Defaults to <code>false</code>.</p>
<dt><code>format_code &lt;FourCC&gt;</code></p>
<dd> This sets the input video format to the format given by the FourCC. To see the supported values of your device(s) use <code>list_formats</code>. Note that there is a FourCC <code>&#8216;pal &#8216;</code> that can also be used as <code>pal</code> (3 letters). Default behavior is autodetection of the input video format, if the hardware supports it.</p>
<dt><code>raw_format</code></p>
<dd> Set the pixel format of the captured video. Available values are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>auto</code></p>
<dd> This is the default which means 8-bit <font SIZE="-1">YUV 422</font> or 8-bit <font SIZE="-1">ARGB</font> if format autodetection is used, 8-bit <font SIZE="-1">YUV 422</font> otherwise.</p>
<dt><code>uyvy422</code></p>
<dd> 8-bit <font SIZE="-1">YUV 422.</font></p>
<dt><code>yuv422p10</code></p>
<dd> 10-bit <font SIZE="-1">YUV 422.</font></p>
<dt><code>argb</code></p>
<dd> 8-bit <font SIZE="-1">RGB.</font></p>
<dt><code>bgra</code></p>
<dd> 8-bit <font SIZE="-1">RGB.</font></p>
<dt><code>rgb10</code></p>
<dd> 10-bit <font SIZE="-1">RGB.</font></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>teletext_lines</code></p>
<dd> If set to nonzero, an additional teletext stream will be captured from the vertical ancillary data. Both <font SIZE="-1">SD PAL</font> (576i) and <font SIZE="-1">HD</font> (1080i or 1080p) sources are supported. In case of <font SIZE="-1">HD</font> sources, <font SIZE="-1">OP47</font> packets are decoded. </p>
<p> This option is a bitmask of the <font SIZE="-1">SD PAL VBI</font> lines captured, specifically lines 6 to 22, and lines 318 to 335. Line 6 is the <font SIZE="-1">LSB</font> in the mask. Selected lines which do not contain teletext information will be ignored. You can use the special <code>all</code> constant to select all possible lines, or <code>standard</code> to skip lines 6, 318 and 319, which are not compatible with all receivers. </p>
<p> For <font SIZE="-1">SD</font> sources, ffmpeg needs to be compiled with <tt>&quot;--enable-libzvbi&quot;</tt>. For <font SIZE="-1">HD</font> sources, on older (pre-4K) DeckLink card models you have to capture in 10 bit mode.</p>
<dt><code>channels</code></p>
<dd> Defines number of audio channels to capture. Must be <code>2</code>, <code>8</code> or <code>16</code>. Defaults to <code>2</code>.</p>
<dt><code>duplex_mode</code></p>
<dd> Sets the decklink device duplex mode. Must be <code>unset</code>, <code>half</code> or <code>full</code>. Defaults to <code>unset</code>.</p>
<dt><code>timecode_format</code></p>
<dd> Timecode type to include in the frame and video stream metadata. Must be <code>none</code>, <code>rp188vitc</code>, <code>rp188vitc2</code>, <code>rp188ltc</code>, <code>rp188hfr</code>, <code>rp188any</code>, <code>vitc</code>, <code>vitc2</code>, or <code>serial</code>. Defaults to <code>none</code> (not included). </p>
<p> In order to properly support 50/60 fps timecodes, the ordering of the queried timecode types for <code>rp188any</code> is <font SIZE="-1">HFR, VITC1, VITC2</font> and <font SIZE="-1">LTC</font> for &gt;30 fps content. Note that this is slightly different to the ordering used by the DeckLink <font SIZE="-1">API,</font> which is <font SIZE="-1">HFR, VITC1, LTC, VITC2.</font></p>
<dt><code>video_input</code></p>
<dd> Sets the video input source. Must be <code>unset</code>, <code>sdi</code>, <code>hdmi</code>, <code>optical_sdi</code>, <code>component</code>, <code>composite</code> or <code>s_video</code>. Defaults to <code>unset</code>.</p>
<dt><code>audio_input</code></p>
<dd> Sets the audio input source. Must be <code>unset</code>, <code>embedded</code>, <code>aes_ebu</code>, <code>analog</code>, <code>analog_xlr</code>, <code>analog_rca</code> or <code>microphone</code>. Defaults to <code>unset</code>.</p>
<dt><code>video_pts</code></p>
<dd> Sets the video packet timestamp source. Must be <code>video</code>, <code>audio</code>, <code>reference</code>, <code>wallclock</code> or <code>abs_wallclock</code>. Defaults to <code>video</code>.</p>
<dt><code>audio_pts</code></p>
<dd> Sets the audio packet timestamp source. Must be <code>video</code>, <code>audio</code>, <code>reference</code>, <code>wallclock</code> or <code>abs_wallclock</code>. Defaults to <code>audio</code>.</p>
<dt><code>draw_bars</code></p>
<dd> If set to <code>true</code>, color bars are drawn in the event of a signal loss. Defaults to <code>true</code>.</p>
<dt><code>queue_size</code></p>
<dd> Sets maximum input buffer size in bytes. If the buffering reaches this value, incoming frames will be dropped. Defaults to <code>1073741824</code>.</p>
<dt><code>audio_depth</code></p>
<dd> Sets the audio sample bit depth. Must be <code>16</code> or <code>32</code>. Defaults to <code>16</code>.</p>
<dt><code>decklink_copyts</code></p>
<dd> If set to <code>true</code>, timestamps are forwarded as they are without removing the initial offset. Defaults to <code>false</code>.</p>
<dt><code>timestamp_align</code></p>
<dd> Capture start time alignment in seconds. If set to nonzero, input frames are dropped till the system timestamp aligns with configured value. Alignment difference of up to one frame duration is tolerated. This is useful for maintaining input synchronization across N different hardware devices deployed for &#8216;N-way&#8217; redundancy. The system time of different hardware devices should be synchronized with protocols such as <font SIZE="-1">NTP</font> or <font SIZE="-1">PTP,</font> before using this option. Note that this method is not foolproof. In some border cases input synchronization may not happen due to thread scheduling jitters in the <font SIZE="-1">OS.</font> Either sync could go wrong by 1 frame or in a rarer case <code>timestamp_align</code> seconds. Defaults to <code>0</code>.</p>
<dt><code>wait_for_tc (</code><i>bool</i><code>)</code></p>
<dd> Drop frames till a frame with timecode is received. Sometimes serial timecode isn&#8217;t received with the first input frame. If that happens, the stored stream timecode will be inaccurate. If this option is set to <code>true</code>, input frames are dropped till a frame with timecode is received. Option <i>timecode_format</i> must be specified. Defaults to <code>false</code>.</p>
<dt><code>enable_klv(</code><i>bool</i><code>)</code></p>
<dd> If set to <code>true</code>, extracts <font SIZE="-1">KLV</font> data from <font SIZE="-1">VANC</font> and outputs <font SIZE="-1">KLV</font> packets. <font SIZE="-1">KLV VANC</font> packets are joined based on <font SIZE="-1">MID</font> and <font SIZE="-1">PSC</font> fields and aggregated into one <font SIZE="-1">KLV</font> packet. Defaults to <code>false</code>.</dl>
<p> <i>Examples</i></p>
<dl>
<dt>&bull;</p>
<dd> List input devices: </p>
<pre>
        ffmpeg -sources decklink
</pre>
<dt>&bull;</p>
<dd> List supported formats: </p>
<pre>
        ffmpeg -f decklink -list_formats 1 -i 'Intensity Pro'
</pre>
<dt>&bull;</p>
<dd> Capture video clip at 1080i50: </p>
<pre>
        ffmpeg -format_code Hi50 -f decklink -i 'Intensity Pro' -c:a copy -c:v copy output.avi
</pre>
<dt>&bull;</p>
<dd> Capture video clip at 1080i50 10 bit: </p>
<pre>
        ffmpeg -raw_format yuv422p10 -format_code Hi50 -f decklink -i 'UltraStudio Mini Recorder' -c:a copy -c:v copy output.avi
</pre>
<dt>&bull;</p>
<dd> Capture video clip at 1080i50 with 16 audio channels: </p>
<pre>
        ffmpeg -channels 16 -format_code Hi50 -f decklink -i 'UltraStudio Mini Recorder' -c:a copy -c:v copy output.avi
</pre>
</dl>
<h3>dshow</h3>
<p> Windows DirectShow input device. </p>
<p> DirectShow support is enabled when FFmpeg is built with the mingw-w64 project. Currently only audio and video devices are supported. </p>
<p> Multiple devices may be opened as separate inputs, but they may also be opened on the same input, which should improve synchronism between them. </p>
<p> The input name should be in the format: </p>
<p>        &lt;TYPE&gt;=&lt;NAME&gt;[:&lt;TYPE&gt;=&lt;NAME&gt;]</p>
<p> where <i></i><font SIZE="-1"><i>TYPE</i></font><i></i> can be either <i>audio</i> or <i>video</i>, and <i></i><font SIZE="-1"><i>NAME</i></font><i></i> is the device&#8217;s name or alternative name.. </p>
<p> <i>Options</i> </p>
<p> If no options are specified, the device&#8217;s defaults are used. If the device does not support the requested options, it will fail to open.</p>
<dl>
<dt><code>video_size</code></p>
<dd> Set the video size in the captured video.</p>
<dt><code>framerate</code></p>
<dd> Set the frame rate in the captured video.</p>
<dt><code>sample_rate</code></p>
<dd> Set the sample rate (in Hz) of the captured audio.</p>
<dt><code>sample_size</code></p>
<dd> Set the sample size (in bits) of the captured audio.</p>
<dt><code>channels</code></p>
<dd> Set the number of channels in the captured audio.</p>
<dt><code>list_devices</code></p>
<dd> If set to <code>true</code>, print a list of devices and exit.</p>
<dt><code>list_options</code></p>
<dd> If set to <code>true</code>, print a list of selected device&#8217;s options and exit.</p>
<dt><code>video_device_number</code></p>
<dd> Set video device number for devices with the same name (starts at 0, defaults to 0).</p>
<dt><code>audio_device_number</code></p>
<dd> Set audio device number for devices with the same name (starts at 0, defaults to 0).</p>
<dt><code>pixel_format</code></p>
<dd> Select pixel format to be used by DirectShow. This may only be set when the video codec is not set or set to rawvideo.</p>
<dt><code>audio_buffer_size</code></p>
<dd> Set audio device buffer size in milliseconds (which can directly impact latency, depending on the device). Defaults to using the audio device&#8217;s default buffer size (typically some multiple of 500ms). Setting this value too low can degrade performance. See also &lt;<code><a rel="nofollow" href="http://msdn.microsoft.com/en-us/library/windows/desktop/dd377582(v=vs.85).aspx">http://msdn.microsoft.com/en-us/library/windows/desktop/dd377582(v=vs.85).aspx</a></code>&gt;</p>
<dt><code>video_pin_name</code></p>
<dd> Select video capture pin to use by name or alternative name.</p>
<dt><code>audio_pin_name</code></p>
<dd> Select audio capture pin to use by name or alternative name.</p>
<dt><code>crossbar_video_input_pin_number</code></p>
<dd> Select video input pin number for crossbar device. This will be routed to the crossbar device&#8217;s Video Decoder output pin. Note that changing this value can affect future invocations (sets a new default) until system reboot occurs.</p>
<dt><code>crossbar_audio_input_pin_number</code></p>
<dd> Select audio input pin number for crossbar device. This will be routed to the crossbar device&#8217;s Audio Decoder output pin. Note that changing this value can affect future invocations (sets a new default) until system reboot occurs.</p>
<dt><code>show_video_device_dialog</code></p>
<dd> If set to <code>true</code>, before capture starts, popup a display dialog to the end user, allowing them to change video filter properties and configurations manually. Note that for crossbar devices, adjusting values in this dialog may be needed at times to toggle between <font SIZE="-1">PAL</font> (25 fps) and <font SIZE="-1">NTSC</font> (29.97) input frame rates, sizes, interlacing, etc. Changing these values can enable different scan rates/frame rates and avoiding green bars at the bottom, flickering scan lines, etc. Note that with some devices, changing these properties can also affect future invocations (sets new defaults) until system reboot occurs.</p>
<dt><code>show_audio_device_dialog</code></p>
<dd> If set to <code>true</code>, before capture starts, popup a display dialog to the end user, allowing them to change audio filter properties and configurations manually.</p>
<dt><code>show_video_crossbar_connection_dialog</code></p>
<dd> If set to <code>true</code>, before capture starts, popup a display dialog to the end user, allowing them to manually modify crossbar pin routings, when it opens a video device.</p>
<dt><code>show_audio_crossbar_connection_dialog</code></p>
<dd> If set to <code>true</code>, before capture starts, popup a display dialog to the end user, allowing them to manually modify crossbar pin routings, when it opens an audio device.</p>
<dt><code>show_analog_tv_tuner_dialog</code></p>
<dd> If set to <code>true</code>, before capture starts, popup a display dialog to the end user, allowing them to manually modify <font SIZE="-1">TV</font> channels and frequencies.</p>
<dt><code>show_analog_tv_tuner_audio_dialog</code></p>
<dd> If set to <code>true</code>, before capture starts, popup a display dialog to the end user, allowing them to manually modify <font SIZE="-1">TV</font> audio (like mono vs. stereo, Language A,B or C).</p>
<dt><code>audio_device_load</code></p>
<dd> Load an audio capture filter device from file instead of searching it by name. It may load additional parameters too, if the filter supports the serialization of its properties to. To use this an audio capture source has to be specified, but it can be anything even fake one.</p>
<dt><code>audio_device_save</code></p>
<dd> Save the currently used audio capture filter device and its parameters (if the filter supports it) to a file. If a file with the same name exists it will be overwritten.</p>
<dt><code>video_device_load</code></p>
<dd> Load a video capture filter device from file instead of searching it by name. It may load additional parameters too, if the filter supports the serialization of its properties to. To use this a video capture source has to be specified, but it can be anything even fake one.</p>
<dt><code>video_device_save</code></p>
<dd> Save the currently used video capture filter device and its parameters (if the filter supports it) to a file. If a file with the same name exists it will be overwritten.</dl>
<p> <i>Examples</i></p>
<dl>
<dt>&bull;</p>
<dd> Print the list of DirectShow supported devices and exit: </p>
<pre>
        $ ffmpeg -list_devices true -f dshow -i dummy
</pre>
<dt>&bull;</p>
<dd> Open video device <i>Camera</i>: </p>
<pre>
        $ ffmpeg -f dshow -i video=&quot;Camera&quot;
</pre>
<dt>&bull;</p>
<dd> Open second video device with name <i>Camera</i>: </p>
<pre>
        $ ffmpeg -f dshow -video_device_number 1 -i video=&quot;Camera&quot;
</pre>
<dt>&bull;</p>
<dd> Open video device <i>Camera</i> and audio device <i>Microphone</i>: </p>
<pre>
        $ ffmpeg -f dshow -i video=&quot;Camera&quot;:audio=&quot;Microphone&quot;
</pre>
<dt>&bull;</p>
<dd> Print the list of supported options in selected device and exit: </p>
<pre>
        $ ffmpeg -list_options true -f dshow -i video=&quot;Camera&quot;
</pre>
<dt>&bull;</p>
<dd> Specify pin names to capture by name or alternative name, specify alternative device name: </p>
<p>$ ffmpeg &#8211; f dshow &#8211; audio_pin_name &#8220;Audio Out&#8221; &#8211; video_pin_name 2 &#8211; i video = video = &#8220;@device_pnp_\?\pci#ven_1a0a&amp;dev_6200&amp;subsys_62021461&amp;rev_01#4&amp;e2c7dd6&amp;0&amp;00e1#{65e8773d-8f56-11d0-a3b9-00a0c9223196}\{ca465100-deb0-4d59-818f-8c477184adf6}&#8221; : audio = &#8220;Microphone&#8221;</p>
<dt>&bull;</p>
<dd> Configure a crossbar device, specifying crossbar pins, allow user to adjust video capture properties at startup: </p>
<pre>
        $ ffmpeg -f dshow -show_video_device_dialog true -crossbar_video_input_pin_number 0
             -crossbar_audio_input_pin_number 3 -i video=&quot;AVerMedia BDA Analog Capture&quot;:audio=&quot;AVerMedia BDA Analog Capture&quot;
</pre>
</dl>
<h3>fbdev</h3>
<p> Linux framebuffer input device. </p>
<p> The Linux framebuffer is a graphic hardware-independent abstraction layer to show graphics on a computer monitor, typically on the console. It is accessed through a file device node, usually <i>/dev/fb0</i>. </p>
<p> For more detailed information read the file Documentation/fb/framebuffer.txt included in the Linux source tree. </p>
<p> See also &lt;<code><a rel="nofollow" href="http://linux-fbdev.sourceforge.net/">http://linux-fbdev.sourceforge.net/</a></code>&gt;, and <code><a href="/docs/linux/man/1-fbset/">fbset</a></code>(1). </p>
<p> To record from the framebuffer device <i>/dev/fb0</i> with <code>ffmpeg</code>: </p>
<pre>
        ffmpeg -f fbdev -framerate 10 -i /dev/fb0 out.avi
</pre>
<p> You can take a single screenshot image with the command: </p>
<pre>
        ffmpeg -f fbdev -framerate 1 -i /dev/fb0 -frames:v 1 screenshot.jpeg
</pre>
<p> <i>Options</i></p>
<dl>
<dt><code>framerate</code></p>
<dd> Set the frame rate. Default is 25.</dl>
<h3>gdigrab</h3>
<p> Win32 GDI-based screen capture device. </p>
<p> This device allows you to capture a region of the display on Windows. </p>
<p> There are two options for the input filename: </p>
<pre>
        desktop
</pre>
<p> or </p>
<pre>
        title=&lt;window_title&gt;
</pre>
<p> The first option will capture the entire desktop, or a fixed region of the desktop. The second option will instead capture the contents of a single window, regardless of its position on the screen. </p>
<p> For example, to grab the entire desktop using <code>ffmpeg</code>: </p>
<pre>
        ffmpeg -f gdigrab -framerate 6 -i desktop out.mpg
</pre>
<p> Grab a 640&#215;480 region at position <tt>&quot;10,20&quot;</tt>: </p>
<pre>
        ffmpeg -f gdigrab -framerate 6 -offset_x 10 -offset_y 20 -video_size vga -i desktop out.mpg
</pre>
<p> Grab the contents of the window named &#8220;Calculator&#8221; </p>
<pre>
        ffmpeg -f gdigrab -framerate 6 -i title=Calculator out.mpg
</pre>
<p> <i>Options</i></p>
<dl>
<dt><code>draw_mouse</code></p>
<dd> Specify whether to draw the mouse pointer. Use the value <tt>0</tt> to not draw the pointer. Default value is <tt>1</tt>.</p>
<dt><code>framerate</code></p>
<dd> Set the grabbing frame rate. Default value is <tt>&quot;ntsc&quot;</tt>, corresponding to a frame rate of <tt>&quot;30000/1001&quot;</tt>.</p>
<dt><code>show_region</code></p>
<dd> Show grabbed region on screen. </p>
<p> If <i>show_region</i> is specified with <tt>1</tt>, then the grabbing region will be indicated on screen. With this option, it is easy to know what is being grabbed if only a portion of the screen is grabbed. </p>
<p> Note that <i>show_region</i> is incompatible with grabbing the contents of a single window. </p>
<p> For example: </p>
<pre>
        ffmpeg -f gdigrab -show_region 1 -framerate 6 -video_size cif -offset_x 10 -offset_y 20 -i desktop out.mpg
</pre>
<dt><code>video_size</code></p>
<dd> Set the video frame size. The default is to capture the full screen if <i>desktop</i> is selected, or the full window size if <i>title=window_title</i> is selected.</p>
<dt><code>offset_x</code></p>
<dd> When capturing a region with <i>video_size</i>, set the distance from the left edge of the screen or desktop. </p>
<p> Note that the offset calculation is from the top left corner of the primary monitor on Windows. If you have a monitor positioned to the left of your primary monitor, you will need to use a negative <i>offset_x</i> value to move the region to that monitor.</p>
<dt><code>offset_y</code></p>
<dd> When capturing a region with <i>video_size</i>, set the distance from the top edge of the screen or desktop. </p>
<p> Note that the offset calculation is from the top left corner of the primary monitor on Windows. If you have a monitor positioned above your primary monitor, you will need to use a negative <i>offset_y</i> value to move the region to that monitor.</dl>
<h3>iec61883</h3>
<p> FireWire <font SIZE="-1">DV/HDV</font> input device using libiec61883. </p>
<p> To enable this input device, you need libiec61883, libraw1394 and libavc1394 installed on your system. Use the configure option <tt>&quot;--enable-libiec61883&quot;</tt> to compile with the device enabled. </p>
<p> The iec61883 capture device supports capturing from a video device connected via <font SIZE="-1">IEEE1394</font> (FireWire), using libiec61883 and the new Linux FireWire stack (juju). This is the default <font SIZE="-1">DV/HDV</font> input method in Linux Kernel 2.6.37 and later, since the old FireWire stack was removed. </p>
<p> Specify the FireWire port to be used as input file, or &#8220;auto&#8221; to choose the first port connected. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>dvtype</code></p>
<dd> Override autodetection of <font SIZE="-1">DV/HDV.</font> This should only be used if auto detection does not work, or if usage of a different device type should be prohibited. Treating a <font SIZE="-1">DV</font> device as <font SIZE="-1">HDV</font> (or vice versa) will not work and result in undefined behavior. The values <code>auto</code>, <code>dv</code> and <code>hdv</code> are supported.</p>
<dt><code>dvbuffer</code></p>
<dd> Set maximum size of buffer for incoming data, in frames. For <font SIZE="-1">DV,</font> this is an exact value. For <font SIZE="-1">HDV,</font> it is not frame exact, since <font SIZE="-1">HDV</font> does not have a fixed frame size.</p>
<dt><code>dvguid</code></p>
<dd> Select the capture device by specifying its <font SIZE="-1">GUID.</font> Capturing will only be performed from the specified device and fails if no device with the given <font SIZE="-1">GUID</font> is found. This is useful to select the input if multiple devices are connected at the same time. Look at /sys/bus/firewire/devices to find out the GUIDs.</dl>
<p> <i>Examples</i></p>
<dl>
<dt>&bull;</p>
<dd> Grab and show the input of a FireWire <font SIZE="-1">DV/HDV</font> device. </p>
<pre>
        ffplay -f iec61883 -i auto
</pre>
<dt>&bull;</p>
<dd> Grab and record the input of a FireWire <font SIZE="-1">DV/HDV</font> device, using a packet buffer of 100000 packets if the source is <font SIZE="-1">HDV.</font> </p>
<pre>
        ffmpeg -f iec61883 -i auto -dvbuffer 100000 out.mpg
</pre>
</dl>
<h3>jack</h3>
<p> <font SIZE="-1">JACK</font> input device. </p>
<p> To enable this input device during configuration you need libjack installed on your system. </p>
<p> A <font SIZE="-1">JACK</font> input device creates one or more <font SIZE="-1">JACK</font> writable clients, one for each audio channel, with name <i>client_name</i>:input_<i>N</i>, where <i>client_name</i> is the name provided by the application, and <i>N</i> is a number which identifies the channel. Each writable client will send the acquired data to the FFmpeg input device. </p>
<p> Once you have created one or more <font SIZE="-1">JACK</font> readable clients, you need to connect them to one or more <font SIZE="-1">JACK</font> writable clients. </p>
<p> To connect or disconnect <font SIZE="-1">JACK</font> clients you can use the <code>jack_connect</code> and <code>jack_disconnect</code> programs, or do it through a graphical interface, for example with <code>qjackctl</code>. </p>
<p> To list the <font SIZE="-1">JACK</font> clients and their properties you can invoke the command <code>jack_lsp</code>. </p>
<p> Follows an example which shows how to capture a <font SIZE="-1">JACK</font> readable client with <code>ffmpeg</code>. </p>
<pre>
        # Create a JACK writable client with name &quot;ffmpeg&quot;.
        $ ffmpeg -f jack -i ffmpeg -y out.wav
        
        # Start the sample jack_metro readable client.
        $ jack_metro -b 120 -d 0.2 -f 4000
        
        # List the current JACK clients.
        $ jack_lsp -c
        system:capture_1
        system:capture_2
        system:playback_1
        system:playback_2
        ffmpeg:input_1
        metro:120_bpm
        
        # Connect metro to the ffmpeg writable client.
        $ jack_connect metro:120_bpm ffmpeg:input_1
</pre>
<p> For more information read: &lt;<code><a rel="nofollow" href="http://jackaudio.org/">http://jackaudio.org/</a></code>&gt; </p>
<p> <i>Options</i></p>
<dl>
<dt><code>channels</code></p>
<dd> Set the number of channels. Default is 2.</dl>
<h3>kmsgrab</h3>
<p> <font SIZE="-1">KMS</font> video input device. </p>
<p> Captures the <font SIZE="-1">KMS</font> scanout framebuffer associated with a specified <font SIZE="-1">CRTC</font> or plane as a <font SIZE="-1">DRM</font> object that can be passed to other hardware functions. </p>
<p> Requires either <font SIZE="-1">DRM</font> master or <font SIZE="-1">CAP_SYS_ADMIN</font> to run. </p>
<p> If you don&#8217;t understand what all of that means, you probably don&#8217;t want this. Look at <code>x11grab</code> instead. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>device</code></p>
<dd> <font SIZE="-1">DRM</font> device to capture on. Defaults to <code>/dev/dri/card0</code>.</p>
<dt><code>format</code></p>
<dd> Pixel format of the framebuffer. This can be autodetected if you are running Linux 5.7 or later, but needs to be provided for earlier versions. Defaults to <code>bgr0</code>, which is the most common format used by the Linux console and Xorg X server.</p>
<dt><code>format_modifier</code></p>
<dd> Format modifier to signal on output frames. This is necessary to import correctly into some APIs. It can be autodetected if you are running Linux 5.7 or later, but will need to be provided explicitly when needed in earlier versions. See the libdrm documentation for possible values.</p>
<dt><code>crtc_id</code></p>
<dd> <font SIZE="-1">KMS CRTC ID</font> to define the capture source. The first active plane on the given <font SIZE="-1">CRTC</font> will be used.</p>
<dt><code>plane_id</code></p>
<dd> <font SIZE="-1">KMS</font> plane <font SIZE="-1">ID</font> to define the capture source. Defaults to the first active plane found if neither <code>crtc_id</code> nor <code>plane_id</code> are specified.</p>
<dt><code>framerate</code></p>
<dd> Framerate to capture at. This is not synchronised to any page flipping or framebuffer changes &#8211; it just defines the interval at which the framebuffer is sampled. Sampling faster than the framebuffer update rate will generate independent frames with the same content. Defaults to <tt>30</tt>.</dl>
<p> <i>Examples</i></p>
<dl>
<dt>&bull;</p>
<dd> Capture from the first active plane, download the result to normal frames and encode. This will only work if the framebuffer is both linear and mappable &#8211; if not, the result may be scrambled or fail to download. </p>
<pre>
        ffmpeg -f kmsgrab -i - -vf 'hwdownload,format=bgr0' output.mp4
</pre>
<dt>&bull;</p>
<dd> Capture from <font SIZE="-1">CRTC ID 42</font> at 60fps, map the result to <font SIZE="-1">VAAPI,</font> convert to <font SIZE="-1">NV12</font> and encode as H.264. </p>
<pre>
        ffmpeg -crtc_id 42 -framerate 60 -f kmsgrab -i - -vf 'hwmap=derive_device=vaapi,scale_vaapi=w=1920:h=1080:format=nv12' -c:v h264_vaapi output.mp4
</pre>
<dt>&bull;</p>
<dd> To capture only part of a plane the output can be cropped &#8211; this can be used to capture a single window, as long as it has a known absolute position and size. For example, to capture and encode the middle quarter of a 1920&#215;1080 plane: </p>
<pre>
        ffmpeg -f kmsgrab -i - -vf 'hwmap=derive_device=vaapi,crop=960:540:480:270,scale_vaapi=960:540:nv12' -c:v h264_vaapi output.mp4
</pre>
</dl>
<h3>lavfi</h3>
<p> Libavfilter input virtual device. </p>
<p> This input device reads data from the open output pads of a libavfilter filtergraph. </p>
<p> For each filtergraph open output, the input device will create a corresponding stream which is mapped to the generated output. Currently only video data is supported. The filtergraph is specified through the option <code>graph</code>. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>graph</code></p>
<dd> Specify the filtergraph to use as input. Each video open output must be labelled by a unique string of the form &quot;out<i>N</i>&quot;, where <i>N</i> is a number starting from 0 corresponding to the mapped input stream generated by the device. The first unlabelled output is automatically assigned to the &#8220;out0&#8221; label, but all the others need to be specified explicitly. </p>
<p> The suffix &#8220;+subcc&#8221; can be appended to the output label to create an extra stream with the closed captions packets attached to that output (experimental; only for <font SIZE="-1">EIA-608 / CEA-708</font> for now). The subcc streams are created after all the normal streams, in the order of the corresponding stream. For example, if there is &#8220;out19+subcc&#8221;, &#8220;out7+subcc&#8221; and up to &#8220;out42&#8221;, the stream #43 is subcc for stream #7 and stream #44 is subcc for stream #19. </p>
<p> If not specified defaults to the filename specified for the input device.</p>
<dt><code>graph_file</code></p>
<dd> Set the filename of the filtergraph to be read and sent to the other filters. Syntax of the filtergraph is the same as the one specified by the option <i>graph</i>.</p>
<dt><code>dumpgraph</code></p>
<dd> Dump graph to stderr.</dl>
<p> <i>Examples</i></p>
<dl>
<dt>&bull;</p>
<dd> Create a color video stream and play it back with <code>ffplay</code>: </p>
<pre>
        ffplay -f lavfi -graph &quot;color=c=pink [out0]&quot; dummy
</pre>
<dt>&bull;</p>
<dd> As the previous example, but use filename for specifying the graph description, and omit the &#8220;out0&#8221; label: </p>
<pre>
        ffplay -f lavfi color=c=pink
</pre>
<dt>&bull;</p>
<dd> Create three different video test filtered sources and play them: </p>
<p>ffplay &#8211; f lavfi &#8211; graph &#8220;testsrc [out0]; testsrc,hflip [out1]; testsrc,negate [out2]&#8221; test3</p>
<dt>&bull;</p>
<dd> Read an audio stream from a file using the amovie source and play it back with <code>ffplay</code>: </p>
<pre>
        ffplay -f lavfi &quot;amovie=test.wav&quot;
</pre>
<dt>&bull;</p>
<dd> Read an audio stream and a video stream and play it back with <code>ffplay</code>: </p>
<p>ffplay &#8211; f lavfi &#8220;movie=test.avi[out0];amovie=test.wav[out1]&#8221;</p>
<dt>&bull;</p>
<dd> Dump decoded frames to images and closed captions to a file (experimental): </p>
<pre>
        ffmpeg -f lavfi -i &quot;movie=test.ts[out0+subcc]&quot; -map v frame%08d.png -map s -c copy -f rawvideo subcc.bin
</pre>
</dl>
<h3>libcdio</h3>
<p> Audio-CD input device based on libcdio. </p>
<p> To enable this input device during configuration you need libcdio installed on your system. It requires the configure option <tt>&quot;--enable-libcdio&quot;</tt>. </p>
<p> This device allows playing and grabbing from an Audio-CD. </p>
<p> For example to copy with <code>ffmpeg</code> the entire Audio-CD in <i>/dev/sr0</i>, you may run the command: </p>
<pre>
        ffmpeg -f libcdio -i /dev/sr0 cd.wav
</pre>
<p> <i>Options</i></p>
<dl>
<dt><code>speed</code></p>
<dd> Set drive reading speed. Default value is 0. </p>
<p> The speed is specified CD-ROM speed units. The speed is set through the libcdio <tt>&quot;cdio_cddap_speed_set&quot;</tt> function. On many CD-ROM drives, specifying a value too large will result in using the fastest speed.</p>
<dt><code>paranoia_mode</code></p>
<dd> Set paranoia recovery mode flags. It accepts one of the following values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>disable</code></p>
<dd>
<dt><code>verify</code></p>
<dd>
<dt><code>overlap</code></p>
<dd>
<dt><code>neverskip</code></p>
<dd>
<dt><code>full</code></p>
<dd></dl>
</dl>
<dl>
<dt>
<dd>
<p> Default value is <code>disable</code>. </p>
<p> For more information about the available recovery modes, consult the paranoia project documentation.</dl>
</dl>
<h3>libdc1394</h3>
<p> <font SIZE="-1">IIDC1394</font> input device, based on libdc1394 and libraw1394. </p>
<p> Requires the configure option <tt>&quot;--enable-libdc1394&quot;</tt>. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>framerate</code></p>
<dd> Set the frame rate. Default is <tt>&quot;ntsc&quot;</tt>, corresponding to a frame rate of <tt>&quot;30000/1001&quot;</tt>.</p>
<dt><code>pixel_format</code></p>
<dd> Select the pixel format. Default is <tt>&quot;uyvy422&quot;</tt>.</p>
<dt><code>video_size</code></p>
<dd> Set the video size given as a string such as <tt>&quot;640x480&quot;</tt> or <tt>&quot;hd720&quot;</tt>. Default is <tt>&quot;qvga&quot;</tt>.</dl>
<h3>openal</h3>
<p> The OpenAL input device provides audio capture on all systems with a working OpenAL 1.1 implementation. </p>
<p> To enable this input device during configuration, you need OpenAL headers and libraries installed on your system, and need to configure FFmpeg with <tt>&quot;--enable-openal&quot;</tt>. </p>
<p> OpenAL headers and libraries should be provided as part of your OpenAL implementation, or as an additional download (an <font SIZE="-1">SDK</font>). Depending on your installation you may need to specify additional flags via the <tt>&quot;--extra-cflags&quot;</tt> and <tt>&quot;--extra-ldflags&quot;</tt> for allowing the build system to locate the OpenAL headers and libraries. </p>
<p> An incomplete list of OpenAL implementations follows:</p>
<dl>
<dt><code>Creative</code></p>
<dd> The official Windows implementation, providing hardware acceleration with supported devices and software fallback. See &lt;<code><a rel="nofollow" href="http://openal.org/">http://openal.org/</a></code>&gt;.</p>
<dt><code>OpenAL Soft</code></p>
<dd> Portable, open source (<font SIZE="-1">LGPL</font>) software implementation. Includes backends for the most common sound APIs on the Windows, Linux, Solaris, and <font SIZE="-1">BSD</font> operating systems. See &lt;<code><a rel="nofollow" href="http://kcat.strangesoft.net/openal.html">http://kcat.strangesoft.net/openal.html</a></code>&gt;.</p>
<dt><code>Apple</code></p>
<dd> OpenAL is part of Core Audio, the official Mac <font SIZE="-1">OS X</font> Audio interface. See &lt;<code><a rel="nofollow" href="http://developer.apple.com/technologies/mac/audio-and-video.html">http://developer.apple.com/technologies/mac/audio-and-video.html</a></code>&gt;</dl>
<p> This device allows one to capture from an audio input device handled through OpenAL. </p>
<p> You need to specify the name of the device to capture in the provided filename. If the empty string is provided, the device will automatically select the default device. You can get the list of the supported devices by using the option <i>list_devices</i>. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>channels</code></p>
<dd> Set the number of channels in the captured audio. Only the values <code>1</code> (monaural) and <code>2</code> (stereo) are currently supported. Defaults to <code>2</code>.</p>
<dt><code>sample_size</code></p>
<dd> Set the sample size (in bits) of the captured audio. Only the values <code>8</code> and <code>16</code> are currently supported. Defaults to <code>16</code>.</p>
<dt><code>sample_rate</code></p>
<dd> Set the sample rate (in Hz) of the captured audio. Defaults to <code>44.1k</code>.</p>
<dt><code>list_devices</code></p>
<dd> If set to <code>true</code>, print a list of devices and exit. Defaults to <code>false</code>.</dl>
<p> <i>Examples</i> </p>
<p> Print the list of OpenAL supported devices and exit: </p>
<pre>
        $ ffmpeg -list_devices true -f openal -i dummy out.ogg
</pre>
<p> Capture from the OpenAL device <i></i><font SIZE="-1"><i>DR-BT101</i></font><i> via PulseAudio</i>: </p>
<pre>
        $ ffmpeg -f openal -i 'DR-BT101 via PulseAudio' out.ogg
</pre>
<p> Capture from the default device (note the empty string &#8221; as filename): </p>
<pre>
        $ ffmpeg -f openal -i '' out.ogg
</pre>
<p> Capture from two devices simultaneously, writing to two different files, within the same <code>ffmpeg</code> command: </p>
<pre>
        $ ffmpeg -f openal -i 'DR-BT101 via PulseAudio' out1.ogg -f openal -i 'ALSA Default' out2.ogg
</pre>
<p> Note: not all OpenAL implementations support multiple simultaneous capture &#8211; try the latest OpenAL Soft if the above does not work.</p>
<h3>oss</h3>
<p> Open Sound System input device. </p>
<p> The filename to provide to the input device is the device node representing the <font SIZE="-1">OSS</font> input device, and is usually set to <i>/dev/dsp</i>. </p>
<p> For example to grab from <i>/dev/dsp</i> using <code>ffmpeg</code> use the command: </p>
<pre>
        ffmpeg -f oss -i /dev/dsp /tmp/oss.wav
</pre>
<p> For more information about <font SIZE="-1">OSS</font> see: &lt;<code><a rel="nofollow" href="http://manuals.opensound.com/usersguide/dsp.html">http://manuals.opensound.com/usersguide/dsp.html</a></code>&gt; </p>
<p> <i>Options</i></p>
<dl>
<dt><code>sample_rate</code></p>
<dd> Set the sample rate in Hz. Default is 48000.</p>
<dt><code>channels</code></p>
<dd> Set the number of channels. Default is 2.</dl>
<h3>pulse</h3>
<p> PulseAudio input device. </p>
<p> To enable this output device you need to configure FFmpeg with <tt>&quot;--enable-libpulse&quot;</tt>. </p>
<p> The filename to provide to the input device is a source device or the string &#8220;default&#8221; </p>
<p> To list the PulseAudio source devices and their properties you can invoke the command <code>pactl list sources</code>. </p>
<p> More information about PulseAudio can be found on &lt;<code><a rel="nofollow" href="http://www.pulseaudio.org">http://www.pulseaudio.org</a></code>&gt;. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>server</code></p>
<dd> Connect to a specific PulseAudio server, specified by an <font SIZE="-1">IP</font> address. Default server is used when not provided.</p>
<dt><code>name</code></p>
<dd> Specify the application name PulseAudio will use when showing active clients, by default it is the <tt>&quot;LIBAVFORMAT_IDENT&quot;</tt> string.</p>
<dt><code>stream_name</code></p>
<dd> Specify the stream name PulseAudio will use when showing active streams, by default it is &#8220;record&#8221;.</p>
<dt><code>sample_rate</code></p>
<dd> Specify the samplerate in Hz, by default 48kHz is used.</p>
<dt><code>channels</code></p>
<dd> Specify the channels in use, by default 2 (stereo) is set.</p>
<dt><code>frame_size</code></p>
<dd> Specify the number of bytes per frame, by default it is set to 1024.</p>
<dt><code>fragment_size</code></p>
<dd> Specify the minimal buffering fragment in PulseAudio, it will affect the audio latency. By default it is unset.</p>
<dt><code>wallclock</code></p>
<dd> Set the initial <font SIZE="-1">PTS</font> using the current time. Default is 1.</dl>
<p> <i>Examples</i> </p>
<p> Record a stream from default device: </p>
<pre>
        ffmpeg -f pulse -i default /tmp/pulse.wav
</pre>
<h3>sndio</h3>
<p> sndio input device. </p>
<p> To enable this input device during configuration you need libsndio installed on your system. </p>
<p> The filename to provide to the input device is the device node representing the sndio input device, and is usually set to <i>/dev/audio0</i>. </p>
<p> For example to grab from <i>/dev/audio0</i> using <code>ffmpeg</code> use the command: </p>
<pre>
        ffmpeg -f sndio -i /dev/audio0 /tmp/oss.wav
</pre>
<p> <i>Options</i></p>
<dl>
<dt><code>sample_rate</code></p>
<dd> Set the sample rate in Hz. Default is 48000.</p>
<dt><code>channels</code></p>
<dd> Set the number of channels. Default is 2.</dl>
<h3>video4linux2, v4l2</h3>
<p> Video4Linux2 input video device. </p>
<p> &#8220;v4l2&#8221; can be used as alias for &#8220;video4linux2&#8221;. </p>
<p> If FFmpeg is built with v4l-utils support (by using the <tt>&quot;--enable-libv4l2&quot;</tt> configure option), it is possible to use it with the <tt>&quot;-use_libv4l2&quot;</tt> input device option. </p>
<p> The name of the device to grab is a file device node, usually Linux systems tend to automatically create such nodes when the device (e.g. an <font SIZE="-1">USB</font> webcam) is plugged into the system, and has a name of the kind <i>/dev/videoN</i>, where <i>N</i> is a number associated to the device. </p>
<p> Video4Linux2 devices usually support a limited set of <i>width</i>x<i>height</i> sizes and frame rates. You can check which are supported using <code>-list_formats all</code> for Video4Linux2 devices. Some devices, like <font SIZE="-1">TV</font> cards, support one or more standards. It is possible to list all the supported standards using <code>-list_standards all</code>. </p>
<p> The time base for the timestamps is 1 microsecond. Depending on the kernel version and configuration, the timestamps may be derived from the real time clock (origin at the Unix Epoch) or the monotonic clock (origin usually at boot time, unaffected by <font SIZE="-1">NTP</font> or manual changes to the clock). The <code>-timestamps abs</code> or <code>-ts abs</code> option can be used to force conversion into the real time clock. </p>
<p> Some usage examples of the video4linux2 device with <code>ffmpeg</code> and <code>ffplay</code>:</p>
<dl>
<dt>&bull;</p>
<dd> List supported formats for a video4linux2 device: </p>
<pre>
        ffplay -f video4linux2 -list_formats all /dev/video0
</pre>
<dt>&bull;</p>
<dd> Grab and show the input of a video4linux2 device: </p>
<pre>
        ffplay -f video4linux2 -framerate 30 -video_size hd720 /dev/video0
</pre>
<dt>&bull;</p>
<dd> Grab and record the input of a video4linux2 device, leave the frame rate and size as previously set: </p>
<pre>
        ffmpeg -f video4linux2 -input_format mjpeg -i /dev/video0 out.mpeg
</pre>
</dl>
<p> For more information about Video4Linux, check &lt;<code><a rel="nofollow" href="http://linuxtv.org/">http://linuxtv.org/</a></code>&gt;. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>standard</code></p>
<dd> Set the standard. Must be the name of a supported standard. To get a list of the supported standards, use the <code>list_standards</code> option.</p>
<dt><code>channel</code></p>
<dd> Set the input channel number. Default to -1, which means using the previously selected channel.</p>
<dt><code>video_size</code></p>
<dd> Set the video frame size. The argument must be a string in the form <i></i><font SIZE="-1"><i>WIDTH</i></font><i></i>x<i></i><font SIZE="-1"><i>HEIGHT</i></font><i></i> or a valid size abbreviation.</p>
<dt><code>pixel_format</code></p>
<dd> Select the pixel format (only valid for raw video input).</p>
<dt><code>input_format</code></p>
<dd> Set the preferred pixel format (for raw video) or a codec name. This option allows one to select the input format, when several are available.</p>
<dt><code>framerate</code></p>
<dd> Set the preferred video frame rate.</p>
<dt><code>list_formats</code></p>
<dd> List available formats (supported pixel formats, codecs, and frame sizes) and exit. </p>
<p> Available values are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>all</code></p>
<dd> Show all available (compressed and non-compressed) formats.</p>
<dt><code>raw</code></p>
<dd> Show only raw video (non-compressed) formats.</p>
<dt><code>compressed</code></p>
<dd> Show only compressed formats.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>list_standards</code></p>
<dd> List supported standards and exit. </p>
<p> Available values are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>all</code></p>
<dd> Show all supported standards.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>timestamps, ts</code></p>
<dd> Set type of timestamps for grabbed frames. </p>
<p> Available values are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>default</code></p>
<dd> Use timestamps from the kernel.</p>
<dt><code>abs</code></p>
<dd> Use absolute timestamps (wall clock).</p>
<dt><code>mono2abs</code></p>
<dd> Force conversion from monotonic to absolute timestamps.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Default value is <tt>&quot;default&quot;</tt>.</dl>
<dt><code>use_libv4l2</code></p>
<dd> Use libv4l2 (v4l-utils) conversion functions. Default is 0.</dl>
<h3>vfwcap</h3>
<p> VfW (Video for Windows) capture input device. </p>
<p> The filename passed as input is the capture driver number, ranging from 0 to 9. You may use &#8220;list&#8221; as filename to print a list of drivers. Any other filename will be interpreted as device number 0. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>video_size</code></p>
<dd> Set the video frame size.</p>
<dt><code>framerate</code></p>
<dd> Set the grabbing frame rate. Default value is <tt>&quot;ntsc&quot;</tt>, corresponding to a frame rate of <tt>&quot;30000/1001&quot;</tt>.</dl>
<h3>x11grab</h3>
<p> X11 video input device. </p>
<p> To enable this input device during configuration you need libxcb installed on your system. It will be automatically detected during configuration. </p>
<p> This device allows one to capture a region of an X11 display. </p>
<p> The filename passed as input has the syntax: </p>
<pre><code>
[&lt;hostname&gt;] : &lt;display_number&gt;.&lt;screen_number&gt;[+&lt;x_offset&gt;, &lt;y_offset&gt;]
</code></pre>
<p> <i>hostname</i>:<i>display_number</i>.<i>screen_number</i> specifies the X11 display name of the screen to grab from. <i>hostname</i> can be omitted, and defaults to &#8220;localhost&#8221;. The environment variable <font SIZE="-1"><code>DISPLAY</code></font> contains the default display name. </p>
<p> <i>x_offset</i> and <i>y_offset</i> specify the offsets of the grabbed area with respect to the top-left border of the X11 screen. They default to 0. </p>
<p> Check the X11 documentation (e.g. <code>man X</code>) for more detailed information. </p>
<p> Use the <code>xdpyinfo</code> program for getting basic information about the properties of your X11 display (e.g. grep for &#8220;name&#8221; or &#8220;dimensions&#8221;). </p>
<p> For example to grab from <i>:0.0</i> using <code>ffmpeg</code>: </p>
<pre>
        ffmpeg -f x11grab -framerate 25 -video_size cif -i :0.0 out.mpg
</pre>
<p> Grab at position <tt>&quot;10,20&quot;</tt>: </p>
<pre>
        ffmpeg -f x11grab -framerate 25 -video_size cif -i :0.0+10,20 out.mpg
</pre>
<p> <i>Options</i></p>
<dl>
<dt><code>select_region</code></p>
<dd> Specify whether to select the grabbing area graphically using the pointer. A value of <tt>1</tt> prompts the user to select the grabbing area graphically by clicking and dragging. A single click with no dragging will select the whole screen. A region with zero width or height will also select the whole screen. This option overwrites the <i>video_size</i>, <i>grab_x</i>, and <i>grab_y</i> options. Default value is <tt>0</tt>.</p>
<dt><code>draw_mouse</code></p>
<dd> Specify whether to draw the mouse pointer. A value of <tt>0</tt> specifies not to draw the pointer. Default value is <tt>1</tt>.</p>
<dt><code>follow_mouse</code></p>
<dd> Make the grabbed area follow the mouse. The argument can be <tt>&quot;centered&quot;</tt> or a number of pixels <i></i><font SIZE="-1"><i>PIXELS</i></font><i></i>. </p>
<p> When it is specified with &#8220;centered&#8221;, the grabbing region follows the mouse pointer and keeps the pointer at the center of region; otherwise, the region follows only when the mouse pointer reaches within <i></i><font SIZE="-1"><i>PIXELS</i></font><i></i> (greater than zero) to the edge of region. </p>
<p> For example: </p>
<pre>
        ffmpeg -f x11grab -follow_mouse centered -framerate 25 -video_size cif -i :0.0 out.mpg
</pre>
<p> To follow only when the mouse pointer reaches within 100 pixels to edge: </p>
<pre>
        ffmpeg -f x11grab -follow_mouse 100 -framerate 25 -video_size cif -i :0.0 out.mpg
</pre>
<dt><code>framerate</code></p>
<dd> Set the grabbing frame rate. Default value is <tt>&quot;ntsc&quot;</tt>, corresponding to a frame rate of <tt>&quot;30000/1001&quot;</tt>.</p>
<dt><code>show_region</code></p>
<dd> Show grabbed region on screen. </p>
<p> If <i>show_region</i> is specified with <tt>1</tt>, then the grabbing region will be indicated on screen. With this option, it is easy to know what is being grabbed if only a portion of the screen is grabbed.</p>
<dt><code>region_border</code></p>
<dd> Set the region border thickness if <code>-show_region 1</code> is used. Range is 1 to 128 and default is 3 (XCB-based x11grab only). </p>
<p> For example: </p>
<pre>
        ffmpeg -f x11grab -show_region 1 -framerate 25 -video_size cif -i :0.0+10,20 out.mpg
</pre>
<p> With <i>follow_mouse</i>: </p>
<pre>
        ffmpeg -f x11grab -follow_mouse centered -show_region 1 -framerate 25 -video_size cif -i :0.0 out.mpg
</pre>
<dt><code>window_id</code></p>
<dd> Grab this window, instead of the whole screen. Default value is 0, which maps to the whole screen (root window). </p>
<p> The id of a window can be found using the <code>xwininfo</code> program, possibly with options -tree and -root. </p>
<p> If the window is later enlarged, the new area is not recorded. Video ends when the window is closed, unmapped (i.e., iconified) or shrunk beyond the video size (which defaults to the initial window size). </p>
<p> This option disables options <code>follow_mouse</code> and <code>select_region</code>.</p>
<dt><code>video_size</code></p>
<dd> Set the video frame size. Default is the full desktop or window.</p>
<dt><code>grab_x</code></p>
<dd>
<dt><code>grab_y</code></p>
<dd> Set the grabbing region coordinates. They are expressed as offset from the top left corner of the X11 window and correspond to the <i>x_offset</i> and <i>y_offset</i> parameters in the device name. The default value for both options is 0.</dl>
<h2>OUTPUT DEVICES</h2>
<p> Output devices are configured elements in FFmpeg that can write multimedia data to an output device attached to your system. </p>
<p> When you configure your FFmpeg build, all the supported output devices are enabled by default. You can list all available ones using the configure option &#8220;&#8211;list-outdevs&#8221;. </p>
<p> You can disable all the output devices using the configure option &#8220;&#8211;disable-outdevs&#8221;, and selectively enable an output device using the option &quot;&#8211;enable-outdev=<i></i><font SIZE="-1"><i>OUTDEV</i></font><i></i>&#8220;, or you can disable a particular input device using the option &#8221;&#8211;disable-outdev=<i></i><font SIZE="-1"><i>OUTDEV</i></font><i></i>&quot;. </p>
<p> The option &#8220;-devices&#8221; of the ff* tools will display the list of enabled output devices. </p>
<p> A description of the currently available output devices follows.</p>
<h3>alsa</h3>
<p> <font SIZE="-1">ALSA</font> (Advanced Linux Sound Architecture) output device. </p>
<p> <i>Examples</i></p>
<dl>
<dt>&bull;</p>
<dd> Play a file on default <font SIZE="-1">ALSA</font> device: </p>
<pre>
        ffmpeg -i INPUT -f alsa default
</pre>
<dt>&bull;</p>
<dd> Play a file on soundcard 1, audio device 7: </p>
<pre>
        ffmpeg -i INPUT -f alsa hw:1,7
</pre>
</dl>
<h3>AudioToolbox</h3>
<p> AudioToolbox output device. </p>
<p> Allows native output to CoreAudio devices on <font SIZE="-1">OSX.</font> </p>
<p> The output filename can be empty (or <tt>&quot;-&quot;</tt>) to refer to the default system output device or a number that refers to the device index as shown using: <tt>&quot;-list_devices true&quot;</tt>. </p>
<p> Alternatively, the audio input device can be chosen by index using the </p>
<pre>
    B&lt;-audio_device_index E&lt;lt&gt;INDEXE&lt;gt&gt;&gt;
</pre>
<p> , overriding any device name or index given in the input filename. </p>
<p> All available devices can be enumerated by using <code>-list_devices true</code>, listing all device names, UIDs and corresponding indices. </p>
<p> <i>Options</i> </p>
<p> AudioToolbox supports the following options:</p>
<dl>
<dt><code>-audio_device_index &lt;</code><font SIZE="-1"><code>INDEX</code></font><code>&gt;</code></p>
<dd> Specify the audio device by its index. Overrides anything given in the output filename.</dl>
<p> <i>Examples</i></p>
<dl>
<dt>&bull;</p>
<dd> Print the list of supported devices and output a sine wave to the default device: </p>
<pre>
        $ ffmpeg -f lavfi -i sine=r=44100 -f audiotoolbox -list_devices true -
</pre>
<dt>&bull;</p>
<dd> Output a sine wave to the device with the index 2, overriding any output filename: </p>
<pre>
        $ ffmpeg -f lavfi -i sine=r=44100 -f audiotoolbox -audio_device_index 2 -
</pre>
</dl>
<h3>caca</h3>
<p> <font SIZE="-1">CACA</font> output device. </p>
<p> This output device allows one to show a video stream in <font SIZE="-1">CACA</font> window. Only one <font SIZE="-1">CACA</font> window is allowed per application, so you can have only one instance of this output device in an application. </p>
<p> To enable this output device you need to configure FFmpeg with <tt>&quot;--enable-libcaca&quot;</tt>. libcaca is a graphics library that outputs text instead of pixels. </p>
<p> For more information about libcaca, check: &lt;<code><a rel="nofollow" href="http://caca.zoy.org/wiki/libcaca">http://caca.zoy.org/wiki/libcaca</a></code>&gt; </p>
<p> <i>Options</i></p>
<dl>
<dt><code>window_title</code></p>
<dd> Set the <font SIZE="-1">CACA</font> window title, if not specified default to the filename specified for the output device.</p>
<dt><code>window_size</code></p>
<dd> Set the <font SIZE="-1">CACA</font> window size, can be a string of the form <i>width</i>x<i>height</i> or a video size abbreviation. If not specified it defaults to the size of the input video.</p>
<dt><code>driver</code></p>
<dd> Set display driver.</p>
<dt><code>algorithm</code></p>
<dd> Set dithering algorithm. Dithering is necessary because the picture being rendered has usually far more colours than the available palette. The accepted values are listed with <tt>&quot;-list_dither algorithms&quot;</tt>.</p>
<dt><code>antialias</code></p>
<dd> Set antialias method. Antialiasing smoothens the rendered image and avoids the commonly seen staircase effect. The accepted values are listed with <tt>&quot;-list_dither antialiases&quot;</tt>.</p>
<dt><code>charset</code></p>
<dd> Set which characters are going to be used when rendering text. The accepted values are listed with <tt>&quot;-list_dither charsets&quot;</tt>.</p>
<dt><code>color</code></p>
<dd> Set color to be used when rendering text. The accepted values are listed with <tt>&quot;-list_dither colors&quot;</tt>.</p>
<dt><code>list_drivers</code></p>
<dd> If set to <code>true</code>, print a list of available drivers and exit.</p>
<dt><code>list_dither</code></p>
<dd> List available dither options related to the argument. The argument must be one of <tt>&quot;algorithms&quot;</tt>, <tt>&quot;antialiases&quot;</tt>, <tt>&quot;charsets&quot;</tt>, <tt>&quot;colors&quot;</tt>.</dl>
<p> <i>Examples</i></p>
<dl>
<dt>&bull;</p>
<dd> The following command shows the <code>ffmpeg</code> output is an <font SIZE="-1">CACA</font> window, forcing its size to 80&#215;25: </p>
<pre>
        ffmpeg -i INPUT -c:v rawvideo -pix_fmt rgb24 -window_size 80x25 -f caca -
</pre>
<dt>&bull;</p>
<dd> Show the list of available drivers and exit: </p>
<pre>
        ffmpeg -i INPUT -pix_fmt rgb24 -f caca -list_drivers true -
</pre>
<dt>&bull;</p>
<dd> Show the list of available dither colors and exit: </p>
<pre>
        ffmpeg -i INPUT -pix_fmt rgb24 -f caca -list_dither colors -
</pre>
</dl>
<h3>decklink</h3>
<p> The decklink output device provides playback capabilities for Blackmagic DeckLink devices. </p>
<p> To enable this output device, you need the Blackmagic DeckLink <font SIZE="-1">SDK</font> and you need to configure with the appropriate <tt>&quot;--extra-cflags&quot;</tt> and <tt>&quot;--extra-ldflags&quot;</tt>. On Windows, you need to run the <font SIZE="-1">IDL</font> files through <code>widl</code>. </p>
<p> DeckLink is very picky about the formats it supports. Pixel format is always uyvy422, framerate, field order and video size must be determined for your device with <code>-list_formats 1</code>. Audio sample rate is always 48 kHz. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>list_devices</code></p>
<dd> If set to <code>true</code>, print a list of devices and exit. Defaults to <code>false</code>. This option is deprecated, please use the <tt>&quot;-sinks&quot;</tt> option of ffmpeg to list the available output devices.</p>
<dt><code>list_formats</code></p>
<dd> If set to <code>true</code>, print a list of supported formats and exit. Defaults to <code>false</code>.</p>
<dt><code>preroll</code></p>
<dd> Amount of time to preroll video in seconds. Defaults to <code>0.5</code>.</p>
<dt><code>duplex_mode</code></p>
<dd> Sets the decklink device duplex mode. Must be <code>unset</code>, <code>half</code> or <code>full</code>. Defaults to <code>unset</code>.</p>
<dt><code>timing_offset</code></p>
<dd> Sets the genlock timing pixel offset on the used output. Defaults to <code>unset</code>.</dl>
<p> <i>Examples</i></p>
<dl>
<dt>&bull;</p>
<dd> List output devices: </p>
<pre>
        ffmpeg -sinks decklink
</pre>
<dt>&bull;</p>
<dd> List supported formats: </p>
<pre>
        ffmpeg -i test.avi -f decklink -list_formats 1 'DeckLink Mini Monitor'
</pre>
<dt>&bull;</p>
<dd> Play video clip: </p>
<pre>
        ffmpeg -i test.avi -f decklink -pix_fmt uyvy422 'DeckLink Mini Monitor'
</pre>
<dt>&bull;</p>
<dd> Play video clip with non-standard framerate or video size: </p>
<pre>
        ffmpeg -i test.avi -f decklink -pix_fmt uyvy422 -s 720x486 -r 24000/1001 'DeckLink Mini Monitor'
</pre>
</dl>
<h3>fbdev</h3>
<p> Linux framebuffer output device. </p>
<p> The Linux framebuffer is a graphic hardware-independent abstraction layer to show graphics on a computer monitor, typically on the console. It is accessed through a file device node, usually <i>/dev/fb0</i>. </p>
<p> For more detailed information read the file <i>Documentation/fb/framebuffer.txt</i> included in the Linux source tree. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>xoffset</code></p>
<dd>
<dt><code>yoffset</code></p>
<dd> Set x/y coordinate of top left corner. Default is 0.</dl>
<p> <i>Examples</i> </p>
<p> Play a file on framebuffer device <i>/dev/fb0</i>. Required pixel format depends on current framebuffer settings. </p>
<pre>
        ffmpeg -re -i INPUT -c:v rawvideo -pix_fmt bgra -f fbdev /dev/fb0
</pre>
<p> See also &lt;<code><a rel="nofollow" href="http://linux-fbdev.sourceforge.net/">http://linux-fbdev.sourceforge.net/</a></code>&gt;, and <code><a href="/docs/linux/man/1-fbset/">fbset</a></code>(1).</p>
<h3>opengl</h3>
<p> OpenGL output device. </p>
<p> To enable this output device you need to configure FFmpeg with <tt>&quot;--enable-opengl&quot;</tt>. </p>
<p> This output device allows one to render to OpenGL context. Context may be provided by application or default <font SIZE="-1">SDL</font> window is created. </p>
<p> When device renders to external context, application must implement handlers for following messages: <tt>&quot;AV_DEV_TO_APP_CREATE_WINDOW_BUFFER&quot;</tt> &#8211; create OpenGL context on current thread. <tt>&quot;AV_DEV_TO_APP_PREPARE_WINDOW_BUFFER&quot;</tt> &#8211; make OpenGL context current. <tt>&quot;AV_DEV_TO_APP_DISPLAY_WINDOW_BUFFER&quot;</tt> &#8211; swap buffers. <tt>&quot;AV_DEV_TO_APP_DESTROY_WINDOW_BUFFER&quot;</tt> &#8211; destroy OpenGL context. Application is also required to inform a device about current resolution by sending <tt>&quot;AV_APP_TO_DEV_WINDOW_SIZE&quot;</tt> message. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>background</code></p>
<dd> Set background color. Black is a default.</p>
<dt><code>no_window</code></p>
<dd> Disables default <font SIZE="-1">SDL</font> window when set to non-zero value. Application must provide OpenGL context and both <tt>&quot;window_size_cb&quot;</tt> and <tt>&quot;window_swap_buffers_cb&quot;</tt> callbacks when set.</p>
<dt><code>window_title</code></p>
<dd> Set the <font SIZE="-1">SDL</font> window title, if not specified default to the filename specified for the output device. Ignored when <code>no_window</code> is set.</p>
<dt><code>window_size</code></p>
<dd> Set preferred window size, can be a string of the form widthxheight or a video size abbreviation. If not specified it defaults to the size of the input video, downscaled according to the aspect ratio. Mostly usable when <code>no_window</code> is not set.</dl>
<p> <i>Examples</i> </p>
<p> Play a file on <font SIZE="-1">SDL</font> window using OpenGL rendering: </p>
<pre>
        ffmpeg  -i INPUT -f opengl &quot;window title&quot;
</pre>
<h3>oss</h3>
<p> <font SIZE="-1">OSS</font> (Open Sound System) output device.</p>
<h3>pulse</h3>
<p> PulseAudio output device. </p>
<p> To enable this output device you need to configure FFmpeg with <tt>&quot;--enable-libpulse&quot;</tt>. </p>
<p> More information about PulseAudio can be found on &lt;<code><a rel="nofollow" href="http://www.pulseaudio.org">http://www.pulseaudio.org</a></code>&gt; </p>
<p> <i>Options</i></p>
<dl>
<dt><code>server</code></p>
<dd> Connect to a specific PulseAudio server, specified by an <font SIZE="-1">IP</font> address. Default server is used when not provided.</p>
<dt><code>name</code></p>
<dd> Specify the application name PulseAudio will use when showing active clients, by default it is the <tt>&quot;LIBAVFORMAT_IDENT&quot;</tt> string.</p>
<dt><code>stream_name</code></p>
<dd> Specify the stream name PulseAudio will use when showing active streams, by default it is set to the specified output name.</p>
<dt><code>device</code></p>
<dd> Specify the device to use. Default device is used when not provided. List of output devices can be obtained with command <code>pactl list sinks</code>.</p>
<dt><code>buffer_size</code></p>
<dd>
<dt><code>buffer_duration</code></p>
<dd> Control the size and duration of the PulseAudio buffer. A small buffer gives more control, but requires more frequent updates. </p>
<p> <code>buffer_size</code> specifies size in bytes while <code>buffer_duration</code> specifies duration in milliseconds. </p>
<p> When both options are provided then the highest value is used (duration is recalculated to bytes using stream parameters). If they are set to 0 (which is default), the device will use the default PulseAudio duration value. By default PulseAudio set buffer duration to around 2 seconds.</p>
<dt><code>prebuf</code></p>
<dd> Specify pre-buffering size in bytes. The server does not start with playback before at least <code>prebuf</code> bytes are available in the buffer. By default this option is initialized to the same value as <code>buffer_size</code> or <code>buffer_duration</code> (whichever is bigger).</p>
<dt><code>minreq</code></p>
<dd> Specify minimum request size in bytes. The server does not request less than <code>minreq</code> bytes from the client, instead waits until the buffer is free enough to request more bytes at once. It is recommended to not set this option, which will initialize this to a value that is deemed sensible by the server.</dl>
<p> <i>Examples</i> </p>
<p> Play a file on default device on default server: </p>
<pre>
        ffmpeg  -i INPUT -f pulse &quot;stream name&quot;
</pre>
<h3>sdl</h3>
<p> <font SIZE="-1">SDL</font> (Simple DirectMedia Layer) output device. </p>
<p> &#8220;sdl2&#8221; can be used as alias for &#8220;sdl&#8221;. </p>
<p> This output device allows one to show a video stream in an <font SIZE="-1">SDL</font> window. Only one <font SIZE="-1">SDL</font> window is allowed per application, so you can have only one instance of this output device in an application. </p>
<p> To enable this output device you need libsdl installed on your system when configuring your build. </p>
<p> For more information about <font SIZE="-1">SDL,</font> check: &lt;<code><a rel="nofollow" href="http://www.libsdl.org/">http://www.libsdl.org/</a></code>&gt; </p>
<p> <i>Options</i></p>
<dl>
<dt><code>window_title</code></p>
<dd> Set the <font SIZE="-1">SDL</font> window title, if not specified default to the filename specified for the output device.</p>
<dt><code>icon_title</code></p>
<dd> Set the name of the iconified <font SIZE="-1">SDL</font> window, if not specified it is set to the same value of <i>window_title</i>.</p>
<dt><code>window_size</code></p>
<dd> Set the <font SIZE="-1">SDL</font> window size, can be a string of the form <i>width</i>x<i>height</i> or a video size abbreviation. If not specified it defaults to the size of the input video, downscaled according to the aspect ratio.</p>
<dt><code>window_x</code></p>
<dd>
<dt><code>window_y</code></p>
<dd> Set the position of the window on the screen.</p>
<dt><code>window_fullscreen</code></p>
<dd> Set fullscreen mode when non-zero value is provided. Default value is zero.</p>
<dt><code>window_enable_quit</code></p>
<dd> Enable quit action (using window button or keyboard key) when non-zero value is provided. Default value is 1 (enable quit action)</dl>
<p> <i>Interactive commands</i> </p>
<p> The window created by the device can be controlled through the following interactive commands.</p>
<dl>
<dt><code>q, </code><font SIZE="-1"><code>ESC</code></font></p>
<dd> Quit the device immediately.</dl>
<p> <i>Examples</i> </p>
<p> The following command shows the <code>ffmpeg</code> output is an <font SIZE="-1">SDL</font> window, forcing its size to the qcif format: </p>
<pre>
        ffmpeg -i INPUT -c:v rawvideo -pix_fmt yuv420p -window_size qcif -f sdl &quot;SDL output&quot;
</pre>
<h3>sndio</h3>
<p> sndio audio output device.</p>
<h3>v4l2</h3>
<p> Video4Linux2 output device.</p>
<h3>xv</h3>
<p> <font SIZE="-1">XV</font> (XVideo) output device. </p>
<p> This output device allows one to show a video stream in a X Window System window. </p>
<p> <i>Options</i></p>
<dl>
<dt><code>display_name</code></p>
<dd> Specify the hardware display name, which determines the display and communications domain to be used. </p>
<p> The display name or <font SIZE="-1">DISPLAY</font> environment variable can be a string in the format <i>hostname</i>[:<i>number</i>[.<i>screen_number</i>]]. </p>
<p> <i>hostname</i> specifies the name of the host machine on which the display is physically attached. <i>number</i> specifies the number of the display server on that host machine. <i>screen_number</i> specifies the screen to be used on that server. </p>
<p> If unspecified, it defaults to the value of the <font SIZE="-1">DISPLAY</font> environment variable. </p>
<p> For example, <tt>&quot;dual-headed:0.1&quot;</tt> would specify screen 1 of display 0 on the machine named &#8220;dual-headed&#8221;. </p>
<p> Check the X11 specification for more detailed information about the display name format.</p>
<dt><code>window_id</code></p>
<dd> When set to non-zero value then device doesn&#8217;t create new window, but uses existing one with provided <i>window_id</i>. By default this options is set to zero and device creates its own window.</p>
<dt><code>window_size</code></p>
<dd> Set the created window size, can be a string of the form <i>width</i>x<i>height</i> or a video size abbreviation. If not specified it defaults to the size of the input video. Ignored when <i>window_id</i> is set.</p>
<dt><code>window_x</code></p>
<dd>
<dt><code>window_y</code></p>
<dd> Set the X and Y window offsets for the created window. They are both set to 0 by default. The values may be ignored by the window manager. Ignored when <i>window_id</i> is set.</p>
<dt><code>window_title</code></p>
<dd> Set the window title, if not specified default to the filename specified for the output device. Ignored when <i>window_id</i> is set.</dl>
<p> For more information about XVideo see &lt;<code><a rel="nofollow" href="http://www.x.org/">http://www.x.org/</a></code>&gt;. </p>
<p> <i>Examples</i></p>
<dl>
<dt>&bull;</p>
<dd> Decode, display and encode video input with <code>ffmpeg</code> at the same time: </p>
<pre>
        ffmpeg -i INPUT OUTPUT -f xv display
</pre>
<dt>&bull;</p>
<dd> Decode and display the input video to multiple X11 windows: </p>
<pre>
        ffmpeg -i INPUT -f xv normal -vf negate -f xv negated
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ffmpeg/">ffmpeg</a></code>(1), <code><a href="/docs/linux/man/1-ffplay/">ffplay</a></code>(1), <code><a href="/docs/linux/man/1-ffprobe/">ffprobe</a></code>(1), <code><a href="/docs/linux/man/3-libavdevice/">libavdevice</a></code>(3)</p>
<h2>AUTHORS</h2>
<p> The FFmpeg developers. </p>
<p> For details about the authorship, see the Git history of the project (<a href="git://source.ffmpeg.org/ffmpeg">git://source.ffmpeg.org/ffmpeg</a>), e.g. by typing the command <code>git log</code> in the FFmpeg source directory, or browsing the online repository at &lt;<code><a rel="nofollow" href="http://source.ffmpeg.org">http://source.ffmpeg.org</a></code>&gt;. </p>
<p> Maintainers for the specific components are listed in the file <i></i><font SIZE="-1"><i>MAINTAINERS</i></font><i></i> in the source code tree. </p>
<h2>Index</h2>
