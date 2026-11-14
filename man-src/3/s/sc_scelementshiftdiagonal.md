---
title: "sc_scelementshiftdiagonal(3)"
name: "sc_scelementshiftdiagonal"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_scelementshiftdiagonal/"
description: "sc::SCElementShiftDiagonal –"
---

<p>sc::SCElementShiftDiagonal &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::SCElementOp</code>.</p>
<h3>Public Member Functions</h3>
<p><code>SCElementShiftDiagonal</code> (double a) </p>
<p> <code>SCElementShiftDiagonal</code> (<code>StateIn</code> &amp;) </p>
<p> int <code>has_side_effects</code> ()<br />
 <i>By default this returns nonzero. </i><br />
 void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 void <code>process</code> (<code>SCMatrixBlockIter</code> &amp;)<br />
 <i>This is the fallback routine to process blocks and is called by process_spec members that are not overridden. </i></p>
<h2>Member Function Documentation</h2>
<h3>int sc::SCElementShiftDiagonal::has_side_effects () [virtual]</h3>
<p>By default this returns nonzero. If the ElementOp specialization will change any elements of the matrix, then this must be overridden to return nonzero. </p>
<p> Reimplemented from <code>sc::SCElementOp</code>.</p>
<h3>void sc::SCElementShiftDiagonal::process (<code>SCMatrixBlockIter</code> &amp;) [virtual]</h3>
<p>This is the fallback routine to process blocks and is called by process_spec members that are not overridden. </p>
<p> Implements <code>sc::SCElementOp</code>.</p>
<h3>void sc::SCElementShiftDiagonal::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SavableState</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
