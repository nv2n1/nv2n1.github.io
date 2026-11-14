---
title: "sc_scelementop3(3)"
name: "sc_scelementop3"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_scelementop3/"
description: "sc::SCElementOp3 –"
---

<p>sc::SCElementOp3 &#8211; </p>
<p> The <code>SCElementOp3</code> class is very similar to the <code>SCElementOp</code> class except that a triplet of blocks is treated simultaneously.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;elemop.h&gt;</code></pre>
<p> Inherits <code>sc::SavableState</code>. Inherited by <code>sc::BlockedSCElementOp3</code>, and <code>sc::OneBody3IntOp</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>SCElementOp3 (StateIn &amp;s)



virtual int has_collect ()



virtual void defer_collect (int)



virtual int has_side_effects ()



virtual int has_side_effects_in_arg1 ()



virtual int has_side_effects_in_arg2 ()



virtual void collect (const Ref&lt; MessageGrp &gt; &amp;)



virtual void process (SCMatrixBlockIter &amp;, SCMatrixBlockIter &amp;, SCMatrixBlockIter &amp;)=0



void process_base (SCMatrixBlock *, SCMatrixBlock *, SCMatrixBlock *)



virtual void process_spec_rect (SCMatrixRectBlock *, SCMatrixRectBlock *, SCMatrixRectBlock *)



virtual void process_spec_ltri (SCMatrixLTriBlock *, SCMatrixLTriBlock *, SCMatrixLTriBlock *)



virtual void process_spec_diag (SCMatrixDiagBlock *, SCMatrixDiagBlock *, SCMatrixDiagBlock *)



virtual void process_spec_vsimp (SCVectorSimpleBlock *, SCVectorSimpleBlock *, SCVectorSimpleBlock *)</code></pre>
<h2>Detailed Description</h2>
<p>The <code>SCElementOp3</code> class is very similar to the <code>SCElementOp</code> class except that a triplet of blocks is treated simultaneously. </p>
<p> The three matrices involved must have identical storage layout, which will be the case if all matrices are of the same type and dimensions.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
