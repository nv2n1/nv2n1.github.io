---
title: "sc_molenergyconvergence(3)"
name: "sc_molenergyconvergence"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_molenergyconvergence/"
description: "sc::MolEnergyConvergence –"
---

<p>sc::MolEnergyConvergence &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::Convergence</code>.</p>
<h3>Public Member Functions</h3>
<p><code>MolEnergyConvergence</code> (<code>StateIn</code> &amp;) </p>
<p> <code>MolEnergyConvergence</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)<br />
 <i>The </i><code>KeyVal</code> constructor.<br />
 void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 void <code>get_grad</code> (const <code>Ref</code>&lt; <code>Function</code> &gt; &amp;)<br />
 <i>Set the current gradient and displacement. </i><br />
 void <code>get_x</code> (const <code>Ref</code>&lt; <code>Function</code> &gt; &amp;) </p>
<p> void <code>set_nextx</code> (const <code>RefSCVector</code> &amp;) </p>
<p> int <code>converged</code> ()<br />
 <i>Return nonzero if the optimization has converged. </i></p>
<h3>Protected Member Functions</h3>
<pre><code>void set_defaults ()



Protected Attributes</code></pre>
<p> <code>Ref</code>&lt; <code>MolecularEnergy</code> &gt; <code>mole_</code> </p>
<p> int <code>cartesian_</code></p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::MolEnergyConvergence::MolEnergyConvergence (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p>The <code>KeyVal</code> constructor. In addition to the keywords read by <code>Convergence</code>, the following keywords are examined: </p>
<dl>
<dt>energy</p>
<dd>The <code>MolecularEnergy</code> object. This is required.</dl>
<dl>
<dt>cartesian</p>
<dd>If true, cartesian displacements and gradients will be compared to the convergence criteria. The default is true.</dl>
<h2>Member Function Documentation</h2>
<h3>void sc::MolEnergyConvergence::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::Convergence</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
