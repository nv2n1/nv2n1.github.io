---
title: "sc_bfgsupdate(3)"
name: "sc_bfgsupdate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_bfgsupdate/"
description: "sc::BFGSUpdate –"
---

<p>sc::BFGSUpdate &#8211; </p>
<p> The <code>DFPUpdate</code> class is used to specify a Broyden, Fletcher, Goldfarb, and Shanno hessian update scheme.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;update.h&gt;</code></pre>
<p> Inherits <code>sc::DFPUpdate</code>.</p>
<h3>Public Member Functions</h3>
<p><code>BFGSUpdate</code> (<code>StateIn</code> &amp;) </p>
<p> <code>BFGSUpdate</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 void <code>update</code> (const <code>RefSymmSCMatrix</code> &amp;ihessian, const <code>Ref</code>&lt; <code>Function</code> &gt; &amp;, const <code>RefSCVector</code> &amp;xnew, const <code>RefSCVector</code> &amp;gnew)</p>
<h2>Detailed Description</h2>
<p>The <code>DFPUpdate</code> class is used to specify a Broyden, Fletcher, Goldfarb, and Shanno hessian update scheme. </p>
<p> This hessian update method is the recommended method for use with <code>QNewtonOpt</code> objects.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::BFGSUpdate::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::DFPUpdate</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
