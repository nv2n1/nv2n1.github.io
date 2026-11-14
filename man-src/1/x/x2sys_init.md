---
title: "x2sys_init(1)"
name: "x2sys_init"
section: "1"
letter: "x"
url: "/docs/linux/man/1-x2sys_init/"
description: "x2sys_init – Initialize a new x2sys track database"
---

<h2>NAME</h2>
<p> x2sys_init &#8211; Initialize a new x2sys track database</p>
<h2>SYNOPSIS</h2>
<p> <code>x2sys_init</code> <i>TAG</i> <i>deffile</i> [ <code>c</code>|<code>f</code>|<code>g</code>|<code>e</code> ] [ <i>suffix</i> ] [ ] [ <code>d</code>|<code>g</code> ] [ <i>dx</i>[/<i>dy</i>] ] [ <code>d</code>|<code>s</code><i>unit</i> ] [ <i>region</i> ] [ [<i>level</i>] ] [ <code>t</code>|<code>d</code><i>gap</i> ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>x2sys_init</code> is the starting point for anyone wishing to use x2sys; it initializes a set of data bases that are particular to one kind of track data. These data, their associated data bases, and key parameters are given a short-hand notation called an x2sys TAG. The TAG keeps track of settings such as file format, whether the data are geographic or not, and the binning resolution for track indices. Running <code>x2sys_init</code> is a prerequisite to running any of the other x2sys programs, such as <code>x2sys_binlist</code>, which will create a crude representation of where each data track go within the domain and which observations are available; this information serves as input to <code>x2sys_put</code> which updates the track data base. Then, <code>x2sys_get</code> can be used to find which tracks and data are available inside a given region. With that list of tracks you can use <code>x2sys_cross</code> to calculate track crossovers, use <code>x2sys_report</code> to report crossover statistics or <code>x2sys_list</code> to pull out selected crossover information that <code>x2sys_solve</code> can use to determine track-specific systematic corrections. These corrections may be used with <code>x2sys_datalist</code> to extract corrected data values for use in subsequent work. Because you can run <code>x2sys_init</code> you <i>must</i> set the environmental parameter X2SYS_HOME to a directory where you have write permission, which is where x2sys can keep track of your settings.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>TAG</i></p>
<dd> The unique name of this data type x2sys TAG.</p>
<dt><code>-D</code><i>deffile</i></p>
<dd> Definition file prefix for this data set [See DEFINITION FILES below for more information]. Specify full path if the file is not in the current directory.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-Cc</code>|<code>f</code>|<code>g</code>|<code>e</code></p>
<dd> Select procedure for along-track distance calculation when needed by other programs: </p>
<p> <code>c</code> Cartesian distances [Default, unless <code>-G</code> is set]. </p>
<p> <code>f</code> Flat Earth distances. </p>
<p> <code>g</code> Great circle distances [Default if <code>-G</code> is set]. </p>
<p> <code>e</code> Geodesic distances on current GMT ellipsoid.</p>
<dt><code>-E</code><i>suffix</i></p>
<dd> Specifies the file extension (suffix) for these data files. If not given we use the definition file prefix as the suffix (see <code>-D</code>).</p>
<dt><code>-F</code></p>
<dd> Force creating new files if old ones are present [Default will abort if old TAG files are found].</p>
<dt><code>-Gd</code>|<code>g</code></p>
<dd> Selects geographical coordinates. Append <code>d</code> for discontinuity at the Dateline (makes longitude go from -180 to + 180) or <code>g</code> for discontinuity at Greenwich (makes longitude go from 0 to 360 [Default]). If not given we assume the data are Cartesian.</p>
<dt><code>-I</code><i>dx</i>[/<i>dy</i>]</p>
<dd> <i>x_inc</i> [and optionally <i>y_inc</i>] is the grid spacing. Append <code>m</code> to indicate minutes or <code>c</code> to indicate seconds for geographic data. These spacings refer to the binning used in the track bin-index data base.</p>
<dt><code>-Nd</code>|<code>s</code><i>unit</i></p>
<dd> Sets the units used for distance and speed when requested by other programs. Append <code>d</code> for distance or <code>s</code> for speed, then give the desired <i>unit</i> as <code>c</code> (Cartesian userdist or userdist/usertime), <code>e</code> (meters or m/s), <code>f</code> (feet or feet/s), <code>k</code> (km or kms/hr), <code>m</code> (miles or miles/hr), <code>n</code> (nautical miles or knots) or <code>u</code> (survey feet or survey feet/s). [Default is <code>-Ndk</code> <code>-Nse</code> (km and m/s) if <code>-G</code> is set and <code>-Ndc</code> and <code>-Nsc</code> otherwise (Cartesian units)].</p>
<dt><code>-R</code>[<i>unit</i>]<i>west</i>/<i>east</i>/<i>south</i>/<i>north</i>[/<i>zmin</i>/<i>zmax</i>][<code>r</code>]</p>
<dd> <i>west</i>, <i>east</i>, <i>south</i>, and <i>north</i> specify the region of interest, and you may specify them in decimal degrees or in [+-]dd:mm[:ss.xxx][W|E|S|N] format. Append <code>r</code> if lower left and upper right map coordinates are given instead of w/e/s/n. The two shorthands <code>-Rg</code> and <code>-Rd</code> stand for global domain (0/360 and -180/+180 in longitude respectively, with -90/+90 in latitude). Alternatively for grid creation, give <code>R</code><i>code</i><i>lon</i>/<i>lat</i>/<i>nx</i>/<i>ny</i>, where <i>code</i> is a 2-character combination of L, C, R (for left, center, or right) and T, M, B for top, middle, or bottom. e.g., BL for lower left. This indicates which point on a rectangular region the <i>lon</i>/<i>lat</i> coordinate refers to, and the grid dimensions <i>nx</i> and <i>ny</i> with grid spacings via <code>-I</code> is used to create the corresponding region. Alternatively, specify the name of an existing grid file and the <code>-R</code> settings (and grid spacing, if applicable) are copied from the grid. Using <code>-R</code><i>unit</i> expects projected (Cartesian) coordinates compatible with chosen <code>-J</code> and we inversely project to determine actual rectangular geographic region. For perspective view (<code>-p</code>), optionally append /<i>zmin</i>/<i>zmax</i>. In case of perspective view (<code>-p</code>), a z-range (<i>zmin</i>, <i>zmax</i>) can be appended to indicate the third dimension. This needs to be done only when using the <code>-Jz</code> option, not when using only the <code>-p</code> option. In the latter case a perspective view of the plane is plotted, with no third dimension. For Cartesian data just give <i>xmin/xmax/ymin/ymax</i>. This option bases the statistics on those COE that fall inside the specified domain.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-Wt</code>|<code>d</code><i>gap</i></p>
<dd> Give <code>t</code> or <code>d</code> and append the corresponding maximum time gap (in user units; this is typically seconds [Infinity]), or distance (for units, see ) gap [Infinity]) allowed between the two data points immediately on either side of a crossover. If these limits are exceeded then a data gap is assumed and no COE will be determined.</p>
<dt><code>-^</code> or just <code>&#8211;</code></p>
<dd> Print a short message about the syntax of the command, then exits (NOTE: on Windows use just <code>&#8211;</code>).</p>
<dt><code>-+</code> or just <code>+</code></p>
<dd> Print an extensive usage (help) message, including the explanation of any module-specific option (but not the GMT common options), then exits.</p>
<dt><code>-?</code> or no arguments</p>
<dd> Print a complete usage (help) message, including the explanation of options, then exits.</p>
<dt><code>&#8211;</code><code>-version</code></p>
<dd> Print GMT version and exit.</p>
<dt><code>&#8211;</code><code>-show-datadir</code></p>
<dd> Print full path to GMT share directory and exit.</dl>
<h2>DEFINITION FILES</h2>
<p> These *.def files contain information about the data file format and have two sections: (1) header information and (2) column information. All header information starts with the character # in the first column, immediately followed by an upper-case directive. If the directive takes an argument it is separated by white-space. You may append a trailing # comments. Five directives are recognized: </p>
<p> <code>ASCII</code> states that the data files are in ASCII format. </p>
<p> <code>BINARY</code> states that the data files are native binary files. </p>
<p> <code>NETCDF</code> states that the data files are COARDS-compliant 1-D netCDF files. </p>
<p> <code>SKIP</code> takes an integer argument which is either the number of lines to skip (when reading ASCII files) or the number of bytes to skip (when reading native binary files). Not used with netCDF files. </p>
<p> <code>GEO</code> indicates that these files are geographic data sets, with periodicities in the <i>x</i>-coordinate (longitudes). Alternatively, use <code>-G</code>. </p>
<p> <code>MULTISEG</code> means each track consists of multiple segments separated by a GMT segment header (alternatively, use <code>-m</code> when defining the system TAG). Not used with netCDF files. </p>
<p> The column information consists of one line per column in the order the columns appear in the data file. For each column you must provide seven attributes: </p>
<p> <i>name type NaN NaN-proxy scale offset oformat</i> </p>
<p> <i>name</i> is the name of the column variable. It is expected that you will use the special names <i>lon</i> (or <i>x</i> if Cartesian) and <i>lat</i> (or <i>y</i>) for the two required coordinate columns, and <i>time</i> when optional time data are present. </p>
<p> <i>type</i> is always <code>a</code> for ASCII representations of numbers, whereas for binary files you may choose among <code>c</code> for signed 1-byte character (-127,+128), <code>u</code> for unsigned byte (0-255), <code>h</code> for signed 2-byte integers (-32768,+32767), <code>i</code> for signed 4-byte integers (-2,147,483,648,+2,147,483,647), <code>f</code> for 4-byte floating points and <code>d</code> for 8-byte double precision floating points. For netCDF, simply use <code>d</code> as netCDF will automatically handle type-conversions during reading. </p>
<p> <i>NaN</i> is Y if certain values (e.g, -9999) are to be replaced by NAN, and N otherwise. </p>
<p> <i>NaN-proxy</i> is that special value (e.g., -9999). </p>
<p> <i>scale</i> is used to multiply the data after reading. </p>
<p> <i>offset</i> is used to add to the scaled data. </p>
<p> <i>oformat</i> is a C-style format string used to print values from this column. </p>
<p> If you give &#8211; as the <i>oformat</i> then GMT&#8217;s formatting machinery will be used instead (i.e., <i>FORMAT_FLOAT_OUT</i>, <i>FORMAT_GEO_MAP</i>, <i>FORMAT_DATE_MAP</i>, <i>FORMAT_CLOCK_MAP</i>). Some file formats already have definition files premade. These include mgd77 (for plain ASCII MGD77 data files), mgd77+ (for enhanced MGD77+ netCDF files), gmt (for old mgg supplement binary files), xy (for plain ASCII x, y tables), xyz (same, with one z-column), geo (for plain ASCII longitude, latitude files), and geoz (same, with one z-column).</p>
<h2>EXAMPLES</h2>
<p> If you have a large set of track data files you can organize them using the x2sys tools. Here we will outline the steps. Let us assume that your track data file format consist of 2 header records with text information followed by any number of identically formatted data records with 6 columns (lat, lon, time, obs1, obs2, obs3) and that files are called *.trk. We will call this the &quot;line&quot; format. First, we create the line.def file: <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=7>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> # Define file for the line format </td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=7>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> # SKIP 2 </td>
<td> # Skip 2 header records </td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=7>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> # GEO </td>
<td> # Data are geographic </td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=7>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> #name </td>
<td> type </td>
<td> NaN </td>
<td> NaN-proxy </td>
<td> scale </td>
<td> offset </td>
<td> oformat
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=7>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> lat </td>
<td> a </td>
<td> N </td>
<td> 0 </td>
<td> 1 </td>
<td> 0 </td>
<td> %9.5f
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=7>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> lon </td>
<td> a </td>
<td> N </td>
<td> 0 </td>
<td> 1 </td>
<td> 0 </td>
<td> %10.5f
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=7>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> time </td>
<td> a </td>
<td> N </td>
<td> 0 </td>
<td> 1 </td>
<td> 0 </td>
<td> %7.1f
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=7>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> obs1 </td>
<td> a </td>
<td> N </td>
<td> 0 </td>
<td> 1 </td>
<td> 0 </td>
<td> %7.2f
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=7>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> obs2 </td>
<td> a </td>
<td> N </td>
<td> 0 </td>
<td> 1 </td>
<td> 0 </td>
<td> %7.2f
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=7>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> obs3 </td>
<td> a </td>
<td> N </td>
<td> 0 </td>
<td> 1 </td>
<td> 0 </td>
<td> %7.2f
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=7>
<hr>
</td>
</tr>
</table>
<p></center> </p>
<p> Next we create the TAG and the TAG directory with the databases for these line track files. Assuming these contain geographic data and that we want to keep track of the data distribution at a 1 x 1 degree resolution, with distances in km calculated along geodesics and with speeds given in knots, we may run </p>
<pre>
gmt x2sys_init LINE -V -G -Dline -Rg -Ce -Ndk -NsN -I1/1 -Etrk
</pre>
<p> where we have selected LINE to be our x2sys tag. When x2sys tools try to read your line data files they will first look in the current directory and second look in the file <i>TAG</i>_paths.txt for a list of additional directories to examine. Therefore, create such a file (here LINE_paths.txt) and stick the full paths to your data directories there. All TAG-related files (definition files, tag files, and track data bases created) will be expected to be in the directory pointed to by <code>$X2SYS_HOME</code>/<i>TAG</i> (in our case <code>$X2SYS_HOME</code>/LINE). Note that the argument to <code>-D</code> must contain the full path if the *.def file is not in the current directory. <code>x2sys_init</code> will copy this file to the <code>$X2SYS_HOME</code>/<i>TAG</i> directory where all other x2sys tools will expect to find it.</p>
<dl>
<dt><code>Create tbf file(s):</code></p>
<dd> Once the (empty) TAG databases have been initialized we go through a two-step process to populate them. First we run <code>x2sys_binlist</code> on all our track files to create one (or more) multisegment track bin-index files (tbf). These contain information on which 1 x 1 degree bins (or any other blocksize; see <code>-I</code>) each track has visited and which observations (in your case obs1, obs2, obs3) were actually observed (not all tracks may have all three kinds of observations everywhere). For instance, if your tracks are listed in the file tracks.lis we may run this command: </p>
<pre>
gmt x2sys_binlist -V -TLINE :tracks.lis &gt; tracks.tbf
</pre>
<dt><code>Update index data base:</code></p>
<dd> Next, the track bin-index files are fed to <code>x2sys_put</code> which will insert the information into the TAG databases: </p>
<pre>
gmt x2sys_put -V -TLINE tracks.tbf
</pre>
<dt><code>Search for data:</code></p>
<dd> You may now use <code>x2sys_get</code> to find all the tracks within a certain sub-region, and optionally limit the search to those tracks that have a particular combination of observables. E.g., to find all the tracks which has both obs1 and obs3 inside the specified region, run </p>
<pre>
gmt x2sys_get -V -TLINE -R20/40/-40/-20 -Fobs1,obs3 &gt; tracks.tbf
</pre>
<dt><code>MGD77[+] or GMT:</code></p>
<dd> Definition files already exist for MGD77 files (both standard ASCII and enhanced netCDF-based MGD77+ files) and the old *.gmt files manipulated by the mgg supplements; for these data sets the <code>-C</code> and <code>-N</code> will default to great circle distance calculation in km and speed in m/s. There are also definition files for plain x,y[,z] and lon,lat[,z] tracks. To initiate new track databases to be used with MGD77 data from NGDC, try </p>
<pre>
gmt x2sys_init MGD77 -V -Dmgd77 -Emgd77 -Rd -Gd -Nsn -I1/1 -Wt900 -Wd5
</pre>
<p> where we have chosen a 15 minute (900 sec) or 5 km threshold to indicate a data gap and selected knots as the speed; the other steps are similar.</p>
<dt><code>Binary files:</code></p>
<dd> Let us pretend that your line files actually are binary files with a 128-byte header structure (to be skipped) followed by the data records and where <i>lon</i>, <i>lat</i>, <i>time</i> are double precision numbers while the three observations are 2-byte integers which must be multiplied by 0.1. Finally, the first two observations may be -32768 which means there is no data available. All that is needed is a different line.def file: <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=7>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> # Define file for the binary line format </td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=7>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> # BINARY </td>
<td> # File is now binary </td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=7>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> # SKIP 128 </td>
<td> # Skip 128 bytes </td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=7>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> # GEO </td>
<td> # Data are geographic </td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=7>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> #name </td>
<td> type </td>
<td> NaN </td>
<td> NaN-proxy </td>
<td> scale </td>
<td> offset </td>
<td> oformat
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=7>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> lon </td>
<td> d </td>
<td> N </td>
<td> 0 </td>
<td> 1 </td>
<td> 0 </td>
<td> %10.5f
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=7>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> lat </td>
<td> d </td>
<td> N </td>
<td> 0 </td>
<td> 1 </td>
<td> 0 </td>
<td> %9.5f
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=7>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> time </td>
<td> d </td>
<td> N </td>
<td> 0 </td>
<td> 1 </td>
<td> 0 </td>
<td> %7.1f
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=7>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> obs1 </td>
<td> h </td>
<td> Y </td>
<td> -32768 </td>
<td> 0.1 </td>
<td> 0 </td>
<td> %6.1f
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=7>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> obs2 </td>
<td> h </td>
<td> Y </td>
<td> -32768 </td>
<td> 0.1 </td>
<td> 0 </td>
<td> %6.1f
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=7>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> obs3 </td>
<td> h </td>
<td> N </td>
<td> 0 </td>
<td> 0.1 </td>
<td> 0 </td>
<td> %6.1f
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=7>
<hr>
</td>
</tr>
</table>
<p></center> </p>
<p> The rest of the steps are identical.</p>
<dt><code>COARDS 1-D netCDF files:</code></p>
<dd> Finally, suppose that your line files actually are netCDF files that conform to the COARDS convention, with data columns named <i>lon</i>, <i>lat</i>, <i>time</i>, <i>obs1</i>, <i>obs2</i>, and <i>obs3</i>. All that is needed is a different line.def file: <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=7>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> # Define file for the netCDF COARDS line format </td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=7>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> # NETCDF </td>
<td> # File is now netCDF </td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=7>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> # GEO </td>
<td> # Data are geographic </td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=7>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> #name </td>
<td> type </td>
<td> NaN </td>
<td> NaN-proxy </td>
<td> scale </td>
<td> offset </td>
<td> oformat
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=7>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> lon </td>
<td> d </td>
<td> N </td>
<td> 0 </td>
<td> 1 </td>
<td> 0 </td>
<td> %10.5f
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=7>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> lat </td>
<td> d </td>
<td> N </td>
<td> 0 </td>
<td> 1 </td>
<td> 0 </td>
<td> %9.5f
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=7>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> time </td>
<td> d </td>
<td> N </td>
<td> 0 </td>
<td> 1 </td>
<td> 0 </td>
<td> %7.1f
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=7>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> obs1 </td>
<td> d </td>
<td> N </td>
<td> 0 </td>
<td> 1 </td>
<td> 0 </td>
<td> %6.1f
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=7>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> obs2 </td>
<td> d </td>
<td> N </td>
<td> 0 </td>
<td> 1 </td>
<td> 0 </td>
<td> %6.1f
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=7>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> obs3 </td>
<td> d </td>
<td> N </td>
<td> 0 </td>
<td> 1 </td>
<td> 0 </td>
<td> %6.1f
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=7>
<hr>
</td>
</tr>
</table>
<p></center> </p>
<p> Note we use no scaling or NAN proxies since those issues are usually handled internally in the netCDF format description.</dl>
<h2>SEE ALSO</h2>
<p> <code>x2sys_binlist</code>, <code>x2sys_datalist</code>, <code>x2sys_get</code>, <code>x2sys_list</code>, <code>x2sys_put</code>, <code>x2sys_report</code>, <code>x2sys_solve</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
