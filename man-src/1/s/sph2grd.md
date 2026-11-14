---
title: "sph2grd(1)"
name: "sph2grd"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sph2grd/"
description: "sph2grd – Compute grid from spherical harmonic coefficients"
---

<h2>NAME</h2>
<p> sph2grd &#8211; Compute grid from spherical harmonic coefficients</p>
<h2>SYNOPSIS</h2>
<p> <code>sph2grd</code> [ <i>table</i> ] <i>grdfile</i> <i>increment</i> <i>region</i> [ [<code>g</code>|<code>n</code>] ] [ ] [ [<code>k</code>]<i>filter</i> ] [ [<i>norm</i>] ] [ ] [ [<i>level</i>] ] [ <code>-bi</code><i>&lt;binary&gt;</i> ] [ <code>-h</code><i>&lt;headers&gt;</i> ] [ <code>-i</code><i>&lt;flags&gt;</i> ] [ <code>-r</code> ] [ <code>-x</code>[[-]<i>n</i>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>sph2grd</code> reads a spherical harmonics coefficient table with records of L, M, C[L,M], S[L,M] and evaluates the spherical harmonic model on the specified grid.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><code>-G</code><i>grdfile</i></p>
<dd> <i>grdfile</i> is the name of the binary output grid file. (See GRID FILE FORMAT below.)</p>
<dt><code>-I</code><i>xinc</i>[<i>unit</i>][<code>=</code>|<code>+</code>][/<i>yinc</i>[<i>unit</i>][<code>=</code>|<code>+</code>]]</p>
<dd> <i>x_inc</i> [and optionally <i>y_inc</i>] is the grid spacing. Optionally, append a suffix modifier. <code>Geographical (degrees) coordinates</code>: Append <code>m</code> to indicate arc minutes or <code>s</code> to indicate arc seconds. If one of the units <code>e</code>, <code>f</code>, <code>k</code>, <code>M</code>, <code>n</code> or <code>u</code> is appended instead, the increment is assumed to be given in meter, foot, km, Mile, nautical mile or US survey foot, respectively, and will be converted to the equivalent degrees longitude at the middle latitude of the region (the conversion depends on <i>PROJ_ELLIPSOID</i>). If /<i>y_inc</i> is given but set to 0 it will be reset equal to <i>x_inc</i>; otherwise it will be converted to degrees latitude. <code>All coordinates</code>: If <code>=</code> is appended then the corresponding max <i>x</i> (<i>east</i>) or <i>y</i> (<i>north</i>) may be slightly adjusted to fit exactly the given increment [by default the increment may be adjusted slightly to fit the given domain]. Finally, instead of giving an increment you may specify the <i>number of nodes</i> desired by appending <code>+</code> to the supplied integer argument; the increment is then recalculated from the number of nodes and the domain. The resulting increment value depends on whether you have selected a gridline-registered or pixel-registered grid; see <i>App-file-formats</i> for details. Note: if <code>-R</code><i>grdfile</i> is used then the grid spacing has already been initialized; use <code>-I</code> to override the values.</p>
<dt><code>-R</code>[<i>unit</i>]<i>xmin</i>/<i>xmax</i>/<i>ymin</i>/<i>ymax</i>[<code>r</code>] <i>(more &#8230;)</i></p>
<dd> Specify the region of interest.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><i>table</i></p>
<dd> One or more ASCII [or binary, see <code>-bi</code>] files holding the spherical harmonic coefficients. We expect the first four columns to hold the degree L, the order M, followed by the cosine and sine coefficients.</p>
<dt><code>-D</code>[<code>g</code>|<code>n</code>]</p>
<dd> Will evaluate a derived field from a geopotential model. Choose between <code>Dg</code> which will compute the gravitational field or <code>Dn</code> to compute the geoid [Add <code>-E</code> for anomalies on the ellipsoid].</p>
<dt><code>-E</code></p>
<dd> Evaluate expansion on the current ellipsoid [Default is sphere].</p>
<dt><code>-F</code>[<code>d</code>]<i>filter</i></p>
<dd> Filter coefficients according to one of two kinds of filter specifications:. Select <code>-Fk</code> if values are given in km [Default is coefficient harmonic degree L]. a) Cosine band-pass: Append four wavelengths <i>lc/lp/hp/hc</i>. Coefficients outside <i>lc/hc</i> are cut; those inside <i>lp/hp</i> are passed, while the rest are tapered. Replace wavelength by &#8211; to skip, e.g., <code>-F</code>-/-/50/75 is a low-pass filter. b) Gaussian band-pass: Append two wavelengths <i>lo/hi</i> where filter amplitudes = 0.5. Replace wavelength by &#8211; to skip, e.g., <code>-F</code>70/- is a high-pass Gaussian filter.</p>
<dt><code>-N</code>[<i>norm</i>]</p>
<dd> Normalization used for coefficients. Choose among <code>m</code>: Mathematical normalization &#8211; inner products summed over surface equal 1 [Default]. <code>g</code> Geodesy normalization &#8211; inner products summed over surface equal 4pi. <code>s</code>: Schmidt normalization &#8211; as used in geomagnetism.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-bi</code>[<i>ncols</i>][<code>t</code>] <i>(more &#8230;)</i></p>
<dd> Select native binary input. [Default is 4 input columns].</p>
<dt><code>-h</code>[<code>i</code>|<code>o</code>][<i>n</i>][<code>+c</code>][<code>+d</code>][<code>+r</code><i>remark</i>][<code>+r</code><i>title</i>] <i>(more &#8230;)</i></p>
<dd> Skip or produce header record(s). Not used with binary data.</p>
<dt><code>-i</code><i>cols</i>[<code>l</code>][<code>s</code><i>scale</i>][<code>o</code><i>offset</i>][,<i>&#8230;</i>] <i>(more &#8230;)</i></p>
<dd> Select input columns (0 is first column).</p>
<dt><code>-r</code> <i>(more &#8230;)</i></p>
<dd> Set pixel node registration [gridline].</p>
<dt><code>-x</code>[[-]<i>n</i>] <i>(more &#8230;)</i></p>
<dd> Limit number of cores used in multi-threaded algorithms (OpenMP required).</p>
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
<h2>GRID VALUES PRECISION</h2>
<p> Regardless of the precision of the input data, GMT programs that create grid files will internally hold the grids in 4-byte floating point arrays. This is done to conserve memory and furthermore most if not all real data can be stored using 4-byte floating point values. Data with higher precision (i.e., double precision values) will lose that precision once GMT operates on the grid or writes out new grids. To limit loss of precision when processing data you should always consider normalizing the data prior to processing.</p>
<h2>GRID FILE FORMATS</h2>
<p> By default GMT writes out grid as single precision floats in a COARDS-complaint netCDF file format. However, GMT is able to produce grid files in many other commonly used grid file formats and also facilitates so called &quot;packing&quot; of grids, writing out floating point data as 1- or 2-byte integers. To specify the precision, scale and offset, the user should add the suffix <code>=</code><i>id</i>[<code>/</code><i>scale</i><code>/</code><i>offset</i>[<code>/</code><i>nan</i>]], where <i>id</i> is a two-letter identifier of the grid type and precision, and <i>scale</i> and <i>offset</i> are optional scale factor and offset to be applied to all grid values, and <i>nan</i> is the value used to indicate missing data. See <code>grdconvert</code> and Section <i>grid-file-format</i> of the GMT Technical Reference and Cookbook for more information. </p>
<p> When writing a netCDF file, the grid is stored by default with the variable name &quot;z&quot;. To specify another variable name <i>varname</i>, append <code>?</code><i>varname</i> to the file name. Note that you may need to escape the special meaning of <code>?</code> in your shell program by putting a backslash in front of it, or by placing the filename and suffix between quotes or double quotes.</p>
<h2>GEOGRAPHICAL AND TIME COORDINATES</h2>
<p> When the output grid type is netCDF, the coordinates will be labeled &quot;longitude&quot;, &quot;latitude&quot;, or &quot;time&quot; based on the attributes of the input data or grid (if any) or on the <code>-f</code> or <code>-R</code> options. For example, both <code>-f0x</code> <code>-f1t</code> and <code>-R</code>90w/90e/0t/3t will result in a longitude/time grid. When the x, y, or z coordinate is time, it will be stored in the grid as relative time since epoch as specified by <i>TIME_UNIT</i> and <i>TIME_EPOCH</i> in the <code>gmt.conf</code> file or on the command line. In addition, the <code>unit</code> attribute of the time variable will indicate both this unit and epoch.</p>
<h2>EXAMPLES</h2>
<p> To create a 1 x 1 degree global grid file from the ASCII coefficients in EGM96_to_360.txt, use </p>
<pre>
gmt sph2grd EGM96_to_360.txt -GEGM96_to_360.nc -Rg -I1 -V
</pre>
<h2>REFERENCE</h2>
<p> Holmes, S. A., and Featherstone, W. E., 2002, A unified approach to the Clenshaw summation and the recursive computation of very high degree and order normalized associated Legendre functions: <i>J. Geodesy, v. 76, p. 279-299</i>.</p>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>grdfft</code>, <code>grdmath</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
