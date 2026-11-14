---
title: "sc_taylormolecularenergy(3)"
name: "sc_taylormolecularenergy"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_taylormolecularenergy/"
description: "sc::TaylorMolecularEnergy –"
---

<p>sc::TaylorMolecularEnergy &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::MolecularEnergy</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>TaylorMolecularEnergy (const Ref&lt; KeyVal &gt; &amp;)



TaylorMolecularEnergy (StateIn &amp;)



void save_data_state (StateOut &amp;)


Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.


void print (std::ostream &amp;=ExEnv::out0()) const


Print information about the object.


void compute ()


Recompute at least the results that have compute true and are not already computed.


int value_implemented () const


Information about the availability of values, gradients, and hessians.


int gradient_implemented () const



int hessian_implemented () const</code></pre>
<h2>Member Function Documentation</h2>
<h3>void sc::TaylorMolecularEnergy::compute () [virtual]</h3>
<p>Recompute at least the results that have compute true and are not already computed. This should only be called by Result&#8217;s members. </p>
<p> Implements <code>sc::Compute</code>.</p>
<h3>void sc::TaylorMolecularEnergy::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::MolecularEnergy</code>.</p>
<h3>int sc::TaylorMolecularEnergy::value_implemented () const [virtual]</h3>
<p>Information about the availability of values, gradients, and hessians. </p>
<p> Reimplemented from <code>sc::Function</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
