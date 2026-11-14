---
title: "sc_molecularcoor(3)"
name: "sc_molecularcoor"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_molecularcoor/"
description: "sc::MolecularCoor –"
---

<p>sc::MolecularCoor &#8211; </p>
<p> The <code>MolecularCoor</code> abstract class describes the coordinate system used to describe a molecule.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;coor.h&gt;</code></pre>
<p> Inherits <code>sc::SavableState</code>. Inherited by <code>sc::CartMolecularCoor</code>, and <code>sc::IntMolecularCoor</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>MolecularCoor (Ref&lt; Molecule &gt; &amp;)



MolecularCoor (StateIn &amp;)



MolecularCoor (const Ref&lt; KeyVal &gt; &amp;)


The KeyVal constructor.


void save_data_state (StateOut &amp;)


Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.


RefSCDimension dim_natom3 ()


Returns a smart reference to an SCDimension equal to the number of atoms in the molecule times 3.


Ref&lt; Molecule &gt; molecule () const


Returns the molecule.


virtual void print (std::ostream &amp;=ExEnv::out0()) const =0


Print the coordinate.


virtual void print_simples (std::ostream &amp;=ExEnv::out0()) const =0



virtual RefSCDimension dim ()=0


Returns a smart reference to an SCDimension equal to the number of coordinates (be they Cartesian, internal, or whatever) that are being optimized.


int to_cartesian (const RefSCVector &amp;internal)


Given a set of displaced internal coordinates, update the cartesian coordinates of the Molecule contained herein.


virtual int to_cartesian (const Ref&lt; Molecule &gt; &amp;mol, const RefSCVector &amp;internal)=0



virtual int to_internal (RefSCVector &amp;internal)=0


Fill in the vector ``internal'' with the current internal coordinates.


virtual int to_cartesian (RefSCVector &amp;cartesian, RefSCVector &amp;internal)=0


Convert the internal coordinate gradients in ``internal'' to Cartesian coordinates and copy these Cartesian coordinate gradients to ``cartesian''.


virtual int to_internal (RefSCVector &amp;internal, RefSCVector &amp;cartesian)=0


Convert the Cartesian coordinate gradients in ``cartesian'' to internal coordinates and copy these internal coordinate gradients to ``internal''.


virtual int to_cartesian (RefSymmSCMatrix &amp;cartesian, RefSymmSCMatrix &amp;internal)=0


Convert the internal coordinate Hessian ``internal'' to Cartesian coordinates and copy the result to ``cartesian''.


virtual int to_internal (RefSymmSCMatrix &amp;internal, RefSymmSCMatrix &amp;cartesian)=0


Convert the Cartesian coordinate Hessian ``cartesian'' to internal coordinates and copy the result to ``internal''.


virtual void guess_hessian (RefSymmSCMatrix &amp;hessian)=0


Calculate an approximate hessian and place the result in ``hessian''.


virtual RefSymmSCMatrix inverse_hessian (RefSymmSCMatrix &amp;)=0


Given an Hessian, return the inverse of that hessian.


virtual int nconstrained ()


Returns the number of constrained coordinates.


virtual Ref&lt; NonlinearTransform &gt; change_coordinates ()


When this is called, MoleculeCoor may select a new internal coordinate system and return a transform to it.


Ref&lt; SCMatrixKit &gt; matrixkit () const



Protected Attributes</code></pre>
<p> <code>Ref</code>&lt; <code>Molecule</code> &gt; <code>molecule_</code> </p>
<p> <code>RefSCDimension</code> <code>dnatom3_</code> </p>
<p> <code>Ref</code>&lt; <code>SCMatrixKit</code> &gt; <code>matrixkit_</code> </p>
<p> int <code>debug_</code></p>
<h2>Detailed Description</h2>
<p>The <code>MolecularCoor</code> abstract class describes the coordinate system used to describe a molecule. </p>
<p> It is used to convert a molecule&#8217;s cartesian coordinates to and from this coordinate system.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::MolecularCoor::MolecularCoor (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p>The <code>KeyVal</code> constructor. .IP &quot;molecule&quot; 1c A <code>Molecule</code> object. There is no default. </p>
<dl>
<dt>debug</p>
<dd>An integer which, if nonzero, will cause extra output.</dl>
<dl>
<dt>matrixkit</p>
<dd>A <code>SCMatrixKit</code> object. It is usually unnecessary to give this keyword.</dl>
<dl>
<dt>natom3</p>
<dd>An <code>SCDimension</code> object for the dimension of the vector of cartesian coordinates. It is usually unnecessary to give this keyword.</dl>
<h2>Member Function Documentation</h2>
<h3>virtual <code>Ref</code>&lt;<code>NonlinearTransform</code>&gt; sc::MolecularCoor::change_coordinates () [virtual]</h3>
<p>When this is called, MoleculeCoor may select a new internal coordinate system and return a transform to it. The default action is to not change anything and return an <code>IdentityTransform</code>. </p>
<p> Reimplemented in <code>sc::SymmMolecularCoor</code>.</p>
<h3>virtual <code>RefSCDimension</code> sc::MolecularCoor::dim () [pure virtual]</h3>
<p>Returns a smart reference to an <code>SCDimension</code> equal to the number of coordinates (be they Cartesian, internal, or whatever) that are being optimized. </p>
<p> Implemented in <code>sc::IntMolecularCoor</code>, and <code>sc::CartMolecularCoor</code>.</p>
<h3><code>RefSCDimension</code> sc::MolecularCoor::dim_natom3 () [inline]</h3>
<p>Returns a smart reference to an <code>SCDimension</code> equal to the number of atoms in the molecule times 3.</p>
<h3>virtual void sc::MolecularCoor::guess_hessian (<code>RefSymmSCMatrix</code> &amp; hessian) [pure virtual]</h3>
<p>Calculate an approximate hessian and place the result in &#8220;hessian&#8221;. </p>
<p> Implemented in <code>sc::SymmMolecularCoor</code>, <code>sc::RedundMolecularCoor</code>, and <code>sc::CartMolecularCoor</code>.</p>
<h3>virtual <code>RefSymmSCMatrix</code> sc::MolecularCoor::inverse_hessian (<code>RefSymmSCMatrix</code> &amp;) [pure virtual]</h3>
<p>Given an Hessian, return the inverse of that hessian. For singular matrices this should return the generalized inverse. </p>
<p> Implemented in <code>sc::SymmMolecularCoor</code>, <code>sc::RedundMolecularCoor</code>, and <code>sc::CartMolecularCoor</code>.</p>
<h3>void sc::MolecularCoor::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SavableState</code>. </p>
<p> Reimplemented in <code>sc::IntMolecularCoor</code>, <code>sc::SymmMolecularCoor</code>, <code>sc::RedundMolecularCoor</code>, and <code>sc::CartMolecularCoor</code>.</p>
<h3>virtual int sc::MolecularCoor::to_cartesian (<code>RefSymmSCMatrix</code> &amp; cartesian, <code>RefSymmSCMatrix</code> &amp; internal) [pure virtual]</h3>
<p>Convert the internal coordinate Hessian &#8220;internal&#8221; to Cartesian coordinates and copy the result to &#8220;cartesian&#8221;. Only the variable internal coordinate force constants are transformed. </p>
<p> Implemented in <code>sc::IntMolecularCoor</code>, and <code>sc::CartMolecularCoor</code>.</p>
<h3>virtual int sc::MolecularCoor::to_cartesian (<code>RefSCVector</code> &amp; cartesian, <code>RefSCVector</code> &amp; internal) [pure virtual]</h3>
<p>Convert the internal coordinate gradients in &#8220;internal&#8221; to Cartesian coordinates and copy these Cartesian coordinate gradients to &#8220;cartesian&#8221;. Only the variable internal coordinate gradients are transformed. </p>
<p> Implemented in <code>sc::IntMolecularCoor</code>, and <code>sc::CartMolecularCoor</code>.</p>
<h3>int sc::MolecularCoor::to_cartesian (const <code>RefSCVector</code> &amp; internal)</h3>
<p>Given a set of displaced internal coordinates, update the cartesian coordinates of the <code>Molecule</code> contained herein. This function does not change the vector &#8220;internal&#8221;.</p>
<h3>virtual int sc::MolecularCoor::to_internal (<code>RefSymmSCMatrix</code> &amp; internal, <code>RefSymmSCMatrix</code> &amp; cartesian) [pure virtual]</h3>
<p>Convert the Cartesian coordinate Hessian &#8220;cartesian&#8221; to internal coordinates and copy the result to &#8220;internal&#8221;. Only the variable internal coordinate force constants are calculated. </p>
<p> Implemented in <code>sc::IntMolecularCoor</code>, and <code>sc::CartMolecularCoor</code>.</p>
<h3>virtual int sc::MolecularCoor::to_internal (<code>RefSCVector</code> &amp; internal, <code>RefSCVector</code> &amp; cartesian) [pure virtual]</h3>
<p>Convert the Cartesian coordinate gradients in &#8220;cartesian&#8221; to internal coordinates and copy these internal coordinate gradients to &#8220;internal&#8221;. Only the variable internal coordinate gradients are calculated. </p>
<p> Implemented in <code>sc::IntMolecularCoor</code>, and <code>sc::CartMolecularCoor</code>.</p>
<h3>virtual int sc::MolecularCoor::to_internal (<code>RefSCVector</code> &amp; internal) [pure virtual]</h3>
<p>Fill in the vector &#8220;internal&#8221; with the current internal coordinates. Note that this member will update the values of the variable internal coordinates. </p>
<p> Implemented in <code>sc::IntMolecularCoor</code>, and <code>sc::CartMolecularCoor</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
