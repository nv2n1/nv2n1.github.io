---
title: "sc_dfpupdate(3)"
name: "sc_dfpupdate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_dfpupdate/"
description: "sc::DFPUpdate –"
---

<p>sc::DFPUpdate &#8211; </p>
<p> The <code>DFPUpdate</code> class is used to specify a Davidson, Fletcher, and Powell hessian update scheme.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;update.h&gt;</code></pre>
<p> Inherits <code>sc::HessianUpdate</code>. Inherited by <code>sc::BFGSUpdate</code>.</p>
<h3>Public Member Functions</h3>
<p><code>DFPUpdate</code> (<code>StateIn</code> &amp;) </p>
<p> <code>DFPUpdate</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)<br />
 <i>The </i><code>KeyVal</code> constructor reads the following keywords:.<br />
 void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 void <code>update</code> (const <code>RefSymmSCMatrix</code> &amp;ihessian, const <code>Ref</code>&lt; <code>Function</code> &gt; &amp;, const <code>RefSCVector</code> &amp;xnew, const <code>RefSCVector</code> &amp;gnew) </p>
<p> void <code>apply_transform</code> (const <code>Ref</code>&lt; <code>NonlinearTransform</code> &gt; &amp;) </p>
<p> void <code>set_inverse</code> ()</p>
<h3>Protected Attributes</h3>
<p><code>RefSCVector</code> <code>xprev</code> </p>
<p> <code>RefSCVector</code> <code>gprev</code></p>
<h2>Detailed Description</h2>
<p>The <code>DFPUpdate</code> class is used to specify a Davidson, Fletcher, and Powell hessian update scheme.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::DFPUpdate::DFPUpdate (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p>The <code>KeyVal</code> constructor reads the following keywords:. .IP &quot;xprev&quot; 1c The previous coordinates can be given (but is not recommended). The default is none. </p>
<dl>
<dt>gprev</p>
<dd>The previous gradient can be given (but is not recommended). The default is none.</dl>
<h2>Member Function Documentation</h2>
<h3>void sc::DFPUpdate::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::HessianUpdate</code>. </p>
<p> Reimplemented in <code>sc::BFGSUpdate</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
