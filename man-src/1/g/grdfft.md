---
title: "grdfft(1)"
name: "grdfft"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grdfft/"
description: "grdfft – Do mathematical operations on grids in the wavenumber (or frequency) domain"
---

<h2>NAME</h2>
<p> grdfft &#8211; Do mathematical operations on grids in the wavenumber (or frequency) domain</p>
<h2>SYNOPSIS</h2>
<p> <code>grdfft</code> <i>ingrid</i> [ <i>ingrid2</i> ] <i>outfile</i> [ <i>azimuth</i> ] [ <i>zlevel</i> ] [ [<i>scale</i>|<code>g</code>] ] [ [<code>r</code>|<code>x</code>|<code>y</code>][<code>w</code>[<code>k</code>]] ] [ [<code>r</code>|<code>x</code>|<code>y</code>]<i>params</i> ] [ [<i>scale</i>|<code>g</code>] ] [ [<code>f</code>|<code>q</code>|<code>s</code>|<i>nx/ny</i>][<code>+a</code>|<code>d</code>|<code>h</code>|<code>l</code>][<code>+e</code>|<code>n</code>|<code>m</code>][<code>+t</code><i>width</i>][<code>+w</code>[<i>suffix</i>]][<code>+z</code>[<code>p</code>]] ] [ <i>scale</i> ] [ [<i>level</i>] ] [ <code>-fg</code> ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>grdfft</code> will take the 2-D forward Fast Fourier Transform and perform one or more mathematical operations in the frequency domain before transforming back to the space domain. An option is provided to scale the data before writing the new values to an output file. The horizontal dimensions of the grid are assumed to be in meters. Geographical grids may be used by specifying the <code>-fg</code> option that scales degrees to meters. If you have grids with dimensions in km, you could change this to meters using <code>grdedit</code> or scale the output with <code>grdmath</code>.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>ingrid</i></p>
<dd> 2-D binary grid file to be operated on. (See GRID FILE FORMATS below). For cross-spectral operations, also give the second grid file <i>ingrd2</i>.</p>
<dt><code>-G</code><i>outfile</i></p>
<dd> Specify the name of the output grid file or the 1-D spectrum table (see <code>-E</code>). (See GRID FILE FORMATS below).</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-A</code><i>azimuth</i></p>
<dd> Take the directional derivative in the <i>azimuth</i> direction measured in degrees CW from north.</p>
<dt><code>-C</code><i>zlevel</i></p>
<dd> Upward (for <i>zlevel</i> &gt; 0) or downward (for <i>zlevel</i> &lt; 0) continue the field <i>zlevel</i> meters.</p>
<dt><code>-D</code>[<i>scale</i>|<code>g</code>]</p>
<dd> Differentiate the field, i.e., take d(field)/dz. This is equivalent to multiplying by kr in the frequency domain (kr is radial wave number). Append a scale to multiply by (kr * <i>scale</i>) instead. Alternatively, append <code>g</code> to indicate that your data are geoid heights in meters and output should be gravity anomalies in mGal. [Default is no scale].</p>
<dt><code>-E</code>[<code>r</code>|<code>x</code>|<code>y</code>][<code>w</code>[<code>k</code>]]</p>
<dd> Estimate power spectrum in the radial direction [<code>r</code>]. Place <code>x</code> or <code>y</code> immediately after <code>-E</code> to compute the spectrum in the x or y direction instead. No grid file is created. If one grid is given then f (i.e., frequency or wave number), power[f], and 1 standard deviation in power[f] are written to the file set by <code>-G</code> [stdout]. If two grids are given we write f and 8 quantities: Xpower[f], Ypower[f], coherent power[f], noise power[f], phase[f], admittance[f], gain[f], coherency[f]. Each quantity is followed by its own 1-std dev error estimate, hence the output is 17 columns wide. Append <code>w</code> to write wavelength instead of frequency. If your grid is geographic you may further append <code>k</code> to scale wavelengths from meter [Default] to km.</p>
<dt><code>-F</code>[<code>r</code>|<code>x</code>|<code>y</code>]<i>params</i></p>
<dd> Filter the data. Place <code>x</code> or <code>y</code> immediately after <code>-F</code> to filter <i>x</i> or <i>y</i> direction only; default is isotropic [<code>r</code>]. Choose between a cosine-tapered band-pass, a Gaussian band-pass filter, or a Butterworth band-pass filter.</p>
<dt><code>Cosine-taper:</code></p>
<dd> Specify four wavelengths <i>lc</i>/<i>lp</i>/<i>hp</i>/<i>hc</i> in correct units (see <code>-fg</code>) to design a bandpass filter: wavelengths greater than <i>lc</i> or less than <i>hc</i> will be cut, wavelengths greater than <i>lp</i> and less than <i>hp</i> will be passed, and wavelengths in between will be cosine-tapered. E.g., <code>-F</code>1000000/250000/50000/10000 <code>-fg</code> will bandpass, cutting wavelengths &gt; 1000 km and &lt; 10 km, passing wavelengths between 250 km and 50 km. To make a highpass or lowpass filter, give hyphens (-) for <i>hp</i>/<i>hc</i> or <i>lc</i>/<i>lp</i>. E.g., <code>-Fx</code>-/-/50/10 will lowpass <i>x</i>, passing wavelengths &gt; 50 and rejecting wavelengths &lt; 10. <code>-Fy</code>1000/250/-/- will highpass <i>y</i>, passing wavelengths &lt; 250 and rejecting wavelengths &gt; 1000.</p>
<dt><code>Gaussian band-pass:</code></p>
<dd> Append <i>lo</i>/<i>hi</i>, the two wavelengths in correct units (see <code>-fg</code>) to design a bandpass filter. At the given wavelengths the Gaussian filter weights will be 0.5. To make a highpass or lowpass filter, give a hyphen (-) for the <i>hi</i> or <i>lo</i> wavelength, respectively. E.g., <code>-F</code>-/30 will lowpass the data using a Gaussian filter with half-weight at 30, while <code>-F</code>400/- will highpass the data.</p>
<dt><code>Butterworth band-pass:</code></p>
<dd> Append <i>lo</i>/<i>hi</i>/<i>order</i>, the two wavelengths in correct units (see <code>-fg</code>) and the filter order (an integer) to design a bandpass filter. At the given wavelengths the Butterworth filter weights will be 0.5. To make a highpass or lowpass filter, give a hyphen (-) for the <i>hi</i> or <i>lo</i> wavelength, respectively. E.g., <code>-F</code>-/30/2 will lowpass the data using a 2nd-order Butterworth filter, with half-weight at 30, while <code>-F</code>400/-/2 will highpass the data.</p>
<dt><code>-I</code>[<i>scale</i>|<code>g</code>]</p>
<dd> Integrate the field, i.e., compute integral_over_z (field * dz). This is equivalent to divide by kr in the frequency domain (kr is radial wave number). Append a scale to divide by (kr * <i>scale</i>) instead. Alternatively, append <code>g</code> to indicate that your data set is gravity anomalies in mGal and output should be geoid heights in meters. [Default is no scale].</p>
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
<dt><code>-S</code><i>scale</i></p>
<dd> Multiply each element by <i>scale</i> in the space domain (after the frequency domain operations). [Default is 1.0].</p>
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
<p> netCDF COARDS grids will automatically be recognized as geographic. For other grids geographical grids were you want to convert degrees into meters, select <code>-fg</code>. If the data are close to either pole, you should consider projecting the grid file onto a rectangular coordinate system using <code>grdproject</code></p>
<h2>EXAMPLES</h2>
<p> To upward continue the sea-level magnetic anomalies in the file mag_0.nc to a level 800 m above sealevel: </p>
<pre>
gmt grdfft mag_0.nc -C800 -V -Gmag_800.nc
</pre>
<p> To transform geoid heights in m (geoid.nc) on a geographical grid to free-air gravity anomalies in mGal: </p>
<pre>
gmt grdfft geoid.nc -Dg -V -Ggrav.nc
</pre>
<p> To transform gravity anomalies in mGal (faa.nc) to deflections of the vertical (in micro-radians) in the 038 direction, we must first integrate gravity to get geoid, then take the directional derivative, and finally scale radians to micro-radians: </p>
<pre>
gmt grdfft faa.nc -Ig -A38 -S1e6 -V -Gdefl_38.nc
</pre>
<p> Second vertical derivatives of gravity anomalies are related to the curvature of the field. We can compute these as mGal/m^2 by differentiating twice: </p>
<pre>
gmt grdfft gravity.nc -D -D -V -Ggrav_2nd_derivative.nc
</pre>
<p> To compute cross-spectral estimates for co-registered bathymetry and gravity grids, and report result as functions of wavelengths in km, try </p>
<pre>
gmt grdfft bathymetry.nc gravity.grd -Ewk -fg -V &gt; cross_spectra.txt
</pre>
<p> To examine the pre-FFT grid after detrending, point-symmetry reflection, and tapering has been applied, as well as saving the real and imaginary components of the raw spectrum of the data in topo.nc, try </p>
<pre>
gmt grdfft topo.nc -N+w+z -fg -V
</pre>
<p> You can now make plots of the data in topo_taper.nc, topo_real.nc, and topo_imag.nc.</p>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>grdedit</code>, <code>grdfilter</code>, <code>grdmath</code>, <code>grdproject</code>, <code>gravfft</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
