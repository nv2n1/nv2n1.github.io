---
title: "sc_orbital(3)"
name: "sc_orbital"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_orbital/"
description: "sc::Orbital –"
---

<p>sc::Orbital &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::Volume</code>.</p>
<h3>Public Member Functions</h3>
<p><code>Orbital</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;) </p>
<p> <code>Orbital</code> (const <code>Ref</code>&lt; <code>OneBodyWavefunction</code> &gt; &amp;, int orbital) </p>
<p> virtual void <code>boundingbox</code> (double valuemin, double valuemax, <code>SCVector3</code> &amp;p1, <code>SCVector3</code> &amp;p2)</p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>compute</code> ()<br />
 <i>Recompute at least the results that have compute true and are not already computed. </i></p>
<h3>Protected Attributes</h3>
<p><code>Ref</code>&lt; <code>OneBodyWavefunction</code> &gt; <code>wfn_</code> </p>
<p> int <code>orbital_</code></p>
<h2>Member Function Documentation</h2>
<h3>virtual void sc::Orbital::compute () [protected, virtual]</h3>
<p>Recompute at least the results that have compute true and are not already computed. This should only be called by Result&#8217;s members. </p>
<p> Implements <code>sc::Volume</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
