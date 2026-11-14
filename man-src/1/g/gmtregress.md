---
title: "gmtregress(1)"
name: "gmtregress"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gmtregress/"
description: "gmtregress – Linear regression of 1-D data sets"
---

<h2>NAME</h2>
<p> gmtregress &#8211; Linear regression of 1-D data sets</p>
<h2>SYNOPSIS</h2>
<p> <code>gmtregress</code> [ <i>table</i> ] [ <i>min</i>/<i>max</i>/<i>inc</i> ] [ <i>level</i> ] [ <code>x</code>|<code>y</code>|<code>o</code>|<code>r</code> ] [ <i>flags</i> ] [ <code>1</code>|<code>2</code>|<code>r</code>|<code>w</code> ] [ [<code>r</code>] ] [ <i>min</i>/<i>max</i>/<i>inc</i> | <i>n</i> ] [ [<code>w</code>][<code>x</code>][<code>y</code>][<code>r</code>] ] [ [<i>level</i>] ] [ <code>-a</code><i>&lt;flags&gt;</i> ] [ <code>-b</code><i>&lt;binary&gt;</i> ] [ <code>-g</code><i>&lt;gaps&gt;</i> ] [ <code>-h</code><i>&lt;headers&gt;</i> ] [ <code>-i</code><i>&lt;flags&gt;</i> ] [ <code>-o</code><i>&lt;flags&gt;</i> ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>gmtregress</code> reads one or more data tables [or <i>stdin</i>] and determines the best linear regression model <i>y</i> = <i>a</i> + <i>b</i>* <i>x</i> for each segment using the chosen parameters. The user may specify which data and model components should be reported. By default, the model will be evaluated at the input points, but alternatively you can specify an equidistant range over which to evaluate the model, or turn off evaluation completely. Instead of determining the best fit we can perform a scan of all possible regression lines (for a range of slope angles) and examine how the chosen misfit measure varies with slope. This is particularly useful when analyzing data with many outliers. Note: If you actually need to work with log10 of <i>x</i> or <i>y</i> you can accomplish that transformation during read by using the <code>-i</code> option.</p>
<h2>REQUIRED ARGUMENTS</h2>
<p> None</p>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><i>table</i></p>
<dd> One or more ASCII (or binary, see <code>-bi</code>[<i>ncols</i>][<i>type</i>]) data table file(s) holding a number of data columns. If no tables are given then we read from standard input. The first two columns are expected to contain the required <i>x</i> and <i>y</i> data. Depending on your <code>-W</code> and <code>-E</code> settings we may expect an additional 1-3 columns with error estimates of one of both of the data coordinates, and even their correlation.</p>
<dt><code>-A</code><i>min</i>/<i>max</i>/<i>inc</i></p>
<dd> Instead of determining a best-fit regression we explore the full range of regressions. Examine all possible regression lines with slope angles between <i>min</i> and <i>max</i>, using steps of <i>inc</i> degrees [-90/+90/1]. For each slope the optimum intercept is determined based on your regression type (<code>-E</code>) and misfit norm (<code>-N</code>) settings. For each segment we report the four columns <i>angle</i>, <i>E</i>, <i>slope</i>, <i>intercept</i>, for the range of specified angles. The best model parameters within this range are written into the segment header and reported in verbose mode (<code>-V</code>).</p>
<dt><code>-C</code><i>level</i></p>
<dd> Set the confidence level (in %) to use for the optional calculation of confidence bands on the regression [95]. This is only used if <code>-F</code> includes the output column <code>c</code>.</p>
<dt><code>-Ex</code>|<code>y</code>|<code>o</code>|<code>r</code></p>
<dd> Type of linear regression, i.e., select the type of misfit we should calculate. Choose from <code>x</code> (regress <i>x</i> on <i>y</i>; i.e., the misfit is measured horizontally from data point to regression line), <code>y</code> (regress <i>y</i> on <i>x</i>; i.e., the misfit is measured vertically [Default]), <code>o</code> (orthogonal regression; i.e., the misfit is measured from data point orthogonally to nearest point on the line), or <code>r</code> (Reduced Major Axis regression; i.e., the misfit is the product of both vertical and horizontal misfits) [<code>y</code>].</p>
<dt><code>-F</code><i>flags</i></p>
<dd> Append a combination of the columns you wish returned; the output order will match the order specified. Choose from <code>x</code> (observed <i>x</i>), <code>y</code> (observed <i>y</i>), <code>m</code> (model prediction), <code>r</code> (residual = data minus model), <code>c</code> (symmetrical confidence interval on the regression; see <code>-C</code> for specifying the level), <code>z</code> (standardized residuals or so-called <i>z-scores</i>) and <code>w</code> (outlier weights 0 or 1; for <code>-Nw</code> these are the Reweighted Least Squares weights) [<code>xymrczw</code>]. As an alternative to evaluating the model, just give <code>-Fp</code> and we instead write a single record with the model parameters <i>npoints xmean ymean angle misfit slope intercept sigma_slope sigma_intercept</i>.</p>
<dt><code>-N1</code>|<code>2</code>|<code>r</code>|<code>w</code></p>
<dd> Selects the norm to use for the misfit calculation. Choose among <code>1</code> (L-1 measure; the mean of the absolute residuals), <code>2</code> (Least-squares; the mean of the squared residuals), <code>r</code> (LMS; The least median of the squared residuals), or <code>w</code> (RLS; Reweighted Least Squares: the mean of the squared residuals after outliers identified via LMS have been removed) [Default is <code>2</code>]. Traditional regression uses L-2 while L-1 and in particular LMS are more robust in how they handle outliers. As alluded to, RLS implies an initial LMS regression which is then used to identify outliers in the data, assign these a zero weight, and then redo the regression using a L-2 norm.</p>
<dt><code>-S</code>[<code>r</code>]</p>
<dd> Restricts which records will be output. By default all data records will be output in the format specified by <code>-F</code>. Use <code>-S</code> to exclude data points identified as outliers by the regression. Alternatively, use <code>-Sr</code> to reverse this and only output the outlier records.</p>
<dt><code>-T</code><i>min</i>/<i>max</i>/<i>inc</i> | <code>-T</code><i>n</i></p>
<dd> Evaluate the best-fit regression model at the equidistant points implied by the arguments. If <code>-T</code><i>n</i> is given instead we will reset <i>min</i> and <i>max</i> to the extreme <i>x</i>-values for each segment and determine <i>inc</i> so that there are exactly <i>n</i> output values for each segment. To skip the model evaluation entirely, simply provide <code>-T</code>0.</p>
<dt><code>-W</code>[<code>w</code>][<code>x</code>][<code>y</code>][<code>r</code>]</p>
<dd> Specifies weighted regression and which weights will be provided. Append <code>x</code> if giving 1-sigma uncertainties in the <i>x</i>-observations, <code>y</code> if giving 1-sigma uncertainties in <i>y</i>, and <code>r</code> if giving correlations between <i>x</i> and <i>y</i> observations, in the order these columns appear in the input (after the two required and leading <i>x</i>, <i>y</i> columns). Giving both <code>x</code> and <code>y</code> (and optionally <code>r</code>) implies an orthogonal regression, otherwise giving <code>x</code> requires <code>-Ex</code> and <code>y</code> requires <code>-Ey</code>. We convert uncertainties in <i>x</i> and <i>y</i> to regression weights via the relationship weight = 1/sigma. Use <code>-Ww</code> if the we should interpret the input columns to have precomputed weights instead. Note: residuals with respect to the regression line will be scaled by the given weights. Most norms will then square this weighted residual (<code>-N1</code> is the only exception).</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-a</code><i>col</i>=<i>name</i>[<i>&#8230;</i>] <i>(more &#8230;)</i></p>
<dd> Set aspatial column associations <i>col</i>=<i>name</i>.</p>
<dt><code>-bi</code>[<i>ncols</i>][<code>t</code>] <i>(more &#8230;)</i></p>
<dd> Select native binary input.</p>
<dt><code>-bo</code>[<i>ncols</i>][<i>type</i>] <i>(more &#8230;)</i></p>
<dd> Select native binary output. [Default is same as input].</p>
<dt><code>-g</code>[<code>a</code>]<code>x</code>|<code>y</code>|<code>d</code>|<code>X</code>|<code>Y</code>|<code>D</code>|[<i>col</i>]<code>z</code>[+|-]<i>gap</i>[<code>u</code>] <i>(more &#8230;)</i></p>
<dd> Determine data gaps and line breaks.</p>
<dt><code>-h</code>[<code>i</code>|<code>o</code>][<i>n</i>][<code>+c</code>][<code>+d</code>][<code>+r</code><i>remark</i>][<code>+r</code><i>title</i>] <i>(more &#8230;)</i></p>
<dd> Skip or produce header record(s).</p>
<dt><code>-i</code><i>cols</i>[<code>l</code>][<code>s</code><i>scale</i>][<code>o</code><i>offset</i>][,<i>&#8230;</i>] <i>(more &#8230;)</i></p>
<dd> Select input columns (0 is first column).</p>
<dt><code>-o</code><i>cols</i>[,&#8230;] <i>(more &#8230;)</i></p>
<dd> Select output columns (0 is first column).</p>
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
<h2>EXAMPLES</h2>
<p> To do a standard least-squares regression on the <i>x-y</i> data in points.txt and return x, y, and model prediction with 99% confidence intervals, try </p>
<pre>
gmt regress points.txt -Fxymc -C99 &gt; points_regressed.txt
</pre>
<p> To just get the slope for the above regression, try </p>
<pre>
slope=`gmt regress points.txt -Fp -o5`
</pre>
<p> To do a reweighted least-squares regression on the data rough.txt and return x, y, model prediction and the RLS weights, try </p>
<pre>
gmt regress rough.txt -Fxymw &gt; points_regressed.txt
</pre>
<p> To do an orthogonal least-squares regression on the data crazy.txt but first take the logarithm of both x and y, then return x, y, model prediction and the normalized residuals (z-scores), try </p>
<pre>
gmt regress crazy.txt -Eo -Fxymz -i0-1l &gt; points_regressed.txt
</pre>
<p> To examine how the orthogonal LMS misfits vary with angle between 0 and 90 in steps of 0.2 degrees for the same file, try </p>
<pre>
gmt regress points.txt -A0/90/0.2 -Eo -Nr &gt; points_analysis.txt
</pre>
<h2>REFERENCES</h2>
<p> Draper, N. R., and H. Smith, 1998, <i>Applied regression analysis</i>, 3rd ed., 736 pp., John Wiley and Sons, New York. </p>
<p> Rousseeuw, P. J., and A. M. Leroy, 1987, <i>Robust regression and outlier detection</i>, 329 pp., John Wiley and Sons, New York. </p>
<p> York, D., N. M. Evensen, M. L. Martinez, and J. De Basebe Delgado, 2004, Unified equations for the slope, intercept, and standard errors of the best straight line, <i>Am. J. Phys.</i>, <a href="/docs/linux/man/3-72/">72</a>(3), 367-375.</p>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>trend1d</code>, <code>trend2d</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
