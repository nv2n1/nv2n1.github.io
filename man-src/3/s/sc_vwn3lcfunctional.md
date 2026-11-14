---
title: "sc_vwn3lcfunctional(3)"
name: "sc_vwn3lcfunctional"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_vwn3lcfunctional/"
description: "sc::VWN3LCFunctional –"
---

<p>sc::VWN3LCFunctional &#8211; </p>
<p> The <code>VWN3LCFunctional</code> computes energies and densities using the VWN3 local correlation term (from Vosko, Wilk, and Nusair).</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;functional.h&gt;</code></pre>
<p> Inherits <code>sc::VWNLCFunctional</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>VWN3LCFunctional (int mcp=1, int mce0=1)



VWN3LCFunctional (const Ref&lt; KeyVal &gt; &amp;)



VWN3LCFunctional (StateIn &amp;)



void save_data_state (StateOut &amp;)


Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.


void point_lc (const PointInputData &amp;, PointOutputData &amp;, double &amp;, double &amp;, double &amp;)



Protected Attributes
int monte_carlo_prefactor_



int monte_carlo_e0_</code></pre>
<h2>Detailed Description</h2>
<p>The <code>VWN3LCFunctional</code> computes energies and densities using the VWN3 local correlation term (from Vosko, Wilk, and Nusair).</p>
<h2>Member Function Documentation</h2>
<h3>void sc::VWN3LCFunctional::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::VWNLCFunctional</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
