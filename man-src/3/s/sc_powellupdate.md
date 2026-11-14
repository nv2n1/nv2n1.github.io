---
title: "sc_powellupdate(3)"
name: "sc_powellupdate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_powellupdate/"
description: "sc::PowellUpdate –"
---

<p>sc::PowellUpdate &#8211; </p>
<p> The <code>PowellUpdate</code> class is used to specify a Powell hessian update.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;update.h&gt;</code></pre>
<p> Inherits <code>sc::HessianUpdate</code>.</p>
<h3>Public Member Functions</h3>
<p><code>PowellUpdate</code> (<code>StateIn</code> &amp;) </p>
<p> <code>PowellUpdate</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 void <code>update</code> (const <code>RefSymmSCMatrix</code> &amp;ihessian, const <code>Ref</code>&lt; <code>Function</code> &gt; &amp;func, const <code>RefSCVector</code> &amp;xnew, const <code>RefSCVector</code> &amp;gnew) </p>
<p> void <code>apply_transform</code> (const <code>Ref</code>&lt; <code>NonlinearTransform</code> &gt; &amp;)</p>
<h3>Protected Attributes</h3>
<p><code>RefSCVector</code> <code>xprev</code> </p>
<p> <code>RefSCVector</code> <code>gprev</code></p>
<h2>Detailed Description</h2>
<p>The <code>PowellUpdate</code> class is used to specify a Powell hessian update. </p>
<p> This hessian update method is the recommended method for use with transition state searches (the <code>EFCOpt</code> class can be used for transition state searches).</p>
<h2>Member Function Documentation</h2>
<h3>void sc::PowellUpdate::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::HessianUpdate</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
