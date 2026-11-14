---
title: "makecpt(1)"
name: "makecpt"
section: "1"
letter: "m"
url: "/docs/linux/man/1-makecpt/"
description: "makecpt – Make GMT color palette tables"
---

<h2>NAME</h2>
<p> makecpt &#8211; Make GMT color palette tables</p>
<h2>SYNOPSIS</h2>
<p> <code>makecpt</code> [ [<code>+</code>]<i>transparency</i> ] [ <i>cpt</i> ] [ [<code>i</code>|<code>o</code>] ] [ [<i>nlevels</i>] ] [ [<code>R</code>|<code>r</code>|<code>h</code>|<code>c</code> ] [ <i>zlo</i>/<i>zhi</i> ] [ ] [ ] [ ] [ [<code>i</code>|<code>o</code>] ] [ <i>z_min</i>/<i>z_max</i>[/<i>z_inc</i>[+]] | <code>-T</code><i>ztable</i> ] [ [<i>level</i>] ] [ ] [ ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>makecpt</code> is a utility that will help you make color palette tables (CPT files). You define an equidistant set of contour intervals or pass your own z-table, and create a new CPT file based on an existing master CPT file. The resulting CPT file can be reversed relative to the master cpt, and can be made continuous or discrete. For color tables beyond the standard GMT offerings, visit cpt-city: <i><a rel="nofollow" href="http://soliton.vm.bytemark.co.uk/pub/cpt-city/">http://soliton.vm.bytemark.co.uk/pub/cpt-city/</a></i>. </p>
<p> The CPT file includes three additional colors beyond the range of z-values. These are the background color (B) assigned to values lower than the lowest <i>z</i>-value, the foreground color (F) assigned to values higher than the highest <i>z</i>-value, and the NaN color (N) painted wherever values are undefined. </p>
<p> If the master CPT file includes B, F, and N entries, these will be copied into the new master file. If not, the parameters <i>COLOR_BACKGROUND</i>, <i>COLOR_FOREGROUND</i>, and <i>COLOR_NAN</i> from the <code>gmt.conf</code> file or the command line will be used. This default behavior can be overruled using the options <code>-D</code>, <code>-M</code> or <code>-N</code>. </p>
<p> The color model (RGB, HSV or CMYK) of the palette created by <code>makecpt</code> will be the same as specified in the header of the master CPT file. When there is no <i>COLOR_MODEL</i> entry in the master CPT file, the <i>COLOR_MODEL</i> specified in the <code>gmt.conf</code> file or on the command line will be used.</p>
<h2>REQUIRED ARGUMENTS</h2>
<p> None.</p>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-A</code>[<code>+</code>]<i>transparency</i></p>
<dd> Sets a constant level of transparency (0-100) for all color slices. Prepend <code>+</code> to also affect the fore-, back-, and nan-colors [Default is no transparency, i.e., 0 (opaque)].</p>
<dt><code>-C</code><i>cpt</i></p>
<dd> Selects the master color table CPT file to use in the interpolation. Choose among the built-in tables (type <code>makecpt</code> to see the list) or give the name of an existing CPT file [Default gives a rainbow CPT file]. Yet another option is to specify -Ccolor1,color2[,color3,&#8230;] to build a linear continuous cpt from those colors automatically. In this case <i>color</i><code>n</code> can be a r/g/b triplet, a color name, or an HTML hexadecimal color (e.g. #aabbcc ).</p>
<dt><code>-D</code>[<code>i</code>|<code>o</code>]</p>
<dd> Select the back- and foreground colors to match the colors for lowest and highest <i>z</i>-values in the output CPT file [Default uses the colors specified in the master file, or those defined by the parameters <i>COLOR_BACKGROUND</i>, <i>COLOR_FOREGROUND</i>, and <i>COLOR_NAN</i>]. Append <code>i</code> to match the colors for the lowest and highest values in the input (instead of the output) CPT file.</p>
<dt><code>-E</code>[<i>nlevels</i>]</p>
<dd> Implies reading data table(s) from given command-line files or standard input. We use the last data column to determine the data range; use <code>-i</code> to select another column, and use <code>-bi</code> if your data table is native binary. This z-range information is used instead of providing the <code>-T</code> option. We create a linear color table by dividing the table data z-range into <i>nlevels</i> equidistant slices. If <i>nlevels</i> is not given it defaults to the number of levels in the chosen CPT file.</p>
<dt><code>-F</code>[<code>R</code>|<code>r</code>|<code>h</code>|<code>c</code>]</p>
<dd> Force output CPT file to written with r/g/b codes, gray-scale values or color name (<code>R</code>, default) or r/g/b codes only (<code>r</code>), or h-s-v codes (<code>h</code>), or c/m/y/k codes (<code>c</code>).</p>
<dt><code>-G</code><i>zlo</i>/<i>zhi</i></p>
<dd> Truncate the incoming CPT so that the lowest and highest z-levels are to <i>zlo</i> and <i>zhi</i>. If one of these equal NaN then we leave that end of the CPT alone. The truncation takes place before any resampling.</p>
<dt><code>-I</code></p>
<dd> Reverses the sense of color progression in the master CPT file. Also exchanges the foreground and background colors, including those specified by the parameters <i>COLOR_BACKGROUND</i> and <i>COLOR_FOREGROUND</i>.</p>
<dt><code>-M</code></p>
<dd> Overrule background, foreground, and NaN colors specified in the master CPT file with the values of the parameters <i>COLOR_BACKGROUND</i>, <i>COLOR_FOREGROUND</i>, and <i>COLOR_NAN</i> specified in the <code>gmt.conf</code> file or on the command line. When combined with <code>-D</code>, only <i>COLOR_NAN</i> is considered.</p>
<dt><code>-N</code></p>
<dd> Do not write out the background, foreground, and NaN-color fields [Default will write them].</p>
<dt><code>-Q</code>[<code>i</code>|<code>o</code>]</p>
<dd> Selects a logarithmic interpolation scheme [Default is linear]. <code>-Qi</code> expects input z-values to be log10(z), assigns colors, and writes out z [Default]. <code>-Qo</code> takes log10(z) first, assigns colors, and writes out z.</p>
<dt><code>-T</code><i>z_min</i>/<i>z_max</i>[/<i>z_inc</i>[+]] | <code>-T</code><i>ztable</i></p>
<dd> Defines the range of the new CPT file by giving the lowest and highest z-value and interval. When used with <code>-C</code> and <i>z_inc</i> is not specified, the number of intervals remains the same as in the input palette. If <i>z_inc</i> is specified with a trailing <code>+</code> we interpret <i>z_inc</i> as the number of desired intervals instead. Alternatively, give the name of a ASCII file that has one z-value per record. If <code>-T</code> is not given, the existing range in the master CPT file will be used intact.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-W</code></p>
<dd> Do not interpolate the input color table but pick the output colors starting at the beginning of the color table, until colors for all intervals are assigned. This is particularly useful in combination with a categorical color table, like &quot;categorical&quot;. Cannot be used in combination with <code>-Z</code>.</p>
<dt><code>-Z</code></p>
<dd> Creates a continuous CPT file [Default is discontinuous, i.e., constant colors for each interval].</p>
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
<p> To make a CPT file with z-values from -200 to 200, with discrete color changes every 25, and using a polar blue-white-red colortable: </p>
<pre>
gmt makecpt -Cpolar -T-200/200/25 &gt; colors.cpt
</pre>
<p> To make an equidistant CPT file from z = -2 to 6, in steps of 1, using continuous default rainbow colors: </p>
<pre>
gmt makecpt -T-2/6/1 -Z &gt; rainbow.cpt
</pre>
<p> To make a GEBCO look-alike CPT file for bathymetry, run </p>
<pre>
gmt makecpt -Cgebco &gt; my_gebco.cpt
</pre>
<p> To create a 24-level rainbow color table suitable for plotting the depths in the data table depths.txt (with lon, lat, depths), run </p>
<pre>
gmt makecpt -Cgebco depths.txt -i2 -Z -E24 &gt; my_depths.cpt
</pre>
<h2>BUGS</h2>
<p> Since <code>makecpt</code> will also interpolate from any existing CPT file you may have in your directory, you cannot use one of the listed cpt names as an output filename; hence the my_gebco.cpt in the example.</p>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>grd2cpt</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
