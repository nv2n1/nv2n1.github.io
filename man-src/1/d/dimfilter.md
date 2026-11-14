---
title: "dimfilter(1)"
name: "dimfilter"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dimfilter/"
description: "dimfilter – Directional filtering of 2-D gridded files in the space (or time) domain"
---

<h2>NAME</h2>
<p> dimfilter &#8211; Directional filtering of 2-D gridded files in the space (or time) domain</p>
<h2>SYNOPSIS</h2>
<p> <code>dimfilter</code> <i>input_file.nc</i> <i>distance_flag</i> <i>&lt;filtertype&gt;&lt;width&gt;</i>[<i>mode</i>] <i>output_file.nc</i> <i>&lt;filtertype&gt;&lt;n_sectors&gt;</i> [ <i>cols</i> ] [ <i>increment</i> ] [ <i>region</i> ] [ ] [ [<i>level</i>] ] [ <code>-f</code><i>&lt;flags&gt;</i> ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>dimfilter</code> will filter a <i>.nc</i> file in the space (or time) domain by dividing the given filter circle into <i>n_sectors</i>, applying one of the selected primary convolution or non-convolution filters to each sector, and choosing the final outcome according to the selected secondary filter. It computes distances using Cartesian or Spherical geometries. The output <i>.nc</i> file can optionally be generated as a subregion of the input and/or with a new <code>-I</code>ncrement. In this way, one may have &quot;extra space&quot; in the input data so that there will be no edge effects for the output grid. If the filter is low-pass, then the output may be less frequently sampled than the input. <code>-Q</code> is for the error analysis mode and only requires the total number of columns in the input file, which contains the filtered depths. Finally, one should know that <code>dimfilter</code> will not produce a smooth output as other spatial filters do because it returns a minimum median out of <i>N</i> medians of <i>N</i> sectors. The output can be rough unless the input data is noise-free. Thus, an additional filtering (e.g., Gaussian via <code>grdfilter</code>) of the DiM-filtered data is generally recommended.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>input_file.nc</i></p>
<dd> The data grid to be filtered.</p>
<dt><code>-D</code><i>distance_flag</i></p>
<dd> Distance <i>flag</i> tells how grid (x,y) relates to filter <i>width</i>, as follows: </p>
<p> <i>flag</i> = 0: grid (x,y) same units as <i>width</i>, Cartesian distances. <i>flag</i> = 1: grid (x,y) in degrees, <i>width</i> in kilometers, Cartesian distances. <i>flag</i> = 2: grid (x,y) in degrees, <i>width</i> in km, dx scaled by cos(middle y), Cartesian distances. </p>
<p> The above options are fastest because they allow weight matrix to be computed only once. The next three options are slower because they recompute weights for each latitude. </p>
<p> <i>flag</i> = 3: grid (x,y) in degrees, <i>width</i> in km, dx scaled by cosine(y), Cartesian distance calculation. </p>
<p> <i>flag</i> = 4: grid (x,y) in degrees, <i>width</i> in km, Spherical distance calculation.</p>
<dt><code>-F</code><i>&lt;filtertype&gt;&lt;width&gt;</i>[<i>mode</i>]</p>
<dd> Sets the primary filter type. Choose among convolution and non-convolution filters. Append the filter code followed by the full diameter <i>width</i>. Available convolution filters are: </p>
<p> (<code>b</code>) Boxcar: All weights are equal. </p>
<p> (<code>c</code>) Cosine Arch: Weights follow a cosine arch curve. </p>
<p> (<code>g</code>) Gaussian: Weights are given by the Gaussian function. </p>
<p> Non-convolution filters are: </p>
<p> (<code>m</code>) Median: Returns median value. </p>
<p> (<code>p</code>) Maximum likelihood probability (a mode estimator): Return modal value. If more than one mode is found we return their average value. Append &#8211; or + to the filter width if you rather want to return the smallest or largest of the modal values.</p>
<dt><code>-N</code><i>&lt;filtertype&gt;&lt;n_sectors&gt;</i></p>
<dd> Sets the secondary filter type and the number of bow-tie sectors. <i>n_sectors</i> must be integer and larger than 0. When <i>n_sectors</i> is set to 1, the secondary filter is not effective. Available secondary filters are: </p>
<p> (<code>l</code>) Lower: Return the minimum of all filtered values. </p>
<p> (<code>u</code>) Upper: Return the maximum of all filtered values. </p>
<p> (<code>a</code>) Average: Return the mean of all filtered values. </p>
<p> (<code>m</code>) Median: Return the median of all filtered values. </p>
<p> (<code>p</code>) Mode: Return the mode of all filtered values.</p>
<dt><code>-G</code><i>output_file.nc</i></p>
<dd> <i>output_file.nc</i> is the output of the filter.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-I</code></p>
<dd> <i>x_inc</i> [and optionally <i>y_inc</i>] is the output Increment. Append <code>m</code> to indicate minutes, or <code>c</code> to indicate seconds. If the new <i>x_inc</i>, <i>y_inc</i> are NOT integer multiples of the old ones (in the input data), filtering will be considerably slower. [Default: Same as input.]</p>
<dt><code>-R</code></p>
<dd> <i>west</i>, <i>east</i>, <i>south</i>, and <i>north</i> defines the Region of the output points. [Default: Same as input.]</p>
<dt><code>-T</code></p>
<dd> Toggle the node registration for the output grid so as to become the opposite of the input grid [Default gives the same registration as the input grid].</p>
<dt><code>-Q</code><i>cols</i></p>
<dd> <i>cols</i> is the total number of columns in the input text table file. For this mode, it expects to read depths consisted of several columns. Each column represents a filtered grid with a filter width, which can be obtained by <code>grd2xyz -Z</code>. The outcome will be median, MAD, and mean. So, the column with the medians is used to generate the regional component and the column with the MADs is used to conduct the error analysis.</p>
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
<p> Suppose that north_pacific_dbdb5.nc is a file of 5 minute bathymetry from 140E to 260E and 0N to 50N, and you want to find the medians of values within a 300km radius (600km full width) of the output points, which you choose to be from 150E to 250E and 10N to 40N, and you want the output values every 0.5 degree. To prevent the medians from being biased by the sloping plane, you want to divide the filter circle into 6 sectors and to choose the lowest value among 6 medians. Using spherical distance calculations, you need: </p>
<pre>
gmt dimfilter north_pacific_dbdb5.nc -Gfiltered_pacific.nc -Fm600 -D4 \
    -Nl6 -R150/250/10/40 -I0.5 -V
</pre>
<p> Suppose that cape_verde.nc is a file of 0.5 minute bathymetry from 32W to 15W and 8N to 25N, and you want to remove small-length-scale features in order to define a swell in an area extending from 27.5W to 20.5W and 12.5N to 19.5N, and you want the output value every 2 minute. Using cartesian distance calculations, you need: </p>
<pre>
gmt dimfilter cape_verde.nc -Gt.nc -Fm220 -Nl8 -D2 -R-27.5/-20.5/12.5/19.5 -I2m -V
gmt grdfilter t.nc -Gcape_swell.nc -Fg50 -D2 -V
</pre>
<p> Suppose that you found a range of filter widths for a given area, and you filtered the given bathymetric data using the range of filter widths (e.g., <i>f100.nc f110.nc f120.nc f130.nc</i>), and you want to define a regional trend using the range of filter widths, and you want to obtain median absolute deviation (MAD) estimates at each data point. Then, you will need to do: </p>
<pre>
gmt grd2xyz f100.nc -Z &gt; f100.d
gmt grd2xyz f110.nc -Z &gt; f110.d
gmt grd2xyz f120.nc -Z &gt; f120.d
gmt grd2xyz f130.nc -Z &gt; f130.d
paste f100.d f110.d f120.d f130.d &gt; depths.d
gmt dimfilter depths.d -Q4 &gt; output.z
</pre>
<h2>LIMITATIONS</h2>
<p> When working with geographic (lat, lon) grids, all three convolution filters (boxcar, cosine arch, and gaussian) will properly normalize the filter weights for the variation in gridbox size with latitude, and correctly determine which nodes are needed for the convolution when the filter &quot;circle&quot; crosses a periodic (0-360) boundary or contains a geographic pole. However, the spatial filters, such as median and mode filters, do not use weights and thus should only be used on Cartesian grids (or at very low latitudes) only. If you want to apply such spatial filters you should project your data to an equal-area projection and run dimfilter on the resulting Cartesian grid.</p>
<h2>SCRIPT TEMPLATE</h2>
<p> The dim.template.sh is a skeleton shell script that can be used to set up a complete DiM analysis, including the MAD analysis.</p>
<h2>REFERENCE</h2>
<p> Kim, S.-S., and Wessel, P. (2008), Directional Median Filtering for Regional-Residual Separation of Bathymetry, <i>Geochem. Geophys. Geosyst.</i>, <code>9</code>, Q03005, doi:10.1029/2007GC001850.</p>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>grdfilter</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
