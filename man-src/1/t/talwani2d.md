---
title: "talwani2d(1)"
name: "talwani2d"
section: "1"
letter: "t"
url: "/docs/linux/man/1-talwani2d/"
description: "talwani2d – Compute free-air, geoid or vertical gravity gradients anomalies over 2-D bodies"
---

<h2>NAME</h2>
<p> talwani2d &#8211; Compute free-air, geoid or vertical gravity gradients anomalies over 2-D bodies</p>
<h2>SYNOPSIS</h2>
<p> <code>talwani2d</code> [ <i>modeltable</i> ] [ ] [ <i>rho</i> ] ] [ <code>f</code>|<code>n</code>|<code>v</code> ] [ [<code>h</code>][<code>v</code>] ] [ <i>trackfile</i> ] [ <i>min</i><i>max</i>/<i>inc</i> ] [ <i>level</i>[<i>ymin</i>/<i>ymax</i>] ] [ [<i>level</i>] ] [ <code>-bi</code><i>&lt;binary&gt;</i> ] [ <code>-i</code><i>&lt;flags&gt;</i> ] [ <code>-o</code><i>&lt;flags&gt;</i> ] [ <code>-x</code>[[-]<i>n</i>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>talwani2d</code> will read the multi-segment <i>modeltable</i> from file or standard input. This file contains cross-sections of one or more 2-D bodies, with one polygon per segment. The segment header must contain the parameter <i>rho</i>, which states the the density of this body (individual body densities may be overridden by a fixed constant density contrast given via <code>-D</code>). We can compute anomalies on an equidistant lattice (by specifying a lattice with <code>-T</code>) or provide arbitrary output points specified in a file via <code>-N</code>. Choose between free-air anomalies, vertical gravity gradient anomalies, or geoid anomalies. Options are available to control axes units and direction.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>modeltable</i></p>
<dd> The file describing cross-sectional polygons of one or more bodies. Polygons will be automatically closed if not already closed, and repeated vertices will be eliminated.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-A</code></p>
<dd> The <i>z</i>-axis should be positive upwards [Default is down].</p>
<dt><code>-D</code><i>unit</i></p>
<dd> Sets fixed density contrast that overrides any setting in model file, in kg/m^3.</p>
<dt><code>-F</code><code>f</code>|<code>n</code>|<code>v</code></p>
<dd> Specify desired gravitational field component. Choose between <code>f</code> (free-air anomaly) [Default], <code>n</code> (geoid) or <code>v</code> (vertical gravity gradient).</p>
<dt><code>-M</code>[<code>h</code>][<code>v</code>]</p>
<dd> Sets units used. Append <code>h</code> to indicate horizontal distances are in km [m], and append <code>z</code> to indicate vertical distances are in km [m].</p>
<dt><code>-N</code><i>trackfile</i></p>
<dd> Specifies locations where we wish to compute the predicted value. When this option is used you cannot use <i>-T*</i> to set an equidistant lattice. The output data records are written to stdout.</p>
<dt><code>-T</code><i>min</i><i>max</i>/<i>inc</i></p>
<dd> Specify an equidistant output lattice starting at <i>x = min</i>, with increments <i>inc</i> and ending at <i>x = max</i>.</p>
<dt><code>-Z</code><i>level</i>[<i>ymin</i>/<i>ymax</i>]</p>
<dd> Set observation level as a constant [0]. Optionally, and for gravity anomalies only, append the finite extent limits of a 2.5-D body.</p>
<dt><code>-bi</code>[<i>ncols</i>][<code>t</code>] <i>(more &#8230;)</i></p>
<dd> Select native binary input. [Default is 2 input columns].</p>
<dt><code>-h</code>[<code>i</code>|<code>o</code>][<i>n</i>][<code>+c</code>][<code>+d</code>][<code>+r</code><i>remark</i>][<code>+r</code><i>title</i>] <i>(more &#8230;)</i></p>
<dd> Skip or produce header record(s). Not used with binary data.</p>
<dt><code>-i</code><i>cols</i>[<code>l</code>][<code>s</code><i>scale</i>][<code>o</code><i>offset</i>][,<i>&#8230;</i>] <i>(more &#8230;)</i></p>
<dd> Select input columns (0 is first column).</p>
<dt><code>-o</code><i>cols</i>[,&#8230;] <i>(more &#8230;)</i></p>
<dd> Select output columns (0 is first column).</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-x</code>[[-]<i>n</i>] <i>(more &#8230;)</i></p>
<dd> Limit number of cores used in multi-threaded algorithms (OpenMP required).</p>
<dt><code>-:</code>[<code>i</code>|<code>o</code>] <i>(more &#8230;)</i></p>
<dd> Swap 1st and 2nd column on input and/or output.</p>
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
<h2>UNITS</h2>
<p> For map distance unit, append <i>unit</i> <code>d</code> for arc degree, <code>m</code> for arc minute, and <code>s</code> for arc second, or <code>e</code> for meter [Default], <code>f</code> for foot, <code>k</code> for km, <code>M</code> for statute mile, <code>n</code> for nautical mile, and <code>u</code> for US survey foot. By default we compute such distances using a spherical approximation with great circles. Prepend <code>&#8211;</code> to a distance (or the unit is no distance is given) to perform &quot;Flat Earth&quot; calculations (quicker but less accurate) or prepend <code>+</code> to perform exact geodesic calculations (slower but more accurate).</p>
<h2>EXAMPLES</h2>
<p> To compute the free-air anomalies on a grid over a 2-D body that has been contoured and saved to body.txt, using 1.7 g/cm^3 as the density contrast, try </p>
<pre>
gmt talwani2d -T-200/200/2 body.txt -D1700 -Fg &gt; 2dgrav.txt
</pre>
<p> To obtain the vertical gravity gradient anomaly along the track in crossing.txt for the same model, try </p>
<pre>
gmt talwani2d -Ncrossing.txt body.txt -D1700 -Fv &gt; vgg_crossing.txt
</pre>
<p> The geoid anomaly for the same setup is given by </p>
<pre>
gmt talwani2d -Ncrossing.txt body.txt -D1700 -Fn &gt; n_crossing.txt
</pre>
<h2>NOTES</h2>
<dl>
<dt>1.</p>
<dd> The 2-D geoid anomaly is a logarithmic potential and thus has no natural reference level. We simply remove the most negative (if density contrast is positive) or positive (if density contrast is negative) computed value from all values, rendering the entire anomaly positive (or negative). You can use <code>gmtmath</code> to change the zero level to suit your needs.</dl>
<h2>REFERENCES</h2>
<p> Chapman, M. E. (1979), Techniques for interpretation of geoid anomalies, J. Geophys. Res., 84(B8), 3793-3801. Talwani, M., J. L. Worzel, and M. Landisman (1959), Rapid gravity computations for two-dimensional bodies with application to the Mendocino submarine fracture zone, J. Geophys. Res., 64, 49-59.</p>
<h2>SEE ALSO</h2>
<p> <code>gmt.conf</code>, <code>gmt</code>, <code>grdmath</code>, <code>gmtmath</code>, <code>gravfft</code>, <code>gmtgravmag3d</code>, <code>grdgravmag3d</code>, <code>talwani3d</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
