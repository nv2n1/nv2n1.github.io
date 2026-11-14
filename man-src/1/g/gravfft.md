---
title: "gravfft(1)"
name: "gravfft"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gravfft/"
description: "gravfft – Compute gravitational attraction of 3-D surfaces in the wavenumber (or frequency) domain"
---

<h2>NAME</h2>
<p> gravfft &#8211; Compute gravitational attraction of 3-D surfaces in the wavenumber (or frequency) domain</p>
<h2>SYNOPSIS</h2>
<p> <code>gravfft</code> <i>ingrid</i> [ <i>ingrid2</i> ] <i>outfile</i> [ <i>n/wavelength/mean_depth/tbw</i> ] [ <i>density</i>|<i>rhogrid</i> ] [ <i>n_terms</i> ] [ [<code>f</code>[<code>+</code>]|<code>g</code>|<code>v</code>|<code>n</code>|<code>e</code>] ] [ <code>w</code>|<code>b</code>|<code>c</code>|<code>t</code> |<code>k</code> ] [ [<code>f</code>|<code>q</code>|<code>s</code>|<i>nx/ny</i>][<code>+a</code>|<code>d</code>|<code>h</code> |<code>l</code>][<code>+e</code>|<code>n</code>|<code>m</code>][<code>+t</code><i>width</i>][<code>+w</code>[<i>suffix</i>]][<code>+z</code>[<code>p</code>]] [ ] [ <i>te/rl/rm/rw</i>[<code>+m</code>] ] [ [<i>level</i>] ] [ <i>wd</i>] [ <i>zm</i>[<i>zl</i>] ] [ <code>-fg</code> ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>gravfft</code> can be used into three main modes. Mode 1: Simply compute the geopotential due to the surface given in the topo.grd file. Requires a density contrast (<code>-D</code>) and possibly a different observation level (<code>-W</code>). It will take the 2-D forward FFT of the grid and use the full Parker&#8217;s method up to the chosen terms. Mode 2: Compute the geopotential response due to flexure of the topography file. It will take the 2-D forward FFT of the grid and use the full Parker&#8217;s method applied to the chosen isostatic model. The available models are the &quot;loading from top&quot;, or elastic plate model, and the &quot;loading from below&quot; which accounts for the plate&#8217;s response to a sub-surface load (appropriate for hot spot modeling &#8211; if you believe them). In both cases, the model parameters are set with <code>-T</code> and <code>-Z</code> options. Mode 3: compute the admittance or coherence between two grids. The output is the average in the radial direction. Optionally, the model admittance may also be calculated. The horizontal dimensions of the grdfiles are assumed to be in meters. Geographical grids may be used by specifying the <code>-fg</code> option that scales degrees to meters. If you have grids with dimensions in km, you could change this to meters using <code>grdedit</code> or scale the output with <code>grdmath</code>. Given the number of choices this program offers, is difficult to state what are options and what are required arguments. It depends on what you are doing; see the examples for further guidance.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>ingrid</i></p>
<dd> 2-D binary grid file to be operated on. (See GRID FILE FORMATS below). For cross-spectral operations, also give the second grid file <i>ingrd2</i>.</p>
<dt><code>-G</code><i>outfile</i></p>
<dd> Specify the name of the output grid file or the 1-D spectrum table (see <code>-E</code>). (See GRID FILE FORMATS below).</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-C</code><i>n/wavelength/mean_depth/tbw</i></p>
<dd> Compute only the theoretical admittance curves of the selected model and exit. <i>n</i> and <i>wavelength</i> are used to compute (n * wavelength) the total profile length in meters. <i>mean_depth</i> is the mean water depth. Append dataflags (one or two) of <i>tbw</i> in any order. <i>t</i> = use &quot;from top&quot; model, <i>b</i> = use &quot;from below&quot; model. Optionally specify <i>w</i> to write wavelength instead of frequency.</p>
<dt><code>-D</code><i>density</i>|<i>rhogrid</i></p>
<dd> Sets density contrast across surface. Used, for example, to compute the gravity attraction of the water layer that can later be combined with the free-air anomaly to get the Bouguer anomaly. In this case do not use <code>-T</code>. It also implicitly sets <code>-N+h</code>. Alternatively, specify a co-registered grid with density contrasts if a variable density contrast is required.</p>
<dt><code>-E</code><i>n_terms</i></p>
<dd> Number of terms used in Parker expansion (limit is 10, otherwise terms depending on n will blow out the program) [Default = 3]</p>
<dt><code>-F</code>[<code>f</code>[<code>+</code>]|<code>g</code>|<code>v</code>|<code>n</code>|<code>e</code>]</p>
<dd> Specify desired geopotential field: compute geoid rather than gravity <code>f</code> = Free-air anomalies (mGal) [Default]. Append <code>+</code> to add in the slab implied when removing the mean value from the topography. This requires zero topography to mean no mass anomaly. </p>
<p> <code>g</code> = Geoid anomalies (m). </p>
<p> <code>v</code> = Vertical Gravity Gradient (VGG; 1 Eotvos = 0.1 mGal/km). </p>
<p> <code>e</code> = East deflections of the vertical (micro-radian). </p>
<p> <code>n</code> = North deflections of the vertical (micro-radian).</p>
<dt><code>-I</code><code>w</code>|<code>b</code>|<code>c</code>|<code>t</code> |<code>k</code></p>
<dd> Use <i>ingrd2</i> and <i>ingrd1</i> (a grid with topography/bathymetry) to estimate admittance|coherence and write it to stdout (<code>-G</code> ignored if set). This grid should contain gravity or geoid for the same region of <i>ingrd1</i>. Default computes admittance. Output contains 3 or 4 columns. Frequency (wavelength), admittance (coherence) one sigma error bar and, optionally, a theoretical admittance. Append dataflags (one to three) from <code>w</code>|<code>b</code>|<code>c</code>|<code>t</code>. <code>w</code> writes wavelength instead of wavenumber, <code>k</code> selects km for wavelength unit [m], <code>c</code> computes coherence instead of admittance, <code>b</code> writes a fourth column with &quot;loading from below&quot; theoretical admittance, and <code>t</code> writes a fourth column with &quot;elastic plate&quot; theoretical admittance.</p>
<dt><code>-N</code>[<code>f</code>|<code>q</code>|<code>s</code>|<i>nx/ny</i>][<code>+a</code>|[<code>+d</code>|<code>h</code>|<code>l</code>][<code>+e</code>|<code>n</code>|<code>m</code>][<code>+t</code><i>width</i>][<code>+w</code>[<i>suffix</i>]][<code>+z</code>[<code>p</code>]]</p>
<dd> Choose or inquire about suitable grid dimensions for FFT and set optional parameters. Control the FFT dimension: <code>-Nf</code> will force the FFT to use the actual dimensions of the data. </p>
<p> <code>-Nq</code> will inQuire about more suitable dimensions, report those, then continue. </p>
<p> <code>-Ns</code> will present a list of optional dimensions, then exit. </p>
<p> <code>-N</code><i>nx/ny</i> will do FFT on array size <i>nx/ny</i> (must be &gt;= grid file size). Default chooses dimensions &gt;= data which optimize speed and accuracy of FFT. If FFT dimensions &gt; grid file dimensions, data are extended and tapered to zero. </p>
<p> Control detrending of data: Append modifiers for removing a linear trend: <code>+d</code>: Detrend data, i.e. remove best-fitting linear trend [Default]. </p>
<p> <code>+a</code>: Only remove mean value. </p>
<p> <code>+h</code>: Only remove mid value, i.e. 0.5 * (max + min). </p>
<p> <code>+l</code>: Leave data alone. </p>
<p> Control extension and tapering of data: Use modifiers to control how the extension and tapering are to be performed: <code>+e</code> extends the grid by imposing edge-point symmetry [Default], </p>
<p> <code>+m</code> extends the grid by imposing edge mirror symmetry </p>
<p> <code>+n</code> turns off data extension. </p>
<p> Tapering is performed from the data edge to the FFT grid edge [100%]. Change this percentage via <code>+t</code><i>width</i>. When <code>+n</code> is in effect, the tapering is applied instead to the data margins as no extension is available [0%]. </p>
<p> Control writing of temporary results: For detailed investigation you can write the intermediate grid being passed to the forward FFT; this is likely to have been detrended, extended by point-symmetry along all edges, and tapered. Append <code>+w</code>[<i>suffix</i>] from which output file name(s) will be created (i.e., <i>ingrid_prefix.ext</i>) [tapered], where <i>ext</i> is your file extension. Finally, you may save the complex grid produced by the forward FFT by appending <code>+z</code>. By default we write the real and imaginary components to <i>ingrid</i>_real.<i>ext</i> and <i>ingrid</i>_imag.<i>ext</i>. Append <code>p</code> to save instead the polar form of magnitude and phase to files <i>ingrid</i>_mag.<i>ext</i> and <i>ingrid</i>_phase.<i>ext</i>.</p>
<dt><code>-Q</code></p>
<dd> Writes out a grid with the flexural topography (with z positive up) whose average was set by <code>-Z</code><i>zm</i> and model parameters by <code>-T</code> (and output by <code>-G</code>). That is the &quot;gravimetric Moho&quot;. <code>-Q</code> implicitly sets <code>-N+h</code></p>
<dt><code>-S</code></p>
<dd> Computes predicted gravity or geoid grid due to a subplate load produced by the current bathymetry and the theoretical model. The necessary parameters are set within <code>-T</code> and <code>-Z</code> options. The number of powers in Parker expansion is restricted to 1. See an example further down.</p>
<dt><code>-T</code><i>te/rl/rm/rw</i>[<code>+m</code>]</p>
<dd> Compute the isostatic compensation from the topography load (input grid file) on an elastic plate of thickness <i>te</i>. Also append densities for load, mantle, and water in SI units. Give average mantle depth via <code>-Z</code>. If the elastic thickness is &gt; 1e10 it will be interpreted as the flexural rigidity (by default it is computed from <i>te</i> and Young modulus). Optionally, append <i>+m</i> to write a grid with the Moho&#8217;s geopotential effect (see <code>-F</code>) from model selected by <code>-T</code>. If <i>te</i> = 0 then the Airy response is returned. <code>-T+m</code> implicitly sets <code>-N+h</code></p>
<dt><code>-W</code><i>wd</i></p>
<dd> Set water depth (or observation height) relative to topography [0]. Append <code>k</code> to indicate km.</p>
<dt><code>-Z</code><i>zm</i>[<i>zl</i>]</p>
<dd> Moho [and swell] average compensation depths. For the &quot;load from top&quot; model you only have to provide <i>zm</i>, but for the &quot;loading from below&quot; don&#8217;t forget <i>zl</i>.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-fg</code></p>
<dd> Geographic grids (dimensions of longitude, latitude) will be converted to meters via a &quot;Flat Earth&quot; approximation using the current ellipsoid parameters.</p>
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
<h2>GRID DISTANCE UNITS</h2>
<p> If the grid does not have meter as the horizontal unit, append <code>+u</code><i>unit</i> to the input file name to convert from the specified unit to meter. If your grid is geographic, convert distances to meters by supplying <code>-fg</code> instead.</p>
<h2>CONSIDERATIONS</h2>
<p> netCDF COARDS grids will automatically be recognized as geographic. For other grids geographical grids were you want to convert degrees into meters, select <code>-fg</code>. If the data are close to either pole, you should consider projecting the grid file onto a rectangular coordinate system using <code>grdproject</code>.</p>
<h2>PLATE FLEXURE</h2>
<p> The FFT solution to elastic plate flexure requires the infill density to equal the load density. This is typically only true directly beneath the load; beyond the load the infill tends to be lower-density sediments or even water (or air). Wessel [2001] proposed an approximation that allows for the specification of an infill density different from the load density while still allowing for an FFT solution. Basically, the plate flexure is solved for using the infill density as the effective load density but the amplitudes are adjusted by a factor <i>A</i> = sqrt ((rm &#8211; ri)/(rm &#8211; rl)), which is the theoretical difference in amplitude due to a point load using the two different load densities. The approximation is very good but breaks down for large loads on weak plates, a fairy uncommon situation.</p>
<h2>EXAMPLES</h2>
<p> To compute the effect of the water layer above the bat.grd bathymetry using 2700 and 1035 for the densities of crust and water and writing the result on water_g.grd (computing up to the fourth power of bathymetry in Parker expansion): </p>
<pre>
gmt gravfft bat.grd -D1665 -Gwater_g.grd -E4
</pre>
<p> Now subtract it to your free-air anomaly faa.grd and you will get the Bouguer anomaly. You may wonder why we are subtracting and not adding. After all the Bouguer anomaly pretends to correct the mass deficiency presented by the water layer, so we should add because water is less dense than the rocks below. The answer relies on the way gravity effects are computed by the Parker&#8217;s method and practical aspects of using the FFT. </p>
<pre>
gmt grdmath faa.grd water_g.grd SUB = bouguer.grd
</pre>
<p> Want an MBA anomaly? Well compute the crust mantle contribution and add it to the sea-bottom anomaly. Assuming a 6 km thick crust of density 2700 and a mantle with 3300 density we could repeat the command used to compute the water layer anomaly, using 600 (3300 &#8211; 2700) as the density contrast. But we now have a problem because we need to know the mean Moho depth. That is when the scale/offset that can be appended to the grid&#8217;s name comes in hand. Notice that we didn&#8217;t need to do that before because mean water depth was computed directly from data (notice also the negative sign of the offset due to the fact that <i>z</i> is positive up): </p>
<pre>
gmt gravfft bat.grd=nf/1/-6000 -D600 -Gmoho_g.grd
</pre>
<p> Now, subtract it to the sea-bottom anomaly to obtain the MBA anomaly. That is: </p>
<pre>
gmt grdmath water_g.grd moho_g.grd SUB = mba.grd
</pre>
<p> To compute the Moho gravity effect of an elastic plate bat.grd with Te = 7 km, density of 2700, over a mantle of density 3300, at an average depth of 9 km </p>
<pre>
gmt gravfft bat.grd -Gelastic.grd -T7000/2700/3300/1035+m -Z9000
</pre>
<p> If you add now the sea-bottom and Moho&#8217;s effects, you will get the full gravity response of your isostatic model. We will use here only the first term in Parker expansion. </p>
<pre>
gmt gravfft bat.grd -D1665 -Gwater_g.grd -E1
gmt gravfft bat.grd -Gelastic.grd -T7000/2700/3300/1035+m -Z9000 -E1
gmt grdmath water_g.grd elastic.grd ADD = model.grd
</pre>
<p> The same result can be obtained directly by the next command. However, PAY ATTENTION to the following. I don&#8217;t yet know if it&#8217;s because of a bug or due to some limitation, but the fact is that the following and the previous commands only give the same result if <code>-E</code>1 is used. For higher powers of bathymetry in Parker expansion, only the above example seams to give the correct result. </p>
<pre>
gmt gravfft bat.grd -Gmodel.grd -T7000/2700/3300/1035 -Z9000 -E1
</pre>
<p> And what would be the geoid anomaly produced by a load at 50 km depth, below the a region whose bathymetry is given by bat.grd, a Moho at 9 km depth and the same densities as before? </p>
<pre>
gmt gravfft topo.grd -Gswell_geoid.grd -T7000/2700/3300/1035 -Fg -Z9000/50000 -S -E1
</pre>
<p> To compute the admittance between the topo.grd bathymetry and faa.grd free-air anomaly grid using the elastic plate model of a crust of 6 km mean thickness with 10 km effective elastic thickness in a region of 3 km mean water depth: </p>
<pre>
gmt gravfft topo.grd faa.grd -It -T10000/2700/3300/1035 -Z9000
</pre>
<p> To compute the admittance between the topo.grd bathymetry and geoid.grd geoid grid with the &quot;loading from below&quot; (LFB) model with the same as above and sub-surface load at 40 km, but assuming now the grids are in geographic and we want wavelengths instead of frequency: </p>
<pre>
gmt gravfft topo.grd geoid.grd -Ibw -T10000/2700/3300/1035 -Z9000/40000 -fg
</pre>
<p> To compute the gravity theoretical admittance of a LFB along a 2000 km long profile using the same parameters as above </p>
<pre>
gmt gravfft -C400/5000/3000/b -T10000/2700/3300/1035 -Z9000/40000
</pre>
<h2>REFERENCES</h2>
<p> Luis, J.F. and M.C. Neves. 2006, The isostatic compensation of the Azores Plateau: a 3D admittance and coherence analysis. J. Geothermal Volc. Res. Volume 156, Issues 1-2, Pages 10-22, <i><a rel="nofollow" href="http://dx.doi.org/10.1016/j.jvolgeores.2006.03.010">http://dx.doi.org/10.1016/j.jvolgeores.2006.03.010</a></i> Parker, R. L., 1972, The rapid calculation of potential anomalies, Geophys. J., 31, 447-455. Wessel. P., 2001, Global distribution of seamounts inferred from gridded Geosat/ERS-1 altimetry, J. Geophys. Res., 106(B9), 19,431-19,441, <i><a rel="nofollow" href="http://dx.doi.org/10.1029/2000JB000083">http://dx.doi.org/10.1029/2000JB000083</a></i></p>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>grdfft</code>, <code>grdmath</code>, <code>grdproject</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
