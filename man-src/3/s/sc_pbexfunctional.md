---
title: "sc_pbexfunctional(3)"
name: "sc_pbexfunctional"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_pbexfunctional/"
description: "sc::PBEXFunctional –"
---

<p>sc::PBEXFunctional &#8211; </p>
<p> Implements the Perdew-Burke-Ernzerhof (PBE) exchange functional.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;functional.h&gt;</code></pre>
<p> Inherits <code>sc::DenFunctional</code>.</p>
<h3>Public Member Functions</h3>
<p><code>PBEXFunctional</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;) </p>
<p> <code>PBEXFunctional</code> (<code>StateIn</code> &amp;) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 int <code>need_density_gradient</code> () </p>
<p> void <code>point</code> (const <code>PointInputData</code> &amp;, <code>PointOutputData</code> &amp;)</p>
<h3>Protected Member Functions</h3>
<pre><code>void spin_contrib (const PointInputData::SpinData &amp;, double &amp;mpw, double &amp;dmpw_dr, double &amp;dmpw_dg)



void init_constants ()



Protected Attributes
double mu



double kappa</code></pre>
<h2>Detailed Description</h2>
<p>Implements the Perdew-Burke-Ernzerhof (PBE) exchange functional. </p>
<p> John P. Perdew, Kieron Burke, and Yue Wang, Phys. Rev. B, 54(23), pp. 16533-16539, 1996. </p>
<p> John P. Perdew, Kieron Burke, and Matthias Ernzerhof, Phys. Rev. Lett., 77(18), pp. 3865-3868 1996. </p>
<p> See also the comment and reply discussing the revPBE modification which adjusts the value of kappa: </p>
<p> Yingkai Zhang and Weitao Yang, Phys. Rev. Lett., <a href="/docs/linux/man/4-80/">80</a>(4), pp. 890, 1998. </p>
<p> John P. Perdew, Kieron Burke, and Matthias Ernzerhof, Phys. Rev. Lett., <a href="/docs/linux/man/4-80/">80</a>(4), pp. 891, 1998.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::PBEXFunctional::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::DenFunctional</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
