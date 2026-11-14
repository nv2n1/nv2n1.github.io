---
title: "sc_spatialmopairiter_neq(3)"
name: "sc_spatialmopairiter_neq"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_spatialmopairiter_neq/"
description: "sc::SpatialMOPairIter_neq –"
---

<p>sc::SpatialMOPairIter_neq &#8211; </p>
<p> <code>SpatialMOPairIter_neq</code> gives the ordering of pairs of spatial orbitals from different spaces.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;pairiter.h&gt;</code></pre>
<p> Inherits <code>sc::SpatialMOPairIter</code>.</p>
<h3>Public Member Functions</h3>
<p><code>SpatialMOPairIter_neq</code> (const <code>Ref</code>&lt; <code>MOIndexSpace</code> &gt; &amp;space1, const <code>Ref</code>&lt; <code>MOIndexSpace</code> &gt; &amp;space2)<br />
 <i>Initialize an iterator for the given MO spaces. </i><br />
 void <code>start</code> (const int ij_offset=0)<br />
 <i>Initialize the iterator assuming that iteration will start with pair ij_offset. </i><br />
 void <code>next</code> ()<br />
 <i>Move to the next pair. </i><br />
 <code>operator int</code> () const<br />
 <i>Returns nonzero if the iterator currently hold valid data. </i><br />
 int <code>nij_aa</code> () const<br />
 <i>Returns the number of functions in alpha-alpha space. </i><br />
 int <code>nij_ab</code> () const<br />
 <i>Returns the number of functions in alpha-beta space. </i><br />
 int <code>ij_aa</code> () const<br />
 <i>Returns compound index ij for alpha-alpha case. </i><br />
 int <code>ij_ab</code> () const<br />
 <i>Returns compound index ij for alpha-beta case. </i><br />
 int <code>ij_ba</code> () const<br />
 <i>Returns compound index ij for beta-alpha case. </i></p>
<h2>Detailed Description</h2>
<p><code>SpatialMOPairIter_neq</code> gives the ordering of pairs of spatial orbitals from different spaces. </p>
<p> It iterates over all ij combinations (total of ni_*nj_ pairs).</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
