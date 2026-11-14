---
title: "sc_blockedscmatrixkit(3)"
name: "sc_blockedscmatrixkit"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_blockedscmatrixkit/"
description: "sc::BlockedSCMatrixKit –"
---

<p>sc::BlockedSCMatrixKit &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::SCMatrixKit</code>.</p>
<h3>Public Member Functions</h3>
<p><code>BlockedSCMatrixKit</code> (const <code>Ref</code>&lt; <code>SCMatrixKit</code> &gt; &amp;subkit) </p>
<p> <code>BlockedSCMatrixKit</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;) </p>
<p> <code>SCMatrix</code> * <code>matrix</code> (const <code>RefSCDimension</code> &amp;, const <code>RefSCDimension</code> &amp;)<br />
 <i>Given the dimensions, create matrices or vectors. </i><br />
 <code>SymmSCMatrix</code> * <code>symmmatrix</code> (const <code>RefSCDimension</code> &amp;) </p>
<p> <code>DiagSCMatrix</code> * <code>diagmatrix</code> (const <code>RefSCDimension</code> &amp;) </p>
<p> <code>SCVector</code> * <code>vector</code> (const <code>RefSCDimension</code> &amp;) </p>
<p> <code>Ref</code>&lt; <code>SCMatrixKit</code> &gt; <code>subkit</code> () </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
