---
title: "sc_r12amplitudes(3)"
name: "sc_r12amplitudes"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_r12amplitudes/"
description: "sc::R12Amplitudes –"
---

<p>sc::R12Amplitudes &#8211; </p>
<p> <code>R12Amplitudes</code> gives the amplitudes of some linear-R12-ansatz-related terms in wave function.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;r12_amps.h&gt;</code></pre>
<p> Inherits <code>sc::RefCount</code>.</p>
<h3>Public Member Functions</h3>
<p><code>R12Amplitudes</code> (const <code>RefSCMatrix</code> &amp;T2_aa, const <code>RefSCMatrix</code> &amp;T2_ab, const <code>RefSCMatrix</code> &amp;Rvv_aa, const <code>RefSCMatrix</code> &amp;Rvv_ab, const <code>RefSCMatrix</code> &amp;Roo_aa, const <code>RefSCMatrix</code> &amp;Roo_ab, const <code>RefSCMatrix</code> &amp;Rvo_aa, const <code>RefSCMatrix</code> &amp;Rvo_ab, const <code>RefSCMatrix</code> &amp;Rxo_aa, const <code>RefSCMatrix</code> &amp;Rxo_ab) </p>
<p> const <code>RefSCMatrix</code> <code>T2_aa</code> () const </p>
<p> const <code>RefSCMatrix</code> <code>T2_ab</code> () const </p>
<p> const <code>RefSCMatrix</code> <code>Rvv_aa</code> () const </p>
<p> const <code>RefSCMatrix</code> <code>Rvv_ab</code> () const </p>
<p> const <code>RefSCMatrix</code> <code>Roo_aa</code> () const </p>
<p> const <code>RefSCMatrix</code> <code>Roo_ab</code> () const </p>
<p> const <code>RefSCMatrix</code> <code>Rvo_aa</code> () const </p>
<p> const <code>RefSCMatrix</code> <code>Rvo_ab</code> () const </p>
<p> const <code>RefSCMatrix</code> <code>Rxo_aa</code> () const </p>
<p> const <code>RefSCMatrix</code> <code>Rxo_ab</code> () const</p>
<h2>Detailed Description</h2>
<p><code>R12Amplitudes</code> gives the amplitudes of some linear-R12-ansatz-related terms in wave function. </p>
<p> The first-order wave function terms which result from linear R12 terms are: Fij (1) = Ckl ij ( r12 |kl&gt; &#8211; 0.5 rab kl |ab&gt; &#8211; 0.5 rmn kl |mn&gt; &#8211; ram kl |am&gt; &#8211; ra&#8217;m kl |a&#8217;m&gt; ) where C are optimal first-order coefficients and r are antisymmetrized integrals over r12 operator. Indices a, b are virtual MOs; m,n are occupied MOs; i, j, k, l are active occupied MOs, a&#8217; is an RI basis index.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
