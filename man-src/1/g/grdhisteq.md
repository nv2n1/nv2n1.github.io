---
title: "grdhisteq(1)"
name: "grdhisteq"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grdhisteq/"
description: "grdhisteq – Perform histogram equalization for a grid"
---

<h2>NAME</h2>
<p> grdhisteq &#8211; Perform histogram equalization for a grid</p>
<h2>SYNOPSIS</h2>
<p> <code>grdhisteq</code> <i>in_grdfile</i> [ <i>out_grdfile</i> ] [ <i>n_cells</i> ] [ [<i>file</i>] ] [ [<i>norm</i>] ] [ ] <i>region</i> [<i>level</i>] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>grdhisteq</code> allows the user to find the data values which divide a given grid file into patches of equal area. One common use of <code>grdhisteq</code> is in a kind of histogram equalization of an image. In this application, the user might have a grid of flat topography with a mountain in the middle. Ordinary gray shading of this file (using grdimage/grdview) with a linear mapping from topography to graytone will result in most of the image being very dark gray, with the mountain being almost white. One could use <code>grdhisteq</code> to write to stdout or file an ASCII list of those data values which divide the range of the data into <i>n_cells</i> segments, each of which has an equal area in the image. Using <code>awk</code> or <code>makecpt</code> one can take this output and build a CPT file; using the CPT file with grdimage will result in an image with all levels of gray occurring equally. Alternatively, see <code>grd2cpt</code>. </p>
<p> The second common use of <code>grdhisteq</code> is in writing a grid with statistics based on some kind of cumulative distribution function. In this application, the output has relative highs and lows in the same (x,y) locations as the input file, but the values are changed to reflect their place in some cumulative distribution. One example would be to find the lowest 10% of the data: Take a grid, run <code>grdhisteq</code> and make a grid using <i>n_cells</i> = 10, and then contour the result to trace the 1 contour. This will enclose the lowest 10% of the data, regardless of their original values. Another example is in equalizing the output of <code>grdgradient</code>. For shading purposes it is desired that the data have a smooth distribution, such as a Gaussian. If you run <code>grdhisteq</code> on output from <code>grdgradient</code> and make a grid file output with the Gaussian option, you will have a grid whose values are distributed according to a Gaussian distribution with zero mean and unit variance. The locations of these values will correspond to the locations of the input; that is, the most negative output value will be in the (x,y) location of the most negative input value, and so on.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>in_grdfile</i></p>
<dd> 2-D grid file to be equalized. (See GRID FILE FORMATS below).</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-C</code><i>n_cells</i></p>
<dd> Sets how many cells (or divisions) of data range to make [16].</p>
<dt><code>-D</code></p>
<dd> Dump level information to <i>file</i>, or standard output if no file is provided.</p>
<dt><code>-G</code><i>out_grdfile</i></p>
<dd> Name of output 2-D grid file. Used with <code>-N</code> only. (See GRID FILE FORMATS below).</p>
<dt><code>-N</code>[<i>norm</i>]</p>
<dd> Gaussian output. Use with <code>-G</code> to make an output grid with standard normal scores. Append <i>norm</i> to force the scores to fall in the &lt;-1,+1&gt; range [Default is standard normal scores].</p>
<dt><code>-Q</code></p>
<dd> Use quadratic intensity scaling. [Default is linear].</p>
<dt><code>-R</code>[<i>unit</i>]<i>xmin</i>/<i>xmax</i>/<i>ymin</i>/<i>ymax</i>[<code>r</code>] <i>(more &#8230;)</i></p>
<dd> Specify the region of interest. Using the <code>-R</code> option will select a subsection of <i>in_grdfile</i> grid. If this subsection exceeds the boundaries of the grid, only the common region will be extracted.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
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
<p> To find the height intervals that divide the file heights.nc into 16 divisions of equal area: </p>
<pre>
gmt grdhisteq heights.nc -C16 -D &gt; levels.d
</pre>
<p> To make the poorly distributed intensities in the file raw_intens.nc suitable for use with <code>grdimage</code> or <code>grdview</code>, run </p>
<pre>
gmt grdhisteq raw_intens.nc -Gsmooth_intens.nc -N -V
</pre>
<h2>RESTRICTIONS</h2>
<p> If you use <code>grdhisteq</code> to make a Gaussian output for gradient shading in <code>grdimage</code> or <code>grdview</code>, you should be aware of the following: the output will be in the range [-x, x], where x is based on the number of data in the input grid (nx * ny) and the cumulative Gaussian distribution function F(x). That is, let N = nx * ny. Then x will be adjusted so that F(x) = (N &#8211; 1 + 0.5)/N. Since about 68% of the values from a standard normal distribution fall within +/- 1, this will be true of the output grid. But if N is very large, it is possible for x to be greater than 4. Therefore, with the <code>grdview</code> program clipping gradients to the range [-1, 1], you will get correct shading of 68% of your data, while 16% of them will be clipped to -1 and 16% of them clipped to +1. If this makes too much of the image too light or too dark, you should take the output of <code>grdhisteq</code> and rescale it using <code>grdmath</code> and multiplying by something less than 1.0, to shrink the range of the values, thus bringing more than 68% of the image into the range [-1, 1]. Alternatively, supply a normalization factor with <code>-N</code>.</p>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>gmt.conf</code>, <code>grd2cpt</code>, <code>grdgradient</code>, <code>grdimage</code>, <code>grdmath</code>, <code>grdview</code>, <code>makecpt</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
