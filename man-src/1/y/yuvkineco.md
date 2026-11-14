---
title: "yuvkineco(1)"
name: "yuvkineco"
section: "1"
letter: "y"
url: "/docs/linux/man/1-yuvkineco/"
description: "yuvkineco – revert 2-3 pulldown movie"
---

<h2 class="name">NAME</h2>
<p> yuvkineco &#8211; revert 2-3 pulldown movie</p>
<h2>SYNOPSIS</h2>
<p> <code>yuvkineco</code> [<i>options</i>] [<code>-C</code> <i>PATH</i>]<br />
 <code>yuvkineco</code> [<i>options</i>] <code>-O</code>|<code>N</code> <i>PATH</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>yuvkineco</code> reverts to original non-interlaced frames, from NTSC video which was film sourced and 2-3 pulled down. Input fps code must be 4(29.97fps), output fps code can be selected from 1(23.97fps) to 4(29.97fps). If 2, 3 or 4 selected, duplicated frames remain but they are reverted to non-interlaced. If input was non-interlaced only remove duplicate frames. Interlaced frame detection may fail in conditions like:<br />
&nbsp;<wbr>Pull down cycle changed&nbsp;<wbr>(video editing).<br />
&nbsp;<wbr>Low quality pull down.<br />
&nbsp;<wbr>Motionless scene.<br />
 If <code>-C</code> <i>PATH</i> was specified, <code>yuvkineco</code> outputs 2-3 pull down cycle list to the file. You can edit this file by hand and feed it to <code>yuvkineco</code> with <code>-O</code> or <code>-N</code> option to correct mistake of 1st <code>yuvkineco</code>. Try <code>-C</code> and see cycle list.<br />
&nbsp;<wbr>&nbsp;<wbr>EXAMPLE&nbsp;<wbr>#1: for 24p movie&nbsp;<wbr>/&nbsp;<wbr>automatically<br />
&nbsp;<wbr><code>lav2yuv 60i.eli |&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>yuvkineco -F 1 | yuv2lav -f a -I 0 -o 24p.avi</code><br />
&nbsp;<wbr>&nbsp;<wbr>EXAMPLE&nbsp;<wbr>#2: for 30p/24p mix&nbsp;<wbr>/&nbsp;<wbr>automatically<br />
&nbsp;<wbr><code>lav2yuv 60i.eli |&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>yuvkineco -F 4 | yuv2lav -f a -I 0 -o 30p.avi</code><br />
&nbsp;<wbr>&nbsp;<wbr>EXAMPLE&nbsp;<wbr>#3: for 24p movie&nbsp;<wbr>/&nbsp;<wbr>check and repair<br />
&nbsp;<wbr><code>lav2yuv 60i.eli |&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>yuvkineco -F 1 -C 60i.23c |&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>yuv2lav -f a -I 1 -o take1.avi<br />
&nbsp;<wbr>glav -F&nbsp;<wbr>+n take1.avi</code>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>check and edit 60i.23c<br />
&nbsp;<wbr><code>lav2yuv take1.avi |&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>yuvkineco -F 1 -N 60i.23c |&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>yuv2lav -f a -I 0 -o take2.avi</code><br />
&nbsp;<wbr>&nbsp;<wbr>EXAMPLE&nbsp;<wbr>#4: for 24p movie&nbsp;<wbr>/&nbsp;<wbr>check and retry<br />
&nbsp;<wbr><code>lav2yuv 60i.eli |&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>yuvkineco -F 1 -C 60i.23c |&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>yuv2lav -f a -I 0 -o take1.avi<br />
&nbsp;<wbr>glav -F&nbsp;<wbr>+n take1.avi</code>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>check and edit 60i.23c<br />
&nbsp;<wbr><code>lav2yuv 60i.eli |&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>yuvkineco -F 1 -O 60i.23c |&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>yuv2lav -f a -I 0 -o take2.avi</code> </p>
<h2>OPTIONS</h2>
<p> <code>yuvkineco</code> accepts the following options:</p>
<dl>
<dt><code>-F</code><i>&nbsp;<wbr>FPSCODE</i></p>
<dd> Set output fps code (default: same as input).</p>
<dt><code>-C</code><i>&nbsp;<wbr>PATH</i></p>
<dd> Specify 2-3 pull down cycle list file name to write.</p>
<dt><code>-O</code><i>&nbsp;<wbr>PATH</i></p>
<dd> Specify cycle list name to read with old yuv stream to retry.</p>
<dt><code>-N</code><i>&nbsp;<wbr>PATH</i></p>
<dd> Specify cycle list name to read with new yuv stream to repair.</p>
<dt><code>-S</code><i>&nbsp;<wbr>MIN</i></p>
<dd> Use <code><a href="/docs/linux/man/1-yuvycsnoise/">yuvycsnoise</a></code>(1) as preprocessor and specify minimum threshold.</p>
<dt><code>-n</code><i>&nbsp;<wbr>LEVEL</i></p>
<dd> Specify noise level of input (default: 10). This affects both pulldown cycle detection and deinterlacing.</p>
<dt><code>-c</code><i>&nbsp;<wbr>THRESHOLD</i></p>
<dd> Specify threshold to decide pictures in 2 frames are same (default: 4). <code>yuvkineco</code> compares several frames, searches pair of frame they contain same pictures, to decide which frame should be dropped. If <i>THRESHOLD</i> is 0, pair which has smallest difference will be selected. If 16, selected from pairs those have differences smaller than average.</p>
<dt><code>-i</code><i>&nbsp;<wbr>PERMIL</i></p>
<dd> <code>yuvkineco</code> deinterlaces each frame after 2-3 pulldown reverting process, specify how much pixels deinterlaced to decide to use or not use deinterlacing result (default: 10). If <i>PERMIL</i> is 10 and 1% or more of pixels deinterlaced, deinterlacing result will be used. If 0, always deinterlacing result will be used. If 1000, deinterlacing result will not be used, but deinterlacing process will run on all of frames. To disable deinterlacing process, specify negative value.</p>
<dt><code>-u</code></p>
<dd> Set interlace information in header of output to unknown (default: non-interlaced). </p>
</dl>
<h2>AUTHOR</h2>
<p> <code>yuvkineco</code> was written by Kawamata/Hitoshi.<br />
 If you have questions, remarks, problems or you just want to contact the developers, the main mailing list for the MJPEG-tools is:<br />
&nbsp;<wbr>&nbsp;<wbr><i>mjpeg-users [at] lists.sourceforge.net</i> </p>
<dl>
<dt>For more info, see our website at</p>
<dd> <i><a rel="nofollow" href="http://mjpeg.sourceforge.net/">http://mjpeg.sourceforge.net/</a></i> </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mjpegtools/">mjpegtools</a></code>(1), <code><a href="/docs/linux/man/1-yuvycsnoise/">yuvycsnoise</a></code>(1). </p>
<h2>Index</h2>
