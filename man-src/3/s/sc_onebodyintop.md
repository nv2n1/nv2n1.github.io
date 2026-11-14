---
title: "sc_onebodyintop(3)"
name: "sc_onebodyintop"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_onebodyintop/"
description: "sc::OneBodyIntOp –"
---

<p>sc::OneBodyIntOp &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::SCElementOp</code>.</p>
<h3>Public Member Functions</h3>
<p><code>OneBodyIntOp</code> (const <code>Ref</code>&lt; <code>OneBodyInt</code> &gt; &amp;) </p>
<p> <code>OneBodyIntOp</code> (const <code>Ref</code>&lt; <code>OneBodyIntIter</code> &gt; &amp;) </p>
<p> void <code>process</code> (<code>SCMatrixBlockIter</code> &amp;)<br />
 <i>This is the fallback routine to process blocks and is called by process_spec members that are not overridden. </i><br />
 void <code>process_spec_rect</code> (<code>SCMatrixRectBlock</code> *)<br />
 <i>Matrices should call these members when the type of block is known. </i><br />
 void <code>process_spec_ltri</code> (<code>SCMatrixLTriBlock</code> *) </p>
<p> void <code>process_spec_rectsub</code> (<code>SCMatrixRectSubBlock</code> *) </p>
<p> void <code>process_spec_ltrisub</code> (<code>SCMatrixLTriSubBlock</code> *) </p>
<p> bool <code>cloneable</code> ()<br />
 <i>Returns true if this </i><code>SCElementOp</code> supports the cloneable member.<br />
 <code>Ref</code>&lt; <code>SCElementOp</code> &gt; <code>clone</code> ()<br />
 <i>Returns a clone of this object. </i><br />
 int <code>has_side_effects</code> ()<br />
 <i>By default this returns nonzero. </i></p>
<h3>Protected Attributes</h3>
<p><code>Ref</code>&lt; <code>OneBodyIntIter</code> &gt; <code>iter</code></p>
<h2>Member Function Documentation</h2>
<h3><code>Ref</code>&lt;<code>SCElementOp</code>&gt; sc::OneBodyIntOp::clone () [virtual]</h3>
<p>Returns a clone of this object. This is needed for multithreaded use of <code>SCElementOp</code> objects that are not thread safe. The default implemenation throws an exception. </p>
<p> Reimplemented from <code>sc::SCElementOp</code>.</p>
<h3>bool sc::OneBodyIntOp::cloneable () [virtual]</h3>
<p>Returns true if this <code>SCElementOp</code> supports the cloneable member. The default implmentation returns false. </p>
<p> Reimplemented from <code>sc::SCElementOp</code>.</p>
<h3>int sc::OneBodyIntOp::has_side_effects () [virtual]</h3>
<p>By default this returns nonzero. If the ElementOp specialization will change any elements of the matrix, then this must be overridden to return nonzero. </p>
<p> Reimplemented from <code>sc::SCElementOp</code>.</p>
<h3>void sc::OneBodyIntOp::process (<code>SCMatrixBlockIter</code> &amp;) [virtual]</h3>
<p>This is the fallback routine to process blocks and is called by process_spec members that are not overridden. </p>
<p> Implements <code>sc::SCElementOp</code>.</p>
<h3>void sc::OneBodyIntOp::process_spec_rect (<code>SCMatrixRectBlock</code> *) [virtual]</h3>
<p>Matrices should call these members when the type of block is known. ElementOp specializations should override these when efficiency is important, since these give the most efficient access to the elements of the block. </p>
<p> Reimplemented from <code>sc::SCElementOp</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
