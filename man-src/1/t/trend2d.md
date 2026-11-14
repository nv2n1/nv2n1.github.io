---
title: "trend2d(1)"
name: "trend2d"
section: "1"
letter: "t"
url: "/docs/linux/man/1-trend2d/"
description: "trend2d – Fit a [weighted] [robust] polynomial model for z = f(x,y) to xyz[w] data"
---

<h2>NAME</h2>
<p> trend2d &#8211; Fit a [weighted] [robust] polynomial model for z = f(x,y) to xyz[w] data</p>
<h2>SYNOPSIS</h2>
<p> <code>trend2d</code> [ <i>table</i> ] <code>xyzmrw</code> <i>n_model</i>[<code>r</code>] [ <i>xyz[w]file</i> ] [ <i>condition_number</i> ] [ [<i>confidence_level</i>] ] [ [<i>level</i>] ] [ ] [ [ <code>-b</code><i>&lt;binary&gt;</i> ] [ <code>-d</code><i>&lt;nodata&gt;</i> ] [ <code>-f</code><i>&lt;flags&gt;</i> ] [ <code>-h</code><i>&lt;headers&gt;</i> ] [ <code>-i</code><i>&lt;flags&gt;</i> ] [ <code>-:</code>[<code>i</code>|<code>o</code>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>trend2d</code> reads x,y,z [and w] values from the first three [four] columns on standard input [or <i>xyz[w]file</i>] and fits a regression model z = f(x,y) + e by [weighted] least squares. The fit may be made robust by iterative reweighting of the data. The user may also search for the number of terms in f(x,y) which significantly reduce the variance in z. n_model may be in [1,10] to fit a model of the following form (similar to grdtrend): m1 + m2*x + m3*y + m4*x*y + m5*x*x + m6*y*y + m7*x*x*x + m8*x*x*y + m9*x*y*y + m10*y*y*y. </p>
<p> The user must specify <code>-N</code><i>n_model</i>, the number of model parameters to use; thus, <code>-N</code><i>4</i> fits a bilinear trend, <code>-N</code><i>6</i> a quadratic surface, and so on. Optionally, append <code>r</code> to perform a robust fit. In this case, the program will iteratively reweight the data based on a robust scale estimate, in order to converge to a solution insensitive to outliers. This may be handy when separating a &quot;regional&quot; field from a &quot;residual&quot; which should have non-zero mean, such as a local mountain on a regional surface.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><code>-F</code><code>xyzmrw</code></p>
<dd> Specify up to six letters from the set {<code>x y z m r w</code>} in any order to create columns of ASCII [or binary] output. <code>x</code> = x, <code>y</code> = y, <code>z</code> = z, <code>m</code> = model f(x,y), <code>r</code> = residual z &#8211; <code>m</code>, <code>w</code> = weight used in fitting.</p>
<dt><code>-N</code><i>n_model</i>[<code>r</code>]</p>
<dd> Specify the number of terms in the model, <i>n_model</i>, and append <code>r</code> to do a robust fit. E.g., a robust bilinear model is <code>-N</code><i>4</i><code>r</code>.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><i>table</i></p>
<dd> One or more ASCII [or binary, see <code>-bi</code>] files containing x,y,z [w] values in the first 3 [4] columns. If no files are specified, <code>trend2d</code> will read from standard input.</p>
<dt><code>-C</code><i>condition_number</i></p>
<dd> Set the maximum allowed condition number for the matrix solution. <code>trend2d</code> fits a damped least squares model, retaining only that part of the eigenvalue spectrum such that the ratio of the largest eigenvalue to the smallest eigenvalue is <i>condition_#</i>. [Default: <i>condition_#</i> = 1.0e06. ].</p>
<dt><code>-I</code>[<i>confidence_level</i>]</p>
<dd> Iteratively increase the number of model parameters, starting at one, until <i>n_model</i> is reached or the reduction in variance of the model is not significant at the <i>confidence_level</i> level. You may set <code>-I</code> only, without an attached number; in this case the fit will be iterative with a default confidence level of 0.51. Or choose your own level between 0 and 1. See remarks section.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-W</code></p>
<dd> Weights are supplied in input column 4. Do a weighted least squares fit [or start with these weights when doing the iterative robust fit]. [Default reads only the first 3 columns.]</p>
<dt><code>-bi</code>[<i>ncols</i>][<code>t</code>] <i>(more &#8230;)</i></p>
<dd> Select native binary input. [Default is 3 (or 4 if <code>-W</code> is set) input columns].</p>
<dt><code>-bo</code>[<i>ncols</i>][<i>type</i>] <i>(more &#8230;)</i></p>
<dd> Select native binary output. [Default is 1-6 columns as set by <code>-F</code>].</p>
<dt><code>-d</code>[<code>i</code>|<code>o</code>]<i>nodata</i> <i>(more &#8230;)</i></p>
<dd> Replace input columns that equal <i>nodata</i> with NaN and do the reverse on output.</p>
<dt><code>-f</code>[<code>i</code>|<code>o</code>]<i>colinfo</i> <i>(more &#8230;)</i></p>
<dd> Specify data types of input and/or output columns.</p>
<dt><code>-h</code>[<code>i</code>|<code>o</code>][<i>n</i>][<code>+c</code>][<code>+d</code>][<code>+r</code><i>remark</i>][<code>+r</code><i>title</i>] <i>(more &#8230;)</i></p>
<dd> Skip or produce header record(s).</p>
<dt><code>-i</code><i>cols</i>[<code>l</code>][<code>s</code><i>scale</i>][<code>o</code><i>offset</i>][,<i>&#8230;</i>] <i>(more &#8230;)</i></p>
<dd> Select input columns (0 is first column).</p>
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
<h2>REMARKS</h2>
<p> The domain of x and y will be shifted and scaled to [-1, 1] and the basis functions are built from Chebyshev polynomials. These have a numerical advantage in the form of the matrix which must be inverted and allow more accurate solutions. In many applications of <code>trend2d</code> the user has data located approximately along a line in the x,y plane which makes an angle with the x axis (such as data collected along a road or ship track). In this case the accuracy could be improved by a rotation of the x,y axes. <code>trend2d</code> does not search for such a rotation; instead, it may find that the matrix problem has deficient rank. However, the solution is computed using the generalized inverse and should still work out OK. The user should check the results graphically if <code>trend2d</code> shows deficient rank. NOTE: The model parameters listed with <code>-V</code> are Chebyshev coefficients; they are not numerically equivalent to the m#s in the equation described above. The description above is to allow the user to match <code>-N</code> with the order of the polynomial surface. For evaluating Chebyshev polynomials, see <code>grdmath</code>. </p>
<p> The <code>-N</code><i>n_model</i><code>r</code> (robust) and <code>-I</code> (iterative) options evaluate the significance of the improvement in model misfit Chi-Squared by an F test. The default confidence limit is set at 0.51; it can be changed with the <code>-I</code> option. The user may be surprised to find that in most cases the reduction in variance achieved by increasing the number of terms in a model is not significant at a very high degree of confidence. For example, with 120 degrees of freedom, Chi-Squared must decrease by 26% or more to be significant at the 95% confidence level. If you want to keep iterating as long as Chi-Squared is decreasing, set <i>confidence_level</i> to zero. </p>
<p> A low confidence limit (such as the default value of 0.51) is needed to make the robust method work. This method iteratively reweights the data to reduce the influence of outliers. The weight is based on the Median Absolute Deviation and a formula from Huber [1964], and is 95% efficient when the model residuals have an outlier-free normal distribution. This means that the influence of outliers is reduced only slightly at each iteration; consequently the reduction in Chi-Squared is not very significant. If the procedure needs a few iterations to successfully attenuate their effect, the significance level of the F test must be kept low.</p>
<h2>ASCII FORMAT PRECISION</h2>
<p> The ASCII output formats of numerical data are controlled by parameters in your <code>gmt.conf</code> file. Longitude and latitude are formatted according to <i>FORMAT_GEO_OUT</i>, whereas other values are formatted according to <i>FORMAT_FLOAT_OUT</i>. Be aware that the format in effect can lead to loss of precision in the output, which can lead to various problems downstream. If you find the output is not written with enough precision, consider switching to binary output (<code>-bo</code> if available) or specify more decimals using the <i>FORMAT_FLOAT_OUT</i> setting.</p>
<h2>EXAMPLES</h2>
<p> To remove a planar trend from data.xyz by ordinary least squares, use: </p>
<pre>
gmt trend2d data.xyz -Fxyr -N2 &gt; detrended_data.xyz
</pre>
<p> To make the above planar trend robust with respect to outliers, use: </p>
<pre>
gmt trend2d data.xzy -Fxyr -N2r &gt; detrended_data.xyz
</pre>
<p> To find out how many terms (up to 10 in a robust interpolant are significant in fitting data.xyz, use: </p>
<pre>
gmt trend2d data.xyz -N10r -I -V
</pre>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>grdmath</code>, <code>grdtrend</code>, <code>trend1d</code></p>
<h2>REFERENCES</h2>
<p> Huber, P. J., 1964, Robust estimation of a location parameter, <i>Ann. Math. Stat.</i>, <code>35</code>, 73-101. </p>
<p> Menke, W., 1989, Geophysical Data Analysis: Discrete Inverse Theory, Revised Edition, Academic Press, San Diego.</p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
