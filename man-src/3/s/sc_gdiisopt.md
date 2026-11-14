---
title: "sc_gdiisopt(3)"
name: "sc_gdiisopt"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_gdiisopt/"
description: "sc::GDIISOpt –"
---

<p>sc::GDIISOpt &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::Optimize</code>.</p>
<h3>Public Member Functions</h3>
<p><code>GDIISOpt</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;) </p>
<p> <code>GDIISOpt</code> (<code>StateIn</code> &amp;) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 void <code>init</code> ()<br />
 <i>Initialize the optimizer. </i><br />
 int <code>update</code> ()<br />
 <i>Take a step. </i></p>
<h3>Protected Attributes</h3>
<pre><code>int nsave



int diis_iter



double maxabs_gradient



double convergence_



double accuracy_



RefSCVector * coords_



RefSCVector * grad_



RefSCVector * error_



RefSymmSCMatrix ihessian_



Ref&lt; HessianUpdate &gt; update_</code></pre>
<h2>Member Function Documentation</h2>
<h3>void sc::GDIISOpt::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::Optimize</code>.</p>
<h3>int sc::GDIISOpt::update () [virtual]</h3>
<p>Take a step. Returns 1 if the optimization has converged, otherwise 0. </p>
<p> Implements <code>sc::Optimize</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
