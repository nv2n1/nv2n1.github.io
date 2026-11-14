---
title: "gmtdigitize(1)"
name: "gmtdigitize"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gmtdigitize/"
description: "gmtdigitize – Digitizing and Inverse map transformation of map x/y coordinates"
---

<h2>NAME</h2>
<p> gmtdigitize &#8211; Digitizing and Inverse map transformation of map x/y coordinates</p>
<h2>SYNOPSIS</h2>
<p> <code>gmtdigitize</code> <code>-J</code><i>parameters</i> <code>-R</code><i>west</i>/<i>east</i>/<i>south</i>/<i>north</i>[<code>r</code>] [ <code>-A</code> ] [ <code>-C</code><i>device</i> ] [ <code>-D</code><i>limit</i> ] [ <code>-F</code> ] [ <code>-H</code>[<code>i</code>][<i>nrec</i>] ] [ <code>-L</code><i>lpi</i> ] [ <code>-N</code><i>namestem</i> ] [ <code>-S</code> ] [ <code>-V</code> ] [ <code>-Zk</code>|<code>v</code> ] [ <code>-bo</code>[<code>s</code>|<code>S</code>|<code>d</code>|<code>D</code>[<i>ncol</i>]|<code>c</code>[<i>var1</i><code>/</code><i>&#8230;</i>]] ] [ <code>-m</code>[<i>flag</i>] ] [ &gt; output.d ]</p>
<h2>DESCRIPTION</h2>
<p> <code>gmtdigitize</code> digitizes points from a digitizer via a serial line connection and computes map coordinates using the specified map projection. The program is interactive and will take you through the setup procedure and how you will digitize points. The program will determine the actual map scale as well as rotation of the paper that is taped to the digitizer table. By default the output will go to stdout.<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>No space between the option flag and the associated arguments. Use upper case for the<br />
 option flags and lower case for modifiers.</p>
<dl>
<dt><code>-J</code></p>
<dd> Selects the map projection. Scale is UNIT/degree, 1:xxxxx, or width in UNIT (upper case modifier). UNIT is cm, inch, or m, depending on the <code>MEASURE_UNIT</code> setting in .gmtdefaults4, but this can be overridden on the command line by appending <code>c</code>, <code>i</code>, or <code>m</code> to the scale/width value. When central meridian is optional, default is center of longitude range on <code>-R</code> option. Default standard parallel is the equator. For map height, max dimension, or min dimension, append <code>h</code>, <code>+</code>, or <code>&#8211;</code> to the width, respectively.<br />
 More details can be found in the <code>psbasemap</code> man pages. </p>
<p> <code>CYLINDRICAL PROJECTIONS:</code> </p>
<p> <code>-Jc</code><i>lon0/lat0/scale</i> (Cassini)<br />
 <code>-Jcyl_stere</code>/[<i>lon0/</i>[<i>lat0/</i>]]<i>scale</i> (Cylindrical Stereographic)<br />
 <code>-Jj</code>[<i>lon0/</i>]<i>scale</i> (Miller)<br />
 <code>-Jm</code>[<i>lon0</i>/[<i>lat0/</i>]]<i>scale</i> (Mercator)<br />
 <code>-Jm</code><i>lon0/lat0/scale</i> (Mercator &#8211; Give meridian and standard parallel)<br />
 <code>-Jo</code>[<code>a</code>]<i>lon0/lat0/azimuth/scale</i> (Oblique Mercator &#8211; point and azimuth)<br />
 <code>-Jo</code>[<code>b</code>]<i>lon0/lat0/lon1/lat1/scale</i> (Oblique Mercator &#8211; two points)<br />
 <code>-Joc</code><i>lon0/lat0/lonp/latp/scale</i> (Oblique Mercator &#8211; point and pole)<br />
 <code>-Jq</code>[<i>lon0/</i>[<i>lat0/</i>]]<i>scale</i> (Cylindrical Equidistant)<br />
 <code>-Jt</code><i>lon0/</i>[<i>lat0/</i>]<i>scale</i> (TM &#8211; Transverse Mercator)<br />
 <code>-Ju</code><i>zone/scale</i> (UTM &#8211; Universal Transverse Mercator)<br />
 <code>-Jy</code>[<i>lon0/</i>[<i>lat0/</i>]]<i>scale</i> (Cylindrical Equal-Area) </p>
<p> <code>CONIC PROJECTIONS:</code> </p>
<p> <code>-Jb</code><i>lon0/lat0/lat1/lat2/scale</i> (Albers)<br />
 <code>-Jd</code><i>lon0/lat0/lat1/lat2/scale</i> (Conic Equidistant)<br />
 <code>-Jl</code><i>lon0/lat0/lat1/lat2/scale</i> (Lambert Conic Conformal)<br />
 <code>-Jpoly</code>/[<i>lon0/</i>[<i>lat0/</i>]]<i>scale</i> ((American) Polyconic) </p>
<p> <code>AZIMUTHAL PROJECTIONS:</code> </p>
<p> <code>-Ja</code><i>lon0/lat0</i>[<i>/horizon</i>]<i>/scale</i> (Lambert Azimuthal Equal-Area)<br />
 <code>-Je</code><i>lon0/lat0</i>[<i>/horizon</i>]<i>/scale</i> (Azimuthal Equidistant)<br />
 <code>-Jf</code><i>lon0/lat0</i>[<i>/horizon</i>]<i>/scale</i> (Gnomonic)<br />
 <code>-Jg</code><i>lon0/lat0</i>[<i>/horizon</i>]<i>/scale</i> (Orthographic)<br />
 <code>-Jg</code><i>lon0/lat0/altitude/azimuth/tilt/twist/Width/Height/scale</i> (General Perspective).<br />
 <code>-Js</code><i>lon0/lat0</i>[<i>/horizon</i>]<i>/scale</i> (General Stereographic) </p>
<p> <code>MISCELLANEOUS PROJECTIONS:</code> </p>
<p> <code>-Jh</code>[<i>lon0/</i>]<i>scale</i> (Hammer)<br />
 <code>-Ji</code>[<i>lon0/</i>]<i>scale</i> (Sinusoidal)<br />
 <code>-Jkf</code>[<i>lon0/</i>]<i>scale</i> (Eckert IV)<br />
 <code>-Jk</code>[<code>s</code>][<i>lon0/</i>]<i>scale</i> (Eckert IV)<br />
 <code>-Jn</code>[<i>lon0/</i>]<i>scale</i> (Robinson)<br />
 <code>-Jr</code>[<i>lon0/</i>]<i>scale</i> (Winkel Tripel)<br />
 <code>-Jv</code>[<i>lon0/</i>]<i>scale</i> (Van der Grinten)<br />
 <code>-Jw</code>[<i>lon0/</i>]<i>scale</i> (Mollweide) </p>
<p> <code>NON-GEOGRAPHICAL PROJECTIONS:</code> </p>
<p> <code>-Jp</code>[<code>a</code>]<i>scale</i>[<i>/origin</i>][<code>r</code>|<code>z</code>] (Polar coordinates (theta,r))<br />
 <code>-Jx</code><i>x-scale</i>[<code>d</code>|<code>l</code>|<code>p</code><i>pow</i>|<code>t</code>|<code>T</code>][<i>/y-scale</i>[<code>d</code>|<code>l</code>|<code>p</code><i>pow</i>|<code>t</code>|<code>T</code>]] (Linear, log, and power scaling)<br />
 For geographic projections you can give 1 as the scale will be solved for anyway.</p>
<dt><code>-R</code></p>
<dd> <i>xmin</i>, <i>xmax</i>, <i>ymin</i>, and <i>ymax</i> specify the Region of interest. For geographic regions, these limits correspond to <i>west, east, south,</i> and <i>north</i> and you may specify them in decimal degrees or in [+-]dd:mm[:ss.xxx][W|E|S|N] format. Append <code>r</code> if lower left and upper right map coordinates are given instead of w/e/s/n. The two shorthands <code>-Rg</code> and <code>-Rd</code> stand for global domain (0/360 and -180/+180 in longitude respectively, with -90/+90 in latitude). Alternatively, specify the name of an existing grid file and the <code>-R</code> settings (and grid spacing, if applicable) are copied from the grid. For calendar time coordinates you may either give (a) relative time (relative to the selected <code>TIME_EPOCH</code> and in the selected <code>TIME_UNIT</code>; append <code>t</code> to <code>-JX</code>|<code>x</code>), or (b) absolute time of the form [<i>date</i>]<code>T</code>[<i>clock</i>] (append <code>T</code> to <code>-JX</code>|<code>x</code>). At least one of <i>date</i> and <i>clock</i> must be present; the <code>T</code> is always required. The <i>date</i> string must be of the form [-]yyyy[-mm[-dd]] (Gregorian calendar) or yyyy[-Www[-d]] (ISO week calendar), while the <i>clock</i> string must be of the form hh:mm:ss[.xxx]. The use of delimiters and their type and positions must be exactly as indicated (however, input, output and plot formats are customizable; see <code>gmtdefaults</code>).</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-A</code></p>
<dd> Give an audible signal each time the digitizer mouse/puck is clicked [Default is silent].</p>
<dt><code>-C</code></p>
<dd> Specify the device (port) to read from [Default is /dev/ttyS0].</p>
<dt><code>-D</code></p>
<dd> Only output a point if it is further than <i>limit</i> units from the previous point. Append <code>c, i, m, p</code> for cm, inch, meter, or point, respectively [Default is no limit].</p>
<dt><code>-F</code></p>
<dd> Force the program to ask for 4 arbitrary calibration points [Default is to use the 4 corners of the map, if possible].</p>
<dt><code>-H</code></p>
<dd> This option allows you to write out any number of header records to the beginning of the output file. Each record will automatically start with a #-character to indicate comment. Headers are not written if multiple output files are selected with <code>-N</code> <code>-m</code>.</p>
<dt><code>-L</code></p>
<dd> Set the digitizer table resolution in lines per inch [2540].</p>
<dt><code>-N</code></p>
<dd> Set name for output file(s). If a regular filename is given, then all digitized data will be written to that file. If the file contains a C-format for an integer (i.e., %d) then the file is used as a format statement to create unique filenames based on the current segment number (e.g., line_%d.d will yield files line_0.d, line_1.d, etc). By default, all output is written to stdout. Multiple segment files requires specifying the <code>-m</code> option.</p>
<dt><code>-S</code></p>
<dd> Suppress points that fall outside the specified map region [Default outputs all points].</p>
<dt><code>-V</code></p>
<dd> Selects verbose mode, which will send progress reports to stderr [Default runs &quot;silently&quot;]. The program will also duplicate data output to stderr for monitoring.</p>
<dt><code>-Z</code></p>
<dd> Append <code>v</code> to prompt for a <i>z</i>-value and output it as a third data column. Append <code>k</code> to output the button key as the final data column. Both <code>-Zk</code> and <code>-Zv</code> can be specified. [Default is just 2 column x,y output].</p>
<dt><code>-bo</code></p>
<dd> Selects binary output. Append <code>s</code> for single precision [Default is <code>d</code> (double)]. Uppercase <code>S</code> or <code>D</code> will force byte-swapping. Optionally, append <i>ncol</i>, the number of desired columns in your binary output file.</p>
<dt><code>-m</code></p>
<dd> Multiple segment file(s). Segments are separated by a special record. For ASCII files the first character must be <i>flag</i> [Default is &#8216;&gt;&#8217;]. For binary files all fields must be NaN and <code>-b</code> must set the number of output columns explicitly. By default the <code>-m</code> setting applies to both input and output. Use <code>-mi</code> and <code>-mo</code> to give separate settings to input and output.</dl>
<h2>EXAMPLES</h2>
<p> To digitize lines from a mercator map made for a given region, and save each line segment in individual files called segment_000.xy, segment_001.xy etc, try </p>
<p> gmtdigitize <code>-R</code>20/50/12/25 <code>-Jm</code>1:1 <code>-m</code> <code>-N</code>segment_%3.3d.xy </p>
<p> To digitize seismically defined interfaces from a multichannel seismic section, with horizontal distances from 130 to 970, and vertical times from 0 to 10 seconds, write out the button code, and save all line segment to a single multisegment file, and beep at each click, try </p>
<p> gmtdigitize <code>-R</code>130/970/0/10 <code>-Jx</code>1/-1 <code>-m</code> <code>-A</code> <code>-Z</code> &gt; interfaces.d </p>
<h2>SYSTEM SETUP</h2>
<p> This applies to the Calcomp DrawingBoard III hooked up to a RedHat Linux workstation. We use /dev/ttyS0 as the serial port and change permissions so that it is world read/write-able. Then, stty -F /dev/ttyS0 evenp will set the terminal settings, which can be checked with stty -F /dev/ttyS0 -a. Setup of digitizer: We use the CalComp 2000 ASCII (Save 3) setup, which has:<br />
 Mode: Point<br />
 Baud Rate: 9600<br />
 Data Bits: 7<br />
 Parity: Even<br />
 Data Rate: 125 pps<br />
 Resolution: 200 lpi<br />
 Output Format: Format 0<br />
 Emulation: CalComp 2000 ASCII<br />
 (A)We need to make a slight modification to the Preset No 3 settings: (1) 2450 LPI instead of 200, and (2) None instead of yes for added CR. These modifications can be changed and saved to Preset 3 on the digitizer but a power outage may reset in back to the factory defaults, necessitating a manual reset of those two settings. (B) Setup tty port. stty -F /dev/ttyS0 evenp (C) Run gmtdigitize. Map scale does not matter; it is computed from the region and plot size.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/l-gmtdefaults/">gmtdefaults</a></i>(l), <i><a href="/docs/linux/man/l-gmt/">GMT</a></i>(l), <i><a href="/docs/linux/man/l-gmtstitch/">gmtstitch</a></i>(l), <i><a href="/docs/linux/man/l-mapproject/">mapproject</a></i>(l), <i><a href="/docs/linux/man/l-project/">project</a></i>(l) </p>
<h2>Index</h2>
