---
title: "grace(1)"
name: "grace"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grace/"
description: "grace – command line interface xmgrace – full-featured GUI mode gracebat – batch mode – print and exit"
---

<h2 class="name">NAME</h2>
<p> grace &#8211; command line interface<br />
 xmgrace &#8211; full-featured GUI mode<br />
 gracebat &#8211; batch mode &#8211; print and exit</p>
<h2>DESCRIPTION</h2>
<p> Grace is a WYSIWYG tool to make two-dimensional plots of scientific data. </p>
<h2>SYNOPSIS</h2>
<p> <code>grace</code> [ <i>option</i> | <i>filename</i> ]&#8230;<br />
 <code>xmgrace</code> [ <i>option</i> | <i>filename</i> ]&#8230;<br />
 <code>gracebat</code> [ <i>option</i> | <i>filename</i> ]&#8230; </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-autoscale </code><i>x|y|xy|none</i></p>
<dd> Set autoscale type</p>
<dt><code>-barebones </code></p>
<dd> Turn off all toolbars</p>
<dt><code>-batch </code><i>file</i></p>
<dd> Execute batch <i>file</i> on start up (i.e., after all other options have been processed and the UI initialized)</p>
<dt><code>-block </code><i>file</i></p>
<dd> Assume the data <i>file</i> is block data</p>
<dt><code>-bxy </code><i>x:y:etc.</i></p>
<dd> Form a set from the current block data set using the current set type from columns given in the argument</p>
<dt><code>-datehint </code><i>iso|european|us|days|seconds|nohint</i></p>
<dd> Set the hint for dates analysis</p>
<dt><code>-dpipe </code><i>descriptor</i></p>
<dd> Read data from descriptor on startup</p>
<dt><code>-fixed </code><i>width height</i></p>
<dd> Set canvas size fixed to width*height</p>
<dt><code>-free </code></p>
<dd> Use free page layout</p>
<dt><code>-graph </code><i>number</i></p>
<dd> Set the current graph number</p>
<dt><code>-graphtype </code><i>xy|chart|fixed|polar|pie</i></p>
<dd> Set the type of the current graph</p>
<dt><code>-hardcopy</code></p>
<dd> No interactive session, just print and quit</p>
<dt><code>-hdevice </code><i>device_name</i></p>
<dd> Set default hardcopy device. See <code>xmgrace -version</code> for a list of supported devices.</p>
<dt><code>-install</code></p>
<dd> Install private colormap</p>
<dt><code>-legend load</code></p>
<dd> Turn the graph legend on</p>
<dt><code>-log </code><i>x|y|xy</i></p>
<dd> Set the axis scaling of the current graph to logarithmic</p>
<dt><code>-maxpath </code><i>length</i></p>
<dd> Set the maximal drawing path length</p>
<dt><code>-mono </code></p>
<dd> Run grace in monochrome mode (affects the display only)</p>
<dt><code>-netcdf </code><i>file</i></p>
<dd> Assume data file is in netCDF format. This option is present only if the netCDF support was compiled in</p>
<dt><code>-netcdfxy </code><i>X_var Y_var</i></p>
<dd> If -netcdf was used previously, read from the netCDF file X_var and Y_var variables and create a set. If X_var is &quot;null&quot; then load the index of Y to X. This option is present only if the netCDF support was compiled in</p>
<dt><code>-noask</code></p>
<dd> Assume the answer is yes to all requests, if the operation would overwrite a file, grace will do so without prompting</p>
<dt><code>-noinstall </code></p>
<dd> Don&#8217;t use private colormap</p>
<dt><code>-noprint </code></p>
<dd> In batch mode, do not print</p>
<dt><code>-nosafe </code></p>
<dd> Disable safe mode</p>
<dt><code>-nosigcatch </code></p>
<dd> Don&#8217;t catch signals</p>
<dt><code>-npipe </code><i>file</i></p>
<dd> Read data from named pipe on startup</p>
<dt><code>-nxy </code><i>file</i></p>
<dd> Assume data file is in X Y1 Y2 Y3 &#8230; format</p>
<dt><code>-param </code><i>file</i></p>
<dd> Load parameters from <i>file</i> to the current graph</p>
<dt><code>-pexec </code><i>string</i></p>
<dd> Interpret string as a parameter setting</p>
<dt><code>-pipe</code></p>
<dd> Read data from stdin on startup</p>
<dt><code>-printfile </code><i>file</i></p>
<dd> Save print output to <i>file </i></p>
<dt><code>-remove </code></p>
<dd> Remove data file(s) after read</p>
<dt><code>-results </code><i>file</i></p>
<dd> Write results of some data manipulations to <i>file</i></p>
<dt><code>-rvideo</code></p>
<dd> Exchange the color indices for black and white</p>
<dt><code>-safe </code></p>
<dd> Run in the safe mode (default)</p>
<dt><code>-saveall </code><i>file</i></p>
<dd> Save all to <i>file</i></p>
<dt><code>-seed </code><i>value</i></p>
<dd> Integer seed for random number generator</p>
<dt><code>-settype </code><i>xy|xydx|&#8230;</i></p>
<dd> Set the type of the next data file</p>
<dt><code>-source </code><i>disk|pipe</i></p>
<dd> Source type of next data file</p>
<dt><code>-timer </code><i>delay</i></p>
<dd> Set allowed time slice for real time inputs to <i>delay</i> ms</p>
<dt><code>-timestamp </code></p>
<dd> Add timestamp to plot</p>
<dt><code>-version </code></p>
<dd> Show the program version, registered devices and build time configuration information.</p>
<dt><code>-viewport </code><i>xmin ymin xmax ymax</i></p>
<dd> Set the viewport for the current graph</p>
<dt><code>-wd </code><i>path</i></p>
<dd> Set the working directory</p>
<dt><code>-world </code><i>xmin ymin xmax ymax</i></p>
<dd> Set the world coordinates for the current graph</p>
<dt><code>-usage|-help</code></p>
<dd> This message </p>
</dl>
<h2>RESOURCES</h2>
<dl>
<dt>When run in the GUI mode, the interface is a subject to X resource settings.</p>
<dd> Please refer to the User&#8217;s Guide for a list of important ones. </p>
</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>GRACE_HOME</code></p>
<dd> Specifies the directory where the Grace docs and libs are stored. Default is <code>/usr/local/grace</code></p>
<dt><code>GRACE_HELPVIEWER</code></p>
<dd> The shell command to run an HTML viewer for on-line browsing of the help documents. Must include at least one instance of &quot;%s&quot; which will be replaced with the actual URL by Grace. Default is <code>mozilla %s</code></p>
<dt><code>GRACE_EDITOR</code></p>
<dd> Specifies the editor which is used to edit sets. Default is <code>xterm -e vi</code></p>
<dt><code>GRACE_PRINT_CMD</code></p>
<dd> The print command.</p>
<dt><code>GRACE_FFTW_RAM_WISDOM</code></p>
<dd> and <code>GRACE_FFTW_WISDOM_FILE</code> A flag (0 or 1) and a file name which determine whether a FFT should use `wisdom&#8217; when using the FFTW libraries. </p>
</dl>
<h2>FILES</h2>
<p> In many cases, when Grace needs to access a file given with a relative <i> pathname</i> , it searches for the file along the following path: <i><br />
&nbsp;<wbr>./pathname:./.grace/pathname:~/.grace/pathname:$GRACE_HOME/pathname </i> </p>
<p> The following files are of a special importance: </p>
<p> <code>gracerc</code> &#8211; init file loaded upon start up. </p>
<p> <code>templates/Default.agr</code> &#8211; the default template, loaded whenever a new project is started. </p>
<p> <code>fonts/FontDataBase</code> &#8211; the file responsible for font configuration. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-grconvert/">grconvert</a>(1), <a href="/docs/linux/man/1-x/">X</a>(1) [or <a href="/docs/linux/man/1-xorg/">Xorg</a>(1)], Grace User&#8217;s Guide </p>
<h2>HOME PAGE</h2>
<p> <a rel="nofollow" href="http://plasma-gate.weizmann.ac.il/Grace/">http://plasma-gate.weizmann.ac.il/Grace/</a> </p>
<h2>BUGS</h2>
<p> The best way to submit a bug report is using the &quot;Help/Comments&quot; menu entry. Alternatively, see the home page. </p>
<h2>AUTHORS</h2>
<p> <code>Grace</code> is derived from <code>ACE/gr</code> (a.k.a <code>Xmgr</code> ) written by Paul J Turner. From version number 4.00, the development was taken over by a team of volunteers under the coordination of Evgeny Stambulchik. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 1991-1995 Paul J Turner, Portland, OR<br />
 Copyright (c) 1996-2007 Grace Development Team </p>
<h2>LICENSE</h2>
<p> The program is distributed under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<h2>Index</h2>
