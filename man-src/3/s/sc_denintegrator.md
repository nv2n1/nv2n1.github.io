---
title: "sc_denintegrator(3)"
name: "sc_denintegrator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_denintegrator/"
description: "sc::DenIntegrator –"
---

<p>sc::DenIntegrator &#8211; </p>
<p> An abstract base class for integrating the electron density.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;integrator.h&gt;</code></pre>
<p> Inherits <code>sc::SavableState</code>. Inherited by <code>sc::RadialAngularIntegrator</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>DenIntegrator ()


Construct a new DenIntegrator.


DenIntegrator (const Ref&lt; KeyVal &gt; &amp;)


Construct a new DenIntegrator given the KeyVal input.


DenIntegrator (StateIn &amp;)


Construct a new DenIntegrator given the StateIn data.


void save_data_state (StateOut &amp;)


Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.


Ref&lt; Wavefunction &gt; wavefunction () const


Returns the wavefunction used for the integration.


double value () const


Returns the result of the integration.


void set_accuracy (double a)


Sets the accuracy to use in the integration.


double get_accuracy (void)



void set_compute_potential_integrals (int)


Call with non zero if the potential integrals are to be computed.


const double * alpha_vmat () const


Returns the alpha potential integrals.


const double * beta_vmat () const


Returns the beta potential integrals.


virtual void init (const Ref&lt; Wavefunction &gt; &amp;)


Called before integrate.


virtual void done ()


Must be called between calls to init.


virtual void integrate (const Ref&lt; DenFunctional &gt; &amp;, const RefSymmSCMatrix &amp;densa=0, const RefSymmSCMatrix &amp;densb=0, double *nuclear_grad=0)=0


Performs the integration of the given functional using the given alpha and beta density matrices.



Protected Member Functions
void init_integration (const Ref&lt; DenFunctional &gt; &amp;func, const RefSymmSCMatrix &amp;densa, const RefSymmSCMatrix &amp;densb, double *nuclear_gradient)



void done_integration ()



void init_object ()



Protected Attributes</code></pre>
<p> <code>Ref</code>&lt; <code>Wavefunction</code> &gt; <code>wfn_</code> </p>
<p> <code>Ref</code>&lt; <code>BatchElectronDensity</code> &gt; <code>den_</code> </p>
<p> <code>Ref</code>&lt; <code>ThreadGrp</code> &gt; <code>threadgrp_</code> </p>
<p> <code>Ref</code>&lt; <code>MessageGrp</code> &gt; <code>messagegrp_</code> </p>
<p> double <code>value_</code> </p>
<p> double <code>accuracy_</code> </p>
<p> double * <code>alpha_vmat_</code> </p>
<p> double * <code>beta_vmat_</code> </p>
<p> int <code>spin_polarized_</code> </p>
<p> int <code>need_density_</code> </p>
<p> double <code>density_</code> </p>
<p> int <code>nbasis_</code> </p>
<p> int <code>nshell_</code> </p>
<p> int <code>n_integration_center_</code> </p>
<p> int <code>natom_</code> </p>
<p> int <code>compute_potential_integrals_</code> </p>
<p> int <code>linear_scaling_</code> </p>
<p> int <code>use_dmat_bound_</code></p>
<h2>Detailed Description</h2>
<p>An abstract base class for integrating the electron density.</p>
<h2>Member Function Documentation</h2>
<h3>const double* sc::DenIntegrator::alpha_vmat () const [inline]</h3>
<p>Returns the alpha potential integrals. Stored as the lower triangular, row-major format.</p>
<h3>const double* sc::DenIntegrator::beta_vmat () const [inline]</h3>
<p>Returns the beta potential integrals. Stored as the lower triangular, row-major format.</p>
<h3>virtual void sc::DenIntegrator::init (const <code>Ref</code>&lt; <code>Wavefunction</code> &gt; &amp;) [virtual]</h3>
<p>Called before integrate. Does not need to be called again unless the geometry changes or done is called.</p>
<h3>virtual void sc::DenIntegrator::integrate (const <code>Ref</code>&lt; <code>DenFunctional</code> &gt; &amp;, const <code>RefSymmSCMatrix</code> &amp; densa = 0, const <code>RefSymmSCMatrix</code> &amp; densb = 0, double * nuclear_grad = 0) [pure virtual]</h3>
<p>Performs the integration of the given functional using the given alpha and beta density matrices. The nuclear derivative <code>contribution</code> is placed in nuclear_grad, if it is non-null. </p>
<p> Implemented in <code>sc::RadialAngularIntegrator</code>.</p>
<h3>void sc::DenIntegrator::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SavableState</code>. </p>
<p> Reimplemented in <code>sc::RadialAngularIntegrator</code>.</p>
<h3>void sc::DenIntegrator::set_compute_potential_integrals (int)</h3>
<p>Call with non zero if the potential integrals are to be computed. They can be returned with the vmat() member.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
