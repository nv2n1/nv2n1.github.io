---
title: "sc_spatialmopairiter_eq(3)"
name: "sc_spatialmopairiter_eq"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_spatialmopairiter_eq/"
description: "sc::SpatialMOPairIter_eq –"
---

<p>sc::SpatialMOPairIter_eq &#8211; </p>
<p> <code>SpatialMOPairIter_eq</code> gives the ordering of same-spin and different-spin orbital pairs if both orbitals of the pairs are from the same space.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;pairiter.h&gt;</code></pre>
<p> Inherits <code>sc::SpatialMOPairIter</code>.</p>
<h3>Public Member Functions</h3>
<p><code>SpatialMOPairIter_eq</code> (const <code>Ref</code>&lt; <code>MOIndexSpace</code> &gt; &amp;space1)<br />
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
<p><code>SpatialMOPairIter_eq</code> gives the ordering of same-spin and different-spin orbital pairs if both orbitals of the pairs are from the same space. </p>
<p> It iterates over all i &gt;= j combinations (total of (ni_+1)*(ni_+2)/2 pairs).</p>
<h2>Member Function Documentation</h2>
<h3>int sc::SpatialMOPairIter_eq::ij_aa () const [inline, virtual]</h3>
<p>Returns compound index ij for alpha-alpha case. The i == j combination doesn&#8217;t make sense, so <code>ij_aa()</code> will return -1 for such pairs. </p>
<p> Implements <code>sc::SpatialMOPairIter</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
