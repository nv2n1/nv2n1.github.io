---
title: "sc_distscmatrixlistsubblockiter(3)"
name: "sc_distscmatrixlistsubblockiter"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_distscmatrixlistsubblockiter/"
description: "sc::DistSCMatrixListSubblockIter –"
---

<p>sc::DistSCMatrixListSubblockIter &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::SCMatrixListSubblockIter</code>.</p>
<h3>Public Member Functions</h3>
<p><code>DistSCMatrixListSubblockIter</code> (Access, const <code>Ref</code>&lt; <code>SCMatrixBlockList</code> &gt; &amp;locallist, const <code>Ref</code>&lt; <code>MessageGrp</code> &gt; &amp;grp) </p>
<p> void <code>begin</code> ()<br />
 <i>Start at the beginning. </i><br />
 void <code>next</code> ()<br />
 <i>Proceed to the next block. </i></p>
<h3>Protected Member Functions</h3>
<pre><code>void maybe_advance_list ()



void advance_list ()



Protected Attributes</code></pre>
<p> <code>Ref</code>&lt; <code>MessageGrp</code> &gt; <code>grp_</code> </p>
<p> <code>StateSend</code> <code>out_</code> </p>
<p> <code>StateRecv</code> <code>in_</code> </p>
<p> int <code>step_</code> </p>
<p> <code>Ref</code>&lt; <code>SCMatrixBlockList</code> &gt; <code>locallist_</code> </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
