---
title: "yuvdenoise(1)"
name: "yuvdenoise"
section: "1"
letter: "y"
url: "/docs/linux/man/1-yuvdenoise/"
description: "yuvdenoise – Motion-Compensating-YUV4MPEG2-frame-denoiser"
---

<h2 class="name">NAME</h2>
<p> yuvdenoise &#8211; Motion-Compensating-YUV4MPEG2-frame-denoiser</p>
<h2>SYNOPSIS</h2>
<p> <code>yuvdenoise</code> [<i>options</i>] &lt;/dev/stdin &gt;/dev/stdout </p>
<h2>DESCRIPTION</h2>
<p> <code>yuvdenoise</code> is a spatio-temporal noise-filter for YUV4MPEG2 streams. This is useful to reduce the bitrate needed to encode your captured movies for VCD and SVCD creation. </p>
<h2>OPTIONS</h2>
<p> <code>yuvdenoise</code> accepts the following options:</p>
<dl>
<dt><code>-g</code><i> y,u,v [0..255] Gaussian filter thresholds</i></p>
<dd> This sets the thresholds for the gaussian filter. A value of 0 disables filtering for a specific component and 0,0,0 completely disables/bypasses the filter. This filter is applied <code>before</code> the temporal (-t) filter.<br />
 (default=0,0,0) </p>
<dt><code>-m</code><i> y,u,v [0..255] Pre 3D Median filter thresholds</i></p>
<dd> This sets the thresholds for the pre-processing 3D median filter. A value of 0 disables median filtering for a specific component and 0,0,0 completely disables/bypasses the filter. This filter is applied <code>before</code> the temporal (-t) filter.<br />
 (default=0,0,0) </p>
<dt><code>-r</code><i> y,u,v [0..255] Renoising filter thresholds</i></p>
<dd> This sets the thresholds for adding random &quot;noise&quot; back into the video stream. Default is disabled (not adding random noise). This filter, if enabled, is run as the Blast filter (after the median and temporal filters). Reasonable value is 4,8,8 but if you are working with monochrome (black and white movie) then 4,0,0 will speed things up by not processing the chroma planes.<br />
 (default=0,0,0) </p>
<dt><code>-t</code><i> y,u,v [0..255] Temporal noise-filter thresholds</i></p>
<dd> This sets the thresholds for the temporal noise-filter. Values above 12 may introduce ghosting. The default value for Y&#8217; (y) is often a little high and reducing it to 4 or 5 may be necessary. If the chroma smears or ghosts try using values of 5 or 6 instead of the default (12). A value of 0 disables temporal filtering for the specified component (0,0,0 disables/bypasses all temporal filtering). Thus for black and white movies 4,0,0 will be faster by not denoising the chroma planes.<br />
 (default=4,8,8) </p>
<dt><code>-M</code><i> y,u,v [0..255] Post 3D Median filter thresholds</i></p>
<dd> This sets the thresholds for the post-processing 3D median filter. A value of 0 disables median filtering for a specific component and 0,0,0 completely disables/bypasses the filter. This filter is applied <code>after</code> the temporal (-t) filter. Reasonable value is 4,8,8 but if you are working with monochrome (black and white movie) then 4,0,0 will speed things up by not processing the chroma planes.<br />
 (default=0,0,0) </p>
</dl>
<h2>HOW IT WORKS</h2>
<p> To Be Written (maybe) in the future. </p>
<h2>TYPICAL USAGE AND TIPS</h2>
<p> As it is self-adapting to the noise-situation found in the stream you normally just can go without any options set: </p>
<p> lav2yuv my-video.avi | yuvdenoise | mpeg2enc -t 1 -o my-video.m1v </p>
<h2>AUTHOR</h2>
<p> This man page was written by Stefan Fendt &lt;stefan [at] lionfish.ping.de&gt; and revised by Steven Schultz. </p>
<h2>ADDITIONAL INFO</h2>
<p> If you have questions, remarks, problems or you just want to contact the developers, the main mailing list for the MJPEG-tools is: </p>
<p> <i>mjpeg-users [at] lists.sourceforge.net</i> </p>
<p> For more info, see our website at </p>
<p> <i><a rel="nofollow" href="http://mjpeg.sourceforge.net/">http://mjpeg.sourceforge.net/</a></i> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mjpegtools/">mjpegtools</a></code>(1), <code><a href="/docs/linux/man/1-mpeg2enc/">mpeg2enc</a></code>(1) <code><a href="/docs/linux/man/1-lavrec/">lavrec</a></code>(1) <code><a href="/docs/linux/man/1-lav2yuv/">lav2yuv</a></code>(1) </p>
<h2>Index</h2>
