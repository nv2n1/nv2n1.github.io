---
title: "med(1)"
name: "med"
section: "1"
letter: "m"
url: "/docs/linux/man/1-med/"
description: "med – NCAR CGM metafile frame editor"
---

<h2>NAME</h2>
<p> med &#8211; NCAR CGM metafile frame editor</p>
<h2>SYNOPSIS</h2>
<p> <code>med</code> [ <code>-e</code><i> command</i> ]* [ <code>-f</code><i> sfilename</i> ] [ <code>-l</code><i> local_dir</i> ] [ <code>-V</code> ] [ <i>filename</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>med </code> is a frame-level, metafile editor designed to resemble syntactically <font SIZE="-1">UNIX&#8217;s </font> <code><a href="/docs/linux/man/1-sed/">sed</a></code>(1) and <code><a href="/docs/linux/man/1-ed/">ed</a>(1).</code> <code>med </code> operates on a copy of <i>filename</i>, called a buffer, and overwrites a file only when you issue the <code>w </code> (write) command. <code>med </code> provides line oriented editing commands to display or delete frames from the buffer, to move, copy or merge frames within the buffer, or to write frames from and read frames into the buffer. By default <code>med</code> reads in commands from standard input.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-e</code><i> command</i></p>
<dd> <i>command</i> is a single <code>med</code> command. The valid <code>med</code> commands are discussed in the <code>Commands</code> section below. Multiple <code>-e</code> options may appear on a single command line. Be careful to use quotes if your command contains spaces or metacharacters that might be interpreted by the shell. When this option is used <code>med</code> does not enter interactive mode. It simply performs the given commands and then exits.</p>
<dt><code>-f</code><i> sfilename</i></p>
<dd> Execute the <code>med</code> line-separated list of commands in the file <i>sfilename</i>. After the commands are exhausted <code>med</code> will exit.</p>
<dt><code>-l</code><i> local_dir</i></p>
<dd> Use <i>local_dir </i> as the tmp directory for scratch disk space. If this option is not specified <code>med</code> will use the value of the <i>$NCARG_TMP </i> or the <i>$TMPDIR</i> environment variable. See ncargintro(1ncarg) for a discussion on NCAR Graphics environment variables.</p>
<dt><code>-V</code></p>
<dd> Print the version number and then exit.</dl>
<h2>USAGE</h2>
<h3>Command Structure</h3>
<p> <code>med </code> commands attempt to have a syntactically identical form to those of <code><a href="/docs/linux/man/1-ed/">ed</a></code>(1) or <code><a href="/docs/linux/man/1-sed/">sed</a></code>(1)<code>.</code> Commands consist of an optional <i>address</i> or two optional, comma separated, <i>addresses</i>, followed by a <i>command</i>, which may be abbreviated, possibly followed by a third <i>address</i> or a <i>command</i> specific <i>argument</i> list :</p>
<dl>
<dt>
<dd> [ <i>address</i> [<code>,</code> <i>address</i> ] ] <i>command</i> [ <i>address | args</i> ]</dl>
<p> If only one <i>address</i> is specified, operations are performed on that frame. If two <i>address</i>es are specified, <code>med</code> performs the operation on the inclusive range of frames. If no address is specified then the <i>current</i> frame is used as a default. The exception to this are the <code>w</code> (write) and the <code>a</code> (append) commands. The default address for <code>w</code> is the entire buffer. </p>
<p> For example, <code>1,10p</code> means &#8220;print (display) frame 1 through 10&#8221; (two addresses), <code>d</code> means &#8220;delete the current frame&#8221; (no address implies the current frame used as default), and <code>1,5c5</code> means &#8220;append a copy of frames 1 through 5 at frame 5&#8221; (three addresses). The meaning of <i>argument</i> varies for each operation. In <code>med&#8217;s</code> current state the only valid argument is a filename &#8212; for the write, <code>w ,</code> command for instance, <i>argument </i> is the name of the file to write to. </p>
<p> Unlike its friends <code><a href="/docs/linux/man/1-ed/">ed</a></code>(1) and <code><a href="/docs/linux/man/1-sed/">sed</a></code>(1) <code>med</code> attempts to be fairly user friendly. If an invalid or ambiguous command is given <code>med </code> will tell you so. If <code>med </code> thinks it recognizes a command with invalid arguments a usage statement for the offending command is given. If a particular command fails and <code>med </code> is smart enough to figure out why it will tell you. <code>med </code> will almost ALWAYS immediately terminate when an error occurs while processing commands from a file or the command line. Help is available by using the <code>h </code> command. Usage statements for a particular command may be obtained with: <code>h </code> <i>command name .</i></p>
<h3>Addresses</h3>
<p> Frames can be addressed in several ways:</p>
<dl>
<dt><i>nnn</i></p>
<dd> By frame number. Frames in the buffer are numbered relative to the start of the buffer. The first frame is frame 1.</p>
<dt><code>$</code></p>
<dd> The last frame of the buffer.</p>
<dt><code>.</code></p>
<dd> The current frame. <code>med</code> keeps track of the frame on which you last performed an operation. This frame is called the <i>current frame</i>. You can address this frame by typing a &#8220;dot&#8221; character.</p>
<dt><code>&plusmn;</code><i>n</i></p>
<dd> By relative frame number. Address the frame number that is <i>n</i> frames higher, or <i>n</i> frames lower than the current frame.</p>
<dt><i>address</i><code>&plusmn;</code><i>n</i></p>
<dd> An address followed by a plus sign (<code>+</code>) or a minus sign (<code>&#8211;</code>), followed by a decimal number, specifies that address plus or minus the indicated number of frames. If the address is omitted, the current frame is used as the base. For example, `<code>31-3</code>&#8216; addresses frame 28 in the buffer.</dl>
<p> If you do not specify an address for a command to operate on, a command that requires an address supplies one by default, usually the current frame. </p>
<p> A pair of addresses separated by a comma signifies an inclusive range of frames, and the current frame is not changed unless the command changes it.</p>
<h3>Commands</h3>
<p> Only one command may appear per line. Commands may accept zero, one or two addresses, followed by possibly a third address or an argument. Commands that accept up to two addresses regard a third as an error. Likewise, commands that do not accept an argument regard one as an error. Commands may be abbreviated. </p>
<p> In the absence of a second address for a two or three address command the command will regard the second address as the same as the first. For example, <code>2d</code> is equivalent to <code>2,2d .</code> The absence of a first address, where required, will result in the current frame being used as the default. The same is true in the absence of a required third address. For example, <code>c </code> is equivalent to <code>.,.c.</code>. </p>
<p> The commands <code>q</code> (quit) and <code>e</code> (edit) may be followed by a &#8216;!&#8217; to override <code>med&#8217;s </code> user protection. </p>
<p> In the following list of <code>med</code> commands, the default addresses/arguments appear in parentheses; the parenthesized addresses are not part of the command. Unless otherwise noted a command does not change the current frame number.</p>
<dl>
<dt> (<code>1</code>,<code>$</code>)<code>append</code> <i>metafile</i></p>
<dd>
<dd>Append buffer to a file. Append the addressed frames in the buffer to <i>metafile. </i> If no address is specified the entire buffer is written. If the file does not exist create it.</p>
<dt>(.,.) copy (.)</p>
<dd>
 Copy frames. Duplicate the addressed frames in the buffer and append them after the third address. The current frame becomes the destination of the last frame copied.</p>
<dt>(<code>.</code>,<code>.</code>)<code>delete</code></p>
<dd> Delete the addressed lines from the buffer. <code>delete</code> accepts one or two addresses; the default is the current frame. The current frame is set to the first frame after the deleted frame(s).</p>
<dt><code>edit</code><i> metafile</i></p>
<dd> Edit a metafile. The current contents of the buffer, if any, are erased. The named metafile is read in to the buffer. The resulting current frame is the last frame in the buffer. If changes have been made to the buffer since the last write <code>med </code> will refuse the request unless the command is appended with a &#8216;!&#8217;. <code>edit</code> prints the number of frames in the metafile. If no <i>metafile </i> is given, the current metafile, if any is used. The current frame becomes the last frame in the file.</p>
<dt><code>help</code><i> command</i></p>
<dd> help. Give a usage message for <i>command .</i> If no command is given, print list of command names with a short description of each.</p>
<dt> (<code>.</code>,<code>.</code>)<code>label</code> <i>string</i></p>
<dd>
<dd>Label the addressed frames with <i>string .</i> The <code>CGM</code> <i>Begin Picture</i> element contained in each metafile frame allows for the encoding of character data. <code>label</code> provides a means for accessing this data.</p>
<dt>(<code>.</code>,<code>.</code>)<code>merge</code></p>
<dd> Merge the contents of the second addressed frame on top of the first addressed frame. The first addressed frame is thus changed. The second frame remains the same. The current frame is set to the first addressed frame.</p>
<dt>(.,.) move (.)</p>
<dd>
 Move the addressed frames to the first frame following the third address.</p>
<dt>(<code>.</code>,<code>.</code>)<code>print</code></p>
<dd> Show the contents of the buffer at the given address. What is actually displayed is information regarding the addressed frames. This information includes: relative frame number within the buffer, the number of records contained in the frame, the starting record for the frame and the contents of the <code>CGM element </code> <i>BEGIN PICTURE .</i> If no address is specified the current frame does not change. Otherwise it becomes the last frame printed.</p>
<dt> <code>quit</code></p>
<dd>
<dd>Quit. Terminate the editing session without saving the buffer contents. In order to save the buffer an explicit write must be performed. If changes to the buffer have been made since the last write <code>med</code> will refuse to terminate unless <code>quit</code> is appended with a &#8216;!&#8217;.</p>
<dt> (<code>.</code>)<code>read</code> <i>metafile</i></p>
<dd>
<dd>Read in a metafile. Read the contents of <i>metafile </i> into the buffer and append it at the given address. <i>metafile </i> must be a valid NCAR CGM. The resulting current frame is the last frame read in.</p>
<dt> (1,$)<code>split</code>&lt;number&gt; <i>outfile</i></p>
<dd>
<dd>Split the current metafile into <i>number</i> files. The <code>split</code> command attempts to create <i>number</i> metafiles from the addressed frames, each containing approximately n / number frames where &#8216;n&#8217; is the total number of addressed frames. The first file is named <i>outfile</i>001.ncgm, the second file is named <i>outfile</i>002.ncgm, and so on lexicographically. If no <i>outfile</i> is given, <code>med</code> is used as the default (output files will be called med001.ncgm, med002.ncgm, etc.).</p>
<dt> (1<code>,</code>$<code>)</code>write <i>metafile</i></p>
<dd>
<dd>Write buffer. Write the addressed frames in the buffer to <i>metafile. </i> If no address is specified the entire buffer is written. If the file does not exist create it. If no file name is specified <code>med</code> uses the last currently remembered file name, if any. The currently remembered file name is the file name from the most recent <code>edit</code> command, or the file name <code>med</code> was invoked with if no <code>edit </code> commands have been issued.</p>
<dt><code>!</code><i> command</i></p>
<dd>
 Escape to the shell and execute <i>command.</i> <i>command </i> is a valid UNIX command.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>NCARG_TMP</code></p>
<dd> If set, this environment variable contains a directory path to be used for temporary files. On most systems the default is <code>/tmp</code>.</dl>
<h2>FILES</h2>
<dl>
<dt><code>/tmp/cgm_tools.#</code></p>
<dd> temporary; <i># </i> is the process id. </p>
</dl>
<h2>EXAMPLES</h2>
<p> To concatenate the files <code>ncgm1</code>, <code>ncgm2</code>, and <code>ncgm3 </code> into a single file <code>ncgm123</code> one might use the following: </p>
<dl>
<dt>
<dd> <code>% med -e &#8216;r ncgm1&#8217; -e &#8216;r ncgm2&#8217; -e &#8216;r ncgm3&#8217; -e &#8216;w ncgm123&#8217;</code> </p>
</dl>
<p> Or one could pass the following script to <code>med</code> as a <code>-f</code><i>scriptfile</i> option or enter the commands interactively. </p>
<dl>
<dt>
<dd> r ncgm1<br />
 r ncgm2<br />
 r ncgm3<br />
 w ncgm123 </p>
</dl>
<p> To Overlay the contents of frame <code>5</code> on top of frame <code>4 </code> from a file <code>ncgm1</code> one could execute:</p>
<dl>
<dt>
<dd>
<p> <code>% med -e &#8216;4,5 me&#8217; -e &#8216;w!&#8217; ncgm1</code> </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code>cgm(5NCARG),</code> <i><a href="/docs/linux/man/1-ed/">ed</a>(1),</i> <code><a href="//www.systutorials.com/docs/linux/man/1V-sed/">sed</a>(1V)</code> </p>
<p> Hardcopy: NCAR Graphics Fundamentals, UNIX Version</p>
<h2>BUGS</h2>
<p> <code>med</code><br />
&nbsp;<wbr>does not understand filenames that begin with a digit or a period. </p>
<h2>CAVEATS</h2>
<p> The <code>append, read </code> and <code>merge </code> commands may produce surprising results. A CGM may contain a set of global graphical primitive attributes that are applied to every frame in a file. Thus reading frames in from a file with different global attributes than the current working file may not produce the desired effect. The same is true when appending frames to a previously existing file. Similarly, the CGM standard specifies that graphical attributes specified within a metafile frame affect all succeeding primitives. Thus a frame which is the product of the <code>merge</code> command may appear differently than expected.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research </p>
<p> The use of this Software is governed by a License Agreement. </p>
<h2>Index</h2>
