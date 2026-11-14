---
title: "sc_symmscmatrixscextraperror(3)"
name: "sc_symmscmatrixscextraperror"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_symmscmatrixscextraperror/"
description: "sc::SymmSCMatrixSCExtrapError –"
---

<p>sc::SymmSCMatrixSCExtrapError &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::SCExtrapError</code>.</p>
<h3>Public Member Functions</h3>
<p><code>SymmSCMatrixSCExtrapError</code> (<code>StateIn</code> &amp;) </p>
<p> <code>SymmSCMatrixSCExtrapError</code> (const <code>RefSymmSCMatrix</code> &amp;) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 double <code>error</code> ()<br />
 <i>Returns some measure of the total error. </i><br />
 double <code>scalar_product</code> (const <code>Ref</code>&lt; <code>SCExtrapError</code> &gt; &amp;)</p>
<h2>Member Function Documentation</h2>
<h3>void sc::SymmSCMatrixSCExtrapError::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SCExtrapError</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
