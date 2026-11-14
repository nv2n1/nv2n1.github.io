---
title: "recordmydesktop(1)"
name: "recordmydesktop"
section: "1"
letter: "r"
url: "/docs/linux/man/1-recordmydesktop/"
description: "recordMyDesktop – record desktop sessions to an Ogg-Theora-Vorbis file."
---

<h2 class="name">NAME</h2>
<p> recordMyDesktop &#8211; record desktop sessions to an Ogg-Theora-Vorbis file. </p>
<h2>SYNOPSIS</h2>
<p> <code>recordmydesktop</code> [ <code>Options</code> ]^ <code>filename</code> </p>
<h2>DESCRIPTION</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>recordMyDesktop produces a file(default out.ogv)&nbsp;<wbr>that contains a video and audio recording<br />
 of a linux desktop session. The default behavior of recording is to mark areas that have changed(through libxdamage)<br />
 and update the frame. This behavior can be changed (option <code>&#8211;full-shots</code> ) to produce a more accurate result<br />
 or capture windows that do not generate events on change(windows with accelerated 3d context)<br />
 but this will notably increase the workload.<br />
 recordMyDesktop doesn&#8217;t have a commandline interface.<br />
 After startup, it can be controled only through the following signals: </p>
<p> <code>SIGUSR1</code> causes the program to pause if it&#8217;s currently recording, and vice-versa.<br />
 <code>SIGTERM</code> causes normal termination of the recording.<br />
 <code>SIGINT</code> also causes normal termination.<br />
 <code>SIGABRT</code> terminates the program and removes the specified output file. </p>
<p> This signals can also be delivered on the application, with the use of shortcuts.<br />
 See <code>&#8211;pause-shortcut</code> and <code>&#8211;stop-shortcut</code> , on the <code>Misc.</code> section of <code>Options</code> bellow. </p>
<p>&nbsp;<wbr> </p>
<p>&nbsp;<wbr> </p>
<p>&nbsp;<wbr> A typical scenario of recording can be a command as simple as:<br />
 <code>~$ recordmydesktop</code><br />
 which will produce a fullscreen recording named out.ogv<br />
 while a command like:<br />
 <code>~$ recordmydesktop foo.ogv</code><br />
 will write output to foo.ogv </p>
<p> Since version 0.3, encoding will happen right after the recording finishes.<br />
 While this behavior saves a lot of CPU, you can revert to the old one by entering the &#8211;on-the-fly-encoding switch. </p>
<p> To specify a region for recording you can type this:<br />
 <code>~$ recordmydesktop -x X_pos -y Y_pos &#8211;width WIDTH &#8211;height HEIGHT -o foo.ogv</code><br />
 where X_pos and Y_pos specify the offset in pixels from the upper left<br />
 corner of your screen and WIDTH and HEIGHT the size of the window to be recorded(again in pixels).<br />
 If the area extends beyond your current resolution, you will be notified appropriately and nothing will happen.<br />
 Notice also, that if any option is entered you have to specify the output file with the -o switch.<br />
 If you try to save under a filename that already exists, the name will be post-fixed with a number (incremented if that name exists already) </p>
<p> <code>To normally end a recording you can press ctl-c.</code><br />
 (which will send a <code>SIGINT</code> to the program). </p>
<p> For further manipulation of the end result look at the <code>OPTIONS</code> and <code>NOTES</code> sections. </p>
<h2>EXIT STATUS</h2>
<p> 0 is success<br />
 Non-zero means an error occurred, which is printed in stderr. </p>
<p> The following error codes indicate the nature of the error:<br />
 1 Error while parsing the arguments.<br />
 2 Initializing the encoder failed(either vorbis or theora).<br />
 3 Could not open/configure sound card.<br />
 4 Xdamage extension not present.<br />
 5 Shared memory extension not present.<br />
 6 Xfixes extension not present.<br />
 7 XInitThreads failed.<br />
 8 No $DISPLAY environment variable and none specified as argument.<br />
 9 Cannot connect to Xserver.<br />
 10 Color depth is not 32, 24 or 16bpp.<br />
 11 Improper window specification.<br />
 12 Cannot attach shared memory to proccess.<br />
 13 Cannot open file for writting.<br />
 14 Cannot load the Jack library ( <code>UNUSED SINCE 0.3.8</code> ).<br />
 15 Cannot create new client.<br />
 16 Cannot activate client.<br />
 17 Port registration/connection failure. </p>
<h2>OPTIONS</h2>
<p> <code>Generic Options:</code> </p>
<dl>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-h or &#8211;help</code></p>
<dd>
&nbsp;<wbr>Print help summary and exit. </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;version</code></p>
<dd>
&nbsp;<wbr>Print program version and exit. </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;print-config</code></p>
<dd>
&nbsp;<wbr>Print info about options selected during compilation and exit.
</dl>
<p> <code>Image Options:</code> </p>
<dl>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;windowid id_of_window</code></p>
<dd>
&nbsp;<wbr>id of window to be recorded. </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;display DISPLAY</code></p>
<dd>
&nbsp;<wbr>Display to connect to. </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-x X</code></p>
<dd>
&nbsp;<wbr>Offset in x direction. </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-y Y</code></p>
<dd>
&nbsp;<wbr>Offset in y direction. </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;width N</code></p>
<dd>
&nbsp;<wbr>Width of recorded window. </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;height N</code></p>
<dd>
&nbsp;<wbr>Height of recorded window. </p>
<dt><code><br />
 </code></p>
<dd>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;dummy-cursor color</code></p>
<dd>
&nbsp;<wbr>Draw a dummy cursor, instead of the normal one.Value of color can be&nbsp;<wbr>&quot;black&quot;&nbsp;<wbr>or&nbsp;<wbr>&quot;white&quot;. </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;no-cursor</code></p>
<dd>
&nbsp;<wbr>Disable drawing of the cursor. </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;no-shared</code></p>
<dd>
&nbsp;<wbr>Disable usage of MIT-shared memory extension <code>(Not Recommended).</code> </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;full-shots</code></p>
<dd>
&nbsp;<wbr>Take full screenshot at every frame(Not recomended!). </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;follow-mouse</code></p>
<dd>
&nbsp;<wbr>When this option is enabled, the capture area follows the mouse cursor. This<br />
&nbsp;<wbr>is meaningfull only when the selected area is a subset of the full screen.<br />
&nbsp;<wbr>This option auto-enables &#8211;full-shots. </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;quick-subsampling</code></p>
<dd>
&nbsp;<wbr>Do subsampling of the chroma planes by discarding extra pixels. </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;fps N(number&gt;0.0)</code></p>
<dd>
&nbsp;<wbr>A positive number denoting desired framerate. </p>
</dl>
<p> <code>Sound Options:</code> </p>
<dl>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;channels N(number&gt;0)</code></p>
<dd>
&nbsp;<wbr>A positive number denoting desired sound channels in recording. </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;freq N(number&gt;0)</code></p>
<dd>
&nbsp;<wbr>A positive number denoting desired sound frequency. </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;buffer-size N(number&gt;0)</code></p>
<dd>
&nbsp;<wbr>A positive number denoting the desired sound buffer size(in frames, when using ALSA or OSS). </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;ring-buffer-size N(float number&gt;0)</code></p>
<dd>
&nbsp;<wbr>A float number denoting the desired ring buffer size&nbsp;<wbr>(in seconds,when using JACK only).<br />
&nbsp;<wbr>The overall size of the buffer in bytes will be:<br />
&nbsp;<wbr>ring_buffer_size&nbsp;<wbr>*&nbsp;<wbr>samplerate&nbsp;<wbr>*&nbsp;<wbr>number_of_ports&nbsp;<wbr>*&nbsp;<wbr>sizeof(jack_default_audio_sample_t),<br />
&nbsp;<wbr>where sizeof(jack_default_audio_sample_t)&nbsp;<wbr>is normally 4. </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;device SOUND_DEVICE</code></p>
<dd>
&nbsp;<wbr>Sound device(default hw:0,0 or&nbsp;<wbr>/dev/dsp, depending on whether ALSA or OSS is used). </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;use-jack port1 port2&#8230; portn</code></p>
<dd>
&nbsp;<wbr>Record audio from the specified list of <code>space-separated</code> jack ports.<br />
&nbsp;<wbr>When using this option, all the rest audio related ones(except &#8211;no-sound)&nbsp;<wbr>are not taken into account. </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;no-sound</code></p>
<dd>
&nbsp;<wbr>Do not record sound.
</dl>
<p> <code>Encoding Options:</code> </p>
<dl>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;on-the-fly-encoding</code></p>
<dd>
&nbsp;<wbr>Encode the audio-video data, while recording. </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;v_quality n</code></p>
<dd>
&nbsp;<wbr>A number from 0 to 63 for desired encoded video quality(default 63). </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;v_bitrate n</code></p>
<dd>
&nbsp;<wbr>A number from 45000 to 2000000 for desired encoded video bitrate(default 45000). </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;s_quality n</code></p>
<dd>
&nbsp;<wbr>Desired audio quality(-1 to 10).
</dl>
<p> <code>Misc Options:</code> </p>
<dl>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;rescue path_to_data&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code></p>
<dd>
&nbsp;<wbr>Encode cache data from a previous session, into an Ogg/Theora+Vorbis<br />
&nbsp;<wbr>file. The filename will be the one that was chosen initially.<br />
&nbsp;<wbr>Any other option specified with this one will be implicitly ignored<br />
&nbsp;<wbr>and recordMyDesktop will exit after the end of the encoding.<br />
&nbsp;<wbr>This option was added in recordMyDesktop 0.3.7 and it will not<br />
&nbsp;<wbr>work with cache files produced from earlier versions.<br />
&nbsp;<wbr>When using this option, remember that recordMyDesktop&#8217;s cache is&nbsp;<wbr><br />
&nbsp;<wbr>not safe, in respect to type-sizes and endianness. </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;print-config</code></p>
<dd>
&nbsp;<wbr>Print compilation time options. Currently prints whether Jack capture is<br />
&nbsp;<wbr>enabled and if ALSA or OSS is used&nbsp;<wbr>(may contain more information<br />
&nbsp;<wbr>in the future). </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;no-wm-check</code></p>
<dd>
&nbsp;<wbr>When a 3d compositing window manager is detected the program will function as if the<br />
&nbsp;<wbr>&#8211;full-shots option has been specified. This option disables that<br />
&nbsp;<wbr>behavior alltogether. </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;no-frame</code></p>
<dd>
&nbsp;<wbr>Normally, around the recording area, there is drawn a frame to assist<br />
&nbsp;<wbr>the user in identifying what does and what doesn&#8217;t get captured.<br />
&nbsp;<wbr>This frame will also follow around the mouse, when &#8211;follow-mouse<br />
&nbsp;<wbr>is used. The frame might cause problems for drag and drop. If you do<br />
&nbsp;<wbr>not wish this frame to appear, use this option. </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;pause-shortcut MOD+KEY</code></p>
<dd>
&nbsp;<wbr>Shortcut that will be used for pausing or unpausing the recording.<br />
&nbsp;<wbr>MOD can be any combination of the following modifier keys:<br />
&nbsp;<wbr>Control, Shift and Mod1 to Mod5. The modifiers can be separated&nbsp;<wbr><br />
&nbsp;<wbr>with any character( <code>except SPACE</code> ) or none at all. KEY can be any key defined in<br />
&nbsp;<wbr>/usr/include/X11/keysymdef.h without the XK_&nbsp;<wbr>prefix.<br />
&nbsp;<wbr>The list of modifiers must be separated from the key with a plus(&#8216;+&#8217;)<br />
&nbsp;<wbr>sign.<br />
&nbsp;<wbr>Default is Control+Mod1+p&nbsp;<wbr>(Mod1 usually corresponds to left Alt).<br />
&nbsp;<wbr> </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;stop-shortcut MOD+KEY</code></p>
<dd>
&nbsp;<wbr>Shortcut that will be used to stop the recording.<br />
&nbsp;<wbr>For more, see -pause-shortcut above.<br />
&nbsp;<wbr>Default is Control+Mod1+s.&nbsp;<wbr> </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;compress-cache</code></p>
<dd>
&nbsp;<wbr>Image data are cached with a light compression. </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;workdir DIR</code></p>
<dd>
&nbsp;<wbr>Location where a temporary directory will be created to hold project files(default&nbsp;<wbr>/var/tmp). </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;delay n[H|h|M|m]</code></p>
<dd>
&nbsp;<wbr>Number of secs(default),minutes or hours before capture starts(number can be float). </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;overwrite</code></p>
<dd>
&nbsp;<wbr>If there is already a file with the same name, delete it.<br />
&nbsp;<wbr>Default action is to add a number postfix to the new file.<br />
&nbsp;<wbr>For example when not specifying a name, if out.ogv exists,<br />
&nbsp;<wbr>the new file will be out-1.ogv and if that exists too, out-2.ogv<br />
&nbsp;<wbr>and so on&nbsp;<wbr>(no ad-infinitum though, more like ad-short-integer&#8230;) </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-o filename</code></p>
<dd>
&nbsp;<wbr>Name of recorded video(default out.ogv). </p>
</dl>
<p> If no other option is specified, filename can be given without the -o switch. </p>
<h2>USAGE</h2>
<dl>
<dt><code>recordmydesktop [OPTIONS]^filename</code></p>
<dd>
</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DISPLAY</code></p>
<dd>
 Display environment variable, specifying X server to connect to.
</dl>
<h2>NOTES</h2>
<p>&nbsp;<wbr>Recording a window using the &#8211;windowid option, doesn&#8217;t track the window itself, but the region that it covers.<br />
 Also when using that option the -x,-y,&#8211;width and &#8211;height options are relative to the specified window area.<br />
 An easy way to find out the id of a window, is by using the <code>xwininfo</code> program.<br />
 Running a command like :<br />
 <code>xwininfo | awk &#8216;/Window id:/ {print $4}&#8217;</code><br />
 will give you only the id of the window(which should look like this: 0x4800005)<br />
 More conviniently you can put all that in the command that launches recordMyDesktop like this:<br />
 <code>~$recordmydesktop &#8211;windowid $(xwininfo | awk &#8216;/Window id:/ {print $4}&#8217;)</code> </p>
<p>&nbsp;<wbr>Also, the lower quality you select on a video recording&nbsp;<wbr>( <code>-v_quality</code> option), the highest CPU-power that you will need.<br />
 So <code>if you are doing the encoding on the fly</code> ,it&#8217;s better to start with default values and manipulate the end-result with another program. </p>
<p> An excellent converter is the <code>vlc</code> media player, which can perform a variety of transcoding<br />
 operations, either using the graphical interface, or the commandline for more flexibility.<br />
 vlc is a complex piece of software, so you should consult it&#8217;s documentation, before<br />
 using it. </p>
<p> An example follows, which will resize a recording named out.ogv to 512&#215;384:<br />
 <code>vlc -I dummy out.ogv vlc:quit &#8211;sout &quot;#transcode{ vcodec = theo, width = 512, height = 384 }:duplicate{ dst = std{ access = file, mux=ogg, dst = \&quot;out_512x384.ogv\&quot; }}&quot;</code> </p>
<p> If you wish to change the video quality you can append the <code>&#8211;sout-theora-quality=n,</code> with <code>n</code> in the range <code>[1,10]</code> e.g:<br />
 <code>vlc -I dummy out.ogv vlc:quit &#8211;sout &quot;#transcode{ vcodec = theo, width = 512, height = 384 }:duplicate{ dst = std{ access = file, mux=ogg, dst = \&quot;out_512x384.ogv\&quot; }}&quot; &#8211;sout-theora-quality=3</code><br />
 which will give a file of a video quality 18 (in a range of 0-63), thus appropriate for web-publishing. </p>
<p> Another option is <code>ffmpeg2theora</code> , which despite its name is also a theora to theora converter.<br />
 Changing the quality of a recordng with it, can be as simple as :<br />
 <code>ffmpeg2theora infile.ogv -v 3 -a 4 -o outfile.ogv</code><br />
 It can even perform resizing on the size of the recording, or change the overall duration. </p>
<h2>BUGS</h2>
<p> Does not record 3d windows, if &#8211;full-shots isn&#8217;t specified.<br />
 Saving 65536 files with the same name, will result in upredictable behavior,<br />
 which might manifest as an endless loop, or a segmentation fault. </p>
<h2>AUTHORS</h2>
<p> John Varouhakis(johnvarouhakis [at] gmail.com) </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-xwininfo/">xwininfo</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-vlc/">vlc</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-ffmpeg2theora/">ffmpeg2theora</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-jack_lsp/">jack_lsp</a>(1)</code> </p>
<h2>Index</h2>
