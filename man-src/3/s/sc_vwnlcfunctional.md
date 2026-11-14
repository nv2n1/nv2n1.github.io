---
title: "sc_vwnlcfunctional(3)"
name: "sc_vwnlcfunctional"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_vwnlcfunctional/"
description: "sc::VWNLCFunctional –"
---

<p>sc::VWNLCFunctional &#8211; </p>
<p> An abstract base class from which the various VWN (Vosko, Wilk and Nusair) local correlation functional (1, 2, 3, 4, 5) classes are derived.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;functional.h&gt;</code></pre>
<p> Inherits <code>sc::LSDACFunctional</code>. Inherited by <code>sc::VWN1LCFunctional</code>, <code>sc::VWN2LCFunctional</code>, <code>sc::VWN3LCFunctional</code>, <code>sc::VWN4LCFunctional</code>, and <code>sc::VWN5LCFunctional</code>.</p>
<h3>Public Member Functions</h3>
<p><code>VWNLCFunctional</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;) </p>
<p> <code>VWNLCFunctional</code> (<code>StateIn</code> &amp;) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 virtual void <code>point_lc</code> (const <code>PointInputData</code> &amp;, <code>PointOutputData</code> &amp;, double &amp;, double &amp;, double &amp;)</p>
<h3>Protected Member Functions</h3>
<pre><code>void init_constants ()



double F (double x, double A, double x0, double b, double c)



double dFdr_s (double x, double A, double x0, double b, double c)



Protected Attributes
double Ap_



double Af_



double A_alpha_



double x0p_mc_



double bp_mc_



double cp_mc_



double x0f_mc_



double bf_mc_



double cf_mc_



double x0p_rpa_



double bp_rpa_



double cp_rpa_



double x0f_rpa_



double bf_rpa_



double cf_rpa_



double x0_alpha_mc_



double b_alpha_mc_



double c_alpha_mc_



double x0_alpha_rpa_



double b_alpha_rpa_



double c_alpha_rpa_</code></pre>
<h2>Detailed Description</h2>
<p>An abstract base class from which the various VWN (Vosko, Wilk and Nusair) local correlation functional (1, 2, 3, 4, 5) classes are derived. </p>
<p> S. H. Vosko, L. Wilk, and M. Nusair, Can. J. Phys., 58, pp. 1200-1211, 1980.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::VWNLCFunctional::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::LSDACFunctional</code>. </p>
<p> Reimplemented in <code>sc::VWN1LCFunctional</code>, <code>sc::VWN2LCFunctional</code>, <code>sc::VWN3LCFunctional</code>, <code>sc::VWN4LCFunctional</code>, and <code>sc::VWN5LCFunctional</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
