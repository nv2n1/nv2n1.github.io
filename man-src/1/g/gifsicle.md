---
title: "gifsicle(1)"
name: "gifsicle"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gifsicle/"
description: "gifsicle – manipulates GIF images and animations"
---

<h2>NAME</h2>
<p> gifsicle &#8211; manipulates GIF images and animations</p>
<h2>SYNOPSIS</h2>
<p> <code>gifsicle</code> [options, frames, and filenames]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>gifsicle</code> is a powerful command-line program for creating, editing, manipulating, and getting information about GIF images and animations. </p>
<p> <code>Gifsicle</code> normally processes input GIF files according to its command line options and writes the result to the standard output. The <code>-i</code> option, for example, tells <code>gifsicle</code> to interlace its inputs: </p>
<dl>
<dt>
<dd>
<pre>
<code>gifsicle -i &lt; pic.gif &gt; interlaced-pic.gif</code>
</pre>
</dl>
<p> <code>Gifsicle</code> is good at creating and manipulating GIF animations. By default, it combines two or more input files into a &#8220;flipbook&#8221; animation: </p>
<dl>
<dt>
<dd>
<pre>
<code>gifsicle pic1.gif pic2.gif pic3.gif &gt; animation.gif</code>
</pre>
</dl>
<p> Use options like <code>&#8211;delay</code>, <code>&#8211;loopcount</code>, and <code>&#8211;optimize</code> to tune your animations. </p>
<p> To modify GIF files in place, use the <code>&#8211;batch</code> option. With <code>&#8211;batch</code>, <code>gifsicle</code> will modify the files you specify instead of writing a new file to the standard output. To interlace all the GIFs in the current directory, you could say: </p>
<dl>
<dt>
<dd>
<pre>
<code>gifsicle --batch -i *.gif
</code></pre>
</dl>
<p> New users may want to skip to the Examples section at the end.</p>
<h2>CONCEPT INDEX</h2>
<p> Concepts are on the left, relevant <code>gifsicle</code> options are on the right. </p>
<dl>
<dt>Animations, changing</p>
<dd> frame selections, frame changes, etc.</p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>disposal</p>
<dd> <code>&#8211;disposal</code></p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>looping</p>
<dd> <code>&#8211;loopcount</code></p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>portions of</p>
<dd> frame selections</p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>smaller</p>
<dd> <code>&#8211;optimize</code>, <code>&#8211;colors</code></p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>speed</p>
<dd> <code>&#8211;delay</code></p>
<dt>Bad output</p>
<dd> <code>&#8211;careful</code></p>
<dt>Background color</p>
<dd> <code>&#8211;background</code></p>
<dt>Colors, changing</p>
<dd> <code>&#8211;change-color</code>, <code>&#8211;use-colormap</code>, <code>&#8211;dither</code>, <code>&#8211;transform-colormap</code></p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>reducing number</p>
<dd> <code>&#8211;colors</code>, <code>&#8211;dither</code>, <code>&#8211;gamma</code></p>
<dt>Comments</p>
<dd> <code>&#8211;comment</code></p>
<dt>Extensions</p>
<dd> <code>&#8211;extension</code>, <code>&#8211;app-extension</code>, <code>&#8211;extension-info</code></p>
<dt>File size</p>
<dd> <code>&#8211;optimize</code>, <code>&#8211;unoptimize</code>, <code>&#8211;colors</code></p>
<dt>Image transformations</p>
<dd>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>cropping</p>
<dd> <code>&#8211;crop</code>, <code>&#8211;crop-transparency</code></p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>flipping</p>
<dd> <code>&#8211;flip-*</code></p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>resizing</p>
<dd> <code>&#8211;resize</code>, <code>&#8211;scale</code></p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rotating</p>
<dd> <code>&#8211;rotate-*</code></p>
<dt>Grayscale</p>
<dd> <code>&#8211;use-colormap</code></p>
<dt>Interlacing</p>
<dd> <code>&#8211;interlace</code></p>
<dt>Positioning frames</p>
<dd> <code>&#8211;position</code></p>
<dt>Screen, logical</p>
<dd> <code>&#8211;logical-screen</code></p>
<dt>Selecting frames</p>
<dd> frame selections (like <code>&#8216;#0&#8217;</code>)</p>
<dt>Transparency</p>
<dd> <code>&#8211;transparent</code></p>
<dt>Warnings</p>
<dd> <code>&#8211;no-warnings</code></dl>
<h2>COMMAND LINE</h2>
<p> <code>gifsicle</code>&#8216;s command line consists of GIF input files and options. Most options start with a dash (-) or plus (+); frame selections, a kind of option, start with a number sign (#). Anything else is a GIF input file. </p>
<p> <code>gifsicle</code> reads and processes GIF input files in order. If no GIF input file is given, or you give the special filename &#8216;-&#8216;, it reads from the standard input. </p>
<p> <code>gifsicle</code> exits with status 0 if there were no errors and status 1 otherwise.</p>
<h2>OPTIONS</h2>
<p> Every option has a long form, &#8216;<code>&#8211;long-descriptive-name</code>&#8216;. You don&#8217;t need to type the whole long descriptive name, just enough to make it unambiguous. </p>
<p> Some options also have a short form, &#8216;<code>-X</code>&#8216;. You can combine short options if they don&#8217;t take arguments: &#8216;<code>-IIb</code>&#8216; is the same as &#8216;<code>-I -I -b</code>&#8216;. But be careful with options that do take arguments: &#8216;<code>-cblah</code>&#8216; means &#8216;<code>-c blah</code>&#8216;, not &#8216;<code>-c -b -l -a -h</code>&#8216;. </p>
<p> Many options also have a converse, &#8216;<code>&#8211;no-option</code>&#8216;, which turns off the option. You can turn off a short option &#8216;<code>-X</code>&#8216; by saying &#8216;<code>+X</code>&#8216; instead.</p>
<h3>Mode Options</h3>
<p> Mode options tell <code>gifsicle</code> what kind of output to generate. There can be at most one, and it must precede any GIF inputs.</p>
<dl>
<dt> <code>&#8211;merge</code>, <code>-m</code></p>
<dd> Combine all GIF inputs into one file with multiple frames and write that file to the standard output. This is the default mode.</p>
<dt> <code>&#8211;batch</code>, <code>-b</code></p>
<dd> Modify each GIF input in place by reading and writing to the same filename. (GIFs read from the standard input are written to the standard output.)</p>
<dt> <code>&#8211;explode</code>, <code>-e</code></p>
<dd> Create an output GIF for each frame of each input file. The output GIFs are named &#8216;xxx.000&#8217;, &#8216;xxx.001&#8217;, and so on, where &#8216;xxx&#8217; is the name of the input file (or whatever you specified with &#8216;<code>&#8211;output</code>&#8216;) and the numeric extension is the frame number.</p>
<dt> <code>&#8211;explode-by-name</code>, <code>-E</code></p>
<dd> Same as <code>&#8211;explode</code>, but write any named frames to files &#8216;xxx.<i>name</i>&#8216; instead of &#8216;xxx.<i>frame-number</i>&#8216;. Frames are named using the &#8216;<code>&#8211;name</code>&#8216; option.</dl>
<h3>General Options</h3>
<p> General options control the information <code>gifsicle</code> prints and where it writes its output. The info options and <code>&#8211;verbose</code> can be turned off with &#8216;<code>&#8211;no-X</code>&#8216;. </p>
<dl>
<dt> <code>&#8211;info</code>, <code>-I</code></p>
<dd> Print a human-readable description of each input GIF to the standard output, or whatever file you specify with <code>-o</code>. This option suppresses normal output, and cannot be combined with mode options like <code>&#8211;batch</code>. If you give two <code>&#8211;info</code> or <code>-I</code> options, however, information is printed to standard error, and normal output takes place as usual. </p>
<dt> <code>&#8211;color-info</code>, <code>&#8211;cinfo</code></p>
<dd> Like <code>&#8211;info</code>, but also print information about input files&#8217; colormaps. </p>
<dt> <code>&#8211;extension-info</code>, <code>&#8211;xinfo</code></p>
<dd> Like <code>&#8211;info</code>, but also print any unrecognized GIF extensions in a <code><a href="/docs/linux/man/1-hexdump/">hexdump</a></code>(1)-like format. </p>
<dt> <code>&#8211;size-info</code>, <code>&#8211;sinfo</code></p>
<dd> Like <code>&#8211;info</code>, but also print information about compressed image sizes. </p>
<dt> <code>&#8211;help</code>, <code>-h</code></p>
<dd> Print usage information and exit. </p>
<dt> <i></i><code>-o </code><i>file</i><i></i><i></i></p>
<dd>
<dt> <i></i><code>&#8211;output </code><i>file</i><i></i><i></i></p>
<dd> Send output to <i>file</i>. The special filename &#8216;-&#8216; means the standard output. </p>
<dt> <code>&#8211;verbose</code>, <code>-V</code></p>
<dd> Print progress information (files read and written) to standard error. </p>
<dt> <code>&#8211;no-warnings</code>, <code>-w</code></p>
<dd> Suppress all warning messages. </p>
<dt> <code>&#8211;version</code></p>
<dd> Print the version number and some short non-warranty information and exit. </p>
<dt> <code>&#8211;careful</code></p>
<dd> Write slightly larger GIFs that avoid bugs in some other GIF implementations. Some Java and Internet Explorer versions cannot display the correct, minimal GIFs that Gifsicle produces. Use the <code>&#8211;careful</code> option if you are having problems with a particular image. </p>
<dt> <code>&#8211;conserve-memory</code></p>
<dd> Conserve memory usage at the expense of processing time. This may be useful if you are processing large GIFs on a computer without very much memory. </p>
<dt> <code>&#8211;nextfile</code></p>
<dd> Allow input files to contain multiple concatenated GIF images. If a filename appears multiple times on the command line, <code>gifsicle</code> will read a new image from the file each time. This option can help scripts avoid the need for temporary files. For example, to create an animated GIF with three frames with different delays, you might run &quot;<code>gifsicle &#8211;nextfile -d10 &#8211; -d20 &#8211; -d30 &#8211; &gt; out.gif</code>&quot; and write the three GIF images, in sequence, to <code>gifsicle</code>&#8216;s standard input. </p>
<dt> <code>&#8211;multifile</code></p>
<dd> Like <code>&#8211;nextfile</code>, but read <i>as many GIF images as possible</i> from each file. This option is intended for scripts. For example, to merge an unknown number of GIF images into a single animation, run &quot;<code>gifsicle &#8211;multifile &#8211; &gt; out.gif</code>&quot; and write the GIF images, in sequence, to <code>gifsicle</code>&#8216;s standard input. Any frame selections apply only to the last file in the concatenation.</dl>
<h3>Frame Selections</h3>
<p> A frame selection tells <code>gifsicle</code> which frames to use from the current input file. They are useful only for animations, as non-animated GIFs only have one frame. Here are the acceptable forms for frame specifications. </p>
<dl>
<dt><code>#</code><i>num</i></p>
<dd> Select frame <i>num</i>. (The first frame is &#8216;<code>#0</code>&#8216;. Negative numbers count backwards from the last frame, which is &#8216;<code>#-1</code>&#8216;.)</p>
<dt><code>#</code><i>num1</i><code>&#8211;</code><i>num2</i></p>
<dd> Select frames <i>num1</i> through <i>num2</i>.</p>
<dt><code>#</code><i>num1</i><code>&#8211;</code></p>
<dd> Select frames <i>num1</i> through the last frame.</p>
<dt><code>#</code><i>name</i></p>
<dd> Select the frame named <i>name</i>.</dl>
<p> The &#8216;#&#8217; character has special meaning for many shells, so you generally need to quote it. </p>
<p> For example,</p>
<dl>
<dt>
<dd>
<pre>
<code>gifsicle happy.gif &quot;#0&quot;</code>
</pre>
</dl>
<p> uses the first frame from happy.gif;</p>
<dl>
<dt>
<dd>
<pre>
<code>gifsicle happy.gif &quot;#0-2&quot;</code>
</pre>
</dl>
<p> uses its first three frames; and</p>
<dl>
<dt>
<dd>
<pre>
<code>gifsicle happy.gif &quot;#-1-0&quot;</code>
</pre>
</dl>
<p> uses its frames in reverse order (starting from frame #-1 &#8212; the last frame &#8212; and ending at frame #0 &#8212; the first). </p>
<p> The action performed with the selected frames depends on the current mode. In merge mode, only the selected frames are merged into the output GIF. In batch mode, only the selected frames are modified; other frames remain unchanged. In explode mode, only the selected frames are exploded into output GIFs.</p>
<h3>Frame Change Options</h3>
<p> Frame change options insert new frames into an animation or replace or delete frames that already exist. Some things &#8212; for example, changing one frame in an animation &#8212; are difficult to express with frame selections, but easy with frame changes.</p>
<dl>
<dt> <i></i><code>&#8211;delete </code><i>frames</i> [<i>frames</i>&#8230;]<i></i></p>
<dd> Delete <i>frames</i> from the input GIF.</p>
<dt> <i></i><code>&#8211;insert-before </code><i>frame other-GIFs</i><i></i><i></i></p>
<dd> Insert <i>other-GIFs</i> before <i>frame</i> in the input GIF.</p>
<dt> <i></i><code>&#8211;append </code><i>other-GIFs</i><i></i><i></i></p>
<dd> Append <i>other-GIFs</i> to the input GIF.</p>
<dt> <i></i><code>&#8211;replace </code><i>frames other-GIFs</i><i></i><i></i></p>
<dd> Replace <i>frames</i> from the input GIF with <i>other-GIFs</i>.</p>
<dt><code>&#8211;done</code></p>
<dd> Complete the current set of frame changes.</dl>
<p> The <i>frames</i> arguments are frame selections (see above). These arguments always refer to frames from the <i>original</i> input GIF. So, if &#8216;a.gif&#8217; has 3 frames and &#8216;b.gif&#8217; has one, this command</p>
<dl>
<dt>
<dd>
<pre>
<code>gifsicle a.gif --delete &quot;#0&quot; --replace &quot;#2&quot; b.gif</code>
</pre>
</dl>
<p> will produce an output animation with 2 frames: &#8216;a.gif&#8217; frame 1, then &#8216;b.gif&#8217;. </p>
<p> The <i>other-GIFs</i> arguments are any number of GIF input files and frame selections. These images are combined in merge mode and added to the input GIF. The <i>other-GIFs</i> last until the next frame change option, so this command replaces the first frame of &#8216;in.gif&#8217; with the merge of &#8216;a.gif&#8217; and &#8216;b.gif&#8217;:</p>
<dl>
<dt>
<dd>
<pre>
<code>gifsicle -b in.gif --replace &quot;#0&quot; a.gif b.gif</code>
</pre>
</dl>
<p> This command, however, replaces the first frame of &#8216;in.gif&#8217; with &#8216;a.gif&#8217; and then processes &#8216;b.gif&#8217; separately:</p>
<dl>
<dt>
<dd>
<pre>
<code>gifsicle -b in.gif --replace &quot;#0&quot; a.gif --done b.gif</code>
</pre>
</dl>
<p> Warning: You shouldn&#8217;t use both frame selections and frame changes on the same input GIF.</p>
<h3>Image Options</h3>
<p> Image options modify input images &#8212; by changing their interlacing, transparency, and cropping, for example. Image options have three forms: &#8216;<code>&#8211;X</code>&#8216;, &#8216;<code>&#8211;no-X</code>&#8216;, and &#8216;<code>&#8211;same-X</code>&#8216;. The &#8216;<code>&#8211;X</code>&#8216; form selects a value for the feature, the &#8216;<code>&#8211;no-X</code>&#8216; form turns off the feature, and the &#8216;<code>&#8211;same-X</code>&#8216; form means that the feature&#8217;s value is copied from each input. The default is always &#8216;<code>&#8211;same-X</code>&#8216;. For example, <code>-background=</code>&quot;#0000FF&quot; sets the background color to blue, <code>&#8211;no-background</code> turns the background color off (by setting it to 0), and <code>&#8211;same-background</code> uses input images&#8217; existing background colors. You can give each option multiple times; for example,</p>
<dl>
<dt>
<dd>
<pre>
<code>gifsicle -b -O2 -i a.gif --same-interlace b.gif c.gif</code>
</pre>
</dl>
<p> will make &#8216;a.gif&#8217; interlaced, but leave &#8216;b.gif&#8217; and &#8216;c.gif&#8217; interlaced only if they were already. </p>
<dl>
<dt> <i></i><code>-B </code><i>color</i><i></i><i></i></p>
<dd>
<dt> <i></i><code>&#8211;background </code><i>color</i><i></i><i></i></p>
<dd> Set the output GIF&#8217;s background to <i>color</i>. The argument can have the same forms as in the <code>&#8211;transparent</code> option below. </p>
<dt> </i><code>&#8211;crop </code><i>x1</i>,<i>y1</i>&#8211;<i>x2,<i>y2</i></p>
<dd>
<dt> </i><code>&#8211;crop </code><i>x1</i>,<i>y1</i>+<i>widthx<i>height</i></p>
<dd> Crop the following input frames to a smaller rectangular area. The top-left corner of this rectangle is (<i>x1</i>,<i>y1</i>); you can give either the lower-right corner, (<i>x2</i>,<i>y2</i>), or the width and height of the rectangle. In the <i>x1</i>,<i>y1</i>+<i>width</i>x<i>height</i> form, <i>width</i> and <i>height</i> can be zero or negative. A zero dimension means the cropping area goes to the edge of the image; a negative dimension brings the cropping area that many pixels back from the image edge. For example, <code>&#8211;crop</code> 2,2+-2x-2 will shave 2 pixels off each side of the input image. Cropping takes place before any rotation, flipping, resizing, or positioning. </p>
<dt> <code>&#8211;crop-transparency</code></p>
<dd> Crop any transparent borders off the following input frames. This happens after any cropping due to the <code>&#8211;crop</code> option. It works on the raw input images; for example, any transparency options have not yet been applied. </p>
<dt> <code>&#8211;flip-horizontal</code></p>
<dd>
<dt> <code>&#8211;flip-vertical</code></p>
<dd> Flip the following frames horizontally or vertically. </p>
<dt> <code>-i</code></p>
<dd>
<dt> <code>&#8211;interlace</code></p>
<dd> Turn interlacing on. </p>
<dt> <i></i><code>-S </code><i>width</i>x<i>height</i><i></i></p>
<dd>
<dt> <i></i><code>&#8211;logical-screen </code><i>width</i>x<i>height</i><i></i></p>
<dd> Set the output logical screen to <i>width</i>x<i>height</i>. <code>&#8211;no-logical-screen</code> sets the output logical screen to the size of the largest output frame, while <code>&#8211;same-logical-screen</code> sets the output logical screen to the largest input logical screen. <code>&#8211;screen</code> is a synonym for <code>&#8211;logical-screen</code>. </p>
<dt> </i><code>-p </code><i>x,<i>y</i><i></i><i></i></p>
<dd>
<dt> </i><code>&#8211;position </code><i>x,<i>y</i><i></i><i></i></p>
<dd> Set the following frames&#8217; positions to (<i>x</i>,<i>y</i>). <code>&#8211;no-position</code> means <code>&#8211;position</code> 0,0. Normally, </i><code>&#8211;position </code><i>x,<i>y</i><i></i><i></i> places every succeeding frame exactly at <i>x</i>,<i>y</i>. However, if an entire animation is input, <i>x</i>,<i>y</i> is treated as the position for the animation. </p>
<dt> <code>&#8211;rotate-90</code></p>
<dd>
<dt> <code>&#8211;rotate-180</code></p>
<dd>
<dt> <code>&#8211;rotate-270</code></p>
<dd> Rotate the following frames by 90, 180, or 270 degrees. <code>&#8211;no-rotate</code> turns off any rotation. </p>
<dt> <i></i><code>-t </code><i>color</i><i></i><i></i></p>
<dd>
<dt> <i></i><code>&#8211;transparent </code><i>color</i><i></i><i></i></p>
<dd> Make <i>color</i> transparent in the following frames. <i>Color</i> can be a colormap index (0-255), a hexadecimal color specification (like &quot;#FF00FF&quot; for magenta), or slash- or comma-separated red, green and blue values (each between 0 and 255).</dl>
<h3>Extension Options</h3>
<p> Extension options add non-visual information to the output GIF. This includes names, comments, and generic extensions. </p>
<dl>
<dt> <i></i><code>&#8211;app-extension </code><i>app-name</i> <i>extension</i><i></i></p>
<dd> Add an application extension named <i>app-name</i> and with the value <i>extension</i> to the output GIF. <code>&#8211;no-app-extensions</code> removes application extensions from the input images. </p>
<dt> <i></i><code>-c </code><i>text</i><i></i><i></i></p>
<dd>
<dt> <i></i><code>&#8211;comment </code><i>text</i><i></i><i></i></p>
<dd> Add a comment, <i>text</i>, to the output GIF. The comment will be placed before the next frame in the stream. <code>&#8211;no-comments</code> removes comments from the input images. </p>
<dt> <i></i><code>&#8211;extension </code><i>number</i> <i>extension</i><i></i></p>
<dd> Add an extension numbered <i>number</i> and with the value <i>extension</i> to the output GIF. <i>Number</i> can be in decimal, octal, hex, or it can be a single character like &#8216;n&#8217;, whose ASCII value is used. <code>&#8211;no-extensions</code> (or <code>+x</code>) removes extensions from the input images. </p>
<dt> <i></i><code>-n </code><i>text</i><i></i><i></i></p>
<dd>
<dt> <i></i><code>&#8211;name </code><i>text</i><i></i><i></i></p>
<dd> Set the next frame&#8217;s name to <i>text</i>. This name is stored as an extension in the output GIF (extension number 0xCE, followed by the characters of the frame name). <code>&#8211;no-names</code> removes name extensions from the input images.</dl>
<h3>Animation Options</h3>
<p> Animation options apply to GIF animations, or to individual frames in GIF animations. As with image options, most animation options have three forms, &#8216;<code>&#8211;X</code>&#8216;, &#8216;<code>&#8211;no-X</code>&#8216;, and &#8216;<code>&#8211;same-X</code>&#8216;, and you can give animation options multiple times; for example,</p>
<dl>
<dt>
<dd>
<pre>
<code>gifsicle -b a.gif -d50 &quot;#0&quot; &quot;#1&quot; -d100 &quot;#2&quot; &quot;#3&quot;</code>
</pre>
</dl>
<p> sets the delays of frames 0 and 1 to 50, and frames 2 and 3 to 100. </p>
<dl>
<dt> <i></i><code>-d </code><i>time</i><i></i><i></i></p>
<dd>
<dt> <i></i><code>&#8211;delay </code><i>time</i><i></i><i></i></p>
<dd> Set the delay between frames to <i>time</i> in hundredths of a second. </p>
<dt> <i></i><code>-D </code><i>method</i><i></i><i></i></p>
<dd>
<dt> <i></i><code>&#8211;disposal </code><i>method</i><i></i><i></i></p>
<dd> Set the disposal method for the following frames to <i>method</i>. A frame&#8217;s disposal method determines how a viewer should remove the frame when it&#8217;s time to display the next. <i>Method</i> can be a number between 0 and 7 (although only 0 through 3 are generally meaningful), or one of these names: <code>none</code> (leave the frame visible for future frames to build upon), <code>asis</code> (same as &quot;none&quot;), <code>background</code> (or <code>bg</code>) (replace the frame with the background), or <code>previous</code> (replace the frame with the area from the previous displayed frame). <code>&#8211;no-disposal</code> means <code>&#8211;disposal</code>=<code>none</code>. </p>
<dt> <code>-l</code>[<i>count</i>]</p>
<dd>
<dt> <code>&#8211;loopcount</code>[=<i>count</i>]</p>
<dd> Set the Netscape loop extension to <i>count</i>. <i>Count</i> is an integer, or <code>forever</code> to loop endlessly. If you supply a <code>&#8211;loopcount</code> option without specifying <i>count</i>, Gifsicle will use <code>forever</code>. <code>&#8211;no-loopcount</code> (the default) turns off looping. </p>
<p> Set the loop count to one less than the number of times you want the animation to run. An animation with <code>&#8211;no-loopcount</code> will show every frame once; <code>&#8211;loopcount</code>=1 will loop once, thus showing every frame twice; and so forth. Note that <code>&#8211;loopcount</code>=0 is equivalent to <code>&#8211;loopcount</code>=forever, not <code>&#8211;no-loopcount</code>. </p>
<dt> <code>-O</code>[<i>level</i>]</p>
<dd>
<dt> <code>&#8211;optimize</code>[=<i>level</i>]</p>
<dd> Optimize output GIF animations for space. <i>Level</i> determines how much optimization is done; higher levels take longer, but may have better results. There are currently three levels: </p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>-O1</code></p>
<dd> Stores only the changed portion of each image. This is the default.</p>
<dt> <code>-O2</code></p>
<dd> Also uses transparency to shrink the file further.</p>
<dt> <code>-O3</code></p>
<dd> Try several optimization methods (usually slower, sometimes better results). </p>
</dl>
<p> Other optimization flags provide finer-grained control. </p>
<dl>
<dt> <code>-Okeep-empty</code></p>
<dd> Preserve empty transparent frames (they are dropped by default). </p>
</dl>
<p> You may also be interested in other options for shrinking GIFs, such as <code>-k</code> and <code>&#8211;no-extensions</code>.</dl>
<dt> <i></i><code>-U </code><i></i><i></i><i></i></p>
<dd>
<dt> <i></i><code>&#8211;unoptimize </code><i></i><i></i><i></i></p>
<dd> Unoptimize GIF animations into an easy-to-edit form. </p>
<p> GIF animations are often optimized (see <code>&#8211;optimize</code>) to make them smaller and faster to load, which unfortunately makes them difficult to edit. <code>&#8211;unoptimize</code> changes optimized input GIFs into unoptimized GIFs, where each frame is a faithful representation of what a user would see at that point in the animation.</dl>
<h3>Image Transformation Options</h3>
<p> Image transformation options apply to entire GIFs as they are read or written. They can be turned off with &#8216;<code>&#8211;no-option</code>&#8216;. </p>
<dl>
<dt> <i></i><code>&#8211;resize </code><i>width</i>x<i>height</i><i></i></p>
<dd> Resize the output GIF to <i>width</i>x<i>height</i>. Either <i>width</i> or <i>height</i> may be an underscore &#8216;_&#8217;. If the argument is <i>width</i>x_, then the output GIF is scaled to <i>width</i> pixels wide without changing its aspect ratio. An analogous operation is performed for _x<i>height</i>. Resizing happens after all input frames have been combined and before optimization. Resizing uses logical screen dimensions; if the input stream has an unusual logical screen (many GIF displayers ignore logical screens), you may want to provide <code>&#8211;no-logical-screen</code> (or <code>+S</code>) to reset it so <code>gifsicle</code> uses image dimensions instead. See also <code>&#8211;resize-method</code>. </p>
<dt> <i></i><code>&#8211;resize-width </code><i>width</i><i></i><i></i></p>
<dd>
<dt> <i></i><code>&#8211;resize-height </code><i>height</i><i></i><i></i></p>
<dd> Like <i></i><code>&#8211;resize </code><i>width</i>x_<i></i><i></i> and <i></i><code>&#8211;resize </code><i></i>_x<i>height</i><i></i> respectively. </p>
<dt> <i></i><code>&#8211;resize-fit </code><i>width</i>x<i>height</i><i></i></p>
<dd> Like <code>&#8211;resize</code>, but resizes the output GIF to fit <i>within</i> a rectangle with dimensions <i>width</i>x<i>height</i>. The GIF&#8217;s aspect ratio remains unchanged. No resize is performed if the GIF already fits within the given rectangle. Either <i>width</i> or <i>height</i> may be an underscore &#8216;_&#8217;, which is treated as infinity. </p>
<dt> <i></i><code>&#8211;resize-fit-width </code><i>width</i><i></i><i></i></p>
<dd>
<dt> <i></i><code>&#8211;resize-fit-height </code><i>height</i><i></i><i></i></p>
<dd> Like <i></i><code>&#8211;resize-fit </code><i>width</i>x_<i></i><i></i> and <i></i><code>&#8211;resize-fit </code><i></i>_x<i>height</i><i></i> respectively. </p>
<dt> <i></i><code>&#8211;scale </code><i>Xfactor</i>[x<i>Yfactor</i>]<i></i></p>
<dd> Scale the output GIF&#8217;s width and height by <i>Xfactor</i> and <i>Yfactor</i>. If <i>Yfactor</i> is not given, it defaults to <i>Xfactor</i>. Scaling happens after all input frames have been combined and before optimization. </p>
<dt> <i></i><code>&#8211;resize-method </code><i>method</i><i></i><i></i></p>
<dd> Set the method used to resize images. The &#8216;sample&#8217; method runs very quickly, but when shrinking images, it produces noisy results. The &#8216;mix&#8217; method is somewhat slower, but produces better-looking results. The default method is currently &#8216;mix&#8217;.</p>
<dl>
<dt>
<dd>
<p> Details: The resize methods differ most when shrinking images. The &#8216;sample&#8217; method is a point sampler. Each pixel position in the output image maps to exactly one pixel position in the input, so when shrinking, full rows and columns from the input are dropped. The other methods use all input pixels, which generally produces better-looking images. The &#8216;box&#8217; method, a box sampler, is faster than the more complex filters and produces somewhat sharper results, but there will be anomalies when shrinking images by a small amount in one dimension. (Some output pixels will correspond to exactly 1 input row or column, while others will correspond to exactly 2 input rows or columns.) The &#8216;mix&#8217; method is a full bilinear interpolator. This is slower and produces somewhat blurrier results, but avoids such anomalies. </p>
<p> Gifsicle also supports several complex resamplers, including Catmull-Rom cubic resampling (&#8216;catrom&#8217;), the Mitchell-Netravali filter (&#8216;mitchell&#8217;), a 2-lobed Lanczos filter (&#8216;lanczos2&#8217;), and a 3-lobed Lanczos filter (&#8216;lanczos3&#8217;). These filters are slower still, but can give sharper, better results.</dl>
<dt> <i></i><code>&#8211;resize-colors </code><i>n</i><i></i><i></i></p>
<dd> Allow Gifsicle to add intermediate colors when resizing images. Normally, Gifsicle&#8217;s resize algorithms use input images&#8217; color palettes without changes. When shrinking images with very few colors (e.g., pure black-and-white images), adding intermediate colors can improve the results. Example: <i></i><code>&#8211;resize-colors </code><i>64</i><i></i><i></i> allows Gifsicle to add intermediate colors for images that have fewer than 64 input colors.</dl>
<h3>Color Options</h3>
<p> Color options apply to entire GIFs as they are read or written. They can be turned off with &#8216;<code>&#8211;no-option</code>&#8216;. </p>
<dl>
<dt> <i></i><code>-k </code><i>num</i><i></i><i></i></p>
<dd>
<dt> <i></i><code>&#8211;colors </code><i>num</i><i></i><i></i></p>
<dd> Reduce the number of distinct colors in each output GIF to <i>num</i> or less. <i>Num</i> must be between 2 and 256. This can be used to shrink output GIFs or eliminate any local color tables. </p>
<p> Normally, an adaptive group of colors is chosen from the existing color table. You can affect this process with the <code>&#8211;color-method</code> option or by giving your own colormap with <code>&#8211;use-colormap</code>. Gifsicle may need to add an additional color (making <i>num</i>+1 in all) if there is transparency in the image. </p>
<dt> <i></i><code>&#8211;color-method </code><i>method</i><i></i><i></i></p>
<dd> Determine how a smaller colormap is chosen. &#8216;<code>diversity</code>&#8216;, the default, is <code><a href="/docs/linux/man/1-xv/">xv</a></code>(1)&#8217;s diversity algorithm, which uses a strict subset of the existing colors and generally produces good results. &#8216;<code>blend-diversity</code>&#8216; is a modification of this: some color values are blended from groups of existing colors. &#8216;<code>median-cut</code>&#8216; is the median cut algorithm described by Heckbert. <code>&#8211;method</code> is a synonym for <code>&#8211;color-method</code>. </p>
<dt> <i></i><code>-f </code><i></i><i></i><i></i></p>
<dd>
<dt> <code>&#8211;dither</code>[=<i>method</i>]</p>
<dd> When <code>&#8211;dither</code> is on and the colormap is changed, combinations of colors are used to approximate missing colors. This looks better, but makes bigger files and can cause animation artifacts, so it is off by default. </p>
<p> Specify a dithering algorithm with the optional <i>method</i> argument. The default, &#8216;<code>floyd-steinberg</code>&#8216;, uses Floyd-Steinberg error diffusion. This usually looks best, but can cause animation artifacts, because dithering choices will vary from frame to frame. Gifsicle also supports ordered dithering algorithms that avoid animation artifacts. The &#8216;<code>ro64</code>&#8216; mode uses a large, random-looking pattern and generally produces good results. The &#8216;<code>o3</code>&#8216;, &#8216;<code>o4</code>&#8216;, and &#8216;<code>o8</code>&#8216; modes use smaller, more regular patterns. The &#8216;<code>ordered</code>&#8216; mode chooses a good ordered dithering algorithm. For special effects, try the halftone modes &#8216;<code>halftone</code>&#8216;, &#8216;<code>squarehalftone</code>&#8216;, and &#8216;<code>diagonal</code>&#8216;. Some modes take optional parameters using commas. The halftone modes take a cell size and a color limit: &#8216;<code>halftone,10,3</code>&#8216; creates 10-pixel wide halftone cells where each cell uses up to 3 colors. </p>
<dt> <i></i><code>&#8211;gamma </code><i>gamma</i><i></i><i></i></p>
<dd> Set the gamma correction to <i>gamma</i>, which can be a real number or &#8216;<code>srgb</code>&#8216;. Roughly speaking, higher numbers exaggerate shadows and lower numbers exaggerate highlights. The default is the function defined by the standard sRGB color space, which usually works well. (Its effects are similar to <code>&#8211;gamma</code>=2.2.) Gifsicle uses gamma correction when choosing a color palette (<code>&#8211;colors</code>) and when dithering (<code>&#8211;dither</code>). </p>
<dt> <i></i><code>&#8211;change-color </code><i>color1</i> <i>color2</i><i></i></p>
<dd> Change <i>color1</i> to <i>color2</i> in the following input GIFs. (The <i>color</i> arguments have the same forms as in the <code>-t</code> option.) Change multiple colors by giving the option multiple times. Color changes don&#8217;t interfere with one another, so you can safely swap two colors with &#8216;<code>&#8211;change-color</code><i> color1 color2</i><code> &#8211;change-color</code><i> color2 color1</i>&#8216;. They all take effect as an input GIF is read. <code>&#8211;no-change-color</code> cancels all color changes. </p>
<dt> <i></i><code>&#8211;transform-colormap </code><i>command</i><i></i><i></i></p>
<dd> <i>Command</i> should be a shell command that reads from standard input and writes to standard output. Each colormap in the output GIF is translated into text colormap format (see <code>&#8211;use-colormap</code> below) and piped to the command. The output that command generates (which should also be in text colormap format) will replace the input colormap. The replacement doesn&#8217;t consider color matching, so pixels that used color slot <i>n</i> in the input will still use color slot <i>n</i> in the output. </p>
<dt> <i></i><code>&#8211;use-colormap </code><i>colormap</i><i></i><i></i></p>
<dd> Change the image to use <i>colormap</i>. Each pixel in the image is changed to the closest match in <i>colormap</i> (or, if <code>&#8211;dither</code> is on, to a dithered combination of colors in <i>colormap</i>). <i>Colormap</i> can be <code>web</code> for the 216-color &#8220;Web-safe palette&#8221;; <code>gray</code> for grayscale; <code>bw</code> for black-and-white; or the name of a file. That file should either be a text file (the format is described below) or a GIF file, whose global colormap will be used. If </i><code>&#8211;colors=<i>N</code> is also given, an <i>N</i>-sized subset of <i>colormap</i> will be used. </p>
<p> Text colormap files use this format: </p>
<dl>
<dt>
<dd>
<pre><code>
;
each non - comment line represents one color, "red green blue";
each component should be between 0 and 255 0 0 0;
like this 255 255 255;
or use web hex notation
#ffffff; like this
</code></pre>
</dl>
</dl>
<h2>EXAMPLES</h2>
<p> First, let&#8217;s create an animation, &#8216;anim.gif&#8217;: </p>
<dl>
<dt>
<dd>
<pre>
<code>gifsicle a.gif b.gif c.gif d.gif &gt; anim.gif</code>
</pre>
</dl>
<p> This animation will move very quickly: since we didn&#8217;t specify a delay, a browser will cycle through the frames as fast as it can. Let&#8217;s slow it down and pause .5 seconds between frames, using the <code>&#8211;delay</code> option. </p>
<dl>
<dt>
<dd>
<pre>
<code>gifsicle --delay 50 a.gif b.gif c.gif d.gif &gt; anim.gif</code>
</pre>
</dl>
<p> If we also want the GIF to loop three times, we can use <code>&#8211;loopcount</code>: </p>
<dl>
<dt>
<dd>
<pre>
<code>gifsicle -d 50 --loop=3 a.gif b.gif c.gif d.gif &gt; anim.gif</code>
</pre>
</dl>
<p> (Rather than type <code>&#8211;delay</code> again, we used its short form, <code>-d</code>. Many options have short forms; you can see them by running &#8216;<code>gifsicle &#8211;help</code>&#8216;. We also abbreviated <code>&#8211;loopcount</code> to <code>&#8211;loop</code>, which is OK since no other option starts with &#8216;loop&#8217;.) </p>
<p> To explode &#8216;anim.gif&#8217; into its component frames: </p>
<dl>
<dt>
<dd>
<pre>
<code>gifsicle --explode anim.gif</code>
<br>
<code>ls anim.gif*</code>
<br>
anim.gif  anim.gif.000  anim.gif.001  anim.gif.002  anim.gif.003
</pre>
</dl>
<p> To optimize &#8216;anim.gif&#8217;: </p>
<dl>
<dt>
<dd>
<pre>
<code>gifsicle -b -O2 anim.gif</code>
</pre>
</dl>
<p> To change the second frame of &#8216;anim.gif&#8217; to &#8216;x.gif&#8217;: </p>
<dl>
<dt>
<dd>
<pre>
<code>gifsicle -b --unoptimize -O2 anim.gif --replace &quot;#1&quot; x.gif</code>
</pre>
</dl>
<p> <code>&#8211;unoptimize</code> is used since &#8216;anim.gif&#8217; was optimized in the last step. Editing individual frames in optimized GIFs is dangerous without <code>&#8211;unoptimize</code>; frames following the changed frame could be corrupted by the change. Of course, this might be what you want. </p>
<p> Note that <code>&#8211;unoptimize</code> and <code>&#8211;optimize</code> can be on simultaneously. <code>&#8211;unoptimize</code> affects <i>input</i> GIF files, while <code>&#8211;optimize</code> affects <i>output</i> GIF files. </p>
<p> To print information about the first and fourth frames of &#8216;anim.gif&#8217;: </p>
<dl>
<dt>
<dd>
<pre>
<code>gifsicle -I &quot;#0&quot; &quot;#3&quot; &lt; anim.gif</code>
</pre>
</dl>
<p> To make black the transparent color in all the GIFs in the current directory, and also print information about each: </p>
<dl>
<dt>
<dd>
<pre>
<code>gifsicle -bII --trans &quot;#000000&quot; *.gif</code>
</pre>
</dl>
<p> Giving <code>-I</code> twice forces normal output to occur. With only one <code>-I</code>, the GIFs would not be modified. </p>
<p> To change &#8216;anim.gif&#8217; to use a 64-color subset of the Web-safe palette: </p>
<dl>
<dt>
<dd>
<pre>
<code>gifsicle -b --colors=64 --use-col=web anim.gif</code>
</pre>
</dl>
<p> To make a dithered black-and-white version of &#8216;anim.gif&#8217;: </p>
<dl>
<dt>
<dd>
<pre>
<code>gifsicle --dither --use-col=bw anim.gif &gt; anim-bw.gif</code>
</pre>
</dl>
<p> To overlay one GIF atop another &#8212; producing a one-frame output GIF that looks like the superposition of the two inputs &#8212; use <code>gifsicle</code> twice: </p>
<dl>
<dt>
<dd>
<pre>
<code>gifsicle bottom.gif top.gif | gifsicle -U &quot;#1&quot; &gt; result.gif</code>
</pre>
</dl>
<h2>BUGS</h2>
<p> Some optimized output GIFs may appear incorrectly on some GIF implementations (for example, Java&#8217;s); see the <code>&#8211;careful</code> option. </p>
<p> Please email suggestions, additions, patches and bugs to ekohler [at] gmail.com.</p>
<h2>SEE ALSO</h2>
<p> For a tutorial on GIF images and animations, you might try some of the resources listed on-line at webreference.com:<br />
 <a rel="nofollow" href="http://www.webreference.com/authoring/graphics/animation.html">http://www.webreference.com/authoring/graphics/animation.html</a></p>
<h2>AUTHORS</h2>
<p> Eddie Kohler &lt;ekohler [at] gmail.com&gt;<br />
 <a rel="nofollow" href="http://www.read.seas.harvard.edu/~kohler/">http://www.read.seas.harvard.edu/~kohler/</a><br />
 He wrote it. </p>
<p> Anne Dudfield &lt;annied [at] frii.com&gt;<br />
 <a rel="nofollow" href="http://www.frii.com/~annied/">http://www.frii.com/~annied/</a><br />
 She named it. </p>
<p> Hans Dinsen-Hansen &lt;dino [at] danbbs.dk&gt;<br />
 <a rel="nofollow" href="http://www.danbbs.dk/~dino/">http://www.danbbs.dk/~dino/</a><br />
 Adaptive tree method for GIF writing. </p>
<p> <a rel="nofollow" href="http://www.lcdf.org/gifsicle/">http://www.lcdf.org/gifsicle/</a><br />
 The <code>gifsicle</code> home page. </p>
<h2>Index</h2>
