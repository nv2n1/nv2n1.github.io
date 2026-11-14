---
title: "grdflexure(1)"
name: "grdflexure"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grdflexure/"
description: "grdflexure – Compute flexural deformation of 3-D surfaces for various rheologies"
---

<h2>NAME</h2>
<p> grdflexure &#8211; Compute flexural deformation of 3-D surfaces for various rheologies</p>
<h2>SYNOPSIS</h2>
<p> <code>grdflexure</code> <i>topogrd</i> <i>rm</i>/<i>rl</i>[/<i>ri</i>]/<i>rw</i> <i>Te</i>[<code>u</code>] <i>outgrid</i> [ <i>Nx</i>/<i>Ny</i>/<i>Nxy</i> ] [ <code>p</code><i>poisson</i> ] [ <code>y</code><i>Young</i> ] [ <i>nu_a</i>[/<i>h_a</i>/<i>nu_m</i>] ] [ <i>list</i> ] [ [<code>f</code>|<code>q</code>|<code>s</code>|<i>nx</i>/<i>ny</i>][<code>+a</code>|<code>d</code>|<code>h</code>|<code>l</code>][<code>+e</code>|<code>n</code>|<code>m</code>][<code>+t</code><i>width</i>][<code>+w</code>[<i>suffix</i>]][<code>+z</code>[<code>p</code>]] [ <i>beta</i> ] [ <code>-T</code><i>t0</i>[<code>u</code>][/<i>t1</i>[<code>u</code>]/<i>dt</i>[<code>u</code>]|<i>n</i>][<code>+l</code>] ] [ [<i>level</i>] ] [ <i>wd</i>] [ <i>zm</i>] [ <code>-fg</code> ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>grdflexure</code> computes the flexural response to loads using a range of user-selectable rheologies. User may select from elastic, viscoelastic, or firmoviscous (with one or two viscous layers). Temporal evolution can also be modeled by providing incremental load grids and specifying a range of model output times.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>topogrd</i></p>
<dd> 2-D binary grid file with the topography of the load (in meters); See GRID FILE FORMATS below. If <code>-T</code> is used, <i>topogrd</i> may be a filename template with a floating point format (C syntax) and a different load file name will be set and loaded for each time step. The load times thus coincide with the times given via <code>-T</code> (but not all times need to have a corresponding file). Alternatively, give <i>topogrd</i> as =*flist*, where <i>flist</i> is an ASCII table with one <i>topogrd</i> filename and load time per record. These load times can be different from the evaluation times given via <code>-T</code>. For load time format, see <code>-T</code>.</p>
<dt><code>-D</code><i>rm</i>/<i>rl</i>[/<i>ri</i>]/<i>rw</i></p>
<dd> Sets density for mantle, load, infill (optional, otherwise it is assumed to equal the load density), and water or air. If <i>ri</i> differs from <i>rl</i> then an approximate solution will be found. If <i>ri</i> is not given then it defaults to <i>rl</i>.</p>
<dt><code>-E</code><i>Te</i></p>
<dd> Sets the elastic plate thickness (in meter); append <code>k</code> for km. If the elastic thickness exceeds 1e10 it will be interpreted as a flexural rigidity D (by default D is computed from <i>Te</i>, Young&#8217;s modulus, and Poisson&#8217;s ratio; see <code>-C</code> to change these values).</p>
<dt><code>-G</code><i>outfile</i></p>
<dd> If <code>-T</code> is set then <i>grdfile</i> must be a filename template that contains a floating point format (C syntax). If the filename template also contains either %s (for unit name) or %c (for unit letter) then we use the corresponding time (in units specified in <code>-T</code>) to generate the individual file names, otherwise we use time in years with no unit.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-A</code><i>Nx</i>/<i>Ny</i>/<i>Nxy</i></p>
<dd> Specify in-plane compressional or extensional forces in the x- and y-directions, as well as any shear force [no in-plane forces]. Compression is indicated by negative values, while extensional forces are specified using positive values.</p>
<dt><code>-Cp</code><i>poisson</i></p>
<dd> Change the current value of Poisson&#8217;s ratio [0.25].</p>
<dt><code>-Cy</code><i>Young</i></p>
<dd> Change the current value of Young&#8217;s modulus [7.0e10 N/m^2].</p>
<dt><code>-F</code><i>nu_a</i>[/<i>h_a</i>/<i>nu_m</i>]</p>
<dd> Specify a firmoviscous model in conjunction with an elastic plate thickness specified via <code>-E</code>. Just give one viscosity (<i>nu_a</i>) for an elastic plate over a viscous half-space, or also append the thickness of the asthenosphere (<i>h_a</i>) and the lower mantle viscosity (<i>nu_m</i>), with the first viscosity now being that of the asthenosphere. Give viscosities in Pa*s. If used, give the thickness of the asthenosphere in meter; append <code>k</code> for km.</p>
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
<dt><code>-L</code><i>list</i></p>
<dd> Write the names and evaluation times of all grids that were created to the text file <i>list</i>. Requires <code>-T</code>.</p>
<dt><code>-M</code><i>tm</i></p>
<dd> Specify a viscoelastic model in conjunction with an elastic plate thickness specified via <code>-E</code>. Append the Maxwell time <i>tm</i> for the viscoelastic model (in ).</p>
<dt><code>-S</code><i>beta</i></p>
<dd> Specify a starved moat fraction in the 0-1 range, where 1 means the moat is fully filled with material of density <i>ri</i> while 0 means it is only filled with material of density <i>rw</i> (i.e., just water) [1].</p>
<dt><code>-T</code><i>t0</i>[<code>u</code>][/<i>t1</i>[<code>u</code>]/<i>dt</i>[<code>u</code>]|<i>n</i>][<code>+l</code>]</p>
<dd> Specify <i>t0</i>, <i>t1</i>, and time increment (<i>dt</i>) for sequence of calculations [Default is one step, with no time dependency]. For a single specific time, just give start time <i>t0</i>. The unit is years; append <code>k</code> for kyr and <code>M</code> for Myr. For a logarithmic time scale, append <code>+l</code> and specify <i>n</i> steps instead of <i>dt</i>. Alternatively, give a file with the desired times in the first column (these times may have individual units appended, otherwise we assume year). We then write a separate model grid file for each given time step.</p>
<dt><code>-W</code><i>wd</i></p>
<dd> Set reference depth to the undeformed flexed surface in m [0]. Append <code>k</code> to indicate km.</p>
<dt><code>-Z</code><i>zm</i></p>
<dd> Specify reference depth to flexed surface (e.g., Moho) in m; append <code>k</code> for km. Must be positive. [0].</p>
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
<h2>PLATE FLEXURE NOTES</h2>
<p> The FFT solution to plate flexure requires the infill density to equal the load density. This is typically only true directly beneath the load; beyond the load the infill tends to be lower-density sediments or even water (or air). Wessel [2001] proposed an approximation that allows for the specification of an infill density different from the load density while still allowing for an FFT solution. Basically, the plate flexure is solved for using the infill density as the effective load density but the amplitudes are adjusted by the factor <i>A</i> = sqrt ((rm &#8211; ri)/(rm &#8211; rl)), which is the theoretical difference in amplitude due to a point load using the two different load densities. The approximation is very good but breaks down for large loads on weak plates, a fairy uncommon situation.</p>
<h2>EXAMPLES</h2>
<p> To compute elastic plate flexure from the load <i>topo.nc</i>, for a 10 km thick plate with typical densities, try </p>
<pre>
gmt grdflexure topo.nc -Gflex.nc -E10k -D2700/3300/1035
</pre>
<p> To compute the firmoviscous response to a series of incremental loads given by file name and load time in the table l.lis at the single time 1 Ma using the specified rheological values, try </p>
<pre>
gmt grdflexure -T1M =l.lis -D3300/2800/2800/1000 -E5k -Gflx/smt_fv_%03.1f_%s.nc -F2e20 -Nf+a
</pre>
<h2>REFERENCES</h2>
<p> Cathles, L. M., 1975, <i>The viscosity of the earth&#8217;s mantle</i>, Princeton University Press. </p>
<p> Wessel. P., 2001, Global distribution of seamounts inferred from gridded Geosat/ERS-1 altimetry, J. Geophys. Res., 106(B9), 19,431-19,441, <i><a rel="nofollow" href="http://dx.doi.org/10.1029/2000JB000083">http://dx.doi.org/10.1029/2000JB000083</a></i></p>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>grdfft</code>, <code>gravfft</code> <code>grdmath</code>, <code>grdproject</code>, <code>grdseamount</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
