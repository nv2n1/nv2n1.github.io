---
title: "sc_scelementop(3)"
name: "sc_scelementop"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_scelementop/"
description: "sc::SCElementOp –"
---

<p>sc::SCElementOp &#8211; </p>
<p> Objects of class <code>SCElementOp</code> are used to perform operations on the elements of matrices.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;elemop.h&gt;</code></pre>
<p> Inherits <code>sc::SavableState</code>. Inherited by <code>sc::BlockedSCElementOp</code>, <code>sc::OneBodyIntOp</code>, <code>sc::SCElementAccumulateDiagSCMatrix</code>, <code>sc::SCElementAccumulateSCMatrix</code>, <code>sc::SCElementAccumulateSCVector</code>, <code>sc::SCElementAccumulateSymmSCMatrix</code>, <code>sc::SCElementAssign</code>, <code>sc::SCElementDot</code>, <code>sc::SCElementInvert</code>, <code>sc::SCElementKNorm</code>, <code>sc::SCElementMaxAbs</code>, <code>sc::SCElementMinAbs</code>, <code>sc::SCElementRandomize</code>, <code>sc::SCElementScale</code>, <code>sc::SCElementScaleDiagonal</code>, <code>sc::SCElementShiftDiagonal</code>, <code>sc::SCElementSquareRoot</code>, and <code>sc::SCElementSumAbs</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>SCElementOp (StateIn &amp;s)



virtual int has_collect ()


If duplicates of the SCElementOp exist (that is, there is more than one node), then if has_collect returns nonzero then collect is called with a MessageGrp reference after all of the blocks have been processed.


virtual void defer_collect (int)



virtual void collect (const Ref&lt; MessageGrp &gt; &amp;)



virtual void collect (const Ref&lt; SCElementOp &gt; &amp;)


Multithreaded use of cloneable SCElementOp objects requires that data from cloned objects be collected.


virtual int has_side_effects ()


By default this returns nonzero.


virtual bool threadsafe ()


Returns true if this SCElementOp is threadsafe.


virtual bool cloneable ()


Returns true if this SCElementOp supports the cloneable member.


virtual Ref&lt; SCElementOp &gt; clone ()


Returns a clone of this object.


virtual void process (SCMatrixBlockIter &amp;)=0


This is the fallback routine to process blocks and is called by process_spec members that are not overridden.


void process_base (SCMatrixBlock *block)


Lazy matrix implementors can call this member when the type of block specialization is unknown.


virtual void process_spec_rect (SCMatrixRectBlock *)


Matrices should call these members when the type of block is known.


virtual void process_spec_ltri (SCMatrixLTriBlock *)



virtual void process_spec_diag (SCMatrixDiagBlock *)



virtual void process_spec_vsimp (SCVectorSimpleBlock *)



virtual void process_spec_rectsub (SCMatrixRectSubBlock *)



virtual void process_spec_ltrisub (SCMatrixLTriSubBlock *)



virtual void process_spec_diagsub (SCMatrixDiagSubBlock *)



virtual void process_spec_vsimpsub (SCVectorSimpleSubBlock *)</code></pre>
<h2>Detailed Description</h2>
<p>Objects of class <code>SCElementOp</code> are used to perform operations on the elements of matrices. </p>
<p> When the <code>SCElementOp</code> object is given to the element_op member of a matrix, each block the matrix is passed to one of the process, process_base, or process_base members.</p>
<h2>Member Function Documentation</h2>
<h3>virtual <code>Ref</code>&lt;<code>SCElementOp</code>&gt; sc::SCElementOp::clone () [virtual]</h3>
<p>Returns a clone of this object. This is needed for multithreaded use of <code>SCElementOp</code> objects that are not thread safe. The default implemenation throws an exception. </p>
<p> Reimplemented in <code>sc::OneBodyIntOp</code>.</p>
<h3>virtual bool sc::SCElementOp::cloneable () [virtual]</h3>
<p>Returns true if this <code>SCElementOp</code> supports the cloneable member. The default implmentation returns false. </p>
<p> Reimplemented in <code>sc::OneBodyIntOp</code>.</p>
<h3>virtual void sc::SCElementOp::collect (const <code>Ref</code>&lt; <code>SCElementOp</code> &gt; &amp;) [virtual]</h3>
<p>Multithreaded use of cloneable <code>SCElementOp</code> objects requires that data from cloned objects be collected. The default implementation will throw an exception.</p>
<h3>virtual int sc::SCElementOp::has_collect () [virtual]</h3>
<p>If duplicates of the <code>SCElementOp</code> exist (that is, there is more than one node), then if has_collect returns nonzero then collect is called with a <code>MessageGrp</code> reference after all of the blocks have been processed. The default return value of has_collect is 0 and collect&#8217;s default action is do nothing. If defer_collect member is called with nonzero, collect will do nothing (this is only used by the blocked matrices). </p>
<p> Reimplemented in <code>sc::SCElementInvert</code>, <code>sc::SCElementMaxAbs</code>, <code>sc::SCElementMinAbs</code>, <code>sc::SCElementSumAbs</code>, and <code>sc::SCElementKNorm</code>.</p>
<h3>virtual int sc::SCElementOp::has_side_effects () [virtual]</h3>
<p>By default this returns nonzero. If the ElementOp specialization will change any elements of the matrix, then this must be overridden to return nonzero. </p>
<p> Reimplemented in <code>sc::OneBodyIntOp</code>, <code>sc::LevelShift</code>, <code>sc::SCElementScale</code>, <code>sc::SCElementRandomize</code>, <code>sc::SCElementAssign</code>, <code>sc::SCElementSquareRoot</code>, <code>sc::SCElementInvert</code>, <code>sc::SCElementScaleDiagonal</code>, <code>sc::SCElementShiftDiagonal</code>, <code>sc::SCElementDot</code>, <code>sc::SCElementAccumulateSCMatrix</code>, <code>sc::SCElementAccumulateSymmSCMatrix</code>, <code>sc::SCElementAccumulateDiagSCMatrix</code>, and <code>sc::SCElementAccumulateSCVector</code>.</p>
<h3>virtual void sc::SCElementOp::process (<code>SCMatrixBlockIter</code> &amp;) [pure virtual]</h3>
<p>This is the fallback routine to process blocks and is called by process_spec members that are not overridden. </p>
<p> Implemented in <code>sc::OneBodyIntOp</code>, <code>sc::LevelShift</code>, <code>sc::ALevelShift</code>, <code>sc::BLevelShift</code>, <code>sc::SCElementScale</code>, <code>sc::SCElementRandomize</code>, <code>sc::SCElementAssign</code>, <code>sc::SCElementSquareRoot</code>, <code>sc::SCElementInvert</code>, <code>sc::SCElementScaleDiagonal</code>, <code>sc::SCElementShiftDiagonal</code>, <code>sc::SCElementMaxAbs</code>, <code>sc::SCElementMinAbs</code>, <code>sc::SCElementSumAbs</code>, <code>sc::SCElementKNorm</code>, <code>sc::SCElementDot</code>, <code>sc::SCElementAccumulateSCMatrix</code>, <code>sc::SCElementAccumulateSymmSCMatrix</code>, <code>sc::SCElementAccumulateDiagSCMatrix</code>, and <code>sc::SCElementAccumulateSCVector</code>.</p>
<h3>void sc::SCElementOp::process_base (<code>SCMatrixBlock</code> * block)</h3>
<p>Lazy matrix implementors can call this member when the type of block specialization is unknown. However, this will attempt to dynamic_cast block to a block specialization and will thus be less efficient.</p>
<h3>virtual void sc::SCElementOp::process_spec_rect (<code>SCMatrixRectBlock</code> *) [virtual]</h3>
<p>Matrices should call these members when the type of block is known. ElementOp specializations should override these when efficiency is important, since these give the most efficient access to the elements of the block. </p>
<p> Reimplemented in <code>sc::OneBodyIntOp</code>.</p>
<h3>virtual bool sc::SCElementOp::threadsafe () [virtual]</h3>
<p>Returns true if this <code>SCElementOp</code> is threadsafe. The default implementation returns false.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
