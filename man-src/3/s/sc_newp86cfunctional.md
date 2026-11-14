---
title: "sc_newp86cfunctional(3)"
name: "sc_newp86cfunctional"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_newp86cfunctional/"
description: "sc::NewP86CFunctional –"
---

<p>sc::NewP86CFunctional &#8211; </p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::DenFunctional</code>.</p>
<h3>Public Member Functions</h3>
<p> <code>NewP86CFunctional</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;) </p>
<p> <code>NewP86CFunctional</code> (<code>StateIn</code> &amp;) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 int <code>need_density_gradient</code> () </p>
<p> void <code>point</code> (const <code>PointInputData</code> &amp;, <code>PointOutputData</code> &amp;) </p>
<h3>Protected Member Functions</h3>
<p> void <code>init_constants</code> () </p>
<p> double <code>rho_deriv</code> (double rho_a, double rho_b, double mdr) </p>
<p> double <code>gab_deriv</code> (double rho_a, double rho_b, double mdr) </p>
<h3>Protected Attributes</h3>
<p> double <code>a_</code> </p>
<p> double <code>C1_</code> </p>
<p> double <code>C2_</code> </p>
<p> double <code>C3_</code> </p>
<p> double <code>C4_</code> </p>
<p> double <code>C5_</code> </p>
<p> double <code>C6_</code> </p>
<p> double <code>C7_</code> </p>
<h2>Member Function Documentation</h2>
<h3>void sc::NewP86CFunctional::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p> Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::DenFunctional</code>. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for MPQC from the source code.</p>
