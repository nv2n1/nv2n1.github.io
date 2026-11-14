---
title: "sc_denfunctional(3)"
name: "sc_denfunctional"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_denfunctional/"
description: "sc::DenFunctional –"
---

<p>sc::DenFunctional &#8211; </p>
<p> An abstract base class for density functionals.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;functional.h&gt;</code></pre>
<p> Inherits <code>sc::SavableState</code>. Inherited by <code>sc::Becke88XFunctional</code>, <code>sc::G96XFunctional</code>, <code>sc::LSDACFunctional</code>, <code>sc::LYPCFunctional</code>, <code>sc::mPW91XFunctional</code>, <code>sc::NElFunctional</code>, <code>sc::NewP86CFunctional</code>, <code>sc::P86CFunctional</code>, <code>sc::PBECFunctional</code>, <code>sc::PBEXFunctional</code>, <code>sc::PW86XFunctional</code>, <code>sc::PW91CFunctional</code>, <code>sc::PW91XFunctional</code>, <code>sc::SlaterXFunctional</code>, <code>sc::SumDenFunctional</code>, and <code>sc::XalphaFunctional</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>DenFunctional (const Ref&lt; KeyVal &gt; &amp;)



DenFunctional (StateIn &amp;)



void save_data_state (StateOut &amp;)


Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.


virtual void set_spin_polarized (int i)



virtual void set_compute_potential (int i)



virtual int need_density_gradient ()



virtual int need_density_hessian ()



virtual void point (const PointInputData &amp;, PointOutputData &amp;)=0



void gradient (const PointInputData &amp;, PointOutputData &amp;, double *gradient, int acenter, GaussianBasisSet *basis, const double *dmat_a, const double *dmat_b, int ncontrib, const int *contrib, int ncontrib_bf, const int *contrib_bf, const double *bs_values, const double *bsg_values, const double *bsh_values)



virtual double a0 () const


Returns the fraction of Hartee-Fock exchange to be included.


void fd_point (const PointInputData &amp;, PointOutputData &amp;)



int test (const PointInputData &amp;)



int test ()



Protected Member Functions
void do_fd_point (PointInputData &amp;id, double &amp;in, double &amp;out, double lower_bound, double upper_bound)



Protected Attributes
int spin_polarized_



int compute_potential_



double a0_</code></pre>
<h2>Detailed Description</h2>
<p>An abstract base class for density functionals.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::DenFunctional::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SavableState</code>. </p>
<p> Reimplemented in <code>sc::NElFunctional</code>, <code>sc::SumDenFunctional</code>, <code>sc::StdDenFunctional</code>, <code>sc::LSDACFunctional</code>, <code>sc::PBECFunctional</code>, <code>sc::PW91CFunctional</code>, <code>sc::P86CFunctional</code>, <code>sc::NewP86CFunctional</code>, <code>sc::SlaterXFunctional</code>, <code>sc::VWNLCFunctional</code>, <code>sc::VWN1LCFunctional</code>, <code>sc::VWN2LCFunctional</code>, <code>sc::VWN3LCFunctional</code>, <code>sc::VWN4LCFunctional</code>, <code>sc::VWN5LCFunctional</code>, <code>sc::PW92LCFunctional</code>, <code>sc::PZ81LCFunctional</code>, <code>sc::XalphaFunctional</code>, <code>sc::Becke88XFunctional</code>, <code>sc::LYPCFunctional</code>, <code>sc::PW86XFunctional</code>, <code>sc::PBEXFunctional</code>, <code>sc::PW91XFunctional</code>, <code>sc::mPW91XFunctional</code>, and <code>sc::G96XFunctional</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
