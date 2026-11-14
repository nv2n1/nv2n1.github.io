---
title: "grdtrend(1)"
name: "grdtrend"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grdtrend/"
description: "grdtrend – Fit trend surface to grids and compute residuals"
---

<h2>NAME</h2>
<p> grdtrend &#8211; Fit trend surface to grids and compute residuals</p>
<h2>SYNOPSIS</h2>
<p> <code>grdtrend</code> <i>grdfile</i> <i>n_model</i>[<code>r</code>] [ <i>diff.nc</i> ] [ <i>region</i> ] [ <i>trend.nc</i> ] [ <i>weight.nc</i> ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>grdtrend</code> reads a 2-D grid file and fits a low-order polynomial trend to these data by [optionally weighted] least-squares. The trend surface is defined by: m1 + m2*x + m3*y + m4*x*y + m5*x*x + m6*y*y + m7*x*x*x + m8*x*x*y + m9*x*y*y + m10*y*y*y. </p>
<p> The user must specify <code>-N</code><i>n_model</i>, the number of model parameters to use; thus, <code>-N</code><i>3</i> fits a bilinear trend, <code>-N</code><i>6</i> a quadratic surface, and so on. Optionally, append <code>r</code> to the <code>-N</code> option to perform a robust fit. In this case, the program will iteratively reweight the data based on a robust scale estimate, in order to converge to a solution insensitive to outliers. This may be handy when separating a &quot;regional&quot; field from a &quot;residual&quot; which should have non-zero mean, such as a local mountain on a regional surface. </p>
<p> If data file has values set to NaN, these will be ignored during fitting; if output files are written, these will also have NaN in the same locations.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>grdfile</i></p>
<dd> The name of a 2-D binary grid file.</p>
<dt><code>-N</code><i>n_model</i>[<code>r</code>]</p>
<dd> <i>n_model</i> sets the number of model parameters to fit. Append <code>r</code> for robust fit.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-D</code><i>diff.nc</i></p>
<dd> Write the difference (input data &#8211; trend) to the file <i>diff.nc</i>.</p>
<dt><code>-R</code>[<i>unit</i>]<i>xmin</i>/<i>xmax</i>/<i>ymin</i>/<i>ymax</i>[<code>r</code>] <i>(more &#8230;)</i></p>
<dd> Specify the region of interest. Using the <code>-R</code> option will select a subsection of the input grid. If this subsection exceeds the boundaries of the grid, only the common region will be extracted.</p>
<dt><code>-T</code><i>trend.nc</i></p>
<dd> Write the fitted trend to the file <i>trend.nc</i>.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-W</code><i>weight.nc</i></p>
<dd> If <i>weight.nc</i> exists, it will be read and used to solve a weighted least-squares problem. [Default: Ordinary least-squares fit.] If the robust option has been selected, the weights used in the robust fit will be written to <i>weight.nc</i>.</p>
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
<h2>REMARKS</h2>
<p> The domain of x and y will be shifted and scaled to [-1, 1] and the basis functions are built from Legendre polynomials. These have a numerical advantage in the form of the matrix which must be inverted and allow more accurate solutions. NOTE: The model parameters listed with <code>-V</code> are Legendre polynomial coefficients; they are not numerically equivalent to the m#s in the equation described above. The description above is to allow the user to match <code>-N</code> with the order of the polynomial surface. See <code>grdmath</code> if you need to evaluate the trend using the reported coefficients.</p>
<h2>GRID FILE FORMATS</h2>
<p> By default GMT writes out grid as single precision floats in a COARDS-complaint netCDF file format. However, GMT is able to produce grid files in many other commonly used grid file formats and also facilitates so called &quot;packing&quot; of grids, writing out floating point data as 1- or 2-byte integers. To specify the precision, scale and offset, the user should add the suffix <code>=</code><i>id</i>[<code>/</code><i>scale</i><code>/</code><i>offset</i>[<code>/</code><i>nan</i>]], where <i>id</i> is a two-letter identifier of the grid type and precision, and <i>scale</i> and <i>offset</i> are optional scale factor and offset to be applied to all grid values, and <i>nan</i> is the value used to indicate missing data. In case the two characters <i>id</i> is not provided, as in <code>=/</code><i>scale</i> than a <i>id</i><code>=</code><i>nf</i> is assumed. When reading grids, the format is generally automatically recognized. If not, the same suffix can be added to input grid file names. See <code>grdconvert</code> and Section <i>grid-file-format</i> of the GMT Technical Reference and Cookbook for more information. </p>
<p> When reading a netCDF file that contains multiple grids, GMT will read, by default, the first 2-dimensional grid that can find in that file. To coax GMT into reading another multi-dimensional variable in the grid file, append <code>?</code><i>varname</i> to the file name, where <i>varname</i> is the name of the variable. Note that you may need to escape the special meaning of <code>?</code> in your shell program by putting a backslash in front of it, or by placing the filename and suffix between quotes or double quotes. The <code>?</code><i>varname</i> suffix can also be used for output grids to specify a variable name different from the default: &quot;z&quot;. See <code>grdconvert</code> and Sections <i>modifiers-for-CF</i> and <i>grid-file-format</i> of the GMT Technical Reference and Cookbook for more information, particularly on how to read splices of 3-, 4-, or 5-dimensional grids.</p>
<h2>EXAMPLES</h2>
<p> To remove a planar trend from hawaii_topo.nc and write result in hawaii_residual.nc: </p>
<pre>
gmt grdtrend hawaii_topo.nc -N3 -Dhawaii_residual.nc
</pre>
<p> To do a robust fit of a bicubic surface to hawaii_topo.nc, writing the result in hawaii_trend.nc and the weights used in hawaii_weight.nc, and reporting the progress: </p>
<pre>
gmt grdtrend hawaii_topo.nc -N10r -Thawaii_trend.nc -Whawaii_weight.nc -V
</pre>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>grdfft</code>, <code>grdfilter</code>, <code>grdmath</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
