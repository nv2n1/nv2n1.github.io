---
title: "sc_batchelectrondensity(3)"
name: "sc_batchelectrondensity"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_batchelectrondensity/"
description: "sc::BatchElectronDensity –"
---

<p>sc::BatchElectronDensity &#8211; </p>
<p> This a more highly optimized than <code>ElectronDensity</code> since everything is precomputed.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;density.h&gt;</code></pre>
<p> Inherits <code>sc::Volume</code>.</p>
<h3>Public Types</h3>
<p>enum { X = 0, Y = 1, Z = 2 }</p>
<p>This gives the elements of gradient arrays.</p>
<p>enum { XX = 0, YX = 1, YY = 2, ZX = 3, ZY = 4, ZZ = 5 }</p>
<p>This gives the elements of hessian arrays.</p>
<p>Public Member Functions<br />
 <code>BatchElectronDensity</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;) </p>
<p> <code>BatchElectronDensity</code> (const <code>Ref</code>&lt; <code>Wavefunction</code> &gt; &amp;, double accuracy=DBL_EPSILON) </p>
<p> <code>BatchElectronDensity</code> (const <code>Ref</code>&lt; <code>BatchElectronDensity</code> &gt; &amp;d, bool reference_parent_data=false)<br />
 <i>This will construct copies of this. </i><br />
 virtual void <code>boundingbox</code> (double valuemin, double valuemax, <code>SCVector3</code> &amp;p1, <code>SCVector3</code> &amp;p2)<br />
 <i>Returns the bounding box. </i><br />
 void <code>clear</code> ()<br />
 <i>This will cause all stratch storage to be released. </i><br />
 void <code>compute_density</code> (const <code>SCVector3</code> &amp;r, double *alpha_density, double *alpha_density_grad, double *alpha_density_hessian, double *beta_density, double *beta_density_grad, double *beta_density_hessian)<br />
 <i>This is a alternate to the </i><code>Volume</code> interface that avoids some of the overhead of that interface.<br />
 virtual void <code>init</code> (bool initialize_density_matrices=true)<br />
 <i>This is called to finish initialization of the object. </i><br />
 virtual void <code>set_densities</code> (const <code>RefSymmSCMatrix</code> &amp;aden, const <code>RefSymmSCMatrix</code> &amp;bden)<br />
 <i>This will fill in the internel copies of the density matrices with new values. </i><br />
 void <code>set_linear_scaling</code> (bool b)<br />
 <i>Turn linear scaling algorithm on/off. </i><br />
 void <code>set_accuracy</code> (double a)<br />
 <i>Sets the accuracy. </i><br />
 void <code>set_use_dmat_bound</code> (bool b)<br />
 <i>Turn use of density matrix bounds on/off. </i> <code>DFT Support Members.</code><br />
 These return some of the internal data, some of which is only value after a density has been computed. This data is needed by the density functional theory code. </p>
<pre><code>double * alpha_density_matrix ()


Return the alpha density matrix.


double * beta_density_matrix ()


Return the beta density matrix.


int ncontrib ()



int * contrib ()



int ncontrib_bf ()



int * contrib_bf ()



double * bs_values ()



double * bsg_values ()



double * bsh_values ()



void set_need_basis_gradient (bool b)


To ensure that that the basis functions gradients are computed, use this.


void set_need_basis_hessian (bool b)



Protected Member Functions</code></pre>
<p> virtual void <code>init_common_data</code> (bool initialize_density_matrices) </p>
<p> virtual void <code>init_scratch_data</code> () </p>
<p> void <code>compute_basis_values</code> (const <code>SCVector3</code> &amp;r) </p>
<p> void <code>compute_spin_density</code> (const double *dmat, double *rho, double *grad, double *hess) </p>
<p> virtual void <code>compute</code> ()<br />
 <i>Recompute at least the results that have compute true and are not already computed. </i></p>
<h3>Protected Attributes</h3>
<p><code>Ref</code>&lt; <code>Wavefunction</code> &gt; <code>wfn_</code> </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>basis_</code> </p>
<p> double * <code>alpha_dmat_</code> </p>
<p> double * <code>beta_dmat_</code> </p>
<p> double * <code>dmat_bound_</code> </p>
<p> <code>ShellExtent</code> * <code>extent_</code> </p>
<p> <code>GaussianBasisSet::ValueData</code> * <code>valdat_</code> </p>
<p> int <code>ncontrib_</code> </p>
<p> int * <code>contrib_</code> </p>
<p> int <code>ncontrib_bf_</code> </p>
<p> int * <code>contrib_bf_</code> </p>
<p> double * <code>bs_values_</code> </p>
<p> double * <code>bsg_values_</code> </p>
<p> double * <code>bsh_values_</code> </p>
<p> int <code>nshell_</code> </p>
<p> int <code>nbasis_</code> </p>
<p> int <code>spin_polarized_</code> </p>
<p> int <code>linear_scaling_</code> </p>
<p> int <code>use_dmat_bound_</code> </p>
<p> bool <code>need_hessian_</code> </p>
<p> bool <code>need_gradient_</code> </p>
<p> bool <code>need_basis_hessian_</code> </p>
<p> bool <code>need_basis_gradient_</code> </p>
<p> bool <code>using_shared_data_</code> </p>
<p> double <code>accuracy_</code></p>
<h2>Detailed Description</h2>
<p>This a more highly optimized than <code>ElectronDensity</code> since everything is precomputed. </p>
<p> However, it cannot be used if the density and/or geometry might change between computations of the density or bounding box, unless the obsolete member is called.</p>
<h2>Member Enumeration Documentation</h2>
<h3>anonymous enum</h3>
<p>This gives the elements of hessian arrays.</p>
<h3>anonymous enum</h3>
<p>This gives the elements of gradient arrays.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::BatchElectronDensity::BatchElectronDensity (const <code>Ref</code>&lt; <code>BatchElectronDensity</code> &gt; &amp; d, bool reference_parent_data = false)</h3>
<p>This will construct copies of this. If reference_parent_data is true, then data that do not change, such as the density matrices and shell extent, are referenced rather than copied. In this case, the original object that allocated this items must be valid while copied objects are used to compute densities. Also d must have already been intialized and the resulting copy is already initialized (and cannot be reinitialized). </p>
<p> If reference_parent_data is false, then init must be called on this object before it is used.</p>
<h2>Member Function Documentation</h2>
<h3>double* sc::BatchElectronDensity::alpha_density_matrix () [inline]</h3>
<p>Return the alpha density matrix.</p>
<h3>double* sc::BatchElectronDensity::beta_density_matrix () [inline]</h3>
<p>Return the beta density matrix.</p>
<h3>virtual void sc::BatchElectronDensity::boundingbox (double valuemin, double valuemax, <code>SCVector3</code> &amp; p1, <code>SCVector3</code> &amp; p2) [virtual]</h3>
<p>Returns the bounding box. </p>
<p> Implements <code>sc::Volume</code>.</p>
<h3>void sc::BatchElectronDensity::clear ()</h3>
<p>This will cause all stratch storage to be released.</p>
<h3>virtual void sc::BatchElectronDensity::compute () [protected, virtual]</h3>
<p>Recompute at least the results that have compute true and are not already computed. This should only be called by Result&#8217;s members. </p>
<p> Implements <code>sc::Volume</code>.</p>
<h3>void sc::BatchElectronDensity::compute_density (const <code>SCVector3</code> &amp; r, double * alpha_density, double * alpha_density_grad, double * alpha_density_hessian, double * beta_density, double * beta_density_grad, double * beta_density_hessian)</h3>
<p>This is a alternate to the <code>Volume</code> interface that avoids some of the overhead of that interface.</p>
<h3>virtual void sc::BatchElectronDensity::init (bool initialize_density_matrices = true) [virtual]</h3>
<p>This is called to finish initialization of the object. It must not be called with objects that created in a way that they share parent data, those objects are initialized when they are constructed. This member is usually called automatically, however, if it will be used to initial other objects that share parent data, then it must be initialized first and this return is the way to do that. If initialize_density_matrices is false, then the density matrices will be allocated, but not filled in. They must be later filled in with set_densities.</p>
<h3>void sc::BatchElectronDensity::set_accuracy (double a) [inline]</h3>
<p>Sets the accuracy.</p>
<h3>virtual void sc::BatchElectronDensity::set_densities (const <code>RefSymmSCMatrix</code> &amp; aden, const <code>RefSymmSCMatrix</code> &amp; bden) [virtual]</h3>
<p>This will fill in the internel copies of the density matrices with new values. aden is the alpha density matrix and bden is the beta density matrix. bden is ignored if the wavefunction is not spin polarized.</p>
<h3>void sc::BatchElectronDensity::set_linear_scaling (bool b) [inline]</h3>
<p>Turn linear scaling algorithm on/off. The effect of this will be delayed until the next time <code>init()</code> is called.</p>
<h3>void sc::BatchElectronDensity::set_need_basis_gradient (bool b) [inline]</h3>
<p>To ensure that that the basis functions gradients are computed, use this.</p>
<h3>void sc::BatchElectronDensity::set_use_dmat_bound (bool b) [inline]</h3>
<p>Turn use of density matrix bounds on/off.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
