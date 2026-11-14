---
title: "sc_integralcca(3)"
name: "sc_integralcca"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_integralcca/"
description: "sc::IntegralCCA –"
---

<p>sc::IntegralCCA &#8211; </p>
<p> <code>IntegralCCA</code> provides an SC client for CCA IntegralEvaluator components.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;intcca.h&gt;</code></pre>
<p> Inherits <code>sc::Integral</code>.</p>
<h3>Public Member Functions</h3>
<p><code>IntegralCCA</code> (IntegralEvaluatorFactory eval_factory, bool use_opaque, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;b1=0, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;b2=0, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;b3=0, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;b4=0)<br />
 <i>This constructor is used when the framework is not embedded. </i><br />
 <code>IntegralCCA</code> (<code>StateIn</code> &amp;) </p>
<p> <code>IntegralCCA</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)<br />
 <i>The </i><code>KeyVal</code> constructor.<br />
 void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 <code>Integral</code> * <code>clone</code> ()<br />
 <i>Clones the given </i><code>Integral</code> factory. The new factory may need to have set_basis and set_storage to be called on it.<br />
 <code>CartesianIter</code> * <code>new_cartesian_iter</code> (int)<br />
 <i>Return a </i><code>CartesianIter</code> object.<br />
 <code>RedundantCartesianIter</code> * <code>new_redundant_cartesian_iter</code> (int)<br />
 <i>Return a </i><code>RedundantCartesianIter</code> object.<br />
 <code>RedundantCartesianSubIter</code> * <code>new_redundant_cartesian_sub_iter</code> (int)<br />
 <i>Return a </i><code>RedundantCartesianSubIter</code> object.<br />
 <code>SphericalTransformIter</code> * <code>new_spherical_transform_iter</code> (int l, int inv=0, int subl=-1)<br />
 <i>Return a </i><code>SphericalTransformIter</code> object.<br />
 const <code>SphericalTransform</code> * <code>spherical_transform</code> (int l, int inv=0, int subl=-1)<br />
 <i>Return a </i><code>SphericalTransform</code> object.<br />
 <code>Ref</code>&lt; <code>OneBodyInt</code> &gt; <code>overlap</code> ()<br />
 <i>Return a </i><code>OneBodyInt</code> that computes the overlap.<br />
 <code>Ref</code>&lt; <code>OneBodyInt</code> &gt; <code>kinetic</code> ()<br />
 <i>Return a </i><code>OneBodyInt</code> that computes the kinetic energy.<br />
 <code>Ref</code>&lt; <code>OneBodyInt</code> &gt; <code>point_charge</code> (const <code>Ref</code>&lt; <code>PointChargeData</code> &gt; &amp;=0)<br />
 <i>Return a </i><code>OneBodyInt</code> that computes the integrals for interactions with <code>point</code> charges.<br />
 <code>Ref</code>&lt; <code>OneBodyInt</code> &gt; <code>nuclear</code> ()<br />
 <i>Return a </i><code>OneBodyInt</code> that computes the nuclear repulsion integrals.<br />
 <code>Ref</code>&lt; <code>OneBodyInt</code> &gt; <code>hcore</code> ()<br />
 <i>Return a </i><code>OneBodyInt</code> that computes the core Hamiltonian integrals.<br />
 <code>Ref</code>&lt; <code>OneBodyInt</code> &gt; <code>efield_dot_vector</code> (const <code>Ref</code>&lt; <code>EfieldDotVectorData</code> &gt; &amp;=0)<br />
 <i>Return a </i><code>OneBodyInt</code> that computes the electric field integrals dotted with a given vector.<br />
 <code>Ref</code>&lt; <code>OneBodyInt</code> &gt; <code>dipole</code> (const <code>Ref</code>&lt; <code>DipoleData</code> &gt; &amp;=0)<br />
 <i>Return a </i><code>OneBodyInt</code> that computes electric dipole moment integrals.<br />
 <code>Ref</code>&lt; <code>OneBodyInt</code> &gt; <code>quadrupole</code> (const <code>Ref</code>&lt; <code>DipoleData</code> &gt; &amp;=0)<br />
 <i>Return a </i><code>OneBodyInt</code> that computes electric quadrupole moment integrals.<br />
 <code>Ref</code>&lt; <code>OneBodyDerivInt</code> &gt; <code>overlap_deriv</code> ()<br />
 <i>Return a </i><code>OneBodyDerivInt</code> that computes overlap derivatives.<br />
 <code>Ref</code>&lt; <code>OneBodyDerivInt</code> &gt; <code>kinetic_deriv</code> ()<br />
 <i>Return a </i><code>OneBodyDerivInt</code> that computes kinetic energy derivatives.<br />
 <code>Ref</code>&lt; <code>OneBodyDerivInt</code> &gt; <code>nuclear_deriv</code> ()<br />
 <i>Return a </i><code>OneBodyDerivInt</code> that computes nuclear repulsion derivatives.<br />
 <code>Ref</code>&lt; <code>OneBodyDerivInt</code> &gt; <code>hcore_deriv</code> ()<br />
 <i>Return a </i><code>OneBodyDerivInt</code> that computes core Hamiltonian derivatives.<br />
 <code>Ref</code>&lt; <code>TwoBodyInt</code> &gt; <code>electron_repulsion</code> ()<br />
 <i>Return a </i><code>TwoBodyInt</code> that computes electron repulsion integrals.<br />
 <code>Ref</code>&lt; <code>TwoBodyDerivInt</code> &gt; <code>electron_repulsion_deriv</code> ()<br />
 <i>Return a </i><code>TwoBodyDerivInt</code> that computes electron repulsion derivatives.<br />
 void <code>set_basis</code> (const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;b1, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;b2=0, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;b3=0, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;b4=0)<br />
 <i>Set the basis set for each center. </i></p>
<h2>Detailed Description</h2>
<p><code>IntegralCCA</code> provides an SC client for CCA IntegralEvaluator components.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::IntegralCCA::IntegralCCA (IntegralEvaluatorFactory eval_factory, bool use_opaque, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp; b1 = 0, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp; b2 = 0, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp; b3 = 0, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp; b4 = 0)</h3>
<p>This constructor is used when the framework is not embedded.</p>
<h3>sc::IntegralCCA::IntegralCCA (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p>The <code>KeyVal</code> constructor. This constructor is used when the framework is embedded. The following keywords are read: </p>
<dl>
<dt>evaluator_factory</p>
<dd>This gives the symbol name of a CCA IntegralEvaluatorFactory component. This symbol name should also appear in the cca-load argument. The default is MPQC.IntegralEvaluatorFactory.</dl>
<dl>
<dt>integral_package</p>
<dd>If the default MPQC.IntegralEvaluatorFactory is used, then this option may be used to specify the integrals package to use (intv3 or cints). The default is intv3.</dl>
<dl>
<dt>molecule</p>
<dd>This gives a molecule object, it is required.</dl>
<h2>Member Function Documentation</h2>
<h3><code>Ref</code>&lt;<code>OneBodyInt</code>&gt; sc::IntegralCCA::dipole (const <code>Ref</code>&lt; <code>DipoleData</code> &gt; &amp; = 0) [virtual]</h3>
<p>Return a <code>OneBodyInt</code> that computes electric dipole moment integrals. The canonical order of integrals in a set is x, y, z. </p>
<p> Implements <code>sc::Integral</code>.</p>
<h3><code>Ref</code>&lt;<code>OneBodyInt</code>&gt; sc::IntegralCCA::efield_dot_vector (const <code>Ref</code>&lt; <code>EfieldDotVectorData</code> &gt; &amp; = 0) [virtual]</h3>
<p>Return a <code>OneBodyInt</code> that computes the electric field integrals dotted with a given vector. </p>
<p> Implements <code>sc::Integral</code>.</p>
<h3><code>CartesianIter</code>* sc::IntegralCCA::new_cartesian_iter (int) [virtual]</h3>
<p>Return a <code>CartesianIter</code> object. The caller is responsible for freeing the object. </p>
<p> Implements <code>sc::Integral</code>.</p>
<h3><code>RedundantCartesianIter</code>* sc::IntegralCCA::new_redundant_cartesian_iter (int) [virtual]</h3>
<p>Return a <code>RedundantCartesianIter</code> object. The caller is responsible for freeing the object. </p>
<p> Implements <code>sc::Integral</code>.</p>
<h3><code>RedundantCartesianSubIter</code>* sc::IntegralCCA::new_redundant_cartesian_sub_iter (int) [virtual]</h3>
<p>Return a <code>RedundantCartesianSubIter</code> object. The caller is responsible for freeing the object. </p>
<p> Implements <code>sc::Integral</code>.</p>
<h3><code>SphericalTransformIter</code>* sc::IntegralCCA::new_spherical_transform_iter (int l, int inv = 0, int subl = -1) [virtual]</h3>
<p>Return a <code>SphericalTransformIter</code> object. The caller is responsible for freeing the object. </p>
<p> Implements <code>sc::Integral</code>.</p>
<h3><code>Ref</code>&lt;<code>OneBodyInt</code>&gt; sc::IntegralCCA::nuclear () [virtual]</h3>
<p>Return a <code>OneBodyInt</code> that computes the nuclear repulsion integrals. Charges from the atoms on center one are used. If center two is not identical to center one, then the charges on center two are included as well. </p>
<p> Implements <code>sc::Integral</code>.</p>
<h3><code>Ref</code>&lt;<code>OneBodyInt</code>&gt; sc::IntegralCCA::point_charge (const <code>Ref</code>&lt; <code>PointChargeData</code> &gt; &amp; = 0) [virtual]</h3>
<p>Return a <code>OneBodyInt</code> that computes the integrals for interactions with <code>point</code> charges. </p>
<p> Implements <code>sc::Integral</code>.</p>
<h3><code>Ref</code>&lt;<code>OneBodyInt</code>&gt; sc::IntegralCCA::quadrupole (const <code>Ref</code>&lt; <code>DipoleData</code> &gt; &amp; = 0) [virtual]</h3>
<p>Return a <code>OneBodyInt</code> that computes electric quadrupole moment integrals. The canonical order of integrals in a set is x^2, xy, xz, y^2, yz, z^2. </p>
<p> Implements <code>sc::Integral</code>.</p>
<h3>void sc::IntegralCCA::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::Integral</code>.</p>
<h3>const <code>SphericalTransform</code>* sc::IntegralCCA::spherical_transform (int l, int inv = 0, int subl = -1) [virtual]</h3>
<p>Return a <code>SphericalTransform</code> object. The pointer is only valid while this <code>Integral</code> object is valid. </p>
<p> Implements <code>sc::Integral</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
