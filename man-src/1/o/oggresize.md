---
title: "oggresize(1)"
name: "oggresize"
section: "1"
letter: "o"
url: "/docs/linux/man/1-oggresize/"
description: "oggResize – resizes ogg files in multiple ways"
---

<p>oggResize &#8211; resizes ogg files in multiple ways</p>
<h2>Synopsis</h2>
<p><code>oggResize [options] inputfile.ogv outputfile.ogv </code></p>
<h2>Description</h2>
<p><code>oggResize </code> can resize an ogg file (ogg, oga or ogv) in multiple ways: It can change the video frame size, change datarate for the video and/or audio streams contained in the ogg file and it can also change the video frame rate or audio sample rate. </p>
<p> Additionally, since version 0.8 <code>oggResize </code> can add any ogg comment and png-pictures with an alpha channel can be rendered into the video at any time period before and after the resizing process. </p>
<h2>Options</h2>
<dl COMPACT>
<dt>-s</p>
<dd>Sets the size of the video frame. The size is given as <code>&lt;width&gt;x&lt;height&gt;</code> The default size is 480&#215;320. </p>
<p> <i>Example: -s 320&#215;240</i> </p>
<dt>-d</p>
<dd>Sets the datarate in byte per seconds for the video encoder (theora). This meant to be a upper threshold. So the file may be smaller than assumed. If not set, the datarate of the original stream is used. </p>
<p> <i>Example: -d 1024000</i> </p>
<dt>-D</p>
<dd>Sets the datarate in byte per seconds for the audio encoder (vorbis). If not set, the datarate of the original stream is used. </p>
<p> <i>Example: -D 64000</i> </p>
<dt>-f</p>
<dd>Sets the frame rate of the video with numinator and demoninator and is the pictures per second. If only one number is given, the denominator is set to 1. If not set, the framerate of the original video is used. </p>
<p> <i>Example: -f 25:2</i> </p>
<dt>-F</p>
<dd>Sets the sample frequency (sample rate) of the audio data in Hertz. If the sample frequency does not match the one with the original file, resamling is invoked. </p>
<p> <i>Example: -F 32000</i> </p>
<dt>-c</p>
<dd>Adds comments to the video (theora) stream. Comments are given by a pair of type and value in the form &#8216;type=value&#8217;. More than one comment can be concatenated with a semicolon. It is recommended to use apostrophes as the command line may use the semicolon as a seperator. </p>
<p> <i>Example: -c &#8216;AUTHOR=yorn;DATE=03.07.09&#8217;</i> </p>
<dt>-C</p>
<dd>Adds comments to the audio (vorbis) stream. Comments are given by a pair of type and value in the form &#8216;type=value&#8217;. More than one comment can be concatenated with a semicolon. It is recommended to use apostrophes as the command line may use the semicolon as a seperator. </p>
<p> <i>Example: -C &#8216;AUTHOR=yorn;DATE=03.07.09&#8217;</i> </p>
<dt>-q</p>
<dd>Specifies the quality for the resizing process. Values can be chosen between 1 (best quality, with slight bluring) and 6 (worst quality). The default value is 2. </p>
<p> <i>Example: -q1</i> </p>
<dt>-p</p>
<dd>This option is meant to help creating a preview of a film. The number given with this option defines the number of frames, that are omitted. E.g. if a film has 24 frames per second and -p24 is given, the newly created video shows the video 24 times faster as only every 24th frame is used. This option can be combined with the option -f to control the framerate. With both options nice video previews can be created. If -p is used, the audio stream is ignored. </p>
<p> <i>Example: -p 24</i> </p>
<dt>-a</p>
<dd>Adds a picture to the video frame before it is resized. The expression for the picture appearances: </p>
<p> <code>&lt;picture1.png&gt;[,&lt;startTime&gt;[,&lt;endTime&gt;[,s]]]</code> </p>
<p> default <code>startTime </code> is 0 </p>
<p> default <code>endTime</code> is -1, which is the end of the stream duration </p>
<p> default <code>s </code> ist not set. If <code>s </code> is set, the picture slides in smoothly. </p>
<p> More than one picture can be included. To concatenate the expressions use the colon. If the appearance time overlap, the pictures are placed on one another, so the last picture is the uppest layer. </p>
<p> <i>Example: -a etwas.png,2,7,s:etwasneues.png,5,10</i> </p>
<dt>-A</p>
<dd>Adds a picture to the video frame after it is resized. </p>
<p> The syntax follows the same expression as with option -a. </p>
</dl>
<h2>Example</h2>
<p><i>oggResize -s320x240 -d512000 orig.ogv new.ogv</i> </p>
<p> Converts a the video <code>orig.ogv </code> to the video <code>new.ogv </code> with the new frame size 320&#215;240. If there was an audio stream within the orig.ogv file, it is copied into the new file. </p>
<p> <i>oggResize -D64000 -F16000 -N1 orig.ogv new.ogv</i> </p>
<p> Converts only the audio stream of file <code>orig.ogv </code> to a sample rate of 16kHz, a datarate of 64 kBit/s and a mono channel. The video stream is copied as is. </p>
<p> <i>oggResize -s300x200 -D32000 -d1024000 -A etwas.png,2,7,s:etwasneues.png,5,10 orig.ogv new.ogv</i> </p>
<p> Converts the audio and video stream and adds the alpha channel picture <code>etwas.png </code> to the video from second 2 to second 7 with a smooth fade in and fade out. Additionally the alpha channel picture <code>etwasneues.png</code> is placed on top of the video frame from second 5 to second 10 without any fading. </p>
<h2>Author</h2>
<p>Joern Seger &lt;yorn at gmx dot net&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-oggcut/">oggCut</a></code>(1), <code><a href="/docs/linux/man/1-oggcat/">oggCat</a></code>(1), <code><a href="/docs/linux/man/1-oggjoin/">oggJoin</a></code>(1), <code><a href="/docs/linux/man/1-oggsplit/">oggSplit</a></code>(1), <code><a href="/docs/linux/man/1-oggslideshow/">oggSlideshow</a></code>(1), <code><a href="/docs/linux/man/1-oggthumb/">oggThumb</a></code>(1), <code><a href="/docs/linux/man/1-oggsilence/">oggSilence</a></code>(1)</p>
