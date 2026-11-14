---
title: "sc_guessmolecularhessian(3)"
name: "sc_guessmolecularhessian"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_guessmolecularhessian/"
description: "sc::GuessMolecularHessian –"
---

<p>sc::GuessMolecularHessian &#8211; </p>
<p> <code>GuessMolecularHessian</code> is an implementation of <code>MolecularHessian</code> that estimates the hessian based on the internal coordinates.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;hess.h&gt;</code></pre>
<p> Inherits <code>sc::MolecularHessian</code>.</p>
<h3>Public Member Functions</h3>
<p><code>GuessMolecularHessian</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)<br />
 <i>The </i><code>GuessMolecularHessian</code> <code>KeyVal</code> constructor is used to generate a <code>GuessMolecularHessian</code> object from the input.<br />
 <code>GuessMolecularHessian</code> (<code>StateIn</code> &amp;) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 <code>RefSymmSCMatrix</code> <code>cartesian_hessian</code> ()<br />
 <i>Return the hessian in cartesian coordinates. </i></p>
<h3>Protected Attributes</h3>
<p><code>Ref</code>&lt; <code>MolecularCoor</code> &gt; <code>coor_</code></p>
<h2>Detailed Description</h2>
<p><code>GuessMolecularHessian</code> is an implementation of <code>MolecularHessian</code> that estimates the hessian based on the internal coordinates.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::GuessMolecularHessian::GuessMolecularHessian (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p>The <code>GuessMolecularHessian</code> <code>KeyVal</code> constructor is used to generate a <code>GuessMolecularHessian</code> object from the input. It reads the keywords below. </p>
<p> KeywordTypeDefaultDescription coor<code>MolecularCoor</code>noneThis gives the <code>MolecularCoor</code> object that is used to generate the guess hessian. It does not have to be the same <code>MolecularCoor</code> object that is used to optimize the molecule.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::GuessMolecularHessian::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::MolecularHessian</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
