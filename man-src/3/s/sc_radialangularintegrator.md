---
title: "sc_radialangularintegrator(3)"
name: "sc_radialangularintegrator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_radialangularintegrator/"
description: "sc::RadialAngularIntegrator –"
---

<p>sc::RadialAngularIntegrator &#8211; </p>
<p> An implementation of an integrator using any combination of a <code>RadialIntegrator</code> and an <code>AngularIntegrator</code>.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;integrator.h&gt;</code></pre>
<p> Inherits <code>sc::DenIntegrator</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>RadialAngularIntegrator (const Ref&lt; KeyVal &gt; &amp;)


Construct a RadialAngularIntegrator from KeyVal input.


RadialAngularIntegrator (StateIn &amp;)



void save_data_state (StateOut &amp;)


Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.


void integrate (const Ref&lt; DenFunctional &gt; &amp;, const RefSymmSCMatrix &amp;densa=0, const RefSymmSCMatrix &amp;densb=0, double *nuclear_gradient=0)


Performs the integration of the given functional using the given alpha and beta density matrices.


void print (std::ostream &amp;=ExEnv::out0()) const


Print the object.


AngularIntegrator * get_angular_grid (double radius, double atomic_radius, int charge, int deriv_order)



RadialIntegrator * get_radial_grid (int charge, int deriv_order)



void init_default_grids (void)



int angular_grid_offset (int i)



void set_grids (void)



int get_atomic_row (int i)



void init_parameters (void)



void init_parameters (const Ref&lt; KeyVal &gt; &amp;keyval)



void init_pruning_coefficients (const Ref&lt; KeyVal &gt; &amp;keyval)



void init_pruning_coefficients (void)



void init_alpha_coefficients (void)



int select_dynamic_grid (void)



Ref&lt; IntegrationWeight &gt; weight ()



Protected Attributes</code></pre>
<p> <code>Ref</code>&lt; <code>IntegrationWeight</code> &gt; <code>weight_</code> </p>
<p> <code>Ref</code>&lt; <code>RadialIntegrator</code> &gt; <code>radial_user_</code> </p>
<p> <code>Ref</code>&lt; <code>AngularIntegrator</code> &gt; <code>angular_user_</code> </p>
<p> <code>Ref</code>&lt; <code>AngularIntegrator</code> &gt; *** <code>angular_grid_</code> </p>
<p> <code>Ref</code>&lt; <code>RadialIntegrator</code> &gt; ** <code>radial_grid_</code></p>
<h2>Detailed Description</h2>
<p>An implementation of an integrator using any combination of a <code>RadialIntegrator</code> and an <code>AngularIntegrator</code>.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::RadialAngularIntegrator::RadialAngularIntegrator (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p>Construct a <code>RadialAngularIntegrator</code> from <code>KeyVal</code> input. The accepted keyword are listed below. The most important keyword is grid. The dynamic and prune_grid options may be of occassional interest.</p>
<dl>
<dt>grid</p>
<dd>Specifies the fineness of the grid. Possible values are xcoarse, coarse, medium, fine, xfine, and ultrafine, in order of increasing accuracy and cost. The default is fine.</dl>
<dl>
<dt>dynamic</p>
<dd>This gives a boolean value that, if true, will cause the grids to start out coarse, and approach the requested grid value as more accuracy is required, when the calculation is close to convergence. The default is true.</dl>
<dl>
<dt>prune_grid</p>
<dd>This gives a boolean value that, if true, will cause more course angular grids to be used near nuclei. The default is true. When this is true, further control over pruning can be obtained with the angular_points and alpha_coeffs keywords.</dl>
<dl>
<dt>radial</p>
<dd>Specifies the <code>RadialIntegrator</code> object. If this is given, then specifying the grid and dynamic keywords will not affect the radial grid. The default is controlled by other options, but is always one of several <code>EulerMaclaurinRadialIntegrator</code> objects.</dl>
<dl>
<dt>angular</p>
<dd>Specifies the <code>AngularIntegrator</code> object. If this is given, then specifying the grid, prune_grid, and dynamic keywords will not affect the angular grid. The default is controlled by other options, but is always one of several <code>LebedevLaikovIntegrator</code> objects.</dl>
<dl>
<dt>weight</p>
<dd>Specifies the <code>IntegrationWeight</code> object. The default is <code>BeckeIntegrationWeight</code>.</dl>
<h2>Member Function Documentation</h2>
<h3>void sc::RadialAngularIntegrator::integrate (const <code>Ref</code>&lt; <code>DenFunctional</code> &gt; &amp;, const <code>RefSymmSCMatrix</code> &amp; densa = 0, const <code>RefSymmSCMatrix</code> &amp; densb = 0, double * nuclear_grad = 0) [virtual]</h3>
<p>Performs the integration of the given functional using the given alpha and beta density matrices. The nuclear derivative <code>contribution</code> is placed in nuclear_grad, if it is non-null. </p>
<p> Implements <code>sc::DenIntegrator</code>.</p>
<h3>void sc::RadialAngularIntegrator::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::DenIntegrator</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
