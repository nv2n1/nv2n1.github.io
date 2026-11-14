---
title: "sc_gaussianshell(3)"
name: "sc_gaussianshell"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_gaussianshell/"
description: "sc::GaussianShell –"
---

<p>sc::GaussianShell &#8211; </p>
<p> A Gaussian orbital shell.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;gaussshell.h&gt;</code></pre>
<p> Inherits <code>sc::SavableState</code>.</p>
<h3>Public Types</h3>
<p>enum <code>PrimitiveType</code> { <code>Normalized</code>, <code>Unnormalized</code> } </p>
<p> enum <code>GaussianType</code> { <code>Cartesian</code>, <code>Pure</code> }</p>
<h3>Public Member Functions</h3>
<p><code>GaussianShell</code> (int ncn, int nprm, double *e, int *am, int *pure, double **c, PrimitiveType pt=GaussianShell::Normalized, bool do_normalize_shell=true)<br />
 <i>A </i><code>GaussianShell</code> constructor.<br />
 <code>GaussianShell</code> (int ncn, int nprm, double *e, int *am, GaussianType pure, double **c, PrimitiveType pt=GaussianShell::Normalized)<br />
 <i>A </i><code>GaussianShell</code> constructor.<br />
 <code>GaussianShell</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)<br />
 <i>Construct a </i><code>GaussianShell</code> from <code>KeyVal</code> input.<br />
 <code>GaussianShell</code> (<code>StateIn</code> &amp;)<br />
 <i>Restore a </i><code>GaussianShell</code> from a <code>StateIn</code> object.<br />
 <code>GaussianShell</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;, int pure)<br />
 <i>Construct a </i><code>GaussianShell</code> from <code>KeyVal</code> input.<br />
 void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 int <code>nprimitive</code> () const<br />
 <i>The number of primitive Gaussian shells. </i><br />
 int <code>ncontraction</code> () const<br />
 <i>The number of contractions formed from the primitives. </i><br />
 int <code>nfunction</code> () const<br />
 <i>The number of basis functions. </i><br />
 int <code>max_angular_momentum</code> () const<br />
 <i>The maximum angular momentum in the shell. </i><br />
 int <code>min_angular_momentum</code> () const<br />
 <i>The minimum angular momentum in the shell. </i><br />
 int <code>max_cartesian</code> () const<br />
 <i>The maximum number of Cartesian functions in any contraction. </i><br />
 int <code>am</code> (int con) const<br />
 <i>The angular momentum of the given contraction. </i><br />
 int <code>max_am</code> () const<br />
 <i>The maximum angular momentum of any contraction. </i><br />
 int <code>min_am</code> () const<br />
 <i>The minimum angular momentum of any contraction. </i><br />
 char <code>amchar</code> (int con) const<br />
 <i>The character symbol for the angular momentum of the given contraction. </i><br />
 int <code>nfunction</code> (int con) const<br />
 <i>The number of basis functions coming from the given contraction. </i><br />
 int <code>ncartesian</code> () const<br />
 <i>The total number of functions if this shell was Cartesian. </i><br />
 int <code>ncartesian_with_aminc</code> (int aminc) const<br />
 <i>The total number of Cartesian functions if this shift is applied to all of the angular momentums. </i><br />
 int <code>ncartesian</code> (int con) const<br />
 <i>The number of Cartesian functions for the given contraction. </i><br />
 int <code>is_cartesian</code> (int con) const<br />
 <i>Returns nonzero if contraction con is Cartesian. </i><br />
 int <code>is_pure</code> (int con) const<br />
 <i>Returns nonzero if contraction con is solid harmonics. </i><br />
 int <code>has_pure</code> () const<br />
 <i>Returns nonzero if any contraction is solid harmonics. </i><br />
 double <code>coefficient_unnorm</code> (int con, int prim) const<br />
 <i>Returns the contraction coef for unnormalized primitives. </i><br />
 double <code>coefficient_norm</code> (int con, int prim) const<br />
 <i>Returns the contraction coef for normalized primitives. </i><br />
 double <code>exponent</code> (int iprim) const<br />
 <i>Returns the exponent of the given primitive. </i><br />
 int <code>values</code> (<code>CartesianIter</code> **, <code>SphericalTransformIter</code> **, const <code>SCVector3</code> &amp;r, double *basis_values)<br />
 <i></i><code>Compute</code> the values for this shell at position r.<br />
 int <code>grad_values</code> (<code>CartesianIter</code> **, <code>SphericalTransformIter</code> **, const <code>SCVector3</code> &amp;R, double *g_values, double *basis_values=0) const<br />
 <i>Like values(. </i><br />
 int <code>hessian_values</code> (<code>CartesianIter</code> **, <code>SphericalTransformIter</code> **, const <code>SCVector3</code> &amp;R, double *h_values, double *g_values=0, double *basis_values=0) const<br />
 <i>Like values(. </i><br />
 double <code>relative_overlap</code> (const <code>Ref</code>&lt; <code>Integral</code> &gt; &amp;, int con, int func1, int func2) const<br />
 <i>Returns the intra-generalized-contraction overlap matrix element &lt;con func1|con func2&gt; within an arbitrary constant for the shell. </i><br />
 double <code>relative_overlap</code> (int con, int a1, int b1, int c1, int a2, int b2, int c2) const<br />
 <i>Returns the intra-generalized-contraction overlap matrix element &lt;con func1|con func2&gt; within an arbitrary constant for the shell. </i><br />
 int <code>equiv</code> (const <code>GaussianShell</code> *s)<br />
 <i>Returns true if this and the argument are equivalent. </i><br />
 double <code>extent</code> (double threshold) const<br />
 <i>Returns a radius. </i><br />
 double <code>monobound</code> (double r) const<br />
 <i>Returns a bound for the basis function. </i><br />
 void <code>print</code> (std::ostream &amp;=ExEnv::out0()) const<br />
 <i>Print the object. </i></p>
<h2>Detailed Description</h2>
<p>A Gaussian orbital shell.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::GaussianShell::GaussianShell (int ncn, int nprm, double * e, int * am, int * pure, double ** c, PrimitiveType pt = GaussianShell::Normalized, bool do_normalize_shell = true)</h3>
<p>A <code>GaussianShell</code> constructor. Users of <code>GaussianShell</code> must pass pointers to newed memory that is kept by <code>GaussianShell</code> and deleted by the destructor. The arguments for the following ctor are: </p>
<dl>
<dt>*</p>
<dd>ncn is the number of contracted functions (1 except for SP and gen. con.)</p>
<dt>*</p>
<dd>nprm is the number of primitives</p>
<dt>*</p>
<dd>e gives the exponents (length nprm)</p>
<dt>*</p>
<dd>am gives the angular momentum (length ncn)</p>
<dt>*</p>
<dd>pure is 1 for pure am and 0 for cartesian (length ncn)</p>
<dt>*</p>
<dd>c are the contraction coefficients (length ncn by nprm)</p>
<dt>*</p>
<dd>pt describes whether the primitive functions are to be considered normalized or unnormalized. This effects whether or not c is manipulated to give the correct normalization.</p>
<dt>*</p>
<dd>If do_normalize_shell is true (the default), then the shell normalization constants will be folded into the coefficients.</dl>
<h3>sc::GaussianShell::GaussianShell (int ncn, int nprm, double * e, int * am, GaussianType pure, double ** c, PrimitiveType pt = GaussianShell::Normalized)</h3>
<p>A <code>GaussianShell</code> constructor. In this ctor pure is either GaussianShell::Cartesian or Gaussian::Pure and all of the contracted functions are treated in that way. (The user doesn\&#8217;t need to compute generate a int*pure vector in this case.)</p>
<h3>sc::GaussianShell::GaussianShell (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;, int pure)</h3>
<p>Construct a <code>GaussianShell</code> from <code>KeyVal</code> input. If pure is nonzero Cartesian functions will be used, otherwise, solid harmonics will be used.</p>
<h2>Member Function Documentation</h2>
<h3>double sc::GaussianShell::extent (double threshold) const</h3>
<p>Returns a radius. All functions in the shell are below threshold outside this radius.</p>
<h3>int sc::GaussianShell::grad_values (<code>CartesianIter</code> **, <code>SphericalTransformIter</code> **, const <code>SCVector3</code> &amp; R, double * g_values, double * basis_values = 0) const</h3>
<p>Like values(. ..), but computes gradients of the basis function values, too.</p>
<h3>int sc::GaussianShell::hessian_values (<code>CartesianIter</code> **, <code>SphericalTransformIter</code> **, const <code>SCVector3</code> &amp; R, double * h_values, double * g_values = 0, double * basis_values = 0) const</h3>
<p>Like values(. ..), but computes first and second derivatives of the basis function values, too.</p>
<h3>double sc::GaussianShell::monobound (double r) const</h3>
<p>Returns a bound for the basis function. This bound is defined so that it is positive and monotonically decreasing as a function of r.</p>
<h3>int sc::GaussianShell::ncartesian_with_aminc (int aminc) const</h3>
<p>The total number of Cartesian functions if this shift is applied to all of the angular momentums.</p>
<h3>double sc::GaussianShell::relative_overlap (int con, int a1, int b1, int c1, int a2, int b2, int c2) const</h3>
<p>Returns the intra-generalized-contraction overlap matrix element &lt;con func1|con func2&gt; within an arbitrary constant for the shell. func1 and func2 are determined according to the axis exponents, a1, b1, c1, a2, b2, and c2.</p>
<h3>double sc::GaussianShell::relative_overlap (const <code>Ref</code>&lt; <code>Integral</code> &gt; &amp;, int con, int func1, int func2) const</h3>
<p>Returns the intra-generalized-contraction overlap matrix element &lt;con func1|con func2&gt; within an arbitrary constant for the shell.</p>
<h3>void sc::GaussianShell::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SavableState</code>.</p>
<h3>int sc::GaussianShell::values (<code>CartesianIter</code> **, <code>SphericalTransformIter</code> **, const <code>SCVector3</code> &amp; r, double * basis_values)</h3>
<p><code>Compute</code> the values for this shell at position r. The basis_values argument must be vector of length <code>nfunction()</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
