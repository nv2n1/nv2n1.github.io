---
title: "sc_onebodysoint(3)"
name: "sc_onebodysoint"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_onebodysoint/"
description: "sc::OneBodySOInt –"
---

<p>sc::OneBodySOInt &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::RefCount</code>.</p>
<h3>Public Member Functions</h3>
<p><code>OneBodySOInt</code> (const <code>Ref</code>&lt; <code>OneBodyInt</code> &gt; &amp;) </p>
<p> <code>Ref</code>&lt; <code>SOBasis</code> &gt; <code>basis</code> () const </p>
<p> <code>Ref</code>&lt; <code>SOBasis</code> &gt; <code>basis1</code> () const </p>
<p> <code>Ref</code>&lt; <code>SOBasis</code> &gt; <code>basis2</code> () const </p>
<p> const double * <code>buffer</code> () const </p>
<p> virtual void <code>compute_shell</code> (int, int) </p>
<p> virtual void <code>reinitialize</code> () </p>
<p> int <code>only_totally_symmetric</code> () const </p>
<p> void <code>set_only_totally_symmetric</code> (int i)</p>
<h3>Protected Attributes</h3>
<p><code>Ref</code>&lt; <code>OneBodyInt</code> &gt; <code>ob_</code> </p>
<p> <code>Ref</code>&lt; <code>SOBasis</code> &gt; <code>b1_</code> </p>
<p> <code>Ref</code>&lt; <code>SOBasis</code> &gt; <code>b2_</code> </p>
<p> double * <code>buffer_</code> </p>
<p> int <code>only_totally_symmetric_</code> </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
