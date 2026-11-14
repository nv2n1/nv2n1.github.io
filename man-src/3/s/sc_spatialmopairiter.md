---
title: "sc_spatialmopairiter(3)"
name: "sc_spatialmopairiter"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_spatialmopairiter/"
description: "sc::SpatialMOPairIter –"
---

<p>sc::SpatialMOPairIter &#8211; </p>
<p> <code>SpatialMOPairIter</code> gives the ordering of pairs of spatial orbitals.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;pairiter.h&gt;</code></pre>
<p> Inherits <code>sc::MOPairIter</code>. Inherited by <code>sc::SpatialMOPairIter_eq</code>, and <code>sc::SpatialMOPairIter_neq</code>.</p>
<h3>Public Member Functions</h3>
<p><code>SpatialMOPairIter</code> (const <code>Ref</code>&lt; <code>MOIndexSpace</code> &gt; &amp;space_i, const <code>Ref</code>&lt; <code>MOIndexSpace</code> &gt; &amp;space_j)<br />
 <i>Initialize a spatial pair iterator for the given MO spaces. </i><br />
 virtual int <code>nij_aa</code> () const =0<br />
 <i>Returns the number of functions in alpha-alpha space. </i><br />
 virtual int <code>nij_ab</code> () const =0<br />
 <i>Returns the number of functions in alpha-beta space. </i><br />
 virtual int <code>ij_aa</code> () const =0<br />
 <i>Returns compound index ij for alpha-alpha case. </i><br />
 virtual int <code>ij_ab</code> () const =0<br />
 <i>Returns compound index ij for alpha-beta case. </i><br />
 virtual int <code>ij_ba</code> () const =0<br />
 <i>Returns compound index ij for beta-alpha case. </i></p>
<h2>Detailed Description</h2>
<p><code>SpatialMOPairIter</code> gives the ordering of pairs of spatial orbitals. </p>
<p> Different spin cases appear.</p>
<h2>Member Function Documentation</h2>
<h3>virtual int sc::SpatialMOPairIter::ij_aa () const [pure virtual]</h3>
<p>Returns compound index ij for alpha-alpha case. If the combintaion is not allowed then return -1 </p>
<p> Implemented in <code>sc::SpatialMOPairIter_eq</code>, and <code>sc::SpatialMOPairIter_neq</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
