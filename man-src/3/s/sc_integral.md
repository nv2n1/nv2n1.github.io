---
title: "sc_integral(3)"
name: "sc_integral"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_integral/"
description: "sc::Integral –"
---

<p>sc::Integral &#8211; </p>
<p> The <code>Integral</code> abstract class acts as a factory to provide objects that compute one and two electron integrals.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;integral.h&gt;</code></pre>
<p> Inherits <code>sc::SavableState</code>. Inherited by <code>sc::IntegralCCA</code>, <code>sc::IntegralCints</code>, and <code>sc::IntegralV3</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>Integral (StateIn &amp;)


Restore the Integral object from the given StateIn object.


Integral (const Ref&lt; KeyVal &gt; &amp;)


Construct the Integral object from the given KeyVal object.


void save_data_state (StateOut &amp;)


Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.


virtual Integral * clone ()=0


Clones the given Integral factory. The new factory may need to have set_basis and set_storage to be called on it.


virtual int equiv (const Ref&lt; Integral &gt; &amp;)


Returns nonzero if this and the given Integral object have the same integral ordering, normalization conventions, etc.


void set_storage (size_t i)


Sets the total amount of storage, in bytes, that is available.


size_t storage_used ()


Returns how much storage has been used.


size_t storage_unused ()


Returns how much storage was not needed.


virtual size_t storage_required_eri (const Ref&lt; GaussianBasisSet &gt; &amp;b1, const Ref&lt; GaussianBasisSet &gt; &amp;b2=0, const Ref&lt; GaussianBasisSet &gt; &amp;b3=0, const Ref&lt; GaussianBasisSet &gt; &amp;b4=0)


Returns how much storage will be needed to initialize a two-body integrals evaluator for electron repulsion integrals.


virtual size_t storage_required_grt (const Ref&lt; GaussianBasisSet &gt; &amp;b1, const Ref&lt; GaussianBasisSet &gt; &amp;b2=0, const Ref&lt; GaussianBasisSet &gt; &amp;b3=0, const Ref&lt; GaussianBasisSet &gt; &amp;b4=0)


Returns how much storage will be needed to initialize a two-body integrals evaluator for linear R12 integrals.


virtual size_t storage_required_eri_deriv (const Ref&lt; GaussianBasisSet &gt; &amp;b1, const Ref&lt; GaussianBasisSet &gt; &amp;b2=0, const Ref&lt; GaussianBasisSet &gt; &amp;b3=0, const Ref&lt; GaussianBasisSet &gt; &amp;b4=0)


Returns how much storage will be needed to initialize a two-body integrals evaluator for derivative electron repulsion integrals.


void adjust_storage (ptrdiff_t s)


The specific integral classes use this to tell Integral how much memory they are using/freeing.


Ref&lt; PetiteList &gt; petite_list ()


Return the PetiteList object.


Ref&lt; PetiteList &gt; petite_list (const Ref&lt; GaussianBasisSet &gt; &amp;)


Return the PetiteList object for the given basis set.


ShellRotation shell_rotation (int am, SymmetryOperation &amp;, int pure=0)


Return the ShellRotation object for a shell of the given angular momentum.


virtual void set_basis (const Ref&lt; GaussianBasisSet &gt; &amp;b1, const Ref&lt; GaussianBasisSet &gt; &amp;b2=0, const Ref&lt; GaussianBasisSet &gt; &amp;b3=0, const Ref&lt; GaussianBasisSet &gt; &amp;b4=0)


Set the basis set for each center.


virtual CartesianIter * new_cartesian_iter (int)=0


Return a CartesianIter object.


virtual RedundantCartesianIter * new_redundant_cartesian_iter (int)=0


Return a RedundantCartesianIter object.


virtual RedundantCartesianSubIter * new_redundant_cartesian_sub_iter (int)=0


Return a RedundantCartesianSubIter object.


virtual SphericalTransformIter * new_spherical_transform_iter (int l, int inv=0, int subl=-1)=0


Return a SphericalTransformIter object.


virtual const SphericalTransform * spherical_transform (int l, int inv=0, int subl=-1)=0


Return a SphericalTransform object.


virtual Ref&lt; OneBodyInt &gt; overlap ()=0


Return a OneBodyInt that computes the overlap.


virtual Ref&lt; OneBodyInt &gt; kinetic ()=0


Return a OneBodyInt that computes the kinetic energy.


virtual Ref&lt; OneBodyInt &gt; point_charge (const Ref&lt; PointChargeData &gt; &amp;)=0


Return a OneBodyInt that computes the integrals for interactions with point charges.


virtual Ref&lt; OneBodyOneCenterInt &gt; point_charge1 (const Ref&lt; PointChargeData &gt; &amp;)


Return a OneBodyInt that computes the integrals for interactions with point charges.


virtual Ref&lt; OneBodyInt &gt; nuclear ()=0


Return a OneBodyInt that computes the nuclear repulsion integrals.


virtual Ref&lt; OneBodyInt &gt; hcore ()=0


Return a OneBodyInt that computes the core Hamiltonian integrals.


virtual Ref&lt; OneBodyInt &gt; efield_dot_vector (const Ref&lt; EfieldDotVectorData &gt; &amp;)=0


Return a OneBodyInt that computes the electric field integrals dotted with a given vector.


virtual Ref&lt; OneBodyInt &gt; dipole (const Ref&lt; DipoleData &gt; &amp;)=0


Return a OneBodyInt that computes electric dipole moment integrals.


virtual Ref&lt; OneBodyInt &gt; quadrupole (const Ref&lt; DipoleData &gt; &amp;)=0


Return a OneBodyInt that computes electric quadrupole moment integrals.


virtual Ref&lt; OneBodyDerivInt &gt; overlap_deriv ()=0


Return a OneBodyDerivInt that computes overlap derivatives.


virtual Ref&lt; OneBodyDerivInt &gt; kinetic_deriv ()=0


Return a OneBodyDerivInt that computes kinetic energy derivatives.


virtual Ref&lt; OneBodyDerivInt &gt; nuclear_deriv ()=0


Return a OneBodyDerivInt that computes nuclear repulsion derivatives.


virtual Ref&lt; OneBodyDerivInt &gt; hcore_deriv ()=0


Return a OneBodyDerivInt that computes core Hamiltonian derivatives.


virtual Ref&lt; TwoBodyThreeCenterInt &gt; electron_repulsion3 ()


Return a TwoBodyThreeCenterInt that computes electron repulsion integrals.


virtual Ref&lt; TwoBodyThreeCenterDerivInt &gt; electron_repulsion3_deriv ()


Return a TwoBodyThreeCenterInt that computes electron repulsion integrals.


virtual Ref&lt; TwoBodyTwoCenterInt &gt; electron_repulsion2 ()


Return a TwoBodyTwoCenterInt that computes electron repulsion integrals.


virtual Ref&lt; TwoBodyTwoCenterDerivInt &gt; electron_repulsion2_deriv ()


Return a TwoBodyTwoCenterInt that computes electron repulsion integrals.


virtual Ref&lt; TwoBodyInt &gt; electron_repulsion ()=0


Return a TwoBodyInt that computes electron repulsion integrals.


virtual Ref&lt; TwoBodyDerivInt &gt; electron_repulsion_deriv ()=0


Return a TwoBodyDerivInt that computes electron repulsion derivatives.


virtual Ref&lt; TwoBodyInt &gt; grt ()


Return a TwoBodyInt that computes two-electron integrals specific to linear R12 methods.


Ref&lt; MessageGrp &gt; messagegrp ()


Return the MessageGrp used by the integrals objects.



Static Public Member Functions
static Integral * initial_integral (int &amp;argc, char **argv)


Create an integral factory.


static void set_default_integral (const Ref&lt; Integral &gt; &amp;)


Specifies a new default Integral factory.


static Integral * get_default_integral ()


Returns the default Integral factory.



Protected Member Functions</code></pre>
<p> <code>Integral</code> (const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;b1, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;b2, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;b3, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;b4)<br />
 <i>Initialize the </i><code>Integral</code> object given a <code>GaussianBasisSet</code> for each center.</p>
<h3>Protected Attributes</h3>
<p><code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>bs1_</code> </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>bs2_</code> </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>bs3_</code> </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>bs4_</code> </p>
<p> size_t <code>storage_</code> </p>
<p> size_t <code>storage_used_</code> </p>
<p> <code>Ref</code>&lt; <code>MessageGrp</code> &gt; <code>grp_</code></p>
<h2>Detailed Description</h2>
<p>The <code>Integral</code> abstract class acts as a factory to provide objects that compute one and two electron integrals.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::Integral::Integral (const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp; b1, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp; b2, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp; b3, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp; b4) [protected]</h3>
<p>Initialize the <code>Integral</code> object given a <code>GaussianBasisSet</code> for each center.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::Integral::adjust_storage (ptrdiff_t s) [inline]</h3>
<p>The specific integral classes use this to tell <code>Integral</code> how much memory they are using/freeing.</p>
<h3>virtual <code>Ref</code>&lt;<code>OneBodyInt</code>&gt; sc::Integral::dipole (const <code>Ref</code>&lt; <code>DipoleData</code> &gt; &amp;) [pure virtual]</h3>
<p>Return a <code>OneBodyInt</code> that computes electric dipole moment integrals. The canonical order of integrals in a set is x, y, z. </p>
<p> Implemented in <code>sc::IntegralCints</code>, <code>sc::IntegralCCA</code>, and <code>sc::IntegralV3</code>.</p>
<h3>virtual <code>Ref</code>&lt;<code>OneBodyInt</code>&gt; sc::Integral::efield_dot_vector (const <code>Ref</code>&lt; <code>EfieldDotVectorData</code> &gt; &amp;) [pure virtual]</h3>
<p>Return a <code>OneBodyInt</code> that computes the electric field integrals dotted with a given vector. </p>
<p> Implemented in <code>sc::IntegralCints</code>, <code>sc::IntegralCCA</code>, and <code>sc::IntegralV3</code>.</p>
<h3>virtual <code>Ref</code>&lt;<code>TwoBodyTwoCenterInt</code>&gt; sc::Integral::electron_repulsion2 () [virtual]</h3>
<p>Return a <code>TwoBodyTwoCenterInt</code> that computes electron repulsion integrals. If this is not re-implemented it will throw. </p>
<p> Reimplemented in <code>sc::IntegralV3</code>.</p>
<h3>virtual <code>Ref</code>&lt;<code>TwoBodyTwoCenterDerivInt</code>&gt; sc::Integral::electron_repulsion2_deriv () [virtual]</h3>
<p>Return a <code>TwoBodyTwoCenterInt</code> that computes electron repulsion integrals. If this is not re-implemented it will throw.</p>
<h3>virtual <code>Ref</code>&lt;<code>TwoBodyThreeCenterInt</code>&gt; sc::Integral::electron_repulsion3 () [virtual]</h3>
<p>Return a <code>TwoBodyThreeCenterInt</code> that computes electron repulsion integrals. If this is not re-implemented it will throw. </p>
<p> Reimplemented in <code>sc::IntegralV3</code>.</p>
<h3>virtual <code>Ref</code>&lt;<code>TwoBodyThreeCenterDerivInt</code>&gt; sc::Integral::electron_repulsion3_deriv () [virtual]</h3>
<p>Return a <code>TwoBodyThreeCenterInt</code> that computes electron repulsion integrals. If this is not re-implemented it will throw.</p>
<h3>virtual int sc::Integral::equiv (const <code>Ref</code>&lt; <code>Integral</code> &gt; &amp;) [virtual]</h3>
<p>Returns nonzero if this and the given <code>Integral</code> object have the same integral ordering, normalization conventions, etc.</p>
<h3>virtual <code>Ref</code>&lt;<code>TwoBodyInt</code>&gt; sc::Integral::grt () [virtual]</h3>
<p>Return a <code>TwoBodyInt</code> that computes two-electron integrals specific to linear R12 methods. According to the convention in the literature, &#8216;g&#8217; stands for electron repulsion integral, &#8216;r&#8217; for the integral of r12 operator, and &#8216;t&#8217; for the commutator integrals. Implementation for this kind of <code>TwoBodyInt</code> is optional. </p>
<p> Reimplemented in <code>sc::IntegralCints</code>.</p>
<h3>static <code>Integral</code>* sc::Integral::initial_integral (int &amp; argc, char ** argv) [static]</h3>
<p>Create an integral factory. This routine looks for a -integral argument, then the environmental variable INTEGRAL. The argument to -integral should be either string for a <code>ParsedKeyVal</code> constructor or a classname. This factory is not guaranteed to have its storage and basis sets set up properly, hence set_basis and set_storage need to be called on it.</p>
<h3>virtual <code>CartesianIter</code>* sc::Integral::new_cartesian_iter (int) [pure virtual]</h3>
<p>Return a <code>CartesianIter</code> object. The caller is responsible for freeing the object. </p>
<p> Implemented in <code>sc::IntegralCints</code>, <code>sc::IntegralCCA</code>, and <code>sc::IntegralV3</code>.</p>
<h3>virtual <code>RedundantCartesianIter</code>* sc::Integral::new_redundant_cartesian_iter (int) [pure virtual]</h3>
<p>Return a <code>RedundantCartesianIter</code> object. The caller is responsible for freeing the object. </p>
<p> Implemented in <code>sc::IntegralCints</code>, <code>sc::IntegralCCA</code>, and <code>sc::IntegralV3</code>.</p>
<h3>virtual <code>RedundantCartesianSubIter</code>* sc::Integral::new_redundant_cartesian_sub_iter (int) [pure virtual]</h3>
<p>Return a <code>RedundantCartesianSubIter</code> object. The caller is responsible for freeing the object. </p>
<p> Implemented in <code>sc::IntegralCints</code>, <code>sc::IntegralCCA</code>, and <code>sc::IntegralV3</code>.</p>
<h3>virtual <code>SphericalTransformIter</code>* sc::Integral::new_spherical_transform_iter (int l, int inv = 0, int subl = -1) [pure virtual]</h3>
<p>Return a <code>SphericalTransformIter</code> object. The caller is responsible for freeing the object. </p>
<p> Implemented in <code>sc::IntegralCints</code>, <code>sc::IntegralCCA</code>, and <code>sc::IntegralV3</code>.</p>
<h3>virtual <code>Ref</code>&lt;<code>OneBodyInt</code>&gt; sc::Integral::nuclear () [pure virtual]</h3>
<p>Return a <code>OneBodyInt</code> that computes the nuclear repulsion integrals. Charges from the atoms on center one are used. If center two is not identical to center one, then the charges on center two are included as well. </p>
<p> Implemented in <code>sc::IntegralCints</code>, <code>sc::IntegralCCA</code>, and <code>sc::IntegralV3</code>.</p>
<h3>virtual <code>Ref</code>&lt;<code>OneBodyInt</code>&gt; sc::Integral::point_charge (const <code>Ref</code>&lt; <code>PointChargeData</code> &gt; &amp;) [pure virtual]</h3>
<p>Return a <code>OneBodyInt</code> that computes the integrals for interactions with <code>point</code> charges. </p>
<p> Implemented in <code>sc::IntegralCints</code>, <code>sc::IntegralCCA</code>, and <code>sc::IntegralV3</code>.</p>
<h3>virtual <code>Ref</code>&lt;<code>OneBodyOneCenterInt</code>&gt; sc::Integral::point_charge1 (const <code>Ref</code>&lt; <code>PointChargeData</code> &gt; &amp;) [virtual]</h3>
<p>Return a <code>OneBodyInt</code> that computes the integrals for interactions with <code>point</code> charges. </p>
<p> Reimplemented in <code>sc::IntegralV3</code>.</p>
<h3>virtual <code>Ref</code>&lt;<code>OneBodyInt</code>&gt; sc::Integral::quadrupole (const <code>Ref</code>&lt; <code>DipoleData</code> &gt; &amp;) [pure virtual]</h3>
<p>Return a <code>OneBodyInt</code> that computes electric quadrupole moment integrals. The canonical order of integrals in a set is x^2, xy, xz, y^2, yz, z^2. </p>
<p> Implemented in <code>sc::IntegralCints</code>, <code>sc::IntegralCCA</code>, and <code>sc::IntegralV3</code>.</p>
<h3>void sc::Integral::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SavableState</code>. </p>
<p> Reimplemented in <code>sc::IntegralCints</code>, <code>sc::IntegralCCA</code>, and <code>sc::IntegralV3</code>.</p>
<h3><code>ShellRotation</code> sc::Integral::shell_rotation (int am, <code>SymmetryOperation</code> &amp;, int pure = 0)</h3>
<p>Return the <code>ShellRotation</code> object for a shell of the given angular momentum. Pass nonzero to pure to do solid harmonics.</p>
<h3>virtual const <code>SphericalTransform</code>* sc::Integral::spherical_transform (int l, int inv = 0, int subl = -1) [pure virtual]</h3>
<p>Return a <code>SphericalTransform</code> object. The pointer is only valid while this <code>Integral</code> object is valid. </p>
<p> Implemented in <code>sc::IntegralCints</code>, <code>sc::IntegralCCA</code>, and <code>sc::IntegralV3</code>.</p>
<h3>virtual size_t sc::Integral::storage_required_eri (const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp; b1, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp; b2 = 0, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp; b3 = 0, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp; b4 = 0) [virtual]</h3>
<p>Returns how much storage will be needed to initialize a two-body integrals evaluator for electron repulsion integrals. </p>
<p> Reimplemented in <code>sc::IntegralCints</code>.</p>
<h3>virtual size_t sc::Integral::storage_required_eri_deriv (const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp; b1, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp; b2 = 0, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp; b3 = 0, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp; b4 = 0) [virtual]</h3>
<p>Returns how much storage will be needed to initialize a two-body integrals evaluator for derivative electron repulsion integrals.</p>
<h3>virtual size_t sc::Integral::storage_required_grt (const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp; b1, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp; b2 = 0, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp; b3 = 0, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp; b4 = 0) [virtual]</h3>
<p>Returns how much storage will be needed to initialize a two-body integrals evaluator for linear R12 integrals. </p>
<p> Reimplemented in <code>sc::IntegralCints</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
