---
title: "sc_locallbgbuild(3)"
name: "sc_locallbgbuild"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_locallbgbuild/"
description: "sc::LocalLBGBuild –"
---

<p>sc::LocalLBGBuild &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::GBuild&lt; T &gt;</code>.</p>
<h3>Public Member Functions</h3>
<p><code>LocalLBGBuild</code> (T &amp;t, const <code>Ref</code>&lt; <code>TwoBodyInt</code> &gt; &amp;tbi, const <code>Ref</code>&lt; <code>Integral</code> &gt; &amp;ints, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;bs, const <code>Ref</code>&lt; <code>MessageGrp</code> &gt; &amp;g, signed char *pm) </p>
<p> void <code>build_gmat</code> (double accuracy)</p>
<h3>Protected Attributes</h3>
<p><code>Ref</code>&lt; <code>MessageGrp</code> &gt; <code>grp_</code> </p>
<p> <code>Ref</code>&lt; <code>TwoBodyInt</code> &gt; <code>tbi_</code> </p>
<p> <code>Ref</code>&lt; <code>Integral</code> &gt; <code>integral_</code> </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>gbs_</code> </p>
<p> signed char * <code>pmax</code></p>
<h3>template&lt;class T&gt; class sc::LocalLBGBuild&lt; T &gt;</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
