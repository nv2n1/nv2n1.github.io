---
title: "greenspline(1)"
name: "greenspline"
section: "1"
letter: "g"
url: "/docs/linux/man/1-greenspline/"
description: "greenspline – Interpolate using Green’s functions for splines in 1-3 dimensions"
---

<h2>NAME</h2>
<p> greenspline &#8211; Interpolate using Green&#8217;s functions for splines in 1-3 dimensions</p>
<h2>SYNOPSIS</h2>
<p> <code>greenspline</code> [ <i>table</i> ] [ [<code>1</code>|<code>2</code>|<code>3</code>|<code>4</code>|<code>5</code>,]<i>gradfile</i> ] [ [<code>n</code>|<code>v</code>]<i>cut</i>[/<i>file</i>] ] [ <i>mode</i> ] [ <i>grdfile</i> ] [ <i>xinc</i>[/<i>yinc</i>[/<i>zinc</i>]] ] [ ] [ <i>nodefile</i> ] [ <i>az</i>|<i>x/y/z</i> ] [ <i>west</i>/<i>east</i>/<i>south</i>/<i>north</i>[/<i>zmin</i>/<i>zmax</i>][<code>r</code>] ] [ <code>c|t|l|r|p|q</code>[<i>pars</i>] ] [ <i>maskgrid</i> ] [ [<i>level</i>] ] [ ] [ <code>-b</code><i>&lt;binary&gt;</i> ] [ <code>-d</code><i>&lt;nodata&gt;</i> ] [ <code>-f</code><i>&lt;flags&gt;</i> ] [ <code>-h</code><i>&lt;headers&gt;</i> ] [ <code>-o</code><i>&lt;flags&gt;</i> ] [ <code>-x</code>[[-]<i>n</i>] ] [ <code>-:</code>[<code>i</code>|<code>o</code>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>greenspline</code> uses the Green&#8217;s function G(<code>x</code>; <code>x&#8217;</code>) for the chosen spline and geometry to interpolate data at regular [or arbitrary] output locations. Mathematically, the solution is composed as <i>w</i>(<code>x</code>) = sum {<i>c</i>(<i>i</i>) G(<code>x&#8217;</code>; <code>x</code>(<i>i</i>))}, for <i>i</i> = 1, <i>n</i>, the number of data points {<code>x</code>(<i>i</i>), <i>w</i>(<i>i</i>)}. Once the <i>n</i> coefficients <i>c</i>(<i>i</i>) have been found the sum can be evaluated at any output point <code>x</code>. Choose between minimum curvature, regularized, or continuous curvature splines in tension for either 1-D, 2-D, or 3-D Cartesian coordinates or spherical surface coordinates. After first removing a linear or planar trend (Cartesian geometries) or mean value (spherical surface) and normalizing these residuals, the least-squares matrix solution for the spline coefficients <i>c</i>(<i>i</i>) is found by solving the <i>n</i> by <i>n</i> linear system <i>w</i>(<i>j</i>) = sum-over-<i>i</i> {<i>c</i>(<i>i</i>) G(<code>x</code>(<i>j</i>); <code>x</code>(<i>i</i>))}, for <i>j</i> = 1, <i>n</i>; this solution yields an exact interpolation of the supplied data points. Alternatively, you may choose to perform a singular value decomposition (SVD) and eliminate the contribution from the smallest eigenvalues; this approach yields an approximate solution. Trends and scales are restored when evaluating the output.</p>
<h2>REQUIRED ARGUMENTS</h2>
<p> None.</p>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><i>table</i></p>
<dd> The name of one or more ASCII [or binary, see <code>-bi</code>] files holding the <code>x</code>, <i>w</i> data points. If no file is given then we read standard input instead.</p>
<dt><code>-A</code>[<code>1</code>|<code>2</code>|<code>3</code>|<code>4</code>|<code>5</code>,]<i>gradfile</i></p>
<dd> The solution will partly be constrained by surface gradients <code>v</code> = <i>v</i>*<code>n</code>, where <i>v</i> is the gradient magnitude and <code>n</code> its unit vector direction. The gradient direction may be specified either by Cartesian components (either unit vector <code>n</code> and magnitude <i>v</i> separately or gradient components <code>v</code> directly) or angles w.r.t. the coordinate axes. Specify one of five input formats: <code>0</code>: For 1-D data there is no direction, just gradient magnitude (slope) so the input format is <i>x</i>, <i>gradient</i>. Options 1-2 are for 2-D data sets: <code>1</code>: records contain <i>x</i>, <i>y</i>, <i>azimuth</i>, <i>gradient</i> (<i>azimuth</i> in degrees is measured clockwise from the vertical (north) [Default]). <code>2</code>: records contain <i>x</i>, <i>y</i>, <i>gradient</i>, <i>azimuth</i> (<i>azimuth</i> in degrees is measured clockwise from the vertical (north)). Options 3-5 are for either 2-D or 3-D data: <code>3</code>: records contain <code>x</code>, <i>direction(s)</i>, <i>v</i> (<i>direction(s)</i> in degrees are measured counter-clockwise from the horizontal (and for 3-D the vertical axis). <code>4</code>: records contain <code>x</code>, <code>v</code>. <code>5</code>: records contain <code>x</code>, <code>n</code>, <i>v</i>. Append name of ASCII file with the surface gradients (following a comma if a format is specified).</p>
<dt><code>-C</code>[<code>n</code>|<code>v</code>]<i>cut</i>[/<i>file</i>]</p>
<dd> Find an approximate surface fit: Solve the linear system for the spline coefficients by SVD and eliminate the contribution from all eigenvalues whose ratio to the largest eigenvalue is less than <i>cut</i> [Default uses Gauss-Jordan elimination to solve the linear system and fit the data exactly]. Optionally, append /<i>file</i> to save the eigenvalue ratios to the specified file for further analysis. Finally, if a negative <i>cut</i> is given then /<i>file</i> is required and execution will stop after saving the eigenvalues, i.e., no surface output is produced. Specify <code>-Cv</code> to use the largest eigenvalues needed to explain <i>cut</i> % of the data variance. Alternatively, use <code>-Cn</code> to select the <i>cut</i> largest eigenvalues. If a <i>file</i> is given with <code>-Cv</code> then we save the eigenvalues instead of the ratios.</p>
<dt><code>-D</code><i>mode</i></p>
<dd> Sets the distance flag that determines how we calculate distances between data points. Select <i>mode</i> 0 for Cartesian 1-D spline interpolation: <code>-D</code>0 means (<i>x</i>) in user units, Cartesian distances, Select <i>mode</i> 1-3 for Cartesian 2-D surface spline interpolation: <code>-D</code>1 means (<i>x</i>,<i>y</i>) in user units, Cartesian distances, <code>-D</code>2 for (<i>x</i>,<i>y</i>) in degrees, Flat Earth distances, and <code>-D</code>3 for (<i>x</i>,<i>y</i>) in degrees, Spherical distances in km. Then, if <i>PROJ_ELLIPSOID</i> is spherical, we compute great circle arcs, otherwise geodesics. Option <i>mode</i> = 4 applies to spherical surface spline interpolation only: <code>-D</code>4 for (<i>x</i>,<i>y</i>) in degrees, use cosine of great circle (or geodesic) arcs. Select <i>mode</i> 5 for Cartesian 3-D surface spline interpolation: <code>-D</code>5 means (<i>x</i>,<i>y</i>,<i>z</i>) in user units, Cartesian distances.</p>
<dt><code>-G</code><i>grdfile</i></p>
<dd> Name of resulting output file. (1) If options <code>-R</code>, <code>-I</code>, and possibly <code>-r</code> are set we produce an equidistant output table. This will be written to stdout unless <code>-G</code> is specified. Note: for 2-D grids the <code>-G</code> option is required. (2) If option <code>-T</code> is selected then <code>-G</code> is required and the output file is a 2-D binary grid file. Applies to 2-D interpolation only. (3) If <code>-N</code> is selected then the output is an ASCII (or binary; see <code>-bo</code>) table; if <code>-G</code> is not given then this table is written to standard output. Ignored if <code>-C</code> or <code>-C</code>0 is given.</p>
<dt><code>-I</code><i>xinc</i>[/<i>yinc</i>[/<i>zinc</i>]]</p>
<dd> Specify equidistant sampling intervals, on for each dimension, separated by slashes.</p>
<dt><code>-L</code></p>
<dd> Do <i>not</i> remove a linear (1-D) or planer (2-D) trend when <code>-D</code> selects mode 0-3 [For those Cartesian cases a least-squares line or plane is modeled and removed, then restored after fitting a spline to the residuals]. However, in mixed cases with both data values and gradients, or for spherical surface data, only the mean data value is removed (and later and restored).</p>
<dt><code>-N</code><i>nodefile</i></p>
<dd> ASCII file with coordinates of desired output locations <code>x</code> in the first column(s). The resulting <i>w</i> values are appended to each record and written to the file given in <code>-G</code> [or stdout if not specified]; see <code>-bo</code> for binary output instead. This option eliminates the need to specify options <code>-R</code>, <code>-I</code>, and <code>-r</code>.</p>
<dt><code>-Q</code><i>az</i>|<i>x/y/z</i></p>
<dd> Rather than evaluate the surface, take the directional derivative in the <i>az</i> azimuth and return the magnitude of this derivative instead. For 3-D interpolation, specify the three components of the desired vector direction (the vector will be normalized before use).</p>
<dt><code>-R</code><i>xmin</i>/<i>xmax</i>[/<i>ymin</i>/<i>ymax</i>[/<i>zmin</i><i>zmax</i>]]</p>
<dd> Specify the domain for an equidistant lattice where output predictions are required. Requires <code>-I</code> and optionally <code>-r</code>. </p>
<p> <i>1-D:</i> Give <i>xmin/xmax</i>, the minimum and maximum <i>x</i> coordinates. </p>
<p> <i>2-D:</i> Give <i>xmin/xmax/ymin/ymax</i>, the minimum and maximum <i>x</i> and <i>y</i> coordinates. These may be Cartesian or geographical. If geographical, then <i>west</i>, <i>east</i>, <i>south</i>, and <i>north</i> specify the Region of interest, and you may specify them in decimal degrees or in [+-]dd:mm[:ss.xxx][W|E|S|N] format. The two shorthands <code>-Rg</code> and <code>-Rd</code> stand for global domain (0/360 and -180/+180 in longitude respectively, with -90/+90 in latitude). </p>
<p> <i>3-D:</i> Give <i>xmin/xmax/ymin/ymax/zmin/zmax</i>, the minimum and maximum <i>x</i>, <i>y</i> and <i>z</i> coordinates. See the 2-D section if your horizontal coordinates are geographical; note the shorthands <code>-Rg</code> and <code>-Rd</code> cannot be used if a 3-D domain is specified.</p>
<dt><code>-S</code><code>c|t|l|r|p|q</code>[<i>pars</i>]</p>
<dd> Select one of six different splines. The first two are used for 1-D, 2-D, or 3-D Cartesian splines (see <code>-D</code> for discussion). Note that all tension values are expected to be normalized tension in the range 0 &lt; <i>t</i> &lt; 1: (<code>c</code>) Minimum curvature spline [<i>Sandwell</i>, 1987], (<code>t</code>) Continuous curvature spline in tension [<i>Wessel and Bercovici</i>, 1998]; append <i>tension</i>[/<i>scale</i>] with <i>tension</i> in the 0-1 range and optionally supply a length scale [Default is the average grid spacing]. The next is a 1-D or 2-D spline: (<code>l</code>) Linear (1-D) or Bilinear (2-D) spline; these produce output that do not exceed the range of the given data. The next is a 2-D or 3-D spline: (<code>r</code>) Regularized spline in tension [<i>Mitasova and Mitas</i>, 1993]; again, append <i>tension</i> and optional <i>scale</i>. The last two are spherical surface splines and both imply <code>-D</code>4: (<code>p</code>) Minimum curvature spline [<i>Parker</i>, 1994], (<code>q</code>) Continuous curvature spline in tension [<i>Wessel and Becker</i>, 2008]; append <i>tension</i>. The G(<code>x&#8217;</code>; <code>x&#8217;</code>) for the last method is slower to compute (a series solution) so we pre-calculate values and use cubic spline interpolation lookup instead. Optionally append <code>+n</code><i>N</i> (an odd integer) to change how many points to use in the spline setup [10001]. The finite Legendre sum has a truncation error [1e-6]; you can lower that by appending <code>+e</code><i>limit</i> at the expense of longer run-time.</p>
<dt><code>-T</code><i>maskgrid</i></p>
<dd> For 2-D interpolation only. Only evaluate the solution at the nodes in the <i>maskgrid</i> that are not equal to NaN. This option eliminates the need to specify options <code>-R</code>, <code>-I</code>, and <code>-r</code>.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-W</code></p>
<dd> Expect data weights in the final input column, typically given as weight = 1 / sigma, the data uncertainty. This results in a weighted least squares fit. Note that this only has an effect if <code>-CC</code> is used.</p>
<dt><code>-bi</code>[<i>ncols</i>][<code>t</code>] <i>(more &#8230;)</i></p>
<dd> Select native binary input. [Default is 2-4 input columns (<code>x</code>,<i>w</i>); the number depends on the chosen dimension].</p>
<dt><code>-bo</code>[<i>ncols</i>][<i>type</i>] <i>(more &#8230;)</i></p>
<dd> Select native binary output.</p>
<dt><code>-d</code>[<code>i</code>|<code>o</code>]<i>nodata</i> <i>(more &#8230;)</i></p>
<dd> Replace input columns that equal <i>nodata</i> with NaN and do the reverse on output.</p>
<dt><code>-f</code>[<code>i</code>|<code>o</code>]<i>colinfo</i> <i>(more &#8230;)</i></p>
<dd> Specify data types of input and/or output columns.</p>
<dt><code>-h</code>[<code>i</code>|<code>o</code>][<i>n</i>][<code>+c</code>][<code>+d</code>][<code>+r</code><i>remark</i>][<code>+r</code><i>title</i>] <i>(more &#8230;)</i></p>
<dd> Skip or produce header record(s).</p>
<dt><code>-i</code><i>cols</i>[<code>l</code>][<code>s</code><i>scale</i>][<code>o</code><i>offset</i>][,<i>&#8230;</i>] <i>(more &#8230;)</i></p>
<dd> Select input columns (0 is first column).</p>
<dt><code>-o</code><i>cols</i>[,&#8230;] <i>(more &#8230;)</i></p>
<dd> Select output columns (0 is first column).</p>
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
<h2>1-D EXAMPLES</h2>
<p> To resample the <i>x</i>,<i>y</i> Gaussian random data created by <code>gmtmath</code> and stored in 1D.txt, requesting output every 0.1 step from 0 to 10, and using a minimum cubic spline, try </p>
<pre>
gmt math -T0/10/1 0 1 NRAND = 1D.txt
gmt psxy -R0/10/-5/5 -JX6i/3i -B2f1/1 -Sc0.1 -Gblack 1D.txt -K &gt; 1D.ps
gmt greenspline 1D.txt -R0/10 -I0.1 -Sc -V | psxy -R -J -O -Wthin &gt;&gt; 1D.ps
</pre>
<p> To apply a spline in tension instead, using a tension of 0.7, try </p>
<pre>
gmt psxy -R0/10/-5/5 -JX6i/3i -B2f1/1 -Sc0.1 -Gblack 1D.txt -K &gt; 1Dt.ps
gmt greenspline 1D.txt -R0/10 -I0.1 -St0.7 -V | psxy -R -J -O -Wthin &gt;&gt; 1Dt.ps
</pre>
<h2>2-D EXAMPLES</h2>
<p> To make a uniform grid using the minimum curvature spline for the same Cartesian data set from Davis (1986) that is used in the GMT Technical Reference and Cookbook example 16, try </p>
<pre>
gmt greenspline table_5.11 -R0/6.5/-0.2/6.5 -I0.1 -Sc -V -D1 -GS1987.nc
gmt psxy -R0/6.5/-0.2/6.5 -JX6i -B2f1 -Sc0.1 -Gblack table_5.11 -K &gt; 2D.ps
gmt grdcontour -JX6i -B2f1 -O -C25 -A50 S1987.nc &gt;&gt; 2D.ps
</pre>
<p> To use Cartesian splines in tension but only evaluate the solution where the input mask grid is not NaN, try </p>
<pre>
gmt greenspline table_5.11 -Tmask.nc -St0.5 -V -D1 -GWB1998.nc
</pre>
<p> To use Cartesian generalized splines in tension and return the magnitude of the surface slope in the NW direction, try </p>
<pre>
gmt greenspline table_5.11 -R0/6.5/-0.2/6.5 -I0.1 -Sr0.95 -V -D1 -Q-45 -Gslopes.nc
</pre>
<p> Finally, to use Cartesian minimum curvature splines in recovering a surface where the input data is a single surface value (pt.d) and the remaining constraints specify only the surface slope and direction (slopes.d), use </p>
<pre>
gmt greenspline pt.d -R-3.2/3.2/-3.2/3.2 -I0.1 -Sc -V -D1 -A1,slopes.d -Gslopes.nc
</pre>
<h2>3-D EXAMPLES</h2>
<p> To create a uniform 3-D Cartesian grid table based on the data in table_5.23 in Davis (1986) that contains <i>x</i>,<i>y</i>,<i>z</i> locations and a measure of uranium oxide concentrations (in percent), try </p>
<pre>
gmt greenspline table_5.23 -R5/40/-5/10/5/16 -I0.25 -Sr0.85 -V -D5 -G3D_UO2.txt
</pre>
<h2>2-D SPHERICAL SURFACE EXAMPLES</h2>
<p> To recreate Parker&#8217;s [1994] example on a global 1&#215;1 degree grid, assuming the data are in file mag_obs_1990.d, try </p>
<pre>
greenspline -V -Rg -Sp -D3 -I1 -GP1994.nc mag_obs_1990.d
</pre>
<p> To do the same problem but applying tension of 0.85, use </p>
<pre>
greenspline -V -Rg -Sq0.85 -D3 -I1 -GWB2008.nc mag_obs_1990.d
</pre>
<h2>CONSIDERATIONS</h2>
<dl>
<dt>1.</p>
<dd> For the Cartesian cases we use the free-space Green functions, hence no boundary conditions are applied at the edges of the specified domain. For most applications this is fine as the region typically is arbitrarily set to reflect the extent of your data. However, if your application requires particular boundary conditions then you may consider using <code>surface</code> instead.</p>
<dt>2.</p>
<dd> In all cases, the solution is obtained by inverting a <i>n</i> x <i>n</i> double precision matrix for the Green function coefficients, where <i>n</i> is the number of data constraints. Hence, your computer&#8217;s memory may place restrictions on how large data sets you can process with <i>greenspline &lt;greenspline.html&gt;</i>. Pre-processing your data with <i>blockmean &lt;blockmean.html&gt;</i>, <i>blockmedian &lt;blockmedian.html&gt;</i>, or <i>blockmode &lt;blockmode.html&gt;</i> is recommended to avoid aliasing and may also control the size of <i>n</i>. For information, if <i>n</i> = 1024 then only 8 Mb memory is needed, but for <i>n</i> = 10240 we need 800 Mb. Note that <i>greenspline &lt;greenspline.html&gt;</i> is fully 64-bit compliant if compiled as such. For spherical data you may consider decimating using <i>gmtspatial &lt;gmtspatial.html&gt;</i> nearest neighbor reduction.</p>
<dt>3.</p>
<dd> The inversion for coefficients can become numerically unstable when data neighbors are very close compared to the overall span of the data. You can remedy this by pre-processing the data, e.g., by averaging closely spaced neighbors. Alternatively, you can improve stability by using the SVD solution and discard information associated with the smallest eigenvalues (see <code>-C</code>).</p>
<dt>4.</p>
<dd> The series solution implemented for <code>-Sq</code> was developed by Robert L. Parker, Scripps Institution of Oceanography, which we gratefully acknowledge.</p>
<dt>5.</p>
<dd> If you need to fit a certain 1-D spline through your data points you may wish to consider <i>sample1d &lt;sample1d.html&gt;</i> instead. It will offer traditional splines with standard boundary conditions (such as the natural cubic spline, which sets the curvatures at the ends to zero). In contrast, greenspline&#8217;s 1-D spline, as is explained in note 1, does <i>not</i> specify boundary conditions at the end of the data domain.</dl>
<h2>TENSION</h2>
<p> Tension is generally used to suppress spurious oscillations caused by the minimum curvature requirement, in particular when rapid gradient changes are present in the data. The proper amount of tension can only be determined by experimentation. Generally, very smooth data (such as potential fields) do not require much, if any tension, while rougher data (such as topography) will typically interpolate better with moderate tension. Make sure you try a range of values before choosing your final result. Note: the regularized spline in tension is only stable for a finite range of <i>scale</i> values; you must experiment to find the valid range and a useful setting. For more information on tension see the references below.</p>
<h2>REFERENCES</h2>
<p> Davis, J. C., 1986, <i>Statistics and Data Analysis in Geology</i>, 2nd Edition, 646 pp., Wiley, New York, </p>
<p> Mitasova, H., and L. Mitas, 1993, Interpolation by regularized spline with tension: I. Theory and implementation, <i>Math. Geol.</i>, <code>25</code>, 641-655. </p>
<p> Parker, R. L., 1994, <i>Geophysical Inverse Theory</i>, 386 pp., Princeton Univ. Press, Princeton, N.J. </p>
<p> Sandwell, D. T., 1987, Biharmonic spline interpolation of Geos-3 and Seasat altimeter data, <i>Geophys. Res. Lett.</i>, <code>14</code>, 139-142. </p>
<p> Wessel, P., and D. Bercovici, 1998, Interpolation with splines in tension: a Green&#8217;s function approach, <i>Math. Geol.</i>, <code>30</code>, 77-93. </p>
<p> Wessel, P., and J. M. Becker, 2008, Interpolation using a generalized Green&#8217;s function for a spherical surface spline in tension, <i>Geophys. J. Int</i>, <code>174</code>, 21-28. </p>
<p> Wessel, P., 2009, A general-purpose Green&#8217;s function interpolator, <i>Computers &amp; Geosciences</i>, <code>35</code>, 1247-1254, doi:10.1016/j.cageo.2008.08.012.</p>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>gmtmath</code>, <code>nearneighbor</code>, <code>psxy</code>, <code>sphtriangulate</code>, <code>surface</code>, <code>triangulate</code>, <code>xyz2grd</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
