---
title: "sc_mp2basisextrap(3)"
name: "sc_mp2basisextrap"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_mp2basisextrap/"
description: "sc::MP2BasisExtrap –"
---

<p>sc::MP2BasisExtrap &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::SumMolecularEnergy</code>.</p>
<h3>Public Member Functions</h3>
<p><code>MP2BasisExtrap</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;) </p>
<p> <code>MP2BasisExtrap</code> (<code>StateIn</code> &amp;) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.</p>
<h3>Protected Member Functions</h3>
<p>void <code>compute</code> ()<br />
 <i>Recompute at least the results that have compute true and are not already computed. </i></p>
<h2>Member Function Documentation</h2>
<h3>void sc::MP2BasisExtrap::compute () [protected, virtual]</h3>
<p>Recompute at least the results that have compute true and are not already computed. This should only be called by Result&#8217;s members. </p>
<p> Reimplemented from <code>sc::SumMolecularEnergy</code>.</p>
<h3>void sc::MP2BasisExtrap::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SumMolecularEnergy</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
