---
title: "sc_summolecularenergy(3)"
name: "sc_summolecularenergy"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_summolecularenergy/"
description: "sc::SumMolecularEnergy –"
---

<p>sc::SumMolecularEnergy &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::MolecularEnergy</code>. Inherited by <code>sc::MP2BasisExtrap</code>.</p>
<h3>Public Member Functions</h3>
<p><code>SumMolecularEnergy</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;) </p>
<p> <code>SumMolecularEnergy</code> (<code>StateIn</code> &amp;) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 int <code>value_implemented</code> () const<br />
 <i>Information about the availability of values, gradients, and hessians. </i><br />
 int <code>gradient_implemented</code> () const </p>
<p> int <code>hessian_implemented</code> () const </p>
<p> void <code>set_x</code> (const <code>RefSCVector</code> &amp;)<br />
 <i>Set and retrieve the coordinate values. </i></p>
<h3>Protected Member Functions</h3>
<pre><code>void compute ()


Recompute at least the results that have compute true and are not already computed.



Protected Attributes
int n_



Ref&lt; MolecularEnergy &gt; * mole_



double * coef_</code></pre>
<h2>Member Function Documentation</h2>
<h3>void sc::SumMolecularEnergy::compute () [protected, virtual]</h3>
<p>Recompute at least the results that have compute true and are not already computed. This should only be called by Result&#8217;s members. </p>
<p> Implements <code>sc::Compute</code>. </p>
<p> Reimplemented in <code>sc::MP2BasisExtrap</code>.</p>
<h3>void sc::SumMolecularEnergy::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::MolecularEnergy</code>. </p>
<p> Reimplemented in <code>sc::MP2BasisExtrap</code>.</p>
<h3>int sc::SumMolecularEnergy::value_implemented () const [virtual]</h3>
<p>Information about the availability of values, gradients, and hessians. </p>
<p> Reimplemented from <code>sc::Function</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
