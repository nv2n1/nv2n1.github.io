---
title: "sc_scelementaccumulatescvector(3)"
name: "sc_scelementaccumulatescvector"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_scelementaccumulatescvector/"
description: "sc::SCElementAccumulateSCVector –"
---

<p>sc::SCElementAccumulateSCVector &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::SCElementOp</code>.</p>
<h3>Public Member Functions</h3>
<p><code>SCElementAccumulateSCVector</code> (<code>SCVector</code> *) </p>
<p> int <code>has_side_effects</code> ()<br />
 <i>By default this returns nonzero. </i><br />
 void <code>process</code> (<code>SCMatrixBlockIter</code> &amp;)<br />
 <i>This is the fallback routine to process blocks and is called by process_spec members that are not overridden. </i></p>
<h2>Member Function Documentation</h2>
<h3>int sc::SCElementAccumulateSCVector::has_side_effects () [virtual]</h3>
<p>By default this returns nonzero. If the ElementOp specialization will change any elements of the matrix, then this must be overridden to return nonzero. </p>
<p> Reimplemented from <code>sc::SCElementOp</code>.</p>
<h3>void sc::SCElementAccumulateSCVector::process (<code>SCMatrixBlockIter</code> &amp;) [virtual]</h3>
<p>This is the fallback routine to process blocks and is called by process_spec members that are not overridden. </p>
<p> Implements <code>sc::SCElementOp</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
