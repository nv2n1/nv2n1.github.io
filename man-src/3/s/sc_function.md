---
title: "sc_function(3)"
name: "sc_function"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_function/"
description: "sc::Function –"
---

<p>sc::Function &#8211; </p>
<p> The <code>Function</code> class is an abstract base class that, given a set of coordinates, will compute a value and possibly a gradient and hessian at that <code>point</code>.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;function.h&gt;</code></pre>
<p> Inherits <code>sc::SavableState</code>, and <code>sc::Compute</code>. Inherited by <code>sc::MolecularEnergy</code>, and <code>sc::Volume</code>.</p>
<h3>Public Member Functions</h3>
<p><code>Function</code> (<code>StateIn</code> &amp;) </p>
<p> <code>Function</code> (const <code>Function</code> &amp;) </p>
<p> <code>Function</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;, double funcacc=DBL_EPSILON, double gradacc=DBL_EPSILON, double hessacc=DBL_EPSILON)<br />
 <i>The keyval constructor reads the following keywords:. </i><br />
 <code>Function</code> &amp; <code>operator=</code> (const <code>Function</code> &amp;) </p>
<p> <code>Ref</code>&lt; <code>SCMatrixKit</code> &gt; <code>matrixkit</code> () const<br />
 <i>Return the </i><code>SCMatrixKit</code> used to construct vectors and matrices.<br />
 <code>RefSCDimension</code> <code>dimension</code> () const<br />
 <i>Return the </i><code>SCDimension</code> of the problem.<br />
 virtual void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 virtual double <code>value</code> ()<br />
 <i>Return the value of the function. </i><br />
 int <code>value_needed</code> () const<br />
 <i>Returns nonzero if the current value is not up-to-date. </i><br />
 int <code>do_value</code> (int)<br />
 <i>If passed a nonzero number, compute the value the next time </i><code>compute()</code> is called.<br />
 <code>AccResultdouble</code> &amp; <code>value_result</code> () </p>
<p> virtual void <code>set_desired_value_accuracy</code> (double)<br />
 <i>Set the accuracy to which the value is to be computed. </i><br />
 virtual double <code>actual_value_accuracy</code> () const<br />
 <i>Return the accuracy with which the value has been computed. </i><br />
 virtual double <code>desired_value_accuracy</code> () const<br />
 <i>Return the accuracy with which the value is to be computed. </i><br />
 virtual void <code>guess_hessian</code> (<code>RefSymmSCMatrix</code> &amp;)<br />
 <i></i><code>Compute</code> a quick, approximate hessian.<br />
 virtual <code>RefSymmSCMatrix</code> <code>inverse_hessian</code> (<code>RefSymmSCMatrix</code> &amp;) </p>
<p> virtual int <code>value_implemented</code> () const<br />
 <i>Information about the availability of values, gradients, and hessians. </i><br />
 virtual int <code>gradient_implemented</code> () const </p>
<p> virtual int <code>hessian_implemented</code> () const </p>
<p> virtual void <code>set_x</code> (const <code>RefSCVector</code> &amp;)<br />
 <i>Set and retrieve the coordinate values. </i><br />
 <code>RefSCVector</code> <code>get_x</code> () const </p>
<p> const <code>RefSCVector</code> &amp; <code>get_x_no_copy</code> () const </p>
<p> virtual <code>Ref</code>&lt; <code>NonlinearTransform</code> &gt; <code>change_coordinates</code> ()<br />
 <i>An optimizer can call change coordinates periodically to give the function an opportunity to change its coordinate system. </i><br />
 virtual void <code>print</code> (std::ostream &amp;=ExEnv::out0()) const<br />
 <i>Print information about the object. </i> <code>Gradient Members</code><br />
 These are analogous to the routines that deal with values, but work with gradients instead.<br />
 virtual <code>RefSCVector</code> <code>gradient</code> () </p>
<p> int <code>gradient_needed</code> () const </p>
<p> int <code>do_gradient</code> (int) </p>
<p> virtual void <code>set_desired_gradient_accuracy</code> (double) </p>
<p> virtual double <code>actual_gradient_accuracy</code> () const </p>
<p> virtual double <code>desired_gradient_accuracy</code> () const </p>
<p> <code>AccResultRefSCVector</code> &amp; <code>gradient_result</code> ()<br />
 <code>Hessian Members</code><br />
 These are analogous to the routines that deal with values, but work with the hessian instead.<br />
 virtual <code>RefSymmSCMatrix</code> <code>hessian</code> () </p>
<p> int <code>hessian_needed</code> () const </p>
<p> int <code>do_hessian</code> (int) </p>
<p> virtual void <code>set_desired_hessian_accuracy</code> (double) </p>
<p> virtual double <code>actual_hessian_accuracy</code> () const </p>
<p> virtual double <code>desired_hessian_accuracy</code> () const </p>
<p> <code>AccResultRefSymmSCMatrix</code> &amp; <code>hessian_result</code> ()</p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>set_matrixkit</code> (const <code>Ref</code>&lt; <code>SCMatrixKit</code> &gt; &amp;)<br />
 <i>Set the </i><code>SCMatrixKit</code> that should be used to construct the requisite vectors and matrices.<br />
 virtual void <code>set_dimension</code> (const <code>RefSCDimension</code> &amp;) </p>
<p> <code>RefSCVector</code> &amp; <code>get_x_reference</code> ()<br />
 <i>Get read/write access to the coordinates for modification. </i><br />
 void <code>do_change_coordinates</code> (const <code>Ref</code>&lt; <code>NonlinearTransform</code> &gt; &amp;)<br />
 <i>Change the coordinate system and apply the given transform to intermediates matrices and vectors. </i> <code>Update Members</code><br />
 Update the various computable results.<br />
 virtual void <code>set_value</code> (double) </p>
<p> virtual void <code>set_gradient</code> (<code>RefSCVector</code> &amp;) </p>
<p> virtual void <code>set_hessian</code> (<code>RefSymmSCMatrix</code> &amp;)<br />
 <code>Accuracy Setting Members</code><br />
 Set the accuracies with which the various computables have been computed.<br />
 virtual void <code>set_actual_value_accuracy</code> (double) </p>
<p> virtual void <code>set_actual_gradient_accuracy</code> (double) </p>
<p> virtual void <code>set_actual_hessian_accuracy</code> (double)</p>
<h3>Protected Attributes</h3>
<p><code>Ref</code>&lt; <code>SCMatrixKit</code> &gt; <code>matrixkit_</code><br />
 <i>Used to construct new matrices. </i><br />
 <code>RefSCVector</code> <code>x_</code><br />
 <i>The variables. </i><br />
 <code>RefSCDimension</code> <code>dim_</code><br />
 <i>The dimension of x_. </i><br />
 <code>AccResultdouble</code> <code>value_</code><br />
 <i>The value of the function at x_. </i><br />
 <code>AccResultRefSCVector</code> <code>gradient_</code><br />
 <i>The gradient at x_. </i><br />
 <code>AccResultRefSymmSCMatrix</code> <code>hessian_</code><br />
 <i>The hessian at x_. </i></p>
<h2>Detailed Description</h2>
<p>The <code>Function</code> class is an abstract base class that, given a set of coordinates, will compute a value and possibly a gradient and hessian at that <code>point</code>.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::Function::Function (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;, double funcacc = DBL_EPSILON, double gradacc = DBL_EPSILON, double hessacc = DBL_EPSILON)</h3>
<p>The keyval constructor reads the following keywords:. .IP &quot;matrixkit&quot; 1c Gives a <code>SCMatrixKit</code> object. If it is not specified, a default <code>SCMatrixKit</code> is selected. </p>
<dl>
<dt>value_accuracy</p>
<dd>Sets the accuracy to which values are computed. The default is the machine accuracy.</dl>
<dl>
<dt>gradient_accuracy</p>
<dd>Sets the accuracy to which gradients are computed. The default is the machine accuracy.</dl>
<dl>
<dt>hessian_accuracy</p>
<dd>Sets the accuracy to which hessians are computed. The default is the machine accuracy.</dl>
<h2>Member Function Documentation</h2>
<h3>virtual <code>Ref</code>&lt;<code>NonlinearTransform</code>&gt; sc::Function::change_coordinates () [virtual]</h3>
<p>An optimizer can call change coordinates periodically to give the function an opportunity to change its coordinate system. A return value of 0 means the coordinates were not changed. Otherwise, a transform object to the new coordinate system is return. The function object applies the transform to any objects it contains. This will obsolete the function data. </p>
<p> Reimplemented in <code>sc::MolecularEnergy</code>.</p>
<h3>void sc::Function::do_change_coordinates (const <code>Ref</code>&lt; <code>NonlinearTransform</code> &gt; &amp;) [protected]</h3>
<p>Change the coordinate system and apply the given transform to intermediates matrices and vectors.</p>
<h3>int sc::Function::do_value (int)</h3>
<p>If passed a nonzero number, compute the value the next time <code>compute()</code> is called. Return a nonzero number if the value was previously to be computed.</p>
<h3><code>Ref</code>&lt;<code>SCMatrixKit</code>&gt; sc::Function::matrixkit () const</h3>
<p>Return the <code>SCMatrixKit</code> used to construct vectors and matrices.</p>
<h3>virtual void sc::Function::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SavableState</code>. </p>
<p> Reimplemented in <code>sc::MolecularEnergy</code>, <code>sc::SumMolecularEnergy</code>, <code>sc::TaylorMolecularEnergy</code>, <code>sc::CLKS</code>, <code>sc::HSOSKS</code>, <code>sc::UKS</code>, <code>sc::MBPT2</code>, <code>sc::MP2BasisExtrap</code>, <code>sc::MBPT2_R12</code>, <code>sc::PsiWavefunction</code>, <code>sc::PsiSCF</code>, <code>sc::PsiCCSD</code>, <code>sc::PsiCCSD_T</code>, <code>sc::CLHF</code>, <code>sc::CLSCF</code>, <code>sc::HSOSHF</code>, <code>sc::HSOSSCF</code>, <code>sc::OSSHF</code>, <code>sc::OSSSCF</code>, <code>sc::SCF</code>, <code>sc::TCHF</code>, <code>sc::TCSCF</code>, <code>sc::UHF</code>, <code>sc::UnrestrictedSCF</code>, <code>sc::ExtendedHuckelWfn</code>, <code>sc::OneBodyWavefunction</code>, <code>sc::HCoreWfn</code>, and <code>sc::Wavefunction</code>.</p>
<h3>virtual void sc::Function::set_matrixkit (const <code>Ref</code>&lt; <code>SCMatrixKit</code> &gt; &amp;) [protected, virtual]</h3>
<p>Set the <code>SCMatrixKit</code> that should be used to construct the requisite vectors and matrices.</p>
<h3>virtual int sc::Function::value_implemented () const [virtual]</h3>
<p>Information about the availability of values, gradients, and hessians. </p>
<p> Reimplemented in <code>sc::SumMolecularEnergy</code>, <code>sc::TaylorMolecularEnergy</code>, <code>sc::CLKS</code>, <code>sc::HSOSKS</code>, <code>sc::UKS</code>, <code>sc::MBPT2</code>, <code>sc::MBPT2_R12</code>, <code>sc::CLHF</code>, <code>sc::HSOSHF</code>, <code>sc::OSSHF</code>, <code>sc::TCHF</code>, <code>sc::UHF</code>, <code>sc::ExtendedHuckelWfn</code>, <code>sc::HCoreWfn</code>, and <code>sc::Shape</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
