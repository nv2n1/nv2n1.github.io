---
title: "sc_derivcenters(3)"
name: "sc_derivcenters"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_derivcenters/"
description: "sc::DerivCenters –"
---

<p>sc::DerivCenters &#8211; </p>
<p> <code>DerivCenters</code> keeps track the centers that derivatives are taken with respect to.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;dercent.h&gt;

Public Member Functions</code></pre>
<p> <code>DerivCenters</code> ()<br />
 <i>Construct a new, empty </i><code>DerivCenters</code> object. <code>Routines to Modify DerivCenters</code> </p>
<p>&nbsp;<wbr><br />
 void <code>clear</code> ()<br />
 <i>Clear the list of centers. </i><br />
 void <code>add_center</code> (int center, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;bs, int shell)<br />
 <i>Add a center using a basis set and the shell number. </i><br />
 void <code>add_center</code> (int center, int atom)<br />
 <i>Add a center using the atom number. </i><br />
 void <code>add_omitted</code> (int center, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;bs, int shell)<br />
 <i>Add the omitted center using a basis set and the shell number. </i><br />
 void <code>add_omitted</code> (int center, int atom)<br />
 <i>Add the omitted center using the atom number. </i> <code>Routines to Query DerivCenters</code> </p>
<p>&nbsp;<wbr> </p>
<pre><code>int n () const


The number of centers for which derivatives have been computed.


int center (int i) const



int atom (int i) const



int has_omitted_center () const



int omitted_center () const



int omitted_atom () const</code></pre>
<h2>Detailed Description</h2>
<p><code>DerivCenters</code> keeps track the centers that derivatives are taken with respect to.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::DerivCenters::add_center (int center, int atom)</h3>
<p>Add a center using the atom number. <code>Parameters:</code></p>
<dl>
<dd><i>center</i> The center number (between 0 and 3 inclusive).<br />
 <i>atom</i> The center within a <code>GaussianBasisSet</code>.</dl>
<h3>void sc::DerivCenters::add_center (int center, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp; bs, int shell)</h3>
<p>Add a center using a basis set and the shell number. <code>Parameters:</code></p>
<dl>
<dd><i>center</i> The center number (between 0 and 3 inclusive).<br />
 <i>bs</i> The basis set for this center.<br />
 <i>shell</i> The shell number for this center.</dl>
<h3>void sc::DerivCenters::add_omitted (int center, int atom)</h3>
<p>Add the omitted center using the atom number. <code>Parameters:</code></p>
<dl>
<dd><i>center</i> The center number (between 0 and 3 inclusive).<br />
 <i>atom</i> The center within a <code>GaussianBasisSet</code>.</dl>
<h3>void sc::DerivCenters::add_omitted (int center, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp; bs, int shell)</h3>
<p>Add the omitted center using a basis set and the shell number. <code>Parameters:</code></p>
<dl>
<dd><i>center</i> The center number (between 0 and 3 inclusive).<br />
 <i>bs</i> The basis set for this center.<br />
 <i>shell</i> The shell number for this center.</dl>
<h3>int sc::DerivCenters::atom (int i) const [inline]<code>Parameters:</code></h3>
<dl>
<dd><i>i</i> The computed center index (between 0 and <code>n()</code> &#8211; 1, inclusive).</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The atom number.</dl>
<p> Referenced by sc::LocalTBGrad&lt; T &gt;::run().</p>
<h3>int sc::DerivCenters::center (int i) const [inline]<code>Parameters:</code></h3>
<dl>
<dd><i>i</i> The computed center index (between 0 and <code>n()</code> &#8211; 1, inclusive).</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The center number (between 0 and 3, inclusive).</dl>
<h3>int sc::DerivCenters::has_omitted_center () const [inline]<code>Returns:</code></h3>
<dl>
<dd>1 if there is an omitted center, otherwise 0.</dl>
<h3>int sc::DerivCenters::omitted_atom () const [inline]<code>Returns:</code></h3>
<dl>
<dd>The atom that is omitted from the integral buffer.</dl>
<p> Referenced by sc::LocalTBGrad&lt; T &gt;::run().</p>
<h3>int sc::DerivCenters::omitted_center () const [inline]<code>Returns:</code></h3>
<dl>
<dd>The center for which integrals where not computed.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
