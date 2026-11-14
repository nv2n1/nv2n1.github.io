---
title: "sc_gausslegendreangularintegrator(3)"
name: "sc_gausslegendreangularintegrator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_gausslegendreangularintegrator/"
description: "sc::GaussLegendreAngularIntegrator –"
---

<p>sc::GaussLegendreAngularIntegrator &#8211; </p>
<p> An implementation of an angular integrator using the Gauss-Legendre weights and grid points.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;integrator.h&gt;</code></pre>
<p> Inherits <code>sc::AngularIntegrator</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>GaussLegendreAngularIntegrator (const Ref&lt; KeyVal &gt; &amp;)


Contract a GaussLegendreAngularIntegrator from KeyVal input.


GaussLegendreAngularIntegrator (StateIn &amp;)



void save_data_state (StateOut &amp;)


Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.


int num_angular_points (double r_value, int ir)



double angular_point_cartesian (int iangular, double r, SCVector3 &amp;integration_point) const



void print (std::ostream &amp;=ExEnv::out0()) const


Print the object.



Protected Member Functions
int get_ntheta (void) const



void set_ntheta (int i)



int get_nphi (void) const



void set_nphi (int i)



int get_Ktheta (void) const



void set_Ktheta (int i)



int get_ntheta_r (void) const



void set_ntheta_r (int i)



int get_nphi_r (void) const



void set_nphi_r (int i)



int get_Ktheta_r (void) const



void set_Ktheta_r (int i)



int nw (void) const



double sin_theta (SCVector3 &amp;point) const



void gauleg (double x1, double x2, int n)



Protected Attributes
int ntheta_



int nphi_



int Ktheta_



int ntheta_r_



int nphi_r_



int Ktheta_r_



double * theta_quad_weights_



double * theta_quad_points_</code></pre>
<h2>Detailed Description</h2>
<p>An implementation of an angular integrator using the Gauss-Legendre weights and grid points.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::GaussLegendreAngularIntegrator::GaussLegendreAngularIntegrator (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p>Contract a <code>GaussLegendreAngularIntegrator</code> from <code>KeyVal</code> input. This class is for testing, the <code>LebedevLaikovIntegrator</code> is preferred for normal use. The following parameters are read: ntheta, nphi, and Ktheta.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::GaussLegendreAngularIntegrator::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::AngularIntegrator</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
