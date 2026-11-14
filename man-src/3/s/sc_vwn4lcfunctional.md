---
title: "sc_vwn4lcfunctional(3)"
name: "sc_vwn4lcfunctional"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_vwn4lcfunctional/"
description: "sc::VWN4LCFunctional –"
---

<p>sc::VWN4LCFunctional &#8211; </p>
<p> The <code>VWN4LCFunctional</code> computes energies and densities using the VWN4 local correlation term (from Vosko, Wilk, and Nusair).</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;functional.h&gt;</code></pre>
<p> Inherits <code>sc::VWNLCFunctional</code>.</p>
<h3>Public Member Functions</h3>
<p><code>VWN4LCFunctional</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;) </p>
<p> <code>VWN4LCFunctional</code> (<code>StateIn</code> &amp;) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 void <code>point_lc</code> (const <code>PointInputData</code> &amp;, <code>PointOutputData</code> &amp;, double &amp;, double &amp;, double &amp;)</p>
<h3>Protected Attributes</h3>
<pre><code>int monte_carlo_prefactor_</code></pre>
<h2>Detailed Description</h2>
<p>The <code>VWN4LCFunctional</code> computes energies and densities using the VWN4 local correlation term (from Vosko, Wilk, and Nusair).</p>
<h2>Member Function Documentation</h2>
<h3>void sc::VWN4LCFunctional::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::VWNLCFunctional</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
