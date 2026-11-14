---
title: "sc_cartmolecularcoor(3)"
name: "sc_cartmolecularcoor"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_cartmolecularcoor/"
description: "sc::CartMolecularCoor –"
---

<p>sc::CartMolecularCoor &#8211; </p>
<p> The <code>CartMolecularCoor</code> class implements Cartesian coordinates in a way suitable for use in geometry optimizations.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;coor.h&gt;</code></pre>
<p> Inherits <code>sc::MolecularCoor</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>CartMolecularCoor (Ref&lt; Molecule &gt; &amp;mol)



CartMolecularCoor (StateIn &amp;)



CartMolecularCoor (const Ref&lt; KeyVal &gt; &amp;)


The KeyVal constructor.


void save_data_state (StateOut &amp;)


Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.


virtual RefSCDimension dim ()


These implement the virtual functions inherited from MolecularCoor.


virtual int to_cartesian (const Ref&lt; Molecule &gt; &amp;, const RefSCVector &amp;internal)



virtual int to_internal (RefSCVector &amp;internal)


Fill in the vector ``internal'' with the current internal coordinates.


virtual int to_cartesian (RefSCVector &amp;cartesian, RefSCVector &amp;internal)


Convert the internal coordinate gradients in ``internal'' to Cartesian coordinates and copy these Cartesian coordinate gradients to ``cartesian''.


virtual int to_internal (RefSCVector &amp;internal, RefSCVector &amp;cartesian)


Convert the Cartesian coordinate gradients in ``cartesian'' to internal coordinates and copy these internal coordinate gradients to ``internal''.


virtual int to_cartesian (RefSymmSCMatrix &amp;cart, RefSymmSCMatrix &amp;internal)


Convert the internal coordinate Hessian ``internal'' to Cartesian coordinates and copy the result to ``cartesian''.


virtual int to_internal (RefSymmSCMatrix &amp;internal, RefSymmSCMatrix &amp;cart)


Convert the Cartesian coordinate Hessian ``cartesian'' to internal coordinates and copy the result to ``internal''.


virtual void print (std::ostream &amp;=ExEnv::out0()) const


Print the coordinate.


virtual void print_simples (std::ostream &amp;=ExEnv::out0()) const



void guess_hessian (RefSymmSCMatrix &amp;hessian)


Calculate an approximate hessian and place the result in ``hessian''.


RefSymmSCMatrix inverse_hessian (RefSymmSCMatrix &amp;)


Given an Hessian, return the inverse of that hessian.



Protected Member Functions</code></pre>
<p> virtual void <code>init</code> ()<br />
 <i>Initializes the dimensions. </i></p>
<h3>Protected Attributes</h3>
<p><code>RefSCDimension</code> <code>dim_</code></p>
<h2>Detailed Description</h2>
<p>The <code>CartMolecularCoor</code> class implements Cartesian coordinates in a way suitable for use in geometry optimizations. </p>
<p> <code>CartMolecularCoor</code> is a <code>SavableState</code> has <code>StateIn</code> and <code>KeyVal</code> constructors. <code>CartMolecularCoor</code> is derived from <code>MolecularCoor</code>.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::CartMolecularCoor::guess_hessian (<code>RefSymmSCMatrix</code> &amp; hessian) [virtual]</h3>
<p>Calculate an approximate hessian and place the result in &#8220;hessian&#8221;. </p>
<p> Implements <code>sc::MolecularCoor</code>.</p>
<h3><code>RefSymmSCMatrix</code> sc::CartMolecularCoor::inverse_hessian (<code>RefSymmSCMatrix</code> &amp;) [virtual]</h3>
<p>Given an Hessian, return the inverse of that hessian. For singular matrices this should return the generalized inverse. </p>
<p> Implements <code>sc::MolecularCoor</code>.</p>
<h3>void sc::CartMolecularCoor::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::MolecularCoor</code>.</p>
<h3>virtual int sc::CartMolecularCoor::to_cartesian (<code>RefSymmSCMatrix</code> &amp; cartesian, <code>RefSymmSCMatrix</code> &amp; internal) [virtual]</h3>
<p>Convert the internal coordinate Hessian &#8220;internal&#8221; to Cartesian coordinates and copy the result to &#8220;cartesian&#8221;. Only the variable internal coordinate force constants are transformed. </p>
<p> Implements <code>sc::MolecularCoor</code>.</p>
<h3>virtual int sc::CartMolecularCoor::to_cartesian (<code>RefSCVector</code> &amp; cartesian, <code>RefSCVector</code> &amp; internal) [virtual]</h3>
<p>Convert the internal coordinate gradients in &#8220;internal&#8221; to Cartesian coordinates and copy these Cartesian coordinate gradients to &#8220;cartesian&#8221;. Only the variable internal coordinate gradients are transformed. </p>
<p> Implements <code>sc::MolecularCoor</code>.</p>
<h3>virtual int sc::CartMolecularCoor::to_internal (<code>RefSymmSCMatrix</code> &amp; internal, <code>RefSymmSCMatrix</code> &amp; cartesian) [virtual]</h3>
<p>Convert the Cartesian coordinate Hessian &#8220;cartesian&#8221; to internal coordinates and copy the result to &#8220;internal&#8221;. Only the variable internal coordinate force constants are calculated. </p>
<p> Implements <code>sc::MolecularCoor</code>.</p>
<h3>virtual int sc::CartMolecularCoor::to_internal (<code>RefSCVector</code> &amp; internal, <code>RefSCVector</code> &amp; cartesian) [virtual]</h3>
<p>Convert the Cartesian coordinate gradients in &#8220;cartesian&#8221; to internal coordinates and copy these internal coordinate gradients to &#8220;internal&#8221;. Only the variable internal coordinate gradients are calculated. </p>
<p> Implements <code>sc::MolecularCoor</code>.</p>
<h3>virtual int sc::CartMolecularCoor::to_internal (<code>RefSCVector</code> &amp; internal) [virtual]</h3>
<p>Fill in the vector &#8220;internal&#8221; with the current internal coordinates. Note that this member will update the values of the variable internal coordinates. </p>
<p> Implements <code>sc::MolecularCoor</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
