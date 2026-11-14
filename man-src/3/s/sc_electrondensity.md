---
title: "sc_electrondensity(3)"
name: "sc_electrondensity"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_electrondensity/"
description: "sc::ElectronDensity –"
---

<p>sc::ElectronDensity &#8211; </p>
<p> This is a <code>Volume</code> that computer the electron density.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;density.h&gt;</code></pre>
<p> Inherits <code>sc::Volume</code>.</p>
<h3>Public Member Functions</h3>
<p><code>ElectronDensity</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;) </p>
<p> <code>ElectronDensity</code> (const <code>Ref</code>&lt; <code>Wavefunction</code> &gt; &amp;) </p>
<p> virtual void <code>boundingbox</code> (double valuemin, double valuemax, <code>SCVector3</code> &amp;p1, <code>SCVector3</code> &amp;p2)</p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>compute</code> ()<br />
 <i>Recompute at least the results that have compute true and are not already computed. </i></p>
<h3>Protected Attributes</h3>
<p><code>Ref</code>&lt; <code>Wavefunction</code> &gt; <code>wfn_</code></p>
<h2>Detailed Description</h2>
<p>This is a <code>Volume</code> that computer the electron density. </p>
<p> It can be used to generate isodensity surfaces.</p>
<h2>Member Function Documentation</h2>
<h3>virtual void sc::ElectronDensity::compute () [protected, virtual]</h3>
<p>Recompute at least the results that have compute true and are not already computed. This should only be called by Result&#8217;s members. </p>
<p> Implements <code>sc::Volume</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
