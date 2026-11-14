---
title: "sc_g96xfunctional(3)"
name: "sc_g96xfunctional"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_g96xfunctional/"
description: "sc::G96XFunctional –"
---

<p>sc::G96XFunctional &#8211; </p>
<p> Implements the Gill 1996 (G96) exchange functional.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;functional.h&gt;</code></pre>
<p> Inherits <code>sc::DenFunctional</code>.</p>
<h3>Public Member Functions</h3>
<p><code>G96XFunctional</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;) </p>
<p> <code>G96XFunctional</code> (<code>StateIn</code> &amp;) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 int <code>need_density_gradient</code> () </p>
<p> void <code>point</code> (const <code>PointInputData</code> &amp;, <code>PointOutputData</code> &amp;)</p>
<h3>Protected Member Functions</h3>
<pre><code>void init_constants ()



Protected Attributes
double b_</code></pre>
<h2>Detailed Description</h2>
<p>Implements the Gill 1996 (G96) exchange functional. </p>
<p> P. M. W. Gill, Mol. Phys., <a href="/docs/linux/man/2-89/">89</a>(2), pp. 433-445, 1996.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::G96XFunctional::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::DenFunctional</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
