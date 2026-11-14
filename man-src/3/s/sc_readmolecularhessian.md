---
title: "sc_readmolecularhessian(3)"
name: "sc_readmolecularhessian"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_readmolecularhessian/"
description: "sc::ReadMolecularHessian –"
---

<p>sc::ReadMolecularHessian &#8211; </p>
<p> <code>ReadMolecularHessian</code> is an implementation of <code>MolecularHessian</code> that reads the hessian from a file.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;hess.h&gt;</code></pre>
<p> Inherits <code>sc::MolecularHessian</code>.</p>
<h3>Public Member Functions</h3>
<p><code>ReadMolecularHessian</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)<br />
 <i>The </i><code>ReadMolecularHessian</code> <code>KeyVal</code> constructor is used to generate a <code>ReadMolecularHessian</code> object from the input.<br />
 <code>ReadMolecularHessian</code> (<code>StateIn</code> &amp;) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 <code>RefSymmSCMatrix</code> <code>cartesian_hessian</code> ()<br />
 <i>Return the hessian in cartesian coordinates. </i></p>
<h3>Protected Attributes</h3>
<pre><code>char * filename_</code></pre>
<h2>Detailed Description</h2>
<p><code>ReadMolecularHessian</code> is an implementation of <code>MolecularHessian</code> that reads the hessian from a file.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::ReadMolecularHessian::ReadMolecularHessian (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p>The <code>ReadMolecularHessian</code> <code>KeyVal</code> constructor is used to generate a <code>ReadMolecularHessian</code> object from the input. It reads the keywords below. </p>
<p> KeywordTypeDefaultDescription filenamestring<i>basename</i> .hessThe name of the file from which the hessian is read.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::ReadMolecularHessian::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::MolecularHessian</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
