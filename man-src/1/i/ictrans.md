---
title: "ictrans(1)"
name: "ictrans"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ictrans/"
description: "ictrans – interactive NCAR CGM translator ctrans"
---

<h2>NAME</h2>
<p> ictrans &#8211; interactive NCAR CGM translator <code>ctrans</code></p>
<h2>SYNOPSIS</h2>
<p> <code>ictrans</code> [ <code>-d</code><i> device</i> ] [ <code>-font</code><i> font</i> ] [ <code>-e</code><i> script</i> ]* [ <code>-soft</code> ] [ <code>-bell</code> ] [ <code>-lmin</code><i> min</i> ] [ <code>-lmax</code><i> max</i> ] [ <code>-lscale</code><i> scale</i> ] [ <code>-pal</code><i> pal_fname</i> ] [ <code>-Version</code> ] [ <code>-wid</code><i> window_id</i> ] [ <i>device-specific options</i> ] <i>metafile</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>ictrans</code> is the user interface to the Computer Graphics Metafile (<font SIZE="-1">CGM</font>) translator <code>ctrans.</code> <code>ictrans </code> will enter command interpreter mode upon invocation and await instructions from the user. When waiting for commands from the user, <code>ictrans</code> displays the prompt `<code>ictrans&gt;</code>&#8216;. </p>
<p> Upon invocation <code>ictrans </code> performs a configuration of its spooled device table. The table is configured by processing several sources. <code>ictrans </code> first searches for the file <code>ncarv_spool</code> in the $NCARG_ROOT/lib/ncarg directory. If the file exists <code>ictrans</code> will load it into the spooled device table. Next, ictrans searches for the file <code>.ncarv_spool</code> in the user&#8217;s home directory. If found, its contents are merged into the spooler table. Finally, the NCARV_SPOOL environment variable may contain the definition for a single spooler. If this variable is set, its contents also are merged into the table. Each entry in the above set of sources is identified by a name. If a conflict in names exists then the last entry encountered takes precedence. i.e. the previous entry of the same name is overridden.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-bell</code></p>
<dd> Ring the bell at the end of each frame. The default is to run in silent mode. This option is not supported by all devices.</p>
<dt><code>-d</code><i> device</i></p>
<dd> Device name. <code>ictrans</code> will use the <i>Graphcap</i> (if it exists) or the appropriate graphics library indicated by <i>device;</i></p>
<dt>
<dd> If <i>device</i> is preceded by a UNIX directory path then <code>ictrans</code> will look in that directory for the specified graphcap. Otherwise <code>ictrans</code> searches the directory $NCARG_ROOT/lib/ncarg/graphcaps for the graphcap.</p>
<dt>
<dd> For all device specifications except <code>X11</code> output is directed to standard out. In the case of <code>X11</code> translation results in appropriate calls to the X11 libraries. See <code>graphcap(5NCARG)</code> for a description of supported devices. See <code>gcaps(1NCARG)</code> for a list of devices supported by <i>your </i> particular configuration of <code>ctrans</code>.</p>
<dt>
<dd> This option overrides the <code>GRAPHCAP</code> environment variable.</p>
<dt><code>-e</code><i> script</i></p>
<dd> <i>script</i> is a single <code>ictrans</code> command. The valid <code>ictrans</code> commands are discussed in the <code>COMMANDS</code> section below. Multiple <code>-e</code> options may appear on a single command line. Be careful to use quotes if your command contains spaces or metacharacters that might be interpreted by the shell. When this option is used <code>ictrans</code> does not enter interactive mode. It simply performs the given commands and then exits.</p>
<dt><code>-font</code><i> fontcap</i></p>
<dd> Fontcap file to be used for stroking text. When interpreting CGM <code>TEXT</code> command elements use <i>fontcap</i> as the default font for textual translation. Note: CGMs may contain textual descriptions which are not embedded in CGM <code>TEXT</code> elements. Hence they are not influenced by <i>fontcap</i> specifications. Note also that a CGM may explicitly specify a named font which may override a font provided on the command line. The environment variable FONTCAP may also be used to specify a default fontcap.</p>
<dt>
<dd> If <i>fontcap</i> is preceded by a UNIX directory path then <code>ictrans</code> will look in that directory for the specified fontcap. Otherwise <code>ictrans</code> searches the directory $NCARG_ROOT/lib/ncarg/fontcaps for the fontcap.</p>
<dt>
<dd> See <code>fontcap(5NCARG)</code> for a description of the available fontcaps. See <code>fcap(1NCARG)</code> for a list of the fontcaps installed on your system.</p>
<dt>
<dd> This option overrides the <code>FONTCAP</code> environment variable.</p>
<dt><code>-lmin</code><i> min</i></p>
<dd> On devices which support line width scaling all lines are guaranteed to be scaled at least <i>min</i> times the default line width for that device. This option effectively insures that the minimum value for the CGM element &quot;LINE WIDTH&quot; is <i>min</i>.</p>
<dt><code>-lmax</code><i> max</i></p>
<dd> On devices which support line width scaling all lines are guaranteed to be scaled at most <i>max</i> times the default line width for that device. This option effectively insures that the maximum value for the CGM element &quot;LINE WIDTH&quot; is <i>max</i>. The results of setting <i>max</i> less then <i>min</i> are undefined.</p>
<dt><code>-lscale</code><i> scale</i></p>
<dd> On devices which support line width scaling all line width specifications within the metafile will be scaled by <code>scale</code>. will be scaled <i>scale</i> This option is subject to modification by the <code>-lmin</code> and <code>-lmax</code> options.</p>
<dt><code>-pal</code><i> pal_fname</i></p>
<dd> Use the color palette defined in the file <i>pal_fname</i> for subsequent translation of the metafile. This palette will override any color map defined by the CGM being translated. For a description of the format of <i>pal_fname</i> see ras_palette(5NCARG).</p>
<dt><code>-soft</code></p>
<dd> Unconditionally perform software filling of all filled polygons. This option may be useful for devices which have limits on the number of vertices describing a polygon. On some devices this number is known and software filling is performed, as appropriate, without user specification.</p>
<dt><code>-Version</code></p>
<dd> Print the version number and then exit.</dl>
<h2>DEVICE SPECIFIC OPTIONS</h2>
<p> <code>ictrans</code> accepts an identical set of device-specific options to that of <code>ctrans.</code> For a description of the device-specific options see <code>ctrans(1NCARG)</code>.</p>
<h2>COMMANDS</h2>
<h3>Command Structure</h3>
<p> <code>ictrans </code> commands have a simple and regular structure. Commands which operate directly on the metafile being processed may be preceded by a <i>frame_list</i> which designate the frames to which the command applies. Some commands accept arguments. Anything following a command name is regarded as an argument:</p>
<dl>
<dt>
<dd>
<dl>
<dt> ( <i>frame </i>[ <code> ,</code><i>frame</i> ])* <i>command </i>(<i> argument</i> )*</p>
<dd></dl>
</dl>
<dd>A comma-separated pair of frames implies the inclusive list of frames. If a frame list is omitted and a command requires a frame then the current frame is used as the default. If no argument list is specified and one is required then a default argument is used whenever possible. </p>
<p> For example, the command <code>1,5 8 save</code> <i>/tmp/foo</i> would write the first through fifth and the eighth frame of the metafile to the file <i>/tmp/foo</i>. </p>
<p> Commands will ignore any unexpected arguments. Command names may be abbreviated up to the point that they are unique.</p>
<h3>Frame Lists</h3>
<p> Frames can be addressed in several ways:</p>
<dl>
<dt><i>nnn</i></p>
<dd> By frame number. Frames are assigned a relative number from first to last in the metafile. The first frame is numbered <i>1</i>.</p>
<dt><code>$</code></p>
<dd> The last frame in the file.</p>
<dt><code>.</code></p>
<dd> The current frame. <code>ictrans</code> keeps track of the last frame upon which an operation was performed. This frame is called the &quot;current frame&quot;.</p>
<dt><i>frame</i><code>+-</code><i>n</i></p>
<dd> A frame number followed by a plus sign (<code>+</code>) or a minus sign (<code>&#8211;</code>), followed by a decimal number, specifies the frame plus or minus the indicated number of frames. <i>frame</i> may be omitted in which case the current frame is assumed. For example, `<code>10</code>+2<code>&#8216;</code> addresses frame 12 in the metafile.</dl>
<h3>Commands</h3>
<dl>
<dt> <code>!</code> command</p>
<dd>
<dd>Run <i>command </i> as a shell command on the local machine.</p>
<dt> <code>alias</code> [ <i>name</i> [ <i>def</i> ] ]</p>
<dd>
<dd>Assign <i>def</i> to the alias <i>name</i>. If <i>def</i> is omitted, the alias <i>name</i> is displayed along with its current definition. If both <i>name</i> and <i>def</i> are omitted, all aliases are displayed. <i>def </i> is of the form: </p>
<p> <code>:</code> <code>[</code><i> ctrans_args </i><code>]</code> <code>:</code> <code>[</code><i> filter_chain </i><code>]</code> </p>
<p> where <i>ctrans_args</i> is list of command line arguments for the metafile translator <code>ctrans </code> and <i>filter_chain</i> is a set of simple commands separated by <code>|</code>. <i>filter_chain </i> may be terminated by <code>&gt; </code> or <code>&gt;&gt;</code> <i>filename</i>. For example: </p>
<p> <code> ictrans&gt; alias </code><i>name1</i> : -d xwd : | cat &gt; <i>outfile</i> </p>
<p> or </p>
<p> <code> ictrans&gt; alias </code><i>name2</i> : -d ps.mono : | <i>filter1</i> | lpr </p>
<dt> <code>dup</code> <code>[</code><i>number</i><code>]</code></p>
<dd>
<dd>This command is used to set the number of times each frame is displayed during subsequent plotting. The default is one. If <code>dup</code> is invoked without any arguments the current value of dup is returned.</p>
<dt> <code>count</code></p>
<dd>
<dd>Reports number of frames contained in the file.</p>
<dt> <code>current</code></p>
<dd>
<dd>Reports the current frame.</p>
<dt> <code>file</code> <code>[</code><i> metafile ]</i></p>
<dd>
<dd>The file <i>metafile</i> will be used for subsequent translation. <code>ictrans </code> uses the shell defined by the environment variable <code>SHELL</code> (/bin/sh by default) to perform filename substitution on <i>metafile</i>. The rules governing filename substitution are as defined by the working shell. If no argument is given the current metafile name is reported.</p>
<dt> <code>font</code> <code>[</code><i> font </i><code>]</code></p>
<dd>
<dd>Set the fontcap to <i>font</i> for future translation. This function is identical to that of the <code>-font</code> option. If <i>font</i> is omitted the current fontcap name is reported.</p>
<dt> <code>help</code> <code>[</code><i> command </i><code>]</code></p>
<dd>
<dd>Print a usage statement for <i>command</i>. If <i>command</i> is omitted a brief description of all commands is given.</p>
<dt> <code>[</code><i> frames </i><code>]</code> <code>list</code></p>
<dd>
<dd>Provide brief information about each metafile frame in <i>frames</i>. If <i>frames</i> is omitted then the current frame is used. If <i>frames </i> is omitted and the current frame is not the last frame then the current frame is incremented to the next frame in the metafile.</p>
<dt> <code>&lt;</code><i> frame1 </i><code>&gt;</code> <code>&lt;</code><i> frame2 </i><code>&gt;</code> <code>merge</code></p>
<dd>
<dd>Plot frame number <i>frame1</i> and then plot frame number <i>frame2</i> over the first frame without clearing the device. The result is a &quot;merge&quot; of the two plots. The current frame is not changed. There are no defaults for <i>frame1</i> or <i>frame2</i>. The resulting plot might not be what was expected. Attributes from the first frame, such as color, may override attributes in the second frame.</p>
<dt> <code>loop</code></p>
<dd>
<dd>Toggle loop mode on or off. When loop mode is on subsequent <code>plot</code> commands will cause the requested frames to be plotted and then <code>ictrans </code> will proceed to either the first frame in the defined segment or the last and repeatedly display the first through last (last through first) frames. Looping continues until an interrupt signal is received. The determination of which order to loop, forwards or backwards, is made as follows: If the last group of frames plotted was in ascending order loop forward. If the last group of frames plotted was in descending order loop backwards. If the order cannot be determined don&#8217;t loop. For example; if loop mode is set &quot;1 3,4 plot&quot; will result in forward looping, &quot;1 4,3 plot&quot; will result in backward looping, and &quot;3,4 1 plot&quot; will result in no looping because the last group of frames plotted, &quot;1&quot;, is a single frame.</p>
<dt> <code>movie</code> <code>[</code><i> time ]</i></p>
<dd>
<dd>Display each frame for <i>time</i> seconds before proceding to the next frame during subsequent plots. If <i>time</i> is omitted then movie mode is toggled off or on. In the case the movie mode is toggled on the default time is zero seconds. If movie mode is toggled to off a newline must be received before advancing to the next frame during plotting.</p>
<dt> <code>next</code></p>
<dd>
<dd>Multiple files may be specified on the <code>ictrans</code> command line. To edit the next file in the argument list use the <code>next </code> command.</p>
<dt> <code>[</code><i> frames </i><code>]</code> <code>plot</code></p>
<dd>
<dd>Plot the addressed frames. If <i>frames</i> is omitted then the current frame is plotted and if possible, the current frame number is incremented. If &quot;movie&quot; mode is set <code>ictrans </code> will wait <i>time </i> seconds after displaying each plot before continuing. <i>time</i> is set with the <code>movie </code> command. If &quot;movie&quot; mode is not set <code>ictrans</code> will wait for a newline character before advancing to the next frame. <code>plot </code> will report the number of frames and the last frame in <i>frames</i>. Plotting will be terminated and <code>ictrans </code> will reenter command mode after the last frame is plotted or upon receiving a interrupt signal, SIGINT.</p>
<dt> <code>[</code><i> frames </i><code>]</code> <code>Print</code></p>
<dd>
<dd>The addressed frames are translated and sent to the current spooling device. Translation is performed by a spawned translator. The <code>spooler</code> command may be used to select a spooling device. See <code>ncarv_spool(5NCARG).</code></p>
<dt> <code>quit</code></p>
<dd>
<dd>Terminate the session.</p>
<dt> <code>[</code><i> frames </i><code>]</code> <code>save</code> <code>[</code><i> metafile </i><code>]</code></p>
<dd>
<dd>Save the addressed frames to <i>metafile</i>. If <i>metafile</i> does not exist then it is created. Filename substitution is performed on <i>metafile</i>. If <i>metafile</i> is omitted than the last file saved to is used. If <i>frames</i> is omitted than the current frame is used.</p>
<dt> <code>[</code><i> frames </i><code>]</code> <code>Save</code> <code>[</code><i> metafile </i><code>]</code></p>
<dd>
<dd>Same as the <code>save </code> command except <code>Save</code> does not confirm its actions with the user in the case that the file exists. If the file exists but is not a valid NCGM it is overwritten. If the file exists and is a valid NCGM it is appended to.</p>
<dt> <code>skip</code> <code>[</code><i> number </i><code>]</code></p>
<dd>
<dd>Set number of frames to skip over during subsequent plotting. For example, if &quot;skip&quot; is set to 1 and a request is made to plot frames 1 through 10 frames 1, 3, 5, 7, and 9 will be displayed. With no arguments <code>skip</code> reports its current value. The default is zero.</p>
<dt> <code>spooler</code> <code>[</code><i> spooler_alias </i><code>]</code></p>
<dd>
<dd>With no arguments the current spooler alias name is reported. If <i>spooler_alias</i> is a valid alias either defined by the <code>alias</code> command, or in a <code>ncarv_spool</code> configuration file, or by the NCARV_SPOOL environment variable, then <i>spooler alias </i> becomes the current spooler. Subsequent <code>Print</code> commands will use the spooler definition defined by the current spooler. See <code>ncarv_spool(5NCARG).</code></p>
<dt> <code>[</code><i> start frame </i><code>]</code> <code>start</code></p>
<dd>
<dd>This command defines the first frame in a segment of frames. <code>start,</code> together with the <code>stop</code> command, define the boundaries of a segment of metafile frames. When <code>ictrans</code> is in loop mode the contents of this segment are repeatedly displayed. The default <i>start frame</i> is the first frame in the metafile, 1. If no arguments are given <code>start</code> reports the first frame in the current segment.</p>
<dt> <code>[</code><i> stop frame </i><code>]</code> <code>stop</code></p>
<dd>
<dd>This command defines the last frame in a segment of frames. The default <i>stop frame</i> is the last frame in the metafile, $. If no arguments are given <code>stop </code> reports the last frame in the current segment.</p>
<dt> <code>zoom</code> [ <i>llx</i> [ <i>lly</i> [ <i>urx</i> [ <i>ury</i> ]]]]</p>
<dd>
<dd>The <code>zoom </code> command allows for specification of a workstation window (in the GKS sense). Four coordinates are specified which define a rectangular window which is a subset of the normalized VDC rectangle with corner points (0.0, 0.0) and (1.0, 1,0). The specified window is then mapped onto the entire viewport. For example </p>
<p> <code> ictrans&gt; zoom 0.0 0.0 0.5 0.5 </code> </p>
<p> would result in the lower left quarter of subsequent plots being blown up to fill the entire display. Specification of such a window may be used for zooming and panning.</p>
<dt>
<dd> The range with which one may zoom in on a plot may be limited by the integer addressing precision of the device.</dl>
<h2>EXAMPLES</h2>
<p> The following example shows how <code>ictrans </code> might be used in a batch mode to translate a metafile called <code>gmeta</code> and send the translated results of the entire file to a spooled device called &quot;imagen&quot; which might be defined in the system <code>ncarv_spool</code> file: </p>
<dl>
<dt>
<dd> <code>% ictrans -e &#8216;spooler imagen&#8217; -e &#8216;1,$Print&#8217; gmeta</code> </p>
</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>FONTCAP</code></p>
<dd> Default fontcap specifier.</p>
<dt><code>GRAPHCAP</code></p>
<dd> Default output device specifier.</p>
<dt><code>NCARG_ROOT</code></p>
<dd> Path to root of NCAR Graphics installation.</p>
<dt><code>NCARG_LIB</code></p>
<dd> If set this variable contains the path to the installed NCAR Graphics libraries. <code>NCARG_LIB</code> overrides <code>NCARG_ROOT</code>.</p>
<dt><code>NCARG_TMP</code></p>
<dd> If set, this environment variable contains a directory path to be used for temporary files. On most systems the default is <code>/tmp</code>. On some systems the default is <code>/usr/tmp</code>.</p>
<dt><code>TMPDIR</code></p>
<dd> If <code>NCARG_TMP</code> is not set this environment variable specifies the directory path for scratch disk space. If neither <code>NCARG_TMP </code> <code>TMPDIR</code> is set a site-dependent, hard-coded default is used.</dl>
<h2>FILES</h2>
<dl>
<dt><code>$NCARG_ROOT/lib/ncarg/ncarv_spool</code></p>
<dd> local <code>ictrans</code> spooler config file</p>
<dt><code>~/.ncarv_spool</code></p>
<dd> user&#8217;s <code>ictrans</code> spooler config file</dl>
<h2>SEE ALSO</h2>
<p> <code>ctrans(1NCARG),</code> <code>fcaps(1NCARG),</code> <code>gcaps(1NCARG),</code> <code>idt(1NCARG),</code> <code>med(1NCARG),</code> <code>ncarv_spool(5NCARG)</code> </p>
<p> Hardcopy: NCAR Graphics Fundamentals, UNIX Version</p>
<h2>CAVEATS</h2>
<p> Metafile frames written to an existing file via the <code>save</code> command will be subject to the effects of any global &quot;attribute elements&quot; contained within the file.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research </p>
<p> The use of this Software is governed by a License Agreement. </p>
<h2>Index</h2>
