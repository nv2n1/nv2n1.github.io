---
title: "rassplit(1)"
name: "rassplit"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rassplit/"
---

<h2><code>NAME</code></h2>
<p> rassplit &#8211; split a multi-frame rasterfile into single-frame rasterfiles.</p>
<h2><code>SYNOPSIS</code></h2>
<p> <code>rassplit</code> [<code>-f f1 f2 f3 &#8230;</code>] [<code>-ofmt output-format</code>] [<code>-verbose</code>] [<code>-Version</code>] <i>rasterfile</i></p>
<h2><code>DESCRIPTION</code></h2>
<p> The program <code>rassplit</code> will open <i>rasterfile</i> and copy each frame to it&#8217;s own separate output file. By default, all frames are extracted but the user can optionally request a specific set of frames using the <code>-f</code> option. The output format defaults to be the same as the input format, but the user can also optionally select a new output format using the <code>-ofmt</code> option. </p>
<p> The names of the output rasterfiles are derived from the name of the source rasterfile, the output format, and the frame numbers. The examples given below will demonstrate this.</p>
<h2><code>OPTIONS</code></h2>
<dl>
<dt><code>-f</code><i> f1 f2 f3 &#8230;</i></p>
<dd> This option allows the user to specify a list of frames to be extracted from the input rasterfile.</p>
<dt><code>-ofmt</code><i> output-format</i></p>
<dd> The user can specify <i>output-format</i> to be the desired format e.g. <code>hdf</code>, <code>rgb</code>, etc.</p>
<dt><code>-help</code></p>
<dd> Print help information.</p>
<dt><code>-verbose</code></p>
<dd> Print a message each time an output rasterfile is written.</p>
<dt><code>-Version</code></p>
<dd> Print the version number. </p>
</dl>
<h2><code>EXAMPLES</code></h2>
<p> Assume you have a file called &#8216;temp.nrif&#8217; that has three frames and that you&#8217;d like to split it into three separate frames, also in NRIF format. </p>
<pre>
rassplit temp.nrif
</pre>
<p> This will result in three output files named temp.0001.nrif, temp.0002.nrif, and temp.003.nrif. </p>
<p> Assume you only want frames two and three, and you want them produced in HDF format instead of NRIF. </p>
<pre>
rassplit -fmt hdf -f 2 3 temp.nrif
</pre>
<p> This will result in two output files named temp.0001.hdf and temp.0002.hdf. </p>
<h2><code>CAVEATS</code></h2>
<p> If you&#8217;re splitting an HDF file, ask for a non-HDF output format. Otherwise you&#8217;ll just get the first frame over and over again. </p>
<h2><code>SEE ALSO</code></h2>
<p> <code>rasview</code>(1NCARG),<code>rascat</code>(1NCARG),<code>rasls</code>(1NCARG), <code>rasgetpal</code>(1NCARG),<code>ras_formats</code>(5NCARG),<code>ras_palette</code>(5NCARG) </p>
<p> Hardcopy: NCAR Graphics Fundamentals, UNIX Version</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research </p>
<p> The use of this Software is governed by a License Agreement. </p>
<h2>Index</h2>
