---
title: "trend1d(1)"
name: "trend1d"
section: "1"
letter: "t"
url: "/docs/linux/man/1-trend1d/"
description: "trend1d – Fit a [weighted] [robust] polynomial [and/or Fourier] model for y = f(x) to xy[w] data"
---

<h2>NAME</h2>
<p> trend1d &#8211; Fit a [weighted] [robust] polynomial [and/or Fourier] model for y = f(x) to xy[w] data</p>
<h2>SYNOPSIS</h2>
<p> <code>trend1d</code> [ <i>table</i> ] <code>xymrw|p</code> [<code>p</code>|<code>P</code>|<code>f</code>|<code>F</code>|<code>c</code>|<code>C</code>|<code>s</code>|<code>S</code>|<code>x</code>]<i>n</i>[,&#8230;][<code>+l</code><i>length</i>][<code>+o</code><i>origin</i>][<code>+r</code>] [ <i>xy[w]file</i> ] [ <i>condition_number</i> ] [ [<i>confidence_level</i>] ] [ [<i>level</i>] ] [ ] [ <code>-b</code><i>&lt;binary&gt;</i> ] [ <code>-d</code><i>&lt;nodata&gt;</i> ] [ <code>-f</code><i>&lt;flags&gt;</i> ] [ <code>-h</code><i>&lt;headers&gt;</i> ] [ <code>-i</code><i>&lt;flags&gt;</i> ] [ <code>-:</code>[<code>i</code>|<code>o</code>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>trend1d</code> reads x,y [and w] values from the first two [three] columns on standard input [or <i>file</i>] and fits a regression model y = f(x) + e by [weighted] least squares. The functional form of f(x) may be chosen as polynomial or Fourier or a mix of the two, and the fit may be made robust by iterative reweighting of the data. The user may also search for the number of terms in f(x) which significantly reduce the variance in y.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><code>-F</code><code>xymrw|p</code></p>
<dd> Specify up to five letters from the set {<code>x y m r w</code>} in any order to create columns of ASCII [or binary] output. <code>x</code> = x, <code>y</code> = y, <code>m</code> = model f(x), <code>r</code> = residual y &#8211; <code>m</code>, <code>w</code> = weight used in fitting. Alternatively choose <code>-F</code><code>p</code> (i.e., no other of the 5 letters) to output only the model coefficients.</p>
<dt><code>-N</code>[<code>p</code>|<code>P</code>|<code>f</code>|<code>F</code>|<code>c</code>|<code>C</code>|<code>s</code>|<code>S</code>|<code>x</code>]<i>n</i>[,&#8230;][<code>+l</code><i>length</i>][<code>+o</code><i>origin</i>][<code>+r</code>]</p>
<dd> Specify the components of the (possibly mixed) model. Append one or more comma-separated model components. Each component is of the form <code>T</code><i>n</i>, where <code>T</code> indicates the basis function and <i>n</i> indicates the polynomial degree or how many terms in the Fourier series we want to include. Choose <code>T</code> from <code>p</code> (polynomial with intercept and powers of x up to degree <i>terms</i>), <code>P</code> (just the single term <i>x^n</i>), <code>f</code> (Fourier series with <i>n</i> terms), <code>c</code> (Cosine series with <i>n</i> terms), <code>s</code> (sine series with <i>n</i> terms), <code>F</code> (single Fourier component of order <i>n</i>), <code>C</code> (single cosine component of order <i>n</i>), and <code>S</code> (single sine component of order <i>n</i>). By default the <i>x</i>-origin and fundamental period is set to the mid-point and data range, respectively. Change this using the <code>+o</code><i>origin</i> and <code>+l</code><i>length</i> modifiers. We normalize <i>x</i> before evaluating the basis functions. Basically, the trigonometric bases all use the normalized x&#8217; = (2*pi*(x-<i>origin</i>)/<i>length</i>) while the polynomials use x&#8217; = 2*(x-x_mid)/(xmax &#8211; xmin) for stability. Finally, append <code>+r</code> for a robust solution [Default gives a least squares fit]. Use <code>-V</code> to see a plain-text representation of the y(x) model specified in <code>-N</code>.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><i>table</i></p>
<dd> One or more ASCII [or binary, see <code>-bi</code>] files containing x,y [w] values in the first 2 [3] columns. If no files are specified, <code>trend1d</code> will read from standard input.</p>
<dt><code>-C</code><i>condition_number</i></p>
<dd> Set the maximum allowed condition number for the matrix solution. <code>trend1d</code> fits a damped least squares model, retaining only that part of the eigenvalue spectrum such that the ratio of the largest eigenvalue to the smallest eigenvalue is <i>condition_#</i>. [Default: <i>condition_#</i> = 1.0e06. ].</p>
<dt><code>-I</code>[<i>confidence_level</i>]</p>
<dd> Iteratively increase the number of model parameters, starting at one, until <i>n_model</i> is reached or the reduction in variance of the model is not significant at the <i>confidence_level</i> level. You may set <code>-I</code> only, without an attached number; in this case the fit will be iterative with a default confidence level of 0.51. Or choose your own level between 0 and 1. See remarks section. Note that the model terms are added in the order they were given in <code>-N</code> so you should place the most important terms first.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-W</code></p>
<dd> Weights are supplied in input column 3. Do a weighted least squares fit [or start with these weights when doing the iterative robust fit]. [Default reads only the first 2 columns.]</p>
<dt><code>-bi</code>[<i>ncols</i>][<code>t</code>] <i>(more &#8230;)</i></p>
<dd> Select native binary input. [Default is 2 (or 3 if <code>-W</code> is set) columns].</p>
<dt><code>-bo</code>[<i>ncols</i>][<i>type</i>] <i>(more &#8230;)</i></p>
<dd> Select native binary output. [Default is 1-5 columns as given by <code>-F</code>].</p>
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
<h2>ASCII FORMAT PRECISION</h2>
<p> The ASCII output formats of numerical data are controlled by parameters in your <code>gmt.conf</code> file. Longitude and latitude are formatted according to <i>FORMAT_GEO_OUT</i>, whereas other values are formatted according to <i>FORMAT_FLOAT_OUT</i>. Be aware that the format in effect can lead to loss of precision in the output, which can lead to various problems downstream. If you find the output is not written with enough precision, consider switching to binary output (<code>-bo</code> if available) or specify more decimals using the <i>FORMAT_FLOAT_OUT</i> setting.</p>
<h2>REMARKS</h2>
<p> If a polynomial model is included, then the domain of x will be shifted and scaled to [-1, 1] and the basis functions will be Chebyshev polynomials provided the polygon is of full order (otherwise we stay with powers of x). The Chebyshev polynomials have a numerical advantage in the form of the matrix which must be inverted and allow more accurate solutions. The Chebyshev polynomial of degree n has n+1 extrema in [-1, 1], at all of which its value is either -1 or +1. Therefore the magnitude of the polynomial model coefficients can be directly compared. NOTE: The stable model coefficients are Chebyshev coefficients. The corresponding polynomial coefficients in a + bx + cxx + &#8230; are also given in Verbose mode but users must realize that they are NOT stable beyond degree 7 or 8. See Numerical Recipes for more discussion. For evaluating Chebyshev polynomials, see <code>gmtmath</code>. </p>
<p> The <code>-N</code>&#8230;<code>+r</code> (robust) and <code>-I</code> (iterative) options evaluate the significance of the improvement in model misfit Chi-Squared by an F test. The default confidence limit is set at 0.51; it can be changed with the <code>-I</code> option. The user may be surprised to find that in most cases the reduction in variance achieved by increasing the number of terms in a model is not significant at a very high degree of confidence. For example, with 120 degrees of freedom, Chi-Squared must decrease by 26% or more to be significant at the 95% confidence level. If you want to keep iterating as long as Chi-Squared is decreasing, set <i>confidence_level</i> to zero. </p>
<p> A low confidence limit (such as the default value of 0.51) is needed to make the robust method work. This method iteratively reweights the data to reduce the influence of outliers. The weight is based on the Median Absolute Deviation and a formula from Huber [1964], and is 95% efficient when the model residuals have an outlier-free normal distribution. This means that the influence of outliers is reduced only slightly at each iteration; consequently the reduction in Chi-Squared is not very significant. If the procedure needs a few iterations to successfully attenuate their effect, the significance level of the F test must be kept low.</p>
<h2>EXAMPLES</h2>
<p> To remove a linear trend from data.xy by ordinary least squares, use: </p>
<pre>
gmt trend1d data.xy -Fxr -Np1 &gt; detrended_data.xy
</pre>
<p> To make the above linear trend robust with respect to outliers, use: </p>
<pre>
gmt trend1d data.xy -Fxr -Np1+r &gt; detrended_data.xy
</pre>
<p> To fit the model y(x) = a + bx^2 + c * cos(2*pi*3*(x/l) + d * sin(2*pi*3*(x/l), with l the fundamental period (here l = 15), try: </p>
<pre>
gmt trend1d data.xy -Fxm -NP0,P2,F3+l15 &gt; model.xy
</pre>
<p> To find out how many terms (up to 20, say in a robust Fourier interpolant are significant in fitting data.xy, use: </p>
<pre>
gmt trend1d data.xy -Nf20+r -I -V
</pre>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>gmtmath</code>, <code>gmtregress</code>, <code>grdtrend</code>, <code>trend2d</code></p>
<h2>REFERENCES</h2>
<p> Huber, P. J., 1964, Robust estimation of a location parameter, <i>Ann. Math. Stat.</i>, <code>35</code>, 73-101. </p>
<p> Menke, W., 1989, Geophysical Data Analysis: Discrete Inverse Theory, Revised Edition, Academic Press, San Diego.</p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
