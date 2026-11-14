---
title: "sc_twobodysoint(3)"
name: "sc_twobodysoint"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_twobodysoint/"
description: "sc::TwoBodySOInt –"
---

<p>sc::TwoBodySOInt &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::RefCount</code>.</p>
<h3>Public Member Functions</h3>
<p><code>TwoBodySOInt</code> (const <code>Ref</code>&lt; <code>TwoBodyInt</code> &gt; &amp;) </p>
<p> <code>Ref</code>&lt; <code>SOBasis</code> &gt; <code>basis</code> () const </p>
<p> <code>Ref</code>&lt; <code>SOBasis</code> &gt; <code>basis1</code> () const </p>
<p> <code>Ref</code>&lt; <code>SOBasis</code> &gt; <code>basis2</code> () const </p>
<p> <code>Ref</code>&lt; <code>SOBasis</code> &gt; <code>basis3</code> () const </p>
<p> <code>Ref</code>&lt; <code>SOBasis</code> &gt; <code>basis4</code> () const </p>
<p> const double * <code>buffer</code> () const </p>
<p> virtual void <code>compute_shell</code> (int, int, int, int) </p>
<p> int <code>redundant</code> () const </p>
<p> int <code>only_totally_symmetric</code> () const </p>
<p> void <code>set_only_totally_symmetric</code> (int i)</p>
<h3>Protected Attributes</h3>
<p><code>Ref</code>&lt; <code>TwoBodyInt</code> &gt; <code>tb_</code> </p>
<p> <code>Ref</code>&lt; <code>SOBasis</code> &gt; <code>b1_</code> </p>
<p> <code>Ref</code>&lt; <code>SOBasis</code> &gt; <code>b2_</code> </p>
<p> <code>Ref</code>&lt; <code>SOBasis</code> &gt; <code>b3_</code> </p>
<p> <code>Ref</code>&lt; <code>SOBasis</code> &gt; <code>b4_</code> </p>
<p> double * <code>buffer_</code> </p>
<p> int <code>redundant_</code> </p>
<p> int <code>only_totally_symmetric_</code> </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
