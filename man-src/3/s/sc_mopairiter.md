---
title: "sc_mopairiter(3)"
name: "sc_mopairiter"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_mopairiter/"
description: "sc::MOPairIter –"
---

<p>sc::MOPairIter &#8211; </p>
<p> <code>MOPairIter</code> gives the ordering of orbital pairs.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;pairiter.h&gt;</code></pre>
<p> Inherits <code>sc::RefCount</code>. Inherited by <code>sc::SpatialMOPairIter</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>MOPairIter (const Ref&lt; MOIndexSpace &gt; &amp;space_i, const Ref&lt; MOIndexSpace &gt; &amp;space_j)


Initialize an iterator for the given MO spaces.


virtual void start (const int first_ij=0)=0


Start the iteration.


virtual void next ()=0


Move to the next pair.


virtual operator int () const =0


Returns nonzero if the iterator currently hold valid data.


int ni () const


Returns the number of functions in space i.


int nj () const


Returns the number of functions in space j.


int i () const


Returns index i.


int j () const


Returns index j.


int nij () const


Returns the number of pair combinations for this iterator.


int ij () const


Returns the current iteration.



Protected Attributes</code></pre>
<p> bool <code>i_eq_j_</code> </p>
<p> int <code>ni_</code> </p>
<p> int <code>nj_</code> </p>
<p> int <code>i_</code> </p>
<p> int <code>j_</code> </p>
<p> int <code>nij_</code> </p>
<p> int <code>ij_</code></p>
<h2>Detailed Description</h2>
<p><code>MOPairIter</code> gives the ordering of orbital pairs.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
