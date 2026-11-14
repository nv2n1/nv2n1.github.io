---
title: "lavpipe(1)"
name: "lavpipe"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lavpipe/"
description: "lavpipe – creates raw YUV streams from pipe list scripts"
---

<h2 class="name">NAME</h2>
<p> lavpipe &#8211; creates raw YUV streams from pipe list scripts</p>
<h2>SYNOPSIS</h2>
<p> <code>lavpipe</code> [<code>-o</code> <i>num</i>] [<code>-n</code> <i>num</i>] <i>pipe-list</i> </p>
<h2>DESCRIPTION</h2>
<p> lavpipe reads a script file called &#8216;pipe list&#8217; that is of a similar structure as the edit lists that can be fed into lav2yuv. For info about the pipe list format see below. </p>
<p> The pipe list defines several video sources and filters that are combined by lavpipe to produce a single output YUV stream on stdout (which for example can be compressed and stored to disk via <code><a href="/docs/linux/man/1-mpeg2enc/">mpeg2enc</a></code>(1) or <code><a href="/docs/linux/man/1-yuv2lav/">yuv2lav</a></code>(1)). </p>
<h2>OPTIONS</h2>
<p> The command line options are used to output a specific part of the resulting video stream. That means you can tell lavpipe how many frames to skip and how many frames to deliver from that point on. </p>
<dl>
<dt><code>-o </code><i>num</i></p>
<dd> This is the frame offset of the output video. The first <i>num</i> frames of the resulting video simply are neither calculated nor written to stdout. This value defaults to 0. </p>
<dt><code>-n </code><i>num</i></p>
<dd> This is the frame count. If the input files or streams defined in the pipe list script are long enough, the output will be of exactly <i>num</i> frames length. A value of 0 means that all frames until the last one as defined in the pipe list will be written out, as long as there&#8217;s some input (0 is the default). </p>
<dt><i>pipe-list</i></p>
<dd> This is name of the pipe list file that lavpipe will &#8216;execute&#8217;. For information about this file&#8217;s format see below. </p>
<dt><code>-?</code></p>
<dd> Display a synopsis of the command syntax. </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>lavpipe -o 100 -n 25 film.pli</p>
<dd> would calculate and output to stdout frames 100 to 124 as defined in film.pli (in PAL this would be the 5th second of the film).</p>
<dt>lavpipe input.pli | yuv2lav -q80 output.avi</p>
<dd> would save the movie assembled by lavpipe as a single AVI file. </p>
</dl>
<h2>USAGE</h2>
<p> In this section the format of lavpipe&#8217;s input files the pipe list scripts is explained. If you need some examples or a more detailed tutorial, please read the <code><a href="/docs/linux/man/1-mjpegtools/">mjpegtools</a></code>(1) manpage&#8217;s section about <code>CREATING MOVIE TRANSITIONS</code>. and the file <i>README.lavpipe</i> that should be included in the distribution. Also feel free to contact us via the mailing list (see below). </p>
<p> A pipe list contains of two parts: the YUV <code>source list</code> and after this, as many <code>sequence descriptions</code> as wanted. It always begins with the following two lines: </p>
<dl>
<dt><code>LAV Pipe List</code></p>
<dd> This is the first line in every pipe list script. It is used as a simple test if lavpipe really was given a pipe list script and not your PhD thesis as input. </p>
<dt><code>NTSC</code>|<code>PAL</code></p>
<dd> This is the second line in every pipe list and can be either PAL or NTSC, depending on what video standard you use. I don&#8217;t remember if this is used at the moment. </p>
</dl>
<p> Now follows the <code>source list</code>: </p>
<dl>
<dt><i>num</i></p>
<dd> This is the number of input commands. lavpipe will read the next <i>num</i> lines and interpret them as input stream commands. </p>
<dt><i>command</i>&nbsp;<wbr>(<i>num</i>&nbsp;<wbr>times)</p>
<dd> This is a valid command line with two variables $o and $n that will be replaced by lavpipe with the offset and number of frames that the program has to output. Example:<br />
 <code>lav2yuv -o $o -f $n input.avi</code> </p>
</dl>
<p> Thus, an example <code>source list</code> could look like this:<br />
 <code>2</code><br />
 <code>lav2yuv -o $o -f $n scene1.avi</code><br />
 <code>lav2yuv -o $o -f $n scene2.avi</code> </p>
<p> after this you can append as many <code>sequence descriptions</code> as needed. Each of them is built up as follows: </p>
<dl>
<dt><i>num</i></p>
<dd> The number of frames that this sequence will last. </p>
<dt><i>num</i></p>
<dd> The number of inputs that will be used in this sequence. This number must of course be less than or equal to the number of inputs that are defined above. </p>
<dt><i>idx</i> [<i>ofs</i>] (<i>num</i> times)</p>
<dd> These are the indices to the sources that are defined at the beginning of the file (first source is 0) with an optional frame offset (i.e. sequence starts with frame number <i>ofs</i> of this input.) &#8211; this value defaults to 0. Example:<br />
 <code>0 150</code> </p>
<dt><i>command</i></p>
<dd> This is a valid command line to a YUV filter tool that reads <i>num</i> input streams and writes one output stream, combining its inputs. Optionally, the filter tool can be given the two $o and $n variables that will be replaced by lavpipe as in the source commands (see above). For further info read <i>README.lavpipe</i> or the documentation for the filter programs (if available). An example filter could look like this:<br />
 <code>transist.flt -o 0 -O 255 -s $o -n $n -d 50</code><br />
 And if the sequence only has one input that simply should be copied to the output, you can use a dash instead of a command line:<br />
 <code>&#8211;</code> </p>
</dl>
<p> And here&#8217;s an example for a complete pipe list that implements a transistion from scene1.avi to scene2.avi </p>
<p> <code>REMOVE THE COMMENTS AFTER The #</code> </p>
<p> <code>LAV Pipe List</code><br />
 <code>PAL</code><br />
 <code>2</code><br />
 <code>lav2yuv -o $o -f $n scene1.avi</code><br />
 <code>lav2yuv -o $o -f $n scene2.avi</code><br />
 <code>50</code> # first sequence: 50 frames<br />
 <code>1</code> # contains one input:<br />
 <code>0 0</code> # scene1.avi, offset 0<br />
 <code>&#8211;</code> # simple output<br />
 <code>25</code> # second sequence: 25 frames<br />
 <code>2</code> # contains two inputs:<br />
 <code>0 50</code> # scene1.avi, offset 50<br />
 <code>1</code> # scene2.avi, offset 0<br />
 <code>transist.flt -o 0 -O 255 -s $o -n $n -d 50</code> # transistion<br />
 <code>50</code> # third sequence: 50 frames<br />
 <code>1</code> # contains one input:<br />
 <code>1 25</code> # scene2.avi, offset 25<br />
 <code>&#8211;</code> # simple output </p>
<h2>BUGS</h2>
<p> I&#8217;m sure there are enough of them. lavpipe often accepts malformed pipe lists and then writes out a video that was all but intended &#8211; without warning. </p>
<p> <code>The mention of $n above is wrong. At one time there were two parameters but now a program is allowed to produce as many frames as it wants. THe author of the program hard coded, for reasons unknown, $n to be 0.</code></p>
<h2>NOTES</h2>
<p> There are also some serious limitations in the system, such as frame-by-frame processing. But as the goal when writing lavpipe was the simplicity of the pipeline, other tools will have to be written to do more interesting tasks.<br />
 But I want to note that it is very well possible to write a pipe list that combines several files, and then use that pipe list as an input for another pipe list by simply using the lavpipe command in the source list (see above) &#8211; this can be already used to do some nice things, if you have some nice filters. </p>
<p> <code>Comments are NOT allowed in pipelist files. The comments (text after #) above are for illustration only.</code></p>
<h2>AUTHOR</h2>
<p> This man page was written by Philipp Zabel.<br />
 If you have questions, remarks, problems or you just want to contact the developers, the main mailing list for the MJPEG-tools is:<br />
&nbsp;<wbr>&nbsp;<wbr><i>mjpeg-users [at] lists.sourceforge.net</i> </p>
<dl>
<dt>For more info, see our website at</p>
<dd> <i><a rel="nofollow" href="http://mjpeg.sourceforge.net">http://mjpeg.sourceforge.net</a></i> </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-lav2yuv/">lav2yuv</a></code>(1), <code><a href="/docs/linux/man/1-lavplay/">lavplay</a></code>(1), <code><a href="/docs/linux/man/1-lavrec/">lavrec</a></code>(1), <code><a href="/docs/linux/man/1-mpeg2enc/">mpeg2enc</a></code>(1), <code><a href="/docs/linux/man/1-yuv2lav/">yuv2lav</a></code>(1), <code><a href="/docs/linux/man/1-yuvscaler/">yuvscaler</a></code>(1) </p>
<h2>Index</h2>
