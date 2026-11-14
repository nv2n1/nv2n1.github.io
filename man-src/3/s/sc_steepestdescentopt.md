---
title: "sc_steepestdescentopt(3)"
name: "sc_steepestdescentopt"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_steepestdescentopt/"
description: "sc::SteepestDescentOpt –"
---

<p>sc::SteepestDescentOpt &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::Optimize</code>.</p>
<h3>Public Member Functions</h3>
<p><code>SteepestDescentOpt</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;) </p>
<p> <code>SteepestDescentOpt</code> (<code>StateIn</code> &amp;) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 void <code>init</code> ()<br />
 <i>Initialize the optimizer. </i><br />
 int <code>update</code> ()<br />
 <i>Take a step. </i></p>
<h3>Protected Attributes</h3>
<pre><code>double maxabs_gradient



double accuracy_



Ref&lt; LineOpt &gt; lineopt_



int take_newton_step_



int print_x_



int print_gradient_</code></pre>
<h2>Member Function Documentation</h2>
<h3>void sc::SteepestDescentOpt::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::Optimize</code>.</p>
<h3>int sc::SteepestDescentOpt::update () [virtual]</h3>
<p>Take a step. Returns 1 if the optimization has converged, otherwise 0. </p>
<p> Implements <code>sc::Optimize</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
