---
title: "sc_efcopt(3)"
name: "sc_efcopt"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_efcopt/"
description: "sc::EFCOpt –"
---

<p>sc::EFCOpt &#8211; </p>
<p> The <code>EFCOpt</code> class implements eigenvector following as described by Baker in J.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;efc.h&gt;</code></pre>
<p> Inherits <code>sc::Optimize</code>.</p>
<h3>Public Member Functions</h3>
<p><code>EFCOpt</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)<br />
 <i>The </i><code>KeyVal</code> constructor reads the following keywords:.<br />
 <code>EFCOpt</code> (<code>StateIn</code> &amp;) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 void <code>apply_transform</code> (const <code>Ref</code>&lt; <code>NonlinearTransform</code> &gt; &amp;) </p>
<p> void <code>init</code> ()<br />
 <i>Initialize the optimizer. </i><br />
 int <code>update</code> ()<br />
 <i>Take a step. </i></p>
<h3>Protected Attributes</h3>
<pre><code>int tstate



int modef



double maxabs_gradient



double convergence_



double accuracy_



RefSymmSCMatrix hessian_



Ref&lt; HessianUpdate &gt; update_



RefSCVector last_mode_</code></pre>
<h2>Detailed Description</h2>
<p>The <code>EFCOpt</code> class implements eigenvector following as described by Baker in J. </p>
<p> Comput. Chem., Vol 7, No 4, 385-395, 1986.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::EFCOpt::EFCOpt (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p>The <code>KeyVal</code> constructor reads the following keywords:. .IP &quot;update&quot; 1c This gives an <code>HessianUpdate</code> object. The default is to not update the hessian. </p>
<dl>
<dt>transition_state</p>
<dd>If this is true than a transition state search will be performed. The default is false.</dl>
<dl>
<dt>mode_following</p>
<dd>If this is true, then the initial search direction for a transition state search will be choosen to similar to the first coordinate of the <code>Function</code>. The default is false.</dl>
<dl>
<dt>hessian</p>
<dd>By default, the guess hessian is obtained from the <code>Function</code> object. This keyword specifies an lower triangle array (the second index must be less than or equal to than the first) that replaces the guess hessian. If some of the elements are not given, elements from the guess hessian will be used.</dl>
<dl>
<dt>accuracy</p>
<dd>The accuracy with which the first gradient will be computed. If this is too large, it may be necessary to evaluate the first gradient <code>point</code> twice. If it is too small, it may take longer to evaluate the first <code>point</code>. The default is 0.0001.</dl>
<h2>Member Function Documentation</h2>
<h3>void sc::EFCOpt::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::Optimize</code>.</p>
<h3>int sc::EFCOpt::update () [virtual]</h3>
<p>Take a step. Returns 1 if the optimization has converged, otherwise 0. </p>
<p> Implements <code>sc::Optimize</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
