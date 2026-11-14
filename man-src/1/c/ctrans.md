---
title: "ctrans(1)"
name: "ctrans"
section: "1"
letter: "c"
url: "/docs/linux/man/1-ctrans/"
description: "ctrans – a Computer Graphics Metafile ( CGM ) translator"
---

<h2>NAME</h2>
<p> ctrans &#8211; a Computer Graphics Metafile ( <i>CGM</i> ) translator</p>
<h2>SYNOPSIS</h2>
<p> <code>ctrans</code> [ <code>-bell</code> ] [ <code>-d</code><i> device</i> ] [ <code>-f</code><i> font</i> ] [ <code>-lmin</code><i> min</i> ] [ <code>-lmax</code><i> max</i> ] [ <code>-lscale</code><i> scale</i> ] [ <code>-movie</code><i> time</i> ] [ <code>-outfile</code><i> file</i> ] [ <code>-pal</code><i> pal_fname</i> ] [ <code>-pause</code> ] [ <code>-quiet</code> ] [ <code>-record</code><i> record_num &#8230;</i> ] [ <code>-soft</code> ] [ <code>-verbose</code> ] [ <code>-Version</code> ] [ <code>-viewport</code><i> llx:lly:urx:ury</i> ] [ <code>-wid</code><i> window_id</i> ] [ <code>-window</code><i> llx:lly:urx:ury</i> ] [ <i>device-specific options</i> ] [ <code>&#8211; </code> | <i>metafile &#8230;</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>ctrans</code> is a metafile translator, taking <i>metafile(s),</i> a metafile stored in the <code>NCAR Computer Graphics Metafile (CGM)</code> standard, and interpreting its instructions on the device defined by the GRAPHCAP environment variable. Fonts are stroked according to specifications in the Fontcap file defined by the FONTCAP environment variable. <code>ctrans</code> utilizes <i>Graphcaps</i> by default, see <code>graphcap(5NCARG),</code> while providing optional processing by user provided libraries, if that is required by the device or desired by the user. Thus, <code>ctrans</code> is capable of driving any device for which a <i>Graphcap</i> is available; with programming modifications, <code>ctrans</code> can accommodate any device for which an external library of plotting routines is available. Currently, the following <i>Graphcap</i> independent devices are supported: <code>X11 </code> under release 4 and 5, version 11 of <i>X.</i> </p>
<p> <code>ctrans</code> can also translate metacode into the following raster formats: <code>a60, avs, hdf, hppcl, nrif, sun</code> and <code>xwd</code>. The device specifier for these raster formats is the name of the format. For example &quot;-d xwd&quot; specifies translation to an xwd formatted raster file. Additionally, a clear text driver, &quot;-d CTXT&quot;, is available on any terminal. Not all of the aforementioned devices may be supported by your particular configuration of <code>ctrans</code>. For a list of supported devices see the <code>gcaps(1NCARG)</code> command. </p>
<p> <code>ctrans</code> will read from the standard input if no metafile name is specified or the the name specified is `-&#8216;. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-bell</code></p>
<dd> Ring the bell at the end of each frame. The default is to run in silent mode. This option is not supported by all devices.</p>
<dt><code>-d</code><i> device</i></p>
<dd> Device name. <code>ctrans</code> will use the <i>Graphcap</i> (if it exists) or the appropriate graphics library indicated by <i>device;</i></p>
<dt>
<dd> If <i>device</i> is preceded by a UNIX directory path then <code>ctrans</code> will look in that directory for the specified graphcap. Otherwise <code>ctrans</code> searches the directory $NCARG_ROOT/lib/ncarg/graphcaps for the graphcap.</p>
<dt>
<dd> For all device specifications except <code>X11</code> output is directed to standard out. In the case of <code>X11</code> translation results in appropriate calls to the X11 libraries. See <code>graphcap(5NCARG)</code> for a description of supported devices. See <code>gcaps(1NCARG)</code> for a list of devices supported by <i>your </i> particular configuration of <code>ctrans</code>.</p>
<dt>
<dd> This option overrides the <code>GRAPHCAP</code> environment variable.</p>
<dt><code>-f</code><i> fontcap</i></p>
<dd> Fontcap file to be used for stroking text. When interpreting CGM <code>TEXT</code> command elements use <i>fontcap</i> as the default font for textual translation. Note: CGMs may contain textual descriptions which are not embedded in CGM <code>TEXT</code> elements. Hence they are not influenced by <i>fontcap</i> specifications. Note also that a CGM may explicitly specify a named font which may override a font provided on the command line. The environment variable FONTCAP may also be used to specify a default fontcap.</p>
<dt>
<dd> If <i>fontcap</i> is preceded by a UNIX directory path then <code>ctrans</code> will look in that directory for the specified fontcap. Otherwise <code>ctrans</code> searches the directory $NCARG_ROOT/lib/ncarg/fontcaps for the fontcap.</p>
<dt>
<dd> See <code>fontcap(5NCARG)</code> for a description of the available fontcaps. See <code>fcap(1NCARG)</code> for a list of the fontcaps installed on your system.</p>
<dt>
<dd> This option overrides the <code>FONTCAP</code> environment variable.</p>
<dt><code>-lmin</code><i> min</i></p>
<dd> On devices which support line width scaling all lines are guaranteed to be scaled at least <i>min</i> times the default line width for that device. This option effectively insures that the minimum value for the CGM element &quot;LINE WIDTH&quot; is <i>min</i>.</p>
<dt><code>-lmax</code><i> max</i></p>
<dd> On devices which support line width scaling all lines are guaranteed to be scaled at most <i>max</i> times the default line width for that device. This option effectively insures that the maximum value for the CGM element &quot;LINE WIDTH&quot; is <i>max</i>. The results of setting <i>max</i> less then <i>min</i> are undefined.</p>
<dt><code>-lscale</code><i> scale</i></p>
<dd> On devices which support line width scaling all line width specifications within the metafile will be scaled by <code>scale</code>. This option is subject to modification by the <code>-lmin</code> and <code>-lmax</code> options.</p>
<dt><code>-movie</code><i> time</i></p>
<dd> Set pause to <i>time</i> seconds. In normal operation mode the translator requires user interaction after the display of each plot. <code>ctrans </code> will not proceed until the user responds. If <code>movie</code> mode is set <code>ctrans</code> will wait <i>time</i> seconds after the display of each frame and then proceed automatically. This option and the <code>-pause </code> option are mutually exclusive.</dl>
<p> This option may not behave as expected on slower devices.</p>
<dl>
<dt><code>-outfile</code><i> file</i></p>
<dd> Direct translator output to <i>file</i>. By default translator output is written to the standard output. This option has no effect for devices of which <code>ctrans</code> has a function-callable interface. e.g. <code>X11 .</code></p>
<dt><code>-pal</code><i> pal_fname</i></p>
<dd> Use the color palette defined in the file <i>pal_fname</i> for subsequent translation of the metafile. This palette will override any color map defined by the CGM being translated. For a description of the format of <i>pal_fname</i> see <code>ras_palette(5NCARG)</code>.</p>
<dt><code>-pause</code></p>
<dd> Pause after each frame in the metafile is displayed and wait for the user to type a newline before proceding. This option is probably only useful when used in conjunction with the <code>-wid </code> option as this is the normal behaviour for <code>ctrans</code> in most instances. This option and the <code>-movie </code> option are mutually exclusive.</p>
<dt><code>-quiet</code></p>
<dd> Suppress reporting of non-fatal (warning) error messages; only fatal error messages are reported.</p>
<dt><code>-record </code></p>
<dd> &lt; <i>record_number&#8230; </i> &gt;<br />
 If processing only single frames of the metafile is desired, this option specifies the <i>record number</i> containing the start of that frame. <code>ctrans</code> assumes the processing is to start at the first <code>BEGIN PICTURE</code> element in that record. The user must perform bookkeeping to determine the record that contains the desired frame. Normally, a metafile editor (e.g., <code>ictrans(1NCARG)</code>. may be used as the actual user interface to perform this bookkeeping. Without a specified <i>record number,</i> <code>ctrans</code> processes the entire metafile.</p>
<dt><code>-soft</code></p>
<dd> Unconditionally perform software filling of all filled polygons. This option may be useful for devices which do not support the filled polygon drawing primitive or have limits on the number of vertices describing a polygon. On some devices this number is known and software filling is performed, as appropriate, without user specification.</p>
<dt><code>-verbose</code></p>
<dd> Operate in verbose mode.</p>
<dt><code>-Version</code></p>
<dd> Print the version number and then exit.</p>
<dt><code>-viewport</code><i> llx:lly:urx:ury</i></p>
<dd> Set the viewport of the output device. The viewport is the rectangular region of the output device of which the virtual device coordinate system of the metafile is mapped onto. Normally this region is the largest device-addressable square which fits in the center of the device address space. The <code>-viewport </code> option may be used to change the default mapping. <i>llx</i> and <i>lly</i> specify the lower left corner of the device in normalized coordinates. <i>urx</i> and <i>ury</i> specify the upper right corner of the device in normalized coordinates. For example, <code>-viewport 0.0 0.0 0.5 0.5</code>, specifies the lower left corner of the device.</p>
<dt><code>-window</code><i> llx:lly:urx:ury</i></p>
<dd> Specify the workstation window (in the GKS sense). Four coordinates are specified which define a rectangular window which is a subset of the normalized VDC rectangle with corner points (0,0) and (1.0,1.0). <i>llx</i> and <i>lly</i> specify the lower left corner. <i>urx</i> and <i>.ury </i> specify the upper right corner. The specified window is mapped onto the entire display viewport. For example, if the workstation window is defined by the corner points (0,0) and (0.5 0.5) then the lower left quarter of a plot would be blown up to fill the entire viewport. Specification of such a window can be used for zooming and panning.</p>
<dt>
<dd> The range with which one may zoom in on a plot may be limited by the integer addressing precision of the device.</p>
<dt>
<dd></dl>
<h2>DEVICE-SPECIFIC OPTIONS:</h2>
<p> The following options are available when the device is graphcap-driven (See the <code>gcaps(1NCARG)</code> command for a list of graphcap-driven devices):</p>
<dl>
<dt><code>-simulatebg</code></p>
<dd> Simulate CGM background color requests by drawing a large filled rectangle of the appropriate color. This option is useful for devices such as color PostScript printers which have no concept of background color.</dl>
<p> The following options are available when <i>device</i> is <code>CTXT:</code></p>
<dl>
<dt><code>-Data</code></p>
<dd> Suppress display of <i>CGM output primitive</i> data. All other <i>CGM</i> element data is displayed. This may substantially reduce the verbosity of the clear text driver.</p>
<dt><code>-Para</code></p>
<dd> Suppress display of <i>CGM </i> element data except for <i>output primitives.</i> The <code>-Data </code> combined with the <code>-Para</code> option permit the display of only the CGM element names.</dl>
<p> The following options are available when <i>device</i> is <code>X11</code>:</p>
<dl>
<dt><code>-background</code><i> color</i></p>
<dd> Specifies the default window background color for color devices. If the metafile explicitly sets color index 0 then this option is overridden.</p>
<dt><code>-foreground</code><i> color</i></p>
<dd> Specifies the default foreground color for color devices. If the metafile explicitly sets color index 1 then this option is overridden.</p>
<dt><code>-geometry</code><i> geometry</i></p>
<dd> Specify the size and/or position of the graphics window in the format of an <i>X11 Window System </i> geometry string.</p>
<dt><code>-ignorebg</code></p>
<dd> Ignore requests to change the background color. This option may be useful when <code>ctrans</code> renders into a X window created by an application other than <code>ctrans</code>. As a side effect of this option the rendering window is not cleared between frames.</p>
<dt><code>-reverse</code></p>
<dd> On monochrome devices reverse video is simulated by swapping the foreground and background colors.</p>
<dt><code>-wid</code><i> window_id</i></p>
<dd> Render into the previously created X window specified by <i>window_id</i>. Normally <code>ctrans</code> creates its own window for plotting. The window specified by <i>window_id</i> must be of type <code>InputOutput</code>. The window must also have inherited its color map, depth and visual class from the root window.</p>
<dt>
<dd> Note also that when this option is used <code>ctrans</code> cannot receive X events from the drawing window. Hence, <code>ctrans </code> cannot use &quot;mouse clicks&quot; as a signal to advance frames. For this reason the <code>-pause</code> option is useful to prevent <code>ctrans</code> from processing the entire metafile without pausing between frames.</p>
<dt>
<dd> <i>window_id </i> may be specified as a decimal or hexidecimal integer.</dl>
<p> The following options apply to the X11 color map management of <code>ctrans</code> when <i>device</i> is X11:</p>
<dl>
<dt>
<dd> <code>ctrans</code> supports three different methods of X11 color map management.</p>
<dt>
<dd> If the user specifies a shared color map (using the <code>-scmap</code> option), then <code>ctrans</code> will use the default X color map for the screen, that is shared by all applications. If the metafile contains more colors than there are available in the default X color map, then a color matching algorithm is employed. The idea of the algorithm is that the color in the current color table that is <i>closest</i> to the requested color will be selected. <i>Closest</i> is defined in terms of the normal distance metric on the RGB cube. If the closest color is equal to or farther away than the percentage error allowed ( <code>-colerr</code> ), then a warning message will be printed. The closest color is still used.</p>
<dt>
<dd> If the user specifies a private color map (using the <code>-pcmap</code> option), then <code>ctrans</code> will create a private color map for the graphics window. This will guarantee that 256 distinct colors are available to the window. This means that the X window will have a different color map than all the other windows on the screen. Therefore, you usually have to have the mouse pointer in the window for the correct color table to be installed. One disadvantage to this option is that there is usually a color flashing effect on the screen since the wrong color table will be installed for the other windows on the screen.</p>
<dt>
<dd> The default color map management scheme attempts to take the best of the two previous models. It starts out behaving like the shared model, in that it uses the default color map for the screen. It differs in that, once it can&#8217;t allocate any more colors from the default color map, in allocates its own private color table and starts using it. This way, the color flashing is only present if it absolutely needs to be so that <code>ctrans</code> can display the correct color.</p>
<dt><code>-scmap</code></p>
<dd> Ask <code>ctrans</code> to use the shared default X color map only.</p>
<dt>
<dd> This is the option used if <code>-wid</code> is specified.</p>
<dt><code>-colerr</code><i> n</i></p>
<dd> Specifies the percentage color error that is acceptable if the <code>-scmap</code> option is being used. If the color being used is <i>n</i> percentage or more different from the color requested, a warning will be reported by <code>ctrans.</code></p>
<dt><code>-pcmap</code></p>
<dd> Ask <code>ctrans </code> to create its own X color map and use it exclusively.</p>
<dt>
<dd> This option is ignored if the <code>-wid </code> option is present.</dl>
<p> The following options are available when <i>device </i> is <code>a60, avs, hdf, hppcl, nrif, sun, </code> or <code>xwd</code>:</p>
<dl>
<dt><code>-dpi</code><i> dpi</i></p>
<dd> Specify the number of dots per inch. This option is only meaningful for the HP LaserJet, <code>hppcl</code>, which ignores the <code>-resolution </code> option. <i>dpi</i> may be one of 75, 100, 150, or 300. The default is 150.</p>
<dt><code>-direct</code></p>
<dd> By default <code>ctrans</code> outputs raster imagery with 8-bit-indexed encoding. When this option is used, if the raster file format supports it, raster imagery is output in a 24-bit-direct encoding scheme. Be warned: the resultant file is three times the size of its 8-bit-indexed counterpart.</p>
<dt><code>-landscape</code></p>
<dd> Generate the image in landscape mode. This option is ignored by all raster devices except the HP LaserJet, <code>hppcl</code>. By default the LaserJet uses portrait mode.</p>
<dt><code>-resolution</code><i> width</i><code>x</code><i>height</i></p>
<dd> <i>width</i> and <i>height</i> specify the spatial resolution in pixels of the raster file to be created. The default is 512&#215;512.</dl>
<h2>EXAMPLES</h2>
<p> To process a metafile named <code>gmeta</code> and display its contents on the TEKTRONIX 4107 terminal, use the following call: </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> % <code>ctrans -d t4107 gmeta</code> </p>
<p> If this device is already defined by the GRAPHCAP environment variable, simply call: </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> % <code>ctrans gmeta</code> </p>
<p> If you wish to display only the first frame starting in the third record, call: </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> % <code>ctrans -record 3 -d t4107 gmeta</code> </p>
<p> To examine the metafile <code>gmeta&#8217;s</code> contents without <code>CGM</code> element data being displayed: </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> % <code>ctrans -d CTXT -Data -Para gmeta</code> </p>
<p> To render the metafile <code>gmeta </code> (under X Windows) in a window that is 512&#215;512 pixels in dimension in the lower right corner of your screen </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> % <code>ctrans -d X11 -geometry 512&#215;512-0-0 gmeta</code> </p>
<p> To rasterize the contents of the metafile <code>gmeta</code> at a resolution of 1024&#215;1024 pixels, call: </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> % <code>ctrans -d xwd -res 1024&#215;1024 &gt; raster.xwd</code> </p>
<p> The raster output is in X11 &quot;xwd&quot; format and is sent to the file <code>raster.xwd</code>. </p>
<p> To zoom in on the upper right quarter of the metafile <code>gmeta</code> and display it in an X window, call: </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> % <code>ctrans -d X11 -window 0.5:0.5:1.0:1.0</code> </p>
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
<dd> If set, this environment variable contains a directory path to be used for temporary files. On most systems the default is <code>/tmp</code>. On some systems the default is <code>/usr/tmp</code>.</dl>
<h2>FILES</h2>
<dl>
<dt>$NCARG_ROOT/lib/ncarg/graphcaps/*</p>
<dd> The binary NCAR Graphcap files</p>
<dt>$NCARG_ROOT/lib/ncarg/fontcaps/*</p>
<dd> The binary NCAR Fontcap files</dl>
<h2>SEE ALSO</h2>
<p> <code>fcaps(1NCARG),</code> <code>fontcap(5NCARG),</code> <code>gcaps(1NCARG),</code> <code>graphcap(5NCARG),</code> <code>idt(1NCARG),</code> <code>ras_palette(5NCARG),</code> <code>med(1NCARG),</code> <code>ictrans(1NCARG)</code> </p>
<p> Hardcopy: NCAR Graphics Fundamentals, UNIX Version</p>
<h2>CAVEATS</h2>
<p> Running in &quot;movie&quot; mode may give surprising results on slower devices, such as dumb terminals. If too short a time interval is specified slow devices may not have finished rendering before the movie timer expires. This results in no pause between frames. </p>
<p> Metafiles which reference color table indices that were not previously defined may have varying results from one device to the next. </p>
<p> Using the <code>-wid </code> option to have <code>ctrans </code> display its output in a window created by another X application may produce unexpected results, particularly with regard to color. </p>
<p> At <code>ctrans&#8217;</code> current level of implementation, the subset of CGM elements supported is closely approximated by the list provided in <code>NCAR&#8217;s</code> <i>Graphics Installer&#8217;s Guide,</i> Version 2.00 (August 1987). However, the best way to determine whether a particular CGM element is supported by the translator is feed a metafile containing the element in question to <code>ctrans</code>. Consult the aforementioned publication for a discussion of Graphcaps and Fontcaps as well.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research </p>
<p> The use of this Software is governed by a License Agreement. </p>
<h2>Index</h2>
