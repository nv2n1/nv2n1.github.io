---
title: "sc_qnewtonopt(3)"
name: "sc_qnewtonopt"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_qnewtonopt/"
description: "sc::QNewtonOpt –"
---

<p>sc::QNewtonOpt &#8211; </p>
<p> The <code>QNewtonOpt</code> implements a quasi-Newton optimization scheme.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;qnewton.h&gt;</code></pre>
<p> Inherits <code>sc::Optimize</code>.</p>
<h3>Public Member Functions</h3>
<p><code>QNewtonOpt</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)<br />
 <i>The </i><code>KeyVal</code> constructor.<br />
 <code>QNewtonOpt</code> (<code>StateIn</code> &amp;) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 void <code>apply_transform</code> (const <code>Ref</code>&lt; <code>NonlinearTransform</code> &gt; &amp;) </p>
<p> void <code>init</code> ()<br />
 <i>Initialize the optimizer. </i><br />
 int <code>update</code> ()<br />
 <i>Take a step. </i></p>
<h3>Protected Attributes</h3>
<pre><code>double maxabs_gradient



double accuracy_



RefSymmSCMatrix ihessian_



Ref&lt; HessianUpdate &gt; update_



Ref&lt; LineOpt &gt; lineopt_



int take_newton_step_



int print_hessian_



int print_x_



int print_gradient_



int linear_



int restrict_



int dynamic_grad_acc_



int force_search_



int restart_</code></pre>
<h2>Detailed Description</h2>
<p>The <code>QNewtonOpt</code> implements a quasi-Newton optimization scheme.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::QNewtonOpt::QNewtonOpt (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p>The <code>KeyVal</code> constructor. The <code>KeyVal</code> constructor reads the following keywords:</p>
<dl>
<dt>update</p>
<dd>This gives a <code>HessianUpdate</code> object. The default is to not update the hessian.</dl>
<dl>
<dt>hessian</p>
<dd>By default, the guess hessian is obtained from the <code>Function</code> object. This keyword specifies an lower triangle array (the second index must be less than or equal to than the first) that replaces the guess hessian. If some of the elements are not given, elements from the guess hessian will be used.</dl>
<dl>
<dt>lineopt</p>
<dd>This gives a <code>LineOpt</code> object for doing line optimizations in the Newton direction. The default is to skip the line optimizations.</dl>
<dl>
<dt>accuracy</p>
<dd>The accuracy with which the first gradient will be computed. If this is too large, it may be necessary to evaluate the first gradient <code>point</code> twice. If it is too small, it may take longer to evaluate the first <code>point</code>. The default is 0.0001.</dl>
<dl>
<dt>print_x</p>
<dd>If true, print the coordinates each iteration. The default is false.</dl>
<dl>
<dt>print_gradient</p>
<dd>If true, print the gradient each iteration. The default is false.</dl>
<dl>
<dt>print_hessian</p>
<dd>If true, print the approximate hessian each iteration. The default is false.</dl>
<dl>
<dt>restrict</p>
<dd>Use step size restriction when not using a line search. The default is true.</dl>
<h2>Member Function Documentation</h2>
<h3>void sc::QNewtonOpt::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::Optimize</code>.</p>
<h3>int sc::QNewtonOpt::update () [virtual]</h3>
<p>Take a step. Returns 1 if the optimization has converged, otherwise 0. </p>
<p> Implements <code>sc::Optimize</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
