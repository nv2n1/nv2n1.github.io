---
title: "sc_twobodymointstransform_ikjy(3)"
name: "sc_twobodymointstransform_ikjy"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_twobodymointstransform_ikjy/"
description: "sc::TwoBodyMOIntsTransform_ikjy –"
---

<p>sc::TwoBodyMOIntsTransform_ikjy &#8211; </p>
<p> <code>TwoBodyMOIntsTransform_ikjy</code> computes (ik|jy) integrals using parallel integrals-direct AO-&gt;MO transformation.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;transform_ikjy.h&gt;</code></pre>
<p> Inherits <code>sc::TwoBodyMOIntsTransform</code>.</p>
<h3>Public Member Functions</h3>
<p><code>TwoBodyMOIntsTransform_ikjy</code> (<code>StateIn</code> &amp;) </p>
<p> <code>TwoBodyMOIntsTransform_ikjy</code> (const std::string &amp;name, const <code>Ref</code>&lt; <code>MOIntsTransformFactory</code> &gt; &amp;factory, const <code>Ref</code>&lt; <code>MOIndexSpace</code> &gt; &amp;space1, const <code>Ref</code>&lt; <code>MOIndexSpace</code> &gt; &amp;space2, const <code>Ref</code>&lt; <code>MOIndexSpace</code> &gt; &amp;space3, const <code>Ref</code>&lt; <code>MOIndexSpace</code> &gt; &amp;space4) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 std::string <code>type</code> () const<br />
 <i>Implementation of </i><code>TwoBodyMOIntsTransform::type()</code>.<br />
 const size_t <code>memgrp_blksize</code> () const<br />
 <i>Returns the number of bytes allocated for each ij-block of integrals of one type in </i><code>MemoryGrp</code>.<br />
 void <code>compute</code> ()<br />
 <i>Computes transformed integrals. </i><br />
 void <code>check_int_symm</code> (double threshold=<code>TwoBodyMOIntsTransform::zero_integral</code>) const throw (ProgrammingError)<br />
 <i>Check symmetry of transformed integrals. </i></p>
<h2>Detailed Description</h2>
<p><code>TwoBodyMOIntsTransform_ikjy</code> computes (ik|jy) integrals using parallel integrals-direct AO-&gt;MO transformation.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::TwoBodyMOIntsTransform_ikjy::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::TwoBodyMOIntsTransform</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
