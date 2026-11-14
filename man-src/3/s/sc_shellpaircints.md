---
title: "sc_shellpaircints(3)"
name: "sc_shellpaircints"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_shellpaircints/"
description: "sc::ShellPairCints –"
---

<p>sc::ShellPairCints &#8211; </p>
<p> <code>ShellPairCints</code> provides all primitive pair data for a given shell pair.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;shellpairs.h&gt;</code></pre>
<p> Inherits <code>sc::SavableState</code>.</p>
<h3>Public Member Functions</h3>
<p><code>ShellPairCints</code> (<code>Ref</code>&lt; <code>PrimPairsCints</code> &gt; &amp;) </p>
<p> <code>ShellPairCints</code> (<code>StateIn</code> &amp;) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 void <code>init</code> (const int, const int) </p>
<p> <code>prim_pair_t</code> * <code>prim_pair</code> (int p1, int p2) const </p>
<p> double <code>prim_pair_P</code> (int p1, int p2, int xyz) const </p>
<p> double <code>prim_pair_gamma</code> (int p1, int p2) const </p>
<p> double <code>prim_pair_ovlp</code> (int p1, int p2) const</p>
<h3>Friends</h3>
<pre><code>void init_shell_pair (ShellPairsCints &amp;)</code></pre>
<h2>Detailed Description</h2>
<p><code>ShellPairCints</code> provides all primitive pair data for a given shell pair.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::ShellPairCints::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SavableState</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
