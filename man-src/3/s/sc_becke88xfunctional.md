---
title: "sc_becke88xfunctional(3)"
name: "sc_becke88xfunctional"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_becke88xfunctional/"
description: "sc::Becke88XFunctional –"
---

<p>sc::Becke88XFunctional &#8211; </p>
<p> Implements Becke&#8217;s 1988 exchange functional.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;functional.h&gt;</code></pre>
<p> Inherits <code>sc::DenFunctional</code>.</p>
<h3>Public Member Functions</h3>
<p><code>Becke88XFunctional</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;) </p>
<p> <code>Becke88XFunctional</code> (<code>StateIn</code> &amp;) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 int <code>need_density_gradient</code> () </p>
<p> void <code>point</code> (const <code>PointInputData</code> &amp;, <code>PointOutputData</code> &amp;)</p>
<h3>Protected Attributes</h3>
<pre><code>double beta_



double beta6_</code></pre>
<h2>Detailed Description</h2>
<p>Implements Becke&#8217;s 1988 exchange functional. </p>
<p> A. D. Becke, Phys. Rev. A, <a href="/docs/linux/man/6-38/">38</a>(6), pp. 3098-3100, 1988.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::Becke88XFunctional::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::DenFunctional</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
