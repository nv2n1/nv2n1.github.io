---
title: "sc_scmatrixcompositesubblockiter(3)"
name: "sc_scmatrixcompositesubblockiter"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_scmatrixcompositesubblockiter/"
description: "sc::SCMatrixCompositeSubblockIter –"
---

<p>sc::SCMatrixCompositeSubblockIter &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::SCMatrixSubblockIter</code>.</p>
<h3>Public Member Functions</h3>
<p><code>SCMatrixCompositeSubblockIter</code> (Access, int niter) </p>
<p> <code>SCMatrixCompositeSubblockIter</code> (<code>Ref</code>&lt; <code>SCMatrixSubblockIter</code> &gt; &amp;, <code>Ref</code>&lt; <code>SCMatrixSubblockIter</code> &gt; &amp;) </p>
<p> void <code>set_iter</code> (int i, const <code>Ref</code>&lt; <code>SCMatrixSubblockIter</code> &gt; &amp;) </p>
<p> void <code>begin</code> ()<br />
 <i>Start at the beginning. </i><br />
 int <code>ready</code> ()<br />
 <i>Returns nonzero if there is another block. </i><br />
 void <code>next</code> ()<br />
 <i>Proceed to the next block. </i><br />
 <code>SCMatrixBlock</code> * <code>block</code> ()<br />
 <i>Return the current block. </i><br />
 int <code>current_block</code> () const</p>
<h3>Protected Attributes</h3>
<pre><code>int niters_



Ref&lt; SCMatrixSubblockIter &gt; * iters_



int iiter_
</code></pre>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
