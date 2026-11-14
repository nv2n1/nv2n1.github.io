---
title: "sc_onebody3intop(3)"
name: "sc_onebody3intop"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_onebody3intop/"
description: "sc::OneBody3IntOp –"
---

<p>sc::OneBody3IntOp &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::SCElementOp3</code>.</p>
<h3>Public Member Functions</h3>
<p><code>OneBody3IntOp</code> (const <code>Ref</code>&lt; <code>OneBodyInt</code> &gt; &amp;b) </p>
<p> <code>OneBody3IntOp</code> (const <code>Ref</code>&lt; <code>OneBodyIntIter</code> &gt; &amp;) </p>
<p> void <code>process</code> (<code>SCMatrixBlockIter</code> &amp;, <code>SCMatrixBlockIter</code> &amp;, <code>SCMatrixBlockIter</code> &amp;) </p>
<p> void <code>process_spec_rect</code> (<code>SCMatrixRectBlock</code> *, <code>SCMatrixRectBlock</code> *, <code>SCMatrixRectBlock</code> *) </p>
<p> void <code>process_spec_ltri</code> (<code>SCMatrixLTriBlock</code> *, <code>SCMatrixLTriBlock</code> *, <code>SCMatrixLTriBlock</code> *) </p>
<p> int <code>has_side_effects</code> () </p>
<p> int <code>has_side_effects_in_arg1</code> () </p>
<p> int <code>has_side_effects_in_arg2</code> () </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
