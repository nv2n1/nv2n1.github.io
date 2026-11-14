---
title: "sc_diagmolecularhessian(3)"
name: "sc_diagmolecularhessian"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_diagmolecularhessian/"
description: "sc::DiagMolecularHessian –"
---

<p>sc::DiagMolecularHessian &#8211; </p>
<p> <code>DiagMolecularHessian</code> is an implementation of <code>MolecularHessian</code> that returns a hessian that is a diagonal matrix.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;hess.h&gt;</code></pre>
<p> Inherits <code>sc::MolecularHessian</code>.</p>
<h3>Public Member Functions</h3>
<p><code>DiagMolecularHessian</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)<br />
 <i>The </i><code>DiagMolecularHessian</code> <code>KeyVal</code> constructor is used to generate a <code>DiagMolecularHessian</code> object from the input.<br />
 <code>DiagMolecularHessian</code> (<code>StateIn</code> &amp;) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 <code>RefSymmSCMatrix</code> <code>cartesian_hessian</code> ()<br />
 <i>Return the hessian in cartesian coordinates. </i></p>
<h3>Protected Attributes</h3>
<pre><code>double diag_</code></pre>
<h2>Detailed Description</h2>
<p><code>DiagMolecularHessian</code> is an implementation of <code>MolecularHessian</code> that returns a hessian that is a diagonal matrix.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::DiagMolecularHessian::DiagMolecularHessian (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p>The <code>DiagMolecularHessian</code> <code>KeyVal</code> constructor is used to generate a <code>DiagMolecularHessian</code> object from the input. It reads the keywords below. </p>
<p> KeywordTypeDefaultDescription diagdouble1.0Specifies the diagonal elements of the hessian.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::DiagMolecularHessian::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::MolecularHessian</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
