---
title: "grdmath(1)"
name: "grdmath"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grdmath/"
description: "grdmath – Reverse Polish Notation (RPN) calculator for grids (element by element)"
---

<h2>NAME</h2>
<p> grdmath &#8211; Reverse Polish Notation (RPN) calculator for grids (element by element)</p>
<h2>SYNOPSIS</h2>
<p> <code>grdmath</code> [ <i>min_area</i>[/<i>min_level</i>/<i>max_level</i>][<code>+ag</code>|<code>i</code>|<code>s</code> |<code>S</code>][<code>+r</code>|<code>l</code>][<code>p</code><i>percent</i>] ] [ <i>resolution</i>[<code>+</code>] ] [ <i>increment</i> ] [ ] [ ] [ <i>region</i> ] [ [<i>level</i>] ] [ <code>-bi</code><i>&lt;binary&gt;</i> ] [ <code>-di</code><i>&lt;nodata&gt;</i> ] [ <code>-f</code><i>&lt;flags&gt;</i> ] [ <code>-h</code><i>&lt;headers&gt;</i> ] [ <code>-i</code><i>&lt;flags&gt;</i> ] [ <code>-n</code><i>&lt;flags&gt;</i> ] [ <code>-r</code> ] [ <code>-x</code>[[-]<i>n</i>] ] <i>operand</i> [ <i>operand</i> ] <code>OPERATOR</code> [ <i>operand</i> ] <code>OPERATOR</code> &#8230; <code>=</code> <i>outgrdfile</i> </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>grdmath</code> will perform operations like add, subtract, multiply, and divide on one or more grid files or constants using Reverse Polish Notation (RPN) syntax (e.g., Hewlett-Packard calculator-style). Arbitrarily complicated expressions may therefore be evaluated; the final result is written to an output grid file. Grid operations are element-by-element, not matrix manipulations. Some operators only require one operand (see below). If no grid files are used in the expression then options <code>-R</code>, <code>-I</code> must be set (and optionally <code>-r</code>). The expression <code>=</code> <i>outgrdfile</i> can occur as many times as the depth of the stack allows in order to save intermediate results. Complicated or frequently occurring expressions may be coded as a macro for future use or stored and recalled via named memory locations.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>operand</i></p>
<dd> If <i>operand</i> can be opened as a file it will be read as a grid file. If not a file, it is interpreted as a numerical constant or a special symbol (see below).</p>
<dt><i>outgrdfile</i></p>
<dd> The name of a 2-D grid file that will hold the final result. (See GRID FILE FORMATS below).</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-A</code><i>min_area</i>[/<i>min_level</i>/<i>max_level</i>][<code>+ag</code>|<code>i</code>|<code>s</code>|<code>S</code>][<code>+r</code>|<code>l</code>][<code>+p</code><i>percent</i>]</p>
<dd> Features with an area smaller than <i>min_area</i> in km^2 or of hierarchical level that is lower than <i>min_level</i> or higher than <i>max_level</i> will not be plotted [Default is 0/0/4 (all features)]. Level 2 (lakes) contains regular lakes and wide river bodies which we normally include as lakes; append <code>+r</code> to just get river-lakes or <code>+l</code> to just get regular lakes. By default (<code>+ai</code>) we select the ice shelf boundary as the coastline for Antarctica; append <code>+ag</code> to instead select the ice grounding line as coastline. For expert users who wish to print their own Antarctica coastline and islands via <i>psxy</i> you can use <code>+as</code> to skip all GSHHG features below 60S or <code>+aS</code> to instead skip all features north of 60S. Finally, append <code>+p</code><i>percent</i> to exclude polygons whose percentage area of the corresponding full-resolution feature is less than <i>percent</i>. See GSHHG INFORMATION below for more details. (<code>-A</code> is only relevant to the <code>LDISTG</code> operator)</p>
<dt><code>-D</code><i>resolution</i>[<code>+</code>]</p>
<dd> Selects the resolution of the data set to use with the operator LDISTG ((<code>f</code>)ull, (<code>h</code>)igh, (<code>i</code>)ntermediate, (<code>l</code>)ow, and (<code>c</code>)rude). The resolution drops off by 80% between data sets [Default is <code>l</code>]. Append <code>+</code> to automatically select a lower resolution should the one requested not be available [abort if not found].</p>
<dt><code>-I</code><i>xinc</i>[<i>unit</i>][<code>=</code>|<code>+</code>][/<i>yinc</i>[<i>unit</i>][<code>=</code>|<code>+</code>]]</p>
<dd> <i>x_inc</i> [and optionally <i>y_inc</i>] is the grid spacing. Optionally, append a suffix modifier. <code>Geographical (degrees) coordinates</code>: Append <code>m</code> to indicate arc minutes or <code>s</code> to indicate arc seconds. If one of the units <code>e</code>, <code>f</code>, <code>k</code>, <code>M</code>, <code>n</code> or <code>u</code> is appended instead, the increment is assumed to be given in meter, foot, km, Mile, nautical mile or US survey foot, respectively, and will be converted to the equivalent degrees longitude at the middle latitude of the region (the conversion depends on <i>PROJ_ELLIPSOID</i>). If /<i>y_inc</i> is given but set to 0 it will be reset equal to <i>x_inc</i>; otherwise it will be converted to degrees latitude. <code>All coordinates</code>: If <code>=</code> is appended then the corresponding max <i>x</i> (<i>east</i>) or <i>y</i> (<i>north</i>) may be slightly adjusted to fit exactly the given increment [by default the increment may be adjusted slightly to fit the given domain]. Finally, instead of giving an increment you may specify the <i>number of nodes</i> desired by appending <code>+</code> to the supplied integer argument; the increment is then recalculated from the number of nodes and the domain. The resulting increment value depends on whether you have selected a gridline-registered or pixel-registered grid; see <i>App-file-formats</i> for details. Note: if <code>-R</code><i>grdfile</i> is used then the grid spacing has already been initialized; use <code>-I</code> to override the values.</p>
<dt><code>-M</code></p>
<dd> By default any derivatives calculated are in z_units/ x(or y)_units. However, the user may choose this option to convert dx,dy in degrees of longitude,latitude into meters using a flat Earth approximation, so that gradients are in z_units/meter.</p>
<dt><code>-N</code></p>
<dd> Turn off strict domain match checking when multiple grids are manipulated [Default will insist that each grid domain is within 1e-4 * grid_spacing of the domain of the first grid listed].</p>
<dt><code>-R</code>[<i>unit</i>]<i>xmin</i>/<i>xmax</i>/<i>ymin</i>/<i>ymax</i>[<code>r</code>] <i>(more &#8230;)</i></p>
<dd> Specify the region of interest.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-bi</code>[<i>ncols</i>][<code>t</code>] <i>(more &#8230;)</i></p>
<dd> Select native binary input. The binary input option only applies to the data files needed by operators <code>LDIST</code>, <code>PDIST</code>, and <code>INSIDE</code>.</p>
<dt><code>-di</code><i>nodata</i> <i>(more &#8230;)</i></p>
<dd> Replace input columns that equal <i>nodata</i> with NaN.</p>
<dt><code>-f</code>[<code>i</code>|<code>o</code>]<i>colinfo</i> <i>(more &#8230;)</i></p>
<dd> Specify data types of input and/or output columns.</p>
<dt><code>-g</code>[<code>a</code>]<code>x</code>|<code>y</code>|<code>d</code>|<code>X</code>|<code>Y</code>|<code>D</code>|[<i>col</i>]<code>z</code>[+|-]<i>gap</i>[<code>u</code>] <i>(more &#8230;)</i></p>
<dd> Determine data gaps and line breaks.</p>
<dt><code>-h</code>[<code>i</code>|<code>o</code>][<i>n</i>][<code>+c</code>][<code>+d</code>][<code>+r</code><i>remark</i>][<code>+r</code><i>title</i>] <i>(more &#8230;)</i></p>
<dd> Skip or produce header record(s).</p>
<dt><code>-i</code><i>cols</i>[<code>l</code>][<code>s</code><i>scale</i>][<code>o</code><i>offset</i>][,<i>&#8230;</i>] <i>(more &#8230;)</i></p>
<dd> Select input columns (0 is first column).</p>
<dt><code>-n</code>[<code>b</code>|<code>c</code>|<code>l</code>|<code>n</code>][<code>+a</code>][<code>+b</code><i>BC</i>][<code>+c</code>][<code>+t</code><i>threshold</i>] <i>(more &#8230;)</i></p>
<dd> Select interpolation mode for grids.</p>
<dt><code>-r</code> <i>(more &#8230;)</i></p>
<dd> Set pixel node registration [gridline]. Only used with <code>-R</code> <code>-I</code>.</p>
<dt><code>-x</code>[[-]<i>n</i>] <i>(more &#8230;)</i></p>
<dd> Limit number of cores used in multi-threaded algorithms (OpenMP required).</p>
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
<p> Choose among the following 169 operators. &quot;args&quot; are the number of input and output arguments. <center></p>
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
<td> <code>ARC</code> </td>
<td> 2 1 </td>
<td> return arc(A,B) on [0 pi]
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
<td> <code>CAZ</code> </td>
<td> 2 1 </td>
<td> Cartesian azimuth from grid nodes to stack x,y (i.e., A, B)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>CBAZ</code> </td>
<td> 2 1 </td>
<td> Cartesian back-azimuth from grid nodes to stack x,y (i.e., A, B)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>CDIST</code> </td>
<td> 2 1 </td>
<td> Cartesian distance between grid nodes and stack x,y (i.e., A, B)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>CDIST2</code> </td>
<td> 2 1 </td>
<td> As CDIST but only to nodes that are != 0
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
<td> Chi-squared critical value for alpha = A and nu = B
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
<td> <code>CURV</code> </td>
<td> 1 1 </td>
<td> Curvature of A (Laplacian)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>D2DX2</code> </td>
<td> 1 1 </td>
<td> d^2(A)/dx^2 2nd derivative
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>D2DY2</code> </td>
<td> 1 1 </td>
<td> d^2(A)/dy^2 2nd derivative
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>D2DXY</code> </td>
<td> 1 1 </td>
<td> d^2(A)/dxdy 2nd derivative
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
<td> <code>DDX</code> </td>
<td> 1 1 </td>
<td> d(A)/dx Central 1st derivative
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>DDY</code> </td>
<td> 1 1 </td>
<td> d(A)/dy Central 1st derivative
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>DEG2KM</code> </td>
<td> 1 1 </td>
<td> Converts Spherical Degrees to Kilometers
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
<td> <code>EXTREMA</code> </td>
<td> 1 1 </td>
<td> Local Extrema: +2/-2 is max/min, +1/-1 is saddle with max/min in x, 0 elsewhere
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
<td> <code>FLIPLR</code> </td>
<td> 1 1 </td>
<td> Reverse order of values in each row
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
<td> Reverse order of values in each column
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
<td> <code>INSIDE</code> </td>
<td> 1 1 </td>
<td> 1 when inside or on polygon(s) in A, else 0
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
<td> <code>KM2DEG</code> </td>
<td> 1 1 </td>
<td> Converts Kilometers to Spherical Degrees
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
<td> <code>LDIST</code> </td>
<td> 1 1 </td>
<td> Compute minimum distance (in km if -fg) from lines in multi-segment ASCII file A
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>LDIST2</code> </td>
<td> 2 1 </td>
<td> As LDIST, from lines in ASCII file B but only to nodes where A != 0
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>LDISTG</code> </td>
<td> 0 1 </td>
<td> As LDIST, but operates on the GSHHG dataset (see -A, -D for options).
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
<td> <code>PDIST</code> </td>
<td> 1 1 </td>
<td> Compute minimum distance (in km if -fg) from points in ASCII file A
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>PDIST2</code> </td>
<td> 2 1 </td>
<td> As PDIST, from points in ASCII file B but only to nodes where A != 0
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
<td> <code>POINT</code> </td>
<td> 1 2 </td>
<td> Compute mean x and y from ASCII file A and place them on the stack
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
<td> <code>ROTX</code> </td>
<td> 2 1 </td>
<td> Rotate A by the (constant) shift B in x-direction
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>ROTY</code> </td>
<td> 2 1 </td>
<td> Rotate A by the (constant) shift B in y-direction
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>SDIST</code> </td>
<td> 2 1 </td>
<td> Spherical (Great circle|geodesic) distance (in km) between nodes and stack (A, B)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>SDIST2</code> </td>
<td> 2 1 </td>
<td> As SDIST but only to nodes that are != 0
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>SAZ</code> </td>
<td> 2 1 </td>
<td> Spherical azimuth from grid nodes to stack lon, lat (i.e., A, B)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>SBAZ</code> </td>
<td> 2 1 </td>
<td> Spherical back-azimuth from grid nodes to stack lon, lat (i.e., A, B)
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
<td> Heaviside step function: H(A)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>STEPX</code> </td>
<td> 1 1 </td>
<td> Heaviside step function in x: H(x-A)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>STEPY</code> </td>
<td> 1 1 </td>
<td> Heaviside step function in y: H(y-A)
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
<td> Sum of all values in A
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
<td> 2 1 </td>
<td> Unit weights cosine-tapered to zero within A and B of x and y grid margins
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
<td> <code>TN</code> </td>
<td> 2 1 </td>
<td> Chebyshev polynomial Tn(-1&lt;t&lt;+1,n), with t = A, and n = B
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
<td> <code>WRAP</code> </td>
<td> 1 1 </td>
<td> wrap A in radians onto [-pi,pi]
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
<td> 0 if A == NaN and B == NaN, NaN if B == NaN, else A
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
<td> <code>YLM</code> </td>
<td> 2 2 </td>
<td> Re and Im orthonormalized spherical harmonics degree A order B
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>YLMg</code> </td>
<td> 2 2 </td>
<td> Cos and Sin normalized spherical harmonics degree A order B (geophysical convention)
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
<td> 1.192092896e-07 (single precision epsilon
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>XMIN</code> </td>
<td> Minimum x value
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>XMAX</code> </td>
<td> Maximum x value
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>XRANGE</code> </td>
<td> Range of x values
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>XINC</code> </td>
<td> x increment
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>NX</code> </td>
<td> The number of x nodes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>YMIN</code> </td>
<td> Minimum y value
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>YMAX</code> </td>
<td> Maximum y value
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>YRANGE</code> </td>
<td> Range of y values
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>YINC</code> </td>
<td> y increment
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>NY</code> </td>
<td> The number of y nodes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>X</code> </td>
<td> Grid with x-coordinates
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>Y</code> </td>
<td> Grid with y-coordinates
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>XNORM</code> </td>
<td> Grid with normalized [-1 to +1] x-coordinates
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>YNORM</code> </td>
<td> Grid with normalized [-1 to +1] y-coordinates
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>XCOL</code> </td>
<td> Grid with column numbers 0, 1, &#8230;, NX-1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>YROW</code> </td>
<td> Grid with row numbers 0, 1, &#8230;, NY-1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center></p>
<h2>NOTES ON OPERATORS</h2>
<dl>
<dt>1.</p>
<dd> The operator <code>SDIST</code> calculates spherical distances in km between the (lon, lat) point on the stack and all node positions in the grid. The grid domain and the (lon, lat) point are expected to be in degrees. Similarly, the <code>SAZ</code> and <code>SBAZ</code> operators calculate spherical azimuth and back-azimuths in degrees, respectively. The operators <code>LDIST</code> and <code>PDIST</code> compute spherical distances in km if <code>-fg</code> is set or implied, else they return Cartesian distances. Note: If the current <i>PROJ_ELLIPSOID</i> is ellipsoidal then geodesics are used in calculations of distances, which can be slow. You can trade speed with accuracy by changing the algorithm used to compute the geodesic (see <i>PROJ_GEODESIC</i>). </p>
<p> The operator <code>LDISTG</code> is a version of <code>LDIST</code> that operates on the GSHHG data. Instead of reading an ASCII file, it directly accesses one of the GSHHG data sets as determined by the <code>-D</code> and <code>-A</code> options.</p>
<dt>2.</p>
<dd> The operator <code>POINT</code> reads a ASCII table, computes the mean x and mean y values and places these on the stack. If geographic data then we use the mean 3-D vector to determine the mean location.</p>
<dt>3.</p>
<dd> The operator <code>PLM</code> calculates the associated Legendre polynomial of degree L and order M (0 &lt;= M &lt;= L), and its argument is the sine of the latitude. <code>PLM</code> is not normalized and includes the Condon-Shortley phase (-1)^M. <code>PLMg</code> is normalized in the way that is most commonly used in geophysics. The C-S phase can be added by using -M as argument. <code>PLM</code> will overflow at higher degrees, whereas <code>PLMg</code> is stable until ultra high degrees (at least 3000).</p>
<dt>4.</p>
<dd> The operators <code>YLM</code> and <code>YLMg</code> calculate normalized spherical harmonics for degree L and order M (0 &lt;= M &lt;= L) for all positions in the grid, which is assumed to be in degrees. <code>YLM</code> and <code>YLMg</code> return two grids, the real (cosine) and imaginary (sine) component of the complex spherical harmonic. Use the <code>POP</code> operator (and <code>EXCH</code>) to get rid of one of them, or save both by giving two consecutive = file.nc calls. </p>
<p> The orthonormalized complex harmonics <code>YLM</code> are most commonly used in physics and seismology. The square of <code>YLM</code> integrates to 1 over a sphere. In geophysics, <code>YLMg</code> is normalized to produce unit power when averaging the cosine and sine terms (separately!) over a sphere (i.e., their squares each integrate to 4 pi). The Condon-Shortley phase (-1)^M is not included in <code>YLM</code> or <code>YLMg</code>, but it can be added by using -M as argument.</p>
<dt>5.</p>
<dd> All the derivatives are based on central finite differences, with natural boundary conditions.</p>
<dt>6.</p>
<dd> Files that have the same names as some operators, e.g., <code>ADD</code>, <code>SIGN</code>, <code>=</code>, etc. should be identified by prepending the current directory (i.e., ./LOG).</p>
<dt>7.</p>
<dd> Piping of files is not allowed.</p>
<dt>8.</p>
<dd> The stack depth limit is hard-wired to 100.</p>
<dt>9.</p>
<dd> All functions expecting a positive radius (e.g., <code>LOG</code>, <code>KEI</code>, etc.) are passed the absolute value of their argument. (9) The bitwise operators (<code>BITAND</code>, <code>BITLEFT</code>, <code>BITNOT</code>, <code>BITOR</code>, <code>BITRIGHT</code>, <code>BITTEST</code>, and <code>BITXOR</code>) convert a grid&#8217;s single precision values to unsigned 32-bit ints to perform the bitwise operations. Consequently, the largest whole integer value that can be stored in a float grid is 2^24 or 16,777,216. Any higher result will be masked to fit in the lower 24 bits. Thus, bit operations are effectively limited to 24 bit. All bitwise operators return NaN if given NaN arguments or bit-settings &lt;= 0.</p>
<dt>10.</p>
<dd> When OpenMP support is compiled in, a few operators will take advantage of the ability to spread the load onto several cores. At present, the list of such operators is: <code>LDIST</code>.</dl>
<h2>GRID VALUES PRECISION</h2>
<p> Regardless of the precision of the input data, GMT programs that create grid files will internally hold the grids in 4-byte floating point arrays. This is done to conserve memory and furthermore most if not all real data can be stored using 4-byte floating point values. Data with higher precision (i.e., double precision values) will lose that precision once GMT operates on the grid or writes out new grids. To limit loss of precision when processing data you should always consider normalizing the data prior to processing.</p>
<h2>GRID FILE FORMATS</h2>
<p> By default GMT writes out grid as single precision floats in a COARDS-complaint netCDF file format. However, GMT is able to produce grid files in many other commonly used grid file formats and also facilitates so called &quot;packing&quot; of grids, writing out floating point data as 1- or 2-byte integers. To specify the precision, scale and offset, the user should add the suffix <code>=</code><i>id</i>[<code>/</code><i>scale</i><code>/</code><i>offset</i>[<code>/</code><i>nan</i>]], where <i>id</i> is a two-letter identifier of the grid type and precision, and <i>scale</i> and <i>offset</i> are optional scale factor and offset to be applied to all grid values, and <i>nan</i> is the value used to indicate missing data. In case the two characters <i>id</i> is not provided, as in <code>=/</code><i>scale</i> than a <i>id</i><code>=</code><i>nf</i> is assumed. When reading grids, the format is generally automatically recognized. If not, the same suffix can be added to input grid file names. See <code>grdconvert</code> and Section <i>grid-file-format</i> of the GMT Technical Reference and Cookbook for more information. </p>
<p> When reading a netCDF file that contains multiple grids, GMT will read, by default, the first 2-dimensional grid that can find in that file. To coax GMT into reading another multi-dimensional variable in the grid file, append <code>?</code><i>varname</i> to the file name, where <i>varname</i> is the name of the variable. Note that you may need to escape the special meaning of <code>?</code> in your shell program by putting a backslash in front of it, or by placing the filename and suffix between quotes or double quotes. The <code>?</code><i>varname</i> suffix can also be used for output grids to specify a variable name different from the default: &quot;z&quot;. See <code>grdconvert</code> and Sections <i>modifiers-for-CF</i> and <i>grid-file-format</i> of the GMT Technical Reference and Cookbook for more information, particularly on how to read splices of 3-, 4-, or 5-dimensional grids.</p>
<h2>GEOGRAPHICAL AND TIME COORDINATES</h2>
<p> When the output grid type is netCDF, the coordinates will be labeled &quot;longitude&quot;, &quot;latitude&quot;, or &quot;time&quot; based on the attributes of the input data or grid (if any) or on the <code>-f</code> or <code>-R</code> options. For example, both <code>-f0x</code> <code>-f1t</code> and <code>-R</code>90w/90e/0t/3t will result in a longitude/time grid. When the x, y, or z coordinate is time, it will be stored in the grid as relative time since epoch as specified by <i>TIME_UNIT</i> and <i>TIME_EPOCH</i> in the <code>gmt.conf</code> file or on the command line. In addition, the <code>unit</code> attribute of the time variable will indicate both this unit and epoch.</p>
<h2>STORE, RECALL AND CLEAR</h2>
<p> You may store intermediate calculations to a named variable that you may recall and place on the stack at a later time. This is useful if you need access to a computed quantity many times in your expression as it will shorten the overall expression and improve readability. To save a result you use the special operator <code>STO</code>@<i>label</i>, where <i>label</i> is the name you choose to give the quantity. To recall the stored result to the stack at a later time, use [<code>RCL</code>]@<i>label</i>, i.e., <code>RCL</code> is optional. To clear memory you may use <code>CLR</code>@<i>label</i>. Note that <code>STO</code> and <code>CLR</code> leave the stack unchanged.</p>
<h2>GSHHS INFORMATION</h2>
<p> The coastline database is GSHHG (formerly GSHHS) which is compiled from three sources: World Vector Shorelines (WVS), CIA World Data Bank II (WDBII), and Atlas of the Cryosphere (AC, for Antarctica only). Apart from Antarctica, all level-1 polygons (ocean-land boundary) are derived from the more accurate WVS while all higher level polygons (level 2-4, representing land/lake, lake/island-in-lake, and island-in-lake/lake-in-island-in-lake boundaries) are taken from WDBII. The Antarctica coastlines come in two flavors: ice-front or grounding line, selectable via the <code>-A</code> option. Much processing has taken place to convert WVS, WDBII, and AC data into usable form for GMT: assembling closed polygons from line segments, checking for duplicates, and correcting for crossings between polygons. The area of each polygon has been determined so that the user may choose not to draw features smaller than a minimum area (see <code>-A</code>); one may also limit the highest hierarchical level of polygons to be included (4 is the maximum). The 4 lower-resolution databases were derived from the full resolution database using the Douglas-Peucker line-simplification algorithm. The classification of rivers and borders follow that of the WDBII. See the GMT Cookbook and Technical Reference Appendix K for further details.</p>
<h2>MACROS</h2>
<p> Users may save their favorite operator combinations as macros via the file <i>grdmath.macros</i> in their current or user directory. The file may contain any number of macros (one per record); comment lines starting with # are skipped. The format for the macros is <code>name</code> = <code>arg1 arg2 &#8230; arg2</code> : <i>comment</i> where <code>name</code> is how the macro will be used. When this operator appears on the command line we simply replace it with the listed argument list. No macro may call another macro. As an example, the following macro expects three arguments (radius x0 y0) and sets the modes that are inside the given circle to 1 and those outside to 0: </p>
<p> INCIRCLE = CDIST EXCH DIV 1 LE : usage: r x y INCIRCLE to return 1 inside circle </p>
<p> Note: Because geographic or time constants may be present in a macro, it is required that the optional comment flag (:) must be followed by a space.</p>
<h2>EXAMPLES</h2>
<p> To compute all distances to north pole: </p>
<pre>
gmt grdmath -Rg -I1 0 90 SDIST = dist_to_NP.nc
</pre>
<p> To take log10 of the average of 2 files, use </p>
<pre>
gmt grdmath file1.nc file2.nc ADD 0.5 MUL LOG10 = file3.nc
</pre>
<p> Given the file ages.nc, which holds seafloor ages in m.y., use the relation depth(in m) = 2500 + 350 * sqrt (age) to estimate normal seafloor depths: </p>
<pre>
gmt grdmath ages.nc SQRT 350 MUL 2500 ADD = depths.nc
</pre>
<p> To find the angle a (in degrees) of the largest principal stress from the stress tensor given by the three files s_xx.nc s_yy.nc, and s_xy.nc from the relation tan (2*a) = 2 * s_xy / (s_xx &#8211; s_yy), use </p>
<pre>
gmt grdmath 2 s_xy.nc MUL s_xx.nc s_yy.nc SUB DIV ATAN 2 DIV = direction.nc
</pre>
<p> To calculate the fully normalized spherical harmonic of degree 8 and order 4 on a 1 by 1 degree world map, using the real amplitude 0.4 and the imaginary amplitude 1.1: </p>
<pre>
gmt grdmath -R0/360/-90/90 -I1 8 4 YML 1.1 MUL EXCH 0.4 MUL ADD = harm.nc
</pre>
<p> To extract the locations of local maxima that exceed 100 mGal in the file faa.nc: </p>
<pre>
gmt grdmath faa.nc DUP EXTREMA 2 EQ MUL DUP 100 GT MUL 0 NAN = z.nc
gmt grd2xyz z.nc -s &gt; max.xyz
</pre>
<p> To demonstrate the use of named variables, consider this radial wave where we store and recall the normalized radial arguments in radians: </p>
<pre>
gmt grdmath -R0/10/0/10 -I0.25 5 5 CDIST 2 MUL PI MUL 5 DIV STO@r COS @r SIN MUL = wave.nc
</pre>
<h2>REFERENCES</h2>
<p> Abramowitz, M., and I. A. Stegun, 1964, <i>Handbook of Mathematical Functions</i>, Applied Mathematics Series, vol. 55, Dover, New York. </p>
<p> Holmes, S. A., and W. E. Featherstone, 2002, A unified approach to the Clenshaw summation and the recursive computation of very high degree and order normalised associated Legendre functions. <i>Journal of Geodesy</i>, 76, 279-299. </p>
<p> Press, W. H., S. A. Teukolsky, W. T. Vetterling, and B. P. Flannery, 1992, <i>Numerical Recipes</i>, 2nd edition, Cambridge Univ., New York. </p>
<p> Spanier, J., and K. B. Oldman, 1987, <i>An Atlas of Functions</i>, Hemisphere Publishing Corp.</p>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>gmtmath</code>, <code>grd2xyz</code>, <code>grdedit</code>, <code>grdinfo</code>, <code>xyz2grd</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
