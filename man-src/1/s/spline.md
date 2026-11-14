---
title: "spline(1)"
name: "spline"
section: "1"
letter: "s"
url: "/docs/linux/man/1-spline/"
description: "spline – interpolate datasets using splines under tension"
---

<h2>NAME</h2>
<p> spline &#8211; interpolate datasets using splines under tension</p>
<h2>SYNOPSIS</h2>
<p> <code>spline</code> [ <i>options </i> ] [ <i>files </i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>spline</code> reads datasets from standard input or from one or more files, and fits a smooth curve (a &quot;spline&quot;) through each dataset. An interpolated version of each dataset, consisting of points from the smooth curve, is written to standard output. </p>
<p> Unless the <code>-a</code> or <code>-A</code> options are used (see below), each dataset should be a sequence of values for a vector-valued function of a single scalar variable. That is, each dataset should be a sequence of data points, given as alternating <i>t</i> and <i>y</i> values. <i>t</i> is a scalar independent variable, and <i>y</i> is a vector-valued dependent variable. The dimensionality of <i>y</i> is specified with the <code>-d </code> option (the default dimensionality is 1). Between each data point and the next, <i>t</i> should increase. </p>
<p> An input file may contain more than a single dataset. If an input file is in <font SIZE="-1">ASCII </font> format (the default), its datasets should be separated by blank lines. The <i>t</i> and <i>y</i> values of the data points in each dataset may be arranged arbitrarily, so long as they are separated by white space. Besides datasets, an input file may contain any number of comment lines, which should begin with the comment character `#&#8217;. Comment lines are ignored. They are not treated as blank, i.e., they do not interrupt a dataset in progress. </p>
<p> Options and file names may be interspersed on the command line, but the options are processed before the file names are read. If <code>&#8212; </code> is seen, it is interpreted as the end of the options. If no file names are specified, or the file name <code>&#8211; </code> is encountered, the standard input is read. </p>
<p> The type of interpolation, and the format of the input and output files, may be selected by command-line options.</p>
<h2>OPTIONS</h2>
<h3>Interpolation-Related Options</h3>
<dl>
<dt><code>-f</code></p>
<dd>
<dt><code>&#8211;filter</code></p>
<dd> Use a local interpolation algorithm (the cubic Bessel algorithm), so that <code>spline</code> can be used as a real-time filter. The slope of the interpolating curve at each point in a dataset will be chosen by fitting a quadratic function through that point and the two adjacent points in the dataset. If <code>-f</code> is specified then the <code>-t</code> option, otherwise optional, must be used as well. Also, if <code>-f</code> is specified then the <code>-k</code>, <code>-p</code>, and <code>-T</code> options may not be used.</p>
<dt>
<dd> If <code>-f</code> is <i>not</i> specified, then the default (global) interpolation algorithm will be used.</p>
<dt><code>-k</code><i> k</i></p>
<dd>
<dt><code>&#8211;boundary-condition</code><i> k</i></p>
<dd> Set the boundary condition parameter for each constructed spline to be <i>k</i>. (The default value is 1.0.) In each of its components, the spline will satisfy the two boundary conditions y&quot;[0]=ky&quot;[1] and y&quot;[n]=ky&quot;[n-1]. Here y[0] and y[1] signify the values of a specified component of the vector-valued dependent variable <i>y</i> at the first two points of a dataset, and y[n-1] and y[n] the values at the last two points. Setting <i>k</i> to zero will yield a &quot;natural&quot; spline, i.e., one that has zero curvature at the two ends of the dataset. The <code>-k</code> option may not be used if <code>-f</code> or <code>-p</code> is specified.</p>
<dt><code>-n</code><i> n</i></p>
<dd>
<dt><code>&#8211;number-of-intervals</code><i> n</i></p>
<dd> Subdivide the interval over which interpolation occurs into <i>n</i> subintervals. The number of data points computed, and written to the output, will be <i>n+1</i>. The default value for <i>n</i> is 100.</p>
<dt><code>-p</code></p>
<dd>
<dt><code>&#8211;periodic</code></p>
<dd> Construct a periodic spline. If this option is specified, the <i>y</i> values for the first and last points in each dataset must be equal. The <code>-f</code> and <code>-k</code> options may not be used if <code>-p</code> is specified.</p>
<dt><code>-T</code><i> tension</i></p>
<dd>
<dt><code>&#8211;tension</code><i> tension</i></p>
<dd> Each interpolating curve will be a spline under tension. This option sets the tension value (the default is 0.0).</p>
<dt>
<dd> If <i>tension</i> equals zero, the curve will be a piecewise cubic spline. Increasing the tension above zero makes the curve &quot;tighter&quot;, and reduces the likelihood of spurious inflection points. That is because between each pair of successive points in a dataset, the curve will satisfy the fourth-order differential equation y&quot;&quot;=sgn(<i>tension</i>)*(<i>tension</i>^2)y&quot; in each of its components. As <i>tension</i> increases to positive infinity, it will converge to a polygonal line. The <code>-T</code> option may not be used if <code>-f</code> is specified.</p>
<dt><code>-t </code><i>tmin tmax [tspacing]</i></p>
<dd>
<dt><code>&#8211;t-spacing </code><i>tmin tmax [tspacing]</i></p>
<dd> For each dataset, set the interval over which interpolation occurs to be the interval between <i>tmin</i> and <i>tmax</i>. If <i>tspacing</i> is not specified, the interval will be divided into the number of subintervals specified by the <code>-n</code> option.</p>
<dt>
<dd> If the <code>-t</code> option is not used, the interval over which interpolation occurs will be the entire range of the independent variable in the dataset. The <code>-t</code> option must always be used if the <code>-f</code> option is used to request filter-like behavior (see above).</dl>
<h3>Format-Related Options</h3>
<dl>
<dt><code>-d</code><i> dimension</i></p>
<dd>
<dt><code>&#8211;y-dimension</code><i> dimension</i></p>
<dd> Set the dimensionality of the dependent variable <i>y</i> in the input and output files to be <i>dimension</i>. The default dimension is 1.</p>
<dt><code>-I</code><i> data-format</i></p>
<dd>
<dt><code>&#8211;input-format</code><i> data-format</i></p>
<dd> Set the data format for the input file(s) to be <i>data-format</i>, which may be one of the following.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>a</code></p>
<dd> <font SIZE="-1">ASCII</font> format (the default). Each file is a sequence of floating point numbers, interpreted as the <i>t</i> and <i>y</i> coordinates of the successive data points in a dataset. If <i>y</i> is <i>d</i>-dimensional, there will be <i>d+1</i> numbers for each point. The <i>t</i> and <i>y</i> coordinates of a point need not appear on the same line, and points need not appear on different lines. But if a blank line occurs (i.e., two newlines in succession are seen), it is interpreted as the end of a dataset, and the beginning of the next.</p>
<dt><code>f</code></p>
<dd> Single precision binary format. Each file is a sequence of floating point numbers, interpreted as the <i>t</i> and <i>y</i> coordinates of the successive data points in a dataset. If <i>y</i> is <i>d</i>-dimensional, there will be <i>d+1</i> numbers for each point. Successive datasets are separated by a single occurrence of the quantity <font SIZE="-1">FLT_MAX, </font> which is the largest possible single precision floating point number. On most machines this is approximately 3.4&#215;10^38.</p>
<dt><code>d</code></p>
<dd> Double precision binary format. Each file is a sequence of double precision floating point numbers, interpreted as the <i>t</i> and <i>y</i> coordinates of the successive data points in a dataset. If <i>y</i> is <i>d</i>-dimensional, there will be <i>d+1</i> numbers for each point. Successive datasets are separated by a single occurrence of the quantity <font SIZE="-1">DBL_MAX,</font> which is the largest possible double precision floating point number. On most machines this is approximately 1.8&#215;10^308.</p>
<dt><code>i</code></p>
<dd> Integer binary format. Each file is a sequence of integers, interpreted as the <i>t</i> and <i>y</i> coordinates of the successive data points in a dataset. If <i>y</i> is <i>d</i>-dimensional, there will be <i>d+1</i> numbers for each point. Successive datasets are separated by a single occurrence of the quantity <font SIZE="-1">INT_MAX,</font> which is the largest possible integer. On most machines this is 2^31-1.</dl>
</dl>
<dt><code>-a </code><i>[step_size [lower_limit]]</i></p>
<dd>
<dt><code>&#8211;auto-abscissa </code><i>[step_size [lower_limit]]</i></p>
<dd> Automatically generate values for <i>t</i>, the independent variable (the default values of <i>step_size</i> and <i>lower_limit</i> are 1.0 and 0.0, respectively).</p>
<dt>
<dd> Irrespective of data format (`a&#8217;, `f&#8217;, `d&#8217;, or `i&#8217;), this option specifies that the values of <i>t</i> are missing from the input file: the dataset(s) to be read contain only values of <i>y</i>, the dependent variable. So if <i>y</i> is <i>d</i>-dimensional, there will be only <i>d</i> numbers for each point. The increment from each <i>t</i> value to the next will be <i>step_size</i>, and the first <i>t</i> value will be <i>lower_limit</i>. This option is useful, e.g., when interpolating curves rather than functions.</p>
<dt><code>-A</code></p>
<dd>
<dt><code>&#8211;auto-dist-abscissa</code></p>
<dd> Automatically generate values for <i>t</i>, the independent variable. This is a variant form of the <code>-a</code> option. The increment from each <i>t</i> value to the next will be the distance in <i>d</i>-dimensional space between the corresponding <i>y</i> values, and the first <i>t</i> value will be 0.0. That is, <i>t</i> will be &quot;polygonal arclength&quot;. This option is useful when interpolating curves rather than functions.</p>
<dt><code>-O</code><i> data-format</i></p>
<dd>
<dt><code>&#8211;output-format</code><i> data-format</i></p>
<dd> Set the data format for the output file to be <i>data-format</i>. The interpretation of <i>data-format</i> is the same as for the <code>-I</code> option. The default is `a&#8217;, i.e., <font SIZE="-1">ASCII</font> format.</p>
<dt><code>-P</code><i> significant-digits</i></p>
<dd>
<dt><code>&#8211;precision</code><i> significant-digits</i></p>
<dd> Set the numerical precision for the <i>t</i> and <i>y</i> values in the output file to be <i>significant-digits</i>. This takes effect only if the output file is written in `a&#8217; format, i.e., in <font SIZE="-1">ASCII.</font> <i>significant-digits</i> must be a positive integer (the default is 6).</p>
<dt><code>-s</code></p>
<dd>
<dt><code>&#8211;suppress-abscissa</code></p>
<dd> Omit the independent variable <i>t</i> from the output file; for each point, supply only the dependent variable <i>y</i>. If <i>y</i> is <i>d</i>-dimensional, there will be only <i>d</i> numbers for each point, not <i>d+1</i>. This option is useful when interpolating curves rather than functions.</dl>
<h3>Informational Options</h3>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Print a list of command-line options, and exit.</p>
<dt><code>&#8211;version</code></p>
<dd> Print the version number of <code>spline</code> and the plotting utilities package, and exit.</dl>
<h2>EXAMPLES</h2>
<p> Typing </p>
<dl>
<dt>
<dd> <code>echo 0 0 1 1 2 0 | spline</code></dl>
<p> will produce on standard output an interpolated dataset consisting of 101 data points. If graphed, this interpolated dataset will yield a parabola. </p>
<p> It is sometimes useful to interpolate between a sequence of arbitrarily placed points in <i>d</i>-dimensional space, i.e., to &quot;spline a curve&quot; rather than a function. The <code>-a</code> and <code>-s</code> options are used for this. For example, </p>
<dl>
<dt>
<dd> <code>echo 0 0 1 0 1 1 0 1 | spline -d 2 -a -s </code></dl>
<p> will produce on standard output a 101-point dataset that interpolates between the four points (0,0), (1,0), (1,1), and (0,1). The <code>-d 2</code> option specifies that the dependent variable <i>y</i> is two-dimensional. The <code>-a</code> option specifies that the <i>t</i> values are missing from the input and should be automatically generated. The <code>-s</code> option specifies that the <i>t</i> values should be stripped from the output.</p>
<h2>AUTHORS</h2>
<p> <code>spline</code> was written by Robert S. Maier (<code>rsm [at] math.arizona.edu</code>), starting with an earlier version by Rich Murphey (<code>rich [at] freebsd.org</code>). The algorithms for constructing splines under tension are similar to those used in the FITPACK subroutine library, and are ultimately due to Alan K. Cline (<code>cline [at] cs.utexas.edu</code>).</p>
<h2>SEE ALSO</h2>
<p> &quot;The GNU Plotting Utilities Manual&quot;.</p>
<h2>BUGS</h2>
<p> Email bug reports to <code>bug-gnu-utils [at] gnu.org</code>. </p>
<h2>Index</h2>
