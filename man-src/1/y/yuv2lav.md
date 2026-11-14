---
title: "yuv2lav(1)"
name: "yuv2lav"
section: "1"
letter: "y"
url: "/docs/linux/man/1-yuv2lav/"
description: "yuv2lav – encodes lavtool’s raw YUV frame streams into MJPEG files"
---

<h2 class="name">NAME</h2>
<p> yuv2lav &#8211; encodes lavtool&#8217;s raw YUV frame streams into MJPEG files</p>
<h2>SYNOPSIS</h2>
<p> <code>yuv2lav</code> [<code>-f</code><code>&nbsp;<wbr>a</code>|<code>A</code>|<code>q</code>|<code>m</code>] [<code>-q</code> <i>num</i>] [<code>-b</code> <i>num</i>] [<code>-I</code> <i>num</i>] [<code>-m</code> <i>num</i>] [<code>-v</code> <i>num</i>] [<code>-w</code> <i>file</i>] <code>-o</code> <i>output-file</i> </p>
<h2>DESCRIPTION</h2>
<p> yuv2lav is a simple MJPEG encoder for raw YUV frame streams as they are emitted by <code><a href="/docs/linux/man/1-lav2yuv/">lav2yuv</a></code>(1) or <code><a href="/docs/linux/man/1-lavpipe/">lavpipe</a></code>(1), for example. It reads its input from stdin and is capable of writing AVI and Quicktime. </p>
<h2>OPTIONS</h2>
<p> The command line options allow to specify the output file name, JPEG encoding quality and the amount of memory that will be allocated for JPEG compressed data. </p>
<dl>
<dt><code>-o</code><i>&nbsp;<wbr>output-file</i></p>
<dd> This (compulsorary) option sets the name of the file that yuv2lav will write its output to. If the output file contains a % (e.g. file%02d.avi), the output will be written to multiple files in case this is necessary (file00.avi, file01.avi and so on). </p>
<dt><code>-f</code><code>&nbsp;<wbr>a</code>|<code>A</code>|<code>q</code></p>
<dd> This sets the output file format, which has to be one of<br />
 <code>&nbsp;<wbr>a</code> &#8211; for AVI file output,<br />
 <code>&nbsp;<wbr>A</code> &#8211; for AVI with reversed fields,<br />
 <code>&nbsp;<wbr>q</code> &#8211; for Quicktime output or<br />
 AVI with reversed field of course only makes sense if yuv2lav&#8217;s feed is an interlaced video source and should only be needed if you experience frame reversal problems in your output. If you don&#8217;t use that option yuv2lav will set the output format to AVI if the last 3 char are avi, or to Quicktime if you use mov. If you use the -f option it overides the setting in the filename</p>
<dt><code>-q</code><i>&nbsp;<wbr>num</i></p>
<dd> This option specifies the JPEG encoding quality as passed through to libjpeg. The default value is 80, <i>num</i> must lie within 24&#8230;100 inclusive (think of it as percentage values, although with a lossy compression algorithm like JPEG, keeping 100% of the original quality is of course not really possible). </p>
<dt><code>-b</code><i>&nbsp;<wbr>num</i></p>
<dd> This option specifies the size of the buffer (in kBytes) that yuv2lav allocates in order to store the compressed JPEG data in it. The default value (256k) is perfectly enough for 100% quality full sized PAL/NTSC, but if you want to compress Super-Mega-HDTV or if you are low on memory, you can use this option to suit your needs. </p>
<dt><code>-m</code><i>&nbsp;<wbr>num</i></p>
<dd> This is the maximum size (in MB) per file. Normally this depends on the output file type. </p>
<dt><code>-I</code><i>&nbsp;<wbr>num</i></p>
<dd> Force a specific interlacing type. 0 means no interlacing, 1 means top-field-first, 2 means bottom-field-first. </p>
<dt><code>-w</code><i>&nbsp;<wbr>file</i></p>
<dd> This is the WAV file containing audio data to be combined with the video stream into the output file. </p>
<dt><code>-v</code><i>&nbsp;<wbr>num</i></p>
<dd> Verbosity level. 0 means only print error messages, 2 prints full debug output. </p>
<dt><code>-?</code></p>
<dd> Display a synopsis of the command syntax. </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>lav2yuv movie.avi | yuv2lav -fq -q 30 lowbitrate.qt</p>
<dd> would recompress movie.avi as a low bit rate Quicktime file.</p>
<dt>lavpipe input.pli | yuv2lav -q80 output.avi</p>
<dd> would save the movie assembled by lavpipe as a single AVI file. </p>
</dl>
<h2>BUGS</h2>
<p> If you experience any problems with this tool, please feel free to contact the developers (see below). </p>
<h2>AUTHOR</h2>
<p> This man page was written by pHilipp Zabel.<br />
 If you have questions, remarks, problems or you just want to contact the developers, the main mailing list for the MJPEG-tools is: </p>
<p>&nbsp;<wbr><i>mjpeg-users [at] lists.sourceforge.net</i> </p>
<p> For more info, see our website at </p>
<p>&nbsp;<wbr><i><a rel="nofollow" href="http://mjpeg.sourceforge.net/">http://mjpeg.sourceforge.net/</a></i> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-lav2yuv/">lav2yuv</a></code>(1), <code><a href="/docs/linux/man/1-lavpipe/">lavpipe</a></code>(1), <code><a href="/docs/linux/man/1-lavplay/">lavplay</a></code>(1), <code><a href="/docs/linux/man/1-lavrec/">lavrec</a></code>(1), <code><a href="/docs/linux/man/1-mpeg2enc/">mpeg2enc</a></code>(1), <code><a href="/docs/linux/man/1-yuvscaler/">yuvscaler</a></code>(1) </p>
<h2>Index</h2>
