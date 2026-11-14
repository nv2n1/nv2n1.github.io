---
title: "sc_shellpairscints(3)"
name: "sc_shellpairscints"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_shellpairscints/"
description: "sc::ShellPairsCints –"
---

<p>sc::ShellPairsCints &#8211; </p>
<p> <code>ShellPairsCints</code> contains primitive pair data for all shell pairs.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;shellpairs.h&gt;</code></pre>
<p> Inherits <code>sc::SavableState</code>.</p>
<h3>Public Member Functions</h3>
<p><code>ShellPairsCints</code> (const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;) </p>
<p> <code>ShellPairsCints</code> (const <code>Ref</code>&lt; <code>ShellPairsCints</code> &gt; &amp;) </p>
<p> <code>ShellPairsCints</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;) </p>
<p> <code>ShellPairsCints</code> (<code>StateIn</code> &amp;) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 <code>ShellPairCints</code> * <code>shell_pair</code> (int si, int sj) const</p>
<h3>Friends</h3>
<pre><code>void init_shell_pair (ShellPairsCints &amp;)</code></pre>
<h2>Detailed Description</h2>
<p><code>ShellPairsCints</code> contains primitive pair data for all shell pairs.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::ShellPairsCints::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SavableState</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
