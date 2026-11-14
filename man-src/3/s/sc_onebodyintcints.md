---
title: "sc_onebodyintcints(3)"
name: "sc_onebodyintcints"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_onebodyintcints/"
description: "sc::OneBodyIntCints –"
---

<p>sc::OneBodyIntCints &#8211; </p>
<p> This implements most one body integrals in the Cints library.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;obintcints.h&gt;</code></pre>
<p> Inherits <code>sc::OneBodyInt</code>.</p>
<h3>Public Member Functions</h3>
<p><code>OneBodyIntCints</code> (<code>Integral</code> *, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;, IntegralFunction) </p>
<p> void <code>set_multipole_origin</code> (const <code>Ref</code>&lt; <code>DipoleData</code> &gt; &amp;) </p>
<p> void <code>set_EdotV_origin</code> (const <code>Ref</code>&lt; <code>EfieldDotVectorData</code> &gt; &amp;) </p>
<p> void <code>set_Q_origin</code> (const <code>Ref</code>&lt; <code>PointChargeData</code> &gt; &amp;) </p>
<p> void <code>compute_shell</code> (int, int)<br />
 <i>Computes the integrals between basis functions in the given shell pair. </i><br />
 bool <code>cloneable</code> ()<br />
 <i>Return true if the clone member can be called. </i><br />
 <code>Ref</code>&lt; <code>OneBodyInt</code> &gt; <code>clone</code> ()<br />
 <i>Returns a clone of this. </i></p>
<h2>Detailed Description</h2>
<p>This implements most one body integrals in the Cints library. </p>
<p> It is given a function pointer to the Int1e member that computes the particular integral of interest.</p>
<h2>Member Function Documentation</h2>
<h3><code>Ref</code>&lt;<code>OneBodyInt</code>&gt; sc::OneBodyIntCints::clone () [virtual]</h3>
<p>Returns a clone of this. The default implementation throws an exception. </p>
<p> Reimplemented from <code>sc::OneBodyInt</code>.</p>
<h3>bool sc::OneBodyIntCints::cloneable () [virtual]</h3>
<p>Return true if the clone member can be called. The default implementation returns false. </p>
<p> Reimplemented from <code>sc::OneBodyInt</code>.</p>
<h3>void sc::OneBodyIntCints::compute_shell (int, int) [virtual]</h3>
<p>Computes the integrals between basis functions in the given shell pair. </p>
<p> Implements <code>sc::OneBodyInt</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
