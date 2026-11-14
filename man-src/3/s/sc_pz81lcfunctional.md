---
title: "sc_pz81lcfunctional(3)"
name: "sc_pz81lcfunctional"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_pz81lcfunctional/"
description: "sc::PZ81LCFunctional –"
---

<p>sc::PZ81LCFunctional &#8211; </p>
<p> Implements the PZ81 local (LSDA) correlation functional.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;functional.h&gt;</code></pre>
<p> Inherits <code>sc::LSDACFunctional</code>.</p>
<h3>Public Member Functions</h3>
<p><code>PZ81LCFunctional</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;) </p>
<p> <code>PZ81LCFunctional</code> (<code>StateIn</code> &amp;) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 void <code>point_lc</code> (const <code>PointInputData</code> &amp;, <code>PointOutputData</code> &amp;, double &amp;, double &amp;, double &amp;)</p>
<h3>Protected Member Functions</h3>
<pre><code>double Fec_rsgt1 (double rs, double beta_1, double beta_2, double gamma)



double dFec_rsgt1_drho (double rs, double beta_1, double beta_2, double gamma, double &amp;dec_drs)



double Fec_rslt1 (double rs, double A, double B, double C, double D)



double dFec_rslt1_drho (double rs, double A, double B, double C, double D, double &amp;dec_drs)</code></pre>
<h2>Detailed Description</h2>
<p>Implements the PZ81 local (LSDA) correlation functional. </p>
<p> This local correlation functional is used in P86. </p>
<p> J. P. Perdew and A. Zunger, Phys. Rev. B, 23, pp. 5048-5079, 1981.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::PZ81LCFunctional::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::LSDACFunctional</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
