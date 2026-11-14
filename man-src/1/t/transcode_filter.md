---
title: "transcode_filter(1)"
name: "transcode_filter"
section: "1"
letter: "t"
url: "/docs/linux/man/1-transcode_filter/"
description: "transcode – filter modules collection"
---

<h2>NAME</h2>
<p> transcode &#8211; filter modules collection</p>
<h2>SYNOPSIS</h2>
<p> <code>transcode -J filters [other options]</code></p>
<h2>COPYRIGHT</h2>
<p> <code>transcode</code> is Copyright (C) 2001-2003 by Thomas Oestreich, 2003-2004 Tilmann Bitterberg, 2004-2008 Transcode Team </p>
<h2>MODULE OPTIONS</h2>
<p> The syntax for filter options is simple. A filter is specified with </p>
<dl>
<dt>
<dd>
<pre>
-J filter=<i>optionstring</i>
</pre>
</dl>
<p> The optionstring can contain multiple options which are separated by colons `:&#8217; </p>
<dl>
<dt>
<dd>
<pre>
-J filter=<i>option1</i>:<i>option2</i>:<i>option3</i>
</pre>
</dl>
<p> An option can have an argument or non (bool). For options with an argument, the format in which the argument has to be given to the option is specified in a <a href="/docs/linux/man/1-printf/">printf</a>(1) like string. The most common case is `%d&#8217; which simply means a number. The argument has to be seperated from the option by a `=&#8217;. </p>
<dl>
<dt>
<dd>
<pre>
-J filter=<i>bool1</i>:<i>option1</i>=<i>15</i>:<i>option2</i>=<i>20x30</i>
</pre>
</dl>
<p> Most filters try to do the right thing with the default options. You should play with various parameters if you are not satisfied with the default behaviour. If you have no idea what a filter does, its very likely that you don&#8217;t need it. </p>
<p> If a filter takes (for eg.) a filename as an argument, make sure that the filename does not contain a `:&#8217; or a `=&#8217;. Its a limitation of the parser. A comma `,&#8217; is possible but must be extra quoted. For the text filter that is </p>
<dl>
<dt>
<dd>
<pre>
-J text=string=&quot;Hello\, World&quot;
</pre>
</dl>
<h2>FILTER MODULES</h2>
<p> To see what filter modules are avalaible for your transcode installation, do a </p>
<dl>
<dt>
<dd> <code>ls -1 $( tcmodinfo -p )/filter*.so</code></dl>
<p> A complete transcode installation has the following filter modules: </p>
<dl>
<dt><code>29to23</code> &#8211; <code>frame rate conversion filter (interpolating 29 to 23)</code></p>
<dd> <code>29to23</code> was written by Max Alekseyev, Tilmann Bitterberg. The version documented here is v0.3 (2003-07-18). This is a video filter. It can handle RGB and YUV mode. It is a pre-processing only filter.</p>
<dt><code>32detect</code> &#8211; <code>3:2 pulldown / interlace detection plugin</code></p>
<dd> <code>32detect</code> was written by Thomas. The version documented here is v0.2.4 (2003-07-22). This is a video filter. It can handle RGB and YUV mode. It supports multiple instances and can run as a pre-processing and/or as a post-processing filter.</p>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; <i>threshold</i> = <i>%d</i> [default <i>9</i>]</p>
<dl>
<dt>
<dd> Interlace detection threshold</dl>
<p> &bull; <i>chromathres</i> = <i>%d</i> [default <i>4</i>]</p>
<dl>
<dt>
<dd> Interlace detection chroma threshold</dl>
<p> &bull; <i>equal</i> = <i>%d</i> [default <i>10</i>]</p>
<dl>
<dt>
<dd> threshold for equal colors</dl>
<p> &bull; <i>chromaeq</i> = <i>%d</i> [default <i>5</i>]</p>
<dl>
<dt>
<dd> threshold for equal chroma</dl>
<p> &bull; <i>diff</i> = <i>%d</i> [default <i>30</i>]</p>
<dl>
<dt>
<dd> threshold for different colors</dl>
<p> &bull; <i>chromadi</i> = <i>%d</i> [default <i>15</i>]</p>
<dl>
<dt>
<dd> threshold for different chroma</dl>
<p> &bull; <i>force_mode</i> = <i>%d</i> [default <i>0</i>]</p>
<dl>
<dt>
<dd> set internal force de-interlace flag with mode -I N</dl>
<p> &bull; <i>pre</i> = <i>%d</i> [default <i>1</i>]</p>
<dl>
<dt>
<dd> run as pre filter</dl>
<p> &bull; <i>verbose</i> (bool)</p>
<dl>
<dt>
<dd> show results</dl>
<dl>
<dt>
<dd> This filter checks for interlaced video frames. Subsequent de-interlacing with transcode can be enforced with &#8216;force_mode&#8217; option</dl>
</dl>
<dt><code>32drop</code> &#8211; <code>3:2 inverse telecine removal plugin</code></p>
<dd> <code>32drop</code> was written by Thomas Oestreich. The version documented here is v0.4 (2003-02-01). This is a video filter. It can handle RGB and YUV mode. It is a pre-processing only filter.</p>
<dt><code>aclip</code> &#8211; <code>generate audio clips from source</code></p>
<dd> <code>aclip</code> was written by Thomas Oestreich. The version documented here is v0.1.1 (2003-09-04). This is a audio filter. It is a pre-processing only filter.</p>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; <i>level</i> = <i>%d</i> [default <i>10</i>]</p>
<dl>
<dt>
<dd> The audio must be under this level to be skipped</dl>
<p> &bull; <i>range</i> = <i>%d</i> [default <i>25</i>]</p>
<dl>
<dt>
<dd> Number of samples over level will be keyframes</dl>
</dl>
<dt><code>astat</code> &#8211; <code>audio statistics filter plugin</code></p>
<dd> <code>astat</code> was written by Thomas Oestreich. The version documented here is v0.1.3 (2003-09-04). This is a audio filter. It is a pre-processing only filter.</p>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; <i>file</i> = <i>%s</i></p>
<dl>
<dt>
<dd> File to save the calculated volume rescale number to</dl>
</dl>
<dt><code>compare</code> &#8211; <code>compare with other image to find a pattern</code></p>
<dd> <code>compare</code> was written by Antonio Beamud. The version documented here is v0.1.2 (2003-08-29). This is a video filter. It can handle RGB and YUV mode. It supports multiple instances. It is a post-processing only filter.</p>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; <i>pattern</i> = <i>%s</i></p>
<dl>
<dt>
<dd> Pattern image file path</dl>
<p> &bull; <i>results</i> = <i>%s</i></p>
<dl>
<dt>
<dd> Results file path</dl>
<p> &bull; <i>delta</i> = <i>%f</i> [default <i>45.000000</i>]</p>
<dl>
<dt>
<dd> Delta error</dl>
<dl>
<dt>
<dd> Generate a file in with information about the times, frame, etc the pattern defined in the image parameter is observed.</dl>
</dl>
<dt>
<dd> The format of the command file is framenumber followed by at least one whitespace followed by the command followed by at least one whitespace followed by arguments for the command. Empty lines and lines starting with a `#&#8217; are ignored. The frame numbers must be sorted ascending. </p>
<p>#&nbsp;<wbr>Example file<br />
#&nbsp;<wbr>At frame 10 load the smooth filter<br />
10 load smooth<br />
#&nbsp;<wbr>reconfigure at 20<br />
20 configure smooth=strength=0.9<br />
99 disable smooth </p>
<dt><code>cpaudio</code> &#8211; <code>copy one audio channel to the other channel filter plugin</code></p>
<dd> <code>cpaudio</code> was written by William H Wittig. The version documented here is v0.1 (2003-04-30). This is a audio filter. It is a post-processing only filter.</p>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; <i>source</i> = <i>%c</i> [default <i>l</i>]</p>
<dl>
<dt>
<dd> Source channel (l=left, r=right)</dl>
<dl>
<dt>
<dd> Copies audio from one channel to another</dl>
</dl>
<dt><code>decimate</code> &#8211; <code>NTSC decimation plugin</code></p>
<dd> <code>decimate</code> was written by Thanassis Tsiodras. The version documented here is v0.4 (2003-04-22). This is a video filter. It can handle YUV mode only. It is a post-processing only filter.</p>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; <i>verbose</i> (bool)</p>
<dl>
<dt>
<dd> print verbose information</dl>
<dl>
<dt>
<dd> see /docs/README.Inverse.Telecine.txt</dl>
</dl>
<dt><code>denoise3d</code> &#8211; <code>High speed 3D Denoiser</code></p>
<dd> <code>denoise3d</code> was written by Daniel Moreno &amp; A&#8217;rpi. The version documented here is v1.0.6 (2003-12-20). This is a video filter. It can handle YUV mode only. It supports multiple instances. It can be used as a pre-processing or as a post-processing filter.</p>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; <i>luma</i> = <i>%f</i> [default <i>4.000000</i>]</p>
<dl>
<dt>
<dd> spatial luma strength</dl>
<p> &bull; <i>chroma</i> = <i>%f</i> [default <i>3.000000</i>]</p>
<dl>
<dt>
<dd> spatial chroma strength</dl>
<p> &bull; <i>luma_strength</i> = <i>%f</i> [default <i>6.000000</i>]</p>
<dl>
<dt>
<dd> temporal luma strength</dl>
<p> &bull; <i>chroma_strength</i> = <i>%f</i> [default <i>4.000000</i>]</p>
<dl>
<dt>
<dd> temporal chroma strength</dl>
<p> &bull; <i>pre</i> = <i>%d</i> [default <i>0</i>]</p>
<dl>
<dt>
<dd> run as a pre filter</dl>
<dl>
<dt>
<dd> What: The denoise3d filter from mplayer (sibling of hqdn3d). Works very crude and simple but also very fast. In fact it is even faster than the original from mplayer as I managed to tweak some things (a.o. zero frame copying). </p>
<p> Who: Everyone who wants to have their captured frames thoroughly denoised (i.e. who want to encode to mpeg or mjpeg) but do not have enough processing power to real-time encode AND use hqdn3d (better quality but a lot slower) or dnr (yet slower), not to mention the other denoisers that are even slower. Quality is really good for static scenes (if fed with the right parameters), moving objects may show a little ghost-image (also depends on parameters) though. Your milage may vary. </p>
<p> How: Parameters are the same as the hqdn3d module, although in practice you&#8217;ll not end up with exactly the same values. Just experiment. Particular for this version of the filter is that if you supply -1 to either component&#8217;s parameters (luma/chroma), that component will not have the filter applied to. If you&#8217;re still short on CPU cycles, try disabling the luma filter, this will not make much difference in the effectiveness of the filter!</dl>
</dl>
<dt><code>detectclipping</code> &#8211; <code>detect clipping parameters (-j or -Y)</code></p>
<dd> <code>detectclipping</code> was written by Tilmann Bitterberg, A&#8217;rpi. The version documented here is v0.1.0 (2003-11-01). This is a video filter. It can handle RGB and YUV mode. It supports multiple instances and can run as a pre-processing and/or as a post-processing filter.</p>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; <i>range</i> = <i>%u-%u/%d</i> [default <i>0-4294967295/1</i>]</p>
<dl>
<dt>
<dd> apply filter to [start-end]/step frames</dl>
<p> &bull; <i>limit</i> = <i>%d</i> [default <i>24</i>]</p>
<dl>
<dt>
<dd> the sum of a line must be below this limit to be considered as black</dl>
<p> &bull; <i>post</i> (bool)</p>
<dl>
<dt>
<dd> run as a POST filter (calc -Y instead of the default -j)</dl>
<dl>
<dt>
<dd> Detect black regions on top, bottom, left and right of an image. It is suggested that the filter is run for around 100 frames. It will print its detected parameters every frame. If you don&#8217;t notice any change in the printout for a while, the filter probably won&#8217;t find any other values. The filter converges, meaning it will learn.</dl>
</dl>
<dt><code>detectsilence</code> &#8211; <code>audio silence detection with tcmp3cut commandline generation</code></p>
<dd> <code>detectsilence</code> was written by Tilmann Bitterberg. The version documented here is v0.0.1 (2003-07-26). This is a audio filter. It is a pre-processing only filter.</p>
<dt><code>divxkey</code> &#8211; <code>check for DivX 4.xx / OpenDivX / DivX;-) keyframe</code></p>
<dd> <code>divxkey</code> was written by Thomas Oestreich. The version documented here is v0.1 (2002-01-15). This is a video filter. It is a pre-processing only filter.</p>
<dt><code>dnr</code> &#8211; <code>dynamic noise reduction</code></p>
<dd> <code>dnr</code> was written by Gerhard Monzel. The version documented here is v0.2 (2003-01-21). This is a video filter. It can handle RGB and YUV mode. It is a post-processing only filter.</p>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; <i>lt</i> = <i>%d</i> [default <i>10</i>]</p>
<dl>
<dt>
<dd> Threshold to blend luma/red</dl>
<p> &bull; <i>ll</i> = <i>%d</i> [default <i>4</i>]</p>
<dl>
<dt>
<dd> Threshold to lock luma/red</dl>
<p> &bull; <i>ct</i> = <i>%d</i> [default <i>16</i>]</p>
<dl>
<dt>
<dd> Threshold to blend croma/green+blue</dl>
<p> &bull; <i>cl</i> = <i>%d</i> [default <i>8</i>]</p>
<dl>
<dt>
<dd> Threshold to lock croma/green+blue</dl>
<p> &bull; <i>sc</i> = <i>%d</i> [default <i>30</i>]</p>
<dl>
<dt>
<dd> Percentage of picture difference (scene change)</dl>
<dl>
<dt>
<dd> see /docs/filter_dnr.txt (german only)</dl>
</dl>
<dt><code>doublefps</code> &#8211; <code>double frame rate by deinterlacing fields into frames</code></p>
<dd> <code>doublefps</code> was written by Andrew Church. The version documented here is v1.1 (2006-05-14). This is a video and audio filter. It can handle YUV and YUV422 modes. It is a pre-processing only filter.</p>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; <i>topfirst</i> = <i>%d</i> [default <i>0</i> when height=480, else <i>1</i>]</p>
<dl>
<dt>
<dd> Assume top field is displayed first</dl>
<p> &bull; <i>fullheight</i> = <i>%d</i> [default <i>0</i>]</p>
<dl>
<dt>
<dd> Output full-height frames</dl>
<p> Doubles the frame rate of interlaced video by separating each field into a separate frame. The fields can either be left as is (giving a progessive video with half the height of the original) or re-interlaced into their original height (at the doubled frame rate) for the application of a separate deinterlacing filter. </p>
<p> Note that due to transcode limitations, it is currently necessary to use the -Z option to specify the output frame size when using half-height mode (this does not slow the program down if no actual zooming is done).</dl>
<dt><code>extsub</code> &#8211; <code>DVD subtitle overlay plugin</code></p>
<dd> <code>extsub</code> was written by Thomas Oestreich. The version documented here is 0.3.5 (2003-10-15). This is a video filter. It can handle RGB and YUV mode. It can be used as a pre-processing or as a post-processing filter.</p>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; <i>track</i> = <i>%d</i> [default <i>0</i>]</p>
<dl>
<dt>
<dd> Subtitle track to render</dl>
<p> &bull; <i>vertshift</i> = <i>%d</i> [default <i>0</i>]</p>
<dl>
<dt>
<dd> offset of subtitle with respect to bottom of frame in rows</dl>
<p> &bull; <i>timeshift</i> = <i>%d</i> [default <i>0</i>]</p>
<dl>
<dt>
<dd> global display start time correction in msec</dl>
<p> &bull; <i>antialias</i> = <i>%d</i> [default <i>1</i>]</p>
<dl>
<dt>
<dd> anti-aliasing the rendered text (0=off,1=on)</dl>
<p> &bull; <i>pre</i> = <i>%d</i> [default <i>1</i>]</p>
<dl>
<dt>
<dd> Run as a pre filter</dl>
<p> &bull; <i>color1</i> = <i>%d</i> [default <i>0</i>]</p>
<dl>
<dt>
<dd> Make a subtitle color visible with given intensity</dl>
<p> &bull; <i>color2</i> = <i>%d</i> [default <i>0</i>]</p>
<dl>
<dt>
<dd> Make a subtitle color visible with given intensity</dl>
<p> &bull; <i>ca</i> = <i>%d</i> [default <i>0</i>]</p>
<dl>
<dt>
<dd> Shuffle the color assignment by choosing another subtitle color</dl>
<p> &bull; <i>cb</i> = <i>%d</i> [default <i>0</i>]</p>
<dl>
<dt>
<dd> Shuffle the color assignment by choosing another subtitle color</dl>
</dl>
<dt><code>fieldanalysis</code> &#8211; <code>Field analysis for detecting interlace and telecine</code></p>
<dd> <code>fieldanalysis</code> was written by Matthias Hopf. The version documented here is v1.0 pl1 (2004-08-13). This is a video filter. It can handle RGB,YUV and YUV422 mode. It is a pre-processing only filter.</p>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; <i>interlacediff</i> = <i>%f</i> [default <i>1.1</i>]</p>
<dl>
<dt>
<dd> Minimum temporal inter-field difference for detecting interlaced video</dl>
<p> &bull; <i>unknowndiff</i> = <i>%f</i> [default <i>1.5</i>]</p>
<dl>
<dt>
<dd> Maximum inter-frame change vs. detail differences for neglecting interlaced video</dl>
<p> &bull; <i>progressivediff</i> = <i>%f</i> [default <i>8</i>]</p>
<dl>
<dt>
<dd> Minimum inter-frame change vs. detail differences for detecting progressive video</dl>
<p> &bull; <i>progressivechange</i> = <i>%f</i> [default <i>0.2</i>]</p>
<dl>
<dt>
<dd> Minimum temporal change needed for detecting progressive video</dl>
<p> &bull; <i>changedifmore</i> = <i>%f</i> [default <i>10</i>]</p>
<dl>
<dt>
<dd> Minimum temporal change for detecting truly changed frames</dl>
<p> &bull; <i>forcetelecinedetect</i> = <i>%d</i> [default <i>0</i>]</p>
<dl>
<dt>
<dd> Detect telecine even on non-NTSC (29.97fps) video</dl>
<p> &bull; <i>verbose</i> = <i>%d</i> [default <i>0</i>]</p>
<dl>
<dt>
<dd> Output analysis for every frame</dl>
<p> &bull; <i>outdiff</i> = <i>%d</i> [default <i>0</i>]</p>
<dl>
<dt>
<dd> Output internal debug frames as luminance of YUV video (see source)</dl>
</dl>
<dt><code>fields</code> &#8211; <code>Field adjustment plugin</code></p>
<dd> <code>fields</code> was written by Alex Stewart. The version documented here is v0.1.1 (2003-01-21). This is a video filter. It can handle RGB and YUV mode. It is a pre-processing only filter.</p>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; <i>flip</i> (bool)</p>
<dl>
<dt>
<dd> Exchange the top field and bottom field of each frame</dl>
<p> &bull; <i>shift</i> (bool)</p>
<dl>
<dt>
<dd> Shift the video by one field</dl>
<p> &bull; <i>flip_first</i> (bool)</p>
<dl>
<dt>
<dd> Normally shifting is performed before flipping, this option reverses that</dl>
<dl>
<dt>
<dd> The &#8216;fields&#8217; filter is designed to shift, reorder, and generally rearrange independent fields of an interlaced video input. Input retrieved from broadcast (PAL, NTSC, etc) video sources generally comes in an interlaced form where each pass from top to bottom of the screen displays every other scanline, and then the next pass displays the lines between the lines from the first pass. Each pass is known as a &quot;field&quot; (there are generally two fields per frame). When this form of video is captured and manipulated digitally, the two fields of each frame are usually merged together into one flat (planar) image per frame. This usually produces reasonable results, however there are conditions which can cause this merging to be performed incorrectly or less-than-optimally, which is where this filter can help. </p>
<p> The following options are supported for this filter (they can be separated by colons): </p>
<p>&nbsp;<wbr>&nbsp;<wbr>shift &#8211; Shift the video by one field&nbsp;<wbr>(half a frame),<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>changing frame boundaries appropriately.&nbsp;<wbr>&nbsp;<wbr>This is<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>useful if a video capture started grabbing video<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>half a frame&nbsp;<wbr>(one field)&nbsp;<wbr>off from where frame<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>boundaries were actually intended to be. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>flip&nbsp;<wbr>&nbsp;<wbr>&#8211; Exchange the top field and bottom field of each<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>frame.&nbsp;<wbr>&nbsp;<wbr>This can be useful if the video signal was<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>sent&nbsp;<wbr>&quot;bottom field first&quot;&nbsp;<wbr>(which can happen<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>sometimes with PAL video sources)&nbsp;<wbr>or other<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>oddities occurred which caused the frame<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>boundaries to be at the right place, but the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>scanlines to be swapped. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>flip_first<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; Normally shifting is performed before flipping if<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>both are specified.&nbsp;<wbr>&nbsp;<wbr>This option reverses that<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>behavior.&nbsp;<wbr>&nbsp;<wbr>You should not normally need to use<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>this unless you have some extremely odd input<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>material, it is here mainly for completeness. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>help&nbsp;<wbr>&nbsp;<wbr>&#8211; Print this text. </p>
<p> Note: the &#8216;shift&#8217; function may produce slight color discrepancies if YV12 is used as the internal transcode video format (default). This is because YV12 does not contain enough information to do field shifting cleanly. For best (but slower) results, use RGB mode for field shifting.</dl>
</dl>
<dt><code>fps</code> &#8211; <code>convert video frame rate, gets defaults from -f and &#8211;export_fps</code></p>
<dd> <code>fps</code> was written by Christopher Cramer. The version documented here is v1.1 (2004-05-01). This is a video filter. It can handle RGB and YUV mode. It can be used as a pre-processing or as a post-processing filter.</p>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> options: &lt;input fps&gt;:&lt;output fps&gt; example: -J fps=25:29.97 will convert from PAL to NTSC If no options are given, defaults or -f/&#8211;export_fps/&#8211;export_frc will be used. Some examples: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-J fps=10:5:pre<tt>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>convert from 10 fps to 5 fps, preprocess<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-J fps=10:post:12<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>convert from 10 to 12, postprocess<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-J fps=pre=1:7:5<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>convert from 7 to 5, postprocess<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-J fps=9:3.1:post=-0x7<tt>&nbsp;<wbr>&nbsp;<wbr></tt>convert from 9 to 3.1, postprocess</p>
<p> If that last one is confusing you, remember that 0 is false and everything else is true. Of course, octal and hexadecimal numbers are supported too. This is intended to be backward compatible with the old format.</dl>
</dl>
<dt><code>hqdn3d</code> &#8211; <code>High Quality 3D Denoiser</code></p>
<dd> <code>hqdn3d</code> was written by Daniel Moreno &amp; A&#8217;rpi. The version documented here is v1.0.2 (2003-08-15). This is a video filter. It can handle YUV mode only. It supports multiple instances. It can be used as a pre-processing or as a post-processing filter.</p>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; <i>luma</i> = <i>%f</i> [default <i>4.000000</i>]</p>
<dl>
<dt>
<dd> spatial luma strength</dl>
<p> &bull; <i>chroma</i> = <i>%f</i> [default <i>3.000000</i>]</p>
<dl>
<dt>
<dd> spatial chroma strength</dl>
<p> &bull; <i>luma_strength</i> = <i>%f</i> [default <i>6.000000</i>]</p>
<dl>
<dt>
<dd> temporal luma strength</dl>
<p> &bull; <i>chroma_strength</i> = <i>%f</i> [default <i>4.500000</i>]</p>
<dl>
<dt>
<dd> temporal chroma strength</dl>
<p> &bull; <i>pre</i> = <i>%d</i> [default <i>0</i>]</p>
<dl>
<dt>
<dd> run as a pre filter</dl>
<dl>
<dt>
<dd> This filter aims to reduce image noise producing smooth images and making still images really still (This should enhance compressibility).</dl>
</dl>
<dt><code>invert</code> &#8211; <code>invert the image</code></p>
<dd> <code>invert</code> was written by Tilmann Bitterberg. The version documented here is v0.1.4 (2003-10-12). This is a video filter. It can handle RGB,YUV and YUV422 mode. It is a post-processing only filter.</p>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; <i>range</i> = <i>%u-%u/%d</i> [default <i>0-4294967295/1</i>]</p>
<dl>
<dt>
<dd> apply filter to [start-end]/step frames</dl>
</dl>
<dt><code>ivtc</code> &#8211; <code>NTSC inverse telecine plugin</code></p>
<dd> <code>ivtc</code> was written by Thanassis Tsiodras. The version documented here is v0.4.1 (2004-06-01). This is a video filter. It can handle YUV mode only. It is a pre-processing only filter.</p>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; <i>verbose</i> (bool)</p>
<dl>
<dt>
<dd> print verbose information</dl>
<p> &bull; <i>field</i> = <i>%d</i> [default <i>0</i>]</p>
<dl>
<dt>
<dd> which field to replace (0=top 1=bottom)</dl>
<p> &bull; <i>magic</i> = <i>%d</i> [default <i>0</i>]</p>
<dl>
<dt>
<dd> perform magic? (0=no 1=yes)</dl>
<dl>
<dt>
<dd> see /docs/README.Inverse.Telecine.txt</dl>
</dl>
<dt><code>levels</code> &#8211; <code>Luminosity level scaler</code></p>
<dd> <code>levels</code> was written by Bryan Mayland. The version documented here is v1.0.0 (2004-06-09). This is a video filter. It can handle YUV mode only. It supports multiple instances. It is a post-processing only filter.</p>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; <i>input</i> = <i>%d-%d</i> [default <i>0-255</i>]</p>
<dl>
<dt>
<dd> input luma range (black-white)</dl>
<p> &bull; <i>gamma</i> = <i>%f</i> [default <i>1.000000</i>]</p>
<dl>
<dt>
<dd> input luma gamma</dl>
<p> &bull; <i>output</i> = <i>%d-%d</i> [default <i>0-255</i>]</p>
<dl>
<dt>
<dd> output luma range (black-white)</dl>
</dl>
<dt><code>logo</code> &#8211; <code>render image in videostream</code></p>
<dd> <code>logo</code> was written by Tilmann Bitterberg. The version documented here is v0.10 (2003-10-16). This is a video filter. It can handle RGB and YUV mode. It is a post-processing only filter.</p>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; <i>file</i> = <i>%s</i></p>
<dl>
<dt>
<dd> Image filename</dl>
<p> &bull; <i>posdef</i> = <i>%d</i> [default <i>0</i>]</p>
<dl>
<dt>
<dd> Position (0=None, 1=TopL, 2=TopR, 3=BotL, 4=BotR, 5=Center)</dl>
<p> &bull; <i>pos</i> = <i>%dx%d</i> [default <i>0x0</i>]</p>
<dl>
<dt>
<dd> Position (0-width x 0-height)</dl>
<p> &bull; <i>range</i> = <i>%u-%u</i> [default <i>0-0</i>]</p>
<dl>
<dt>
<dd> Restrict rendering to framerange</dl>
<p> &bull; <i>ignoredelay</i> (bool)</p>
<dl>
<dt>
<dd> Ignore delay specified in animations</dl>
<p> &bull; <i>rgbswap</i> (bool)</p>
<dl>
<dt>
<dd> Swap red/blue colors</dl>
<p> &bull; <i>grayout</i> (bool)</p>
<dl>
<dt>
<dd> YUV only: don&#8217;t write Cb and Cr, makes a nice effect</dl>
<p> &bull; <i>flip</i> (bool)</p>
<dl>
<dt>
<dd> Mirror image</dl>
<dl>
<dt>
<dd> This filter renders an user specified image into the video. Any image format ImageMagick can read is accepted. Transparent images are also supported. Image origin is at the very top left. </p>
<p> see /docs/filter_logo.txt</dl>
</dl>
<dt><code>logoaway</code> &#8211; <code>remove an image from the video</code></p>
<dd> <code>logoaway</code> was written by Thomas Wehrspann &lt;thomas [at] wehrspann.de&gt;. The version documented here is v0.5 (2004-03-07). This is a video filter. It can handle RGB and YUV mode. It is a post-processing only filter. It supports multiple instances.</p>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; <i>range</i> = <i>%d-%d</i> [default <i>0-4294967295</i>]</p>
<dl>
<dt>
<dd> Frame Range</dl>
<p> &bull; <i>pos</i> = <i>%dx%d</i> [default <i>-1x-1</i>]</p>
<dl>
<dt>
<dd> Position of logo</dl>
<p> &bull; <i>size</i> = <i>%dx%d</i> [default <i>-2x-2</i>]</p>
<dl>
<dt>
<dd> Size of logo</dl>
<p> &bull; <i>mode</i> = <i>%d</i> [default <i>0</i>]</p>
<dl>
<dt>
<dd> Filter Mode (0=none,1=solid,2=xy,3=shape)</dl>
<p> &bull; <i>border</i> (bool)</p>
<dl>
<dt>
<dd> Visible Border</dl>
<p> &bull; <i>dump</i> (bool)</p>
<dl>
<dt>
<dd> Dump filterarea to file</dl>
<p> &bull; <i>xweight</i> = <i>%d</i> [default <i>50</i>]</p>
<dl>
<dt>
<dd> X-Y Weight(0%-100%)</dl>
<p> &bull; <i>fill</i> = <i>%2x%2x%2x</i> [default <i>000</i>]</p>
<dl>
<dt>
<dd> Solid Fill Color(RGB)</dl>
<p> &bull; <i>file</i> = <i>%s</i></p>
<dl>
<dt>
<dd> Image with alpha/shape information</dl>
<dl>
<dt>
<dd> This filter removes an image in a user specified area from the video. You can choose from different methods. </p>
<p> see /docs/filter_logoaway.txt</dl>
</dl>
<dt><code>lowpass</code> &#8211; <code>High and low pass filter</code></p>
<dd> <code>lowpass</code> was written by Tilmann Bitterberg. The version documented here is v0.1.0 (2002-02-26). This is a audio filter. It is a pre-processing only filter.</p>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; <i>taps</i> = <i>%d</i> [default <i>30</i>]</p>
<dl>
<dt>
<dd> strength (may be negative)</dl>
</dl>
<dt><code>mask</code> &#8211; <code>Filter through a rectangular Mask</code></p>
<dd> <code>mask</code> was written by Thomas Oestreich, Chad Page. The version documented here is v0.2.3 (2003-10-12). This is a video filter. It can handle RGB,YUV and YUV422 mode. It is a pre-processing only filter.</p>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; <i>lefttop</i> = <i>%dx%d</i> [default <i>0x0</i>]</p>
<dl>
<dt>
<dd> Upper left corner of the box</dl>
<p> &bull; <i>rightbot</i> = <i>%dx%d</i> [default <i>32&#215;32</i>]</p>
<dl>
<dt>
<dd> Lower right corner of the box</dl>
<dl>
<dt>
<dd> This filter applies an rectangular mask to the video. Everything outside the mask is set to black.</dl>
</dl>
<dt><code>modfps</code> &#8211; <code>plugin to modify framerate</code></p>
<dd> <code>modfps</code> was written by Marrq. The version documented here is v0.10 (2003-08-18). This is a video filter. It can handle RGB and YUV mode. It is a pre-processing only filter.</p>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; <i>mode</i> = <i>%d</i> [default <i>1</i>]</p>
<dl>
<dt>
<dd> mode of operation</dl>
<p> &bull; <i>infps</i> = <i>%f</i> [default <i>25.000000</i>]</p>
<dl>
<dt>
<dd> Original fps</dl>
<p> &bull; <i>infrc</i> = <i>%d</i> [default <i>0</i>]</p>
<dl>
<dt>
<dd> Original frc</dl>
<p> &bull; <i>buffer </i> = <i>%d</i> [default <i>5</i>]</p>
<dl>
<dt>
<dd> How many frames to buffer</dl>
<p> &bull; <i>subsample</i> = <i>%d</i> [default <i>32</i>]</p>
<dl>
<dt>
<dd> How many pixels to subsample</dl>
<p> &bull; <i>clonetype</i> = <i>%d</i> [default <i>0</i>]</p>
<dl>
<dt>
<dd> How to clone frames</dl>
<p> &bull; <i>verbose</i> = <i>%d</i> [default <i>1</i>]</p>
<dl>
<dt>
<dd> run in verbose mode</dl>
<dl>
<dt>
<dd> This filter aims to allow transcode to alter the fps of video. While one can reduce the fps to any amount, one can only increase the fps to at most twice the original fps. </p>
<p> There are two modes of operation, buffered and unbuffered, unbuffered is quick, but buffered, especially when dropping frames should look better. </p>
<p> For most users, modfps will need either no options, or just mode=1 </p>
<p> see /docs/README.filter.modfps</dl>
</dl>
<dt><code>msharpen</code> &#8211; <code>VirtualDub&#8217;s MSharpen Filter</code></p>
<dd> <code>msharpen</code> was written by Donald Graft, William Hawkins. The version documented here is (1.0) (2003-07-17). This is a video filter. It can handle RGB and YUV mode. It is a post-processing only filter.</p>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; <i>strength</i> = <i>%d</i> [default <i>100</i>]</p>
<dl>
<dt>
<dd> How much of the effect</dl>
<p> &bull; <i>threshold</i> = <i>%d</i> [default <i>10</i>]</p>
<dl>
<dt>
<dd> How close a pixel must be to the brightest or dimmest pixel to be mapped</dl>
<p> &bull; <i>highq</i> = <i>%d</i> [default <i>1</i>]</p>
<dl>
<dt>
<dd> Tradeoff speed for quality of detail detection</dl>
<p> &bull; <i>mask</i> = <i>%d</i> [default <i>0</i>]</p>
<dl>
<dt>
<dd> Areas to be sharpened are shown in white</dl>
<dl>
<dt>
<dd> This plugin implements an unusual concept in spatial sharpening. Although designed specifically for anime, it also works well with normal video. The filter is very effective at sharpening important edges without amplifying noise. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>Strength&nbsp;<wbr>&#8216;strength&#8217;&nbsp;<wbr>(0-255)&nbsp;<wbr>[100]<br />
&nbsp;<wbr>This is the strength of the sharpening to be applied to the edge detail areas. It is applied only to the edge detail areas as determined by the&nbsp;<wbr>&#8216;threshold&#8217;&nbsp;<wbr>parameter. Strength 255 is the strongest sharpening.<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>Threshold&nbsp;<wbr>&#8216;threshold&#8217;&nbsp;<wbr>(0-255)&nbsp;<wbr>[10]<br />
&nbsp;<wbr>This parameter determines what is detected as edge detail and thus sharpened. To see what edge detail areas will be sharpened, use the&nbsp;<wbr>&#8216;mask&#8217;&nbsp;<wbr>parameter.<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>Mask&nbsp;<wbr>&#8216;mask&#8217;&nbsp;<wbr>(0-1)&nbsp;<wbr>[0]<br />
&nbsp;<wbr>When set to true, the areas to be sharpened are shown in white against a black background. Use this to set the level of detail to be sharpened. This function also makes a basic edge detection filter.<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>HighQ&nbsp;<wbr>&#8216;highq&#8217;&nbsp;<wbr>(0-1)&nbsp;<wbr>[1]<br />
&nbsp;<wbr>This parameter lets you tradeoff speed for quality of detail detection. Set it to true for the best detail detection. Set it to false for maximum speed.</dl>
</dl>
<dt><code>normalize</code> &#8211; <code>Volume normalizer</code></p>
<dd> <code>normalize</code> was written by pl, Tilmann Bitterberg. The version documented here is v0.1.1 (2002-06-18). This is a audio filter. It is a pre-processing only filter.</p>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; <i>smooth</i> = <i>%f</i> [default <i>0.06</i>]</p>
<dl>
<dt>
<dd> Value for smoothing ]0.0 1.0[</dl>
<p> &bull; <i>smoothlast</i> = <i>%f</i> [default <i>0.06</i>]</p>
<dl>
<dt>
<dd> Value for smoothing last sample ]0.0, 1.0[</dl>
<p> &bull; <i>algo</i> = <i>%d</i> [default <i>1</i>]</p>
<dl>
<dt>
<dd> Algorithm to use (1 or 2). 1=uses a 1 value memory and coefficients new=a*old+b*cur (with a+b=1). 2=uses several samples to smooth the variations (standard weighted mean on past samples)</dl>
</dl>
<dt><code>null</code> &#8211; <code>demo filter plugin; does nothing</code></p>
<dd> <code>null</code> was written by Thomas Oestreich. The version documented here is v0.2 (2003-09-04). This is a video and audio filter. It can be used as a pre-processing or as a post-processing filter.</p>
<dt><code>pp</code> &#8211; <code>Mplayers postprocess filters</code></p>
<dd> <code>pp</code> was written by Michael Niedermayer et al, Gerhard Monzel. The version documented here is v1.2.4 (2003-01-24). This is a video filter. It can handle YUV mode only. It supports multiple instances. It can be used as a pre-processing or as a post-processing filter.</p>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; <i>hb</i> = <i>%d:%d</i> [default <i>64:40</i>]</p>
<dl>
<dt>
<dd> Horizontal deblocking filter</dl>
<p> &bull; <i>vb</i> = <i>%d:%d</i> [default <i>64:40</i>]</p>
<dl>
<dt>
<dd> Vertical deblocking filter</dl>
<p> &bull; <i>h1</i> (bool)</p>
<dl>
<dt>
<dd> Experimental h deblock filter 1</dl>
<p> &bull; <i>v1</i> (bool)</p>
<dl>
<dt>
<dd> Experimental v deblock filter 1</dl>
<p> &bull; <i>dr</i> (bool)</p>
<dl>
<dt>
<dd> Deringing filter</dl>
<p> &bull; <i>al</i> (bool)</p>
<dl>
<dt>
<dd> Automatic brightness / contrast</dl>
<p> &bull; <i>f</i> (bool)</p>
<dl>
<dt>
<dd> Stretch luminance to (0..255)</dl>
<p> &bull; <i>lb</i> (bool)</p>
<dl>
<dt>
<dd> Linear blend deinterlacer</dl>
<p> &bull; <i>li</i> (bool)</p>
<dl>
<dt>
<dd> Linear interpolating deinterlace</dl>
<p> &bull; <i>ci</i> (bool)</p>
<dl>
<dt>
<dd> Cubic interpolating deinterlacer</dl>
<p> &bull; <i>md</i> (bool)</p>
<dl>
<dt>
<dd> Median deinterlacer</dl>
<p> &bull; <i>de</i> (bool)</p>
<dl>
<dt>
<dd> Default preset (hb:a/vb:a/dr:a/al)</dl>
<p> &bull; <i>fa</i> (bool)</p>
<dl>
<dt>
<dd> Fast preset (h1:a/v1:a/dr:a/al)</dl>
<p> &bull; <i>tn</i> = <i>%d:%d:%d</i> [default <i>64:128:256</i>]</p>
<dl>
<dt>
<dd> Temporal Noise Reducer (1&lt;=2&lt;=3)</dl>
<p> &bull; <i>fq</i> = <i>%d</i> [default <i>15</i>]</p>
<dl>
<dt>
<dd> Force quantizer</dl>
<p> &bull; <i>pre</i> (bool)</p>
<dl>
<dt>
<dd> Run as a PRE filter</dl>
</dl>
<dt><code>preview</code> &#8211; <code>xv/sdl/gtk preview plugin</code></p>
<dd> <code>preview</code> was written by Thomas Oestreich. The version documented here is v0.1.4 (2002-10-08). This is a video filter. It can handle RGB and YUV mode. It is a post-processing only filter.</p>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> XXX: Write me</dl>
</dl>
<dt><code>pv</code> &#8211; <code>xv only preview plugin</code></p>
<dd> <code>pv</code> was written by Thomas Oestreich, Tilmann Bitterberg. The version documented here is v0.2.3 (2004-06-01). This is a video filter. It can handle YUV and YUV422 mode. It is a post-processing only filter.</p>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; <i>cache</i> = <i>%d</i> [default <i>15</i>]</p>
<dl>
<dt>
<dd> Number of raw frames to cache for seeking</dl>
<p> &bull; <i>skip</i> = <i>%d</i> [default <i>0</i>]</p>
<dl>
<dt>
<dd> display only every Nth frame</dl>
<p> &bull; <i>fullscreen</i> (bool)</p>
<dl>
<dt>
<dd> Display in fullscreen mode</dl>
<dl>
<dt>
<dd> The filter listens to mouse and key strokes. If you click into the preview window, the first time say near the upper left corner and the second time near the lower right corner, transcode will draw a rectangle and will print out the coordinates of this rectangle on stdout and the socket. See the table below for available keys. </p>
<p> When you start transcode with the &#8211;socket option and the pv filter with (for example) cache=20 you can talk to transcode and the pv filter at runtime using the socket. </p>
<pre>
transcode -i file.avi -J pv=cache=30 --socket /tmp/sock
</pre>
<dl>
<dt>
<dd>
<dl>
<dt>Available Commands</p>
<dd>
<dt>Key<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Socket*<tt>&nbsp;<wbr></tt>Effect</p>
<dd>
<dt><i>RET</i></p>
<dd> draw<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>redraws the image, applying filters.</p>
<dt><i>u</i></p>
<dd> undo<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>goes to image before draw</p>
<dt><i>SPACE</i></p>
<dd> pause<tt>&nbsp;<wbr>&nbsp;<wbr></tt>pause the preview (and transcode)</p>
<dt><i>UP</i></p>
<dd> fastfw<tt>&nbsp;<wbr></tt>in pause mode, step forward 5 frames</p>
<dt><i>RIGHT</i></p>
<dd> slowfw<tt>&nbsp;<wbr></tt>in pause mode, step forward 1 frame</p>
<dt><i>DOWN</i></p>
<dd> fastbw<tt>&nbsp;<wbr></tt>in pause mode, step back 5 frames</p>
<dt><i>LEFT</i></p>
<dd> slowbw<tt>&nbsp;<wbr></tt>in pause mode, step back 1 frame</p>
<dt><i>q</i></p>
<dd> display<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>toggle display of frames</p>
<dt><i>s</i></p>
<dd> slower<tt>&nbsp;<wbr></tt>slow down</p>
<dt><i>f</i></p>
<dd> faster<tt>&nbsp;<wbr></tt>speed up</p>
<dt><i>y</i></p>
<dd> toggle<tt>&nbsp;<wbr></tt>toggle displaying only every 5 frames</p>
<dt><i>j</i></p>
<dd> grab<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>save a JPEG</p>
<dt><i>r</i></p>
<dd> rotate<tt>&nbsp;<wbr></tt>rotate AVI file after next keyframe</p>
<dt></dl>
</dl>
<dd> (*) all commands must be prefixed with &quot;preview &quot;.</dl>
</dl>
<dt><code>resample</code> &#8211; <code>audio resampling filter plugin</code></p>
<dd> <code>resample</code> was written by Thomas Oestreich. The version documented here is v0.1.4 (2003-08-22). This is a audio filter. It is a pre-processing only filter.</p>
<dt><code>skip</code> &#8211; <code>skip all listed frames</code></p>
<dd> <code>skip</code> was written by Thomas Oestreich. The version documented here is v0.0.1 (2001-11-27). This is a video and audio filter. It is a pre-processing only filter.</p>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; <i>fstart1-fend1 [ fstart2-fend2 [ .. ] ]</i> = <i>%s</i></p>
<dl>
<dt>
<dd> apply filter [start-end] frames</dl>
</dl>
<dt><code>slowmo</code> &#8211; <code>very cheap slow-motion effect</code></p>
<dd> <code>slowmo</code> was written by Tilmann Bitterberg. The version documented here is v0.3 (2003-29-11). This is a video filter. It can handle RGB and YUV mode. It is a pre-processing only filter.</p>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> This filter produces a simple slow-motion effect by duplicating certain frames. I have seen this effect on TV and despite its the simple algorithm it works quite well. The filter has no options.</dl>
</dl>
<dt><code>smartbob</code> &#8211; <code>Motion-adaptive deinterlacing for double-frame-rate output.</code></p>
<dd> <code>smartbob</code> was written by Donald Graft, Tilmann Bitterberg. The version documented here is v1.1beta2 (2003-06-23). This is a video filter. It can handle RGB and YUV mode. It is a post-processing only filter.</p>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; <i>motionOnly</i> = <i>%d</i> [default <i>0</i>]</p>
<dl>
<dt>
<dd> Show motion areas only</dl>
<p> &bull; <i>shiftEven</i> = <i>%d</i> [default <i>0</i>]</p>
<dl>
<dt>
<dd> Blend instead of interpolate in motion areas</dl>
<p> &bull; <i>threshold</i> = <i>%d</i> [default <i>12</i>]</p>
<dl>
<dt>
<dd> Motion Threshold</dl>
<p> &bull; <i>denoise</i> = <i>%d</i> [default <i>1</i>]</p>
<dl>
<dt>
<dd> Phase shift</dl>
<dl>
<dt>
<dd> This filter only makes sense when fed by -J doublefps. It will take the field-frames which filter_doublefps produces and generates full-sized motion adaptive deinterlaced output at the double import framerate.</dl>
</dl>
<dt><code>smartdeinter</code> &#8211; <code>VirtualDub&#8217;s smart deinterlacer</code></p>
<dd> <code>smartdeinter</code> was written by Donald Graft. The version documented here is v2.7b (2003-02-01). This is a video filter. It can handle RGB and YUV mode. It is a pre-processing only filter.</p>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; <i>motionOnly</i> = <i>%d</i> [default <i>0</i>]</p>
<dl>
<dt>
<dd> Show motion areas only</dl>
<p> &bull; <i>Blend</i> = <i>%d</i> [default <i>0</i>]</p>
<dl>
<dt>
<dd> Blend instead of interpolate in motion areas</dl>
<p> &bull; <i>threshold</i> = <i>%d</i> [default <i>15</i>]</p>
<dl>
<dt>
<dd> Motion Threshold</dl>
<p> &bull; <i>scenethreshold</i> = <i>%d</i> [default <i>100</i>]</p>
<dl>
<dt>
<dd> Scene Change Threshold</dl>
<p> &bull; <i>fieldShift</i> = <i>%d</i> [default <i>0</i>]</p>
<dl>
<dt>
<dd> Phase shift</dl>
<p> &bull; <i>inswap</i> = <i>%d</i> [default <i>0</i>]</p>
<dl>
<dt>
<dd> Field swap before phase shift</dl>
<p> &bull; <i>outswap</i> = <i>%d</i> [default <i>0</i>]</p>
<dl>
<dt>
<dd> Field swap after phase shift</dl>
<p> &bull; <i>noMotion</i> = <i>%d</i> [default <i>0</i>]</p>
<dl>
<dt>
<dd> Disable motion processing</dl>
<p> &bull; <i>highq</i> = <i>%d</i> [default <i>0</i>]</p>
<dl>
<dt>
<dd> Motion map denoising for field-only</dl>
<p> &bull; <i>diffmode</i> = <i>%d</i> [default <i>0</i>]</p>
<dl>
<dt>
<dd> Motion Detection (0=frame, 1=field, 2=both)</dl>
<p> &bull; <i>colordiff</i> = <i>%d</i> [default <i>1</i>]</p>
<dl>
<dt>
<dd> Compare color channels instead of luma</dl>
<p> &bull; <i>cubic</i> = <i>%d</i> [default <i>0</i>]</p>
<dl>
<dt>
<dd> Use cubic for interpolation</dl>
<dl>
<dt>
<dd> This filter provides a smart, motion-based deinterlacing capability. In static picture areas, interlacing artifacts do not appear, so data from both fields is used to provide full detail. In moving areas, deinterlacing is performed</dl>
</dl>
<dt><code>smartyuv</code> &#8211; <code>Motion-adaptive deinterlacing</code></p>
<dd> <code>smartyuv</code> was written by Tilmann Bitterberg. The version documented here is 0.1.4 (2003-10-13). This is a video filter. It can handle YUV mode only. It is a pre-processing only filter.</p>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; <i>motionOnly</i> = <i>%d</i> [default <i>0</i>]</p>
<dl>
<dt>
<dd> Show motion areas only, blacking out static areas</dl>
<p> &bull; <i>diffmode</i> = <i>%d</i> [default <i>0</i>]</p>
<dl>
<dt>
<dd> Motion Detection (0=frame, 1=field, 2=both)</dl>
<p> &bull; <i>threshold</i> = <i>%d</i> [default <i>14</i>]</p>
<dl>
<dt>
<dd> Motion Threshold (luma)</dl>
<p> &bull; <i>chromathres</i> = <i>%d</i> [default <i>7</i>]</p>
<dl>
<dt>
<dd> Motion Threshold (chroma)</dl>
<p> &bull; <i>scenethres</i> = <i>%d</i> [default <i>31</i>]</p>
<dl>
<dt>
<dd> Threshold for detecting scenechanges</dl>
<p> &bull; <i>highq</i> = <i>%d</i> [default <i>1</i>]</p>
<dl>
<dt>
<dd> High-Quality processing (motion Map denoising)</dl>
<p> &bull; <i>cubic</i> = <i>%d</i> [default <i>1</i>]</p>
<dl>
<dt>
<dd> Do cubic interpolation</dl>
<p> &bull; <i>Blend</i> = <i>%d</i> [default <i>1</i>]</p>
<dl>
<dt>
<dd> Blend the frames for deinterlacing</dl>
<p> &bull; <i>doChroma</i> = <i>%d</i> [default <i>1</i>]</p>
<dl>
<dt>
<dd> Enable chroma processing (slower but more accurate)</dl>
<p> &bull; <i>verbose</i> = <i>%d</i> [default <i>0</i>]</p>
<dl>
<dt>
<dd> Verbose mode</dl>
<dl>
<dt>
<dd> This filter is basically a rewrite of the smartdeinter filter by Donald Graft (without advanced processing options) for YUV mode only. Its faster than using the smartdeinter in YUV mode and is also tuned with its threshold settings for YUV mode. The filter detects motion and static areas in an image and only deinterlaces (either by blending or by cubic interpolation) the moving areas. The result is an image with high detail in static areas, no information is lost there. </p>
<p> The threshold settings should be sufficent for most users. As a rule of thumb, I recommend setting the chroma threshold to about the half of the luma threshold. If you want more deinterlacing, lower the thresholds. The scene threshold can be easily found by turning on verbose mode and the preview filter. In verbose mode, the filter will print out, when it detects a scene change. If scenechanges go by unnoticed, lower the scene threshold. You can completly disable chroma processing with the doChroma=0 option. Here is a sample commandline </p>
<p> -J smartyuv=highq=1:diffmode=2:cubic=1:Blend=1:chromathres=4:threshold=8:doChroma=1</dl>
</dl>
<dt><code>smooth</code> &#8211; <code>(single-frame) smoothing plugin</code></p>
<dd> <code>smooth</code> was written by Chad Page. The version documented here is v0.2.3 (2003-03-27). This is a video filter. It can handle YUV mode only. It is a pre-processing only filter. It supports multiple instances.</p>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; <i>strength</i> = <i>%f</i> [default <i>0.25</i>]</p>
<dl>
<dt>
<dd> Blending factor</dl>
<p> &bull; <i>cdiff</i> = <i>%d</i> [default <i>6</i>]</p>
<dl>
<dt>
<dd> Max difference in chroma values</dl>
<p> &bull; <i>ldiff</i> = <i>%d</i> [default <i>8</i>]</p>
<dl>
<dt>
<dd> Max difference in luma value</dl>
<p> &bull; <i>range</i> = <i>%d</i> [default <i>4</i>]</p>
<dl>
<dt>
<dd> Search Range</dl>
<dl>
<dt>
<dd> &quot;single-frame&quot; means it only works with the current frame, it does not need the next or the previous frame for operation. Usually smoothing is done by talking the data of previous frames into account to see which parts of the picture can be &quot;safely&quot; smoothed, this filter only needs one frame.</dl>
</dl>
<dt>
<dd> Usage -J subtitler=&quot;[no_objects] [subtitle_file=s] [color_depth=n] [font_dir=s] [font=n] [font_factor=f [frame_offset=n] [debug] [help]&quot; f is float, h is hex, n is integer, s is string. </p>
<p> no_objects disables subtitles and other objects (off).<br />
 color_depth= 32 or 24 (overrides X auto) (32).<br />
 font= 0 or 1, 1 gives strange symbols&#8230; (0).<br />
 font_dir= place where font.desc is (~/.subtitles/font).<br />
 font_factor= .1 to 100 outline characters (10.75).<br />
 frame_offset= positive (text later) or negative (earlier) integer (0).<br />
 subtitle_file= pathfilename.ppml location of ppml file (~/.subtitles/demo.ppml).<br />
 debug prints debug messages (off).<br />
 help prints this list and exit.</p>
<dt><code>testframe</code> &#8211; <code>generate stream of testframes</code></p>
<dd> <code>testframe</code> was written by Thomas Oestreich. The version documented here is v0.1.3 (2003-09-04). This is a video filter. It can handle RGB and YUV mode. It is a pre-processing only filter.</p>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; <i>mode</i> = <i>%d</i> [default <i>0</i>]</p>
<dl>
<dt>
<dd> Choose the test pattern (0-4 interlaced, 5 colorfull)</dl>
</dl>
<dt><code>text</code> &#8211; <code>write text in the image</code></p>
<dd> <code>text</code> was written by Tilmann Bitterberg. The version documented here is v0.1.4 (2004-02-14). This is a video filter. It can handle RGB and YUV mode. It is a post-processing only filter.</p>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; <i>range</i> = <i>%u-%u/%d</i> [default <i>0-4294967295/1</i>]</p>
<dl>
<dt>
<dd> apply filter to [start-end]/step frames</dl>
<p> &bull; <i>string</i> = <i>%s</i></p>
<dl>
<dt>
<dd> text to display (no &#8216;:&#8217;) [defaults to `date`]</dl>
<p> &bull; <i>font</i> = <i>%s</i></p>
<dl>
<dt>
<dd> full path to font file [defaults to arial.ttf]</dl>
<p> &bull; <i>points</i> = <i>%d</i> [default <i>25</i>]</p>
<dl>
<dt>
<dd> size of font (in points)</dl>
<p> &bull; <i>dpi</i> = <i>%d</i> [default <i>96</i>]</p>
<dl>
<dt>
<dd> resolution of font (in dpi)</dl>
<p> &bull; <i>fade</i> = <i>%d</i> [default <i>0</i>]</p>
<dl>
<dt>
<dd> fade in/out (0=off, 1=slow, 10=fast)</dl>
<p> &bull; <i>antialias</i> = <i>%d</i> [default <i>1</i>]</p>
<dl>
<dt>
<dd> Anti-Alias text (0=off 1=on)</dl>
<p> &bull; <i>pos</i> = <i>%dx%d</i> [default <i>0x0</i>]</p>
<dl>
<dt>
<dd> Position (0-width x 0-height)</dl>
<p> &bull; <i>posdef</i> = <i>%d</i> [default <i>0</i>]</p>
<dl>
<dt>
<dd> Position (0=None 1=TopL 2=TopR 3=BotL 4=BotR 5=Cent 6=BotCent)</dl>
<p> &bull; <i>notransparent</i> (bool)</p>
<dl>
<dt>
<dd> disable transparency (enables block box)</dl>
<dl>
<dt>
<dd> see /docs/filter_text.txt</dl>
</dl>
<dt><code>tomsmocomp</code> &#8211; <code>Tom&#8217;s MoComp deinterlacing filter</code></p>
<dd> <code>tomsmocomp</code> was written by Tom Barry et al.. The version documented here is v0.1 (2004-07-31). This is a video filter. It can handle YUV and YUV422 mode. It is a pre-processing only filter.</p>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; <i>TopFirst</i> = <i>%d</i> [default <i>1</i>]</p>
<dl>
<dt>
<dd> Assume the top field should be displayed first</dl>
<p> &bull; <i>SearchEffort</i> = <i>%d</i> [default <i>15</i>]</p>
<dl>
<dt>
<dd> CPU time used to find moved pixels</dl>
<p> &bull; <i>UseStrangeBob</i> = <i>%d</i> [default <i>0</i>]</p>
<dl>
<dt>
<dd> ?Unknown?</dl>
<p> &bull; <i>CpuFlags</i> = <i>%x</i> [default <i>5f</i>]</p>
<dl>
<dt>
<dd> Manual specification of CPU capabilities</dl>
</dl>
<dt><code>unsharp</code> &#8211; <code>unsharp mask &amp; gaussian blur</code></p>
<dd> <code>unsharp</code> was written by Remi Guyomarch. The version documented here is v1.0.1 (2003-10-27). This is a video filter. It can handle YUV mode only. It is a post-processing only filter.</p>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; <i>amount</i> = <i>%f</i> [default <i>0.0</i>]</p>
<dl>
<dt>
<dd> Luma and chroma (un)sharpness amount</dl>
<p> &bull; <i>matrix</i> = <i>%dx%d</i> [default <i>0x0</i>]</p>
<dl>
<dt>
<dd> Luma and chroma search matrix size</dl>
<p> &bull; <i>luma</i> = <i>%f</i> [default <i>0.0</i>]</p>
<dl>
<dt>
<dd> Luma (un)sharpness amount</dl>
<p> &bull; <i>chroma</i> = <i>%f</i> [default <i>0.0</i>]</p>
<dl>
<dt>
<dd> Chroma (un)sharpness amount</dl>
<p> &bull; <i>luma_matrix</i> = <i>%dx%d</i> [default <i>0x0</i>]</p>
<dl>
<dt>
<dd> Luma search matrix size</dl>
<p> &bull; <i>chroma_matrix</i> = <i>%dx%d</i> [default <i>0x0</i>]</p>
<dl>
<dt>
<dd> Chroma search matrix size</dl>
<p> &bull; <i>pre</i> = <i>%d</i> [default <i>0</i>]</p>
<dl>
<dt>
<dd> run as a pre filter</dl>
<dl>
<dt>
<dd> This filter blurs or sharpens an image depending on the sign of &quot;amount&quot;. You can either set amount for both luma and chroma or you can set it individually (recommended). A positive value for amount will sharpen the image, a negative value will blur it. A sane range for amount is -1.5 to 1.5. </p>
<p> The matrix sizes must be odd and define the range/strength of the effect. Sensible ranges are 3&#215;3 to 7&#215;7. </p>
<p> It sometimes makes sense to sharpen the sharpen the luma and to blur the chroma. Sample string is: </p>
<p> luma=0.8:luma_matrix=7&#215;5:chroma=-0.2:chroma_matrix=3&#215;3</dl>
</dl>
<dt><code>whitebalance</code> &#8211; <code>White Balance Filter &#8211; correct images with a broken white balance</code></p>
<dd> <code>whitebalance</code> was written by Guillaume Cottenceau. The version documented here is v0.1 (2003-10-01). This is a video filter. It can handle RGB and YUV mode. It is a pre-processing only filter.</p>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; <i>level</i> = <i>%d</i> [default <i>40</i>]</p>
<dl>
<dt>
<dd> Level of blue-to-yellow white balance shifting (can be negative)</dl>
<p> &bull; <i>limit</i> = <i>%s</i></p>
<dl>
<dt>
<dd> Limit to specified ranges (+fnumber toggles on, -fnumber toggles off)</dl>
<dl>
<dt>
<dd> This filter allows correcting movies with a broken white balance, e.g. bluish movies.</dl>
</dl>
<dt><code>xharpen</code> &#8211; <code>VirtualDub&#8217;s XSharpen Filter</code></p>
<dd> <code>xharpen</code> was written by Donald Graft, Tilmann Bitterberg. The version documented here is (1.0b2) (2003-02-12). This is a video filter. It can handle RGB and YUV mode. It is a post-processing only filter.</p>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; <i>strength</i> = <i>%d</i> [default <i>200</i>]</p>
<dl>
<dt>
<dd> How much of the effect</dl>
<p> &bull; <i>threshold</i> = <i>%d</i> [default <i>255</i>]</p>
<dl>
<dt>
<dd> How close a pixel must be to the brightest or dimmest pixel to be mapped</dl>
<dl>
<dt>
<dd> This filter performs a subtle but useful sharpening effect. The result is a sharpening effect that not only avoids amplifying noise, but also tends to reduce it. A welcome side effect is that files processed with this filter tend to compress to smaller files. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Strength&nbsp;<wbr>&#8216;strength&#8217;&nbsp;<wbr>(0-255)&nbsp;<wbr>[200]<br />
&nbsp;<wbr>When this value is 255, mapped pixels are not blended with the original pixel values, so a full-strength effect is obtained. As the value is reduced, each mapped pixel is blended with more of the original pixel. At a value of 0, the original pixels are passed through and there is no sharpening effect. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Threshold&nbsp;<wbr>&#8216;threshold&#8217;&nbsp;<wbr>(0-255)&nbsp;<wbr>[255]<br />
&nbsp;<wbr>This value determines how close a pixel must be to the brightest or dimmest pixel to be mapped. If a pixel is more than threshold away from the brightest or dimmest pixel, it is not mapped.&nbsp;<wbr>&nbsp;<wbr>Thus, as the threshold is reduced, pixels in the mid range start to be spared.</dl>
</dl>
<dt><code>yuvdenoise</code> &#8211; <code>mjpegs YUV denoiser</code></p>
<dd> <code>yuvdenoise</code> was written by Stefan Fendt, Tilmann Bitterberg. The version documented here is v0.2.1 (2003-11-26). This is a video filter. It can handle YUV mode only. It can be used as a pre-processing or as a post-processing filter.</p>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; <i>radius</i> = <i>%d</i> [default <i>8</i>]</p>
<dl>
<dt>
<dd> Search radius</dl>
<p> &bull; <i>threshold</i> = <i>%d</i> [default <i>5</i>]</p>
<dl>
<dt>
<dd> Denoiser threshold</dl>
<p> &bull; <i>pp_threshold</i> = <i>%d</i> [default <i>4</i>]</p>
<dl>
<dt>
<dd> Pass II threshold</dl>
<p> &bull; <i>delay</i> = <i>%d</i> [default <i>3</i>]</p>
<dl>
<dt>
<dd> Average &#8216;n&#8217; frames for a time-lowpassed pixel</dl>
<p> &bull; <i>postprocess</i> = <i>%d</i> [default <i>1</i>]</p>
<dl>
<dt>
<dd> Filter internal postprocessing</dl>
<p> &bull; <i>luma_contrast</i> = <i>%d</i> [default <i>100</i>]</p>
<dl>
<dt>
<dd> Luminance contrast in percent</dl>
<p> &bull; <i>chroma_contrast</i> = <i>%d</i> [default <i>100</i>]</p>
<dl>
<dt>
<dd> Chrominance contrast in percent.</dl>
<p> &bull; <i>sharpen</i> = <i>%d</i> [default <i>125</i>]</p>
<dl>
<dt>
<dd> Sharpness in percent</dl>
<p> &bull; <i>deinterlace</i> = <i>%d</i> [default <i>0</i>]</p>
<dl>
<dt>
<dd> Force deinterlacing</dl>
<p> &bull; <i>mode</i> = <i>%d</i> [default <i>0</i>]</p>
<dl>
<dt>
<dd> [0]: Progressive [1]: Interlaced [2]: Fast</dl>
<p> &bull; <i>scene_thres</i> = <i>%d%%</i> [default <i>50</i>]</p>
<dl>
<dt>
<dd> Blocks where motion estimation should fail before scenechange</dl>
<p> &bull; <i>block_thres</i> = <i>%d</i> [default <i>1024</i>]</p>
<dl>
<dt>
<dd> Every SAD value greater than this will be considered bad</dl>
<p> &bull; <i>do_reset</i> = <i>%d</i> [default <i>2</i>]</p>
<dl>
<dt>
<dd> Reset the filter for `n&#8217; frames after a scene</dl>
<p> &bull; <i>increment_cr</i> = <i>%d</i> [default <i>2</i>]</p>
<dl>
<dt>
<dd> Increment Cr with constant</dl>
<p> &bull; <i>increment_cb</i> = <i>%d</i> [default <i>2</i>]</p>
<dl>
<dt>
<dd> Increment Cb with constant</dl>
<p> &bull; <i>border</i> = <i>%dx%d-%dx%d</i> [default <i>0x0-32&#215;32</i>]</p>
<dl>
<dt>
<dd> Active image area</dl>
<p> &bull; <i>pre</i> = <i>%d</i> [default <i>0</i>]</p>
<dl>
<dt>
<dd> run this filter as a pre-processing filter</dl>
<dl>
<dt>
<dd> see /docs/filter_yuvdenoise.txt</dl>
</dl>
<dt><code>yuvmedian</code> &#8211; <code>mjpegs YUV median filter</code></p>
<dd> <code>yuvmedian</code> was written by Mike Bernson, Tilmann Bitterberg. The version documented here is v0.1.0 (2003-01-24). This is a video filter. It can handle YUV mode only. It can be used as a pre-processing or as a post-processing filter.</p>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; <i>radius_luma</i> = <i>%d</i> [default <i>2</i>]</p>
<dl>
<dt>
<dd> Radius for median (luma)</dl>
<p> &bull; <i>radius_chroma</i> = <i>%d</i> [default <i>2</i>]</p>
<dl>
<dt>
<dd> Radius for median (chroma)</dl>
<p> &bull; <i>threshold_luma</i> = <i>%d</i> [default <i>2</i>]</p>
<dl>
<dt>
<dd> Trigger threshold (luma)</dl>
<p> &bull; <i>threshold_chroma</i> = <i>%d</i> [default <i>2</i>]</p>
<dl>
<dt>
<dd> Trigger threshold (chroma)</dl>
<p> &bull; <i>interlace</i> = <i>%d</i> [default <i>0</i>]</p>
<dl>
<dt>
<dd> Treat input as interlaced</dl>
<p> &bull; <i>pre</i> = <i>%d</i> [default <i>1</i>]</p>
<dl>
<dt>
<dd> Run as a PRE filter</dl>
</dl>
</dl>
<h2>AUTHORS</h2>
<p> <code>transcode</code> was written by Thomas Oestreich<br />
 &lt;ostreich [at] theorie.physik.uni-goettingen.de&gt; with contributions from many others. See AUTHORS for details. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-transcode/">transcode</a></code>(1), <code><a href="/docs/linux/man/1-transcode_import/">transcode_import</a></code>(1), <code><a href="/docs/linux/man/1-transcode_export/">transcode_export</a></code>(1), <code><a href="/docs/linux/man/1-tcmodinfo/">tcmodinfo</a></code>(1), </p>
<h2>Index</h2>
