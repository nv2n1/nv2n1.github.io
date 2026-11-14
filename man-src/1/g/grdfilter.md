---
title: "grdfilter(1)"
name: "grdfilter"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grdfilter/"
description: "grdfilter – Filter a grid in the space (or time) domain"
---

<h2>NAME</h2>
<p> grdfilter &#8211; Filter a grid in the space (or time) domain</p>
<h2>SYNOPSIS</h2>
<p> <code>grdfilter</code> <i>ingrid</i> <i>distance_flag</i> <code>x</code><i>width</i>[/<i>width2</i>][<i>modifiers</i>] <i>outgrid</i> [ <i>increment</i> ] [ <code>i</code>|<code>p</code>|<code>r</code> ] [ <i>region</i> ] [ ] [ [<i>level</i>] ] [ <code>-f</code><i>&lt;flags&gt;</i> ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>grdfilter</code> will filter a grid file in the time domain using one of the selected convolution or non-convolution isotropic or rectangular filters and compute distances using Cartesian or Spherical geometries. The output grid file can optionally be generated as a sub-region of the input (via <code>-R</code>) and/or with new increment (via <code>-I</code>) or registration (via <code>-T</code>). In this way, one may have &quot;extra space&quot; in the input data so that the edges will not be used and the output can be within one half-width of the input edges. If the filter is low-pass, then the output may be less frequently sampled than the input.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>ingrid</i></p>
<dd> The grid file of points to be filtered. (See GRID FILE FORMATS below).</p>
<dt><code>-D</code><i>distance_flag</i></p>
<dd> Distance <i>flag</i> tells how grid (x,y) relates to filter <i>width</i> as follows: </p>
<p> <i>flag</i> = p: grid (px,py) with <i>width</i> an odd number of pixels; Cartesian distances. </p>
<p> <i>flag</i> = 0: grid (x,y) same units as <i>width</i>, Cartesian distances. </p>
<p> <i>flag</i> = 1: grid (x,y) in degrees, <i>width</i> in kilometers, Cartesian distances. </p>
<p> <i>flag</i> = 2: grid (x,y) in degrees, <i>width</i> in km, dx scaled by cos(middle y), Cartesian distances. </p>
<p> The above options are fastest because they allow weight matrix to be computed only once. The next three options are slower because they recompute weights for each latitude. </p>
<p> <i>flag</i> = 3: grid (x,y) in degrees, <i>width</i> in km, dx scaled by cosine(y), Cartesian distance calculation. </p>
<p> <i>flag</i> = 4: grid (x,y) in degrees, <i>width</i> in km, Spherical distance calculation. </p>
<p> <i>flag</i> = 5: grid (x,y) in Mercator <code>-Jm</code>1 img units, <i>width</i> in km, Spherical distance calculation.</p>
<dt><code>-Fx</code><i>width</i>[/<i>width2</i>][<i>modifiers</i>]</p>
<dd> Sets the filter type. Choose among convolution and non-convolution filters. Use any filter code <code>x</code> (listed below) followed by the full diameter <i>width</i>. This gives an isotropic filter; append /<i>width2</i> for a rectangular filter (requires <code>-Dp</code> or <code>-D0</code>). Some filters allow for optional arguments and modifiers. </p>
<p> Convolution filters (and their codes) are: </p>
<p> (<code>b</code>) Boxcar: All weights are equal. </p>
<p> (<code>c</code>) Cosine Arch: Weights follow a cosine arch curve. </p>
<p> (<code>g</code>) Gaussian: Weights are given by the Gaussian function, where <i>width</i> is 6 times the conventional Gaussian sigma. </p>
<p> (<code>f</code>) Custom: Weights are given by the precomputed values in the filter weight grid file <i>weight</i>, which must have odd dimensions; also requires <code>-D0</code> and output spacing must match input spacing or be integer multiples. </p>
<p> (<code>o</code>) Operator: Weights are given by the precomputed values in the filter weight grid file <i>weight</i>, which must have odd dimensions; also requires <code>-D0</code> and output spacing must match input spacing or be integer multiples. Weights are assumed to sum to zero so no accumulation of weight sums and normalization will be done. </p>
<p> Non-convolution filters (and their codes) are: </p>
<p> (<code>m</code>) Median: Returns median value. To select another quantile append <code>+q</code><i>quantile</i> in the 0-1 range [Default is 0.5, i.e., median]. </p>
<p> (<code>p</code>) Maximum likelihood probability (a mode estimator): Return modal value. If more than one mode is found we return their average value. Append <code>+l</code> or <code>+u</code> if you rather want to return the lowermost or uppermost of the modal values. </p>
<p> (<code>h</code>) Histogram mode (another mode estimator): Return the modal value as the center of the dominant peak in a histogram. Append /<i>binwidth</i> to specify the binning interval. Use modifier <code>+c</code> to center the bins on multiples of <i>binwidth</i> [Default has bin edges that are multiples of <i>binwidth</i>]. If more than one mode is found we return their average value. Append <code>+l</code> or <code>+u</code> if you rather want to return the lowermost or uppermost of the modal values. </p>
<p> (<code>l</code>) Lower: Return the minimum of all values. </p>
<p> (<code>L</code>) Lower: Return minimum of all positive values only. </p>
<p> (<code>u</code>) Upper: Return maximum of all values. </p>
<p> (<code>U</code>) Upper: Return maximum or all negative values only. </p>
<p> In the case of <code>L</code>|<code>U</code> it is possible that no data passes the initial sign test; in that case the filter will return NaN.</p>
<dt><code>-G</code><i>outgrid</i></p>
<dd> <i>outgrid</i> is the output grid file of the filter. (See GRID FILE FORMATS below).</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-I</code><i>xinc</i>[<i>unit</i>][<code>=</code>|<code>+</code>][/<i>yinc</i>[<i>unit</i>][<code>=</code>|<code>+</code>]]</p>
<dd> <i>x_inc</i> [and optionally <i>y_inc</i>] is the output Increment. Append <code>m</code> to indicate arc minutes, or <code>s</code> to indicate arc seconds. If the new <i>x_inc</i>, <i>y_inc</i> are NOT integer multiples of the old ones (in the input data), filtering will be considerably slower. [Default: Same as input.]</p>
<dt><code>-N</code><code>i</code>|<code>p</code>|<code>r</code></p>
<dd> Determine how NaN-values in the input grid affects the filtered output: Append <code>i</code> to ignore all NaNs in the calculation of filtered value [Default], <code>r</code> is same as <code>i</code> except if the input node was NaN then the output node will be set to NaN (only applies if both grids are co-registered), and <code>p</code> which will force the filtered value to be NaN if any grid-nodes with NaN-values are found inside the filter circle.</p>
<dt><code>-R</code></p>
<dd> <i>west</i>, <i>east</i>, <i>south</i>, and <i>north</i> defines the Region of the output points. [Default: Same as input.]</p>
<dt><code>-T</code></p>
<dd> Toggle the node registration for the output grid so as to become the opposite of the input grid [Default gives the same registration as the input grid].</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-f</code>[<code>i</code>|<code>o</code>]<i>colinfo</i> <i>(more &#8230;)</i></p>
<dd> Specify data types of input and/or output columns.</p>
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
<h2>GEOGRAPHICAL AND TIME COORDINATES</h2>
<p> When the output grid type is netCDF, the coordinates will be labeled &quot;longitude&quot;, &quot;latitude&quot;, or &quot;time&quot; based on the attributes of the input data or grid (if any) or on the <code>-f</code> or <code>-R</code> options. For example, both <code>-f0x</code> <code>-f1t</code> and <code>-R</code>90w/90e/0t/3t will result in a longitude/time grid. When the x, y, or z coordinate is time, it will be stored in the grid as relative time since epoch as specified by <i>TIME_UNIT</i> and <i>TIME_EPOCH</i> in the <code>gmt.conf</code> file or on the command line. In addition, the <code>unit</code> attribute of the time variable will indicate both this unit and epoch.</p>
<h2>EXAMPLES</h2>
<p> Suppose that north_pacific_etopo5.nc is a file of 5 minute bathymetry from 140E to 260E and 0N to 50N, and you want to find the medians of values within a 300km radius (600km full width) of the output points, which you choose to be from 150E to 250E and 10N to 40N, and you want the output values every 0.5 degree. Using spherical distance calculations, you need: </p>
<pre>
gmt grdfilter north_pacific_etopo5.nc -Gfiltered_pacific.nc -Fm600 \
              -D4 -R150/250/10/40 -I0.5 -V
</pre>
<p> If we instead wanted a high-pass result then one can perform the corresponding low-pass filter using a coarse grid interval as grdfilter will resample the result to the same resolution as the input grid so we can compute the residuals, e.g., </p>
<pre>
gmt grdfilter north_pacific_etopo5.nc -Gresidual_pacific.nc -Fm-600 \
              -D4 -R150/250/10/40 -I0.5 -V
</pre>
<p> Here, the residual_pacific.nc grid will have the same 5 minute resolution as the original. </p>
<p> To filter the dataset in ripples.nc using a custom anisotropic Gaussian filter exp (-0.5*r^2) whose distances r from the center is given by (2x^2 + y^2 -2xy)/6, with major axis at an angle of 63 degrees with the horizontal, try </p>
<pre>
gmt grdmath -R-10/10/-10/10 -I1 X 2 POW 2 MUL Y 2 POW ADD X Y MUL 2 MUL \
            SUB 6 DIV NEG 2 DIV EXP DUP SUM DIV = gfilter.nc
gmt grdfilter ripples.nc -Ffgfilter.nc -D0 -Gsmooth.nc -V
</pre>
<h2>LIMITATIONS</h2>
<p> To use the <code>-D</code>5 option the input Mercator grid must be created by img2mercgrd using the <code>-C</code> option so the origin of the y-values is the Equator (i.e., x = y = 0 correspond to lon = lat = 0).</p>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>grdfft</code> <code>img2grd</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
