---
title: "yuvinactive(1)"
name: "yuvinactive"
section: "1"
letter: "y"
url: "/docs/linux/man/1-yuvinactive/"
description: "yuvinactive – Set a part of the video to a defined state"
---

<h2>NAME</h2>
<p> yuvinactive &#8211; Set a part of the video to a defined state </p>
<h2>SYNOPSIS</h2>
<p> <code>yuvinactive</code> [<i>options</i>] <i>&lt;/dev/stdin &gt;/dev/stdout</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>yuvinactive</code> operates with a area (rectangle) you define. By default is sets it to really black. But you can tell tell yuvinactive to darken the area, or fill it with a certain color. It can also make the content of the area unreadable, like extreme softening of the area. Or copy the surrounding area into the the specified area. You usually have to use the -i option which sets the area in which yuvinactive will work. If no additional option is given yuvinactive stet the area to black. But you can use the <code>-d -s -a -c options</code> to tell yuvinactive that it shall do something different with that area. You can only use one additional option. yuvinactive was built to remove unwanted things like a logo, from the movie. </p>
<h2>OPTIONS</h2>
<p> <code>lav2yuv</code> accepts the following options: </p>
<dl>
<dt><code>-h</code></p>
<dd> Some help output</p>
<dt><code>-i</code><i>XxY+XOFF+YOFF</i></p>
<dd> Specifies the area yuvinactive shall work with. With this option the area is set to black. There are no restrictions because of interlacing.</p>
<dt><code>-d</code><i> num</i></p>
<dd> How much darker the area should be compared to the original color. This is done by setting a lower value for the luma. The value is in percent from the original luma.</p>
<dt><code>-s</code><i> num</i></p>
<dd> Here you specify a certain color in the yuv format.</p>
<dt><code>-a</code><i> num</i></p>
<dd> With this option the program uses on pixel and averages the surrounding pixels with the same color to make the original less readable. The number tells the the program how much pixels around the original pixel should be overwritten with the same color. You have to use a even number here</p>
<dt><code>-c</code><i> num</i></p>
<dd> Sets the number of surrounding pixels yuvinactive should use to copy them into the given area. You have to use a even number here. yuvinactive uses the lines above and below the specified area for copying them into the area. </p>
</dl>
<h2>BUGS</h2>
<p> Right, there are bugs hidden. The thing is not well tested, and not every option might work. yuvinactive is in the first state of becoming a useful program. </p>
<h2>AUTHOR</h2>
<p> This man page was originally written by Bernhard Praschinger.<br />
 If you have questions, remarks, problems or you just want to contact the developers, the main mailing list for the MJPEG-tools is:<br />
&nbsp;<wbr>&nbsp;<wbr><i>mjpeg-users [at] lists.sourceforge.net</i> </p>
<dl>
<dt>For more info, see our website at</p>
<dd> <i><a rel="nofollow" href="http://mjpeg.sourceforge.net">http://mjpeg.sourceforge.net</a></i> </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mjpegtools/">mjpegtools</a></code>(1), <code><a href="/docs/linux/man/1-lav2yuv/">lav2yuv</a></code>(1), <code><a href="/docs/linux/man/1-mpeg2enc/">mpeg2enc</a></code>(1), <code><a href="/docs/linux/man/1-yuvscaler/">yuvscaler</a></code>(1), <code><a href="/docs/linux/man/1-yuv2lav/">yuv2lav</a></code>(1), <code><a href="/docs/linux/man/1-yuvdenoise/">yuvdenoise</a></code>(1), <code><a href="/docs/linux/man/1-yuvplay/">yuvplay</a></code>(1), <code><a href="/docs/linux/man/1-yuvmedianfilter/">yuvmedianfilter</a></code>(1) </p>
<h2>Index</h2>
