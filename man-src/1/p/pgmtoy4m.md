---
title: "pgmtoy4m(1)"
name: "pgmtoy4m"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pgmtoy4m/"
description: "pgmtoy4m – Convert mpeg2dec pgm and pgmpipe output to YUV4MPEG2"
---

<h2>NAME</h2>
<p> pgmtoy4m &#8211; Convert mpeg2dec pgm and pgmpipe output to YUV4MPEG2</p>
<h2>SYNOPSIS</h2>
<p> <code>pgmtoy4m</code> [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>pgmtoy4m</code> repacks the PGM output from <code>mpeg2dec</code> into YUV4MPEG2 4:2:0p. No actual changes to the data are made. The data is unpacked from the quasi-PGM format and placed in YUV4MPEG2 format with the specified sample aspect, frame rate and field order. Output must be either to a pipe or a file, leaving stdout as a terminal will elicit an error and the program will exit.</p>
<h2>OPTIONS</h2>
<p> <code>pgmtoy4m</code> accepts the following options:</p>
<dl>
<dt><code>-v</code><i> num</i></p>
<dd> Set verbosity level. (default: 0)</p>
<dt><code>-h</code></p>
<dd> Print a usage summary and exit.</p>
<dt><code>-i</code><i> t|b|p</i></p>
<dd> Set the interlacing mode. Top field first (t), bottom field first (b) or progressive/none (p). (default: t)</p>
<dt><code>-a</code><i> sar</i></p>
<dd> Set the sample aspect ratio. (default: 10:11)</p>
<dt><code>-r</code><i> frame rate</i></p>
<dd> Set the frame rate. (default: 30000:1001)</dl>
<h2>EXAMPLES</h2>
<pre>
mpeg2dec -s -o pgmpipe file.mpg | pgmtoy4m -a 10:11 -r 24000:1001 -i b | yuvplay
mpeg2dec -s -o pgm file.mpg
cat *.pgm | pgmtoy4m -r 30000:1001 -i t | yuvplay
</pre>
<h2>NOTES</h2>
<p> This program is specifically designed to work with the output of mpeg2dec and is <code>NOT</code> a general PGM (NetPBM) tool! </p>
<p> From the introduction in the source file: </p>
<pre>
 * Note: mpeg2dec uses a variation of the PGM format - they're really not
 * &quot;Grey Maps&quot; but rather a catenation of the 420P data (commonly called
 * &quot;YUV&quot;).    The type is P5 (&quot;raw&quot;) and the number of rows is really
 * the total of the Y', Cb and Cr heights.   The Cb and Cr data is &quot;joined&quot;
 * together.  After the Y' rows you have 1 row of Cb and 1 row of Cr per 
 * &quot;row&quot; of PGM data.
 * NOTE: You MAY need to know the field order (top/bottom field first),
 *      sample aspect ratio and frame rate because the PGM format makes
 *      none of that information available!
</pre>
<h2>AUTHOR</h2>
<p> This manpage was written by Steven Schultz (sms at 2bsd dot com).</p>
<h2>BUGS</h2>
<p> Possible but none known at the present time. </p>
<h2>Index</h2>
