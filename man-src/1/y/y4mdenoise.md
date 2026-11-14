---
title: "y4mdenoise(1)"
name: "y4mdenoise"
section: "1"
letter: "y"
url: "/docs/linux/man/1-y4mdenoise/"
description: "y4mdenoise – Motion-compensating YUV4MPEG-frame denoiser"
---

<h2 class="name">NAME</h2>
<p> y4mdenoise &#8211; Motion-compensating YUV4MPEG-frame denoiser</p>
<h2>SYNOPSIS</h2>
<p> <code>y4mdenoise</code> [<code>-v</code> <i>verbosity</i>] [<code>-p</code> <i>parallelism</i>] [<code>-r</code> <i>motion-search_radius</i>] [<code>-R</code> <i>color_motion-search_radius</i>] [<code>-t</code> <i>error_tolerance</i>] [<code>-T</code> <i>color_error_tolerance</i>] [<code>-z</code> <i>zero_motion_error_tolerance</i>] [<code>-Z</code> <i>color_zero_motion_error_tolerance</i>] [<code>-m</code> <i>match-count_throttle</i>] [<code>-M</code> <i>match-size_throttle</i>] [<code>-f</code> <i>reference_frames</i>] [<code>-B</code>] [<code>-I</code> <i>interlacing_type</i>] &lt; /dev/stdin &gt; /dev/stdout </p>
<h2>DESCRIPTION</h2>
<p> <code>y4mdenoise</code> can be used to remove noise from images in a YUV4MPEG2 stream. This is useful for cleaning old sources to increase video quality, and to reduce the bitrate needed to encode your video (e.g. for VCD and SVCD creation). </p>
<h2>HOW IT WORKS</h2>
<p> It maintains a list of the last several frames, called reference frames. Each reference frame is composed of reference pixels. Every time a pixel in one frame is proven to be a moved instance of a pixel in another frame, the reference-pixel incorporates its value, and produces an average value for all instances of the pixel. The oldest reference frame, therefore, gets a pretty good idea of the real value of every pixel, but of course output is delayed by the number of reference frames. </p>
<p> The search is not actually done one pixel at a time; it&#8217;s done in terms of pixel groups. An entire pixel-group has to match for any match to be found, but all possible pixel-groups are tested (i.e. all possible overlapping combinations are checked). Using pixel-groups helps to establish a minimum standard for what may be considered a match, in order to avoid finding lots of really small (and really useless) matches. Presently, intensity pixel-groups are 4&#215;2 (i.e. 4 across and 2 down), and color pixel-groups are 2&#215;2. </p>
<p> It compares every pixel-group in the current frame with all pixel-groups in the previous frame, within a given search-radius, and sorts them based on how close the match was, keeping the top contenders. It then flood-fills each found pixel-group in turn, to determine the full size of the match. The first match found to be big enough is applied to the image. The number of contenders to consider, and the minimum size of a match, can be specified on the command line. </p>
<p> At the end of the frame, any new-frame pixels not resolved yet are considered to be new information, and a new reference-pixel is generated for each one. </p>
<p> A &quot;zero-motion pass&quot; happens each frame, before motion-detection, in an attempt to resolve most of the frame cheaply. Its error-tolerance can be set separately. </p>
<h2>OPTIONS</h2>
<p> <code>y4mdenoise</code> accepts the following options: </p>
<dl>
<dt><code>-v</code><i> [0..2] verbosity</i></p>
<dd> 0 = none, 1 = normal (per-frame pixel-detection totals), 2=debug. </p>
<dt><code>-p</code><i> num</i></p>
<dd> Controls the level of parallelism. Since intensity and color are denoised separately by design, it&#8217;s very easy to do each in parallel on a multiple-processor machine. The default value is 1; that reads and writes video frames in parallel with denoising. A value of 2 causes intensity and color to be denoised in parallel. A value of 3 does both types of concurrency. A value of 0 turns off all concurrency. </p>
<dt><code>-r</code><i> [4..] search radius</i></p>
<dd> The search radius, i.e. the maximum distance that a pixel can move and still be found by motion-detection. The default is 16. There are no particular restrictions on the search radius, e.g. it doesn&#8217;t have to be an even multiple of 4. </p>
<dt><code>-R</code><i> [4..] color search radius</i></p>
<dd> The search radius to use for color. Default is whatever the main search-radius was set to. Note that this value ends up getting scaled by the relative size of intensity &amp; color planes in your YUV4MPEG2 stream. </p>
<dt><code>-t</code><i> [0..255] Error tolerance</i></p>
<dd> The largest difference between two pixels that&#8217;s accepted for the two pixels to be considered equal. The default is 3, which is good for medium-noise material like analog cable TV. (This value will have to be changed to whatever is appropriate for your YUV4MPEG2 stream in order to avoid undesirable results. See the instructions below.) </p>
<dt><code>-T</code><i> [0..255] Error tolerance for color</i></p>
<dd> The default is whatever the main error-tolerance was set to. </p>
<dt><code>-z</code><i> [0..255] Error tolerance for zero-motion pass</i></p>
<dd> The error-tolerance used on pixels that haven&#8217;t moved. Usually equal to the main error-tolerance or one less than that. Default is 2. </p>
<dt><code>-Z</code><i> [0..255] Error tolerance for color&#8217;s zero-motion pass</i></p>
<dd> The default is whatever the main zero-motion error-tolerance was set to. </p>
<dt><code>-m</code><i> [num] Match-count throttle</i></p>
<dd> The maximum number of pixel-group matches (within the search radius) to consider. If more are found, only the closest matches are kept. Default is 15. </p>
<dt><code>-M</code><i> [num] Match-size throttle</i></p>
<dd> The minimum size of the flood-filled region generated from a match. Matches smaller than this are thrown away. Specified in terms of pixel-groups. Default is 3. </p>
<dt><code>-f</code><i> num</i></p>
<dd> The number of reference frames to keep. Pixel values are averaged over this many frames before they&#8217;re written to standard output; this also implies that output is delayed by this many frames. Default is 10. </p>
<dt><code>-B</code></p>
<dd> Black-and-white mode. Denoise only the intensity plane, and set the color plane to all white. </p>
<dt><code>-I</code><i> num</i></p>
<dd> Set interlacing type. Default is taken from the YUV4MPEG2 stream. 0 means not interlaced, 1 means top-field interlaced, 2 means bottom-field interlaced. This is useful when the signal is more naturally of some other interlacing type than its current representation (e.g. if the original was shot on film and then later it was transferred to interlaced video, it will denoise better if treated as film, i.e. non-interlaced). </p>
</dl>
<h2>TYPICAL USAGE AND TIPS</h2>
<p> Keep in mind that all of this advice was gained through experience. (Just because one writes a tool doesn&#8217;t mean one understands how it should be used, for the same reason that car designers aren&#8217;t necessarily professional drivers.) </p>
<p> The error-threshold must be determined for every individual YUV4MPEG2 stream. If the threshold is set too low, it&#8217;ll leave noise in the video, and the denoiser will run a lot slower than it has to. If it&#8217;s set too high, the denoiser will start to remove detail: the video will get blurrier, you may see topographical-like bands in the relatively flat areas of the video, and small parts of the video that should be moving will be stuck in place. It may also run a little slower. Additionally, just because the video came to you from a clean source (digital cable TV, LaserDisc, etc.) doesn&#8217;t mean the video itself is clean; <code>y4mdenoise</code> is capable of picking up on noise in the original recording as well as sampling error from the video-capture device. You will have to generate small clips of representative parts of your video, denoise them with various error thresholds, and see what looks the best. As you gain experience with the tool, you may know what error threshold generally works with various types of sources, but you&#8217;ll still want to double-check your assumptions. </p>
<p> Flat, shiny surfaces, like gloss-painted walls, or the polished wood floor of an indoor gymnasium, seem to require a lower error threshold than other types of video. </p>
<p> Here is the author&#8217;s experience: </p>
<p>&nbsp;<wbr>-t 1 : Digital cable TV, most LaserDiscs, DV camcorder video<br />
&nbsp;<wbr>-t 2 : VHS camcorder video, commercially-produced videotapes<br />
&nbsp;<wbr>-t 3 : Analog cable TV, VHS videotape&nbsp;<wbr>(at the 2-hour speed)<br />
&nbsp;<wbr>-t 4 : VHS videotape&nbsp;<wbr>(at the 6-hour speed) </p>
<p> Interlaced video that was made from non-interlaced video (e.g. a videotape or LaserDisc of a film) must be denoised as non-interlaced. Otherwise the result tends to be grainy. </p>
<p> <code>y4mdenoise</code> only removes temporal noise, i.e. noise that occurs over time. And it tends to do such a good job of this, that the spatial noise (i.e. noise that occurs in nearby areas of the same frame) tends to become very distinct. Therefore, always pipe the output of <code>y4mdenoise</code> through a spatial filter such as <code>y4mspatialfilter</code> or <code>yuvmedianfilter</code>. </p>
<p> When producing very low bitrate video (e.g. VCD-compatible video less than 900 kbps), denoise at the output frame size, e.g. don&#8217;t denoise at DVD frame size then downscale to VCD size. That will denoise as well as condition the video for the motion-detection part of <code>mpeg2enc</code>. Not doing this will produce video where the less complex scenes will look really good, but high-motion scenes will blur significantly. </p>
<p> JPEG compression of your video frames, even 100% compression, seems to be inaccurate enough to affect MPEG encoding. Therefore, if you&#8217;re using motion-JPEG files as your intermediary video format, you may want to use the denoiser in your MPEG-encoding pipeline, i.e. after <code>lav2yuv</code> and before <code>mpeg2enc</code>. If you&#8217;re generating multiple resolutions of the same video, e.g. DVD and VCD, experience shows that it&#8217;s acceptable to run <code>y4mdenoise</code> before <code>yuv2lav</code>, but you should still use the spatial-filter (e.g. <code>y4mspatialfilter</code>, <code>yuvmedianfilter</code>) in the MPEG-encoding pipeline, to try to smooth away JPEG encoding artifacts. </p>
<h2>AUTHOR</h2>
<p> The bulk of the <code>y4mdenoise</code> code, and this manual page, was written by Steven Boswell &lt;ulatec [at] users.sourceforge.net&gt;. </p>
<h2>FURTHER INFO</h2>
<p> If you have questions, remarks, problems or you just want to contact the developers, the main mailing list for the MJPEG-tools is: </p>
<p> <i>mjpeg-users [at] lists.sourceforge.net</i> </p>
<p> For more info, see our website at </p>
<p> <i><a rel="nofollow" href="http://mjpeg.sourceforge.net/">http://mjpeg.sourceforge.net/</a></i> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mjpegtools/">mjpegtools</a></code>(1), <code><a href="/docs/linux/man/1-mpeg2enc/">mpeg2enc</a></code>(1), <code><a href="/docs/linux/man/1-yuvdenoise/">yuvdenoise</a></code>(1), <code><a href="/docs/linux/man/1-yuvmedianfilter/">yuvmedianfilter</a></code>(1) </p>
<h2>Index</h2>
