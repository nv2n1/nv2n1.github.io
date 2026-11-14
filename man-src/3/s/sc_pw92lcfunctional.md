---
title: "sc_pw92lcfunctional(3)"
name: "sc_pw92lcfunctional"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_pw92lcfunctional/"
description: "sc::PW92LCFunctional –"
---

<p>sc::PW92LCFunctional &#8211; </p>
<p> Implements the PW92 local (LSDA) correlation term.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;functional.h&gt;</code></pre>
<p> Inherits <code>sc::LSDACFunctional</code>.</p>
<h3>Public Member Functions</h3>
<p><code>PW92LCFunctional</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;) </p>
<p> <code>PW92LCFunctional</code> (<code>StateIn</code> &amp;) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 void <code>point_lc</code> (const <code>PointInputData</code> &amp;, <code>PointOutputData</code> &amp;, double &amp;, double &amp;, double &amp;)</p>
<h3>Protected Member Functions</h3>
<pre><code>double F (double x, double A, double alpha_1, double beta_1, double beta_2, double beta_3, double beta_4, double p)



double dFdr_s (double x, double A, double alpha_1, double beta_1, double beta_2, double beta_3, double beta_4, double p)</code></pre>
<h2>Detailed Description</h2>
<p>Implements the PW92 local (LSDA) correlation term. </p>
<p> This local correlation functional is used in PW91 and PBE. </p>
<p> J. P. Perdew and <code>Y</code>. Wang. Phys. Rev. B, 45, 13244, 1992.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::PW92LCFunctional::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::LSDACFunctional</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
