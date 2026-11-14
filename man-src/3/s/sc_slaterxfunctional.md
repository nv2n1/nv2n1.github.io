---
title: "sc_slaterxfunctional(3)"
name: "sc_slaterxfunctional"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_slaterxfunctional/"
description: "sc::SlaterXFunctional –"
---

<p>sc::SlaterXFunctional &#8211; </p>
<p> Implements the Slater exchange functional.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;functional.h&gt;</code></pre>
<p> Inherits <code>sc::DenFunctional</code>.</p>
<h3>Public Member Functions</h3>
<p><code>SlaterXFunctional</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;) </p>
<p> <code>SlaterXFunctional</code> (<code>StateIn</code> &amp;) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 void <code>point</code> (const <code>PointInputData</code> &amp;, <code>PointOutputData</code> &amp;)</p>
<h2>Detailed Description</h2>
<p>Implements the Slater exchange functional.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::SlaterXFunctional::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::DenFunctional</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
