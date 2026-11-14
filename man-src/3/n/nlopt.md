---
title: "nlopt(3)"
name: "nlopt"
section: "3"
letter: "n"
url: "/docs/linux/man/3-nlopt/"
description: "nlopt – Nonlinear optimization library"
---

<p>nlopt &#8211; Nonlinear optimization library</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;nlopt.h&gt;

nlopt_opt opt = nlopt_create(algorithm, n);
nlopt_set_min_objective(opt, f, f_data);
nlopt_set_ftol_rel(opt, tol);
...
nlopt_optimize(opt, x , &amp;opt_f);
nlopt_destroy(opt);

The &quot;...&quot; indicates any number of calls to NLopt functions, below, to
set parameters of the optimization, constraints, and stopping
criteria.  Here, nlopt_set_ftol_rel is merely an example of a
possible stopping criterion.  You should link the resulting program
with the linker flags -lnlopt -lm on Unix.</code></pre>
<h2>Description</h2>
<p>NLopt is a library for nonlinear optimization. It attempts to minimize (or maximize) a given nonlinear objective function <i>f</i> of <i>n</i> design variables, using the specified <i>algorithm</i>, possibly subject to linear or nonlinear constraints. The optimum function value found is returned in <i>opt_f</i> (type double) with the corresponding design variable values returned in the (double) array <i>x</i> of length <i>n</i>. The input values in <i>x</i> should be a starting guess for the optimum. </p>
<p> The parameters of the optimization are controlled via the object <i>opt</i> of type <code>nlopt_opt</code>, which is created by the function <code>nlopt_create</code> and disposed of by <code>nlopt_destroy</code>. By calling various functions in the NLopt library, one can specify stopping criteria (e.g., a relative tolerance on the objective function value is specified by <code>nlopt_set_ftol_rel</code>), upper and/or lower bounds on the design parameters <i>x</i>, and even arbitrary nonlinear inequality and equality constraints. </p>
<p> By changing the parameter <i>algorithm</i> among several predefined constants described below, one can switch easily between a variety of minimization algorithms. Some of these algorithms require the gradient (derivatives) of the function to be supplied via <i>f</i>, and other algorithms do not require derivatives. Some of the algorithms attempt to find a global optimum within the given bounds, and others find only a local optimum. Most of the algorithms only handle the case where there are no nonlinear constraints. The NLopt library is a wrapper around several free/open-source minimization packages, as well as some new implementations of published optimization algorithms. You could, of course, compile and call these packages separately, and in some cases this will provide greater flexibility than is available via NLopt. However, depending upon the specific function being optimized, the different algorithms will vary in effectiveness. The intent of NLopt is to allow you to quickly switch between algorithms in order to experiment with them for your problem, by providing a simple unified interface to these subroutines.</p>
<h2>Objective Function</h2>
<p>The objective function is specified by calling one of: </p>
<p> <code> nlopt_result nlopt_set_min_objective(nlopt_opt </code><i>opt</i><code>,</code><br />
 <code> nlopt_func </code><i>f</i><code>,</code><br />
 <code> void* </code><i>f_data</i><code>);</code><br />
 <code> nlopt_result nlopt_set_max_objective(nlopt_opt </code><i>opt</i><code>,</code><br />
 <code> nlopt_func </code><i>f</i><code>,</code><br />
 <code> void* </code><i>f_data</i><code>);</code> </p>
<p> depending on whether one wishes to minimize or maximize the objective function <i>f</i>, respectively. The function <i>f</i> should be of the form: </p>
<p> <code> double f(unsigned </code><i>n</i><code>,</code><br />
 <code> const double* </code><i>x</i><code>,</code><br />
 <code> double* </code><i>grad</i><code>,</code><br />
 <code> void* </code><i>f_data</i><code>);</code> </p>
<p> The return value should be the value of the function at the point <i>x</i>, where <i>x</i> points to an array of length <i>n</i> of the design variables. The dimension <i>n</i> is identical to the one passed to <code>nlopt_create</code>. </p>
<p> In addition, if the argument <i>grad</i> is not NULL, then <i>grad</i> points to an array of length <i>n</i> which should (upon return) be set to the gradient of the function with respect to the design variables at <i>x</i>. That is, <i>grad[i]</i> should upon return contain the partial derivative df/dx[i], for 0 &lt;= i &lt; n, if <i>grad</i> is non-NULL. Not all of the optimization algorithms (below) use the gradient information: for algorithms listed as &quot;derivative-free,&quot; the <i>grad</i> argument will always be NULL and need never be computed. (For algorithms that do use gradient information, however, <i>grad</i> may still be NULL for some calls.) </p>
<p> The <i>f_data</i> argument is the same as the one passed to <code>nlopt_set_min_objective</code> or <code>nlopt_set_max_objective</code>, and may be used to pass any additional data through to the function. (That is, it may be a pointer to some caller-defined data structure/type containing information your function needs, which you convert from void* by a typecast.)</p>
<h2>Bound Constraints</h2>
<p>Most of the algorithms in NLopt are designed for minimization of functions with simple bound constraints on the inputs. That is, the input vectors x[i] are constrainted to lie in a hyperrectangle lb[i] &lt;= x[i] &lt;= ub[i] for 0 &lt;= i &lt; n. These bounds are specified by passing arrays <i>lb</i> and <i>ub</i> of length <i>n</i> to one or both of the functions: </p>
<p> <code> nlopt_result nlopt_set_lower_bounds(nlopt_opt </code><i>opt</i><code>,</code><br />
 <code> const double* </code><i>lb</i><code>);</code><br />
 <code> nlopt_result nlopt_set_upper_bounds(nlopt_opt </code><i>opt</i><code>,</code><br />
 <code> const double* </code><i>ub</i><code>);</code> </p>
<p> If a lower/upper bound is not set, the default is no bound (unconstrained, i.e. a bound of infinity); it is possible to have lower bounds but not upper bounds or vice versa. Alternatively, the user can call one of the above functions and explicitly pass a lower bound of -HUGE_VAL and/or an upper bound of +HUGE_VAL for some design variables to make them have no lower/upper bound, respectively. (HUGE_VAL is the standard C constant for a floating-point infinity, found in the math.h header file.) </p>
<p> Note, however, that some of the algorithms in NLopt, in particular most of the global-optimization algorithms, do not support unconstrained optimization and will return an error if you do not supply finite lower and upper bounds. </p>
<p> For convenience, the following two functions are supplied in order to set the lower/upper bounds for all design variables to a single constant (so that you don&#8217;t have to fill an array with a constant value): </p>
<p> <code> nlopt_result nlopt_set_lower_bounds1(nlopt_opt </code><i>opt</i><code>,</code><br />
 <code> double </code><i>lb</i><code>);</code><br />
 <code> nlopt_result nlopt_set_upper_bounds1(nlopt_opt </code><i>opt</i><code>,</code><br />
 <code> double </code><i>ub</i><code>);</code></p>
<h2>Nonlinear Constraints</h2>
<p>Several of the algorithms in NLopt (MMA and ORIG_DIRECT) also support arbitrary nonlinear inequality constraints, and some also allow nonlinear equality constraints (COBYLA, SLSQP, ISRES, and AUGLAG). For these algorithms, you can specify as many nonlinear constraints as you wish by calling the following functions multiple times. </p>
<p> In particular, a nonlinear inequality constraint of the form <i>fc</i>(<i>x</i>) &lt;= 0, where the function <i>fc</i> is of the same form as the objective function described above, can be specified by calling: </p>
<p> <code> nlopt_result nlopt_add_inequality_constraint(nlopt_opt </code><i>opt</i><code>,</code><br />
 <code> nlopt_func </code><i>fc</i><code>,</code><br />
 <code> void* </code><i>fc_data</i><code>,</code><br />
 <code> double </code><i>tol</i><code>);</code> </p>
<p> Just as for the objective function, <i>fc_data</i> is a pointer to arbitrary user data that will be passed through to the <i>fc</i> function whenever it is called. The parameter <i>tol</i> is a tolerance that is used for the purpose of stopping criteria only: a point <i>x</i> is considered feasible for judging whether to stop the optimization if <i>fc</i>(<i>x</i>) &lt;= <i>tol</i>. A tolerance of zero means that NLopt will try not to consider any <i>x</i> to be converged unless <i>fc</i> is strictly non-positive; generally, at least a small positive tolerance is advisable to reduce sensitivity to rounding errors. </p>
<p> A nonlinear equality constraint of the form <i>h</i>(<i>x</i>) = 0, where the function <i>h</i> is of the same form as the objective function described above, can be specified by calling: </p>
<p> <code> nlopt_result nlopt_add_equality_constraint(nlopt_opt </code><i>opt</i><code>,</code><br />
 <code> nlopt_func </code><i>h</i><code>,</code><br />
 <code> void* </code><i>h_data</i><code>,</code><br />
 <code> double </code><i>tol</i><code>);</code> </p>
<p> Just as for the objective function, <i>h_data</i> is a pointer to arbitrary user data that will be passed through to the <i>h</i> function whenever it is called. The parameter <i>tol</i> is a tolerance that is used for the purpose of stopping criteria only: a point <i>x</i> is considered feasible for judging whether to stop the optimization if |<i>h</i>(<i>x</i>)| &lt;= <i>tol</i>. For equality constraints, a small positive tolerance is strongly advised in order to allow NLopt to converge even if the equality constraint is slightly nonzero. </p>
<p> (For any algorithm listed as &quot;derivative-free&quot; below, the <i>grad</i> argument to <i>fc</i> or <i>h</i> will always be NULL and need never be computed.) </p>
<p> To remove all of the inequality and/or equality constraints from a given problem <i>opt</i>, you can call the following functions: </p>
<p> <code> nlopt_result nlopt_remove_inequality_constraints(nlopt_opt </code><i>opt</i><code>);</code><br />
 <code> nlopt_result nlopt_remove_equality_constraints(nlopt_opt </code><i>opt</i><code>);</code></p>
<h2>Algorithms</h2>
<p>The <i>algorithm</i> parameter specifies the optimization algorithm (for more detail on these, see the README files in the source-code subdirectories), and can take on any of the following constant values. </p>
<p> Constants with <code>_G{N,D}_</code> in their names refer to global optimization methods, whereas <code>_L{N,D}_</code> refers to local optimization methods (that try to find a local optimum starting from the starting guess <i>x</i>). Constants with <code>_{G,L}N_</code> refer to non-gradient (derivative-free) algorithms that do not require the objective function to supply a gradient, whereas <code>_{G,L}D_</code> refers to derivative-based algorithms that require the objective function to supply a gradient. (Especially for local optimization, derivative-based algorithms are generally superior to derivative-free ones: the gradient is good to have <i>if </i> you can compute it cheaply, e.g. via an adjoint method.) </p>
<p> The algorithm specified for a given problem <i>opt</i> is returned by the function: </p>
<p> <code> nlopt_algorithm nlopt_get_algorithm(nlopt_opt </code><i>opt</i><code>);</code> </p>
<p> The available algorithms are:</p>
<dl>
<dt><code>NLOPT_GN_DIRECT_L</code></p>
<dd>Perform a global (G) derivative-free (N) optimization using the DIRECT-L search algorithm by Jones et al. as modified by Gablonsky et al. to be more weighted towards local search. Does not support unconstrainted optimization. There are also several other variants of the DIRECT algorithm that are supported: <code>NLOPT_GLOBAL_DIRECT</code>, which is the original DIRECT algorithm; <code>NLOPT_GLOBAL_DIRECT_L_RAND</code>, a slightly randomized version of DIRECT-L that may be better in high-dimensional search spaces; <code>NLOPT_GLOBAL_DIRECT_NOSCAL</code>, <code>NLOPT_GLOBAL_DIRECT_L_NOSCAL</code>, and <code>NLOPT_GLOBAL_DIRECT_L_RAND_NOSCAL</code>, which are versions of DIRECT where the dimensions are not rescaled to a unit hypercube (which means that dimensions with larger bounds are given more weight).</p>
<dt><code>NLOPT_GN_ORIG_DIRECT_L</code></p>
<dd>A global (G) derivative-free optimization using the DIRECT-L algorithm as above, along with <code>NLOPT_GN_ORIG_DIRECT</code> which is the original DIRECT algorithm. Unlike <code>NLOPT_GN_DIRECT_L </code> above, these two algorithms refer to code based on the original Fortran code of Gablonsky et al., which has some hard-coded limitations on the number of subdivisions etc. and does not support all of the NLopt stopping criteria, but on the other hand it supports arbitrary nonlinear inequality constraints.</p>
<dt><code>NLOPT_GD_STOGO</code></p>
<dd>Global (G) optimization using the StoGO algorithm by Madsen et al. StoGO exploits gradient information (D) (which must be supplied by the objective) for its local searches, and performs the global search by a branch-and-bound technique. Only bound-constrained optimization is supported. There is also another variant of this algorithm, <code>NLOPT_GD_STOGO_RAND</code>, which is a randomized version of the StoGO search scheme. The StoGO algorithms are only available if NLopt is compiled with C++ code enabled, and should be linked via -lnlopt_cxx instead of -lnlopt (via a C++ compiler, in order to link the C++ standard libraries).</p>
<dt><code>NLOPT_LN_NELDERMEAD</code></p>
<dd>Perform a local (L) derivative-free (N) optimization, starting at <i>x</i>, using the Nelder-Mead simplex algorithm, modified to support bound constraints. Nelder-Mead, while popular, is known to occasionally fail to converge for some objective functions, so it should be used with caution. Anecdotal evidence, on the other hand, suggests that it works fairly well for some cases that are hard to handle otherwise, e.g. noisy/discontinuous objectives. See also <code>NLOPT_LN_SBPLX</code> below.</p>
<dt><code>NLOPT_LN_SBPLX</code></p>
<dd>Perform a local (L) derivative-free (N) optimization, starting at <i>x</i>, using an algorithm based on the Subplex algorithm of Rowan et al., which is an improved variant of Nelder-Mead (above). Our implementation does not use Rowan&#8217;s original code, and has some minor modifications such as explicit support for bound constraints. (Like Nelder-Mead, Subplex often works well in practice, even for noisy/discontinuous objectives, but there is no rigorous guarantee that it will converge.)</p>
<dt><code>NLOPT_LN_PRAXIS</code></p>
<dd>Local (L) derivative-free (N) optimization using the principal-axis method, based on code by Richard Brent. Designed for unconstrained optimization, although bound constraints are supported too (via the inefficient method of returning +Inf when the constraints are violated).</p>
<dt><code>NLOPT_LD_LBFGS</code></p>
<dd>Local (L) gradient-based (D) optimization using the limited-memory BFGS (L-BFGS) algorithm. (The objective function must supply the gradient.) Unconstrained optimization is supported in addition to simple bound constraints (see above). Based on an implementation by Luksan et al.</p>
<dt><code>NLOPT_LD_VAR2</code></p>
<dd>Local (L) gradient-based (D) optimization using a shifted limited-memory variable-metric method based on code by Luksan et al., supporting both unconstrained and bound-constrained optimization. <code>NLOPT_LD_VAR2</code> uses a rank-2 method, while <code>.B NLOPT_LD_VAR1</code> is another variant using a rank-1 method.</p>
<dt><code>NLOPT_LD_TNEWTON_PRECOND_RESTART</code></p>
<dd>Local (L) gradient-based (D) optimization using an LBFGS-preconditioned truncated Newton method with steepest-descent restarting, based on code by Luksan et al., supporting both unconstrained and bound-constrained optimization. There are several other variants of this algorithm: <code>NLOPT_LD_TNEWTON_PRECOND </code> (same without restarting), <code>NLOPT_LD_TNEWTON_RESTART</code> (same without preconditioning), and <code>NLOPT_LD_TNEWTON</code> (same without restarting or preconditioning).</p>
<dt><code>NLOPT_GN_CRS2_LM</code></p>
<dd>Global (G) derivative-free (N) optimization using the controlled random search (CRS2) algorithm of Price, with the &quot;local mutation&quot; (LM) modification suggested by Kaelo and Ali.</p>
<dt><code>NLOPT_GN_ISRES</code></p>
<dd>Global (G) derivative-free (N) optimization using a genetic algorithm (mutation and differential evolution), using a stochastic ranking to handle nonlinear inequality and equality constraints as suggested by Runarsson and Yao.</p>
<dt><code>NLOPT_G_MLSL_LDS</code>, <code>NLOPT_G_MLSL</code></p>
<dd>Global (G) optimization using the multi-level single-linkage (MLSL) algorithm with a low-discrepancy sequence (LDS) or pseudorandom numbers, respectively. This algorithm executes a low-discrepancy or pseudorandom sequence of local searches, with a clustering heuristic to avoid multiple local searches for the same local optimum. The local search algorithm must be specified, along with termination criteria/tolerances for the local searches, by <i>nlopt_set_local_optimizer</i>. (This subsidiary algorithm can be with or without derivatives, and determines whether the objective function needs gradients.)</p>
<dt><code>NLOPT_LD_MMA</code>, <code>NLOPT_LD_CCSAQ</code></p>
<dd>Local (L) gradient-based (D) optimization using the method of moving asymptotes (MMA), or rather a refined version of the algorithm as published by Svanberg (2002). (NLopt uses an independent free-software/open-source implementation of Svanberg&#8217;s algorithm.) CCSAQ is a related algorithm from Svanberg&#8217;s paper which uses a local quadratic approximation rather than the more-complicated MMA model; the two usually have similar convergence rates. The <code>NLOPT_LD_MMA</code> algorithm supports both bound-constrained and unconstrained optimization, and also supports an arbitrary number (<i>m</i>) of nonlinear inequality (not equality) constraints as described above.</p>
<dt><code>NLOPT_LD_SLSQP</code></p>
<dd>Local (L) gradient-based (D) optimization using sequential quadratic programming and BFGS updates, supporting arbitrary nonlinear inequality and equality constraints, based on the code by Dieter Kraft (1988) adapted for use by the SciPy project. Note that this algorithm uses dense-matrix methods requiring O(<i>n</i>^2) storage and O(<i>n</i>^3) time, making it less practical for problems involving more than a few thousand parameters.</p>
<dt><code>NLOPT_LN_COBYLA</code></p>
<dd>Local (L) derivative-free (N) optimization using the COBYLA algorithm of Powell (Constrained Optimization BY Linear Approximations). The <code>NLOPT_LN_COBYLA</code> algorithm supports both bound-constrained and unconstrained optimization, and also supports an arbitrary number (<i>m</i>) of nonlinear inequality/equality constraints as described above.</p>
<dt><code>NLOPT_LN_NEWUOA</code></p>
<dd>Local (L) derivative-free (N) optimization using a variant of the NEWUOA algorithm of Powell, based on successive quadratic approximations of the objective function. We have modified the algorithm to support bound constraints. The original NEWUOA algorithm is also available, as <code>NLOPT_LN_NEWUOA</code>, but this algorithm ignores the bound constraints <i>lb</i> and <i>ub</i>, and so it should only be used for unconstrained problems. Mostly superseded by BOBYQA.</p>
<dt><code>NLOPT_LN_BOBYQA</code></p>
<dd>Local (L) derivative-free (N) optimization using the BOBYQA algorithm of Powell, based on successive quadratic approximations of the objective function, supporting bound constraints.</p>
<dt><code>NLOPT_AUGLAG</code></p>
<dd>Optimize an objective with nonlinear inequality/equality constraints via an unconstrained (or bound-constrained) optimization algorithm, using a gradually increasing &quot;augmented Lagrangian&quot; penalty for violated constraints. Requires you to specify another optimization algorithm for optimizing the objective+penalty function, using <i>nlopt_set_local_optimizer</i>. (This subsidiary algorithm can be global or local and with or without derivatives, but you must specify its own termination criteria.) A variant, <code>NLOPT_AUGLAG_EQ</code>, only uses the penalty approach for equality constraints, while inequality constraints are handled directly by the subsidiary algorithm (restricting the choice of subsidiary algorithms to those that can handle inequality constraints).</dl>
<h2>Stopping Criteria</h2>
<p>Multiple stopping criteria for the optimization are supported, as specified by the functions to modify a given optimization problem <code>opt</code>. The optimization halts whenever any one of these criteria is satisfied. In some cases, the precise interpretation of the stopping criterion depends on the optimization algorithm above (although we have tried to make them as consistent as reasonably possible), and some algorithms do not support all of the stopping criteria. </p>
<p> Important: you do not need to use all of the stopping criteria! In most cases, you only need one or two, and can omit the remainder (all criteria are disabled by default).</p>
<dl>
<dt><code>nlopt_result nlopt_set_stopval(nlopt_opt </code><i>opt</i><code>,</code></p>
<dd><code> double </code><i>stopval</i><code>);</code> </p>
<p> Stop when an objective value of at least <i>stopval</i> is found: stop minimizing when a value &lt;= <i>stopval</i> is found, or stop maximizing when a value &gt;= <i>stopval</i> is found. (Setting <i>stopval</i> to -HUGE_VAL for minimizing or +HUGE_VAL for maximizing disables this stopping criterion.)</p>
<dt><code>nlopt_result nlopt_set_ftol_rel(nlopt_opt </code><i>opt</i><code>,</code></p>
<dd><code> double </code><i>tol</i><code>);</code> </p>
<p> Set relative tolerance on function value: stop when an optimization step (or an estimate of the optimum) changes the function value by less than <i>tol</i> multiplied by the absolute value of the function value. (If there is any chance that your optimum function value is close to zero, you might want to set an absolute tolerance with <code>nlopt_set_ftol_abs</code> as well.) Criterion is disabled if <i>tol</i> is non-positive.</p>
<dt><code>nlopt_result nlopt_set_ftol_abs(nlopt_opt </code><i>opt</i><code>,</code></p>
<dd><code> double </code><i>tol</i><code>);</code> </p>
<p> Set absolute tolerance on function value: stop when an optimization step (or an estimate of the optimum) changes the function value by less than <i>tol</i>. Criterion is disabled if <i>tol</i> is non-positive.</p>
<dt><code>nlopt_result nlopt_set_xtol_rel(nlopt_opt </code><i>opt</i><code>,</code></p>
<dd><code> double </code><i>tol</i><code>);</code> </p>
<p> Set relative tolerance on design variables: stop when an optimization step (or an estimate of the optimum) changes every design variable by less than <i>tol</i> multiplied by the absolute value of the design variable. (If there is any chance that an optimal design variable is close to zero, you might want to set an absolute tolerance with <code>nlopt_set_xtol_abs</code> as well.) Criterion is disabled if <i>tol</i> is non-positive.</p>
<dt><code>nlopt_result nlopt_set_xtol_abs(nlopt_opt </code><i>opt</i><code>,</code></p>
<dd><code> const double* </code><i>tol</i><code>);</code> </p>
<p> Set absolute tolerances on design variables. <i>tol</i> is a pointer to an array of length <i>n giving the tolerances: stop when an</i> optimization step (or an estimate of the optimum) changes every design variable <i>x</i>[i] by less than <i>tol</i>[i]. </p>
<p> For convenience, the following function may be used to set the absolute tolerances in all <i>n</i> design variables to the same value: </p>
<p> <code> nlopt_result nlopt_set_xtol_abs1(nlopt_opt </code><i>opt</i><code>,</code><br />
 <code> double </code><i>tol</i><code>);</code> </p>
<p> Criterion is disabled if <i>tol</i> is non-positive.</p>
<dt><code>nlopt_result nlopt_set_maxeval(nlopt_opt </code><i>opt</i><code>,</code></p>
<dd><code> int </code><i>maxeval</i><code>);</code> </p>
<p> Stop when the number of function evaluations exceeds <i>maxeval</i>. (This is not a strict maximum: the number of function evaluations may exceed <i>maxeval </i> slightly, depending upon the algorithm.) Criterion is disabled if <i>maxeval</i> is non-positive.</p>
<dt><code>nlopt_result nlopt_set_maxtime(nlopt_opt </code><i>opt</i><code>,</code></p>
<dd><code> double </code><i>maxtime</i><code>);</code> </p>
<p> Stop when the optimization time (in seconds) exceeds <i>maxtime</i>. (This is not a strict maximum: the time may exceed <i>maxtime</i> slightly, depending upon the algorithm and on how slow your function evaluation is.) Criterion is disabled if <i>maxtime</i> is non-positive.</dl>
<h2>Return Value</h2>
<p>Most of the NLopt functions return an enumerated constant of type <code>nlopt_result</code>, which takes on one of the following values:</p>
<h3>Successful termination (positive return values):</h3>
<dl>
<dt><code>NLOPT_SUCCESS</code></p>
<dd>Generic success return value.</p>
<dt><code>NLOPT_STOPVAL_REACHED</code></p>
<dd>Optimization stopped because <i>stopval</i> (above) was reached.</p>
<dt><code>NLOPT_FTOL_REACHED</code></p>
<dd>Optimization stopped because <i>ftol_rel</i> or <i>ftol_abs</i> (above) was reached.</p>
<dt><code>NLOPT_XTOL_REACHED</code></p>
<dd>Optimization stopped because <i>xtol_rel</i> or <i>xtol_abs</i> (above) was reached.</p>
<dt><code>NLOPT_MAXEVAL_REACHED</code></p>
<dd>Optimization stopped because <i>maxeval</i> (above) was reached.</p>
<dt><code>NLOPT_MAXTIME_REACHED</code></p>
<dd>Optimization stopped because <i>maxtime</i> (above) was reached.</dl>
<h3>Error codes (negative return values):</h3>
<dl>
<dt><code>NLOPT_FAILURE</code></p>
<dd>Generic failure code.</p>
<dt><code>NLOPT_INVALID_ARGS</code></p>
<dd>Invalid arguments (e.g. lower bounds are bigger than upper bounds, an unknown algorithm was specified, etcetera).</p>
<dt><code>NLOPT_OUT_OF_MEMORY</code></p>
<dd>Ran out of memory.</p>
<dt><code>NLOPT_ROUNDOFF_LIMITED</code></p>
<dd>Halted because roundoff errors limited progress.</p>
<dt><code>NLOPT_FORCED_STOP</code></p>
<dd>Halted because the user called <code>nlopt_force_stop</code>(<i>opt</i>) on the optimization&#8217;s <code>nlopt_opt</code> object <i>opt</i> from the user&#8217;s objective function.</dl>
<h2>Local Optimizer</h2>
<p>Some of the algorithms, especially MLSL and AUGLAG, use a different optimization algorithm as a subroutine, typically for local optimization. You can change the local search algorithm and its tolerances by calling: </p>
<p> <code> nlopt_result nlopt_set_local_optimizer(nlopt_opt </code><i>opt</i><code>,</code><br />
 <code> const nlopt_opt </code><i>local_opt</i><code>);</code> </p>
<p> Here, <i>local_opt</i> is another <code>nlopt_opt</code> object whose parameters are used to determine the local search algorithm and stopping criteria. (The objective function, bounds, and nonlinear-constraint parameters of <i>local_opt</i> are ignored.) The dimension <i>n</i> of <i>local_opt</i> must match that of <i>opt</i>. </p>
<p> This function makes a copy of the <i>local_opt</i> object, so you can freely destroy your original <i>local_opt</i> afterwards.</p>
<h2>Initial Step Size</h2>
<p>For derivative-free local-optimization algorithms, the optimizer must somehow decide on some initial step size to perturb <i>x</i> by when it begins the optimization. This step size should be big enough that the value of the objective changes significantly, but not too big if you want to find the local optimum nearest to <i>x</i>. By default, NLopt chooses this initial step size heuristically from the bounds, tolerances, and other information, but this may not always be the best choice. </p>
<p> You can modify the initial step size by calling: </p>
<p> <code> nlopt_result nlopt_set_initial_step(nlopt_opt </code><i>opt</i><code>,</code><br />
 <code> const double* </code><i>dx</i><code>);</code> </p>
<p> Here, <i>dx</i> is an array of length <i>n</i> containing the (nonzero) initial step size for each component of the design parameters <i>x</i>. For convenience, if you want to set the step sizes in every direction to be the same value, you can instead call: </p>
<p> <code> nlopt_result nlopt_set_initial_step1(nlopt_opt </code><i>opt</i><code>,</code><br />
 <code> double </code><i>dx</i><code>);</code></p>
<h2>Stochastic Population</h2>
<p>Several of the stochastic search algorithms (e.g., CRS, MLSL, and ISRES) start by generating some initial &quot;population&quot; of random points <i>x</i>. By default, this initial population size is chosen heuristically in some algorithm-specific way, but the initial population can by changed by calling: </p>
<p> <code> nlopt_result nlopt_set_population(nlopt_opt </code><i>opt</i><code>,</code><br />
 <code> unsigned </code><i>pop</i><code>);</code> </p>
<p> (A <i>pop</i> of zero implies that the heuristic default will be used.)</p>
<h2>Pseudorandom Numbers</h2>
<p>For stochastic optimization algorithms, we use pseudorandom numbers generated by the Mersenne Twister algorithm, based on code from Makoto Matsumoto. By default, the seed for the random numbers is generated from the system time, so that they will be different each time you run the program. If you want to use deterministic random numbers, you can set the seed by calling: </p>
<p> <code> void nlopt_srand(unsigned long </code><i>seed</i><code>);</code> </p>
<p> Some of the algorithms also support using low-discrepancy sequences (LDS), sometimes known as quasi-random numbers. NLopt uses the Sobol LDS, which is implemented for up to 1111 dimensions.</p>
<h2>Authors</h2>
<p>Written by Steven G. Johnson. </p>
<p> Copyright (c) 2007-2014 Massachusetts Institute of Technology.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-nlopt_minimize/">nlopt_minimize</a>(3) </p>
