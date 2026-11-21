---
title: "lp_solve(1)"
name: "lp_solve"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lp_solve/"
description: "lp_solve – a mixed integer linear programming (MILP) solver"
---

<h2>SYNOPSIS</h2>
<p> <code>lp_solve</code> [<i>options</i>] [<i>input file</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>lp_solve</code> solves mixed integer linear programming problems. The program accepts models of problems in various different formats (including custom formats through XLIs) and attempts to solve them. There are a large number of different options which can be used to alter the solving process to improve performance or get more accurate results. </p>
<h3>lp file format</h3>
<p> The lp file format is a simple, human readable file format for linear programming models. It is the default format used by <code>lp_solve</code>. </p>
<p> The format consists of series of statements, each ending in a semicolon. The first statement is always the objective function, followed by any number of constraints, followed by any number of declarations. </p>
<p> The objective function consists of an expression to be optimized, optionally prefixed by <code>max:</code> or <code>min:</code> to specify which direction to optimize. The default is to maximize. </p>
<p> Each constraint consists of a relational expression, optionally prefixed by a name followed by a colon. The expression must contain at least one relational operator (<code>&lt;</code>,<code> &lt;=</code>,<code> =,</code> =&gt;,<code> &gt;</code>). You can specify ranges two operators at once (e.g. 2 &lt; x &lt; 4) instead of two separate constraints. </p>
<p> Declarations can be one of:</p>
<dl>
<dt><code>int </code><i>var1 </i>[<code>, </code><i>var2</i>]&#8230; ;</dt>
<dd> Marks the variables as integers.</dd>
<dt><code>bin </code><i>var1 </i>[<code>, </code><i>var2</i>]&#8230; ;</dt>
<dd> Marks the variables as binary (can only take 0 or 1).</dd>
<dt><code>sec </code><i>var1 </i>[<code>, </code><i>var2</i>]&#8230; ;</dt>
<dd> Marks the variables as semi-continuous. These variables can always take the value 0 even if it is outside the variable&#8217;s range.</dd>
<dt><code>free </code><i>var1 </i>[<code>, </code><i>var2</i>]&#8230; ;</dt>
<dd> Marks the variables as free. These variables have no lower bound, unlike other variables which have a default lower bound of 0.</dd>
<dt><code>sos </code>[<i>name</i><code>:</code>] <i>var1 </i>[<code>, </code><i>var2</i>]&#8230; [&lt; <i>sostype</i>];</dt>
<dd> Marks the variables as part of a special ordered set (SOS). Out of the variables listed, only one can be non-zero at once. If <i>sostype</i> is specified, then up to that number of variables can be non-zero as long as they are all adjacent to each other (e.g. for an <i>sostype</i> of 2, <i>var1</i> and <i>var2</i> could be non-zero, but not <i>var1</i> and <i>var3</i>). </dd>
<p> Both C style comments (<code>/* </code>comment here<code> */</code>) and C++ style comments (<code>// </code>comment until end of line) can be used anywhere in the file.</dl>
<h2>OPTIONS</h2>
<h3>General options</h3>
<dl>
<dt><code>-wafter</code></dt>
<dd> Writes the model after solving it (normally any model conversions are processed before solving). This is useful if presolving is used to simplify the model.</dd>
<dt><code>-parse_only</code></dt>
<dd> Parse the input model, but stop before solving it. This can be used to convert models between formats without solving them.</dd>
<dt><code>-timeout</code><i> sec</i></dt>
<dd> Timeout if no solution has be found after <i>sec</i> seconds.</dd>
<dt><code>-nonames</code></dt>
<dd> Ignore variable and constraint names in the input model (this is the same as combining both <code>-norownames</code> <code>-nocolnames</code>).</dd>
<dt><code>-norownames</code></dt>
<dd> Ignore constraint names in the input model.</dd>
<dt><code>-nocolnames</code></dt>
<dd> Ignore variable names in the input model.</dd>
<dt><code>-min</code></dt>
<dd> Minimizes the LP problem, overriding the setting in the input model.</dd>
<dt><code>-max</code></dt>
<dd> Maximizes the LP problem, overriding the setting in the input model.</dd></dl>
<h3>Built-in model languages</h3>
<dl>
<dt><code>-lp</code></dt>
<dd> Read the model from a file in LP format. This the the default.</dd>
<dt><code>-mps</code></dt>
<dd> Read the model from a file in &#8216;fixed width&#8217; MPS format.</dd>
<dt><code>-fmps</code></dt>
<dd> Read the model from a file in &#8216;free&#8217; MPS format. This is the same as <code>-mps</code> except that fields are separated by a number of blanks instead of starting at fixed columns.</dd>
<dt><code>-wlp</code><i> filename</i></dt>
<dd> Converts the input model to LP format and writes it to the a file.</dd>
<dt><code>-wmps</code><i> filename</i></dt>
<dd> Converts the input model to &#8216;fixed width&#8217; MPS format and writes it to a file.</dd>
<dt><code>-wfmps</code><i> filename</i></dt>
<dd> Converts the input model to &#8216;free&#8217; MPS format and writes it to a file.</dd></dl>
<h3>External language interface (XLI)</h3>
<dl>
<dt><code>-rxli</code><i> xliname </i><i>filename</i></dt>
<dd> Read the model using an external language interface (XLI). <i>xliname</i> specifies the path to the shared library containing the XLI, and is searched for according to the normal library search rules in <code><a href="/docs/linux/man/8-ld-so/">ld.so</a></code>(8) with the addition that the library filename is prefixed with <i>lib</i> and suffixed with <i>.so</i> if necessary.</dd>
<dt><code>-rxlidata</code><i> datafilename</i></dt>
<dd> Provides a file containing extra data used by the reading XLI library.</dd>
<dt><code>-rxliopt</code><i> options</i></dt>
<dd> Extra options to pass to the reading XLI library.</dd>
<dt><code>-wxli</code><i> xliname </i><i>filename</i></dt>
<dd> Converts the input model to the format used by an XLI and writes it to a file. The format of <i>xliname</i> is described in <code>-rxli</code> above.</dd>
<dt><code>-wxliopt</code><i> options</i></dt>
<dd> Extra options to pass to the writing XLI library.</dd>
<dt><code>-wxlisol</code><i> xliname </i><i>filename</i></dt>
<dd> Writes the model&#8217;s solution to a file using an XLI library. The format of <i>xliname</i> is described in <code>-rxli</code> above.</dd>
<dt><code>-wxlisolopt</code><i> options</i></dt>
<dd> Extra options to pass to the solution writing XLI library.</dd></dl>
<h3>Printing, verbosity and debugging</h3>
<dl>
<dt><code>-h</code></dt>
<dd> Print a usage message and exit.</dd>
<dt><code>-S</code><i>level</i></dt>
<dd> Solution detail. Each <i>level</i> builds on top of the previous one and adds more detail to the solution. </dd>
<dl>
<dl>
<dt><code>0</code></dt>
<dd> print nothing</dd>
<dt><code>1</code></dt>
<dd> objective value only</dd>
<dt><code>2</code></dt>
<dd> variables (default level)</dd>
<dt><code>3</code></dt>
<dd> constraints</dd>
<dt><code>4</code></dt>
<dd> duals</dd>
<dt><code>5</code></dt>
<dd> lp model</dd>
<dt><code>6</code></dt>
<dd> scales</dd>
<dt><code>7</code></dt>
<dd> lp tableau</dd></dl>
</dl>
<dt><code>-time</code></dt>
<dd> Print CPU time to parse input and to calculate solution.</dd>
<dt><code>-v</code>[<i>level</i>]</dt>
<dd> Verbosity level. Controls the level of messages printed about the operation of the program. </dd>
<dl>
<dl>
<dt><code>0</code></dt>
<dd> neutral</dd>
<dt><code>1</code></dt>
<dd> critical</dd>
<dt><code>2</code></dt>
<dd> severe</dd>
<dt><code>3</code></dt>
<dd> important (default when <code>-v</code> is provided with no <i>level</i>)</dd>
<dt><code>4</code></dt>
<dd> normal (default when no <code>-v</code> option is given)</dd>
<dt><code>5</code></dt>
<dd> detailed</dd>
<dt><code>6</code></dt>
<dd> full</dd></dl>
</dl>
<dt><code>-t</code></dt>
<dd> Trace pivot selection.</dd>
<dt><code>-d</code></dt>
<dd> Debug mode. All intermediate results and branch-and-bound decisions are printed.</dd>
<dt><code>-R</code></dt>
<dd> Report information while solving the model.</dd>
<dt><code>-Db</code><i> filename</i></dt>
<dd> Create a dump of internal model variables before solving the model to given file.</dd>
<dt><code>-Da</code><i> filename</i></dt>
<dd> Create a dump of internal model variables after solving the model, to given file.</dd>
<dt><code>-i</code>[<code>a</code>]</dt>
<dd> Print all intermediate valid solutions. If <code>a</code> is used, prints only non-zero values. Can give useful solutions even if the total run time is too long. </dd>
</dl>
<h3>Parameter files</h3>
<dl>
<dt><code>-rpar</code><i> filename</i></dt>
<dd> Reads a list of parameters from a file. The parameters file can specify the same options as you can by passing arguments to <code>lp_solve</code> but can be more convenient if you need to change lots of settings. The format of the parameters file is in the INI format often used by Windows applications. All parameters are read from key-value pairs in a single section. The default section is <code>[Default]</code>.</dd>
<dt><code>-rparopt</code> &#8216;<code>-h </code><i>header</i>&#8216;</dt>
<dd> Sets options for reading the parameters file. Currently the only option is <code>-h</code> which changes the section within the file to read the parameters from.</dd>
<dt><code>-wpar</code><i> filename</i></dt>
<dd> Writes a parameters file based on the arguments given to <code>lp_solve</code>.</dd>
<dt><code>-wparopt</code> &#8216;<code>-h </code><i>header</i>&#8216;</dt>
<dd> Sets options for writing the parameter file. Currently the only option is <code>-h</code> which changes the section within the file to write the parameters to.</dd></dl>
<h3>Basis files</h3>
<dl>
<dt><code>-rbas</code><i> filename</i></dt>
<dd> Reads a basis file which is used as the starting point for solving the LP model. Basis files must be in MPS basis format.</dd>
<dt><code>-gbas</code><i> filename</i></dt>
<dd> Computes a basis from a list of initial guesses for each variable. Each line of the given file is in the format: <i>variable</i><code>:</code><i>value</i> where <i>value</i> is the initial guess for <i>variable</i>.</dd>
<dt><code>-wbas</code><i> filename</i></dt>
<dd> After solving the LP model, writes a basis file in MPS format. This file can be read back using <code>-rbas</code>. </dd>
<dl>
<dt>
</dt><dd> Available options:</dd>
<dl>
<dt><code>0</code></dt>
<dd> no crash basis (default).</dd>
<dt><code>1</code></dt>
<dd> most feasible basis.</dd>
<dt><code>2</code></dt>
<dd> least degenerate basis.</dd></dl>
</dl>
</dl>
<h3>Integer and branch and bound options</h3>
<dl>
<dt><code>-noint</code></dt>
<dd> Ignore integer restrictions on variables.</dd>
<dt><code>-f</code></dt>
<dd> Stops the branch and bound algorithm immediately after finding its first solution.</dd>
<dt><code>-o</code><i> bound</i></dt>
<dd> Stops the branch and bound algorithm immediately after finding a solution whose objective function has a value greater than this bound.</dd>
<dt><code>-b</code><i> bound</i></dt>
<dd> Sets a lower bound for the objective function. The branch and bound algorithm will immediately reject all solutions lower than this value.</dd>
<dt><code>-depth</code><i> limit</i></dt>
<dd> Sets the depth limit for the branch and bound algorithm. A value of 0 disables depth limiting. A negative value sets a relative depth limit based on the number of variables in the input model. The default limit is -50.</dd>
<dt><code>-e</code><i> tolerance</i></dt>
<dd> Sets the tolerance which is used to determine whether a floating point number is an integer. A number has to be within this value of an integer to be considered one. The default value is 1e-7.</dd>
<dt><code>-g </code><i>tolerance</i>, <code>-ga </code><i>tolerance</i></dt>
<dd> Sets the absolute MIP gap used by the branch and bound algorithm. This tolerance is the difference between the best-found solution yet and the current solution. If the difference is smaller than this tolerance then the solution (and all the sub-solutions) is rejected. This can result in faster solving times, but results in a solution which is not the perfect solution. The default value is 1e-11.</dd>
<dt><code>-gr</code><i> tolerance</i></dt>
<dd> Sets the relative MIP gap used by the branch and bound algorithm. This is similar to the absolute tolerance except that the difference is scaled by the best found solution before being compared to this tolerance. The default value is 1e-11.</dd>
<dt><code>-c</code>, <code>-cc</code></dt>
<dd> During branch and bound, take the ceiling branch first.</dd>
<dt><code>-cf</code></dt>
<dd> During branch and bound, take the floor branch first.</dd>
<dt><code>-ca</code></dt>
<dd> During branch and bound, allow the algorithm to decide which branch to take. This is the default.</dd>
<dt><code>-n</code><i> solution</i></dt>
<dd> If the branch and bound algorithm produces multiple solutions with the same objective function value, prints the nth solution. Solution numbers start at 1.</dd>
<dt><code>-B</code><i>rule</i></dt>
<dd> Sets a branch and bound rule to use. The default rules are: <code>-B5 -Bg -Bd -Bc</code> </dd>
<dl>
<dt>
</dt><dd> These rules are mutually exclusive:</dd>
<dl>
<dt><code>0</code></dt>
<dd> select lowest indexed non-integer column.</dd>
<dt><code>1</code></dt>
<dd> selection based on distance from the current bounds.</dd>
<dt><code>2</code></dt>
<dd> selection based on the largest current bound.</dd>
<dt><code>3</code></dt>
<dd> selection based on largest fractional value.</dd>
<dt><code>4</code></dt>
<dd> simple, unweighted pseudo-cost of a variable.</dd>
<dt><code>5</code></dt>
<dd> extended pseudo-costing strategy based on minimizing the number of integer infeasibilities.</dd>
<dt><code>6</code></dt>
<dd> extended pseudo-costing strategy based on maximizing the normal pseudo-cost divided by the number of infeasibilities.</dd></dl>
<p> The above rules can be combined with any of the following:</p>
<dl>
<dt><code>w</code></dt>
<dd> WeightReverse &#8211; select by criterion minimum (worst), rather than criterion maximum (best).</dd>
<dt><code>b</code></dt>
<dd> BranchReverse &#8211; when <code>-ca</code> is selected, choose the opposite direction.</dd>
<dt><code>g</code></dt>
<dd> Greedy</dd>
<dt><code>p</code></dt>
<dd> PseudoCost &#8211; toggles between weighting based on pseudocost or objective function value.</dd>
<dt><code>f</code></dt>
<dd> DepthFirst &#8211; select the node that has already been selected before the most number of times.</dd>
<dt><code>r</code></dt>
<dd> Randomize &#8211; ddds a randomization factor to the score for any node candidate.</dd>
<dt><code>G</code></dt>
<dd> GubMode</dd>
<dt><code>d</code></dt>
<dd> Dynamic &#8211; when <code>-Bf</code> is selected, switch off this mode when a first solution is found.</dd>
<dt><code>s</code></dt>
<dd> RestartMode &#8211; enables regular restarts of pseudocost value calculations.</dd>
<dt><code>B</code></dt>
<dd> BreadthFirst &#8211; select the node that has been selected before the fewest number of times or not at all.</dd>
<dt><code>o</code></dt>
<dd> AutoOrder &#8211; order variables to improve branch-and-bound performance.</dd>
<dt><code>c</code></dt>
<dd> ReducedCostFixing &#8211; do bound tightening during B&amp;B based of reduced cost info.</dd>
<dt><code>i</code></dt>
<dd> StringInit &#8211; initialize pseudo-costs by strong branching.</dd></dl>
</dl>
</dl>
<h3>Simplex algorithm options</h3>
<dl>
<dt><code>-prim</code>, <code>-simplexpp</code></dt>
<dd> Prefer the primal simplex method for both phase 1 and phase 2.</dd>
<dt><code>-dual</code>, <code>-simplexdd</code></dt>
<dd> Prefer the dual simplex method for both phase 1 and phase 2.</dd>
<dt><code>-simplexdp</code></dt>
<dd> Prefer the dual simplex method for phase 1 and primal method for phase 2. This is the default.</dd>
<dt><code>-simplexpd</code></dt>
<dd> Prefer the primal simplex method for phase 1 and dual method for phase 2.</dd>
<dt><code>-bfp</code><i> filename</i></dt>
<dd> Sets the basis factorization package to use. <i>filename</i> refers to a shared library loaded in the same way <code>-rxli</code> loads libraries.</dd>
<dt><code>-o</code><i>value</i></dt>
<dd> Sets whether the objective function is stored in the top row of the constraint matrix or in separate storage. <code>-o0</code> places the matrix in separate storage, and <code>-o1</code> (the default) places it in the constraint matrix.</dd>
<dt><code>-C</code><i>mode</i></dt>
<dd> Sets the basis crash mode. When base crash is enabled, a heuristic &#8216;crash procedure&#8217; is executed before the first simplex iteration to quickly choose a basis matrix that has fewer artificial variables. This procedure tends to reduce the number of iterations to optimality since a number of iterations are skipped.</dd>
<dt><code>-r</code><i> value</i></dt>
<dd> Sets the maximum number of pivots between a re-inversion of the matrix. For stability reasons, lp_solve re-inverts the matrix on regular times. The default is 250 for the LUSOL bfp and 42 for the other BFPs.</dd>
<dt><code>-trej</code><i> value</i></dt>
<dd> Sets the value that is used as a tolerance pivot element to determine whether a value should be considered as 0. The default is 2e-7.</dd>
<dt><code>-epsd</code><i> value</i></dt>
<dd> Sets the value that is used as a tolerance for reduced costs to determine whether a value should be considered as 0. The default is 1e-9.</dd>
<dt><code>-epsb</code><i> value</i></dt>
<dd> Sets the value that is used as a tolerance for the Right Hand Side (RHS) to determine whether a value should be considered as 0. The default is 1e-10.</dd>
<dt><code>-epsel</code><i> value</i></dt>
<dd> Sets the value that is used as a tolerance for rounding values to zero. The default is 1e-12.</dd>
<dt><code>-epsp</code><i> value</i></dt>
<dd> Sets the value that is used as perturbation scalar for degenerative problems. The default is 1e-5.</dd>
<dt><code>-improve</code><i>level</i></dt>
<dd> Sets the iterative improvement level. <i>level</i> is a number which can be created by combining the different levels below. The default is <code>-improve6</code>. </dd>
<dl>
<dl>
<dt><code>0</code></dt>
<dd> none.</dd>
<dt><code>1</code></dt>
<dd> running accuracy measurement of solved equations on Bx=r.</dd>
<dt><code>2</code></dt>
<dd> improve initial dual feasibility by bound flips.</dd>
<dt><code>4</code></dt>
<dd> low-cost accuracy monitoring in the dual.</dd>
<dt><code>8</code></dt>
<dd> check for primal/dual feasibility at the node level.</dd></dl>
</dl>
<dt><code>-piv</code><i>rule</i></dt>
<dd> Sets a simplex pivot rule or mode to use. The default rules are: <code>-piv2 -piva</code> </dd>
<dl>
<dt>
</dt><dd> These rules are mutually exclusive:</dd>
<dl>
<dt><code>0</code></dt>
<dd> select first.</dd>
<dt><code>1</code></dt>
<dd> select according to Dantzig.</dd>
<dt><code>2</code></dt>
<dd> select Devex pricing from Paula Harris.</dd>
<dt><code>3</code></dt>
<dd> select steepest edge.</dd></dl>
<p> The above rules can be combined with any of the following modes:</p>
<dl>
<dt><code>f</code></dt>
<dd> PrimalFallback &#8211; when steepest edge (<code>-priv3</code>) is selected, fallback to Devex in primal.</dd>
<dt><code>m</code></dt>
<dd> Multiple &#8211; preliminary implementation of the multiple pricing scheme. This means that attractive candidate entering columns from one iteration may be used in the subsequent iteration, avoiding full updating of reduced costs. In the current implementation, lp_solve only reuses the 2nd best entering column alternative</dd>
<dt><code>a</code></dt>
<dd> Adaptive &#8211; temporarily use alternative strategy if cycling is detected.</dd>
<dt><code>r</code></dt>
<dd> Randomize &#8211; adds a small randomization effect to the selected pricer.</dd>
<dt><code>ll</code></dt>
<dd> LoopLeft &#8211; scan entering/leaving columns left rather than right.</dd>
<dt><code>la</code></dt>
<dd> LoopAlternate &#8211; scan entering/leaving columns alternating left/right.</dd>
<dt><code>h</code></dt>
<dd> HarrisTwoPass &#8211; use Harris&#8217; primal pivot logic rather than the default.</dd>
<dt><code>t</code></dt>
<dd> TrueNormInit &#8211; use true norms for Devex and Steepest Edge initializations.</dd></dl>
</dl>
<dt><code>-degen</code><i>option</i></dt>
<dd> Specifies if special handling must be done to reduce degeneracy/cycling while solving. The default options are: <code>-degenf</code> <code>-degens</code>. </dd>
<dl>
<dt>
</dt><dd> Available options:</dd>
<dl>
<dt><code>c</code></dt>
<dd> ColumnCheck</dd>
<dt><code>d</code></dt>
<dd> Dynamic</dd>
<dt><code>f</code></dt>
<dd> FixedVars</dd>
<dt><code>s</code></dt>
<dd> Stalling</dd>
<dt><code>n</code></dt>
<dd> NumFailure</dd>
<dt><code>l</code></dt>
<dd> Lostfeas</dd>
<dt><code>i</code></dt>
<dd> Infeasible</dd>
<dt><code>b</code></dt>
<dd> DuringBB</dd>
<dt><code>r</code></dt>
<dd> RHSPerturb</dd>
<dt><code>p</code></dt>
<dd> BoundFlip</dd></dl>
</dl>
</dl>
<h3>Other solving options</h3>
<dl>
<dt><code>-presolve</code>[<i>option</i>]</dt>
<dd> Enables a presolve option. These options attempt to speed up calculations by simplifying the model before solving it. Any of these options can be combined together. If <i>option</i> is not specified, row and column presolving is enabled (as if <code>-presolverow -presolvecol</code> had been used). The default not to presolve. </dd>
<dl>
<dt>
</dt><dd> Available options:</dd>
<dl>
<dt><code>row</code></dt>
<dd> Rows &#8211; presolve rows.</dd>
<dt><code>col</code></dt>
<dd> Cols &#8211; presolve columns.</dd>
<dt><code>l</code></dt>
<dd> LinDep &#8211; eliminate linearly dependent rows.</dd>
<dt><code>s</code></dt>
<dd> Sos &#8211; convert constraints to SOSes (only SOS type 1 handled).</dd>
<dt><code>r</code></dt>
<dd> ReduceMip &#8211; if the phase 1 solution process finds that a constraint is redundant then this constraint is deleted.</dd>
<dt><code>k</code></dt>
<dd> Knapsack &#8211; simplification of knapsack-type constraints through addition of an extra variable, which also helps bound the objective function.</dd>
<dt><code>q</code></dt>
<dd> ElimEQ2 &#8211; direct substitution of one variable in 2-element equality constraints; this requires changes to the constraint matrix.</dd>
<dt><code>m</code></dt>
<dd> MergeRows &#8211; merges neighboring &gt;= or &lt;= constraints when the vectors are otherwise relatively identical into a single ranged constraint.</dd>
<dt><code>fd</code></dt>
<dd> ColFixDual &#8211; variable fixing and removal based on considering signs of the associated dual constraint.</dd>
<dt><code>bnd</code></dt>
<dd> Bounds &#8211; does bound tightening based on full-row constraint information.</dd>
<dt><code>d</code></dt>
<dd> Duals &#8211; presolve duals.</dd>
<dt><code>f</code></dt>
<dd> ImpliedFree &#8211; identify implied free variables (releasing their explicit bounds).</dd>
<dt><code>slk</code></dt>
<dd> ImpliedSlk- converts qualifying equalities to inequalities by converting a column singleton variable to slack.</dd>
<dt><code>g</code></dt>
<dd> ReduceGCD &#8211; reduce (tighten) coefficients in integer models based on GCD argument.</dd>
<dt><code>b</code></dt>
<dd> ProbeFix &#8211; attempt to fix binary variables at one of their bounds.</dd>
<dt><code>c</code></dt>
<dd> ProbeReduce &#8211; attempt to reduce coefficients in binary models.</dd>
<dt><code>rowd</code></dt>
<dd> RowDominate &#8211; identify and delete qualifying constraints that are dominated by others, also fixes variables at a bound.</dd>
<dt><code>cold</code></dt>
<dd> ColDominate &#8211; deletes variables (mainly binary), that are dominated by others (only one can be non-zero).</dd></dl>
</dl>
<dt><code>-s</code>[<i>mode</i>] [<i>scalelimit</i>]</dt>
<dd> Sets the scaling algorithm and/or scaling limit to use. <i>scalelimit</i> can only be specified when using the mutually exclusive integer modes. Omitting <i>mode</i> is the equivalent of using <code>-s4</code>. The default algorithm and limit is: <code>-s1 5 -si -se</code> </dd>
<dl>
<dt>
</dt><dd> These rules are mutually exclusive:</dd>
<dl>
<dt><code>0</code></dt>
<dd> no scaling.</dd>
<dt><code>1</code></dt>
<dd> geometric scaling.</dd>
<dt><code>2</code></dt>
<dd> Curtis-Reid scaling.</dd>
<dt><code>3</code></dt>
<dd> scale to convergence using largest absolute value.</dd>
<dt><code>4</code></dt>
<dd> numerical range-based scaling.</dd>
<dt><code>5</code></dt>
<dd> scale to convergence using logarithmic mean of all values.</dd>
<dt><code>6</code></dt>
<dd> scale based on the simple numerical range.</dd>
<dt><code>7</code></dt>
<dd> scale quadratic.</dd></dl>
<p> The above rules can be combined with any of the following:</p>
<dl>
<dt><code>p</code></dt>
<dd> also do power scaling.</dd>
<dt><code>i</code></dt>
<dd> also scale integer variables.</dd>
<dt><code>e</code></dt>
<dd> ensure no scaled number is outside the range -1..1.</dd></dl>
</dl>
</dl>
<h2>EXAMPLE</h2>
<h3>Model solving</h3>
<p> The following example shows a model being solved by <code>lp_solve</code>. The first line contains the objective function to be maximized and the last 3 lines contain the constraints. </p>
<pre><code>
$ cat example.lp
        max : 143 x +
    60 y;
120 x + 210 y &lt;= 15000;
110 x + 30 y &lt;= 4000;
x + y &lt;= 75;
$ lp_solve - S3 example.lp
                 Value of objective function : 6315.63 Actual values of the variables : x 21.875 y 53.125 Actual values of the constraints : R1 13781.2 R2 4000 R3 75
</code></pre>
<h3>Format conversion</h3>
<p> This example converts a file in lp format to mps format. </p>
<p> $ <code>lp_solve -parse_only -lp example.lp -wmps example.mps</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-ld-so/">ld.so</a></code>(8) </p>
