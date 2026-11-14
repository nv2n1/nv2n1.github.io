---
title: "gmtmath(1)"
name: "gmtmath"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gmtmath/"
description: "gmtmath – Reverse Polish Notation (RPN) calculator for data tables"
---

<h2>NAME</h2>
<p> gmtmath &#8211; Reverse Polish Notation (RPN) calculator for data tables</p>
<h2>SYNOPSIS</h2>
<p> <code>gmtmath</code> [ <i>t_f(t).d</i>[<code>+e</code>][<code>+s</code>|<code>w</code>] ] [ <i>cols</i> ] [ <i>eigen</i> ] [ ] [ <i>n_col</i>[/<i>t_col</i>] ] [ ] [ [<code>f</code>|<code>l</code>] ] [ <i>t_min</i>/<i>t_max</i>/<i>t_inc</i>[<code>+</code>]|<i>tfile</i> ] [ [<i>level</i>] ] [ <code>-b</code><i>&lt;binary&gt;</i> ] [ <code>-d</code><i>&lt;nodata&gt;</i> ] [ <code>-f</code><i>&lt;flags&gt;</i> ] [ <code>-g</code><i>&lt;gaps&gt;</i> ] [ <code>-h</code><i>&lt;headers&gt;</i> ] [ <code>-i</code><i>&lt;flags&gt;</i> ] [ <code>-o</code><i>&lt;flags&gt;</i> ] [ <code>-s</code><i>&lt;flags&gt;</i> ] <i>operand</i> [ <i>operand</i> ] <code>OPERATOR</code> [ <i>operand</i> ] <code>OPERATOR</code> &#8230; <code>=</code> [ <i>outfile</i> ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>gmtmath</code> will perform operations like add, subtract, multiply, and divide on one or more table data files or constants using Reverse Polish Notation (RPN) syntax (e.g., Hewlett-Packard calculator-style). Arbitrarily complicated expressions may therefore be evaluated; the final result is written to an output file [or standard output]. Data operations are element-by-element, not matrix manipulations (except where noted). Some operators only require one operand (see below). If no data tables are used in the expression then options <code>-T</code>, <code>-N</code> can be set (and optionally <code>-bo</code> to indicate the data type for binary tables). If STDIN is given, the standard input will be read and placed on the stack as if a file with that content had been given on the command line. By default, all columns except the &quot;time&quot; column are operated on, but this can be changed (see <code>-C</code>). Complicated or frequently occurring expressions may be coded as a macro for future use or stored and recalled via named memory locations.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>operand</i></p>
<dd> If <i>operand</i> can be opened as a file it will be read as an ASCII (or binary, see <code>-bi</code>) table data file. If not a file, it is interpreted as a numerical constant or a special symbol (see below). The special argument STDIN means that <i>stdin</i> will be read and placed on the stack; STDIN can appear more than once if necessary.</p>
<dt><i>outfile</i></p>
<dd> The name of a table data file that will hold the final result. If not given then the output is sent to stdout.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-A</code><i>t_f(t).d</i>[<code>+e</code>][<code>+s</code>|<code>w</code>]</p>
<dd> Requires <code>-N</code> and will partially initialize a table with values from the given file containing <i>t</i> and <i>f(t)</i> only. The <i>t</i> is placed in column <i>t_col</i> while <i>f(t)</i> goes into column <i>n_col</i> &#8211; 1 (see <code>-N</code>). If used with operators LSQFIT and SVDFIT you can optionally append the modifier <code>+e</code> which will instead evaluate the solution and write a data set with four columns: t, f(t), the model solution at t, and the the residuals at t, respectively [Default writes one column with model coefficients]. Append <code>+w</code> if <i>t_f(t).d</i> has a third column with weights, or append <code>+s</code> if <i>t_f(t).d</i> has a third column with 1-sigma. In those two cases we find the weighted solution. The weights (or sigmas) will be output as the last column when <code>+e</code> is in effect.</p>
<dt><code>-C</code><i>cols</i></p>
<dd> Select the columns that will be operated on until next occurrence of <code>-C</code>. List columns separated by commas; ranges like 1,3-5,7 are allowed. <code>-C</code> (no arguments) resets the default action of using all columns except time column (see <code>-N</code>). <code>-Ca</code> selects all columns, including time column, while <code>-Cr</code> reverses (toggles) the current choices. When <code>-C</code> is in effect it also controls which columns from a file will be placed on the stack.</p>
<dt><code>-E</code><i>eigen</i></p>
<dd> Sets the minimum eigenvalue used by operators LSQFIT and SVDFIT [1e-7]. Smaller eigenvalues are set to zero and will not be considered in the solution.</p>
<dt><code>-I</code></p>
<dd> Reverses the output row sequence from ascending time to descending [ascending].</p>
<dt><code>-N</code><i>n_col</i>[/<i>t_col</i>]</p>
<dd> Select the number of columns and optionally the column number that contains the &quot;time&quot; variable [0]. Columns are numbered starting at 0 [2/0]. If input files are specified then <code>-N</code> will add any missing columns.</p>
<dt><code>-Q</code></p>
<dd> Quick mode for scalar calculation. Shorthand for <code>-Ca</code> <code>-N</code>1/0 <code>-T</code>0/0/1.</p>
<dt><code>-S</code>[<code>f</code>|<code>l</code>]</p>
<dd> Only report the first or last row of the results [Default is all rows]. This is useful if you have computed a statistic (say the <code>MODE</code>) and only want to report a single number instead of numerous records with identical values. Append <code>l</code> to get the last row and <code>f</code> to get the first row only [Default].</p>
<dt><code>-T</code><i>t_min</i>/<i>t_max</i>/<i>t_inc</i>[<code>+</code>]|<i>tfile</i></p>
<dd> Required when no input files are given. Sets the t-coordinates of the first and last point and the equidistant sampling interval for the &quot;time&quot; column (see <code>-N</code>). Append <code>+</code> if you are specifying the number of equidistant points instead. If there is no time column (only data columns), give <code>-T</code> with no arguments; this also implies <code>-Ca</code>. Alternatively, give the name of a file whose first column contains the desired t-coordinates which may be irregular.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-bi</code>[<i>ncols</i>][<code>t</code>] <i>(more &#8230;)</i></p>
<dd> Select native binary input.</p>
<dt><code>-bo</code>[<i>ncols</i>][<i>type</i>] <i>(more &#8230;)</i></p>
<dd> Select native binary output. [Default is same as input, but see <code>-o</code>]</p>
<dt><code>-d</code>[<code>i</code>|<code>o</code>]<i>nodata</i> <i>(more &#8230;)</i></p>
<dd> Replace input columns that equal <i>nodata</i> with NaN and do the reverse on output.</p>
<dt><code>-f</code>[<code>i</code>|<code>o</code>]<i>colinfo</i> <i>(more &#8230;)</i></p>
<dd> Specify data types of input and/or output columns.</p>
<dt><code>-g</code>[<code>a</code>]<code>x</code>|<code>y</code>|<code>d</code>|<code>X</code>|<code>Y</code>|<code>D</code>|[<i>col</i>]<code>z</code>[+|-]<i>gap</i>[<code>u</code>] <i>(more &#8230;)</i></p>
<dd> Determine data gaps and line breaks.</p>
<dt><code>-h</code>[<code>i</code>|<code>o</code>][<i>n</i>][<code>+c</code>][<code>+d</code>][<code>+r</code><i>remark</i>][<code>+r</code><i>title</i>] <i>(more &#8230;)</i></p>
<dd> Skip or produce header record(s).</p>
<dt><code>-i</code><i>cols</i>[<code>l</code>][<code>s</code><i>scale</i>][<code>o</code><i>offset</i>][,<i>&#8230;</i>] <i>(more &#8230;)</i></p>
<dd> Select input columns (0 is first column).</p>
<dt><code>-o</code><i>cols</i>[,&#8230;] <i>(more &#8230;)</i></p>
<dd> Select output columns (0 is first column).</p>
<dt><code>-s</code>[<i>cols</i>][<code>a</code>|<code>r</code>] <i>(more &#8230;)</i></p>
<dd> Set handling of NaN records.</p>
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
<h2>OPERATORS</h2>
<p> Choose among the following 146 operators. &quot;args&quot; are the number of input and output arguments. <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Operator </td>
<td> args </td>
<td> Returns
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>ABS</code> </td>
<td> 1 1 </td>
<td> abs (A)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>ACOS</code> </td>
<td> 1 1 </td>
<td> acos (A)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>ACOSH</code> </td>
<td> 1 1 </td>
<td> acosh (A)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>ACSC</code> </td>
<td> 1 1 </td>
<td> acsc (A)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>ACOT</code> </td>
<td> 1 1 </td>
<td> acot (A)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>ADD</code> </td>
<td> 2 1 </td>
<td> A + B
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>AND</code> </td>
<td> 2 1 </td>
<td> B if A == NaN, else A
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>ASEC</code> </td>
<td> 1 1 </td>
<td> asec (A)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>ASIN</code> </td>
<td> 1 1 </td>
<td> asin (A)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>ASINH</code> </td>
<td> 1 1 </td>
<td> asinh (A)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>ATAN</code> </td>
<td> 1 1 </td>
<td> atan (A)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>ATAN2</code> </td>
<td> 2 1 </td>
<td> atan2 (A, B)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>ATANH</code> </td>
<td> 1 1 </td>
<td> atanh (A)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>BCDF</code> </td>
<td> 3 1 </td>
<td> Binomial cumulative distribution function for p = A, n = B, and x = C
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>BPDF</code> </td>
<td> 3 1 </td>
<td> Binomial probability density function for p = A, n = B, and x = C
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>BEI</code> </td>
<td> 1 1 </td>
<td> bei (A)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>BER</code> </td>
<td> 1 1 </td>
<td> ber (A)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>BITAND</code> </td>
<td> 2 1 </td>
<td> A &amp; B (bitwise AND operator)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>BITLEFT</code> </td>
<td> 2 1 </td>
<td> A &lt;&lt; B (bitwise left-shift operator)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>BITNOT</code> </td>
<td> 1 1 </td>
<td> ~A (bitwise NOT operator, i.e., return two&#8217;s complement)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>BITOR</code> </td>
<td> 2 1 </td>
<td> A | B (bitwise OR operator)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>BITRIGHT</code> </td>
<td> 2 1 </td>
<td> A &gt;&gt; B (bitwise right-shift operator)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>BITTEST</code> </td>
<td> 2 1 </td>
<td> 1 if bit B of A is set, else 0 (bitwise TEST operator)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>BITXOR</code> </td>
<td> 2 1 </td>
<td> A ^ B (bitwise XOR operator)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>CEIL</code> </td>
<td> 1 1 </td>
<td> ceil (A) (smallest integer &gt;= A)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>CHICRIT</code> </td>
<td> 2 1 </td>
<td> Chi-squared distribution critical value for alpha = A and nu = B
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>CHICDF</code> </td>
<td> 2 1 </td>
<td> Chi-squared cumulative distribution function for chi2 = A and nu = B
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>CHIPDF</code> </td>
<td> 2 1 </td>
<td> Chi-squared probability density function for chi2 = A and nu = B
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>COL</code> </td>
<td> 1 1 </td>
<td> Places column A on the stack
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>COMB</code> </td>
<td> 2 1 </td>
<td> Combinations n_C_r, with n = A and r = B
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>CORRCOEFF</code> </td>
<td> 2 1 </td>
<td> Correlation coefficient r(A, B)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>COS</code> </td>
<td> 1 1 </td>
<td> cos (A) (A in radians)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>COSD</code> </td>
<td> 1 1 </td>
<td> cos (A) (A in degrees)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>COSH</code> </td>
<td> 1 1 </td>
<td> cosh (A)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>COT</code> </td>
<td> 1 1 </td>
<td> cot (A) (A in radians)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>COTD</code> </td>
<td> 1 1 </td>
<td> cot (A) (A in degrees)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>CSC</code> </td>
<td> 1 1 </td>
<td> csc (A) (A in radians)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>CSCD</code> </td>
<td> 1 1 </td>
<td> csc (A) (A in degrees)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>DDT</code> </td>
<td> 1 1 </td>
<td> d(A)/dt Central 1st derivative
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>D2DT2</code> </td>
<td> 1 1 </td>
<td> d^2(A)/dt^2 2nd derivative
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>D2R</code> </td>
<td> 1 1 </td>
<td> Converts Degrees to Radians
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>DENAN</code> </td>
<td> 2 1 </td>
<td> Replace NaNs in A with values from B
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>DILOG</code> </td>
<td> 1 1 </td>
<td> dilog (A)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>DIFF</code> </td>
<td> 1 1 </td>
<td> Difference between adjacent elements of A (A[1]-A[0], A[2]-A[1], &#8230;, 0)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>DIV</code> </td>
<td> 2 1 </td>
<td> A / B
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>DUP</code> </td>
<td> 1 2 </td>
<td> Places duplicate of A on the stack
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>ECDF</code> </td>
<td> 2 1 </td>
<td> Exponential cumulative distribution function for x = A and lambda = B
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>ECRIT</code> </td>
<td> 2 1 </td>
<td> Exponential distribution critical value for alpha = A and lambda = B
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>EPDF</code> </td>
<td> 2 1 </td>
<td> Exponential probability density function for x = A and lambda = B
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>ERF</code> </td>
<td> 1 1 </td>
<td> Error function erf (A)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>ERFC</code> </td>
<td> 1 1 </td>
<td> Complementary Error function erfc (A)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>ERFINV</code> </td>
<td> 1 1 </td>
<td> Inverse error function of A
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>EQ</code> </td>
<td> 2 1 </td>
<td> 1 if A == B, else 0
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>EXCH</code> </td>
<td> 2 2 </td>
<td> Exchanges A and B on the stack
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>EXP</code> </td>
<td> 1 1 </td>
<td> exp (A)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>FACT</code> </td>
<td> 1 1 </td>
<td> A! (A factorial)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>FCDF</code> </td>
<td> 3 1 </td>
<td> F cumulative distribution function for F = A, nu1 = B, and nu2 = C
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>FCRIT</code> </td>
<td> 3 1 </td>
<td> F distribution critical value for alpha = A, nu1 = B, and nu2 = C
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>FLIPUD</code> </td>
<td> 1 1 </td>
<td> Reverse order of each column
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>FLOOR</code> </td>
<td> 1 1 </td>
<td> floor (A) (greatest integer &lt;= A)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>FMOD</code> </td>
<td> 2 1 </td>
<td> A % B (remainder after truncated division)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>FPDF</code> </td>
<td> 3 1 </td>
<td> F probability density function for F = A, nu1 = B, and nu2 = C
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>GE</code> </td>
<td> 2 1 </td>
<td> 1 if A &gt;= B, else 0
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>GT</code> </td>
<td> 2 1 </td>
<td> 1 if A &gt; B, else 0
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>HYPOT</code> </td>
<td> 2 1 </td>
<td> hypot (A, B) = sqrt (A*A + B*B)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>I0</code> </td>
<td> 1 1 </td>
<td> Modified Bessel function of A (1st kind, order 0)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>I1</code> </td>
<td> 1 1 </td>
<td> Modified Bessel function of A (1st kind, order 1)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>IFELSE</code> </td>
<td> 3 1 </td>
<td> B if A != 0, else C
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>IN</code> </td>
<td> 2 1 </td>
<td> Modified Bessel function of A (1st kind, order B)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>INRANGE</code> </td>
<td> 3 1 </td>
<td> 1 if B &lt;= A &lt;= C, else 0
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>INT</code> </td>
<td> 1 1 </td>
<td> Numerically integrate A
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>INV</code> </td>
<td> 1 1 </td>
<td> 1 / A
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>ISFINITE</code> </td>
<td> 1 1 </td>
<td> 1 if A is finite, else 0
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>ISNAN</code> </td>
<td> 1 1 </td>
<td> 1 if A == NaN, else 0
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>J0</code> </td>
<td> 1 1 </td>
<td> Bessel function of A (1st kind, order 0)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>J1</code> </td>
<td> 1 1 </td>
<td> Bessel function of A (1st kind, order 1)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>JN</code> </td>
<td> 2 1 </td>
<td> Bessel function of A (1st kind, order B)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>K0</code> </td>
<td> 1 1 </td>
<td> Modified Kelvin function of A (2nd kind, order 0)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>K1</code> </td>
<td> 1 1 </td>
<td> Modified Bessel function of A (2nd kind, order 1)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>KN</code> </td>
<td> 2 1 </td>
<td> Modified Bessel function of A (2nd kind, order B)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>KEI</code> </td>
<td> 1 1 </td>
<td> kei (A)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>KER</code> </td>
<td> 1 1 </td>
<td> ker (A)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>KURT</code> </td>
<td> 1 1 </td>
<td> Kurtosis of A
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>LCDF</code> </td>
<td> 1 1 </td>
<td> Laplace cumulative distribution function for z = A
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>LCRIT</code> </td>
<td> 1 1 </td>
<td> Laplace distribution critical value for alpha = A
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>LE</code> </td>
<td> 2 1 </td>
<td> 1 if A &lt;= B, else 0
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>LMSSCL</code> </td>
<td> 1 1 </td>
<td> LMS scale estimate (LMS STD) of A
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>LOG</code> </td>
<td> 1 1 </td>
<td> log (A) (natural log)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>LOG10</code> </td>
<td> 1 1 </td>
<td> log10 (A) (base 10)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>LOG1P</code> </td>
<td> 1 1 </td>
<td> log (1+A) (accurate for small A)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>LOG2</code> </td>
<td> 1 1 </td>
<td> log2 (A) (base 2)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>LOWER</code> </td>
<td> 1 1 </td>
<td> The lowest (minimum) value of A
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>LPDF</code> </td>
<td> 1 1 </td>
<td> Laplace probability density function for z = A
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>LRAND</code> </td>
<td> 2 1 </td>
<td> Laplace random noise with mean A and std. deviation B
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>LSQFIT</code> </td>
<td> 1 0 </td>
<td> Let current table be [A | b] return least squares solution x = A \ b
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>LT</code> </td>
<td> 2 1 </td>
<td> 1 if A &lt; B, else 0
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>MAD</code> </td>
<td> 1 1 </td>
<td> Median Absolute Deviation (L1 STD) of A
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>MAX</code> </td>
<td> 2 1 </td>
<td> Maximum of A and B
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>MEAN</code> </td>
<td> 1 1 </td>
<td> Mean value of A
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>MED</code> </td>
<td> 1 1 </td>
<td> Median value of A
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>MIN</code> </td>
<td> 2 1 </td>
<td> Minimum of A and B
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>MOD</code> </td>
<td> 2 1 </td>
<td> A mod B (remainder after floored division)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>MODE</code> </td>
<td> 1 1 </td>
<td> Mode value (Least Median of Squares) of A
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>MUL</code> </td>
<td> 2 1 </td>
<td> A * B
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>NAN</code> </td>
<td> 2 1 </td>
<td> NaN if A == B, else A
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>NEG</code> </td>
<td> 1 1 </td>
<td> -A
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>NEQ</code> </td>
<td> 2 1 </td>
<td> 1 if A != B, else 0
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>NORM</code> </td>
<td> 1 1 </td>
<td> Normalize (A) so max(A)-min(A) = 1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>NOT</code> </td>
<td> 1 1 </td>
<td> NaN if A == NaN, 1 if A == 0, else 0
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>NRAND</code> </td>
<td> 2 1 </td>
<td> Normal, random values with mean A and std. deviation B
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>OR</code> </td>
<td> 2 1 </td>
<td> NaN if B == NaN, else A
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>PCDF</code> </td>
<td> 2 1 </td>
<td> Poisson cumulative distribution function for x = A and lambda = B
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>PERM</code> </td>
<td> 2 1 </td>
<td> Permutations n_P_r, with n = A and r = B
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>PPDF</code> </td>
<td> 2 1 </td>
<td> Poisson distribution P(x,lambda), with x = A and lambda = B
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>PLM</code> </td>
<td> 3 1 </td>
<td> Associated Legendre polynomial P(A) degree B order C
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>PLMg</code> </td>
<td> 3 1 </td>
<td> Normalized associated Legendre polynomial P(A) degree B order C (geophysical convention)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>POP</code> </td>
<td> 1 0 </td>
<td> Delete top element from the stack
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>POW</code> </td>
<td> 2 1 </td>
<td> A ^ B
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>PQUANT</code> </td>
<td> 2 1 </td>
<td> The B&#8217;th Quantile (0-100%) of A
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>PSI</code> </td>
<td> 1 1 </td>
<td> Psi (or Digamma) of A
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>PV</code> </td>
<td> 3 1 </td>
<td> Legendre function Pv(A) of degree v = real(B) + imag(C)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>QV</code> </td>
<td> 3 1 </td>
<td> Legendre function Qv(A) of degree v = real(B) + imag(C)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>R2</code> </td>
<td> 2 1 </td>
<td> R2 = A^2 + B^2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>R2D</code> </td>
<td> 1 1 </td>
<td> Convert Radians to Degrees
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>RAND</code> </td>
<td> 2 1 </td>
<td> Uniform random values between A and B
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>RCDF</code> </td>
<td> 1 1 </td>
<td> Rayleigh cumulative distribution function for z = A
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>RCRIT</code> </td>
<td> 1 1 </td>
<td> Rayleigh distribution critical value for alpha = A
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>RINT</code> </td>
<td> 1 1 </td>
<td> rint (A) (round to integral value nearest to A)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>RPDF</code> </td>
<td> 1 1 </td>
<td> Rayleigh probability density function for z = A
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>ROLL</code> </td>
<td> 2 0 </td>
<td> Cyclicly shifts the top A stack items by an amount B
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>ROTT</code> </td>
<td> 2 1 </td>
<td> Rotate A by the (constant) shift B in the t-direction
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>SEC</code> </td>
<td> 1 1 </td>
<td> sec (A) (A in radians)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>SECD</code> </td>
<td> 1 1 </td>
<td> sec (A) (A in degrees)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>SIGN</code> </td>
<td> 1 1 </td>
<td> sign (+1 or -1) of A
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>SIN</code> </td>
<td> 1 1 </td>
<td> sin (A) (A in radians)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>SINC</code> </td>
<td> 1 1 </td>
<td> sinc (A) (sin (pi*A)/(pi*A))
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>SIND</code> </td>
<td> 1 1 </td>
<td> sin (A) (A in degrees)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>SINH</code> </td>
<td> 1 1 </td>
<td> sinh (A)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>SKEW</code> </td>
<td> 1 1 </td>
<td> Skewness of A
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>SQR</code> </td>
<td> 1 1 </td>
<td> A^2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>SQRT</code> </td>
<td> 1 1 </td>
<td> sqrt (A)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>STD</code> </td>
<td> 1 1 </td>
<td> Standard deviation of A
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>STEP</code> </td>
<td> 1 1 </td>
<td> Heaviside step function H(A)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>STEPT</code> </td>
<td> 1 1 </td>
<td> Heaviside step function H(t-A)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>SUB</code> </td>
<td> 2 1 </td>
<td> A &#8211; B
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>SUM</code> </td>
<td> 1 1 </td>
<td> Cumulative sum of A
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>TAN</code> </td>
<td> 1 1 </td>
<td> tan (A) (A in radians)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>TAND</code> </td>
<td> 1 1 </td>
<td> tan (A) (A in degrees)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>TANH</code> </td>
<td> 1 1 </td>
<td> tanh (A)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>TAPER</code> </td>
<td> 1 1 </td>
<td> Unit weights cosine-tapered to zero within A of end margins
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>TN</code> </td>
<td> 2 1 </td>
<td> Chebyshev polynomial Tn(-1&lt;A&lt;+1) of degree B
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>TCRIT</code> </td>
<td> 2 1 </td>
<td> Student&#8217;s t distribution critical value for alpha = A and nu = B
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>TPDF</code> </td>
<td> 2 1 </td>
<td> Student&#8217;s t probability density function for t = A, and nu = B
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>TCDF</code> </td>
<td> 2 1 </td>
<td> Student&#8217;s t cumulative distribution function for t = A, and nu = B
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>UPPER</code> </td>
<td> 1 1 </td>
<td> The highest (maximum) value of A
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>WCDF</code> </td>
<td> 3 1 </td>
<td> Weibull cumulative distribution function for x = A, scale = B, and shape = C
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>WCRIT</code> </td>
<td> 3 1 </td>
<td> Weibull distribution critical value for alpha = A, scale = B, and shape = C
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>WPDF</code> </td>
<td> 3 1 </td>
<td> Weibull density distribution P(x,scale,shape), with x = A, scale = B, and shape = C
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>XOR</code> </td>
<td> 2 1 </td>
<td> B if A == NaN, else A
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>Y0</code> </td>
<td> 1 1 </td>
<td> Bessel function of A (2nd kind, order 0)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>Y1</code> </td>
<td> 1 1 </td>
<td> Bessel function of A (2nd kind, order 1)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>YN</code> </td>
<td> 2 1 </td>
<td> Bessel function of A (2nd kind, order B)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>ZCDF</code> </td>
<td> 1 1 </td>
<td> Normal cumulative distribution function for z = A
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>ZPDF</code> </td>
<td> 1 1 </td>
<td> Normal probability density function for z = A
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>ZCRIT</code> </td>
<td> 1 1 </td>
<td> Normal distribution critical value for alpha = A
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>ROOTS</code> </td>
<td> 2 1 </td>
<td> Treats col A as f(t) = 0 and returns its roots
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
</table>
<p></center></p>
<h2>SYMBOLS</h2>
<p> The following symbols have special meaning: <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>PI</code> </td>
<td> 3.1415926&#8230;
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>E</code> </td>
<td> 2.7182818&#8230;
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>EULER</code> </td>
<td> 0.5772156&#8230;
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>EPS_F</code> </td>
<td> 1.192092896e-07 (sgl. prec. eps)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>EPS_D</code> </td>
<td> 2.2204460492503131e-16 (dbl. prec. eps)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>TMIN</code> </td>
<td> Minimum t value
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>TMAX</code> </td>
<td> Maximum t value
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>TRANGE</code> </td>
<td> Range of t values
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>TINC</code> </td>
<td> t increment
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>N</code> </td>
<td> The number of records
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>T</code> </td>
<td> Table with t-coordinates
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>TNORM</code> </td>
<td> Table with normalized t-coordinates
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>TROW</code> </td>
<td> Table with row numbers 1, 2, &#8230;, N-1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center></p>
<h2>ASCII FORMAT PRECISION</h2>
<p> The ASCII output formats of numerical data are controlled by parameters in your <code>gmt.conf</code> file. Longitude and latitude are formatted according to <i>FORMAT_GEO_OUT</i>, whereas other values are formatted according to <i>FORMAT_FLOAT_OUT</i>. Be aware that the format in effect can lead to loss of precision in the output, which can lead to various problems downstream. If you find the output is not written with enough precision, consider switching to binary output (<code>-bo</code> if available) or specify more decimals using the <i>FORMAT_FLOAT_OUT</i> setting.</p>
<h2>NOTES ON OPERATORS</h2>
<p> 1. The operators <code>PLM</code> and <code>PLMg</code> calculate the associated Legendre polynomial of degree L and order M in x which must satisfy -1 &lt;= x &lt;= +1 and 0 &lt;= M &lt;= L. x, L, and M are the three arguments preceding the operator. <code>PLM</code> is not normalized and includes the Condon-Shortley phase (-1)^M. <code>PLMg</code> is normalized in the way that is most commonly used in geophysics. The C-S phase can be added by using -M as argument. <code>PLM</code> will overflow at higher degrees, whereas <code>PLMg</code> is stable until ultra high degrees (at least 3000). </p>
<p> 2. Files that have the same names as some operators, e.g., <code>ADD</code>, <code>SIGN</code>, <code>=</code>, etc. should be identified by prepending the current directory (i.e., ./).</p>
<dl>
<dt>3.</p>
<dd> The stack depth limit is hard-wired to 100. </p>
<p> 4. All functions expecting a positive radius (e.g., <code>LOG</code>, <code>KEI</code>, etc.) are passed the absolute value of their argument.</p>
<dt>5.</p>
<dd> The <code>DDT</code> and <code>D2DT2</code> functions only work on regularly spaced data. </p>
<p> 6. All derivatives are based on central finite differences, with natural boundary conditions.</p>
<dt>7.</p>
<dd> <code>ROOTS</code> must be the last operator on the stack, only followed by <code>=</code>.</dl>
<h2>STORE, RECALL AND CLEAR</h2>
<p> You may store intermediate calculations to a named variable that you may recall and place on the stack at a later time. This is useful if you need access to a computed quantity many times in your expression as it will shorten the overall expression and improve readability. To save a result you use the special operator <code>STO</code>@<i>label</i>, where <i>label</i> is the name you choose to give the quantity. To recall the stored result to the stack at a later time, use [<code>RCL</code>]@<i>label</i>, i.e., <code>RCL</code> is optional. To clear memory you may use <code>CLR</code>@<i>label</i>. Note that <code>STO</code> and <code>CLR</code> leave the stack unchanged. </p>
<p> 8. The bitwise operators (<code>BITAND</code>, <code>BITLEFT</code>, <code>BITNOT</code>, <code>BITOR</code>, <code>BITRIGHT</code>, <code>BITTEST</code>, and <code>BITXOR</code>) convert a tables&#8217;s double precision values to unsigned 64-bit ints to perform the bitwise operations. Consequently, the largest whole integer value that can be stored in a double precision value is 2^53 or 9,007,199,254,740,992. Any higher result will be masked to fit in the lower 54 bits. Thus, bit operations are effectively limited to 54 bits. All bitwise operators return NaN if given NaN arguments or bit-settings &lt;= 0. </p>
<p> 9. TAPER will interpret its argument to be a width in the same units as the time-axis, but if no time is provided (i.e., plain data tables) then the width is taken to be given in number of rows.</p>
<h2>MACROS</h2>
<p> Users may save their favorite operator combinations as macros via the file <i>gmtmath.macros</i> in their current or user directory. The file may contain any number of macros (one per record); comment lines starting with # are skipped. The format for the macros is <code>name</code> = <code>arg1 arg2 &#8230; arg2</code> [ : <i>comment</i>] where <code>name</code> is how the macro will be used. When this operator appears on the command line we simply replace it with the listed argument list. No macro may call another macro. As an example, the following macro expects that the time-column contains seafloor ages in Myr and computes the predicted half-space bathymetry: </p>
<p> <code>DEPTH</code> = <code>SQRT 350 MUL 2500 ADD NEG</code> : <i>usage: DEPTH to return half-space seafloor depths</i> </p>
<p> Note: Because geographic or time constants may be present in a macro, it is required that the optional comment flag (:) must be followed by a space. As another example, we show a macro <code>GPSWEEK</code> which determines which GPS week a timestamp belongs to: </p>
<p> <code>GPSWEEK</code> = 1980-01-06T00:00:00 SUB 86400 DIV 7 DIV FLOOR : GPS week without rollover</p>
<h2>EXAMPLES</h2>
<p> To take the square root of the content of the second data column being piped through <code>gmtmath</code> by process1 and pipe it through a 3rd process, use </p>
<pre>
process1 | gmt math STDIN SQRT = | process3
</pre>
<p> To take log10 of the average of 2 data files, use </p>
<pre>
gmt math file1.d file2.d ADD 0.5 MUL LOG10 = file3.d
</pre>
<p> Given the file samples.d, which holds seafloor ages in m.y. and seafloor depth in m, use the relation depth(in m) = 2500 + 350 * sqrt (age) to print the depth anomalies: </p>
<pre>
gmt math samples.d T SQRT 350 MUL 2500 ADD SUB = | lpr
</pre>
<p> To take the average of columns 1 and 4-6 in the three data sets sizes.1, sizes.2, and sizes.3, use </p>
<pre>
gmt math -C1,4-6 sizes.1 sizes.2 ADD sizes.3 ADD 3 DIV = ave.d
</pre>
<p> To take the 1-column data set ages.d and calculate the modal value and assign it to a variable, try </p>
<pre>
gmt set mode_age = `gmt math -S -T ages.d MODE =`
</pre>
<p> To evaluate the dilog(x) function for coordinates given in the file t.d: </p>
<pre>
gmt math -Tt.d T DILOG = dilog.d
</pre>
<p> To demonstrate the use of stored variables, consider this sum of the first 3 cosine harmonics where we store and repeatedly recall the trigonometric argument (2*pi*T/360): </p>
<pre>
gmt math -T0/360/1 2 PI MUL 360 DIV T MUL STO@kT COS @kT 2 MUL COS ADD \
            @kT 3 MUL COS ADD = harmonics.d
</pre>
<p> To use gmtmath as a RPN Hewlett-Packard calculator on scalars (i.e., no input files) and calculate arbitrary expressions, use the <code>-Q</code> option. As an example, we will calculate the value of Kei (((1 + 1.75)/2.2) + cos (60)) and store the result in the shell variable z: </p>
<pre>
set z = `gmt math -Q 1 1.75 ADD 2.2 DIV 60 COSD ADD KEI =`
</pre>
<p> To use <code>gmtmath</code> as a general least squares equation solver, imagine that the current table is the augmented matrix [ A | b ] and you want the least squares solution x to the matrix equation A * x = b. The operator <code>LSQFIT</code> does this; it is your job to populate the matrix correctly first. The <code>-A</code> option will facilitate this. Suppose you have a 2-column file ty.d with <i>t</i> and <i>b(t)</i> and you would like to fit a the model y(t) = a + b*t + c*H(t-t0), where H is the Heaviside step function for a given t0 = 1.55. Then, you need a 4-column augmented table loaded with t in column 1 and your observed y(t) in column 3. The calculation becomes </p>
<pre>
gmt math -N4/1 -Aty.d -C0 1 ADD -C2 1.55 STEPT ADD -Ca LSQFIT = solution.d
</pre>
<p> Note we use the <code>-C</code> option to select which columns we are working on, then make active all the columns we need (here all of them, with <code>-Ca</code>) before calling <code>LSQFIT</code>. The second and fourth columns (col numbers 1 and 3) are preloaded with t and y(t), respectively, the other columns are zero. If you already have a pre-calculated table with the augmented matrix [ A | b ] in a file (say lsqsys.d), the least squares solution is simply </p>
<pre>
gmt math -T lsqsys.d LSQFIT = solution.d
</pre>
<p> Users must be aware that when <code>-C</code> controls which columns are to be active the control extends to placing columns from files as well. Contrast the different result obtained by these very similar commands: </p>
<pre>
echo 1 2 3 4 | gmt math STDIN -C3 1 ADD =
1    2    3    5
</pre>
<p> versus </p>
<pre>
echo 1 2 3 4 | gmt math -C3 STDIN 1 ADD =
0    0    0    5
</pre>
<h2>REFERENCES</h2>
<p> Abramowitz, M., and I. A. Stegun, 1964, <i>Handbook of Mathematical Functions</i>, Applied Mathematics Series, vol. 55, Dover, New York. </p>
<p> Holmes, S. A., and W. E. Featherstone, 2002, A unified approach to the Clenshaw summation and the recursive computation of very high degree and order normalized associated Legendre functions. <i>Journal of Geodesy</i>, 76, 279-299. </p>
<p> Press, W. H., S. A. Teukolsky, W. T. Vetterling, and B. P. Flannery, 1992, <i>Numerical Recipes</i>, 2nd edition, Cambridge Univ., New York. </p>
<p> Spanier, J., and K. B. Oldman, 1987, <i>An Atlas of Functions</i>, Hemisphere Publishing Corp.</p>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>grdmath</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
