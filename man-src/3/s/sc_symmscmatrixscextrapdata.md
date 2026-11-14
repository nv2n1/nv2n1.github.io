---
title: "sc_symmscmatrixscextrapdata(3)"
name: "sc_symmscmatrixscextrapdata"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_symmscmatrixscextrapdata/"
description: "sc::SymmSCMatrixSCExtrapData –"
---

<p>sc::SymmSCMatrixSCExtrapData &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::SCExtrapData</code>.</p>
<h3>Public Member Functions</h3>
<p><code>SymmSCMatrixSCExtrapData</code> (<code>StateIn</code> &amp;) </p>
<p> <code>SymmSCMatrixSCExtrapData</code> (const <code>RefSymmSCMatrix</code> &amp;) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 <code>SCExtrapData</code> * <code>copy</code> ()<br />
 <i>Return a copy of this. </i><br />
 void <code>zero</code> ()<br />
 <i>Set this to zero. </i><br />
 void <code>accumulate_scaled</code> (double, const <code>Ref</code>&lt; <code>SCExtrapData</code> &gt; &amp;)</p>
<h2>Member Function Documentation</h2>
<h3><code>SCExtrapData</code>* sc::SymmSCMatrixSCExtrapData::copy () [virtual]</h3>
<p>Return a copy of this. </p>
<p> Implements <code>sc::SCExtrapData</code>.</p>
<h3>void sc::SymmSCMatrixSCExtrapData::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SCExtrapData</code>.</p>
<h3>void sc::SymmSCMatrixSCExtrapData::zero () [virtual]</h3>
<p>Set this to zero. </p>
<p> Implements <code>sc::SCExtrapData</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
