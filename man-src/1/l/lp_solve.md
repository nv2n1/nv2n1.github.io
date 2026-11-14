---
title: "lp_solve(1)"
name: "lp_solve"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lp_solve/"
description: "lp_solve – a mixed integer linear programming (MILP) solver"
---

<h2 class="name">NAME</h2>
<p> lp_solve &#8211; a mixed integer linear programming (MILP) solver </p>
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
<dt><code>int </code><i>var1 </i>[<code>, </code><i>var2</i>]&#8230; ;</p>
<dd> Marks the variables as integers.</p>
<dt><code>bin </code><i>var1 </i>[<code>, </code><i>var2</i>]&#8230; ;</p>
<dd> Marks the variables as binary (can only take 0 or 1).</p>
<dt><code>sec </code><i>var1 </i>[<code>, </code><i>var2</i>]&#8230; ;</p>
<dd> Marks the variables as semi-continuous. These variables can always take the value 0 even if it is outside the variable&#8217;s range.</p>
<dt><code>free </code><i>var1 </i>[<code>, </code><i>var2</i>]&#8230; ;</p>
<dd> Marks the variables as free. These variables have no lower bound, unlike other variables which have a default lower bound of 0.</p>
<dt><code>sos </code>[<i>name</i><code>:</code>] <i>var1 </i>[<code>, </code><i>var2</i>]&#8230; [&lt; <i>sostype</i>];</p>
<dd> Marks the variables as part of a special ordered set (SOS). Out of the variables listed, only one can be non-zero at once. If <i>sostype</i> is specified, then up to that number of variables can be non-zero as long as they are all adjacent to each other (e.g. for an <i>sostype</i> of 2, <i>var1</i> and <i>var2</i> could be non-zero, but not <i>var1</i> and <i>var3</i>). </p>
<p> Both C style comments (<code>/* </code>comment here<code> */</code>) and C++ style comments (<code>// </code>comment until end of line) can be used anywhere in the file.</dl>
<h2>OPTIONS</h2>
<h3>General options</h3>
<dl>
<dt><code>-wafter</code></p>
<dd> Writes the model after solving it (normally any model conversions are processed before solving). This is useful if presolving is used to simplify the model.</p>
<dt><code>-parse_only</code></p>
<dd> Parse the input model, but stop before solving it. This can be used to convert models between formats without solving them.</p>
<dt><code>-timeout</code><i> sec</i></p>
<dd> Timeout if no solution has be found after <i>sec</i> seconds.</p>
<dt><code>-nonames</code></p>
<dd> Ignore variable and constraint names in the input model (this is the same as combining both <code>-norownames</code> <code>-nocolnames</code>).</p>
<dt><code>-norownames</code></p>
<dd> Ignore constraint names in the input model.</p>
<dt><code>-nocolnames</code></p>
<dd> Ignore variable names in the input model.</p>
<dt><code>-min</code></p>
<dd> Minimizes the LP problem, overriding the setting in the input model.</p>
<dt><code>-max</code></p>
<dd> Maximizes the LP problem, overriding the setting in the input model.</dl>
<h3>Built-in model languages</h3>
<dl>
<dt><code>-lp</code></p>
<dd> Read the model from a file in LP format. This the the default.</p>
<dt><code>-mps</code></p>
<dd> Read the model from a file in &#8216;fixed width&#8217; MPS format.</p>
<dt><code>-fmps</code></p>
<dd> Read the model from a file in &#8216;free&#8217; MPS format. This is the same as <code>-mps</code> except that fields are separated by a number of blanks instead of starting at fixed columns.</p>
<dt><code>-wlp</code><i> filename</i></p>
<dd> Converts the input model to LP format and writes it to the a file.</p>
<dt><code>-wmps</code><i> filename</i></p>
<dd> Converts the input model to &#8216;fixed width&#8217; MPS format and writes it to a file.</p>
<dt><code>-wfmps</code><i> filename</i></p>
<dd> Converts the input model to &#8216;free&#8217; MPS format and writes it to a file.</dl>
<h3>External language interface (XLI)</h3>
<dl>
<dt><code>-rxli</code><i> xliname </i><i>filename</i></p>
<dd> Read the model using an external language interface (XLI). <i>xliname</i> specifies the path to the shared library containing the XLI, and is searched for according to the normal library search rules in <code><a href="/docs/linux/man/8-ld-so/">ld.so</a></code>(8) with the addition that the library filename is prefixed with <i>lib</i> and suffixed with <i>.so</i> if necessary.</p>
<dt><code>-rxlidata</code><i> datafilename</i></p>
<dd> Provides a file containing extra data used by the reading XLI library.</p>
<dt><code>-rxliopt</code><i> options</i></p>
<dd> Extra options to pass to the reading XLI library.</p>
<dt><code>-wxli</code><i> xliname </i><i>filename</i></p>
<dd> Converts the input model to the format used by an XLI and writes it to a file. The format of <i>xliname</i> is described in <code>-rxli</code> above.</p>
<dt><code>-wxliopt</code><i> options</i></p>
<dd> Extra options to pass to the writing XLI library.</p>
<dt><code>-wxlisol</code><i> xliname </i><i>filename</i></p>
<dd> Writes the model&#8217;s solution to a file using an XLI library. The format of <i>xliname</i> is described in <code>-rxli</code> above.</p>
<dt><code>-wxlisolopt</code><i> options</i></p>
<dd> Extra options to pass to the solution writing XLI library.</dl>
<h3>Printing, verbosity and debugging</h3>
<dl>
<dt><code>-h</code></p>
<dd> Print a usage message and exit.</p>
<dt><code>-S</code><i>level</i></p>
<dd> Solution detail. Each <i>level</i> builds on top of the previous one and adds more detail to the solution. </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>0</code></p>
<dd> print nothing</p>
<dt><code>1</code></p>
<dd> objective value only</p>
<dt><code>2</code></p>
<dd> variables (default level)</p>
<dt><code>3</code></p>
<dd> constraints</p>
<dt><code>4</code></p>
<dd> duals</p>
<dt><code>5</code></p>
<dd> lp model</p>
<dt><code>6</code></p>
<dd> scales</p>
<dt><code>7</code></p>
<dd> lp tableau</dl>
</dl>
<dt><code>-time</code></p>
<dd> Print CPU time to parse input and to calculate solution.</p>
<dt><code>-v</code>[<i>level</i>]</p>
<dd> Verbosity level. Controls the level of messages printed about the operation of the program. </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>0</code></p>
<dd> neutral</p>
<dt><code>1</code></p>
<dd> critical</p>
<dt><code>2</code></p>
<dd> severe</p>
<dt><code>3</code></p>
<dd> important (default when <code>-v</code> is provided with no <i>level</i>)</p>
<dt><code>4</code></p>
<dd> normal (default when no <code>-v</code> option is given)</p>
<dt><code>5</code></p>
<dd> detailed</p>
<dt><code>6</code></p>
<dd> full</dl>
</dl>
<dt><code>-t</code></p>
<dd> Trace pivot selection.</p>
<dt><code>-d</code></p>
<dd> Debug mode. All intermediate results and branch-and-bound decisions are printed.</p>
<dt><code>-R</code></p>
<dd> Report information while solving the model.</p>
<dt><code>-Db</code><i> filename</i></p>
<dd> Create a dump of internal model variables before solving the model to given file.</p>
<dt><code>-Da</code><i> filename</i></p>
<dd> Create a dump of internal model variables after solving the model, to given file.</p>
<dt><code>-i</code>[<code>a</code>]</p>
<dd> Print all intermediate valid solutions. If <code>a</code> is used, prints only non-zero values. Can give useful solutions even if the total run time is too long. </p>
</dl>
<h3>Parameter files</h3>
<dl>
<dt><code>-rpar</code><i> filename</i></p>
<dd> Reads a list of parameters from a file. The parameters file can specify the same options as you can by passing arguments to <code>lp_solve</code> but can be more convenient if you need to change lots of settings. The format of the parameters file is in the INI format often used by Windows applications. All parameters are read from key-value pairs in a single section. The default section is <code>[Default]</code>.</p>
<dt><code>-rparopt</code> &#8216;<code>-h </code><i>header</i>&#8216;</p>
<dd> Sets options for reading the parameters file. Currently the only option is <code>-h</code> which changes the section within the file to read the parameters from.</p>
<dt><code>-wpar</code><i> filename</i></p>
<dd> Writes a parameters file based on the arguments given to <code>lp_solve</code>.</p>
<dt><code>-wparopt</code> &#8216;<code>-h </code><i>header</i>&#8216;</p>
<dd> Sets options for writing the parameter file. Currently the only option is <code>-h</code> which changes the section within the file to write the parameters to.</dl>
<h3>Basis files</h3>
<dl>
<dt><code>-rbas</code><i> filename</i></p>
<dd> Reads a basis file which is used as the starting point for solving the LP model. Basis files must be in MPS basis format.</p>
<dt><code>-gbas</code><i> filename</i></p>
<dd> Computes a basis from a list of initial guesses for each variable. Each line of the given file is in the format: <i>variable</i><code>:</code><i>value</i> where <i>value</i> is the initial guess for <i>variable</i>.</p>
<dt><code>-wbas</code><i> filename</i></p>
<dd> After solving the LP model, writes a basis file in MPS format. This file can be read back using <code>-rbas</code>. </p>
<dl>
<dt>
<dd> Available options:</p>
<dl>
<dt><code>0</code></p>
<dd> no crash basis (default).</p>
<dt><code>1</code></p>
<dd> most feasible basis.</p>
<dt><code>2</code></p>
<dd> least degenerate basis.</dl>
</dl>
</dl>
<h3>Integer and branch and bound options</h3>
<dl>
<dt><code>-noint</code></p>
<dd> Ignore integer restrictions on variables.</p>
<dt><code>-f</code></p>
<dd> Stops the branch and bound algorithm immediately after finding its first solution.</p>
<dt><code>-o</code><i> bound</i></p>
<dd> Stops the branch and bound algorithm immediately after finding a solution whose objective function has a value greater than this bound.</p>
<dt><code>-b</code><i> bound</i></p>
<dd> Sets a lower bound for the objective function. The branch and bound algorithm will immediately reject all solutions lower than this value.</p>
<dt><code>-depth</code><i> limit</i></p>
<dd> Sets the depth limit for the branch and bound algorithm. A value of 0 disables depth limiting. A negative value sets a relative depth limit based on the number of variables in the input model. The default limit is -50.</p>
<dt><code>-e</code><i> tolerance</i></p>
<dd> Sets the tolerance which is used to determine whether a floating point number is an integer. A number has to be within this value of an integer to be considered one. The default value is 1e-7.</p>
<dt><code>-g </code><i>tolerance</i>, <code>-ga </code><i>tolerance</i></p>
<dd> Sets the absolute MIP gap used by the branch and bound algorithm. This tolerance is the difference between the best-found solution yet and the current solution. If the difference is smaller than this tolerance then the solution (and all the sub-solutions) is rejected. This can result in faster solving times, but results in a solution which is not the perfect solution. The default value is 1e-11.</p>
<dt><code>-gr</code><i> tolerance</i></p>
<dd> Sets the relative MIP gap used by the branch and bound algorithm. This is similar to the absolute tolerance except that the difference is scaled by the best found solution before being compared to this tolerance. The default value is 1e-11.</p>
<dt><code>-c</code>, <code>-cc</code></p>
<dd> During branch and bound, take the ceiling branch first.</p>
<dt><code>-cf</code></p>
<dd> During branch and bound, take the floor branch first.</p>
<dt><code>-ca</code></p>
<dd> During branch and bound, allow the algorithm to decide which branch to take. This is the default.</p>
<dt><code>-n</code><i> solution</i></p>
<dd> If the branch and bound algorithm produces multiple solutions with the same objective function value, prints the nth solution. Solution numbers start at 1.</p>
<dt><code>-B</code><i>rule</i></p>
<dd> Sets a branch and bound rule to use. The default rules are: <code>-B5 -Bg -Bd -Bc</code> </p>
<dl>
<dt>
<dd> These rules are mutually exclusive:</p>
<dl>
<dt><code>0</code></p>
<dd> select lowest indexed non-integer column.</p>
<dt><code>1</code></p>
<dd> selection based on distance from the current bounds.</p>
<dt><code>2</code></p>
<dd> selection based on the largest current bound.</p>
<dt><code>3</code></p>
<dd> selection based on largest fractional value.</p>
<dt><code>4</code></p>
<dd> simple, unweighted pseudo-cost of a variable.</p>
<dt><code>5</code></p>
<dd> extended pseudo-costing strategy based on minimizing the number of integer infeasibilities.</p>
<dt><code>6</code></p>
<dd> extended pseudo-costing strategy based on maximizing the normal pseudo-cost divided by the number of infeasibilities.</dl>
<p> The above rules can be combined with any of the following:</p>
<dl>
<dt><code>w</code></p>
<dd> WeightReverse &#8211; select by criterion minimum (worst), rather than criterion maximum (best).</p>
<dt><code>b</code></p>
<dd> BranchReverse &#8211; when <code>-ca</code> is selected, choose the opposite direction.</p>
<dt><code>g</code></p>
<dd> Greedy</p>
<dt><code>p</code></p>
<dd> PseudoCost &#8211; toggles between weighting based on pseudocost or objective function value.</p>
<dt><code>f</code></p>
<dd> DepthFirst &#8211; select the node that has already been selected before the most number of times.</p>
<dt><code>r</code></p>
<dd> Randomize &#8211; ddds a randomization factor to the score for any node candidate.</p>
<dt><code>G</code></p>
<dd> GubMode</p>
<dt><code>d</code></p>
<dd> Dynamic &#8211; when <code>-Bf</code> is selected, switch off this mode when a first solution is found.</p>
<dt><code>s</code></p>
<dd> RestartMode &#8211; enables regular restarts of pseudocost value calculations.</p>
<dt><code>B</code></p>
<dd> BreadthFirst &#8211; select the node that has been selected before the fewest number of times or not at all.</p>
<dt><code>o</code></p>
<dd> AutoOrder &#8211; order variables to improve branch-and-bound performance.</p>
<dt><code>c</code></p>
<dd> ReducedCostFixing &#8211; do bound tightening during B&amp;B based of reduced cost info.</p>
<dt><code>i</code></p>
<dd> StringInit &#8211; initialize pseudo-costs by strong branching.</dl>
</dl>
</dl>
<h3>Simplex algorithm options</h3>
<dl>
<dt><code>-prim</code>, <code>-simplexpp</code></p>
<dd> Prefer the primal simplex method for both phase 1 and phase 2.</p>
<dt><code>-dual</code>, <code>-simplexdd</code></p>
<dd> Prefer the dual simplex method for both phase 1 and phase 2.</p>
<dt><code>-simplexdp</code></p>
<dd> Prefer the dual simplex method for phase 1 and primal method for phase 2. This is the default.</p>
<dt><code>-simplexpd</code></p>
<dd> Prefer the primal simplex method for phase 1 and dual method for phase 2.</p>
<dt><code>-bfp</code><i> filename</i></p>
<dd> Sets the basis factorization package to use. <i>filename</i> refers to a shared library loaded in the same way <code>-rxli</code> loads libraries.</p>
<dt><code>-o</code><i>value</i></p>
<dd> Sets whether the objective function is stored in the top row of the constraint matrix or in separate storage. <code>-o0</code> places the matrix in separate storage, and <code>-o1</code> (the default) places it in the constraint matrix.</p>
<dt><code>-C</code><i>mode</i></p>
<dd> Sets the basis crash mode. When base crash is enabled, a heuristic &#8216;crash procedure&#8217; is executed before the first simplex iteration to quickly choose a basis matrix that has fewer artificial variables. This procedure tends to reduce the number of iterations to optimality since a number of iterations are skipped.</p>
<dt><code>-r</code><i> value</i></p>
<dd> Sets the maximum number of pivots between a re-inversion of the matrix. For stability reasons, lp_solve re-inverts the matrix on regular times. The default is 250 for the LUSOL bfp and 42 for the other BFPs.</p>
<dt><code>-trej</code><i> value</i></p>
<dd> Sets the value that is used as a tolerance pivot element to determine whether a value should be considered as 0. The default is 2e-7.</p>
<dt><code>-epsd</code><i> value</i></p>
<dd> Sets the value that is used as a tolerance for reduced costs to determine whether a value should be considered as 0. The default is 1e-9.</p>
<dt><code>-epsb</code><i> value</i></p>
<dd> Sets the value that is used as a tolerance for the Right Hand Side (RHS) to determine whether a value should be considered as 0. The default is 1e-10.</p>
<dt><code>-epsel</code><i> value</i></p>
<dd> Sets the value that is used as a tolerance for rounding values to zero. The default is 1e-12.</p>
<dt><code>-epsp</code><i> value</i></p>
<dd> Sets the value that is used as perturbation scalar for degenerative problems. The default is 1e-5.</p>
<dt><code>-improve</code><i>level</i></p>
<dd> Sets the iterative improvement level. <i>level</i> is a number which can be created by combining the different levels below. The default is <code>-improve6</code>. </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>0</code></p>
<dd> none.</p>
<dt><code>1</code></p>
<dd> running accuracy measurement of solved equations on Bx=r.</p>
<dt><code>2</code></p>
<dd> improve initial dual feasibility by bound flips.</p>
<dt><code>4</code></p>
<dd> low-cost accuracy monitoring in the dual.</p>
<dt><code>8</code></p>
<dd> check for primal/dual feasibility at the node level.</dl>
</dl>
<dt><code>-piv</code><i>rule</i></p>
<dd> Sets a simplex pivot rule or mode to use. The default rules are: <code>-piv2 -piva</code> </p>
<dl>
<dt>
<dd> These rules are mutually exclusive:</p>
<dl>
<dt><code>0</code></p>
<dd> select first.</p>
<dt><code>1</code></p>
<dd> select according to Dantzig.</p>
<dt><code>2</code></p>
<dd> select Devex pricing from Paula Harris.</p>
<dt><code>3</code></p>
<dd> select steepest edge.</dl>
<p> The above rules can be combined with any of the following modes:</p>
<dl>
<dt><code>f</code></p>
<dd> PrimalFallback &#8211; when steepest edge (<code>-priv3</code>) is selected, fallback to Devex in primal.</p>
<dt><code>m</code></p>
<dd> Multiple &#8211; preliminary implementation of the multiple pricing scheme. This means that attractive candidate entering columns from one iteration may be used in the subsequent iteration, avoiding full updating of reduced costs. In the current implementation, lp_solve only reuses the 2nd best entering column alternative</p>
<dt><code>a</code></p>
<dd> Adaptive &#8211; temporarily use alternative strategy if cycling is detected.</p>
<dt><code>r</code></p>
<dd> Randomize &#8211; adds a small randomization effect to the selected pricer.</p>
<dt><code>ll</code></p>
<dd> LoopLeft &#8211; scan entering/leaving columns left rather than right.</p>
<dt><code>la</code></p>
<dd> LoopAlternate &#8211; scan entering/leaving columns alternating left/right.</p>
<dt><code>h</code></p>
<dd> HarrisTwoPass &#8211; use Harris&#8217; primal pivot logic rather than the default.</p>
<dt><code>t</code></p>
<dd> TrueNormInit &#8211; use true norms for Devex and Steepest Edge initializations.</dl>
</dl>
<dt><code>-degen</code><i>option</i></p>
<dd> Specifies if special handling must be done to reduce degeneracy/cycling while solving. The default options are: <code>-degenf</code> <code>-degens</code>. </p>
<dl>
<dt>
<dd> Available options:</p>
<dl>
<dt><code>c</code></p>
<dd> ColumnCheck</p>
<dt><code>d</code></p>
<dd> Dynamic</p>
<dt><code>f</code></p>
<dd> FixedVars</p>
<dt><code>s</code></p>
<dd> Stalling</p>
<dt><code>n</code></p>
<dd> NumFailure</p>
<dt><code>l</code></p>
<dd> Lostfeas</p>
<dt><code>i</code></p>
<dd> Infeasible</p>
<dt><code>b</code></p>
<dd> DuringBB</p>
<dt><code>r</code></p>
<dd> RHSPerturb</p>
<dt><code>p</code></p>
<dd> BoundFlip</dl>
</dl>
</dl>
<h3>Other solving options</h3>
<dl>
<dt><code>-presolve</code>[<i>option</i>]</p>
<dd> Enables a presolve option. These options attempt to speed up calculations by simplifying the model before solving it. Any of these options can be combined together. If <i>option</i> is not specified, row and column presolving is enabled (as if <code>-presolverow -presolvecol</code> had been used). The default not to presolve. </p>
<dl>
<dt>
<dd> Available options:</p>
<dl>
<dt><code>row</code></p>
<dd> Rows &#8211; presolve rows.</p>
<dt><code>col</code></p>
<dd> Cols &#8211; presolve columns.</p>
<dt><code>l</code></p>
<dd> LinDep &#8211; eliminate linearly dependent rows.</p>
<dt><code>s</code></p>
<dd> Sos &#8211; convert constraints to SOSes (only SOS type 1 handled).</p>
<dt><code>r</code></p>
<dd> ReduceMip &#8211; if the phase 1 solution process finds that a constraint is redundant then this constraint is deleted.</p>
<dt><code>k</code></p>
<dd> Knapsack &#8211; simplification of knapsack-type constraints through addition of an extra variable, which also helps bound the objective function.</p>
<dt><code>q</code></p>
<dd> ElimEQ2 &#8211; direct substitution of one variable in 2-element equality constraints; this requires changes to the constraint matrix.</p>
<dt><code>m</code></p>
<dd> MergeRows &#8211; merges neighboring &gt;= or &lt;= constraints when the vectors are otherwise relatively identical into a single ranged constraint.</p>
<dt><code>fd</code></p>
<dd> ColFixDual &#8211; variable fixing and removal based on considering signs of the associated dual constraint.</p>
<dt><code>bnd</code></p>
<dd> Bounds &#8211; does bound tightening based on full-row constraint information.</p>
<dt><code>d</code></p>
<dd> Duals &#8211; presolve duals.</p>
<dt><code>f</code></p>
<dd> ImpliedFree &#8211; identify implied free variables (releasing their explicit bounds).</p>
<dt><code>slk</code></p>
<dd> ImpliedSlk- converts qualifying equalities to inequalities by converting a column singleton variable to slack.</p>
<dt><code>g</code></p>
<dd> ReduceGCD &#8211; reduce (tighten) coefficients in integer models based on GCD argument.</p>
<dt><code>b</code></p>
<dd> ProbeFix &#8211; attempt to fix binary variables at one of their bounds.</p>
<dt><code>c</code></p>
<dd> ProbeReduce &#8211; attempt to reduce coefficients in binary models.</p>
<dt><code>rowd</code></p>
<dd> RowDominate &#8211; identify and delete qualifying constraints that are dominated by others, also fixes variables at a bound.</p>
<dt><code>cold</code></p>
<dd> ColDominate &#8211; deletes variables (mainly binary), that are dominated by others (only one can be non-zero).</dl>
</dl>
<dt><code>-s</code>[<i>mode</i>] [<i>scalelimit</i>]</p>
<dd> Sets the scaling algorithm and/or scaling limit to use. <i>scalelimit</i> can only be specified when using the mutually exclusive integer modes. Omitting <i>mode</i> is the equivalent of using <code>-s4</code>. The default algorithm and limit is: <code>-s1 5 -si -se</code> </p>
<dl>
<dt>
<dd> These rules are mutually exclusive:</p>
<dl>
<dt><code>0</code></p>
<dd> no scaling.</p>
<dt><code>1</code></p>
<dd> geometric scaling.</p>
<dt><code>2</code></p>
<dd> Curtis-Reid scaling.</p>
<dt><code>3</code></p>
<dd> scale to convergence using largest absolute value.</p>
<dt><code>4</code></p>
<dd> numerical range-based scaling.</p>
<dt><code>5</code></p>
<dd> scale to convergence using logarithmic mean of all values.</p>
<dt><code>6</code></p>
<dd> scale based on the simple numerical range.</p>
<dt><code>7</code></p>
<dd> scale quadratic.</dl>
<p> The above rules can be combined with any of the following:</p>
<dl>
<dt><code>p</code></p>
<dd> also do power scaling.</p>
<dt><code>i</code></p>
<dd> also scale integer variables.</p>
<dt><code>e</code></p>
<dd> ensure no scaled number is outside the range -1..1.</dl>
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
<h2>Index</h2>
