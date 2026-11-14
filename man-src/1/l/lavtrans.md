---
title: "lavtrans(1)"
name: "lavtrans"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lavtrans/"
description: "lavtrans – Convert MJPEG videos to other MJPEG video formats"
---

<h2 class="name">NAME</h2>
<p> lavtrans &#8211; Convert MJPEG videos to other MJPEG video formats</p>
<h2>SYNOPSIS</h2>
<p> <code>lavtrans -o</code> <i>outputfile</i> <code>-f a</code>|<code>q</code>|<code>i</code>|<code>w</code> [<code>-i</code> <i>num</i>] <i>lavfile1 </i>[<i>lavfile2 </i>&#8230;<i> lavfileN</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>lavtrans</code> can be used to convert the recorded videos from one MJPEG &quot;container&quot; format to another one. It can also be used to split the streams, or do destructive edits. </p>
<p> Like all the other <code><a href="/docs/linux/man/1-mjpegtools/">mjpegtools</a></code>(1) lavtrans also accept a edit list file in place of actual video files. This allows it to be used to construct a stand-alone copy of the editted video sequence described in the editlist. </p>
<p> Note that lavtrans can only change the container type of MJPEG video, not the format. As such it is not possible to use it combine streams of different format. </p>
<h2>OPTIONS</h2>
<p> <code>lavtrans</code> accepts the following options: </p>
<dl>
<dt><code>-f</code> [<code>a</code>|<code>q</code>|<code>m</code>|<code>i</code>|<code>w</code>]</p>
<dd> Specifies the output format that should be saved.<br />
&nbsp;<wbr>&nbsp;<wbr>a &#8211; output to AVI file<br />
&nbsp;<wbr>&nbsp;<wbr>q &#8211; output to Qicktime file<br />
&nbsp;<wbr>&nbsp;<wbr>i &#8211; output single JPEG images,<br />
&nbsp;<wbr>&nbsp;<wbr>w &#8211; output WAV file&nbsp;<wbr>(sound only!) </p>
<dt><code>-i</code><i> num</i></p>
<dd> Convert a single frame to a JPEG file. </p>
<dt><code>-o</code><i> outputfile</i></p>
<dd> Specifies the name of the output file If you want as output single JPEG images the output file string must be a valid format string </p>
<dt><i>filename</i></p>
<dd> Multiple filenames as input are acceped, also mixing of edit list files and other in video files. </p>
</dl>
<h2>BUGS</h2>
<p> There seem to be problems with the transoding of large Quicktime movies. One other thing is that with interlaced movies only one field is extracted. So you get pictures with the full horizontal size and half vertical size. </p>
<h2>AUTHOR</h2>
<p> This man page was written by Bernhard Praschinger.<br />
 If you have questions, remarks, problems or you just want to contact the developers, the main mailing list for the MJPEG-tools is:<br />
&nbsp;<wbr>&nbsp;<wbr><i>mjpeg-users [at] lists.sourceforge.net</i> </p>
<dl>
<dt>For more info, see our website at</p>
<dd> <i><a rel="nofollow" href="http://mjpeg.sourceforge.net">http://mjpeg.sourceforge.net</a></i> </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mjpegtools/">mjpegtools</a></code>(1), <code><a href="/docs/linux/man/1-lavplay/">lavplay</a></code>(1) </p>
<h2>Index</h2>
