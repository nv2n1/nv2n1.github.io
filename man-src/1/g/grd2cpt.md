---
title: "grd2cpt(1)"
name: "grd2cpt"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grd2cpt/"
description: "grd2cpt – Make linear or histogram-equalized color palette table from grid"
---

<h2>NAME</h2>
<p> grd2cpt &#8211; Make linear or histogram-equalized color palette table from grid</p>
<h2>SYNOPSIS</h2>
<p> <code>grd2cpt</code> <i>grid</i> [ [<code>+</code>]<i>transparency</i> ] [ <i>cpt</i> ] [ [<code>i</code>|<code>o</code>] ] [ <i>nlevels</i> ] [ [<code>R</code>|<code>r</code>|<code>h</code>|<code>c</code> ] [ <i>zlo</i>/<i>zhi</i> ] [ ] [ <i>minlimit/maxlimit</i> ] [ ] [ ] [ [<code>i</code>|<code>o</code>] ] [ <i>region</i> ] [ <i>zstart/zstop/zinc</i> ] [ <code>&#8211;</code>|<code>+</code>|<code>_</code>|<code>=</code> ] [ [<i>level</i>] ] [ ] [ ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>grd2cpt</code> reads one or more grid files and writes a color palette (CPT) file to standard output. The CPT file is based on an existing master CPT file of your choice, and the mapping from data value to colors is through the data&#8217;s cumulative distribution function (CDF), so that the colors are histogram equalized. Thus if the grid(s) and the resulting CPT file are used in <code>grdimage</code> with a linear projection, the colors will be uniformly distributed in area on the plot. Let z be the data values in the grid. Define CDF(Z) = (# of z &lt; Z) / (# of z in grid). (NaNs are ignored). These z-values are then normalized to the master CPT file and colors are sampled at the desired intervals. </p>
<p> The color palette includes three additional colors beyond the range of z-values. These are the background color (B) assigned to values lower than the lowest <i>z</i>-value, the foreground color (F) assigned to values higher than the highest <i>z</i>-value, and the NaN color (N) painted wherever values are undefined. For color tables beyond the standard GMT offerings, visit cpt-city: <i><a rel="nofollow" href="http://soliton.vm.bytemark.co.uk/pub/cpt-city/">http://soliton.vm.bytemark.co.uk/pub/cpt-city/</a></i>. </p>
<p> If the master CPT file includes B, F, and N entries, these will be copied into the new master file. If not, the parameters <i>COLOR_BACKGROUND</i>, <i>COLOR_FOREGROUND</i>, and <i>COLOR_NAN</i> from the <code>gmt.conf</code> file or the command line will be used. This default behavior can be overruled using the options <code>-D</code>, <code>-M</code> or <code>-N</code>. </p>
<p> The color model (RGB, HSV or CMYK) of the palette created by <code>makecpt</code> will be the same as specified in the header of the master CPT file. When there is no <i>COLOR_MODEL</i> entry in the master CPT file, the <i>COLOR_MODEL</i> specified in the <code>gmt.conf</code> file or on the command line will be used.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>grid</i></p>
<dd> Names of one or more grid files used to derive the color palette table. All grids need to have the same size and dimensions. (See GRID FILE FORMATS below).</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-A</code>[<code>+</code>]<i>transparency</i></p>
<dd> Sets a constant level of transparency (0-100) for all color slices. Prepend <code>+</code> to also affect the fore-, back-, and nan-colors [Default is no transparency, i.e., 0 (opaque)].</p>
<dt><code>-C</code><i>cpt</i></p>
<dd> Selects the master color table to use in the interpolation. Choose among the built-in tables (type <code>grd2cpt</code> to see the list) or give the name of an existing CPT file [Default gives a rainbow CPT file]. Yet another option is to specify -Ccolor1,color2[,color3,&#8230;] to build a linear continuous CPT from those colors automatically. In this case <i>color</i><code>n</code> can be a r/g/b triplet, a color name, or an HTML hexadecimal color (e.g. #aabbcc ).</p>
<dt><code>-D</code>[<code>i</code>|<code>o</code>]</p>
<dd> Select the back- and foreground colors to match the colors for lowest and highest <i>z</i>-values in the output CPT file [Default uses the colors specified in the master file, or those defined by the parameters <i>COLOR_BACKGROUND</i>, <i>COLOR_FOREGROUND</i>, and <i>COLOR_NAN</i>]. Append <code>i</code> to match the colors for the lowest and highest values in the input (instead of the output) CPT file.</p>
<dt><code>-E</code><i>nlevels</i></p>
<dd> Create a linear color table by dividing the grid z-range into <i>nlevels</i> equidistant slices.</p>
<dt><code>-F</code>[<code>R</code>|<code>r</code>|<code>h</code>|<code>c</code>]</p>
<dd> Force output CPT file to written with r/g/b codes, gray-scale values or color name (<code>R</code>, default) or r/g/b codes only (<code>r</code>), or h-s-v codes (<code>h</code>), or c/m/y/k codes (<code>c</code>).</p>
<dt><code>-G</code><i>zlo</i>/<i>zhi</i></p>
<dd> Truncate the incoming CPT so that the lowest and highest z-levels are to <i>zlo</i> and <i>zhi</i>. If one of these equal NaN then we leave that end of the CPT alone. The truncation takes place before any resampling.</p>
<dt><code>-I</code></p>
<dd> Reverses the sense of color progression in the master CPT file. Also exchanges the foreground and background colors, including those specified by the parameters <i>COLOR_BACKGROUND</i> and <i>COLOR_FOREGROUND</i>.</p>
<dt><code>-L</code><i>minlimit/maxlimit</i></p>
<dd> Limit range of CPT file to <i>minlimit/maxlimit</i>, and don&#8217;t count data outside this range when estimating CDF(Z). [Default uses min and max of data.]</p>
<dt><code>-M</code></p>
<dd> Overrule background, foreground, and NaN colors specified in the master CPT file with the values of the parameters <i>COLOR_BACKGROUND</i>, <i>COLOR_FOREGROUND</i>, and <i>COLOR_NAN</i> specified in the <code>gmt.conf</code> file or on the command line. When combined with <code>-D</code>, only <i>COLOR_NAN</i> is considered.</p>
<dt><code>-N</code></p>
<dd> Do not write out the background, foreground, and NaN-color fields [Default will write them].</p>
<dt><code>-Q</code>[<code>i</code>|<code>o</code>]</p>
<dd> Selects a logarithmic interpolation scheme [Default is linear]. <code>-Qi</code> expects input z-values to be log10(z), assigns colors, and writes out z [Default]. <code>-Qo</code> takes log10(z) first, assigns colors, and writes out z.</p>
<dt><code>-R</code>[<i>unit</i>]<i>xmin</i>/<i>xmax</i>/<i>ymin</i>/<i>ymax</i>[<code>r</code>] <i>(more &#8230;)</i></p>
<dd> Specify the region of interest.</p>
<dt><code>-S</code><i>zstart/zstop/zinc</i> or <code>-S</code><i>n</i></p>
<dd> Set steps in CPT file. Calculate entries in CPT file from <i>zstart</i> to <i>zstop</i> in steps of (<i>zinc</i>). Default chooses arbitrary values by a crazy scheme based on equidistant values for a Gaussian CDF. Use <code>-S</code><i>n</i> to select <i>n</i> points from such a cumulative normal distribution [11].</p>
<dt><code>-T</code><code>&#8211;</code>|<code>+</code>|<code>_</code>|<code>=</code></p>
<dd> Force the color table to be symmetric about zero (from -R to +R). Append flag to set the range R: <code>&#8211;</code> for R =|zmin|, <code>+</code> for R = |zmax|, <code>_</code> for R = min(|zmin|, |zmax|), or <code>=</code> for R = max(|zmin|, |zmax|).</p>
<dt><code>-V</code></p>
<dd> Verbose operation. This will write CDF(Z) estimates to stderr. [Default is silent.]</p>
<dt><code>-W</code></p>
<dd> Do not interpolate the input color table but pick the output colors starting at the beginning of the map. This is particularly useful in combination with a categorical color table. Cannot be used in combination with <code>-Z</code>.</p>
<dt><code>-Z</code></p>
<dd> Will create a continuous color palette. [Default is discontinuous, i.e., constant color intervals]</p>
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
<h2>GRID FILE FORMATS</h2>
<p> By default GMT writes out grid as single precision floats in a COARDS-complaint netCDF file format. However, GMT is able to produce grid files in many other commonly used grid file formats and also facilitates so called &quot;packing&quot; of grids, writing out floating point data as 1- or 2-byte integers. To specify the precision, scale and offset, the user should add the suffix <code>=</code><i>id</i>[<code>/</code><i>scale</i><code>/</code><i>offset</i>[<code>/</code><i>nan</i>]], where <i>id</i> is a two-letter identifier of the grid type and precision, and <i>scale</i> and <i>offset</i> are optional scale factor and offset to be applied to all grid values, and <i>nan</i> is the value used to indicate missing data. In case the two characters <i>id</i> is not provided, as in <code>=/</code><i>scale</i> than a <i>id</i><code>=</code><i>nf</i> is assumed. When reading grids, the format is generally automatically recognized. If not, the same suffix can be added to input grid file names. See <code>grdconvert</code> and Section <i>grid-file-format</i> of the GMT Technical Reference and Cookbook for more information. </p>
<p> When reading a netCDF file that contains multiple grids, GMT will read, by default, the first 2-dimensional grid that can find in that file. To coax GMT into reading another multi-dimensional variable in the grid file, append <code>?</code><i>varname</i> to the file name, where <i>varname</i> is the name of the variable. Note that you may need to escape the special meaning of <code>?</code> in your shell program by putting a backslash in front of it, or by placing the filename and suffix between quotes or double quotes. The <code>?</code><i>varname</i> suffix can also be used for output grids to specify a variable name different from the default: &quot;z&quot;. See <code>grdconvert</code> and Sections <i>modifiers-for-CF</i> and <i>grid-file-format</i> of the GMT Technical Reference and Cookbook for more information, particularly on how to read splices of 3-, 4-, or 5-dimensional grids.</p>
<h2>EXAMPLES</h2>
<p> Sometimes you don&#8217;t want to make a CPT file (yet) but would find it helpful to know that 90% of your data lie between z1 and z2, something you cannot learn from <code>grdinfo</code>. So you can do this to see some points on the CDF(Z) curve (use <code>-V</code> option to see more): </p>
<pre>
gmt grd2cpt mydata.nc -V &gt; /dev/null
</pre>
<p> To make a CPT file with entries from 0 to 200 in steps of 20, and ignore data below zero in computing CDF(Z), and use the built-in master cpt file relief, run </p>
<pre>
gmt grd2cpt mydata.nc -Crelief -L0/10000 -S0/200/20 &gt; mydata.cpt
</pre>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>gmt.conf</code>, <code>grdhisteq</code>, <code>grdinfo</code>, <code>makecpt</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
