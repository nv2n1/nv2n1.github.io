---
title: "sc_onebodyintcca(3)"
name: "sc_onebodyintcca"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_onebodyintcca/"
description: "sc::OneBodyIntCCA –"
---

<p>sc::OneBodyIntCCA &#8211; </p>
<p> This implements one body integrals through the CCA interface.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;obintcca.h&gt;</code></pre>
<p> Inherits <code>sc::OneBodyInt</code>.</p>
<h3>Public Member Functions</h3>
<p><code>OneBodyIntCCA</code> (<code>Integral</code> *, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;, IntegralEvaluatorFactory, IntegralFunction, bool) </p>
<p> void <code>compute_shell</code> (int, int)<br />
 <i>Computes the integrals between basis functions in the given shell pair. </i><br />
 bool <code>cloneable</code> ()<br />
 <i>Return true if the clone member can be called. </i><br />
 <code>Ref</code>&lt; <code>OneBodyInt</code> &gt; <code>clone</code> ()<br />
 <i>Returns a clone of this. </i></p>
<h3>Protected Types</h3>
<p>typedef void(sc::Int1eCCA::* <code>IntegralFunction</code> )(int, int)</p>
<h3>Protected Attributes</h3>
<p><code>Ref</code>&lt; <code>sc::Int1eCCA</code> &gt; <code>int1ecca_</code> </p>
<p> IntegralFunction <code>intfunc_</code></p>
<h2>Detailed Description</h2>
<p>This implements one body integrals through the CCA interface. </p>
<p> It is given a function pointer to the IntCCA member that computes the particular integral of interest.</p>
<h2>Member Function Documentation</h2>
<h3><code>Ref</code>&lt;<code>OneBodyInt</code>&gt; sc::OneBodyIntCCA::clone () [virtual]</h3>
<p>Returns a clone of this. The default implementation throws an exception. </p>
<p> Reimplemented from <code>sc::OneBodyInt</code>.</p>
<h3>bool sc::OneBodyIntCCA::cloneable () [virtual]</h3>
<p>Return true if the clone member can be called. The default implementation returns false. </p>
<p> Reimplemented from <code>sc::OneBodyInt</code>.</p>
<h3>void sc::OneBodyIntCCA::compute_shell (int, int) [virtual]</h3>
<p>Computes the integrals between basis functions in the given shell pair. </p>
<p> Implements <code>sc::OneBodyInt</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
