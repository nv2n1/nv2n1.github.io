---
title: "ode(1)"
name: "ode"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ode/"
description: "ode – numerical solution of ordinary differential equations"
---

<h2>NAME</h2>
<p> ode &#8211; numerical solution of ordinary differential equations</p>
<h2>SYNOPSIS</h2>
<p> <code>ode</code> [ <i>options</i> ] [ <i>file</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>ode</code> is a tool that solves, by numerical integration, the initial value problem for a specified system of first-order ordinary differential equations. Three distinct numerical integration schemes are available: Runge-Kutta-Fehlberg (the default), Adams-Moulton, and Euler. The Adams-Moulton and Runge-Kutta schemes are available with adaptive step size. </p>
<p> The operation of <code>ode</code> is specified by a program, written in its input language. The program is simply a list of expressions for the derivatives of the variables to be integrated, together with some control statements. Some examples are given in the <font SIZE="-1"><code>EXAMPLES </code></font> section. </p>
<p> <code>ode</code> reads the program from the specified file, or from standard input if no file name is given. If reading from standard input, <code>ode</code> will stop reading and exit when it sees a single period on a line by itself. </p>
<p> At each time step, the values of variables specified in the program are written to standard output. So a table of values will be produced, with each column showing the evolution of a variable. If there are only two columns, the output can be piped to <code><a href="/docs/linux/man/1-graph/">graph</a></code>(1) or a similar plotting program.</p>
<h2>OPTIONS</h2>
<h3>Input Options</h3>
<dl>
<dt><code>-f</code><i> file</i></p>
<dd>
<dt><code>&#8211;input-file</code><i> file</i></p>
<dd> Read input from <i>file</i> before reading from standard input. This option makes it possible to work interactively, after reading a program fragment that defines the system of differential equations.</dl>
<h3>Output Options</h3>
<dl>
<dt><code>-p</code><i> prec</i></p>
<dd>
<dt><code>&#8211;precision</code><i> prec</i></p>
<dd> When printing numerical results, use <i>prec</i> significant digits (the default is 6). If this option is given, the print format will be scientific notation.</p>
<dt><code>-t</code></p>
<dd>
<dt><code>&#8211;title</code></p>
<dd> Print a title line at the head of the output, naming the variables in each column. If this option is given, the print format will be scientific notation.</dl>
<h3>Integration Scheme Options</h3>
<p> The following options specify the numerical integration scheme. Only one of the three basic options <code>-R</code>, <code>-A</code>, <code>-E</code> may be specified. The default is <code>-R</code> (Runge-Kutta-Fehlberg).</p>
<dl>
<dt><code>-R</code><i> [stepsize]</i></p>
<dd>
<dt><code>&#8211;runge-kutta</code><i> [stepsize]</i></p>
<dd> Use a fifth-order Runge-Kutta-Fehlberg algorithm, with an adaptive stepsize unless a constant stepsize is specified. When a constant stepsize is specified and no error analysis is requested, then a classical fourth-order Runge-Kutta scheme is used.</p>
<dt><code>-A</code><i> [stepsize]</i></p>
<dd>
<dt><code>&#8211;adams-moulton</code><i> [stepsize]</i></p>
<dd> Use a fourth-order Adams-Moulton predictor-corrector scheme, with an adaptive stepsize unless a constant stepsize, <i>stepsize</i>, is specified. The Runge-Kutta-Fehlberg algorithm is used to get past `bad&#8217; points (if any).</p>
<dt><code>-E</code><i> [stepsize]</i></p>
<dd>
<dt><code>&#8211;euler</code><i> [stepsize]</i></p>
<dd> Use a `quick and dirty&#8217; Euler scheme, with a constant stepsize. The default value of <i>stepsize</i> is 0.1. Not recommended for serious applications.</p>
<dt>
<dd> The error bound options <code>-r</code> and <code>-e</code> (see below) may not be used if <code>-E</code> is specified.</p>
<dt><code>-h</code><i> hmin [hmax]</i></p>
<dd>
<dt><code>&#8211;step-size-bound</code><i> hmin [hmax]</i></p>
<dd> Use a lower bound <i>hmin</i> on the stepsize. The numerical scheme will not let the stepsize go below <i>hmin</i>. The default is to allow the stepsize to shrink to the machine limit, i.e., the minimum nonzero double-precision floating point number.</p>
<dt>
<dd> The optional argument <i>hmax</i>, if included, specifies a maximum value for the stepsize. It is useful in preventing the numerical routine from skipping quickly over an interesting region.</dl>
<h3>Error Bound Options</h3>
<dl>
<dt><code>-r</code><i> rmax [rmin]</i></p>
<dd>
<dt><code>&#8211;relative-error-bound</code><i> rmax [rmin]</i></p>
<dd> The <code>-r</code> option sets an upper bound on the relative single-step error. If the <code>-r</code> option is used, the relative single-step error in any dependent variable will never exceed <i>rmax</i> (the default for which is 10^-9). If this should occur, the solution will be abandoned and an error message will be printed. If the stepsize is not constant, the stepsize will be decreased `adaptively&#8217;, so that the upper bound on the single-step error is not violated. Thus, choosing a smaller upper bound on the single-step error will cause smaller stepsizes to be chosen. A lower bound <i>rmin</i> may optionally be specified, to suggest when the stepsize should be increased (the default for <i>rmin</i> is <i>rmax</i>/1000).</p>
<dt><code>-e</code><i> emax [emin]</i></p>
<dd>
<dt><code>&#8211;absolute-error-bound</code><i> emax [emin]</i></p>
<dd> Similar to <code>-r</code>, but bounds the absolute rather than the relative single-step error.</p>
<dt><code>-s</code></p>
<dd>
<dt><code>&#8211;suppress-error-bound</code></p>
<dd> Suppress the ceiling on single-step error, allowing <code>ode</code> to continue even if this ceiling is exceeded. This may result in large numerical errors.</dl>
<h3>Informational Options</h3>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Print a list of command-line options, and exit.</p>
<dt><code>&#8211;version</code></p>
<dd> Print the version number of <code>ode</code> and the plotting utilities package, and exit.</dl>
<h2>DIAGNOSTICS</h2>
<p> Mostly self-explanatory. The biggest exception is `syntax error&#8217;, meaning there is a grammatical error. Language error messages are of the form </p>
<dl>
<dt>
<dd> <code>ode: nnn: message&#8230;</code></dl>
<p> where `nnn&#8217; is the number of the input line containing the error. If the <code>-f</code> option is used, the phrase &quot;(file)&quot; follows the `nnn&#8217; for errors encountered inside the file. Subsequently, when <code>ode</code> begins reading the standard input, line numbers start over from 1. </p>
<p> No effort is made to recover successfully from syntactic errors in the input. However, there is a meager effort to resynchronize so more than one error can be found in one scan. </p>
<p> Run-time errors elicit a message describing the problem, and the solution is abandoned.</p>
<h2>EXAMPLES</h2>
<p> The program </p>
<dl>
<dt>
<dd> <code>y&#8217; = y</code><br />
 <code>y = 1</code><br />
 <code>print t, y</code><br />
 <code>step 0, 1</code></dl>
<p> solves an initial value problem whose solution is <i>y=e^t</i>. When <code>ode</code> runs this program, it will write two columns of numbers to standard output. Each line will show the value of the independent variable <i>t</i>, and the variable <i>y</i>, as <i>t</i> is stepped from 0 to 1. </p>
<p> A more sophisticated example would be </p>
<dl>
<dt>
<dd> <code>sine&#8217; = cosine</code><br />
 <code>cosine&#8217; = -sine</code><br />
 <code>sine = 0</code><br />
 <code>cosine = 1</code><br />
 <code>print t, sine</code><br />
 <code>step 0, 2*PI</code></dl>
<p> This program solves an initial value problem for a system of two differential equations. The initial value problem turns out to define the sine and cosine functions. The program steps the system over a full period.</p>
<h2>AUTHORS</h2>
<p> <code>ode</code> was written by Nicholas B. Tufillaro (<code>nbt [at] reed.edu</code>), and slightly enhanced by Robert S. Maier (<code>rsm [at] math.arizona.edu</code>) to merge it into the GNU plotting utilities.</p>
<h2>SEE ALSO</h2>
<p> &quot;The GNU Plotting Utilities Manual&quot;.</p>
<h2>BUGS</h2>
<p> Email bug reports to <code>bug-gnu-utils [at] gnu.org</code>. </p>
<h2>Index</h2>
