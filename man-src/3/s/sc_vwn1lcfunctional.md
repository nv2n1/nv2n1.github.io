---
title: "sc_vwn1lcfunctional(3)"
name: "sc_vwn1lcfunctional"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_vwn1lcfunctional/"
description: "sc::VWN1LCFunctional –"
---

<p>sc::VWN1LCFunctional &#8211; </p>
<p> The <code>VWN1LCFunctional</code> computes energies and densities using the VWN1 local correlation term (from Vosko, Wilk, and Nusair).</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;functional.h&gt;</code></pre>
<p> Inherits <code>sc::VWNLCFunctional</code>.</p>
<h3>Public Member Functions</h3>
<p><code>VWN1LCFunctional</code> ()<br />
 <i>Construct a VWN1 functional using Monte-Carlo parameters. </i><br />
 <code>VWN1LCFunctional</code> (int use_rpa)<br />
 <i>Construct a VWN1 functional using the RPA parameters. </i><br />
 <code>VWN1LCFunctional</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)<br />
 <i>Construct a VWN1 functional using the Monte-Carlo parameters by default. </i><br />
 <code>VWN1LCFunctional</code> (<code>StateIn</code> &amp;) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 void <code>point_lc</code> (const <code>PointInputData</code> &amp;, <code>PointOutputData</code> &amp;, double &amp;, double &amp;, double &amp;)</p>
<h3>Protected Attributes</h3>
<pre><code>double x0p_



double bp_



double cp_



double x0f_



double bf_



double cf_</code></pre>
<h2>Detailed Description</h2>
<p>The <code>VWN1LCFunctional</code> computes energies and densities using the VWN1 local correlation term (from Vosko, Wilk, and Nusair).</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::VWN1LCFunctional::VWN1LCFunctional (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p>Construct a VWN1 functional using the Monte-Carlo parameters by default. If rpa is set to true, then load the RPA paramenters. Furthermore, each value can be overridden by assigning to x0p, bp, cp, x0f, bf, and/or cf.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::VWN1LCFunctional::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::VWNLCFunctional</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
