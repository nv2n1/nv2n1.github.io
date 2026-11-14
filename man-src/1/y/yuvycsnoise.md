---
title: "yuvycsnoise(1)"
name: "yuvycsnoise"
section: "1"
letter: "y"
url: "/docs/linux/man/1-yuvycsnoise/"
description: "yuvycsnoise – Noise filter specialized for NTSC Y/C separation noise"
---

<h2 class="name">NAME</h2>
<p> yuvycsnoise &#8211; Noise filter specialized for NTSC Y/C separation noise</p>
<h2>SYNOPSIS</h2>
<p> <code>yuvycsnoise</code> [<code>-t</code>] [<code>-m t</code>|<code>b</code>|<code>i</code>|<code>c</code>] [<code>-S</code> <i>MIN</i>] [<code>-T</code> <i>ERRT</i>[<code>,</code><i>MAXT</i>]] [<code>-B</code> <i>ERRB</i>[<code>,</code><i>MAXB</i>]] [<code>-I</code> <i>ERRI</i>[<code>,</code><i>MAXI</i>]] [<code>-C</code> <i>ERRC</i>[<code>,</code><i>MAXC</i>]] </p>
<h2>DESCRIPTION</h2>
<p> If video capture hardware has only a poor Y/C separator, at vertical stripe (especially red/blue), noises appear which seem checker flag and bright/dark invert per 1 frame. <code>yuvycsnoise</code> reduces noises of this type. </p>
<h2>OPTIONS</h2>
<p> <code>yuvycsnoise</code> accepts the following options:</p>
<dl>
<dt><code>-t</code></p>
<dd> test. Instead of noise reduction, noises will be marked as black pixel.</p>
<dt><code>-m</code><i>&nbsp;<wbr>METHOD</i></p>
<dd> (default: <code>tbic</code>).<br />
 Select method. <i>METHOD</i> is string in which each character mean method.<br />
&nbsp;<wbr><code>t</code>:&nbsp;<wbr>&#8216;triframe&#8217;&nbsp;<wbr>method of luma noise reduction.<br />
&nbsp;<wbr><code>b</code>:&nbsp;<wbr>&#8216;biframe&#8217;&nbsp;<wbr>method of luma noise reduction.<br />
&nbsp;<wbr><code>i</code>:&nbsp;<wbr>&#8216;infield&#8217;&nbsp;<wbr>method of luma noise reduction.<br />
&nbsp;<wbr><code>c</code>: chroma noise reduction. use 3 frames as&nbsp;<wbr>&#8216;triframe&#8217;.</p>
<dt><code>-S</code><i>&nbsp;<wbr>MIN</i></p>
<dd> (default: 4).<br />
 Set minimum threshold of luma/chroma difference which is treated as noise.</p>
<dt><code>-T</code><i>&nbsp;<wbr>ERRT</i>[,<i>MAXT</i>]</p>
<dd> (default: 32,255).</p>
<dt><code>-B</code><i>&nbsp;<wbr>ERRB</i>[,<i>MAXB</i>]</p>
<dd> (default: 32,255).</p>
<dt><code>-I</code><i>&nbsp;<wbr>ERRI</i>[,<i>MAXI</i>]</p>
<dd> (default: 16,255).</p>
<dt><code>-C</code><i>&nbsp;<wbr>ERRC</i>[,<i>MAXC</i>]</p>
<dd> (default: 12,255).<br />
 Set threshold of luma/chroma difference of each methods. <i>ERRx</i> is maximum error of luma/chroma of pixels around target pixel, which should be same if target contain noise. <i>MAXx</i> is maximum threshold of luma/chroma difference of target pixel from luma/chroma after noise reduced. </p>
</dl>
<h2>AUTHOR</h2>
<p> <code>yuvycsnoise</code> was written by Kawamata/Hitoshi.<br />
 If you have questions, remarks, problems or you just want to contact the developers, the main mailing list for the MJPEG-tools is:<br />
&nbsp;<wbr>&nbsp;<wbr><i>mjpeg-users [at] lists.sourceforge.net</i> </p>
<dl>
<dt>For more info, see our website at</p>
<dd> <i><a rel="nofollow" href="http://mjpeg.sourceforge.net/">http://mjpeg.sourceforge.net/</a></i> </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mjpegtools/">mjpegtools</a></code>(1) </p>
<h2>Index</h2>
