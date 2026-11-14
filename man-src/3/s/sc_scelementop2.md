---
title: "sc_scelementop2(3)"
name: "sc_scelementop2"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_scelementop2/"
description: "sc::SCElementOp2 –"
---

<p>sc::SCElementOp2 &#8211; </p>
<p> The <code>SCElementOp2</code> class is very similar to the <code>SCElementOp</code> class except that pairs of blocks are treated simultaneously.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;elemop.h&gt;</code></pre>
<p> Inherits <code>sc::SavableState</code>. Inherited by <code>sc::BlockedSCElementOp2</code>, <code>sc::SCDestructiveElementProduct</code>, <code>sc::SCElementScalarProduct</code>, and <code>sc::SCFEnergy</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>SCElementOp2 (StateIn &amp;s)



virtual int has_collect ()



virtual void defer_collect (int)



virtual int has_side_effects ()



virtual int has_side_effects_in_arg ()



virtual void collect (const Ref&lt; MessageGrp &gt; &amp;)



virtual void process (SCMatrixBlockIter &amp;, SCMatrixBlockIter &amp;)=0



void process_base (SCMatrixBlock *, SCMatrixBlock *)



virtual void process_spec_rect (SCMatrixRectBlock *, SCMatrixRectBlock *)



virtual void process_spec_ltri (SCMatrixLTriBlock *, SCMatrixLTriBlock *)



virtual void process_spec_diag (SCMatrixDiagBlock *, SCMatrixDiagBlock *)



virtual void process_spec_vsimp (SCVectorSimpleBlock *, SCVectorSimpleBlock *)</code></pre>
<h2>Detailed Description</h2>
<p>The <code>SCElementOp2</code> class is very similar to the <code>SCElementOp</code> class except that pairs of blocks are treated simultaneously. </p>
<p> The two matrices involved must have identical storage layout, which will be the case if both matrices are of the same type and dimensions.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
