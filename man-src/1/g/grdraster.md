---
title: "grdraster(1)"
name: "grdraster"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grdraster/"
description: "grdraster – Extract subregion from a binary raster and save as a GMT grid"
---

<h2>NAME</h2>
<p> grdraster &#8211; Extract subregion from a binary raster and save as a GMT grid</p>
<h2>SYNOPSIS</h2>
<p> <code>grdraster</code> [ <i>filenumber</i> | <i>&quot;text pattern&quot;</i> ] <i>region</i> [ <i>grdfile</i> ] [ <i>increment</i> ] [ <i>parameters</i> ] [ [<i>level</i>] ] [ <code>-bo</code><i>&lt;binary&gt;</i> ] [ <code>-do</code><i>&lt;nodata&gt;</i> ] [ <code>-o</code><i>&lt;flags&gt;</i> ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>grdraster</code> reads a file called <i>grdraster.info</i> from the current working directory, the directories pointed to by the environment variables <code>$GMT_USERDIR</code> and <code>$GMT_DATADIR</code>, or in <code>$GMT_SHAREDIR</code>/dbase (in that order). The file <i>grdraster.info</i> defines binary arrays of data stored in scan-line format in data files. Each file is given a <i>filenumber</i> in the info file. <code>grdraster</code> figures out how to load the raster data into a grid file spanning a region defined by <code>-R</code>. By default the grid spacing equals the raster spacing. The <code>-I</code> option may be used to sub-sample the raster data. No filtering or interpolating is done, however; the <i>x_inc</i> and <i>y_inc</i> of the grid must be multiples of the increments of the raster file and <code>grdraster</code> simply takes every n&#8217;th point. The output of <code>grdraster</code> is either grid or pixel registered depending on the registration of the raster used. It is up to the GMT system person to maintain the <i>grdraster.info</i> file in accordance with the available rasters at each site. Raster data sets are not supplied with GMT but can be obtained by anonymous ftp and on CD-ROM (see README page in dbase directory). <code>grdraster</code> will list the available files if no arguments are given. Finally, <code>grdraster</code> will write xyz-triplets to stdout if no output gridfile name is given</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>filenumber</i></p>
<dd> If an integer matching one of the files listed in the <i>grdraster.info</i> file is given we will use that data set, else we will match the given text pattern with the data set description in order to determine the data set.</p>
<dt><code>-R</code>[<i>unit</i>]<i>west</i>/<i>east</i>/<i>south</i>/<i>north</i>[/<i>zmin</i>/<i>zmax</i>][<code>r</code>]</p>
<dd> <i>west</i>, <i>east</i>, <i>south</i>, and <i>north</i> specify the region of interest, and you may specify them in decimal degrees or in [+-]dd:mm[:ss.xxx][W|E|S|N] format. Append <code>r</code> if lower left and upper right map coordinates are given instead of w/e/s/n. The two shorthands <code>-Rg</code> and <code>-Rd</code> stand for global domain (0/360 and -180/+180 in longitude respectively, with -90/+90 in latitude). Alternatively for grid creation, give <code>R</code><i>code</i><i>lon</i>/<i>lat</i>/<i>nx</i>/<i>ny</i>, where <i>code</i> is a 2-character combination of L, C, R (for left, center, or right) and T, M, B for top, middle, or bottom. e.g., BL for lower left. This indicates which point on a rectangular region the <i>lon</i>/<i>lat</i> coordinate refers to, and the grid dimensions <i>nx</i> and <i>ny</i> with grid spacings via <code>-I</code> is used to create the corresponding region. Alternatively, specify the name of an existing grid file and the <code>-R</code> settings (and grid spacing, if applicable) are copied from the grid. Using <code>-R</code><i>unit</i> expects projected (Cartesian) coordinates compatible with chosen <code>-J</code> and we inversely project to determine actual rectangular geographic region. For perspective view (<code>-p</code>), optionally append /<i>zmin</i>/<i>zmax</i>. In case of perspective view (<code>-p</code>), a z-range (<i>zmin</i>, <i>zmax</i>) can be appended to indicate the third dimension. This needs to be done only when using the <code>-Jz</code> option, not when using only the <code>-p</code> option. In the latter case a perspective view of the plane is plotted, with no third dimension. If <code>r</code> is appended, you may also specify a map projection to define the shape of your region. The output region will be rounded off to the nearest whole grid-step in both dimensions.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-G</code><i>grdfile</i></p>
<dd> Name of output grid file. If not set, the grid will be written as ASCII (or binary; see <code>-bo</code>) xyz-triplets to stdout instead.</p>
<dt><code>-I</code><i>xinc</i>[<i>unit</i>][<code>=</code>|<code>+</code>][/<i>yinc</i>[<i>unit</i>][<code>=</code>|<code>+</code>]]</p>
<dd> <i>x_inc</i> [and optionally <i>y_inc</i>] is the grid spacing. Optionally, append a suffix modifier. <code>Geographical (degrees) coordinates</code>: Append <code>m</code> to indicate arc minutes or <code>s</code> to indicate arc seconds. If one of the units <code>e</code>, <code>f</code>, <code>k</code>, <code>M</code>, <code>n</code> or <code>u</code> is appended instead, the increment is assumed to be given in meter, foot, km, Mile, nautical mile or US survey foot, respectively, and will be converted to the equivalent degrees longitude at the middle latitude of the region (the conversion depends on <i>PROJ_ELLIPSOID</i>). If /<i>y_inc</i> is given but set to 0 it will be reset equal to <i>x_inc</i>; otherwise it will be converted to degrees latitude. <code>All coordinates</code>: If <code>=</code> is appended then the corresponding max <i>x</i> (<i>east</i>) or <i>y</i> (<i>north</i>) may be slightly adjusted to fit exactly the given increment [by default the increment may be adjusted slightly to fit the given domain]. Finally, instead of giving an increment you may specify the <i>number of nodes</i> desired by appending <code>+</code> to the supplied integer argument; the increment is then recalculated from the number of nodes and the domain. The resulting increment value depends on whether you have selected a gridline-registered or pixel-registered grid; see <i>App-file-formats</i> for details. Note: if <code>-R</code><i>grdfile</i> is used then the grid spacing has already been initialized; use <code>-I</code> to override the values.</p>
<dt><code>-J</code><i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Select map projection.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-bo</code>[<i>ncols</i>][<i>type</i>] <i>(more &#8230;)</i></p>
<dd> Select native binary output.</p>
<dt><code>-do</code><i>nodata</i> <i>(more &#8230;)</i></p>
<dd> Replace output columns that equal NaN with <i>nodata</i>.</p>
<dt><code>-o</code><i>cols</i>[,&#8230;] <i>(more &#8230;)</i></p>
<dd> Select output columns (0 is first column). </p>
<pre>
This option applies only if no <code>-G</code> option has been set.
</pre>
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
<h2>EXAMPLES</h2>
<p> To extract data from raster 1, taking one point every 30 minutes, in an area extended beyond 360 degrees to allow later filtering, run </p>
<pre>
gmt grdraster 1 -R-4/364/-62/62 -I30m -Gdata.nc
</pre>
<p> To obtain data for an oblique Mercator projection we need to extract more data that is actually used. This is necessary because the output of <code>grdraster</code> has edges defined by parallels and meridians, while the oblique map in general does not. Hence, to get all the data from the ETOPO2 data needed to make a contour map for the region defined by its lower left and upper right corners and the desired projection, use </p>
<pre>
gmt grdraster ETOPO2 -R160/20/220/30r -Joc190/25.5/292/69/1 -Gdata.nc
</pre>
<p> To extract data from the 2 min Geoware relief blend and write it as binary double precision xyz-triplets to standard output: </p>
<pre>
gmt grdraster &quot;2 min Geoware&quot; -R20/25/-10/5 -bo &gt; triplets.b
</pre>
<h2>SEE ALSO</h2>
<p> <code>gmtdefaults</code>, <code>gmt</code>, <code>grdsample</code>, <code>grdfilter</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
