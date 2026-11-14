---
title: "lavplay(1)"
name: "lavplay"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lavplay/"
description: "lavplay – Playback and edit MJPEG video"
---

<h2 class="name">NAME</h2>
<p> lavplay &#8211; Playback and edit MJPEG video</p>
<h2>SYNOPSIS</h2>
<p> <code>lavplay</code> [<i>options</i>] <i>lavfile1 [lavfile2 &#8230; lavfileN]</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>lavplay</code> can be used to playback video in MJPEG format (either quicktime or AVI) on a zoran video-capture device, such as the Miro/Pinnacle DC10(+), the Iomega Buz or Linux Media Labs&#8217; LML33, or in software mode (using SDL). </p>
<p> It also provides mechanisms for non-destructive editting video using an interactive front-end such as <code><a href="/docs/linux/man/1-glav/">glav</a></code>(1). See <code>SEARCHING AND EDITING</code> below for details. </p>
<h2>OPTIONS</h2>
<p> <code>lavplay</code> accepts the following options:</p>
<dl>
<dt><code>-p/&#8211;playback</code> [<code>S</code>|<code>C</code>|<code>H</code>]</p>
<dd> The playback mode to be used. &#8216;S&#8217; means software-playback using SDL.<br />
&nbsp;<wbr>&#8216;H&#8217;&nbsp;<wbr>means hardware-playback on the monitor&nbsp;<wbr>(on-screen).&nbsp;<wbr>&#8216;C&#8217;&nbsp;<wbr>means hardware-playback to the video-out of the zoran video-capture device. Obviously, &#8216;C&#8217; and &#8216;H&#8217; only work on computers with zoran video-capture devices.</p>
<dt><code>-Z/&#8211;full-screen</code></p>
<dd> Full-screen playback. This works if SDL- or onscreen-playback is chosen.</p>
<dt><code>&#8211;size</code><i> NxN</i></p>
<dd> Size of the video window (default: size of the input video) when using software (SDL) or hardware onscreen playback</p>
<dt><code>-a/&#8211;audio</code><i> num</i></p>
<dd> When play audio, 0 means never, or sum of<br />
&nbsp;<wbr>&nbsp;<wbr>1: while playing forward,<br />
&nbsp;<wbr>&nbsp;<wbr>2: while playing reverse,<br />
&nbsp;<wbr>&nbsp;<wbr>4: even fast playing,<br />
&nbsp;<wbr>&nbsp;<wbr>8: while pausing<br />
 (default: 7: forward/reverse/fast). If 8(pausing) was contained, lavplay will be very noisy, but useful when you want to edit by sound.</p>
<dt><code>-z/&#8211;zoom</code></p>
<dd> Zooms the video to fit the screen as good as possible.</p>
<dt><code>-x</code></p>
<dd> Exchange fields of an interlaced video. Try this if the video looks weird. It shouldn&#8217;t be necessary with stuff captured using <a href="/docs/linux/man/1-lavrec/">lavrec</a>(1) but could be needed for other sources.</p>
<dt><code>-s/&#8211;skip</code><i> num</i></p>
<dd> Skip &lt;num&gt; seconds of video at the beginning.</p>
<dt><code>-x/&#8211;exchange-fields</code></p>
<dd> Invert field order (for videos which are recorded with wrong field order interlacing settings)</p>
<dt><code>-F/&#8211;flicker</code></p>
<dd> Disable stills flicker reduction. This is useful if you want to see stills exactly as they were recorded rather than flicker-free!</p>
<dt><code>-c/&#8211;synchronization</code> [<code>0</code>|<code>1</code>]</p>
<dd> Enables (1) or disables (0) the use of sync corrections. Basically, you almost certainly want this. Disabling is really there for diagnostic purposes and not much else.</p>
<dt><code>-H/&#8211;H-offset</code><i> num, </i><code>-V/&#8211;V-offset</code><i> num</i></p>
<dd> Horizontal (-H) and vertical (-V) offset when using hardware-playback. Offset plus width or height should be smaller than or equal to the playback device&#8217;s maximum allowed size (DC10+: 640&#215;480 or 768&#215;576, LML33/Marvel/Buz: 720&#215;480/576).</p>
<dt><code>&#8211;s-x-offset</code><i> num, </i><code>&#8211;s-y-offset</code><i> num</i></p>
<dd> Offset for the video window (from top left screen corner) when using hardware onscreen playback in non-fullscreen mode.</p>
<dt><code>&#8211;display</code><i> :x.x</i></p>
<dd> When using hardware fullsreen video playback (-pH), this setting can be used to specify the video display (default: :0.0) to use for video display.</p>
<dt><code>-q/&#8211;no-quit</code></p>
<dd> Makes lavplay stay alive at the end of the video (lavplay won&#8217;t quit). Use &#8216;q&lt;enter&gt;&#8217; on the command line to quit (see below, <code>SEARCHING AND EDITING</code>).</p>
<dt><code>-g/&#8211;gui-mode</code></p>
<dd> Enables GUI-mode. This is used by glav and Linux Video Studio. It will output the current position in the video each frame, so that the glav or LVS can keep track of where we are in the video which is being played back.</p>
<dt><code>-P/&#8211;preserve-pathnames</code></p>
<dd> This is used by glav and Linux Video Studio. When editlists are created the original pathnames for files are used and not the canonicalised pathnames from the root directory. Useful if you&#8217;ve got things like automounters active that make directories with the same non-canonical name have different canonical names on different machines.</p>
<dt><code>-U/&#8211;use-write</code></p>
<dd> Use the write() system call rather than the mmap() system call for audio writing to the sound device. This may fix some audio playback problems.</p>
<dt><code>-n/&#8211;mjpeg-buffers</code><i> num</i></p>
<dd> Number of MJPEG-buffers. Default is 32. Try changing this number if you have many lost frames.</p>
<dt><code>-v/&#8211;verbose</code><i> num</i></p>
<dd> Verbosity level (0, 1 or 2) </p>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> The following environment variables can be recognized by lavrec:</p>
<dl>
<dt><code>LAV_VIDEO_DEV</code></p>
<dd> The video device. Default is /dev/video</p>
<dt><code>LAV_AUDIO_DEV</code></p>
<dd> The audio device. Default is /dev/dsp</dl>
<h2>SEARCHING AND EDITING</h2>
<p> <code>lavplay</code> can do more than simple plain playback. It is also intended to be controlled using commands sent via stdin from a front-end like <code><a href="/docs/linux/man/1-glav/">glav</a>(1)</code> or similar, more sophisticated tools. The most significant aspect of this functionality is the ability to create <i>edit list</i> files giving the playback sequence of an editted version of the input video. The edit list file can be read by any of the <a href="/docs/linux/man/1-mjpegtools/">mjpegtools</a>(1) (including lavplay!) wherever an actual video file would be acceptable. Such edit lists record only the original source file and start and stop frames of the components of the editted video editting rather than the video itself. As such editting leaves the original files unchanged and requires only tiny amounts of data-movement. The drawback is that for the edit list to work the original files must remain unchanged, and that interactive play may be jumpy due to the playback sequence &quot;skipping about&quot; between different parts of the original video sequence. </p>
<p> If a stand-alone consolidated versions of editted video is required it can be produced by running the <a href="/docs/linux/man/1-lavtrans/">lavtrans</a>(1) utility on the edit list. </p>
<p> Edit list files are plain text with a very simple syntax to allow easy manual editting using a text-editor or writing of scripted editting tools. </p>
<h2>STDIN COMMANDS</h2>
<p> The commands accepted on standard input sre as follows (and can of course be entered directly by command-line junkies): </p>
<dl>
<dt><code>+, &#8211;</code></p>
<dd> Goes to next/previous frame. Only makes sense when the video is paused.</p>
<dt><code>pN</code></p>
<dd> Sets playback speed to N (N=&#8230;, -1, 0, 1, &#8230;)</p>
<dt><code>a[01]</code></p>
<dd> Enables/disables audio playback</p>
<dt><code>sN</code></p>
<dd> if N is a number, this means to go to frame N. if N is prefixed by a + or -, this means to go N frames back- or forward.</p>
<dt><code>om editlist [N1 N2 [N3 N4]]</code></p>
<dd> Opens a movie or editlist. A second and third argument can specify to only open a specific range of frames from this video (N1=-1 means whole video). N3 and N4 can specify to show only a specific range of frames from the frames which were just opened (useful for trimming).</p>
<dt><code>w[as] file</code></p>
<dd> Save the current editlist (a) or the current selection (s) to a file.</p>
<dt><code>q</code></p>
<dd> Quit lavplay.</p>
<dt><code>e[ou] N1 N2</code></p>
<dd> Cuts (u) or copies (o) frames N1-N2 from the current editlist into an internal selection.</p>
<dt><code>ep</code></p>
<dd> Pastes the contents of the selection into the current position in the editlist.</p>
<dt><code>em N1 N2 N3</code></p>
<dd> Moves frames N1-N2 to position N3 in the video.</p>
<dt><code>ed N1 N2</code></p>
<dd> Deletes frames N1-N2 from the editlist.</p>
<dt><code>ea video N1 N2 N3</code></p>
<dd> Adds frames N1-N2 of the video into position N3 within the editlist. N1=-1 means to add the whole video.</p>
<dt><code>es N1 N2</code></p>
<dd> Sets the current viewable frames within the whole video to N1-N2. This is useful for trimming. </p>
</dl>
<h2>BUGS</h2>
<p> Editlists record absolute pathnames. This more or less forces manual editting of the pathnames in them if it is desired to move editlists and source video files. </p>
<p> lavplay really ought to make a decent job of detecting what playback options are feasible (on-screen hardware, video-out port hardware, software) and set the default playback mode appropriately. Alas, it does not. </p>
<h2>AUTHOR</h2>
<p> This man page was written by Ronald Bultje.<br />
 If you have questions, remarks, problems or you just want to contact the developers, the main mailing list for the MJPEG-tools is: </p>
<p>&nbsp;<wbr><i>mjpeg-users [at] lists.sourceforge.net</i> </p>
<p> For more info, see our website at </p>
<p>&nbsp;<wbr><i><a rel="nofollow" href="http://mjpeg.sourceforge.net/">http://mjpeg.sourceforge.net/</a></i> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mjpegtools/">mjpegtools</a></code>(1), <code><a href="/docs/linux/man/1-lavrec/">lavrec</a></code>(1), <code><a href="/docs/linux/man/1-glav/">glav</a></code>(1) </p>
<h2>Index</h2>
