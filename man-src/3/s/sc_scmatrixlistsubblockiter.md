---
title: "sc_scmatrixlistsubblockiter(3)"
name: "sc_scmatrixlistsubblockiter"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_scmatrixlistsubblockiter/"
description: "sc::SCMatrixListSubblockIter –"
---

<p>sc::SCMatrixListSubblockIter &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::SCMatrixSubblockIter</code>. Inherited by <code>sc::DistSCMatrixListSubblockIter</code>, and <code>sc::ReplSCMatrixListSubblockIter</code>.</p>
<h3>Public Member Functions</h3>
<p><code>SCMatrixListSubblockIter</code> (Access, const <code>Ref</code>&lt; <code>SCMatrixBlockList</code> &gt; &amp;list) </p>
<p> void <code>begin</code> ()<br />
 <i>Start at the beginning. </i><br />
 int <code>ready</code> ()<br />
 <i>Returns nonzero if there is another block. </i><br />
 void <code>next</code> ()<br />
 <i>Proceed to the next block. </i><br />
 <code>SCMatrixBlock</code> * <code>block</code> ()<br />
 <i>Return the current block. </i></p>
<h3>Protected Attributes</h3>
<p><code>Ref</code>&lt; <code>SCMatrixBlockList</code> &gt; <code>list_</code> </p>
<p> <code>SCMatrixBlockListIter</code> <code>iter_</code> </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
